#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""悬浮球问答的本地代理（仅用于 demo，不上线）。

存在的理由只有一个：**API key 绝不能进浏览器**。站是 GitHub Pages 纯静态，
一旦把 key 写进前端，任何人 view-source 就能拿走当免费 API 用。
所以本地 demo 也照线上的形状来：浏览器 → 这个代理 → 模型厂商。
上线时把同样的逻辑搬进 Cloudflare Worker（仓库里已有 worker.js 那套白名单骨架）。

用法：
    export HW_CHAT_KEY=sk-xxx                  # DeepSeek 或硅基流动的 key
    export HW_CHAT_BASE=https://api.deepseek.com/chat/completions   # 可选
    export HW_CHAT_MODEL=deepseek-chat                              # 可选
    python3 scripts/chat_dev_proxy.py

不设 HW_CHAT_KEY 时进入 stub 模式：不调任何外部服务，返回一段拼接好的假答案，
用来先看交互和排版。

限流：按 IP 每天 5 次，记在内存里。前端那份 localStorage 计数只是提示，
改一行就能绕过——真正的闸门必须在这一层。
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import time
import urllib.request
from collections import defaultdict
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = int(os.environ.get("HW_CHAT_PORT", "8787"))
KEY = os.environ.get("HW_CHAT_KEY", "").strip()
BASE = os.environ.get("HW_CHAT_BASE", "https://api.deepseek.com/chat/completions")
# 默认 DeepSeek-V3.2：2026-09-01 在硅基上同题三轮实测，它在三项上同时最好——
# 中位 10.0s（V4-Flash 16.2 / V4-Pro 26.8）、token 中位 918（1671 / 2089）、
# 引用位置正确 14/15（10/11 / 12/16）。token 少一半直接等于额度翻倍。
MODEL = os.environ.get("HW_CHAT_MODEL", "deepseek-ai/DeepSeek-V3.2")
BASE_DEFAULT_NOTE = "硅基流动：https://api.siliconflow.cn/v1/chat/completions"
DAILY = int(os.environ.get("HW_CHAT_DAILY", "5"))
ALLOWED = {"http://localhost:8899", "http://127.0.0.1:8899"}

_hits = defaultdict(list)


def allowed(ip):
    now = time.time()
    _hits[ip] = [t for t in _hits[ip] if now - t < 86400]
    return len(_hits[ip]) < DAILY


# 提示词**从 worker/chat.js 里读**，不在这里抄第二份。
# 这个文件开头一直写着「改 prompt 两边都要改，否则线上线下答案不一致」——
# 靠人记住是不牢的，加英文那份的时候就正好会漏掉一边。改成读同一个源，
# 这条规矩就不需要人去守了。
def _prompts():
    src = os.path.join(ROOT, "worker", "chat.js")
    t = io.open(src, encoding="utf-8").read()
    out = {}
    for name, key in (("SYSTEM", "zh"), ("SYSTEM_EN", "en")):
        m = re.search(r"const %s = `(.*?)`;" % name, t, re.S)
        if m:
            out[key] = m.group(1)
    if "zh" not in out:
        raise SystemExit("worker/chat.js 里找不到 SYSTEM —— 提示词读不出来")
    return out


PROMPTS = _prompts()
SYSTEM = PROMPTS["zh"]


def build_prompt(q, ctx, scene=""):
    parts = []
    for i, c in enumerate(ctx):
        parts.append(
            "【资料 %d】%s · %s（%s）\n%s\n出处链接：%s"
            % (i, c.get("p", ""), c.get("n", ""), c.get("w", ""), c.get("txt", "")[:700], c.get("u", ""))
        )
    head = "读者说：%s" % q
    if scene:
        head += "\n\n读者的处境：%s" % scene
    return "%s\n\n可用资料：\n\n%s" % (head, "\n\n".join(parts))


def call_model(q, ctx, scene="", history=None, lang="zh"):
    body = json.dumps({
        "model": MODEL,
        "messages": [
            {"role": "system", "content": PROMPTS.get(lang, SYSTEM)},
            *[m for t in (history or [])[-3:]
                for m in ({"role": "user", "content": str(t.get("q", ""))[:200]},
                          {"role": "assistant", "content": str(t.get("a", ""))[:300]})
              if t.get("q") and t.get("a")],
            {"role": "user", "content": build_prompt(q, ctx, scene)},
        ],
        "temperature": 0.3,
        "max_tokens": 700,
    }).encode("utf-8")
    req = urllib.request.Request(BASE, data=body, headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer " + KEY,
    })
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.loads(r.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"]


def stub(q, ctx):
    top = ctx[0] if ctx else {}
    return ("（stub 模式，没有调用任何模型——设 HW_CHAT_KEY 才会真的问）\n\n"
            "你说的是「%s」。站里对得上的第一条是 %s 的《%s》：%s\n\n"
            "另外还找到 %d 篇相关的，列在下面。\nUSED: 0"
            % (q, top.get("p", ""), top.get("n", ""), top.get("dek", ""), max(0, len(ctx) - 1)))


class H(BaseHTTPRequestHandler):
    def _cors(self):
        o = self.headers.get("Origin", "")
        self.send_header("Access-Control-Allow-Origin", o if o in ALLOWED else "null")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Vary", "Origin")

    def _json(self, obj, code=200):
        b = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(b)))
        self._cors()
        self.end_headers()
        self.wfile.write(b)

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_POST(self):
        if self.path != "/chat":
            return self._json({"error": "not found"}, 404)
        if self.headers.get("Origin", "") not in ALLOWED:
            return self._json({"error": "forbidden origin"}, 403)
        ip = self.client_address[0]
        if not allowed(ip):
            return self._json({"error": "今天的 %d 次已经用完了" % DAILY}, 429)
        try:
            n = int(self.headers.get("Content-Length", "0"))
            body = json.loads(self.rfile.read(n).decode("utf-8"))
        except Exception as e:
            return self._json({"error": "bad json: %s" % e}, 400)
        q = (body.get("q") or "").strip()[:500]
        ctx = body.get("ctx") or []
        if not q:
            return self._json({"error": "empty question"}, 400)
        try:
            raw = stub(q, ctx) if not KEY else call_model(
                q, ctx, (body.get("scene") or "")[:40], body.get("history") or [])
        except Exception as e:
            return self._json({"error": "upstream failed: %s" % e}, 502)
        # 排版兜底。prompt 里都写了，但这些是确定性的事，不该指望模型每次都听：
        raw = re.sub(r"(?m)^\s*#{1,6}\s*", "", raw)       # 去掉 # 标题
        # 直引号转「」：prompt 里要求了，但它常滑，成对替换更可靠。
        def _q(m):
            _q.n += 1
            return "」" if _q.n % 2 == 0 else "「"
        _q.n = 0
        raw = re.sub(r"[\u201c\u201d\"]", _q, raw)
        raw = re.sub(r"(?m)^[ \t]+", "", raw)             # 去掉行首缩进
        # 分点之间补空行：「1.」「第二，」这类开头前面若不是空行，插一个
        raw = re.sub(r"(?<=\S)\n(?=(?:\d+[.、]|第[一二三四五六七八九十]+[，、,]))", "\n\n", raw)
        raw = re.sub(r"\n{3,}", "\n\n", raw)             # 别超过一个空行

        # 引用改成行内 [N]，不再需要末尾的 USED 行；模型偶尔还会带上，擦掉。
        raw = re.sub(r"\n*USED\s*[:：].*$", "", raw).rstrip()
        # 「（资料0）」这类内部说法也擦——prompt 里禁了，但提示词不是保证。
        raw = re.sub(r"[（(]\s*资料\s*(\d+)\s*[)）]", r"[\1]", raw)
        raw = re.sub(r"资料\s*(\d+)", r"[\1]", raw)
        used = sorted({int(x) for x in re.findall(r"\[(\d+)\]", raw)})
        _hits[ip].append(time.time())
        self._json({"answer": raw, "used": used, "left": DAILY - len(_hits[ip])})

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    mode = ("stub（未设 HW_CHAT_KEY，不会调用任何模型）" if not KEY
            else "真调用 %s / %s" % (BASE, MODEL))
    print("问答代理 http://localhost:%d/chat" % PORT)
    print("  模式：%s" % mode)
    print("  限流：每 IP 每天 %d 次（内存计数，重启清零）" % DAILY)
    print("  只接受来自 %s 的请求" % "、".join(sorted(ALLOWED)))
    try:
        ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)

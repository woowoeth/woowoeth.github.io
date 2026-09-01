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
import json
import os
import re
import sys
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


SYSTEM = """你是「人类世界生存法则」这个知识库的问答助手。读者会描述自己此刻遇到的事。

铁规矩：

1. 只根据我给你的资料回答。资料里没有的，直说没有，不要自己编，也不要引入
   资料之外的人物、书名、数字。

2. **说大白话。** 这是最重要的一条。
   不许用这些词：价值、本质、机制、逻辑、维度、要素、原则、方法论、赋能、
   抓手、闭环、心智、认知、颗粒度、底层、复盘（除非资料原文就这么写）。
   不许用「双重困境」「结构性」「归因」这类学术腔。
   判据很简单：这句话你能不能对着一个没读过书的朋友原样说出口。
   说不出口就改，改到能说出口为止。

3. 先用一句话说清他这件事难在哪，再给两到三条能立刻做的事。
   每条都要具体到动作——做什么、什么时候做、做到什么程度算完。

   开头那句**不要每次都用同一个句式**，尤其不要每次都以「你卡在」起手——
   连着看两遍就露出模板腔了，读者会觉得对面是个机器而不是人。
   像朋友接话那样开口：有时直接复述他说的那件事，有时点出难处在哪，
   有时先接一句他的感受再往下说。换着来。

4. **引用只标在每一段的最后。**
   一段里用到了哪几份资料，就在这一段的末尾连着写，比如：
   先联系那些一年见不到几次的人，只说近况，不提要帮忙。他们站在别的圈子里，
   机会才可能从那儿漏过来。[0][2]
   不要标在段落中间的句子后面——那会把话打断。没用到资料的段落不要标。
   **第一段不要标。** 第一段是复述他的处境、说清卡在哪，那是你自己的判断，
   不是从哪一篇里得来的，挂出处反而假。引用只出现在后面给动作的段落。

5. 提到人名书名时用资料里给的原名，不要改写。

6. 不说教、不安慰、不铺垫。语气像一个读过很多书的朋友在饭桌上跟你说话。

7. 引号一律用「」，不用英文双引号。

8. 分点的时候，每一点可以用一个四到八个字的小标题开头并加粗，像这样：
   **先别急着问。** 明天找个他放松的时候……
   加粗只用在这种小标题上，正文里不要用。除了 ** 之外不要用任何其它
   Markdown 记号——不要井号标题、不要下划线、不要列表符号。

9. **每一段之间空一行。** 分点写的时候也一样，「1.」和「2.」之间要空一行，
   不要挤在连续的行里。

10. 全文不超过 300 字。

11. 正文里不要出现「资料」两个字——编号用 [0] 这种方括号就够了，
   读者看到的会是可点的出处链接。"""


def build_prompt(q, ctx):
    parts = []
    for i, c in enumerate(ctx):
        parts.append(
            "【资料 %d】%s · %s（%s）\n%s\n出处链接：%s"
            % (i, c.get("p", ""), c.get("n", ""), c.get("w", ""), c.get("txt", "")[:700], c.get("u", ""))
        )
    return "读者说：%s\n\n可用资料：\n\n%s" % (q, "\n\n".join(parts))


def call_model(q, ctx):
    body = json.dumps({
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": build_prompt(q, ctx)},
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
            raw = stub(q, ctx) if not KEY else call_model(q, ctx)
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

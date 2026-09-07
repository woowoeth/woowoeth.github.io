#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上问答的两件事：**部署的是不是仓库里这份**，以及**英文站是不是用英文答**。

    python3 scripts/check_chat_lang.py           # 只比对部署指纹，不花 API
    python3 scripts/check_chat_lang.py --live    # 再真问一句英文，看答案的语言

为什么单独有这个：这个 Worker 不进 CI，靠人去 Cloudflare 后台粘贴部署。
仓库里 2026-09-04 就写好了英文提示词（SYSTEM_EN），线上一直是旧的那份，
英文站的读者问英文、答案全是中文 —— 页面正常、请求 200、没有任何红灯，
**只有真问一句才看得见**。这是「没有人读的那一层坏了没人报」的又一种形状
（FAILURES 第 27、30 条），补法也一样：给那一层配一个会说话的判据。
"""
import json
import os
import re
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ORIGIN = "https://ourword.ai"


def endpoint():
    """端点写在前端页面里，不另存一份 —— 两处会走散。"""
    for p in ("en/index.html", "index.html"):
        f = os.path.join(ROOT, p)
        if not os.path.exists(f):
            continue
        m = re.search(r'HW_CHAT_ENDPOINT\s*=\s*"([^"]+)"', open(f, encoding="utf-8", errors="ignore").read())
        if m and m.group(1).strip():
            return m.group(1).strip().rstrip("/")
    return ""


def get(url):
    r = urllib.request.Request(url, headers={"Origin": ORIGIN, "User-Agent": "hw-check/1"})
    with urllib.request.urlopen(r, timeout=20) as x:
        return json.loads(x.read())


def post(url, payload):
    r = urllib.request.Request(url, data=json.dumps(payload).encode(),
                               headers={"Content-Type": "application/json", "Origin": ORIGIN,
                                        "Referer": ORIGIN + "/en/", "User-Agent": "hw-check/1"})
    with urllib.request.urlopen(r, timeout=90) as x:
        return json.loads(x.read())


def main():
    ep = endpoint()
    if not ep:
        print("问答没开（前端 HW_CHAT_ENDPOINT 是空的）—— 跳过"); return 0
    src = open(os.path.join(ROOT, "worker", "chat.js"), encoding="utf-8").read()
    want = re.search(r"const BUILD = '([^']+)'", src)
    want = want.group(1) if want else ""
    bad = []
    try:
        got = (get(ep + "/?build") or {}).get("build", "")
    except urllib.error.HTTPError as e:
        # 404/405 = 线上那份还不认识 ?build，也就是旧版 —— 这是要报的
        got = "旧版（?build 打不开：%s）" % e.code
    except Exception as e:
        # 断网、DNS、超时：闸门不该因为没网就红。说一句，跳过。
        print("！问答那道闸跳过了：连不上 %s（%s）—— 有网时再跑一次"
              % (ep, type(e).__name__))
        return 0
    if got != want:
        bad.append("线上跑的不是仓库里这份 chat.js：线上 %r，仓库 %r —— 去 Cloudflare 后台"
                   " Edit code 重贴 worker/chat.js 再 Deploy" % (got, want))
    if "--live" in sys.argv and not bad:
        try:
            r = post(ep, {"q": "My manager keeps changing priorities and I feel exhausted. What should I do?",
                          "ctx": [], "cid": "hw-check", "pass": 0, "lang": "en"})
            # 字段名是 answer。第一版写成 .get("a") —— 永远读到空串、永远数出 0 个汉字、
            # 永远报绿。**空答案和英文答案在那个判据眼里一模一样**，
            # 这是「量了代理指标，没量结果」的老毛病（FAILURES 第 23、29 条）。
            a = str(r.get("answer") or r.get("a") or "")
        except Exception as e:
            a = ""
            bad.append("英文实测请求失败：%s" % e)
        else:
            if len(a.strip()) < 40:
                bad.append("英文站答了个空（%d 字）—— 不是语言的问题，是根本没答上来：%r" % (len(a), a[:80]))
        zh = sum(1 for c in a if "一" <= c <= "鿿")
        if len(a.strip()) >= 40 and zh > 5:
            bad.append("英文站的答案里有 %d 个汉字 —— 读者问英文、拿到中文。前 60 字：%s" % (zh, a[:60]))
    if bad:
        print("\n问答有问题 %d 处：" % len(bad))
        for b in bad:
            print("  - " + b)
        return 1
    print("✓ 问答：线上跑的就是仓库里这份（build %s）%s" % (want, "，英文站用英文答" if "--live" in sys.argv else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())

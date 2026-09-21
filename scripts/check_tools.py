#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MCP server 和 Skill 是活的：协议能应答、检索取得到真章节、边界没被删掉。

为什么值得占一道闸：这两样**不在网站的构建链里**，改坏了页面照样全绿、线上照样正常，
只有真去装的人才会发现 —— 又是「没有读者的那一层」（FAILURES #33 是同一个形状：
代码写好了，但它跑的地方没人看着）。所以这里**真起一个 server，按模型的走法走一遍**：
browse 拿组 → 进组拿处境和章节 → 照它给的 url 读正文。不查文件在不在 ——
文件在、协议坏，才是这类东西最常见的坏法。

组名和章节 url 都从上一步的返回里取，不写死：写死的那一刻，这道闸判的就变成
「那个组还在不在」，而不是「这条链通不通」。

联网：server 的数据来自 ourword.ai，所以这道闸在断网时**只跑 Skill 那半边**并说明，
不红 —— 闸门必须能离线跑完（和 check_chat_lang 同一条规矩）。
"""
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MCP = os.path.join(ROOT, "tools", "mcp", "ourword_mcp.py")
SKILL = os.path.join(ROOT, "tools", "skill", "ourword", "SKILL.md")
SITE = "https://ourword.ai"
# 这几句删了这件东西就变质，所以盯着它们（品味标准的第一个信号：肯拦住自己）
HARD = ["只用库里真有的", "指回原文", "不做医疗、法律、金融的个人建议", "紧急求助"]


def online():
    try:
        urllib.request.urlopen(SITE + "/assets/hw-chat-index.json", timeout=15).read(1)
        return True
    except Exception:
        return False


def ask(reqs):
    """一次把几条 JSON-RPC 喂给 server，按 id 收回来。"""
    p = subprocess.run([sys.executable, MCP],
                       input="\n".join(json.dumps(r) for r in reqs),
                       capture_output=True, text=True, timeout=180)
    out = {}
    for line in p.stdout.splitlines():
        try:
            o = json.loads(line)
        except ValueError:
            continue
        out[o.get("id")] = o
    return out, p.stderr


def payload(resp):
    return json.loads(resp["result"]["content"][0]["text"])


def call(name, args, rid):
    return {"jsonrpc": "2.0", "id": rid, "method": "tools/call",
            "params": {"name": name, "arguments": args}}


def check_mcp(bad):
    r, err = ask([{"jsonrpc": "2.0", "id": 1, "method": "tools/list"},
                  call("browse", {}, 2)])
    names = [t["name"] for t in (r.get(1, {}).get("result", {}) or {}).get("tools", [])]
    for want in ("browse", "read_chapter", "search"):
        if want not in names:
            bad.append("MCP 少了工具 %s（现在只有 %s）" % (want, names or "一个都没有"))
    if not names:
        bad.append("server 没应答 tools/list；stderr：%s" % (err.strip()[:200] or "空"))
        return
    try:
        groups = payload(r[2]).get("处境归类", [])
    except Exception as e:
        bad.append("browse() 顶层调用失败：%s" % e)
        return
    if len(groups) < 20:
        bad.append("browse() 只列出 %d 个处境组 —— 索引没载进来" % len(groups))
        return

    # 按模型的走法往下走一层：随便挑一个组，进去看处境和章节
    g = groups[0] if isinstance(groups[0], str) else groups[0].get("具体说法", "")
    r2, _ = ask([call("browse", {"group": g}, 3)])
    try:
        o = payload(r2[3])
    except Exception as e:
        bad.append("browse(group=%s) 失败：%s" % (g, e))
        return
    chs = [c for x in o.get("处境", []) for c in x.get("以前的人怎么处理", [])]
    if len(o.get("处境", [])) < 1:
        bad.append("browse(group=%s) 一条处境都没有" % g)
    if not chs:
        bad.append("browse(group=%s) 的处境里一篇章节都没有" % g)
        return
    off = [c for c in chs if not c.get("url", "").startswith(SITE + "/")]
    if off:
        bad.append("browse 返回的章节里 %d 条 url 不是站内绝对地址（如 %r）"
                   " —— 答案就指不回原文了" % (len(off), off[0].get("url", "")))

    # 英文侧随行的那几句话不许是中文。这是这个仓第五次栽在同一形状上
    # （FAILURES #33 前后那几条：英文站照着中文站的路径/文案写死）——
    # 处境和章节都换成英文了，"怎么用""边界"却还是中文，本地试装时才看见。
    r4, _ = ask([call("browse", {"lang": "en"}, 5)])
    try:
        oe = payload(r4[5])
        han = [k for k in ("怎么用", "边界")
               if re.search(r"[\u4e00-\u9fff]", oe.get(k, ""))]
        if han:
            bad.append("browse(lang=en) 的 %s 还是中文 —— 英文侧的随行说明没跟着换"
                       % "、".join(han))
    except Exception as e:
        bad.append("browse(lang=en) 失败：%s" % e)

    # 照它自己给的地址读正文：模型下一步一定这么做
    u = chs[0]["url"]
    r3, _ = ask([call("read_chapter", {"url": u}, 4)])
    try:
        o3 = payload(r3[4])
    except Exception as e:
        bad.append("read_chapter(%s) 失败：%s" % (u, e))
        return
    if len(o3.get("正文", "")) < 200:
        bad.append("read_chapter(%s) 取不到正文（%d 字）—— browse 给的地址它自己读不了"
                   % (u, len(o3.get("正文", ""))))


def check_skill(bad):
    if not os.path.isfile(SKILL):
        bad.append("没有 tools/skill/ourword/SKILL.md")
        return
    t = open(SKILL, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    if not m:
        bad.append("SKILL.md 没有 frontmatter")
    else:
        fm = m.group(1)
        nm = re.search(r"^name:\s*(\S+)", fm, re.M)
        if not nm or nm.group(1) != "ourword":
            bad.append("SKILL.md 的 name 必须等于目录名 ourword（现在是 %s）"
                       % (nm.group(1) if nm else "没写"))
        if not re.search(r"^description:\s*\S", fm, re.M):
            bad.append("SKILL.md 缺 description —— 没有它，模型不知道什么时候该用")
    for h in HARD:
        if h not in t:
            bad.append("SKILL.md 里「%s」这条边界被删了 —— 删掉它这件东西就变质" % h)


def main():
    bad = []
    if not os.path.isfile(MCP):
        bad.append("没有 tools/mcp/ourword_mcp.py")
        net = False
    else:
        net = online()
        if net:
            check_mcp(bad)
    check_skill(bad)
    if bad:
        print("\n  MCP / Skill 有问题 %d 处：" % len(bad))
        for b in bad[:8]:
            print("    ✗ " + b)
        return 1
    if not net:
        print("  断网：MCP 那半边跳过（它的数据在 ourword.ai 上）；"
              "Skill 的 name 和四条硬边界都在")
        return 0
    print("  MCP：browse 列组 → 进组拿章节 → 照它给的 url 读到正文，"
          "地址都指回站内；Skill 的 name 和四条硬边界都在")
    return 0


if __name__ == "__main__":
    sys.exit(main())

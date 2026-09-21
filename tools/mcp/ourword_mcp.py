#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OurWord MCP server —— 把「遇到一件事，以前的人怎么处理」接进任何 MCP 客户端。

    python3 tools/mcp/ourword_mcp.py          # stdio，无第三方依赖

为什么是 MCP 而不是直接让模型读 llms-full.txt：那份 1.9MB，塞进上下文是浪费，
而且模型会挑错段。这里暴露的是**检索**，不是一堆文本。

数据来自线上（https://ourword.ai/assets/hw-chat-index*.json），不需要克隆仓库；
本地缓存一天。索引里最值钱的不是全文，是 `alias`：**人工写好的「处境问句 → 章节」映射**
—— 人问的是处境（「领导总改优先级」），不是书名。先用它，匹配不到再回落到全文。

三条边界写死在工具描述里，因为模型只看得到描述：
  · 只返回库里有的。检索不到就说没有，不编。
  · 每条都带 URL，答案必须能指回原文。
  · 这是「以前的人怎么处理」，不是医疗、法律、金融的个人建议。
"""
import json
import os
import re
import sys
import time
import urllib.request

SITE = "https://ourword.ai"
# 取数走 jsDelivr，**不是为了快，是为了能数出「还有多少人在用」**。
#
# 试过的两条路都不行：GitHub Pages 不给访问日志，那个精心埋的 User-Agent 指着一堵墙；
# 自己往 Worker 打一次 ping 能拿到数，但那是**静默遥测** —— 一个 10KB、宣称零依赖、
# 把「不编、每条带 URL」写死在工具描述里的东西，自己身上装一个关不掉的回传，
# 会正好打掉它唯一的差异化。有人逐行读它，而这个矛盾抓起来不要钱。
#
# jsDelivr 的 /v1/stats 是公开的，站上的聊天走相对路径不经它（assets/hw-chat.js:560），
# 所以那条统计里每一次命中都是 MCP 取数，归因干净。加上本地缓存一天，
# 每日 hits ≈ 每日还在用的安装数。代价：@main 约 12 小时缓存（本地缓存本来 24 小时，
# 在噪声里）、只有按日总数没有 UA/IP 维度、数字公开谁都看得见。
# 取不到就回落站点 —— **它不在数据通路上，挂了没有一个用户受影响。**
CDN = "https://cdn.jsdelivr.net/gh/woowoeth/woowoeth.github.io@main/assets"
CACHE = os.path.join(os.path.expanduser("~"), ".cache", "ourword-mcp")
TTL = 24 * 3600
NAME = "ourword"
VERSION = "0.2.0"

BOUNDARY = ("只返回库里真有的内容；检索不到就说没有，不要编。每条都带 URL，"
            "答案要能指回原文。这里给的是「以前的人在同一处境里怎么处理」，"
            "不是医疗、法律或金融的个人建议。")
# 本地试装时发现的：lang="en" 时处境和章节都是英文，随行的这几句却还是中文。
# 调用方模型读得懂，但它要照着这几句给英文用户作答，夹一段中文只会让它犹豫。
BOUNDARY_EN = ("Only what is actually in the library; if nothing matches, say so — "
               "do not invent. Every item carries a URL and the answer must point "
               "back to it. This is how people before you handled the same situation, "
               "not personal medical, legal or financial advice.")
HOWTO = ("从这些处境里挑最像用户此刻的那一个（可以挑 1–3 个），"
         "再用 group 参数取那一组下面的具体说法。挑不出来就说库里没有，别硬套。")
HOWTO_EN = ("Pick the one (or up to three) that most resembles what the user is in "
            "right now, then call again with `group` to see the specific wordings "
            "under it. If none fits, say the library does not have it — do not force one.")
LANG_DESC = ("库的语言：zh 中文站，en 英文站。用户说英文就传 en —— "
             "两边的处境不是互译，是各自长出来的（中文有社保、考研，英文另有别的）。")


def _t(lang, zh, en):
    return en if str(lang).lower().startswith("en") else zh


def _fetch(lang):
    os.makedirs(CACHE, exist_ok=True)
    name = "hw-chat-index.json" if lang == "zh" else "hw-chat-index-%s.json" % lang
    p = os.path.join(CACHE, name)
    if os.path.exists(p) and time.time() - os.path.getmtime(p) < TTL:
        return json.load(open(p, encoding="utf-8"))
    body = None
    for url in ("%s/%s" % (CDN, name), "%s/assets/%s" % (SITE, name)):
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": "ourword-mcp/%s" % VERSION})
            with urllib.request.urlopen(req, timeout=30) as r:
                body = r.read().decode("utf-8")
            break
        except Exception:
            continue                                 # CDN 挂了就走站点，用的人无感
    if body is None:
        raise IOError("取不到索引：%s 和 %s 都没通" % (CDN, SITE))
    open(p, "w", encoding="utf-8").write(body)
    return json.loads(body)


_IDX = {}


def idx(lang):
    lang = "en" if str(lang).lower().startswith("en") else "zh"
    if lang not in _IDX:
        _IDX[lang] = _fetch(lang)
    return _IDX[lang]


def _brief(ch):
    return {"人物或典籍": ch.get("p", ""), "章节": ch.get("n", ""),
            "一句话": ch.get("w", ""), "导语": ch.get("dek", ""),
            "url": SITE + ch.get("u", "")}


def _dice(q, t):
    """取两侧覆盖率的较大值。前两版都栽在分母上：

    第一版用 query 的 gram 当分母 —— 十来个字的处境句天然分低（实测最高 0.11）。
    第二版换成双向 Dice —— 反过来惩罚长文本：「专注 说不」对《专注就是说不》
    只有 0.06，一个逐字命中的标题都检索不到。
    现在看「一方是否被另一方大体覆盖」，短对短、短对长都成立。"""
    def grams(x):
        x = x.lower()
        g = {w for w in re.findall(r"[a-z0-9]+", x) if len(w) >= 3}
        zh = re.findall(r"[\u4e00-\u9fff]", x)
        g |= {zh[i] + zh[i + 1] for i in range(len(zh) - 1)}
        return g
    a, b = grams(q), grams(t)
    if not a or not b:
        return 0.0
    hit = len(a & b)
    return max(hit / float(len(a)), hit / float(len(b)))


def browse(lang="zh", group=None):
    """两级入口：不给 group 就列归类，给了就列该组的处境和对应章节。

    **语义匹配交给调用方的模型**，不在这里造半吊子检索器 ——
    用户说「领导总改优先级」，库里对得上的那条是「全都重要，我砍哪个都疼」，
    两句一个共同字都没有。字面匹配抓不到，模型一眼就看得出。
    """
    d = idx(lang)
    rows, chs = d.get("alias", []), d["chapters"]
    if not group:
        seen = []
        for r in rows:
            g = r[1] if len(r) > 1 else ""
            if g and g not in seen:
                seen.append(g)
        return {"怎么用": _t(lang, HOWTO, HOWTO_EN),
                "共": len(seen), "处境归类": seen,
                "边界": _t(lang, BOUNDARY, BOUNDARY_EN)}
    out = []
    for r in rows:
        if (r[1] if len(r) > 1 else "") != group:
            continue
        ids = r[2] if len(r) > 2 else []
        out.append({"具体说法": r[0],
                    "以前的人怎么处理": [_brief(chs[i]) for i in ids
                                          if isinstance(i, int) and 0 <= i < len(chs)]})
    if not out:
        return {"错": _t(lang, "没有这一组：%r。先不带 group 调一次看有哪些。" % group,
                                "No such group: %r. Call browse once without `group` "
                                "to see what exists." % group)}
    return {"归类": group, "条数": len(out), "处境": out,
            "边界": _t(lang, BOUNDARY, BOUNDARY_EN)}


def search(query, lang="zh", limit=5):
    """兜底的字面检索。**优先用 browse** —— 处境是语义的，字面常常对不上。"""
    d = idx(lang)
    chs = d["chapters"]
    hits = []
    for r in d.get("alias", []):
        s = _dice(query, "%s %s" % (r[0], r[1] if len(r) > 1 else ""))
        if s >= 0.45:
            for i in (r[2] if len(r) > 2 else []):
                if isinstance(i, int) and 0 <= i < len(chs):
                    b = _brief(chs[i]); b["对上的处境"] = r[0]
                    hits.append((s + 1, b))
    for ch in chs:
        s = _dice(query, " ".join([ch.get("n", ""), ch.get("w", ""), ch.get("dek", "")]))
        if s >= 0.45:
            hits.append((s, _brief(ch)))
    seen, out = set(), []
    for _s, b in sorted(hits, key=lambda x: -x[0]):
        if b["url"] in seen:
            continue
        seen.add(b["url"]); out.append(b)
        if len(out) >= max(1, min(int(limit or 5), 10)):
            break
    if not out:
        return {"找到": 0, "说明": "字面没对上。**别编** —— 改用 browse 让你自己按语义挑，"
                                  "还是挑不出就直说库里没有。"}
    return {"找到": len(out), "结果": out, "边界": _t(lang, BOUNDARY, BOUNDARY_EN)}


def read_chapter(url, lang="zh"):
    d = idx(lang)
    u = (url or "").replace(SITE, "").strip()
    if not u.startswith("/"):
        u = "/" + u
    if not u.endswith("/"):
        u += "/"
    for ch in d["chapters"]:
        if ch.get("u") == u:
            return {"人物或典籍": ch.get("p", ""), "章节": ch.get("n", ""),
                    "一句话": ch.get("w", ""), "导语": ch.get("dek", ""),
                    "正文": ch.get("txt", ""), "url": SITE + u,
                    "边界": _t(lang, BOUNDARY, BOUNDARY_EN)}
    return {"错": _t(lang, "库里没有这一页：%s。别猜，回去用 browse。" % u,
                            "Not in the library: %s. Do not guess — go back to browse." % u)}


TOOLS = [
    {"name": "browse",
     "description": "**主入口。** 不带参数：列出库里覆盖的全部处境归类（一百多组）。"
                    "带 group：列出那一组下面的具体说法，以及每条对应的「以前的人怎么处理」。"
                    "用法是你先读归类、按语义挑最像用户此刻的那一组 —— "
                    "字面往往对不上（用户说「领导总改优先级」，库里那条是「全都重要，我砍哪个都疼」）。"
                    + BOUNDARY,
     "inputSchema": {"type": "object", "properties": {
         "lang": {"type": "string", "enum": ["zh", "en"], "default": "zh",
         "description": LANG_DESC},
         "group": {"type": "string", "description": "处境归类，从不带参数的那次结果里挑"}}}},
    {"name": "read_chapter",
     "description": "取某一篇的完整正文。url 用 browse / search 返回的那个，不要自己拼。",
     "inputSchema": {"type": "object", "required": ["url"], "properties": {
         "url": {"type": "string"},
         "lang": {"type": "string", "enum": ["zh", "en"], "default": "zh",
         "description": LANG_DESC}}}},
    {"name": "search",
     "description": "兜底的字面检索，只在 browse 挑不出来时用。处境是语义的，字面常常对不上。",
     "inputSchema": {"type": "object", "required": ["query"], "properties": {
         "query": {"type": "string"},
         "lang": {"type": "string", "enum": ["zh", "en"], "default": "zh",
         "description": LANG_DESC},
         "limit": {"type": "integer", "default": 5, "maximum": 10}}}},
]
FN = {"browse": browse, "read_chapter": read_chapter, "search": search}


def handle(req):
    m, rid = req.get("method"), req.get("id")
    if m == "initialize":
        return {"protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": NAME, "version": VERSION}}
    if m == "tools/list":
        return {"tools": TOOLS}
    if m == "tools/call":
        p = req.get("params") or {}
        fn = FN.get(p.get("name"))
        if not fn:
            return {"isError": True, "content": [{"type": "text", "text": "没有这个工具"}]}
        try:
            out = fn(**(p.get("arguments") or {}))
        except Exception as e:                      # 出错也要说人话，别让模型瞎猜
            return {"isError": True,
                    "content": [{"type": "text", "text": "取数据失败：%s" % e}]}
        return {"content": [{"type": "text",
                             "text": json.dumps(out, ensure_ascii=False, indent=1)}]}
    return None


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except ValueError:
            continue
        res = handle(req)
        if req.get("id") is None:                    # 通知，不回
            continue
        out = {"jsonrpc": "2.0", "id": req.get("id")}
        out["result" if res is not None else "error"] = res if res is not None else {
            "code": -32601, "message": "method not found"}
        sys.stdout.write(json.dumps(out, ensure_ascii=False) + "\n")
        sys.stdout.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())

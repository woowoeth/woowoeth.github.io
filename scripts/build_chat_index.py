#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""为悬浮球问答生成检索索引 assets/hw-chat-index.json。

不用 llms-full.txt 做检索：它 1.4MB，整篇喂给模型既超上下文又贵。
这里把 290 篇章节压成检索单元，并把处境层的 346 个问题作为「查询别名」——
那些问题本来就是第一人称口语（「我知道该做，可就是动不了」），
跟用户描述自己处境的说法是同一种语言，是最好的匹配信号。

产物结构：
  {"v": 1, "chapters": [{i,p,n,w,u,dek,txt,q}], "alias": [[问题, 章节下标...]]}
    txt 是给模型看的正文（story + 分则 + apply），截断到 ~700 字
    q   是这篇的金句，回答时可直接引用
"""
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, "seo"); sys.path.insert(0, "scripts")
import hw_chapters as C, hw_slugs          # noqa: E402
from hwx_scenes import SCENES              # noqa: E402

plain = lambda t: re.sub(r"\s+", " ", str(t or "").replace("==", "")).strip()

idx = {}
chapters = []
for c in C.CHAPTERS:
    sl = hw_slugs.slug_for(c["parent"])
    body = [plain(c["story"])]
    for f in c.get("f", []):
        body.append("%s：%s" % (plain(f.get("n")), plain(f.get("d"))))
    body.append(plain(c.get("apply", "")))
    txt = " ".join(x for x in body if x)[:700]
    idx[(sl, c["k"])] = len(chapters)
    chapters.append({
        "i": len(chapters), "p": c["parent"], "n": c["n"], "w": plain(c.get("w")),
        "u": "/i/%s/%s/" % (sl, c["k"]), "dek": plain(c.get("dek")),
        "txt": txt, "q": [plain(x) for x in (c.get("q") or [])][:2],
    })

alias = []
for name, grp, QS in SCENES:
    for q, ans in QS:
        hits = [idx[tuple(a)] for a in ans if tuple(a) in idx]
        if hits:
            alias.append([q, name, hits])

out = {"v": 1, "chapters": chapters, "alias": alias}
os.makedirs("assets", exist_ok=True)
with open("assets/hw-chat-index.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
size = os.path.getsize("assets/hw-chat-index.json")
print("检索索引：%d 篇章节 + %d 条问题别名，%.0f KB" % (len(chapters), len(alias), size / 1024))

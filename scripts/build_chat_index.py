#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""为悬浮球问答生成检索索引。

    assets/hw-chat-index.json      中文（简体站与繁体站共用）
    assets/hw-chat-index-en.json   英文

不用 llms-full.txt 做检索：它 1.4MB，整篇喂给模型既超上下文又贵。
这里把章节压成检索单元，并把处境层的问题作为「查询别名」——
那些问题本来就是第一人称口语（「我知道该做，可就是动不了」／
"I know what to do. I'm not doing it."），跟用户描述自己处境的说法是同一种
语言，是最好的匹配信号。

产物结构：
  {"v": 1, "lang": "zh"|"en", "chapters": [{i,p,n,w,u,dek,txt,q}],
   "alias": [[问题, 处境名, 章节下标...]]}
    txt 是给模型看的正文（story + 分则 + apply），截断到 ~700
    q   是这篇的金句，回答时可直接引用

英文那份的正文截断按**词**算不按字符算：700 个英文字符大约只有 110 个词，
比中文 700 字少掉一大截信息，模型会因为资料不够而答得笼统。
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, "seo")
sys.path.insert(0, "scripts")

plain = lambda t: re.sub(r"\s+", " ", str(t or "").replace("==", "")).strip()


def build(lang, chapters_pkg, scenes_mod, url_prefix, out_name, sep, limit):
    import importlib
    import pkgutil

    here = os.path.join(ROOT, "seo", chapters_pkg)
    rows = []
    for mod in sorted(m.name for m in pkgutil.iter_modules([here])):
        m = importlib.import_module(chapters_pkg + "." + mod)
        spec = getattr(m, "PARENT", {}) or {}
        for ch in getattr(m, "CHAPTERS", []) or []:
            rows.append((spec.get("name", ""), spec.get("slug", ""), ch))

    idx, chapters = {}, []
    for parent, slug, c in rows:
        body = [plain(c["story"])]
        for f in c.get("f", []):
            body.append("%s%s%s" % (plain(f.get("n")), sep, plain(f.get("d"))))
        body.append(plain(c.get("apply", "")))
        txt = " ".join(x for x in body if x)
        # 中文按字符截，英文按词截 —— 同样 700，一个是 700 字一个是 110 词
        txt = txt[:limit] if lang == "zh" else " ".join(txt.split()[:limit])
        idx[(slug, c["k"])] = len(chapters)
        chapters.append({
            "i": len(chapters), "p": parent, "n": c["n"], "w": plain(c.get("w")),
            "u": "%s/i/%s/%s/" % (url_prefix, slug, c["k"]),
            "dek": plain(c.get("dek")), "txt": txt,
            "q": [plain(x) for x in (c.get("q") or [])][:2],
        })

    alias = []
    for name, _grp, QS in importlib.import_module(scenes_mod).SCENES:
        for q, ans in QS:
            hits = [idx[tuple(a)] for a in ans if tuple(a) in idx]
            if hits:
                alias.append([q, name, hits])

    out = {"v": 1, "lang": lang, "chapters": chapters, "alias": alias}
    os.makedirs("assets", exist_ok=True)
    p = os.path.join("assets", out_name)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
    print("检索索引 %s：%d 篇章节 + %d 条问题别名，%.0f KB"
          % (out_name, len(chapters), len(alias), os.path.getsize(p) / 1024))


def main():
    # 中文：hw_chapters 那条老路径（它在导入时自己 _load()）
    import hw_chapters as C
    import hw_slugs
    from hwx_scenes import SCENES

    idx, chapters = {}, []
    for c in C.CHAPTERS:
        sl = hw_slugs.slug_for(c["parent"])
        body = [plain(c["story"])]
        for f in c.get("f", []):
            body.append("%s：%s" % (plain(f.get("n")), plain(f.get("d"))))
        body.append(plain(c.get("apply", "")))
        idx[(sl, c["k"])] = len(chapters)
        chapters.append({
            "i": len(chapters), "p": c["parent"], "n": c["n"], "w": plain(c.get("w")),
            "u": "/i/%s/%s/" % (sl, c["k"]), "dek": plain(c.get("dek")),
            "txt": " ".join(x for x in body if x)[:700],
            "q": [plain(x) for x in (c.get("q") or [])][:2],
        })
    alias = []
    for name, _grp, QS in SCENES:
        for q, ans in QS:
            hits = [idx[tuple(a)] for a in ans if tuple(a) in idx]
            if hits:
                alias.append([q, name, hits])
    out = {"v": 1, "lang": "zh", "chapters": chapters, "alias": alias}
    with open("assets/hw-chat-index.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
    print("检索索引 hw-chat-index.json：%d 篇章节 + %d 条问题别名，%.0f KB"
          % (len(chapters), len(alias),
             os.path.getsize("assets/hw-chat-index.json") / 1024))

    if os.path.isdir(os.path.join(ROOT, "seo", "chapters_en")):
        build("en", "chapters_en", "hwx_scenes_en", "/en",
              "hw-chat-index-en.json", " — ", 260)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SEO/GEO build for 人类世界生存法则. Run from the repo root: python seo/build_seo.py

The knowledge base lives in one inline JS array in index.html, which means every
crawler that does not run JavaScript — including all the AI answer engines — sees
an empty page. This reads that array and writes one static page per entry.
"""
import datetime
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import geo_kit as G

SITE = G.Site(
    path="humanworld",
    name="Human World", name_zh="人类世界生存法则",
    tagline="70+ people and books on how the world actually works, across 2,600 years",
    tagline_zh="70+ 个人物与典籍的生存智慧，跨越 2600 年",
    description=(
        "A knowledge base of the durable rules people have worked out about strategy, money, "
        "power, human nature and building things — drawn from more than seventy figures and "
        "classic texts across 2,600 years. Each entry gives the one idea that person is "
        "actually remembered for, the story behind it, the sub-principles with worked "
        "examples, and how it applies today."),
    description_zh=(
        "一个关于「世界到底怎么运转」的知识库：战略、财富、权力、人性、创业，取自 70 多位"
        "人物与典籍，跨越 2600 年。每一条都写清楚这个人真正留下的那一个想法、背后的故事、"
        "拆开的分则与例子，以及今天怎么用。"),
    keywords=("生存智慧, 战略思维, 孙子兵法, 人性, 财富 投资 原则, 权力 治理, 创业 方法论, "
              "经典 解读, life principles, strategy, human nature, classic texts"),
    item_type="Article", item_noun="entry", item_noun_zh="条目",
    lang="zh-Hans", changefreq="weekly",
)

HOW = ("Written by hand, one entry per figure or text. Each entry is condensed to the single "
       "idea that person is actually remembered for, then unpacked into sub-principles with "
       "historical and modern worked examples.")

CITE = ("Cite the individual entry page. Quotes from classical texts inside an entry belong to "
        "those texts; attribute the condensation and the modern reading to "
        "\"人类世界生存法则 (OurWord AI)\".")


def load_array(path="index.html", varname="D"):
    """Pull `const D=[...]` out of index.html and turn it into real data."""
    s = open(path, encoding="utf-8").read()
    m = re.search(r"(?:const|let|var)\s+%s\s*=\s*\[" % re.escape(varname), s)
    if not m:
        return []
    j = s.index("[", m.start())
    depth, k = 0, j
    while k < len(s):
        c = s[k]
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
            if depth == 0:
                break
        elif c == '"':
            k += 1
            while k < len(s) and s[k] != '"':
                if s[k] == "\\":
                    k += 1
                k += 1
        k += 1
    raw = s[j:k + 1]
    raw = re.sub(r"([{,]\s*)([A-Za-z_]\w*)\s*:",
                 lambda mm: '%s"%s":' % (mm.group(1), mm.group(2)), raw)
    raw = re.sub(r",\s*([}\]])", r"\1", raw)
    return json.loads(raw)


def flat(v):
    """Fields are variously a string, a list of strings, or a list of {n, why/d} dicts."""
    if v is None:
        return ""
    if isinstance(v, str):
        return v
    out = []
    for x in (v if isinstance(v, list) else [v]):
        if isinstance(x, dict):
            head = x.get("n") or x.get("name") or x.get("t") or ""
            body = x.get("why") or x.get("d") or x.get("desc") or x.get("eg") or ""
            out.append(("%s：%s" % (head, body)).strip("：") if head or body else "")
        else:
            out.append(str(x))
    return "\n".join(o for o in out if o)


def era_bucket(y):
    """A shared era label so entries cluster into hubs instead of each having its own."""
    try:
        y = int(y)
    except Exception:
        return ""
    for lo, hi, label in ((-3000, -200, "先秦与古典时代"), (-200, 400, "秦汉至魏晋"),
                          (400, 1400, "中古"), (1400, 1800, "近世"),
                          (1800, 1950, "工业时代"), (1950, 3000, "现代")):
        if lo <= y < hi:
            return label
    return ""


def load_items():
    items = []
    entries = list(load_array())
    # 反向关联索引，与 index.html 中的 relOf/contrastOf 保持一致：l 和 contrast 是手写的
    # 单向边，若不补齐反向，静态页里被指向的一方看不到来源，新条目在抓取层等于孤岛。
    rev_l, rev_c = {}, {}
    for e in entries:
        src = e.get("n") or ""
        for x in (e.get("l") or []):
            rev_l.setdefault(x, []).append(src)
        for c in (e.get("contrast") or []):
            if isinstance(c, dict) and c.get("n"):
                rev_c.setdefault(c["n"], []).append({"n": src, "why": c.get("why") or ""})
    for e in entries:
        name = e.get("n") or ""
        rel = list(e.get("l") or [])
        seen = set(rel)
        for x in rev_l.get(name, []):
            if x != name and x not in seen:
                seen.add(x)
                rel.append(x)
        ctr = [c for c in (e.get("contrast") or []) if isinstance(c, dict)]
        seen_c = {c.get("n") for c in ctr}
        for c in rev_c.get(name, []):
            if c["n"] != name and c["n"] not in seen_c:
                seen_c.add(c["n"])
                ctr.append(c)
        e_year = e.get("y")
        one = e.get("w") or ""
        era = e.get("e") or ""
        cat = e.get("c") or ""
        blocks = []
        if e.get("d"):
            blocks.append(("Q：这个人（这本书）到底留下了什么？", e["d"]))
        if e.get("story"):
            blocks.append(("Q：背后是什么故事？", e["story"]))
        for f in (e.get("f") or []):
            if not isinstance(f, dict):
                continue
            body = f.get("d") or ""
            if f.get("eg"):
                body += "\n例：" + f["eg"]
            if body:
                blocks.append(("分则 · %s" % (f.get("n") or ""), body))
        if e.get("apply"):
            blocks.append(("Q：今天怎么用？", flat(e["apply"])))
        if e.get("q"):
            blocks.append(("原话", flat(e["q"])))
        if ctr:
            blocks.append(("Q：和谁对照着读？", flat(ctr)))
        if rel:
            blocks.append(("延伸", flat(rel)))

        summary = "%s%s——%s。%s" % (name, ("（%s）" % era if era else ""), one,
                                   G.plain(e.get("d"), 140))
        # Chinese-only site: no English twin, so no hreflang pair and no duplicate URL.
        # geo_kit renders the default /i/ pages in Chinese because Site.lang is zh-Hans.
        # 典籍 are Books, everyone else is a Person — a truer schema type than
        # generic Article, and the one an answer engine reasons about.
        is_text = (cat == "典籍·洞见") or any(
            k in name for k in ("经", "论", "简史", "兵法", "史记", "书", "记", "传", "录"))
        extra = ({"about": one} if one else {})
        if is_text:
            extra["bookFormat"] = "https://schema.org/Hardcover"
        items.append(G.Item(
            slug=name, title=name, summary=summary,
            blocks=blocks,
            tags=[t for t in [cat, era_bucket(e_year), one] if t],
            updated="",
            schema_type="Book" if is_text else "Person",
            schema_extra=extra,
        ))
    items.sort(key=lambda i: i.title)
    return items


def main():
    items = load_items()
    rep = G.build(SITE, items, root=".", today=datetime.date.today().isoformat(),
                  how_built=HOW, cite_as=CITE,
                  extra_sitemaps=[])
    print("HumanWorld seo/geo:", json.dumps(rep, ensure_ascii=False))
    return rep


if __name__ == "__main__":
    main()

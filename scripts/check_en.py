#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""English site gate.

    python3 scripts/check_en.py

The English site is not a conversion of the Chinese one — every string is
written by hand — so none of the繁体 machinery applies. What can go wrong here
is different, and each rule below covers one way it actually goes wrong:

① Every (slug, k) resolves to a real chapter. A typo here renders a dead link
   that looks completely normal on the page — this is the single most likely
   defect, because the refs are copied by hand from the Chinese layer.
② Every referenced entry is inside the pilot set. A ref to an untranslated
   entry sends an English reader to a Chinese page. Rule ① would pass it.
③ No CJK anywhere in the English strings. A line left untranslated is invisible
   in review — you read past it — but it is glaring to a reader.
④ No duplicate questions, and no duplicate (group, situation). The Chinese
   layer has near-identical phrasings on purpose; if two came across as the
   same English sentence, one of them is dead weight in the list.
⑤ Group and situation names carry no trailing punctuation and stay short
   enough for the chip strip — long ones wrap and break the row.
⑥ Coverage back-check: every pilot entry is reachable from at least one
   question, and every chapter of every pilot entry too. An entry nothing
   points at is a page no reader can find from the front door.
⑦ 「今日一句」的每条映射：值必须是处境层里的**原句**，而且那一句必须真的
   引用了这一章。差一个字就是配错，而配错的第一人称句是假共情 —— 中文那边
   的教训写在 quote_asks.py 开头。每章必须且只能有一条。
⑧ 英文章节的长度闸。中文一个字顶英文一个词还多，照着中文的篇幅写英文，
   dek 会长到吃掉两行、金句会长到没法当金句用。这几个数是排版定的，不是
   风格偏好：dek 12-30 词、story 50-110 词、分则 20-55 词、例 8-40 词、
   金句 ≤14 词。
   靠眼睛盯 79 章必漏，所以让机器数。
⑨ 章节数据自身完整：每章七个字段都在，f 至少两条，q 至少两条，
   story 里恰好一处 ==…== 强调（模板拿它做引文块，没有就是一段白文，
   两处则第二处不会被渲染）。
"""
import collections
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "seo"))

import hw_chapters as H          # _load() runs at import — do not call it again
from hwx_scenes_en import SCENES
from quote_asks_en import QUOTE_ASKS_EN

PILOT = """su-shi wang-yangming zhuangzi pu-songling huineng fan-li li-ka-shing han-feizi
kasparov wiener excellent-sheep maslach cacioppo harvard-study granovetter curie
hochschild rat-park vygotsky thomas-gordon cs-lewis churchill perel jung sapolsky
dweck john-ratey gottman montessori boyd""".split()

def load_en():
    """已经写好的英文章节。

    单独加载而不是靠 HW_CHAPTERS 环境变量切换，是因为这道闸要同时用到两份：
    引用是否成立要拿**中文章节**当全集校验（那是这一版计划里存在的 79 章），
    长度和完整性只能校验**已经写出来的**那些。混用一份的话，写到一半时闸门
    会把还没写的章全报成「引用指向不存在的页」，把真正的错埋掉。
    """
    import importlib
    import pkgutil
    here = os.path.join(ROOT, "seo", "chapters_en")
    if not os.path.isdir(here):
        return []
    sys.path.insert(0, os.path.join(ROOT, "seo"))
    out = []
    for mod in sorted(m.name for m in pkgutil.iter_modules([here])):
        m = importlib.import_module("chapters_en." + mod)
        spec = getattr(m, "PARENT", {}) or {}
        for ch in getattr(m, "CHAPTERS", []) or []:
            ch = dict(ch)
            ch["parent_slug"] = spec.get("slug", "")
            ch["parent"] = spec.get("name", "")
            out.append(ch)
    return out


CJK = re.compile(r"[　-〿一-鿿＀-￯]")
# 例（eg）和分则（d）不是一回事，不能共用一个区间：d 是论证，要说完；
# eg 是一句具体的例子，短才好用。第一版把 20-55 同时套在两者上，
# 结果闸门把一批写得正好的例子判成太短 —— 照它去注水只会写坏。
LEN = {"dek": (12, 30), "story": (50, 110),
       "part": (20, 55), "eg": (8, 40), "quote": (1, 14)}
MAX_SCENE = 46          # 处境名进 chip 条，长了换行把整排挤散
MAX_GROUP = 30


def main():
    real = {(c["parent_slug"], c["k"]) for c in H.CHAPTERS}
    bad, seen_q, seen_s = [], {}, {}
    hit_entry, hit_ch = set(), set()

    for scene, group, qs in SCENES:
        # ③ 英文层里不该有中日韩字符
        for label, s in (("group", group), ("situation", scene)):
            if CJK.search(s):
                bad.append("%s still Chinese: %r" % (label, s))
        # ⑤ 名字的形状
        if len(scene) > MAX_SCENE:
            bad.append("situation too long (%d > %d): %r" % (len(scene), MAX_SCENE, scene))
        if len(group) > MAX_GROUP:
            bad.append("group too long (%d > %d): %r" % (len(group), MAX_GROUP, group))
        if scene.rstrip() != scene or scene.endswith((".", "?", "!", ":")):
            bad.append("situation should not end in punctuation: %r" % scene)
        # ④ (分组, 处境) 不能重
        if (group, scene) in seen_s:
            bad.append("duplicate situation: %r in %r" % (scene, group))
        seen_s[(group, scene)] = 1

        for q, refs in qs:
            if CJK.search(q):
                bad.append("question still Chinese: %r" % q)
            if q in seen_q:
                bad.append("duplicate question: %r (%r and %r)" % (q, seen_q[q], scene))
            seen_q[q] = scene
            if not refs:
                bad.append("question with no chapter: %r" % q)
            for slug, k in refs:
                # ② 必须在试水名单里
                if slug not in PILOT:
                    bad.append("%r points at %s, which is not in the pilot set" % (q, slug))
                # ① 必须真的存在
                elif (slug, k) not in real:
                    bad.append("%r points at %s/%s, which does not exist" % (q, slug, k))
                else:
                    hit_entry.add(slug)
                    hit_ch.add((slug, k))

    # ⑥ 反向：每个条目、每一章都得有人指得到
    for slug in PILOT:
        if slug not in hit_entry:
            bad.append("nothing points at entry %s" % slug)
    for slug, k in sorted(real):
        if slug in PILOT and (slug, k) not in hit_ch:
            bad.append("nothing points at chapter %s/%s" % (slug, k))

    # ⑦ 今日一句
    q_of = {}
    for scene, group, qs in SCENES:
        for q, refs in qs:
            for r in refs:
                q_of.setdefault("%s/%s" % r, set()).add(q)
    strip = lambda x: x.strip(" .?!\"'").lower()
    for key, q in sorted(QUOTE_ASKS_EN.items()):
        if key not in q_of:
            bad.append("today's line maps %s, which no question points at" % key)
        elif q not in q_of[key]:
            near = any(strip(x) == strip(q) for x in q_of[key])
            bad.append("today's line for %s is not a question that points at it: %r%s"
                       % (key, q, "  (punctuation differs?)" if near else ""))
    for key in sorted(q_of):
        if key not in QUOTE_ASKS_EN:
            bad.append("no today's line for chapter %s" % key)

    # ⑧⑨ 章节自身
    def words(x):
        return len(x.split())

    written = load_en()
    planned = {(c["parent_slug"], c["k"]) for c in H.CHAPTERS if c["parent_slug"] in PILOT}
    for ch in sorted(written, key=lambda c: (c["parent_slug"], c["k"])):
        if (ch["parent_slug"], ch["k"]) not in planned:
            bad.append("%s/%s is written in English but not in the pilot plan"
                       % (ch["parent_slug"], ch["k"]))
            continue
        where = "%s/%s" % (ch["parent_slug"], ch["k"])
        for field in ("n", "w", "src", "dek", "story", "apply"):
            if not (ch.get(field) or "").strip():
                bad.append("%s is missing %s" % (where, field))
        parts, quotes = ch.get("f") or [], ch.get("q") or []
        if len(parts) < 2:
            bad.append("%s has %d parts, needs at least 2" % (where, len(parts)))
        if len(quotes) < 2:
            bad.append("%s has %d lines to keep, needs at least 2" % (where, len(quotes)))
        n_emph = (ch.get("story") or "").count("==")
        if n_emph != 2:
            bad.append("%s: story needs exactly one ==...== span, found %d marks"
                       % (where, n_emph))
        for field, key in (("dek", "dek"), ("story", "story")):
            lo, hi = LEN[key]
            n = words(ch.get(field) or "")
            if not lo <= n <= hi:
                bad.append("%s: %s is %d words (want %d-%d)" % (where, field, n, lo, hi))
        for i, part in enumerate(parts, 1):
            for key in ("d", "eg"):
                lo, hi = LEN["part" if key == "d" else "eg"]
                n = words(part.get(key) or "")
                if not lo <= n <= hi:
                    bad.append("%s: part %d %s is %d words (want %d-%d)"
                               % (where, i, key, n, lo, hi))
        for q in quotes:
            if words(q) > LEN["quote"][1]:
                bad.append("%s: line to keep is %d words (max %d): %r"
                           % (where, words(q), LEN["quote"][1], q))

    nq = sum(len(q) for _, _, q in SCENES)
    print("English: %d groups · %d situations · %d questions · "
          "%d entries · %d chapters planned · %d today's-lines · "
          "%d/%d chapters written"
          % (len({g for _, g, _ in SCENES}), len(SCENES), nq,
             len(hit_entry), len(hit_ch), len(QUOTE_ASKS_EN),
             len(written), len(planned)))
    if bad:
        print("\nnot ready:")
        for b in bad[:40]:
            print("  x " + b)
        if len(bad) > 40:
            print("  … and %d more" % (len(bad) - 40))
        return 1
    print("ok — every ref resolves, all inside the pilot set, no Chinese left, "
          "no duplicates, every entry and chapter reachable,\n   every chapter has a today's line that points back at it")
    return 0


if __name__ == "__main__":
    sys.exit(main())

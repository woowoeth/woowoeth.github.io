#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Standing checks for the deep-read layer. Run from the repo root."""
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "seo"))
import hw_chapters as C  # noqa: E402

plain = lambda t: str(t or "").replace("==", "")
bad = []

# every catalog item must have an essay, and vice versa
for name, spec in C.PARENTS.items():
    keys = {it["k"] for it in spec["items"] if it.get("ready")}
    have = {c["k"] for c in C.CHAPTERS if c["parent"] == name}
    for k in keys - have:
        bad.append("%s: catalog lists %s but there is no chapter" % (name, k))
    for k in have - keys:
        bad.append("%s: chapter %s is not in the catalog" % (name, k))

# shape: the structure every chapter is supposed to share
for c in C.CHAPTERS:
    where = "%s/%s" % (c["parent"], c["n"])
    if not 25 <= len(plain(c["dek"])) <= 70:
        bad.append("%s: dek %d chars (want 25-70)" % (where, len(plain(c["dek"]))))
    if not 80 <= len(plain(c["story"])) <= 190:
        bad.append("%s: story %d chars (want 80-190)" % (where, len(plain(c["story"]))))
    if len(c["f"]) < 3:
        bad.append("%s: only %d 分则" % (where, len(c["f"])))
    for f in c["f"]:
        if not 35 <= len(plain(f["d"])) <= 110:
            bad.append("%s/%s: d %d chars (want 35-110)" % (where, f["n"], len(plain(f["d"]))))
    if plain(c["apply"]).count("\n") != 2:
        bad.append("%s: apply is not 局面/先问/用反了" % where)
    if len(c["q"]) != 3:
        bad.append("%s: %d quotes (want 3)" % (where, len(c["q"])))
    # 正文的加重只留一套：故事段至多一处红字（这一篇引的原话或它赖以成立的那个事实），
    # 分则交给金句就地加重（b.key），文末金句块整块就是金句、不再往里标红。
    # 原来是「至少有一处」，改完之后全站 957+745 处压到 363 处。
    n_story = c["story"].count("==") // 2
    if n_story > 1:
        bad.append("%s: story 有 %d 处红字（至多一处）" % (where, n_story))
    if any("==" in f["d"] for f in c["f"]):
        bad.append("%s: 分则里有红字（该交给金句就地加重）" % where)
    if any("==" in x for x in c["q"]):
        bad.append("%s: 文末金句块里有红字" % where)
    # 原来写的是 `if c["src"] and not plain(...)` —— 空串是 falsy，
    # 这条分支对**真正空掉的 src** 永远不触发，只能抓到「写了但全是 == 或空白」。
    # 也就是说它想拦的那种情况恰好拦不住。门禁自检注入空 src 时报「这条分支是死的」
    # 才发现。全站 376 章现在 0 个空 src，收紧不会误伤。
    if not plain(c.get("src") or "").strip():
        bad.append("%s: empty src" % where)

# no sentence may appear in two chapters
seen = {}
for c in C.CHAPTERS:
    parts = [plain(c["story"]), plain(c["apply"])] + \
            [plain(f.get(k, "")) for f in c["f"] for k in ("d", "eg")] + \
            [plain(q) for q in c["q"]]
    for blob in parts:
        for x in re.split(r"(?<=[。！？\n])", blob):
            x = x.strip()
            if len(x) > 12:
                seen.setdefault(x, set()).add(c["n"])
for x, where in seen.items():
    if len(where) > 1:
        bad.append("repeated across %s: %s" % ("/".join(sorted(where)), x[:34]))

print("chapters: %d across %d parents" % (len(C.CHAPTERS), len(C.PARENTS)))
if bad:
    print("problems: %d" % len(bad))
    for b in bad:
        print("  -", b)
    sys.exit(1)
print("all checks pass")

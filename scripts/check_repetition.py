#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Same-page repetition audit. Run from the repo root.

Counts each visible text block exactly once: blockquotes are pulled out first so
their inner <p> is not also counted as a paragraph — doing it the naive way
reports one false positive per quote on the page.
"""
import os
import re
import sys
from collections import Counter

txt = lambda x: re.sub(r"<[^>]+>", "", x).strip()
worst, total, pages = [], 0, 0
root = sys.argv[1] if len(sys.argv) > 1 else "."
for dp, dn, fn in os.walk(os.path.join(root, "i")):
    if "index.html" not in fn:
        continue
    path = os.path.join(dp, "index.html")
    s = open(path, encoding="utf-8").read()
    if 'http-equiv="refresh"' in s or "<article>" not in s:
        continue
    b = s[s.index("<article>"):s.index("</article>")]
    blocks = [txt(m.group(1)) for m in re.finditer(r"<blockquote[^>]*>(.*?)</blockquote>", b, re.S)]
    rest = re.sub(r"<blockquote[^>]*>.*?</blockquote>", "", b, flags=re.S)
    for tag in ("p", "aside"):
        blocks += [txt(m.group(1)) for m in re.finditer(r"<%s[^>]*>(.*?)</%s>" % (tag, tag), rest, re.S)]
    blocks = [x for x in blocks if len(x) > 10]
    dup = {k: v for k, v in Counter(blocks).items() if v > 1}
    if dup:
        pages += 1
        n = sum(v - 1 for v in dup.values())
        total += n
        worst.append((n, path, sorted(dup.items(), key=lambda kv: -kv[1])[0]))
print("同页重复的可见文本块：%d 处，分布在 %d 个页面" % (total, pages))
for n, p, (t, c) in sorted(worst, reverse=True)[:10]:
    print("   %-42s %dx  %s" % (p, c, t[:40]))
sys.exit(1 if total else 0)

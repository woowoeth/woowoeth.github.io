#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""重新生成歧义字白名单（审阅记录）。

**跑这个之前先看 check_tw.py 报出来的新增条目**——这个脚本会把当前 tw/ 里
所有上下文一次性登记成「已审」，没看就跑等于把闸关掉。
正常流程是：改完内容 → build_tw → check_tw 报出新增的几条 → 人看一眼 → 跑这个。
"""
import os, re, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from tw_convert import contexts  # noqa: E402
ROOT = os.path.dirname(HERE)
TAG = re.compile(r"<script.*?</script>|<style.*?</style>", re.S)
cnt = collections.Counter()
for dp, dn, fn in os.walk(os.path.join(ROOT, "tw")):
    for f in fn:
        if f not in ("index.html", "404.html"):
            continue
        s = open(os.path.join(dp, f), encoding="utf-8").read()
        cnt.update(contexts(" ".join(re.findall(r">([^<>]+)<", TAG.sub("", s)))))
p = os.path.join(HERE, "tw_allow.txt")
old = [l for l in open(p, encoding="utf-8")] if os.path.exists(p) else []
hdr = "".join(l for l in old if l.startswith("#"))
open(p, "w", encoding="utf-8").write(hdr + "\n".join(sorted(cnt)) + "\n")
print("白名单 %d 条 → %s" % (len(cnt), os.path.relpath(p, ROOT)))

# -*- coding: utf-8 -*-
import os
import re

_PAT = re.compile(r"<p>\s*本页可直接引用\s*<code>[^<]*</code>\s*</p>\s*")

def strip_cite(root="."):
    n = 0
    base = os.path.join(root, "i")
    if not os.path.isdir(base):
        return 0
    for dirpath, _dirs, files in os.walk(base):
        if "index.html" not in files:
            continue
        path = os.path.join(dirpath, "index.html")
        src = open(path, encoding="utf-8").read()
        out = _PAT.sub("", src)
        if out != src:
            open(path, "w", encoding="utf-8").write(out)
            n += 1
    return n

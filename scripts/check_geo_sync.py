#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GEO 层同步门禁：建出来的页面，必须在 llms/feed/sitemap 里都能找到。

    python3 scripts/check_geo_sync.py

出过的事：英文站的 llms.txt / llms-full.txt / feed.xml 里**一个章节都没有**
—— 只有 30 个条目，而站上有 80 个章节，章节才是真正讲道理的那一层。
原因是 build_en 漏调了 hw_chapters.write_indexes()（中文那边调了）。

为什么没人发现：页面建出来了、sitemap 也有、链接也通，所有「页面在不在」
的检查全绿。GEO 层是给**模型**读的，不是给人读的 —— 人打开网站什么都正常，
而一个读 llms-full.txt 的模型看到的英文站只有 30 页内容。
这一层没人会顺手看一眼，所以必须有judge。

判据：每种语言的章节页数量，和它自己的 llms.txt / llms-full.txt / feed.xml
里出现的章节地址数量对得上（feed 里每章出现两次：link 和 guid）。
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CH_URL = re.compile(r"/i/[^/\s\"<)]+/[^/\s\"<)]+/")

SITES = [("简体", "", ""), ("繁体", "tw", "/tw"), ("英文", "en", "/en")]


def count_pages(prefix):
    root = os.path.join(ROOT, prefix, "i") if prefix else os.path.join(ROOT, "i")
    n = 0
    if not os.path.isdir(root):
        return 0
    for slug in os.listdir(root):
        d = os.path.join(root, slug)
        if not os.path.isdir(d):
            continue
        for k in os.listdir(d):
            if os.path.isfile(os.path.join(d, k, "index.html")):
                n += 1
    return n


def main():
    bad = []
    for label, prefix, _url in SITES:
        pages = count_pages(prefix)
        if not pages:
            continue
        for name, per in (("llms.txt", 1), ("llms-full.txt", 1), ("feed.xml", 2)):
            p = os.path.join(ROOT, prefix, name) if prefix else os.path.join(ROOT, name)
            if not os.path.exists(p):
                bad.append("%s 没有 %s" % (label, name))
                continue
            s = io.open(p, encoding="utf-8", errors="ignore").read()
            got = len(set(CH_URL.findall(s)))
            if got == 0:
                bad.append("%s 的 %s 里**一个章节都没有**（站上有 %d 章）"
                           "—— 多半是漏调了 hw_chapters.write_indexes()"
                           % (label, name, pages))
            elif got < pages:
                bad.append("%s 的 %s 只收了 %d 章，站上有 %d 章"
                           % (label, name, got, pages))
        print("  %s：章节页 %d" % (label, pages))

    if bad:
        print("\n不合格：")
        for x in bad:
            print("  ✗ " + x)
        return 1
    print("✓ 三种语言的章节都进了各自的 llms.txt / llms-full.txt / feed.xml")
    return 0


if __name__ == "__main__":
    sys.exit(main())

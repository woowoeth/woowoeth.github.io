#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""话题页在三种语言之间必须互相指到。

为什么单独一道闸：章节页三语同 slug，套个前缀就对；**话题页不是** ——
slug 由各自语言的标签名派生（中文「心智与情绪」→ /t/mind/，
英文 Mind and feeling → /en/t/mind-and-feeling/）。

2026-09-16 的后果（FAILURES #34）：英文话题页的 hreflang 指着
/t/<英文 slug>/ —— 404；中文那边反过来，根本没有 en 这一条。整组语言互链是断的。
「目标存不存在」那条判据（check_links）抓得住前一半，**抓不住后一半** ——
少写一条 en 不会报错，只是悄悄没了。所以要有这一条：**互指，而不只是不死。**

对应关系的唯一来源是 seo/topic_pairs.py（它从三张已有的表推，不另抄一份）。
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "seo"))
import topic_pairs                                    # noqa: E402

SITE = "https://ourword.ai"
ALT = re.compile(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)">')


def alts(rel):
    p = os.path.join(ROOT, rel, "index.html")
    if not os.path.isfile(p):
        return None
    return dict(ALT.findall(io.open(p, encoding="utf-8", errors="ignore").read()))


def main():
    bad, n = [], 0
    en_left, _zh_left = topic_pairs.missing(ROOT)
    for e in en_left:
        bad.append("英文话题 /en/t/%s/ 没有对应关系 —— 去 seo/en_names.py 或 en_ui.py 补译名" % e)
    for zs, es in sorted(topic_pairs.pairs().items()):
        want = {"zh-Hans": "%s/t/%s/" % (SITE, zs),
                "en": "%s/en/t/%s/" % (SITE, es),
                "zh-Hant": "%s/tw/t/%s/" % (SITE, zs),
                "x-default": "%s/t/%s/" % (SITE, zs)}
        for rel in ("t/%s" % zs, "en/t/%s" % es, "tw/t/%s" % zs):
            got = alts(rel)
            if got is None:
                continue                              # 这一语言没建这个话题，不算账
            n += 1
            for lang, url in want.items():
                if os.path.isdir(os.path.join(ROOT, url[len(SITE) + 1:])) and got.get(lang) != url:
                    bad.append("/%s/ 的 hreflang %s 是 %s，应为 %s"
                               % (rel, lang, got.get(lang) or "（没有）", url))
    if bad:
        print("\n  话题页多语言互指有问题 %d 处：" % len(bad))
        for b in bad[:12]:
            print("    ✗ " + b)
        return 1
    print("  话题页 %d 个（三语）互相指到，slug 按 seo/topic_pairs.py 的对应表" % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())

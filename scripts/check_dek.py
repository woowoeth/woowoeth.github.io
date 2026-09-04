#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""条目页导语门禁：三种语言都要收得住，且不许和正文重复。

    python3 scripts/check_dek.py

导语（<p class="dek">）的设计意图只有一句话：**留下认人的那半句，把后面
重复的部分裁掉**。it.summary 是「名字（年代）——关键词。」+ d 的前 140 字，
而 d 在几行之下会完整印一遍 —— 不裁的话全站有一万多字是同页重复。

出过的事：seo/hw_theme.py 的 _dek() 只认中文标点，找「——」和「。」。
英文的 summary 用的是单破折号「 — 」和半角句点「.」，两个都找不到，
于是**整块不裁**：英文条目页上露出的是 d[:140] 那个硬切口 ——
「… a cook and a provincial governor. He was banished」后面直接没了。
共用模板里写死 CJK 标点，就是这么只在另一种语言上发作的。

两条判据：
① 模板形制 —— 带「（年代）＋破折号」的那种导语（模板生成的），必须在
   破折号后的第一个句号处结束，后面一个字都不许有。
② 不重复 —— 认人那半句之后剩下的字，不许在同页别处出现。① 判形制，
   ② 判结果；② 还能抓住「正好切在句号上但还是重复了」这种。

判据里没有「必须以句号结尾」这一条：条目页的中文导语是**手写**的名词
短语（「把「这是谁的课题」问成一把刀的心理学家」），本来就不带句号。
第一版拿「收尾」当判据，一口气把 159 条里的手写导语全判成缺陷 ——
闸门判错的时候，先怀疑判据抄的是哪一种语言的习惯。
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

DEK = re.compile(r'<p class="dek">([^<]*)</p>')
TAGS = re.compile(r"<script.*?</script>|<style.*?</style>", re.S)
# 「认人那半句」在破折号后的第一个句号处结束。两套标点都算。
HEAD = re.compile(r"^.*?[—][^。.]*[。.]")
ERA = re.compile(r"[（(][^（()）]*\d{3,4}[^（()）]*[)）]")
DASH = re.compile(r"[—]")
DIRS = [("简体", "i"), ("繁体", os.path.join("tw", "i")), ("英文", os.path.join("en", "i"))]


def main():
    bad, n = [], 0
    for label, d in DIRS:
        root = os.path.join(ROOT, d)
        if not os.path.isdir(root):
            bad.append("%s 条目目录不存在：%s" % (label, d))
            continue
        for slug in sorted(os.listdir(root)):
            p = os.path.join(root, slug, "index.html")
            if not os.path.isfile(p):
                continue
            s = io.open(p, encoding="utf-8", errors="ignore").read()
            m = DEK.search(s)
            if not m:
                continue
            n += 1
            dek = m.group(1).strip()
            where = "%s /%s/%s/" % (label, d.replace(os.sep, "/"), slug)

            # ① 模板形制：有「（年代）」也有破折号的，就是模板生成的那种。
            #    手写导语不走这条 —— 它们没有年代括号。
            tpl = ERA.search(dek) and DASH.search(dek)
            h = HEAD.match(dek)
            if tpl and not h:
                bad.append("%s 模板导语里找不到「破折号 … 句号」这个形制：%s"
                           % (where, dek[:60]))
                continue
            if tpl and h and dek[h.end():].strip():
                bad.append("%s 模板导语没在破折号后的句号处收住：…%s"
                           % (where, dek[h.end():].strip()[:45]))
                continue

            # ② 认人那半句之后不许还有别处也有的字
            rest = dek[h.end():].strip() if h else ""
            if len(rest) >= 12:
                body = TAGS.sub("", s).replace(dek, "", 1)
                probe = rest[:40]
                if probe in body:
                    bad.append("%s 导语没裁：「%s…」同页别处也有"
                               % (where, probe[:30]))
        if len(bad) >= 8:
            break

    print("条目页导语：三种语言共 %d 条" % n)
    if bad:
        print("\n不合格：")
        for x in bad[:8]:
            print("  ✗ " + x)
        return 1
    print("✓ 模板导语都在破折号后的句号处收住，认人那半句之后没有同页重复的内容")
    return 0


if __name__ == "__main__":
    sys.exit(main())

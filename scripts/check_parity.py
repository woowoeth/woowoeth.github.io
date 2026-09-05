#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""三种语言的条目和章节必须一一对应。

    python3 scripts/check_parity.py

这一条补的是一个**空洞**：站里所有比对中英两版的判据，写法都是
「两边都有这一页时，比它们的内容」——

    if not (os.path.isfile(zp) and os.path.isfile(ep)):
        continue          # ← 中文有、英文没有的，从这里静默溜走

于是「英文少了一整篇」不会被任何一条判据点名，因为**没人知道它本该在**。
英文站一度只有 40 条而中文有 159 条，全部十六道闸绿着；那 119 条不是写坏了，
是从来没有任何一条判据要求过它们存在。（第 27、30 条是同一个形状的另外两次：
一层东西没有读者，坏了不会有人报。）

判据落在「有没有」上，不是「对不对」：
① 每个中文条目页 /i/<slug>/ 都要有 /en/i/<slug>/ 和 /tw/i/<slug>/。
② 每个中文章节页 /i/<slug>/<k>/ 都要有对应的英文页和繁体页。
③ 反过来也查：英文或繁体多出中文没有的页，那是没人维护的孤儿。

繁体是从简体转出来的，正常情况下自动一致；它一旦对不上，说明
build_tw 的跳过表漏了目录，值得当场知道。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def pages(base):
    """{slug: set(章key)}；base 不存在时返回空。"""
    out = {}
    d = os.path.join(ROOT, base, "i")
    if not os.path.isdir(d):
        return out
    for slug in sorted(os.listdir(d)):
        p = os.path.join(d, slug)
        if not os.path.isdir(p) or not os.path.exists(
                os.path.join(p, "index.html")):
            continue
        ks = {k for k in os.listdir(p)
              if os.path.isdir(os.path.join(p, k))
              and os.path.exists(os.path.join(p, k, "index.html"))}
        out[slug] = ks
    return out


def main():
    zh, en, tw = pages("."), pages("en"), pages("tw")
    bad = []

    for name, other in (("英文", en), ("繁体", tw)):
        miss = sorted(set(zh) - set(other))
        extra = sorted(set(other) - set(zh))
        if miss:
            bad.append("%s站缺 %d 个条目：%s%s"
                       % (name, len(miss), "、".join(miss[:6]),
                          " …" if len(miss) > 6 else ""))
        if extra:
            bad.append("%s站多出 %d 个中文没有的条目（孤儿页）：%s"
                       % (name, len(extra), "、".join(extra[:6])))
        n_ch = 0
        for slug in sorted(set(zh) & set(other)):
            mk = sorted(zh[slug] - other[slug])
            ek = sorted(other[slug] - zh[slug])
            if mk and len([x for x in bad if "缺章" in x]) < 6:
                bad.append("%s站 %s 缺章：%s" % (name, slug, "、".join(mk)))
            if ek and len([x for x in bad if "多章" in x]) < 6:
                bad.append("%s站 %s 多章（中文没有）：%s" % (name, slug, "、".join(ek)))
            n_ch += len(zh[slug])

    print("三语对应：中文 %d 条 / %d 章 · 英文 %d 条 · 繁体 %d 条"
          % (len(zh), sum(len(v) for v in zh.values()), len(en), len(tw)))
    if bad:
        print("\n不合格：")
        for b in bad[:14]:
            print("  ✗ " + b)
        if len(bad) > 14:
            print("  … 还有 %d 条" % (len(bad) - 14))
        return 1
    print("✓ 每个条目和章节在三种语言里都有，没有孤儿页")
    return 0


if __name__ == "__main__":
    sys.exit(main())

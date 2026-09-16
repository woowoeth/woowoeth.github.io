#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""话题页在三种语言之间怎么对应 —— 唯一的一份。

为什么要有这份：话题页的 slug 是 `slugify(标签名)` 派生的，而三种语言的标签名不同
（中文「心智与情绪」→ `/t/mind/`，英文 Mind and feeling → `/en/t/mind-and-feeling/`）。
两边只有各自 slugify 的结果，**没有任何东西记得它们是同一个话题** ——
2026-09-16 的后果就是 16 个英文话题页的 hreflang 指着 404（FAILURES #34）。

这份不另抄一张表，而是**从已有的三张表推**：

    seo/hw_slugs.py   TAG_SLUGS   中文标签 → 中文 slug
    seo/en_names.py   CATEGORY    中文标签 → 英文名（十个主题）
    seo/en_ui.py      UI          中文 → 英文（里面有六个时代分期）

好处是只有一处真相：谁加了新标签、改了译名，这里自动跟上；
译名漏了 `missing()` 当场点名，而不是等到线上 hreflang 指空。
繁体站的 slug 和简体一致，所以只需要中↔英这一组。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)


def _tables():
    import en_names
    import en_ui
    import hw_slugs
    zh2en = dict(en_names.CATEGORY)                  # 十个主题
    for zh, en in en_ui.UI:                          # 六个时代分期也在这张表里
        zh2en.setdefault(zh, en)
    return hw_slugs.TAG_SLUGS, zh2en, en_names.CATEGORY


def pairs():
    """{中文 slug: 英文 slug}。同一个中文 slug 有多个标签写法时，认主题表那一个。"""
    import geo_kit
    tag_slugs, zh2en, category = _tables()
    out, from_category = {}, set()
    for tag, zs in sorted(tag_slugs.items()):
        en = zh2en.get(tag)
        if not en:
            continue
        es = geo_kit.slugify(en)
        if zs in out and zs in from_category and tag not in category:
            continue                                 # 已有主题表给的答案，别被别名覆盖
        out[zs] = es
        if tag in category:
            from_category.add(zs)
    return out


def missing(root="."):
    """真建出来了、却没人给它对应关系的话题页。这就是欠账清单。"""
    m = pairs()
    zh = {d for d in os.listdir(os.path.join(root, "t"))
          if os.path.isdir(os.path.join(root, "t", d))} if os.path.isdir(os.path.join(root, "t")) else set()
    en = {d for d in os.listdir(os.path.join(root, "en", "t"))
          if os.path.isdir(os.path.join(root, "en", "t", d))} if os.path.isdir(os.path.join(root, "en", "t")) else set()
    # slug 两边一样的（medieval / modern / early-modern）本来就对得上
    same = zh & en
    paired_zh = set(m) | same
    paired_en = set(m.values()) | same
    return sorted(en - paired_en), sorted(zh - paired_zh)


if __name__ == "__main__":
    m = pairs()
    for a, b in sorted(m.items()):
        print("  /t/%-16s ↔ /en/t/%s" % (a, b))
    en_left, zh_left = missing(os.path.dirname(HERE))
    print("\n英文话题没有对应的：", en_left or "无")
    print("中文话题没有对应的：%d 个（多是历史遗留的重复目录）" % len(zh_left))

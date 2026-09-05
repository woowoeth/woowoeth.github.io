#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按正确顺序跑完整条构建链。

    python3 scripts/build_all.py

顺序不是随便排的，每一步的位置都有原因，而且**排错过两次**：

  1 patch_geo_seo      GEO 附加项
  2 apply_redesign     条目页独立成页
  3 build_seo          SEO/GEO 产物、条目页、章节页
  4 force_chapter_ui   往简体页上盖挂件（第一遍）
  5 build_en           英文站：条目页、章节页、首页
  6 force_chapter_ui   再盖一遍（第二遍）
  7 build_chat_index   聊天检索索引
  8 build_tw           繁体站，整树转出

为什么 force_chapter_ui 要跑两遍 —— 这两步互相依赖：

  · build_en 要从一个**已构建的**简体页上把夜间模式挂件整块搬过去，
    所以它得排在第一遍之后。
  · force_chapter_ui 的 hreflang 要知道「哪些页有英文版」，而那个集合读的是
    真实的 en/ 树，所以它得排在 build_en 之后。

只跑一遍的后果实测过两次：第一次 hreflang 整批漏掉 en（英文站还没建），
第二次首页宣称有英文版而 /en/ 其实不存在，英文语系的浏览器被 location.replace
弹到一个 404 —— 而门禁报出来的是「#hwx-tabs2 是 undefined」，看着毫不相干。
force_chapter_ui 是幂等的（重跑零改动，验过），所以跑两遍只是多花几秒。

build_tw 必须最后：繁体站是拿构建好的简体树整树转出来的，排在任何生成步骤
之前，转出来的就是上一次的旧内容。
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CHAIN = [
    ("GEO 附加项", "scripts/patch_geo_seo.py"),
    ("条目页独立成页", "scripts/apply_redesign.py"),
    ("SEO/GEO 产物", "seo/build_seo.py"),
    ("简体挂件（第一遍）", "scripts/force_chapter_ui.py"),
    ("英文站", "scripts/build_en.py"),
    ("简体挂件（第二遍，此时才知道哪些页有英文版）", "scripts/force_chapter_ui.py"),
    ("聊天检索索引", "scripts/build_chat_index.py"),
    # 挂件的繁体文案由简体文案生成。放在繁体站之前：assets/hw-chat.js 是
    # 三个语言站共用的静态资源，build_tw 只转 tw/ 下的文件、转不到它。
    ("聊天挂件繁体文案", "scripts/gen_chat_tw.py"),
    ("繁体站", "scripts/build_tw.py"),
    # 盖章必须在**所有**站都构建完之后：它扫的是最终产物，
    # 中英繁三个站里任何一处的 /assets/ 引用都要盖到。
    ("资源版本号盖章", "scripts/stamp_assets.py"),
]


def main():
    for i, (name, script) in enumerate(CHAIN, 1):
        print("\n[%d/%d] %s  —  %s" % (i, len(CHAIN), name, script))
        r = subprocess.run([sys.executable, script], cwd=ROOT)
        if r.returncode:
            print("✗ 第 %d 步失败：%s" % (i, script))
            return r.returncode
    print("\n✓ 构建链跑完。接着跑 python3 scripts/gate.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())

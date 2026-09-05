#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把首页里那两大块**数据**搬到外部文件，让每天变的那份页面变小。

    python3 scripts/split_home_data.py

量出来的事实（2026-09-06）：首页 index.html 2182 KB / gzip 782 KB，
其中 94% 是内联 <script>，而里面两块是纯数据：

    var HWXD  = {…}   1276 KB (gzip 404)  就压在 <body> 后 5% 处
    const D   = […]    716 KB (gzip 306)

而 HTML 的缓存是 `max-age=600` —— **超过十分钟再打开，782 KB 重下一遍**。
数据其实很少变（只有上新内容时才变），页面外壳每天都在变，两者焊在一起，
于是不变的那 700 KB 跟着天天变的外壳一起重下。

搬出去之后：外壳约 gzip 75 KB，数据文件由 scripts/stamp_assets.py 按内容
哈希盖章 —— 内容不变 URL 就不变，浏览器不会再下第二次。

**只搬 HWXD，不搬 `const D`。** 后者虽然也有 306 KB(gzip)，但它是**手写内容**，
而且是四个构建脚本的输入（apply_redesign / gen_map / inject_week / build_en
都从 index.html 里读 `const D=[`）。把它搬走等于改掉「上新内容时改哪个文件」，
风险和收益不成比例。它留在原地。

**index.html 既是产物又是输入**，所以这个脚本有两个方向：
构建**开始**时 `--inline` 把数据装回页面里，构建**结束**时再拆出去。
中间那九步一个字都不用改 —— 它们看到的永远是老样子。
（第一版只做了拆，结果下一轮构建第 2 步就报「const D=[ not found」：
拆出去的东西成了下一轮的输入。）

**为什么用普通 <script src> 而不是 defer/async：** 普通脚本是同步、按序执行的，
和内联时的语义完全一样 —— 后面那些内联脚本仍然能在自己那一行拿到数据。
用 defer 会让它跑到所有内联脚本之后，页面当场坏掉。

**为什么不影响 SEO / GEO：**
- 页面上的可见 HTML 一个字没动；
- <script type="application/ld+json"> 那块结构化数据仍然内联，原样留在页面里；
- 搜索引擎执行 JS，外部脚本照样执行、内容照样渲染出来；
- llms.txt / llms-full.txt / feed.xml / sitemap.xml 是另外的文件，根本没碰。

**必须在 build_tw 之后跑。** 繁体页是从简体页转出来的：先拆的话，
tw/index.html 会指向 assets/ 下那份**简体**数据，繁体站当场变简体。
放在后面，繁体从它自己那份已经转好的页面里取数据，写进 tw/assets/。
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# (页面, 数据文件相对仓库根的路径, 页面里写的 src)
TARGETS = [
    ("index.html", "assets", ""),
    ("tw/index.html", "tw/assets", "/tw"),
    # 英文页引的是共用的 /assets/，所以只能靠文件名区分
    ("en/index.html", "assets", ""),
]
BLOCKS = [("home-hwxd", re.compile(r"^\s*var\s+HWXD\s*="))]
SCRIPT = re.compile(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", re.S)


def inline():
    """把数据装回页面里 —— 构建开始时跑。

    index.html 既是产物又是输入：build_en 要从它里面读 `var HWXD={`，
    apply_redesign 要读 `const D=[`。拆出去的页面直接喂给下一轮构建，
    第 2 步就会报「找不到」。所以拆完的状态只在提交里存在，
    构建一开始先还原。
    """
    n = 0
    for page, assets_dir, prefix in TARGETS:
        p = os.path.join(ROOT, page)
        if not os.path.exists(p):
            continue
        s = io.open(p, encoding="utf-8").read()
        suffix = "-en" if page.startswith("en/") else ""
        for name, _pat in BLOCKS:
            fn = "%s%s.js" % (name, suffix)
            src = "%s/%s/%s" % (prefix, assets_dir.split("/")[-1], fn)
            tag = re.search(r'<script src="%s(\?v=[A-Za-z0-9.]*)?"></script>'
                            % re.escape(src), s)
            if not tag:
                continue
            f = os.path.join(ROOT, assets_dir, fn)
            if not os.path.exists(f):
                print("✗ %s 指向 %s，但那个文件不在" % (page, src))
                return 1
            body = io.open(f, encoding="utf-8").read().strip()
            s = s[:tag.start()] + "<script>" + body + "</script>" + s[tag.end():]
            n += 1
        io.open(p, "w", encoding="utf-8").write(s)
    print("首页数据：装回页面 %d 处（构建期间用）" % n)
    return 0


def main():
    total_before = total_after = 0
    for page, assets_dir, prefix in TARGETS:
        p = os.path.join(ROOT, page)
        if not os.path.exists(p):
            print("跳过（没有这一页）：%s" % page)
            continue
        s = io.open(p, encoding="utf-8").read()
        total_before += len(s.encode())
        suffix = "-en" if page.startswith("en/") else ""
        moved = []
        for name, pat in BLOCKS:
            hit = None
            for m in SCRIPT.finditer(s):
                if pat.match(m.group(1)):
                    hit = m
                    break
            if hit is None:
                # 已经搬过了（构建链会重跑），或者页面结构变了。
                # 两种都不该静默 —— 后者是真事故。
                fn = "%s%s.js" % (name, suffix)
                if os.path.exists(os.path.join(ROOT, assets_dir, fn)):
                    continue
                print("✗ %s 里找不到 %s 那一块，也没有已经搬好的文件"
                      % (page, name))
                return 1
            fn = "%s%s.js" % (name, suffix)
            out = os.path.join(ROOT, assets_dir, fn)
            io.open(out, "w", encoding="utf-8").write(hit.group(1).strip() + "\n")
            tag = '<script src="%s/%s/%s"></script>' % (prefix, assets_dir.split("/")[-1], fn)
            s = s[:hit.start()] + tag + s[hit.end():]
            moved.append("%s→%s/%s" % (name, assets_dir, fn))
        if moved:
            io.open(p, "w", encoding="utf-8").write(s)
        total_after += len(s.encode())
        print("%-16s %5d KB → %4d KB   %s"
              % (page, (len(io.open(p, encoding='utf-8').read().encode()) +
                        sum(os.path.getsize(os.path.join(ROOT, assets_dir,
                            "%s%s.js" % (n, suffix))) for n, _ in BLOCKS)) // 1024,
                 len(s.encode()) // 1024, "、".join(moved) or "（已经是搬好的）"))
    if total_before:
        print("首页外壳合计：%d KB → %d KB"
              % (total_before // 1024, total_after // 1024))
    return 0


if __name__ == "__main__":
    sys.exit(inline() if "--inline" in sys.argv else main())

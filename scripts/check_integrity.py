#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全站完整性闸门。

这个脚本收的都是本次会话里真实发生过、且当时没被任何检查拦住的错误：

  1. 加了条目却没写章节 —— 条目页没有「深度阅读」，也进不了「最新」
  2. 加了条目却没写手写介绍 —— 首页卡片回落到简介首句
  3. 加了章节却没生成分享图 —— 分享出去还是全站通用图
  4. 关联字段指向尚未收录的条目 —— 生成死链
  5. 新类别条目数不足却进了 slug 表 —— 主题页不生成，链接悬空
  6. 条目没有英文 slug —— 生成中文路径 URL
  7. 二维码被换坏 —— 页脚和分享卡的码扫不出来

每一条都曾经是「我以为做完了」。现在改成构建失败。
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, "seo")
sys.path.insert(0, "scripts")

import build_seo          # noqa: E402
import hw_chapters as C   # noqa: E402
import hw_slugs           # noqa: E402

problems = []


def bad(kind, detail):
    problems.append("%s: %s" % (kind, detail))


entries = build_seo.load_array()
names = {e["n"] for e in entries}
parents = {c["parent"] for c in C.CHAPTERS}

# 1) 每个条目至少一篇深度阅读
for e in entries:
    if e["n"] not in parents:
        bad("条目无深度阅读", e["n"])

# 2) 每个条目有手写介绍
try:
    src = open("scripts/force_chapter_ui.py", encoding="utf-8").read()
    seg = src[src.index("HWX_INTROS = {"):]
    seg = seg[:seg.index("\n}") + 2]
    ns = {}
    exec(seg, ns)
    intros = ns["HWX_INTROS"]
except Exception as exc:                      # pragma: no cover
    intros = {}
    bad("读取 HWX_INTROS 失败", exc)
for e in entries:
    slug = hw_slugs.slug_for(e["n"])
    if slug not in intros:
        bad("条目无手写介绍", "%s (%s)" % (e["n"], slug))

# 3) 每篇章节有专属分享图
for ch in C.CHAPTERS:
    png = os.path.join("i", hw_slugs.slug_for(ch["parent"]), ch["k"], "og.png")
    if not os.path.exists(png):
        bad("章节无分享图", png)

# 4) 关联字段只能指向已收录的条目（前向引用会生成死链）
home = open("index.html", encoding="utf-8").read()
for ref in set(re.findall(r'\{n:"([^"]+)",why:', home)):
    if ref not in names:
        bad("contrast 指向未收录条目", ref)
for block in re.findall(r'l:\[([^\]]*)\]', home):
    for ref in re.findall(r'"([^"]+)"', block):
        if ref not in names:
            bad("l 指向未收录条目", ref)

# 5) 类别要么条目数达标、要么不进 slug 表（否则主题页不生成，链接悬空）
HUB_MIN = 3
counts = {}
for e in entries:
    counts[e["c"]] = counts.get(e["c"], 0) + 1
tag_slugs = getattr(hw_slugs, "TAG_SLUGS", {})
for cat, n in counts.items():
    if cat in tag_slugs and n < HUB_MIN:
        bad("类别进了 slug 表但条目不足",
            "%s 只有 %d 个，需要 %d" % (cat, n, HUB_MIN))

# 6) 条目必须有英文 slug
for e in entries:
    slug = hw_slugs.slug_for(e["n"])
    if re.search(r"[\u4e00-\u9fff]", slug or ""):
        bad("条目无英文 slug", "%s → %s" % (e["n"], slug))

# 7) 信息流里同类卡片不得重复
#    真实事故：金句取用写成 (i*53) % 池大小，而池子正好 53 条，
#    于是两个 feed 里所有金句卡都是同一句。用浏览器跑一遍实际渲染来验。
def check_feed_dupes():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("（跳过信息流查重：无 playwright）")
        return
    import subprocess, time
    srv = subprocess.Popen(["python3", "-m", "http.server", "8971"], cwd=ROOT,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2.5)
    try:
        with sync_playwright() as pw:
            b = pw.chromium.launch()
            pg = b.new_page(viewport={"width": 390, "height": 1200})
            pg.goto("http://localhost:8971/", timeout=30000)
            pg.wait_for_timeout(1800)
            for tab, sel in (("最新", "#hwx-ncfeed"), ("全部", "#hwx-feed")):
                if tab == "全部":
                    pg.evaluate("()=>document.querySelectorAll('#hwx-tabs2 button')[1].click()")
                    pg.wait_for_timeout(800)
                got = pg.evaluate("""(s)=>{var o={};
                  ['.qc','.pc','.nc','.kc'].forEach(function(k){
                    o[k]=Array.from(document.querySelectorAll(s+' '+k))
                          .map(function(e){return (e.innerText||'').slice(0,40)})});
                  return o}""", sel)
                for kind, texts in got.items():
                    if len(texts) > 1 and len(set(texts)) < len(texts):
                        from collections import Counter
                        worst = Counter(texts).most_common(1)[0]
                        bad("信息流卡片重复",
                            "%s tab 的 %s：%d 张里只有 %d 种，最多的一张出现 %d 次"
                            % (tab, kind, len(texts), len(set(texts)), worst[1]))
            b.close()
    finally:
        srv.terminate()


check_feed_dupes()

# 8) 二维码必须仍可解码
try:
    from PIL import Image
    from pyzbar.pyzbar import decode
    got = [x.data.decode() for x in decode(Image.open("wechat-qr.png"))]
    if not got:
        bad("二维码扫不出", "wechat-qr.png")
    elif "weixin.qq.com" not in got[0]:
        bad("二维码指向异常", got[0])
except ImportError:
    print("（跳过二维码检查：缺 pyzbar/PIL）")
except Exception as exc:
    bad("二维码读取失败", exc)

print("条目 %d / 章节 %d / 覆盖 %d 个条目" % (len(entries), len(C.CHAPTERS), len(parents)))
if problems:
    print("完整性问题 %d 处：" % len(problems))
    for p in problems[:40]:
        print("  - " + p)
    sys.exit(1)
print("完整性检查全部通过 ✅")

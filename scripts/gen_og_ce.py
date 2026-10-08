#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""画 ce/og.png（1200×630）——「测测你的历史分身」被转发时的预览图。

和 gen_og.py 一样是静态资产、不进构建链：改了人物或文案才重画一次，画好的图提交进仓库。
用 playwright 渲染一张 HTML（要本机的宋体/苹方），所以只在本地跑。
    python3 scripts/gen_og_ce.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "seo"))
import ce_data as D  # noqa: E402

PICK = ["项羽", "张良", "苏轼", "徐霞客", "武则天", "诸葛亮", "拿破仑"]   # 一行放得下：两行会顶到页脚


def html():
    fam = {}
    for t in D.TYPES:
        fam[t["who"]] = D.FAMILIES[(t["code"][0], t["code"][2])]["color"]
    chips = "".join('<span style="color:%s;border-color:%s">%s</span>' % (fam[n], fam[n], n) for n in PICK)
    return """<html><head><meta charset="utf-8"><style>
body{margin:0;width:1200px;height:630px;background:#f5f1e8;font-family:-apple-system,"PingFang SC",sans-serif;color:#1f1c17}
.f{position:absolute;inset:28px;border:3px solid #d8d2c6}
.eb{position:absolute;left:96px;top:92px;font-size:22px;letter-spacing:.32em;color:#a33b2e;font-weight:600}
h1{position:absolute;left:92px;top:130px;margin:0;font:700 112px/1.15 "Noto Serif SC","Songti SC",serif;letter-spacing:.04em}
.sub{position:absolute;left:96px;top:282px;font-size:34px;color:#8a8377}
.chips{position:absolute;left:96px;right:96px;top:372px;display:flex;flex-wrap:wrap;gap:14px}
.chips span{font:600 30px "Noto Serif SC","Songti SC",serif;border:2px solid;border-radius:999px;padding:6px 20px;background:#faf7f0}
.ft{position:absolute;left:96px;bottom:70px;display:flex;align-items:center;gap:18px;font-size:28px;color:#8a8377}
.seal{width:58px;height:58px;background:#a33b2e;color:#fff;display:flex;align-items:center;justify-content:center;font:700 38px "Noto Serif SC","Songti SC",serif;border-radius:6px}
</style></head><body><div class="f"></div>
<div class="eb">YOUR HISTORICAL TWIN</div><h1>测测你的历史分身</h1>
<div class="sub">20 道遇事题 · 2 分钟 · 32 种历史人格</div>
<div class="chips">%s</div>
<div class="ft"><div class="seal">人</div>ourword.ai/ce · 每一种结果都链到他当年的真事</div>
</body></html>""" % chips


def main():
    from playwright.sync_api import sync_playwright
    out = os.path.join(ROOT, "ce", "og.png")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1200, "height": 630})
        pg.set_content(html())
        pg.wait_for_timeout(300)
        pg.screenshot(path=out)
        b.close()
    print("画好了 %s" % os.path.relpath(out, ROOT))


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""把 seo/figs/*.svg 渲成透明 PNG（2x，560px 宽），放 seo/figs/_png/，给分享图 gen_og.py 用。

SVG 的颜色全走 CSS 变量，脱离页面就没有颜色，所以借 Chromium 带着站上的样式表渲一遍。
手动跑：先在仓库根起 python3 -m http.server 8899，再 python3 scripts/render_figs.py。
只在改了某张 SVG 之后需要重跑；产物随仓库提交。"""
import glob, os, time, pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "seo" / "figs" / "_png"
OUT.mkdir(exist_ok=True)
figs = sorted(glob.glob(str(ROOT / "seo" / "figs" / "*.svg")))
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 700, "height": 600}, device_scale_factor=2)
    for f in figs:
        name = os.path.basename(f)[:-4]
        pg.set_content(
            '<link rel="stylesheet" href="http://localhost:8899/assets/hw-entry.css?cb=%d">'
            '<style>body{background:transparent!important;margin:0}'
            '.hw-fig{max-width:none!important;width:560px;margin:0!important}</style>'
            '<figure class="hw-fig">%s</figure>' % (time.time(), open(f, encoding="utf-8").read()))
        pg.wait_for_timeout(250)
        pg.locator(".hw-fig").screenshot(path=str(OUT / (name + ".png")), omit_background=True)
        print("rendered", name)
    b.close()

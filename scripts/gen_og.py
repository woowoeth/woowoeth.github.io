# -*- coding: utf-8 -*-
"""为每篇章节生成 1200x630 分享图（标题 + 金句排版），输出到 i/<slug>/<k>/og.png。

不挂 CI：图片是一次性生成的静态资产，随仓库提交。新增章节后手动重跑本脚本；
没有 og.png 的章节页会自动回落到全站图（见 force_chapter_ui.patch_chapter_og）。
Pillow 的 PNG 输出不含时间戳，同输入必同输出，不破坏幂等。
"""
import re, sys, pathlib
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "seo"))
import hw_chapters as C, hw_slugs

W, H, M = 1200, 630, 72
PAPER, INK, ACC, MUTED, LINE = "#f5f1e8", "#1f1c17", "#a33b2e", "#8a8377", "#d8d2c6"
# 字体：首选 Noto Serif CJK SC Bold —— 已有 276 张图都是它画的，换字体会让新旧图
# 明显不是一套。本机（macOS）没有它，只能退到 Songti SC Bold；这时脚本自动切到
# 「只补缺失」模式，绝不重画已有的图。要重画全部，必须在装了 Noto 的机器上跑。
CANDIDATES = [
    ("/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc", 2, True),   # Linux，正统
    ("/usr/share/fonts/opentype/noto/NotoSerifCJK.ttc", 2, True),
    ("/System/Library/Fonts/Supplemental/Songti.ttc", 1, False),         # macOS，替补
]
TTC = INDEX = None
CANONICAL = False
for _p, _i, _ok in CANDIDATES:
    if pathlib.Path(_p).exists():
        TTC, INDEX, CANONICAL = _p, _i, _ok
        break
if TTC is None:
    sys.exit("找不到可用的 CJK 衬线字体，候选：\n  " + "\n  ".join(c[0] for c in CANDIDATES))
F = lambda size: ImageFont.truetype(TTC, size, index=INDEX)

def wrap(draw, text, font, maxw):
    lines, cur = [], ""
    for ch in text:
        if draw.textlength(cur + ch, font=font) <= maxw:
            cur += ch
        else:
            lines.append(cur); cur = ch
    if cur: lines.append(cur)
    return lines

def render(title, sub, quote, out):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # 顶部品牌行
    fb = F(25)
    d.text((M, 52), "人类世界生存法则 · ourword.ai", font=fb, fill=MUTED)
    tag = "深度阅读"
    d.text((W - M - d.textlength(tag, font=fb), 52), tag, font=fb, fill=ACC)
    d.line([(M, 104), (W - M, 104)], fill=LINE, width=2)
    # 标题（人名 · 章节名），过长缩字号并换行
    ft = F(56)
    tl = wrap(d, title, ft, W - 2 * M)
    if len(tl) > 2:
        ft = F(46); tl = wrap(d, title, ft, W - 2 * M)[:2]
    y = 146
    for ln in tl:
        d.text((M, y), ln, font=ft, fill=INK)
        y += int(ft.size * 1.32)
    # 副题 w
    fs = F(27)
    d.text((M, y + 8), sub, font=fs, fill=MUTED)
    # 金句块：底部锚定，红竖线
    fq = F(33)
    q = "「" + quote + "」"
    ql = wrap(d, q, fq, W - 2 * M - 30)
    if len(ql) > 3:
        ql = ql[:3]
        ql[-1] = ql[-1][:-2] + "…」"
    lh = int(fq.size * 1.62)
    qh = lh * len(ql)
    qy = H - 88 - qh
    d.rectangle([M, qy + 6, M + 6, qy + qh - 6], fill=ACC)
    for i, ln in enumerate(ql):
        d.text((M + 30, qy + i * lh), ln, font=fq, fill=INK)
    img.convert("P", palette=Image.ADAPTIVE, colors=96).save(out, optimize=True)

def main():
    only_missing = ("--all" not in sys.argv) if CANONICAL else True
    if not CANONICAL:
        print("⚠ 用的是替补字体 %s（正统的 Noto Serif CJK 不在本机）。" % TTC)
        print("  已自动切到「只补缺失」，不会重画已有的图——新图与旧图字形会有差异，")
        print("  要统一请在装了 Noto Serif CJK 的机器上跑 python3 scripts/gen_og.py --all。")
    n, skipped, total = 0, 0, 0
    for ch in C.CHAPTERS:
        slug = hw_slugs.slug_for(ch["parent"])
        out = ROOT / "i" / slug / ch["k"] / "og.png"
        if not out.parent.exists():
            print("跳过（页面目录不存在）:", out.parent); continue
        if only_missing and out.exists():
            skipped += 1; continue
        # 选 q[] 中最长的一条：短句常与标题重复，撑不起版面
        qs = [re.sub(r"==", "", q).strip().rstrip("。") for q in (ch.get("q") or [""])]
        quote = max(qs, key=len)
        render("%s · %s" % (ch["parent"], ch["n"]), ch.get("w", ""), quote, out)
        n += 1; total += out.stat().st_size
    print("生成 %d 张（跳过已存在 %d 张），共 %.1f MB" % (n, skipped, total / 1048576))

if __name__ == "__main__":
    main()

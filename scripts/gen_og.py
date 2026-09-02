# -*- coding: utf-8 -*-
"""分享图（og:image）：章节 364 张、人物 155 张、首页 1 张，都是 1200x630。

这张图给的是还没点开链接的那个人看的，判据是「点不点」，所以：
- 卡片给问题，页面给论断：大字是 dek 里那句处境问题，不是「人名 · 章名」——那是网页标题的事。
- 关键信息全排进中央 630x630 的安全区：微信等聊天窗把预览裁成方形，裁完不能缺字。
- 15 章带示意图的，图进卡片（图影响的正是点不点）；其余放一句金句。
- logo 用站上那枚红色「人」印（icon-512.png）。

字体：本机 Songti SC。以前 276 张 Noto、88 张 Songti 混着，这一版全部重画统一成 Songti；
Linux 上没有 Songti 就退到 Noto，但只补缺失、不重画已有的，免得再混。
不挂 CI：静态资产随仓库提交，新增章节/人物后手动重跑。Pillow 的 PNG 无时间戳，同输入同输出。
示意图的 PNG 由 scripts/render_figs.py 预先渲好放在 seo/figs/_png/。
"""
import re, sys, pathlib
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "seo"))
import hw_chapters as C, hw_slugs
from build_seo import load_array

W, H = 1200, 630
X0, X1 = 285, 915            # 中央方形安全区
PAD = 34
TX0, TX1 = X0 + PAD, X1 - PAD
TW = TX1 - TX0               # 562
PAPER, INK, INK2, MUTED, SEAL, RULE = "#f5f1e8", "#1c1917", "#3f3a34", "#6f6959", "#9d2933", "#e2ddd0"
FIGPNG = ROOT / "seo" / "figs" / "_png"

# (粗体文件, 粗体 index, 细体文件, 细体 index, 是否正统)
FONTS = [
    ("/System/Library/Fonts/Supplemental/Songti.ttc", 1, "/System/Library/Fonts/Supplemental/Songti.ttc", 3, True),
    ("/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc", 2, "/usr/share/fonts/opentype/noto/NotoSerifCJK.ttc", 2, False),
]
_font = next((f for f in FONTS if pathlib.Path(f[0]).exists() and pathlib.Path(f[2]).exists()), None)
if _font is None:
    sys.exit("找不到可用的 CJK 衬线字体")
CANONICAL = _font[4]


def F(kind, size):
    path, idx = (_font[0], _font[1]) if kind == "b" else (_font[2], _font[3])
    return ImageFont.truetype(path, size, index=idx)


ICON = Image.open(ROOT / "icon-512.png").convert("RGBA")


def wrap(d, text, font, maxw):
    lines, cur = [], ""
    for ch in text:
        if d.textlength(cur + ch, font=font) <= maxw:
            cur += ch
        else:
            lines.append(cur); cur = ch
    if cur:
        lines.append(cur)
    return lines


def clip(lines, n):
    if len(lines) <= n:
        return lines
    lines = lines[:n]
    lines[-1] = lines[-1][:-1] + "…"
    return lines


def first_sentence(dek):
    s = re.split(r"(?<=[。？！])", re.sub("==", "", dek or "").strip())[0].strip()
    return s if 6 <= len(s) <= 36 else None


def base(tag):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    ic = ICON.resize((52, 52), Image.LANCZOS)
    img.paste(ic, (TX0, 46), ic)
    d.text((TX0 + 66, 57), "人类世界生存法则", font=F("b", 24), fill=INK)
    ft = F("b", 21)
    d.text((TX1 - d.textlength(tag, font=ft), 61), tag, font=ft, fill=SEAL)
    d.line([(72, 118), (W - 72, 118)], fill=RULE, width=2)
    return img, d


def headline(d, text, y, max_lines=3):
    for size in (46, 42, 38):
        f = F("b", size)
        lines = wrap(d, text, f, TW)
        if len(lines) <= max_lines:
            break
    for ln in clip(lines, max_lines):
        d.text((TX0, y), ln, font=f, fill=INK)
        y += int(size * 1.36)
    return y


def bottom_quote(d, text, size=26, lines=2, fill=INK2):
    fq = F("l", size)
    ql = clip(wrap(d, text, fq, TW - 26), lines)
    lh = int(size * 1.6)
    qh = lh * len(ql)
    qy = H - 70 - qh
    d.rectangle([TX0, qy + 5, TX0 + 5, qy + qh - 5], fill=SEAL)
    for i, ln in enumerate(ql):
        d.text((TX0 + 26, qy + i * lh), ln, font=fq, fill=fill)
    return qy


def save(img, out):
    out.parent.mkdir(parents=True, exist_ok=True)
    img.convert("P", palette=Image.ADAPTIVE, colors=128).save(out, optimize=True)


def render_chapter(ch, out):
    img, d = base("深度阅读")
    y = headline(d, first_sentence(ch["dek"]) or ch["n"], 150)
    d.text((TX0, y + 14), "%s · %s" % (ch["parent"], ch["n"]), font=F("b", 26), fill=SEAL)
    y_after = y + 14 + 36
    fig = next((f.get("fig") for f in ch["f"] if f.get("fig")), None)
    if fig and (FIGPNG / (fig + ".png")).exists():
        im = Image.open(FIGPNG / (fig + ".png")).convert("RGBA")
        scale = min(TW / im.width, ((H - 52) - (y_after + 22)) / im.height)
        if scale * im.width >= 300:
            nw, nh = int(im.width * scale), int(im.height * scale)
            im = im.resize((nw, nh), Image.LANCZOS)
            img.paste(im, (TX0 + (TW - nw) // 2, H - 52 - nh), im)
            save(img, out); return
    qs = [re.sub("==", "", q).strip().rstrip("。") for q in (ch.get("q") or [""])]
    bottom_quote(d, max(qs, key=len))
    save(img, out)


def render_person(e, slug, out):
    img, d = base("人物")
    y = 150
    d.text((TX0, y), e["n"], font=F("b", 60), fill=INK); y += 78
    d.text((TX0, y), e.get("e", ""), font=F("l", 24), fill=MUTED); y += 46
    for ln in clip(wrap(d, e.get("w", ""), F("b", 30), TW), 2):
        d.text((TX0, y), ln, font=F("b", 30), fill=SEAL); y += 42
    P = C.PARENTS.get(slug) or C.PARENTS.get(e["n"]) or {}
    items = [it.get("n", "") for it in (P.get("items") if isinstance(P, dict) else []) or [] if it.get("ready", True)]
    bottom_quote(d, " · ".join(items) if items else (e.get("q") or [""])[0], size=24, lines=2, fill=INK2)
    save(img, out)


def render_home(out):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    ic = ICON.resize((104, 104), Image.LANCZOS)
    # 印章离分割线 62px，整块（印章 + 标题 + 口号）在竖向居中
    img.paste(ic, (TX0, 180), ic)
    d.text((TX0, 312), "人类世界生存法则", font=F("b", 60), fill=INK)
    d.text((TX0, 404), "遇到事了，看看以前的人怎么处理", font=F("l", 30), fill=INK2)
    d.line([(72, 118), (W - 72, 118)], fill=RULE, width=2)
    d.text((TX0, 57), "ourword.ai", font=F("b", 24), fill=MUTED)
    save(img, out)


def main():
    only_missing = (not CANONICAL) or ("--only-missing" in sys.argv)
    if not CANONICAL:
        print("⚠ 非正统字体（本机没有 Songti SC），只补缺失、不重画已有的图。")
    n = skipped = 0
    for ch in C.CHAPTERS:
        out = ROOT / "i" / ch["parent_slug"] / ch["k"] / "og.png"
        if not out.parent.exists():
            print("跳过（页面目录不存在）:", out.parent); continue
        if only_missing and out.exists():
            skipped += 1; continue
        render_chapter(ch, out); n += 1
    m = 0
    for e in load_array(str(ROOT / "index.html"), "D"):
        slug = hw_slugs.slug_for(e["n"])
        out = ROOT / "i" / slug / "og.png"
        if not out.parent.exists():
            continue
        if only_missing and out.exists():
            skipped += 1; continue
        render_person(e, slug, out); m += 1
    render_home(ROOT / "og.png")
    print("章节 %d 张、人物 %d 张、首页 1 张（跳过已存在 %d 张）" % (n, m, skipped))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英文站的分享图（og:image）：章节、条目、首页各一张，1200x630。

    python3 scripts/gen_og_en.py [--only-missing]

为什么单独一份：中文那份 scripts/gen_og.py 的排版是照汉字写的 ——
`wrap()` 逐**字**折行（汉字每个字都能断，英文单词不能）、字体是宋体、
站名是「人类世界生存法则」。这里复用它的画布、配色、安全区和落盘，只换三样：
按**词**折行、Georgia（本机有；Playfair 只在网页端走 Google Fonts，PIL 拿不到）、
站名 OurWord。

为什么必须有：英文站 555 页此前全部共用站根那一张 og.png —— 任何一页转发出去
都长得一样，读者在聊天窗里分不清转的是哪一篇。中文那边每页一张。
这是「没有读者的那一层坏了没人报」的形状（FAILURES 第 27、30 条）：页面正常、
链接正常、只有转发出去才看得见。

输出：en/i/<slug>/<k>/og.png · en/i/<slug>/og.png · en/og.png
配套：hw_chapters 给英文页写的 og:image 必须指向这些文件（不是站根），
scripts/check_en.py 查每一页的 og:image 是不是它自己的。
"""
import os
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
os.environ["HW_CHAPTERS"] = "chapters_en"          # 让 hw_chapters 装英文章节
sys.path.insert(0, str(ROOT / "seo"))
sys.path.insert(0, str(HERE))

from PIL import Image, ImageDraw, ImageFont          # noqa: E402
import gen_og as G                                   # noqa: E402  画布/配色/安全区/save 全部复用
import hw_chapters as C                              # noqa: E402
from en_entries import ENTRIES                       # noqa: E402

OUT = ROOT / "en"
GEORGIA = "/System/Library/Fonts/Supplemental/Georgia.ttf"
GEORGIA_B = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"
if not (pathlib.Path(GEORGIA).exists() and pathlib.Path(GEORGIA_B).exists()):
    sys.exit("找不到 Georgia —— 英文分享图需要一套拉丁衬线")


def F(kind, size):
    return ImageFont.truetype(GEORGIA_B if kind == "b" else GEORGIA, size)


def wrap(d, text, font, maxw):
    """按词折行。中文那份逐字折，英文会把单词从中间切开。"""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=font) <= maxw:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def base(tag):
    img = Image.new("RGB", (G.W, G.H), G.PAPER)
    d = ImageDraw.Draw(img)
    ic = G.ICON.resize((52, 52), Image.LANCZOS)
    img.paste(ic, (G.TX0, 46), ic)
    d.text((G.TX0 + 66, 55), "OurWord", font=F("b", 26), fill=G.INK)
    ft = F("b", 20)
    d.text((G.TX1 - d.textlength(tag, font=ft), 61), tag, font=ft, fill=G.SEAL)
    d.line([(72, 118), (G.W - 72, 118)], fill=G.RULE, width=2)
    return img, d


def headline(d, text, y, max_lines=3):
    for size in (44, 40, 36, 32):
        f = F("b", size)
        lines = wrap(d, text, f, G.TW)
        if len(lines) <= max_lines:
            break
    for ln in G.clip(lines, max_lines):
        d.text((G.TX0, y), ln, font=f, fill=G.INK)
        y += int(size * 1.3)
    return y


def bottom_quote(d, text, size=24, lines=2, fill=G.INK2):
    fq = F("l", size)
    ql = G.clip(wrap(d, text, fq, G.TW - 26), lines)
    lh = int(size * 1.5)
    qh = lh * len(ql)
    qy = G.H - 70 - qh
    d.rectangle([G.TX0, qy + 5, G.TX0 + 5, qy + qh - 5], fill=G.SEAL)
    for i, ln in enumerate(ql):
        d.text((G.TX0 + 26, qy + i * lh), ln, font=fq, fill=fill)
    return qy


def first_sentence(dek):
    s = re.split(r"(?<=[.!?])\s", re.sub("==", "", dek or "").strip())[0].strip()
    return s if 20 <= len(s) <= 140 else None


def render_chapter(ch, out):
    img, d = base("Deep read")
    y = headline(d, first_sentence(ch.get("dek")) or ch["n"], 150)
    d.text((G.TX0, y + 12), "%s · %s" % (ch["parent"], ch["n"]), font=F("b", 22), fill=G.SEAL)
    qs = [re.sub("==", "", q).strip().rstrip(".") for q in (ch.get("q") or [""])]
    bottom_quote(d, max(qs, key=len))
    G.save(img, out)


def render_person(e, out):
    img, d = base("Entry")
    y = 150
    d.text((G.TX0, y), e["n"], font=F("b", 54), fill=G.INK); y += 70
    d.text((G.TX0, y), e.get("e", ""), font=F("l", 22), fill=G.MUTED); y += 42
    for ln in G.clip(wrap(d, e.get("w", ""), F("b", 28), G.TW), 2):
        d.text((G.TX0, y), ln, font=F("b", 28), fill=G.SEAL); y += 38
    P = C.PARENTS.get(e["slug"]) or C.PARENTS.get(e["n"]) or {}
    items = [it.get("n", "") for it in (P.get("items") if isinstance(P, dict) else []) or [] if it.get("ready", True)]
    bottom_quote(d, " · ".join(items) if items else (e.get("q") or [""])[0], size=22, lines=2, fill=G.INK2)
    G.save(img, out)


def render_home(out):
    img = Image.new("RGB", (G.W, G.H), G.PAPER)
    d = ImageDraw.Draw(img)
    ic = G.ICON.resize((104, 104), Image.LANCZOS)
    img.paste(ic, (G.TX0, 180), ic)
    d.text((G.TX0, 312), "OurWord", font=F("b", 60), fill=G.INK)
    d.text((G.TX0, 404), "See how people before you handled it.", font=F("l", 28), fill=G.INK2)
    d.line([(72, 118), (G.W - 72, 118)], fill=G.RULE, width=2)
    d.text((G.TX0, 57), "ourword.ai/en", font=F("b", 24), fill=G.MUTED)
    G.save(img, out)


def main():
    only_missing = "--only-missing" in sys.argv
    n = m = skipped = 0
    for ch in C.CHAPTERS:
        out = OUT / "i" / ch["parent_slug"] / ch["k"] / "og.png"
        if not out.parent.exists():
            continue
        if only_missing and out.exists():
            skipped += 1; continue
        render_chapter(ch, out); n += 1
    for e in ENTRIES:
        out = OUT / "i" / e["slug"] / "og.png"
        if not out.parent.exists():
            continue
        if only_missing and out.exists():
            skipped += 1; continue
        render_person(e, out); m += 1
    render_home(OUT / "og.png")
    print("英文分享图：章节 %d 张、条目 %d 张、首页 1 张（跳过已存在 %d 张）" % (n, m, skipped))
    return 0


if __name__ == "__main__":
    sys.exit(main())

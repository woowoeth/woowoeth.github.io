#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Idempotent GEO extras on top of stock geo_kit.py."""
from pathlib import Path
import re

p = Path("seo/geo_kit.py")
s = p.read_text(encoding="utf-8")

def once(old, new):
    global s
    if new.strip() in s:
        return
    if old not in s:
        print("skip missing block:", old[:60].replace("\n", " "))
        return
    s = s.replace(old, new, 1)

once(
    '    "YisouSpider",\n]',
    '    "YisouSpider", "360Spider", "HaosouSpider", "YandexBot",\n]',
)
once(
    '"sameAs": ["https://github.com/woowoeth"]',
    '"sameAs": ["https://github.com/woowoeth", "https://x.com/futuredotnews"]',
)
once(
    '    out.append(\'<meta name="twitter:card" content="summary_large_image">\')\n',
    '    out.append(\'<meta name="twitter:card" content="summary_large_image">\')\n'
    '    out.append(\'<meta name="twitter:site" content="@futuredotnews">\')\n',
)
once(
    '             "User-agent: *", "Allow: /", ""]',
    '             "User-agent: *",\n'
    '             "Content-Signal: search=yes,ai-input=yes,ai-train=no,use=reference",\n'
    '             "Allow: /", ""]',
)
once(
    '           "    <description>%s</description>\\n    <language>en</language>\\n%s\\n"',
    '           "    <description>%s</description>\\n    <language>zh-cn</language>\\n%s\\n"',
)

# strip a previously injected broken-indent favicon block
s = re.sub(
    r"[ \t]*out\.append\('<link rel=\"icon\".*?\n(?:[ \t]*out\.append\('<link rel=\"(?:icon|apple-touch-icon|shortcut icon)\".*?\n)+",
    "",
    s,
)

TRIO_MARK = "人类生存法则</a>"
if TRIO_MARK not in s:
    n = 0
    s2, n = re.subn(
        r"def sibling_links\(site, zh=False\):\n(?:.*\n)*?    return \" · \".join\(out\)\n",
        (
            'def sibling_links(site, zh=False):\n'
            '    return (\n'
            '        \'<a href="%s">人类生存法则</a> · \'\n'
            '        \'<a href="%s">原声播客</a> · \'\n'
            '        \'<a href="%s">品位 Skill</a>\'\n'
            '        % (esc(SITE + "/"), esc(SITE + "/podcast/"), esc(SITE + "/skill/"))\n'
            '    )\n'
        ),
        s,
        count=1,
    )
    if n:
        s = s2
        print("patched sibling_links")

# --- dead links (checked against the live site 2026-08-29) -------------------
# /idea/ and /pixel/ are 404. Advertising them in llms.txt teaches answer
# engines that our URLs are unreliable; drop them until those repos ship.
for _dead in ('    ("idea", "Idea", "\u7075\u611f\u770b\u677f"),\n',
              '    ("pixel", "PixelPad", "\u50cf\u7d20\u677f"),\n'):
    if _dead in s:
        s = s.replace(_dead, "")
        print("dropped dead SITES entry")

# There is no /zh/ tree — zh_items is 0 and always has been.
once(
    '         "- Every %s has its own static page: %si/<slug>/ \u2014 plus %szh/i/<slug>/ where "\n'
    '         "there is Chinese copy" % (site.item_noun, site.base, site.base),\n',
    '         "- Every %s has its own static page: %si/<slug>/"\n'
    '         % (site.item_noun, site.base),\n',
)

# 404 hop mapped pixelpad -> /pixel/, which is itself a 404.
once(
    "\"var R={'ourword-site':'site','ai-bubble':'ai','skill-store':'skill','pixelpad':'pixel'},\"",
    "\"var R={'ourword-site':'site','ai-bubble':'ai','skill-store':'skill'},\"",
)

# --- block bodies must keep their line breaks ---------------------------------
# Item.__init__ ran plain() over block bodies, and plain() collapses \s+ into a
# single space. _paras() splits on "\n", so it always saw exactly one paragraph:
# the 对照 section rendered as ONE link with every other contrast swallowed into
# its description, and 延伸 arrived as a single space-joined line. Keep newlines
# for blocks; plain() is still what descriptions and llms-full.txt use.
once(
    'def plain(s, limit=None):',
    'def block_text(s):\n'
    '    """Like plain(), but line breaks survive — blocks are multi-paragraph."""\n'
    '    s = re.sub(r"<[^>]+>", " ", str(s or ""))\n'
    '    s = re.sub(r"[ \\t\\r\\f\\v]+", " ", s)\n'
    '    return "\\n".join(x.strip() for x in s.split("\\n") if x.strip())\n'
    '\n'
    '\n'
    'def plain(s, limit=None):',
)
once(
    '        self.blocks = [(plain(h), plain(b)) for h, b in (blocks or []) if plain(b)]',
    '        self.blocks = [(plain(h), block_text(b)) for h, b in (blocks or []) if plain(b)]',
)

# BreadcrumbList's leaf pointed at /zh/i/<slug>/ on all 100 pages. There is no
# /zh/ tree (zh_items is 0), so every page shipped structured data whose leaf
# URL 404s. Everything else already gates the zh URL on has_zh(); this didn't.
once(
    '        {"@type": "ListItem", "position": 3, "name": it.t(zh), "item": it.page(site, zh)}]}',
    '        {"@type": "ListItem", "position": 3, "name": it.t(zh),\n'
    '         "item": it.page(site, zh and it.has_zh())}]}',
)

# og:locale:alternate advertised an en_US twin on every page. There is no English
# version and no hreflang to back it — same class of claim as the /zh/ breadcrumb.
_loc = """    out.append('<meta property="og:locale:alternate" content="%s">'
               % ("en_US" if zh else "zh_CN"))
"""
if _loc in s:
    s = s.replace(_loc, "")
    print("dropped og:locale:alternate")

p.write_text(s, encoding="utf-8")
print("patched geo_kit", p.stat().st_size)

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
    '            "inLanguage": ["en", "zh-Hans"],',
    '            "inLanguage": ["zh-Hans", "en"],',
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

ICONS = (
    "    out.append('<link rel=\"icon\" type=\"image/svg+xml\" href=\"/favicon.svg\">')\n"
    "    out.append('<link rel=\"icon\" type=\"image/png\" sizes=\"32x32\" href=\"/favicon-32.png\">')\n"
    "    out.append('<link rel=\"apple-touch-icon\" sizes=\"180x180\" href=\"/apple-touch-icon.png\">')\n"
    "    out.append('<link rel=\"shortcut icon\" href=\"/favicon.ico\">')\n"
)

if 'href=\"/favicon.svg\"' not in s and "href='/favicon.svg'" not in s:
    m = re.search(r"def head_block\([^)]*\):\n", s)
    if m:
        # insert after first out.append in head_block if present
        start = m.end()
        ins = s.find("out.append", start)
        if ins != -1:
            s = s[:ins] + ICONS.replace("    ", "    ") + s[ins:]
            print("injected favicon into head_block")
        else:
            print("head_block has no out.append")
    else:
        print("no head_block")

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
    else:
        once(
            (
                '        return (\n'
                '            \'<a href="%s">品味</a> · <a href="%s">原声</a>\'\n'
                '            % (esc(SITE + "/skill/"), esc(SITE + "/podcast/"))\n'
                '        )\n'
            ),
            (
                '        return (\n'
                '            \'<a href="%s">人类生存法则</a> · \'\n'
                '            \'<a href="%s">原声播客</a> · \'\n'
                '            \'<a href="%s">品位 Skill</a>\'\n'
                '            % (esc(SITE + "/"), esc(SITE + "/podcast/"), esc(SITE + "/skill/"))\n'
                '        )\n'
            ),
        )

p.write_text(s, encoding="utf-8")
print("patched geo_kit", p.stat().st_size)

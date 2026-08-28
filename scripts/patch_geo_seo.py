#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Idempotent GEO extras on top of stock geo_kit.py."""
from pathlib import Path

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

TRIO = (
    'def sibling_links(site, zh=False):\n'
    '    return (\n'
    '        \'<a href="%s">人类生存法则</a> · \'\n'
    '        \'<a href="%s">原声播客</a> · \'\n'
    '        \'<a href="%s">品位 Skill</a>\'\n'
    '        % (esc(SITE + "/"), esc(SITE + "/podcast/"), esc(SITE + "/skill/"))\n'
    '    )\n'
)

if "人类生存法则</a>" not in s:
    import re
    s2, n = re.subn(
        r"def sibling_links\(site, zh=False\):\n(?:.*\n)*?    return \" · \".join\(out\)\n",
        TRIO,
        s,
        count=1,
    )
    if n:
        s = s2
        print("patched sibling_links")
    else:
        old = (
            '        return (\n'
            '            \'<a href="%s">品味</a> · <a href="%s">原声</a>\'\n'
            '            % (esc(SITE + "/skill/"), esc(SITE + "/podcast/"))\n'
            '        )\n'
        )
        once(old, (
            '        return (\n'
            '            \'<a href="%s">人类生存法则</a> · \'\n'
            '            \'<a href="%s">原声播客</a> · \'\n'
            '            \'<a href="%s">品位 Skill</a>\'\n'
            '            % (esc(SITE + "/"), esc(SITE + "/podcast/"), esc(SITE + "/skill/"))\n'
            '        )\n'
        ))

p.write_text(s, encoding="utf-8")
print("patched geo_kit", p.stat().st_size)

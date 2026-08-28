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
    '    lines.append("")\n    return _write(os.path.join(root, "robots.txt"), "\\n".join(lines))',
    '    lines.append("")\n    return _write(os.path.join(root, "robots.txt"), "\\n".join(lines))',
)

# Content-Signal on robots * group
once(
    '             "User-agent: *", "Allow: /", ""]',
    '             "User-agent: *",\n'
    '             "Content-Signal: search=yes,ai-input=yes,ai-train=no,use=reference",\n'
    '             "Allow: /", ""]',
)

# RSS language
once(
    '           "    <description>%s</description>\\n    <language>en</language>\\n%s\\n"',
    '           "    <description>%s</description>\\n    <language>zh-cn</language>\\n%s\\n"',
)

p.write_text(s, encoding="utf-8")
print("patched geo_kit", p.stat().st_size)

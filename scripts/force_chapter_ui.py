#!/usr/bin/env python3
# Patch generators AND already-built HTML so highlight/sidebar cannot miss.
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
STYLE = (
    '<style id="hw-force">'
    'mark,mark.hl{background:transparent!important;color:#9d2933!important;'
    'font-weight:700!important;text-decoration:underline!important;'
    'text-decoration-color:#9d2933!important;text-underline-offset:.16em;'
    'text-decoration-thickness:1.5px}'
    '@media (max-width:900px){aside.side{display:none!important}'
    '.layout{grid-template-columns:1fr!important}}'
    '</style>'
)
MARK_OPEN = (
    '<mark class="hl" style="background:transparent;color:#9d2933;font-weight:700;'
    'text-decoration:underline;text-decoration-color:#9d2933;text-underline-offset:.16em;'
    'text-decoration-thickness:1.5px">'
)

def patch_html():
    n = 0
    for path in (ROOT / "i").rglob("index.html") if (ROOT / "i").exists() else []:
        s = path.read_text(encoding="utf-8")
        # Legacy CJK-slug stubs are meta-refresh redirects rewritten byte-for-byte
        # by write_legacy_redirects on every build. Touching them here makes the two
        # scripts fight and produces a fresh commit every single run.
        if 'http-equiv="refresh"' in s:
            continue
        orig = s
        if 'id="hw-force"' not in s:
            s = s.replace("</head>", STYLE + "</head>", 1)
        s = re.sub(r"<mark class=\"hl\"(?: style=\"[^\"]*\")?>", MARK_OPEN, s)
        if s != orig:
            path.write_text(s, encoding="utf-8")
            n += 1
    print("force_chapter_ui html", n)

if __name__ == "__main__":
    patch_html()

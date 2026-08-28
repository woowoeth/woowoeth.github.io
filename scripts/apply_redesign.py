#!/usr/bin/env python3
from pathlib import Path
import re
import sys
ROOT = Path(__file__).resolve().parents[1]

def once(path: Path, old: str, new: str, label: str):
    s = path.read_text(encoding="utf-8")
    if old not in s:
        if new[:48] in s:
            print("skip %s (already applied)" % label)
            return
        print("skip %s (marker gone)" % label)
        return
    path.write_text(s.replace(old, new, 1), encoding="utf-8")
    print("applied %s" % label)

ICONS = (
    '        "<link rel=\\"icon\\" type=\\"image/svg+xml\\" href=\\"/favicon.svg\\">\\n"\n'
    '        "<link rel=\\"icon\\" type=\\"image/png\\" sizes=\\"32x32\\" href=\\"/favicon-32.png\\">\\n"\n'
    '        "<link rel=\\"apple-touch-icon\\" href=\\"/apple-touch-icon.png\\">\\n"\n'
    '        "<link rel=\\"shortcut icon\\" href=\\"/favicon.ico\\">\\n"\n'
)

def main():
    theme = ROOT / "seo/hw_theme.py"
    t = theme.read_text(encoding="utf-8")
    if 'href=\\"/favicon.svg\\"' not in t:
        needle = '        "<link rel=\\"stylesheet\\" href=\\"/assets/hw-entry.css?v=6\\">\\n"\n'
        if needle in t:
            t = t.replace(needle, ICONS + needle, 1)
            theme.write_text(t, encoding="utf-8")
            print("icons in hw_theme v6")
        else:
            t2, n = re.subn(
                r'(        "<link rel=\\"stylesheet\\" href=\\"/assets/hw-entry.css\?v=\d+\\">\\n"\n)',
                ICONS + r"\1",
                t,
                count=1,
            )
            if n:
                theme.write_text(t2, encoding="utf-8")
                print("icons in hw_theme")
            else:
                print("skip hw_theme icons (no stylesheet line)")
    else:
        print("hw_theme already has favicon")

    idx = ROOT / "index.html"
    s = idx.read_text(encoding="utf-8")
    s = s.replace('href="favicon.svg"', 'href="/favicon.svg"')
    s = s.replace('href="favicon-32.png"', 'href="/favicon-32.png"')
    s = s.replace('href="apple-touch-icon.png"', 'href="/apple-touch-icon.png"')
    if 'rel="shortcut icon"' not in s:
        s = s.replace(
            '<link rel="icon" type="image/svg+xml" href="/favicon.svg">',
            '<link rel="icon" type="image/svg+xml" href="/favicon.svg">\n<link rel="shortcut icon" href="/favicon.ico">',
        )
    idx.write_text(s, encoding="utf-8")
    print("homepage icons rooted")

    sys_path = str(ROOT / "seo")
    if sys_path not in sys.path:
        sys.path.insert(0, sys_path)
    import hw_slugs
    src = idx.read_text(encoding="utf-8")
    js = hw_slugs.js_map() + "\nfunction slugOf(n){return (HW_SLUGS&&HW_SLUGS[n])||String(n).replace(/[·，、。\\s\\.,]/g,'');}"
    old_fn = "function slugOf(n){return String(n).replace(/[·，、。\\s\\.,]/g,'');}"
    pat = re.compile(r"const HW_SLUGS=\{[\s\S]*?\};\nfunction slugOf\(n\)\{[^}]+\}")
    if pat.search(src):
        idx.write_text(pat.sub(lambda _m: js, src, count=1), encoding="utf-8")
        print("applied slug map refresh")
    elif old_fn in src:
        idx.write_text(src.replace(old_fn, js, 1), encoding="utf-8")
        print("applied english slug map")
    else:
        print("skip slug map (marker gone)")

if __name__ == "__main__":
    main()

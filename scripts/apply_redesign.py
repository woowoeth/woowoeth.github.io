#!/usr/bin/env python3
from pathlib import Path
import re
import sys
ROOT = Path(__file__).resolve().parents[1]

def main():
    idx = ROOT / "index.html"
    s = idx.read_text(encoding="utf-8")
    if "hw-home-lockup.css" not in s:
        s = s.replace(
            "</title>",
            '</title>\n<link rel="stylesheet" href="/assets/hw-home-lockup.css?v=1">',
            1,
        )
        print("linked hw-home-lockup.css")
    else:
        s = re.sub(
            r"hw-home-lockup\.css\?v=\d+",
            "hw-home-lockup.css?v=1",
            s,
            count=1,
        )
        print("lockup css already linked")
    s = s.replace('href="favicon.svg"', 'href="/favicon.svg"')
    s = s.replace('href="favicon-32.png"', 'href="/favicon-32.png"')
    idx.write_text(s, encoding="utf-8")

    try:
        sys.path.insert(0, str(ROOT / "seo"))
        import hw_slugs
        src = idx.read_text(encoding="utf-8")
        js = hw_slugs.js_map() + "\nfunction slugOf(n){return (HW_SLUGS&&HW_SLUGS[n])||String(n).replace(/[·，、。\\s\\.,]/g,'');}"
        pat = re.compile(r"const HW_SLUGS=\{[\s\S]*?\};\nfunction slugOf\(n\)\{[^}]+\}")
        if pat.search(src):
            idx.write_text(pat.sub(lambda _m: js, src, count=1), encoding="utf-8")
            print("slug map ok")
    except Exception as e:
        print("slug map skipped:", e)

if __name__ == "__main__":
    main()

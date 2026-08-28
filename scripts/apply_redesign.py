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

def main():
    idx = ROOT / "index.html"
    s = idx.read_text(encoding="utf-8")
    if 'font-family:"Huiwen-mincho"' not in s.split(".hd-title", 1)[-1][:200]:
        s = s.replace(
            ".hd-title{font-size:26px;font-weight:700;letter-spacing:-.03em;line-height:1.05}",
            ".hd-title{font-family:\"Huiwen-mincho\",\"Songti SC\",\"STSong\",serif;font-size:26px;font-weight:700;letter-spacing:.02em;line-height:1.15}",
        )
    if ".brand-logo" not in s:
        s = s.replace(
            ".brand{font-size:10px;letter-spacing:.22em;text-transform:uppercase;color:var(--ink-50);margin-bottom:11px}",
            ".brand{display:flex;align-items:center;gap:10px;font-size:10px;letter-spacing:.22em;text-transform:uppercase;color:var(--ink-50);margin-bottom:11px}\n.brand-logo{width:40px;height:40px;border-radius:10px}",
        )
    if 'class="brand-logo"' not in s:
        s = s.replace(
            '<div class="brand">HUMAN WORLD</div>',
            '<div class="brand"><img class="brand-logo" src="/favicon.svg" width="40" height="40" alt=""><span>HUMAN WORLD</span></div>',
        )
    idx.write_text(s, encoding="utf-8")
    print("homepage wordmark + logo")

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

    family = (
        '  <nav class="family" style="margin:0 0 22px;font-size:13px;color:var(--ink-50)">'
        '<a href="/">人类生存法则</a> · '
        '<a href="/podcast/">原声播客</a> · '
        '<a href="/skill/">品位 Skill</a></nav>\n'
    )
    once(
        ROOT / "index.html",
        '<footer style="text-align:center;padding:8px 24px 48px;font-size:12px;color:var(--ink-30)">\n  <div class="wx">',
        '<footer style="text-align:center;padding:8px 24px 48px;font-size:12px;color:var(--ink-30)">\n' + family + '  <div class="wx">',
        "homepage family footer",
    )

if __name__ == "__main__":
    main()

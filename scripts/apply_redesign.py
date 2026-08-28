#!/usr/bin/env python3
from pathlib import Path
import re
import sys
ROOT = Path(__file__).resolve().parents[1]

OVERRIDE = '''
/* LOCKUP-FINAL: beat stacked homepage rules; match entry .wordmark */
@import url("https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500;600;700&display=swap");
.hd-title,
.brand .wordmark,
.brand-lockup .hd-title{
  font-family:"Noto Serif SC","Source Han Serif SC","Songti SC","STSong",Georgia,serif !important;
  font-size:20px !important;
  font-weight:700 !important;
  letter-spacing:.04em !important;
  line-height:1.25 !important;
  margin:0 !important;
}
.brand-logo{width:36px !important;height:36px !important;border-radius:9px !important;}
.hd-en,.slogan{font-size:12px !important;font-weight:400 !important;letter-spacing:0 !important;}
@media(max-width:600px){
  .hd-title,.brand .wordmark,.brand-lockup .hd-title{font-size:20px !important;font-weight:700 !important;}
}
'''

def main():
    idx = ROOT / "index.html"
    s = idx.read_text(encoding="utf-8")
    if "LOCKUP-FINAL" not in s:
        s = s.replace("</style>", OVERRIDE + "</style>", 1)
        print("injected LOCKUP-FINAL")
    else:
        s = re.sub(
            r"/\\* LOCKUP-FINAL[\\s\\S]*?@media\(max-width:600px\)\{[\s\\S]*?\\}\\n",
            OVERRIDE.lstrip("\n"),
            s,
            count=1,
        )
        print("refreshed LOCKUP-FINAL")
    s = s.replace('href="favicon.svg"', 'href="/favicon.svg"')
    s = s.replace('href="favicon-32.png"', 'href="/favicon-32.png"')
    s = s.replace('href="apple-touch-icon.png"', 'href="/apple-touch-icon.png"')
    idx.write_text(s, encoding="utf-8")

    theme = ROOT / "seo/hw_theme.py"
    t = theme.read_text(encoding="utf-8")
    if 'href=\\"/favicon.svg\\"' not in t:
        t2, n = re.subn(
            r'(        "<link rel=\\"stylesheet\\" href=\\"/assets/hw-entry.css\?v=\d+\\">\\n"\n)',
            (
                '        "<link rel=\\"icon\\" type=\\"image/svg+xml\\" href=\\"/favicon.svg\\">\\n"\n'
                '        "<link rel=\\"icon\\" type=\\"image/png\\" sizes=\\"32x32\\" href=\\"/favicon-32.png\\">\\n"\n'
                '        "<link rel=\\"apple-touch-icon\\" href=\\"/apple-touch-icon.png\\">\\n"\n'
                '        "<link rel=\\"shortcut icon\\" href=\\"/favicon.ico\\">\\n"\n'
                r'\1'
            ),
            t,
            count=1,
        )
        if n:
            theme.write_text(t2, encoding="utf-8")
            print("icons in hw_theme")

    sys_path = str(ROOT / "seo")
    if sys_path not in sys.path:
        sys.path.insert(0, sys_path)
    import hw_slugs
    src = idx.read_text(encoding="utf-8")
    js = hw_slugs.js_map() + "\nfunction slugOf(n){return (HW_SLUGS&&HW_SLUGS[n])||String(n).replace(/[·，、。\\s\\.,]/g,'');}"
    pat = re.compile(r"const HW_SLUGS=\{[\s\S]*?\};\nfunction slugOf\(n\)\{[^}]+\}")
    if pat.search(src):
        idx.write_text(pat.sub(lambda _m: js, src, count=1), encoding="utf-8")
        print("slug map ok")

if __name__ == "__main__":
    main()

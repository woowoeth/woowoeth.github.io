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

LOCKUP_CSS = '''/* masthead — match entry pages */
.hd{position:relative;z-index:50;margin:0 0 26px;padding:28px 0 16px;background:transparent}
.hd::after{display:none}
.brand{display:flex;flex-direction:row;flex-wrap:nowrap;align-items:center;gap:12px;color:inherit;text-decoration:none;margin:0 0 14px}
.brand-logo{width:36px;height:36px;border-radius:9px;flex:none}
.brand-copy{display:flex;flex-direction:column;gap:3px;min-width:0}
.hd-title,.brand .wordmark{font-family:"Noto Serif SC","Source Han Serif SC","Songti SC","STSong",Georgia,serif;font-size:20px;font-weight:700;letter-spacing:.04em;line-height:1.25;margin:0}
.hd-title .dot,.brand .dot{color:#9d2933}
.hd-en,.slogan{margin:0;color:var(--ink-50);font-size:12px;line-height:1.4;font-weight:400;letter-spacing:0}
.hd-row{display:none}
.hd-stats{display:flex;gap:20px;flex-wrap:wrap}
.stat{font-size:12px;color:var(--ink-50);font-variant-numeric:tabular-nums}
.stat b{color:var(--ink);font-weight:600}
'''

OLD_CSS = '''/* masthead — glass sticky */
.hd{position:sticky;top:0;z-index:50;margin:0 -24px 26px;padding:26px 24px 15px;background:var(--glass-chrome);-webkit-backdrop-filter:blur(16px) saturate(160%);backdrop-filter:blur(16px) saturate(160%)}
.hd::after{content:'';position:absolute;left:24px;right:24px;bottom:0;height:1px;background:linear-gradient(90deg,transparent,rgba(42,46,44,.10),transparent)}
.brand{font-size:10px;letter-spacing:.22em;text-transform:uppercase;color:var(--ink-50);margin-bottom:11px}
.hd-row{display:flex;align-items:baseline;gap:12px;margin-bottom:13px;flex-wrap:wrap}
.hd-title{font-size:26px;font-weight:700;letter-spacing:-.03em;line-height:1.05}
.hd-en{font-size:13px;color:var(--ink-50);letter-spacing:-.005em;font-weight:400}
.hd-stats{display:flex;gap:20px;flex-wrap:wrap}
.stat{font-size:12px;color:var(--ink-50);font-variant-numeric:tabular-nums}
'''

THIN = '.hd-title,.brand .wordmark{font-family:"Noto Serif SC","Source Han Serif SC","Songti SC","STSong",Georgia,serif;font-size:18px;font-weight:600;letter-spacing:.06em;line-height:1.25;margin:0}'
BOLD = '.hd-title,.brand .wordmark{font-family:"Noto Serif SC","Source Han Serif SC","Songti SC","STSong",Georgia,serif;font-size:20px;font-weight:700;letter-spacing:.04em;line-height:1.25;margin:0}'

OLD_HDR = '''  <header class="hd" role="banner">
    <div class="brand">HUMAN WORLD</div>
    <div class="hd-row">
      <h1 class="hd-title">人类世界生存法则</h1>
      <span class="hd-en">人类文明的坐标，照亮千年的灯塔</span>
    </div>'''

NEW_HDR = '''  <header class="hd" role="banner">
    <a class="brand" href="/">
      <img class="brand-logo" src="/favicon.svg" width="36" height="36" alt="">
      <span class="brand-copy">
        <h1 class="hd-title">人类世界<span class="dot">生存法则</span></h1>
        <p class="hd-en">95 个人物与典籍的生存智慧，跨越 2600 年</p>
      </span>
    </a>'''

def main():
    idx = ROOT / "index.html"
    s = idx.read_text(encoding="utf-8")
    if "fonts.googleapis.com/css2?family=Noto+Serif+SC" not in s:
        s = s.replace(
            "</style>",
            '@import url("https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500;600;700&display=swap");\n</style>',
            1,
        )
    if OLD_CSS in s:
        s = s.replace(OLD_CSS, LOCKUP_CSS, 1)
        print("replaced homepage mast css")
    if THIN in s:
        s = s.replace(THIN, BOLD, 1)
        print("bold homepage wordmark")
    if OLD_HDR in s:
        s = s.replace(OLD_HDR, NEW_HDR, 1)
        print("replaced homepage header html")
    s = s.replace(".wrap{padding:0 16px 80px}", ".wrap{padding:0 24px 80px}")
    s = s.replace(
        ".hd{margin:0 -16px 24px;padding:22px 16px 13px}",
        ".hd{margin:0 0 24px;padding:22px 0 14px}",
    )
    idx.write_text(s, encoding="utf-8")

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

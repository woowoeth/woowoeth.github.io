#!/usr/bin/env python3
from pathlib import Path
import re
import sys
ROOT = Path(__file__).resolve().parents[1]

def once(path: Path, old: str, new: str, label: str):
    s = path.read_text(encoding="utf-8")
    if old not in s:
        if new[:40] in s:
            print("skip %s (already applied)" % label)
            return
        print("skip %s (marker gone)" % label)
        return
    path.write_text(s.replace(old, new, 1), encoding="utf-8")
    print("applied %s" % label)

HOME_MQ = """
/* responsive lockup */
@media(max-width:720px){
  .brand-lockup{align-items:flex-start}
  .hd-title{font-size:26px;white-space:nowrap}
  .hd-en{margin:0;font-size:12.5px}
}
@media(max-width:480px){
  .brand-logo{width:36px;height:36px;border-radius:9px}
  .hd-title{font-size:22px;white-space:normal}
  .wrap{padding-left:16px;padding-right:16px}
}
"""

FAMILY = (
    '  <nav class="family" style="margin:0 0 22px;font-size:13px;color:var(--ink-50)">'
    '<a href="/">人类生存法则</a> · '
    '<a href="/podcast/">原声播客</a> · '
    '<a href="/skill/">品位 Skill</a></nav>\n'
)

def main():
    bseo = (ROOT / "seo/build_seo.py").read_text(encoding="utf-8")
    if "import hw_slugs" not in bseo:
        once(
            ROOT / "seo/build_seo.py",
            "import geo_kit as G\n",
            "import geo_kit as G\nimport hw_theme\nhw_theme.install(G)\n",
            "install hw_theme",
        )
    else:
        print("skip install hw_theme (hw_slugs already wired)")
    idx = ROOT / "index.html"
    s = idx.read_text(encoding="utf-8")
    n = 0
    pairs = [
        (".hd-en{font-size:13.5px;color:var(--ink-50);letter-spacing:0;font-weight:400;margin-left:58px}",
         ".hd-en{font-size:13.5px;color:var(--ink-50);letter-spacing:0;font-weight:400;margin:0}"),
        (".hd{position:relative;z-index:50;margin:0 0 28px;padding:clamp(28px,5vw,56px) 0 8px;background:transparent;-webkit-backdrop-filter:none;backdrop-filter:none}",
         ".hd{position:relative;z-index:50;margin:0 0 28px;padding:clamp(28px,6vw,64px) 0 22px;background:transparent;-webkit-backdrop-filter:none;backdrop-filter:none}"),
        (".wrap{max-width:1120px;margin:0 auto;padding:0 clamp(18px,4vw,40px) 96px}",
         ".wrap{max-width:1120px;margin:0 auto;padding:0 clamp(16px,4vw,48px) 96px}"),
        (".brand-lockup{display:flex;align-items:center;gap:14px;text-decoration:none;color:inherit;margin:0 0 14px}",
         ".brand-lockup{display:flex;align-items:flex-start;gap:12px;text-decoration:none;color:inherit;margin:0 0 14px}"),
        (".hd-title{font-family:\"Songti SC\",\"Noto Serif CJK SC\",\"Source Han Serif SC\",Georgia,serif;font-size:clamp(28px,4.6vw,42px);font-weight:700;letter-spacing:-.03em;line-height:.95}",
         ".hd-title{font-family:\"Songti SC\",\"Noto Serif CJK SC\",\"Source Han Serif SC\",Georgia,serif;font-size:clamp(22px,4.2vw,42px);font-weight:700;letter-spacing:-.03em;line-height:1.05}"),
    ]
    for a, b in pairs:
        if a in s:
            s = s.replace(a, b)
            n += 1
    if "/* responsive lockup */" not in s:
        s = s.replace("/* unified brand lockup — match entry pages / yuansheng */", "/* unified brand lockup — match entry pages / yuansheng */" + HOME_MQ)
        if "/* responsive lockup */" in s:
            n += 1
    idx.write_text(s, encoding="utf-8")
    print("applied homepage spacing", n)
    once(
        ROOT / "index.html",
        '''      <span class="brand-copy">
        <h1 class="hd-title">人类世界<span class="dot">生存法则</span></h1>
      </span>
    </a>
    <p class="hd-en">人类文明的坐标，照亮千年的灯塔</p>''',
        '''      <span class="brand-copy">
        <h1 class="hd-title">人类世界<span class="dot">生存法则</span></h1>
        <p class="hd-en">人类文明的坐标，照亮千年的灯塔</p>
      </span>
    </a>''',
        "homepage slogan under wordmark",
    )
    once(
        ROOT / "index.html",
        '<footer style="text-align:center;padding:8px 24px 48px;font-size:12px;color:var(--ink-30)">\n  <div class="wx">',
        '<footer style="text-align:center;padding:8px 24px 48px;font-size:12px;color:var(--ink-30)">\n'
        + FAMILY +
        '  <div class="wx">',
        "homepage family footer",
    )
    sys_path = str(ROOT / "seo")
    if sys_path not in sys.path:
        sys.path.insert(0, sys_path)
    import hw_slugs
    idx = ROOT / "index.html"
    src = idx.read_text(encoding="utf-8")
    js = hw_slugs.js_map() + "\nfunction slugOf(n){return (HW_SLUGS&&HW_SLUGS[n])||String(n).replace(/[·，、。\\s\\.,]/g,'');}"
    old_fn = "function slugOf(n){return String(n).replace(/[·，、。\\s\\.,]/g,'');}"
    pat = re.compile(r"const HW_SLUGS=\{[\s\S]*?\};\nfunction slugOf\(n\)\{[^}]+\}")
    if pat.search(src):
        src2 = pat.sub(lambda _m: js, src, count=1)
        idx.write_text(src2, encoding="utf-8")
        print("applied slug map refresh")
    elif old_fn in src:
        idx.write_text(src.replace(old_fn, js, 1), encoding="utf-8")
        print("applied english slug map")
    else:
        print("skip slug map (marker gone)")

if __name__ == "__main__":
    main()

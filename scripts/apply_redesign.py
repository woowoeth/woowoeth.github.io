#!/usr/bin/env python3
from pathlib import Path
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

def main():
    once(
        ROOT / "seo/build_seo.py",
        "import geo_kit as G\n",
        "import geo_kit as G\nimport hw_theme\nhw_theme.install(G)\n",
        "install hw_theme",
    )
    idx = ROOT / "index.html"
    s = idx.read_text(encoding="utf-8")
    n = 0
    pairs = [
        (".hd-en{font-size:13.5px;color:var(--ink-50);letter-spacing:0;font-weight:400;margin-left:58px}",
         ".hd-en{font-size:13.5px;color:var(--ink-50);letter-spacing:0;font-weight:400;margin:0}"),
        (".hd{position:relative;z-index:50;margin:0 0 28px;padding:clamp(28px,5vw,56px) 0 8px;background:transparent;-webkit-backdrop-filter:none;backdrop-filter:none}",
         ".hd{position:relative;z-index:50;margin:0 0 28px;padding:clamp(36px,6vw,64px) 0 22px;background:transparent;-webkit-backdrop-filter:none;backdrop-filter:none}"),
        (".wrap{max-width:1120px;margin:0 auto;padding:0 clamp(18px,4vw,40px) 96px}",
         ".wrap{max-width:1120px;margin:0 auto;padding:0 clamp(20px,4vw,48px) 96px}"),
        (".brand-lockup{display:flex;align-items:center;gap:14px;text-decoration:none;color:inherit;margin:0 0 14px}",
         ".brand-lockup{display:flex;align-items:flex-start;gap:14px;text-decoration:none;color:inherit;margin:0 0 14px}"),
    ]
    for a, b in pairs:
        if a in s:
            s = s.replace(a, b)
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

if __name__ == "__main__":
    main()

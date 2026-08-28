#!/usr/bin/env python3
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def once(path: Path, old: str, new: str, label: str):
    s = path.read_text(encoding="utf-8")
    if old not in s:
        if "brand-logo" in s and "logo" in label:
            print("skip %s (already applied)" % label)
            return
        if new[:40] in s:
            print("skip %s (already applied)" % label)
            return
        raise SystemExit("apply_redesign: missing marker for %s" % label)
    path.write_text(s.replace(old, new, 1), encoding="utf-8")
    print("applied %s" % label)

HOME_CSS = """
/* unified brand lockup — match entry pages / yuansheng */
.wrap{max-width:1120px;margin:0 auto;padding:0 clamp(18px,4vw,40px) 96px}
.hd{position:relative;z-index:50;margin:0 0 28px;padding:clamp(28px,5vw,56px) 0 8px;background:transparent;-webkit-backdrop-filter:none;backdrop-filter:none}
.hd::after{display:none}
.brand-lockup{display:flex;align-items:center;gap:14px;text-decoration:none;color:inherit;margin:0 0 14px}
.brand-lockup:hover{color:inherit}
.brand-logo{width:44px;height:44px;border-radius:11px;flex:none;box-shadow:0 1px 0 rgba(28,25,23,.06)}
.brand-copy{display:flex;flex-direction:column;gap:4px;min-width:0}
.hd-title{font-family:"Songti SC","Noto Serif CJK SC","Source Han Serif SC",Georgia,serif;font-size:clamp(28px,4.6vw,42px);font-weight:700;letter-spacing:-.03em;line-height:.95}
.hd-title .dot{color:#9d2933}
.hd-en{font-size:13.5px;color:var(--ink-50);letter-spacing:0;font-weight:400;margin-left:58px}
.hd-row{display:none}
.hd .brand{display:none}
@media(max-width:600px){
  .wrap{padding:0 16px 80px}
  .hd{margin:0 0 22px;padding:22px 0 8px}
  .hd-title{font-size:26px}
  .hd-en{margin-left:0}
}
"""

OLD_HEADER = """  <header class=\"hd\" role=\"banner\">
    <div class=\"brand\">HUMAN WORLD</div>
    <div class=\"hd-row\">
      <h1 class=\"hd-title\">人类世界生存法则</h1>
      <span class=\"hd-en\">人类文明的坐标，照亮千年的灯塔</span>
    </div>"""

NEW_HEADER = """  <header class=\"hd\" role=\"banner\">
    <a class=\"brand-lockup\" href=\"/\">
      <img class=\"brand-logo\" src=\"/favicon.svg\" width=\"44\" height=\"44\" alt=\"人类世界生存法则\">
      <span class=\"brand-copy\">
        <h1 class=\"hd-title\">人类世界<span class=\"dot\">生存法则</span></h1>
      </span>
    </a>
    <p class=\"hd-en\">人类文明的坐标，照亮千年的灯塔</p>"""

OLD_SIB = '''def sibling_links(site, zh=False):
    """Every site links to every sibling: eight orphans become one crawlable property."""
    out = []
    for path, en, cn in SITES:
        if path == site.path:
            continue
        out.append('<a href="%s">%s</a>' % (esc(SITE + "/" + (path + "/" if path else "")),
                                            esc(cn if zh else en)))
    return " · ".join(out)
'''

NEW_SIB = '''def sibling_links(site, zh=False):
    """Human World only points at the two sister editorial sites."""
    if site.path == "":
        return (
            '<a href="%s">品味</a> · <a href="%s">原声</a>'
            % (esc(SITE + "/skill/"), esc(SITE + "/podcast/"))
        )
    out = []
    for path, en, cn in SITES:
        if path == site.path:
            continue
        out.append('<a href="%s">%s</a>' % (esc(SITE + "/" + (path + "/" if path else "")),
                                            esc(cn if zh else en)))
    return " · ".join(out)
'''

def main():
    once(
        ROOT / "seo/build_seo.py",
        "import geo_kit as G\n",
        "import geo_kit as G\nimport hw_theme\nhw_theme.install(G)\n",
        "install hw_theme",
    )
    idx = ROOT / "index.html"
    s = idx.read_text(encoding="utf-8")
    repls = [
        ("--white:#fafaf7", "--white:#fffdf8"),
        ("--white:#fffef9", "--white:#fffdf8"),
        ("--paper:#f0f0ec", "--paper:#f7f4ec"),
        ("--paper:#f4f2ec", "--paper:#f7f4ec"),
        ("--paper2:#eae9e3", "--paper2:#efe8dc"),
        ("--paper2:#ece8df", "--paper2:#efe8dc"),
        ("--ink:#2a2e2c", "--ink:#1c1917"),
        ("--ink-70:#4c524e", "--ink-70:#3a342f"),
        ("--ink-70:#3f3a34", "--ink-70:#3a342f"),
        ("--ink-50:#767c76", "--ink-50:#6b6358"),
        ("--ink-50:#6f6959", "--ink-50:#6b6358"),
        ("--ink-30:#a3a8a1", "--ink-30:#9a9184"),
        ("--ink-30:#9a9384", "--ink-30:#9a9184"),
        ("--up:#66794a", "--up:#9d2933"),
        ("--sulfur:#b8c49a", "--sulfur:#f0ddd9"),
        ("--sulfur:#f3e4e0", "--sulfur:#f0ddd9"),
        ("--up-bg:rgba(184,196,154,.28)", "--up-bg:rgba(157,41,51,.12)"),
        ("--down:#b4574b", "--down:#9d2933"),
        ('content="#f0f0ec"', 'content="#f7f4ec"'),
        ("#e7ebdc", "#f0ddd9"),
        (".wrap{max-width:860px;margin:0 auto;padding:0 24px 96px}",
         ".wrap{max-width:1120px;margin:0 auto;padding:0 clamp(18px,4vw,40px) 96px}"),
    ]
    n = 0
    for a, b in repls:
        if a in s:
            s = s.replace(a, b)
            n += 1
    if "/* unified brand lockup" not in s:
        s = s.replace("/* masthead — glass sticky */", "/* masthead — glass sticky */" + HOME_CSS)
        n += 1
    idx.write_text(s, encoding="utf-8")
    print("applied homepage tokens/css", n)
    once(ROOT / "index.html", OLD_HEADER, NEW_HEADER, "homepage brand lockup + logo")
    once(ROOT / "seo/geo_kit.py", OLD_SIB, NEW_SIB, "sibling links taste+podcast")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def once(path: Path, old: str, new: str, label: str):
    s = path.read_text(encoding="utf-8")
    if new.strip()[:40] in s and old not in s:
        print(f"skip {label} (already applied)")
        return
    if old not in s:
        raise SystemExit(f"apply_redesign: missing marker for {label}")
    path.write_text(s.replace(old, new, 1), encoding="utf-8")
    print(f"applied {label}")

EXTRA_CSS = "/* list / hub / all */\n.feed{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:12px;margin:8px 0 40px}\n.feed a{display:flex;flex-direction:column;gap:6px;min-height:132px;background:var(--surface);border:1px solid var(--rule);border-radius:14px;padding:14px 16px 16px;color:inherit}\n.feed a:hover{border-color:var(--seal);color:inherit}\n.feed .k{font-size:11px;letter-spacing:.08em;color:var(--seal)}\n.feed strong{font-family:var(--serif);font-size:18px;line-height:1.3;font-weight:700}\n.feed .s{font-size:13.5px;color:var(--muted);line-height:1.55}\n.hubs{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 22px}\n.hubs a{background:var(--surface);border:1px solid var(--rule);border-radius:999px;padding:4px 12px;font-size:13px;color:var(--ink-2)}\n.hubs a:hover,.hubs a.on{border-color:var(--seal);color:var(--seal)}\n"

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
        ("content=\"#f0f0ec\"", "content=\"#f7f4ec\""),
        ("#e7ebdc", "#f0ddd9"),
    ]
    n = 0
    for a, b in repls:
        if a in s:
            s = s.replace(a, b)
            n += 1
    if n:
        idx.write_text(s, encoding="utf-8")
        print("applied homepage tokens", n)
    else:
        print("skip homepage tokens")
    once(
        ROOT / "index.html",
        ".hd-title{font-size:26px;font-weight:700;letter-spacing:-.03em;line-height:1.05}",
        '.hd-title{font-family:"Songti SC","Noto Serif CJK SC","Source Han Serif SC",Georgia,serif;font-size:28px;font-weight:700;letter-spacing:-.03em;line-height:1.05}',
        "homepage serif title",
    )
    once(
        ROOT / "seo/hw_theme.py",
        "    G.item_page = item_page\n",
        "    G.item_page = item_page\n    import hw_list\n    hw_list.install(G)\n",
        "install hw_list",
    )
    once(
        ROOT / "seo/geo_kit.py",
        '''def sibling_links(site, zh=False):\n    """Every site links to every sibling: eight orphans become one crawlable property."""\n    out = []\n    for path, en, cn in SITES:\n        if path == site.path:\n            continue\n        out.append('<a href="%s">%s</a>' % (esc(SITE + "/" + (path + "/" if path else "")),\n                                            esc(cn if zh else en)))\n    return " · ".join(out)\n''',
        '''def sibling_links(site, zh=False):\n    """Human World only points at the two sister editorial sites."""\n    if site.path == "":\n        return (
            '<a href="%s">品味</a> · <a href="%s">原声</a>'
            % (esc(SITE + "/skill/"), esc(SITE + "/podcast/"))\n        )\n    out = []\n    for path, en, cn in SITES:\n        if path == site.path:\n            continue\n        out.append('<a href="%s">%s</a>' % (esc(SITE + "/" + (path + "/" if path else "")),\n                                            esc(cn if zh else en)))\n    return " · ".join(out)\n''',
        "sibling links taste+podcast",
    )
    css = ROOT / "assets/hw-entry.css"
    s = css.read_text(encoding="utf-8")
    old_root = "--bg:#f4f2ec; --bg-tint:#ece8df; --surface:#fffef9; --surface-2:#f7f4ec;"
    new_root = "--bg:#f7f4ec; --bg-tint:#efe8dc; --surface:#fffdf8; --surface-2:#f3eee6;"
    if old_root in s:
        s = s.replace(old_root, new_root, 1).replace("--seal-soft:#f3e4e0;", "--seal-soft:#f0ddd9;")
        css.write_text(s, encoding="utf-8")
        print("applied entry palette")
    elif "--bg:#f7f4ec" in s:
        print("skip entry palette")
    else:
        print("entry palette marker missing")
    if "/* list / hub / all */" not in css.read_text(encoding="utf-8"):
        css.write_text(css.read_text(encoding="utf-8").rstrip() + "\n" + EXTRA_CSS, encoding="utf-8")
        print("applied list css")
    else:
        print("skip list css")

if __name__ == "__main__":
    main()

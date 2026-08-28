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
    once(
        ROOT / "index.html",
        "  --white:#fafaf7;--paper:#f0f0ec;--paper2:#eae9e3;\n"
        "  --ink:#2a2e2c;--ink-70:#4c524e;--ink-50:#767c76;--ink-30:#a3a8a1;\n"
        "  --up:#66794a;--sulfur:#b8c49a;--up-bg:rgba(184,196,154,.28);\n"
        "  --down:#b4574b;--down-bg:rgba(180,87,75,.10);",
        "  --white:#fffef9;--paper:#f4f2ec;--paper2:#ece8df;\n"
        "  --ink:#1c1917;--ink-70:#3f3a34;--ink-50:#6f6959;--ink-30:#9a9384;\n"
        "  --up:#9d2933;--sulfur:#f3e4e0;--up-bg:rgba(157,41,51,.12);\n"
        "  --down:#9d2933;--down-bg:rgba(157,41,51,.10);",
        "homepage seal/paper tokens",
    )
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
    css = ROOT / "assets/hw-entry.css"
    s = css.read_text(encoding="utf-8")
    if "/* list / hub / all */" not in s:
        css.write_text(s.rstrip() + "\n" + EXTRA_CSS, encoding="utf-8")
        print("applied list css")
    else:
        print("skip list css")

if __name__ == "__main__":
    main()

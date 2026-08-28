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

if __name__ == "__main__":
    main()

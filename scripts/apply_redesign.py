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

if __name__ == "__main__":
    main()

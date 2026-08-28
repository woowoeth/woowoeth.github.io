#!/usr/bin/env python3
# Idempotent homepage + palette + share patch. Safe on every SEO build.
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def once(path: Path, old: str, new: str, label: str, all=False):
    s = path.read_text(encoding="utf-8")
    if new.strip()[:40] in s and old not in s:
        print(f"skip {label} (already applied)")
        return
    if old not in s:
        raise SystemExit(f"apply_redesign: missing marker for {label}")
    path.write_text(s.replace(old, new) if all else s.replace(old, new, 1), encoding="utf-8")
    print(f"applied {label}")


def main():
    idx0 = ROOT / "index.html"
    raw0 = idx0.read_text(encoding="utf-8")
    if "function slugOf" not in raw0:
        once(
            ROOT / "index.html",
            "function op(name){\n  const d=D.find(x=>x.n===name);if(!d)return;",
            "function slugOf(n){return String(n).replace(/[·，、。\\s\\.,]/g,'');}\n"
            "function op(name){\n  const d=D.find(x=>x.n===name);if(!d)return;\n"
            "  location.href='/i/'+encodeURIComponent(slugOf(d.n))+'/';return;",
            "index op() -> /i/",
        )
    else:
        print("skip index op() -> /i/ (already applied)")
    idx = ROOT / "index.html"
    s = idx.read_text(encoding="utf-8")
    if ".ov{display:none !important;" not in s:
        s = s.replace(".ov{", ".ov{display:none !important;", 1)
        idx.write_text(s, encoding="utf-8")
        print("applied hide overlay")
    else:
        print("skip hide overlay")

    # remaining homepage/geo patches already applied on main; keep hook only
    once(
        ROOT / "seo/build_seo.py",
        "import geo_kit as G\n",
        "import geo_kit as G\nimport hw_theme\nhw_theme.install(G)\n",
        "install hw_theme",
    )


if __name__ == "__main__":
    main()

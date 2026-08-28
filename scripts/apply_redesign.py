#!/usr/bin/env python3
# Idempotent homepage + palette patch. Safe to run on every SEO build.
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
        ROOT / "index.html",
        "function op(name){\n  const d=D.find(x=>x.n===name);if(!d)return;",
        "function slugOf(n){return String(n).replace(/[·，、。\\s\\.,]/g,'');}\n"
        "function op(name){\n  const d=D.find(x=>x.n===name);if(!d)return;\n"
        "  location.href='/i/'+encodeURIComponent(slugOf(d.n))+'/';return;",
        "index op() -> /i/",
    )
    idx = ROOT / "index.html"
    s = idx.read_text(encoding="utf-8")
    if ".ov{display:none !important;" not in s:
        s = s.replace(".ov{", ".ov{display:none !important;", 1)
        idx.write_text(s, encoding="utf-8")
        print("applied hide overlay")
    else:
        print("skip hide overlay")

    once(
        ROOT / "seo/geo_kit.py",
        "body{margin:0;background:#f0f0ec;color:#2a2e2c;",
        "body{margin:0;background:#f4f0e8;color:#1c1917;",
        "geo paper",
    )
    once(
        ROOT / "seo/geo_kit.py",
        "a{color:#3a5f3a}",
        "a{color:#7a1e26}",
        "geo link",
    )
    once(
        ROOT / "seo/geo_kit.py",
        "h2{font-size:16px;margin:28px 0 6px;letter-spacing:-.005em}",
        "h2{font-size:13px;letter-spacing:.08em;color:#9d2933;margin:32px 0 8px;font-weight:650}",
        "geo h2",
    )
    once(
        ROOT / "seo/geo_kit.py",
        "color:#4c524e;background:rgba(42,46,44,.05);",
        "color:#4a4338;background:#efe8d8;",
        "geo chips",
    )


if __name__ == "__main__":
    main()

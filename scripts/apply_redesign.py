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

EXTRA_CSS = '/* list / hub / all */\n.feed{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:12px;margin:8px 0 40px}\n.feed a{display:flex;flex-direction:column;gap:6px;min-height:132px;background:var(--surface);border:1px solid var(--rule);border-radius:14px;padding:14px 16px 16px;color:inherit}\n.feed a:hover{border-color:var(--seal);color:inherit}\n.feed .k{font-size:11px;letter-spacing:.08em;color:var(--seal)}\n.feed strong{font-family:var(--serif);font-size:18px;line-height:1.3;font-weight:700}\n.feed .s{font-size:13.5px;color:var(--muted);line-height:1.55}\n.hubs{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 22px}\n.hubs a{background:var(--surface);border:1px solid var(--rule);border-radius:999px;padding:4px 12px;font-size:13px;color:var(--ink-2)}\n.hubs a:hover,.hubs a.on{border-color:var(--seal);color:var(--seal)}\n'
LIST_THEME = open('/dev/null').read() if False else None

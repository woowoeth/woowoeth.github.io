#!/usr/bin/env python3
from pathlib import Path
import re
import sys
ROOT = Path(__file__).resolve().parents[1]

# Typos are fixed at source now: scripts/inject_week.py (D[] batches) and
# seo/hw_chapters.py (deep-read chapters). Keep this list empty — patching the
# built index.html hides the bug in the source and the rules silently rot.
FIXES = []

NEW_FOOT = (
    'const lw=Math.round(W*.048),footFs=Math.round(W*.034),mid=FOOT-Math.round(srcS*.36);'
    'let bx=PADX;'
    'if(dqLogoOK){x.globalAlpha=.92;x.drawImage(dqLogoImg,bx,mid-lw/2,lw,lw);x.globalAlpha=1;bx+=lw+Math.round(W*.016);}'
    'x.font=footFs+\'px -apple-system,"PingFang SC",system-ui,sans-serif\';'
    'x.fillStyle=s.p[2];x.textBaseline="middle";x.fillText("OurWord.ai",bx,mid);'
)
FOOT_RE = re.compile(
    r"let bx=PADX;\s*if\(dqLogoOK\)\{const lw=Math\.round\(W\*\.06\),lh2=lw\*dqLogoImg\.height/dqLogoImg\.width;"
    r"\s*x\.globalAlpha=\.9;x\.drawImage\(dqLogoImg,bx,FOOT-lh2,lw,lh2\);x\.globalAlpha=1;bx\+=lw\+Math\.round\(W\*\.02\);\}"
    r"\s*x\.font=Math\.round\(W\*\.034\)\+'px -apple-system,\"PingFang SC\",system-ui,sans-serif';"
    r"\s*x\.fillStyle=s\.p\[2\];x\.textBaseline=\"alphabetic\";x\.fillText\(\"OurWord\.ai\",bx,FOOT\);"
)

HL = (
    '<mark class="hl" style="background:transparent;color:#9d2933;font-weight:700;' 
    'text-decoration:underline;text-decoration-color:#9d2933;text-underline-offset:.16em;' 
    'text-decoration-thickness:1.5px">%s</mark>'
)

def patch_chapters():
    p = ROOT / "seo" / "hw_chapters.py"
    if not p.exists():
        return
    s = p.read_text(encoding="utf-8")
    s = s.replace(
        "out.append(('<mark class=\"hl\">%s</mark>' % t) if i % 2 else t)",
        "out.append((HL % t) if i % 2 else t)",
    )
    if "HL = " not in s:
        s = s.replace("def rich(s):", "HL = %r\ndef rich(s):" % HL, 1)
    p.write_text(s, encoding="utf-8")
    print("chapters highlight inlined")

def patch_theme():
    theme = ROOT / "seo" / "hw_theme.py"
    if not theme.exists():
        return
    ts = theme.read_text(encoding="utf-8")
    ts = re.sub(r"hw-chapter\.css\?v=\d+", "hw-chapter.css?v=5", ts)
    # NOTE: never delete a %s from hw_theme's body template — the arg tuple still
    # passes page_url and the build dies with "not all arguments converted".
    # The cite line is removed from the *output* by seo/strip_cite.py instead.
    theme.write_text(ts, encoding="utf-8")
    print("theme css v=5")

def patch_entry_css():
    """Idempotent by sentinel. The old whitespace-sniffing check never matched its own
    output, so every CI run appended another copy of the same media query."""
    entry = ROOT / "assets" / "hw-entry.css"
    if not entry.exists():
        return
    es = entry.read_text(encoding="utf-8")
    es = es.replace(".side,.layout .side{display:none!important}\n"
                    ".layout{grid-template-columns:minmax(0,1fr)!important}\n", "")
    mark = "/* hw-entry-overrides */"
    if mark in es:
        es = es[:es.index(mark)].rstrip("\n") + "\n"
    es = es.rstrip("\n") + "\n\n" + mark + "\n" + (
        "@media (max-width:900px){\n"
        "  .layout{grid-template-columns:1fr!important}\n"
        "  .side{display:block!important;position:static;order:-1;margin:0 0 6px}\n"
        "  .side .panel{border:0;background:transparent;padding:0;box-shadow:none}\n"
        "  .side .ph{display:none}\n"
        "  .side .toc{display:flex;flex-wrap:nowrap;overflow-x:auto;gap:8px;"
        "-webkit-overflow-scrolling:touch;scrollbar-width:none;padding:2px 0 8px}\n"
        "  .side .toc::-webkit-scrollbar{display:none}\n"
        "  .side .toc a{flex:0 0 auto;border:1px solid var(--rule,#d8d2c6);border-radius:999px;"
        "padding:5px 11px;font-size:12.5px;white-space:nowrap;color:inherit;text-decoration:none}\n"
        "  .side .toc a .i{color:#9d2933;margin-right:4px}\n}\n"
        "mark.hl{background:transparent;color:#9d2933;font-weight:700;"
        "text-decoration:underline;text-decoration-color:#9d2933;"
        "text-underline-offset:.16em;text-decoration-thickness:1.5px}\n"
    )
    entry.write_text(es, encoding="utf-8")
    print("entry css overrides")


def main():
    sys.path.insert(0, str(ROOT / "scripts"))
    import inject_week
    idx = ROOT / "index.html"
    s = inject_week.inject(idx.read_text(encoding="utf-8"))
    for a, b in FIXES:
        if a in s:
            s = s.replace(a, b)
            print("fixed", a)
    if "hw-home-lockup.css" not in s:
        s = s.replace("</title>", '</title>\n<link rel="stylesheet" href="/assets/hw-home-lockup.css?v=2">', 1)
    else:
        s = re.sub(r"hw-home-lockup\.css\?v=\d+", "hw-home-lockup.css?v=2", s, count=1)
    s = s.replace('<img class="brand-logo" src="/favicon.svg" width="44" height="44"',
                  '<img class="brand-logo" src="/favicon.svg" width="36" height="36"')
    s = s.replace('dqLogoImg.src=DQ_LOGO', 'dqLogoImg.src="/favicon.svg"')
    s = re.sub(
        r"function dqToday\(\)\{return DQ\.length\?\(\(dqDayNum\(\)%DQ\.length\)\+DQ\.length\)%DQ\.length:0;\}",
        "function dqToday(){return DQ.length?Math.floor(Math.random()*DQ.length):0;}",
        s,
        count=1,
    )
    if FOOT_RE.search(s):
        s = FOOT_RE.sub(NEW_FOOT, s, count=1)
        print("dq foot aligned")
    else:
        print("dq foot block not found")
    idx.write_text(s, encoding="utf-8")
    patch_chapters()
    patch_theme()
    patch_entry_css()
    try:
        sys.path.insert(0, str(ROOT / "seo"))
        import hw_slugs
        src = idx.read_text(encoding="utf-8")
        import re as _re
        _names = _re.findall(r'n:"([^"]+)",e:"', idx.read_text(encoding="utf-8"))
        js = hw_slugs.js_map(_names) + "\nfunction slugOf(n){return (HW_SLUGS&&HW_SLUGS[n])||String(n).replace(/[·，、。\\s\\.,]/g,'');}"
        pat = re.compile(r"const HW_SLUGS=\{[\s\S]*?\};\nfunction slugOf\(n\)\{[^}]+\}")
        if pat.search(src):
            idx.write_text(pat.sub(lambda _m: js, src, count=1), encoding="utf-8")
            print("slug map ok")
    except Exception as e:
        print("slug map skipped:", e)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from pathlib import Path
import re
import sys
ROOT = Path(__file__).resolve().parents[1]

FIXES = [
    ("他流了三年干旱", "邻国连着三年干旱"),
    ("下年又乾", "第二年又乾"),
    ("役励超过收益", "役使超过产出"),
    ("项羽能打胡孩能城", "项羽能破城"),
    ("跌坡的业务", "一离开就掉队的业务"),
    ("走马火之利", "跟风求利"),
    ("苏秦在死亡边缘能改革", "秦国在死亡边缘能变法"),
    ("游历齐、宋、藏、梁", "游历齐、宋、滕、梁"),
    ("师付", "师傅"),
    ("不积跌步", "不积跬步"),
    ("塔勑布", "塔勒布"),
    ("奥缘余", "奥、意"),
    ("守彙", "守住"),
]

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

def patch_theme():
    theme = ROOT / "seo" / "hw_theme.py"
    if not theme.exists():
        return
    ts = theme.read_text(encoding="utf-8")
    ts = re.sub(
        r"    toc_html = \"\"\n    if toc:\n        items_t = \[.*?\n        toc_html = .*?\n",
        "    toc_html = \"\"\n",
        ts,
        count=1,
        flags=re.S,
    )
    ts = ts.replace("hw-chapter.css?v=1", "hw-chapter.css?v=3")
    ts = ts.replace("hw-chapter.css?v=2", "hw-chapter.css?v=3")
    ts = ts.replace("<p>本页可直接引用 <code>%s</code></p>\n    ", "")
    theme.write_text(ts, encoding="utf-8")
    print("theme patched")

def patch_chapters():
    p = ROOT / "seo" / "hw_chapters.py"
    if not p.exists():
        return
    s = p.read_text(encoding="utf-8")
    s = re.sub(
        r"\s*<aside class=\"side\">.*?</aside>",
        "",
        s,
        count=1,
        flags=re.S,
    )
    p.write_text(s, encoding="utf-8")
    print("chapters toc stripped")

def patch_entry_css():
    entry = ROOT / "assets" / "hw-entry.css"
    if not entry.exists():
        return
    es = entry.read_text(encoding="utf-8")
    block = (
        "\n.side,.layout .side{display:none!important}\n"
        ".layout{grid-template-columns:minmax(0,1fr)!important}\n"
        "mark.hl{background:none!important;color:#9d2933!important;font-weight:700!important;"
        "text-decoration:underline;text-decoration-color:#9d2933;text-underline-offset:.18em;"
        "text-decoration-thickness:1.5px;padding:0;box-shadow:none}\n"
        ".site-foot p:has(code){display:none}\n"
    )
    if ".side,.layout .side{display:none" not in es:
        entry.write_text(es + block, encoding="utf-8")
        print("entry css patched")

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
    patch_theme()
    patch_chapters()
    patch_entry_css()
    try:
        sys.path.insert(0, str(ROOT / "seo"))
        import hw_slugs
        src = idx.read_text(encoding="utf-8")
        js = hw_slugs.js_map() + "\nfunction slugOf(n){return (HW_SLUGS&&HW_SLUGS[n])||String(n).replace(/[·，、。\\s\\.,]/g,'');}"
        pat = re.compile(r"const HW_SLUGS=\{[\s\S]*?\};\nfunction slugOf\(n\)\{[^}]+\}")
        if pat.search(src):
            idx.write_text(pat.sub(lambda _m: js, src, count=1), encoding="utf-8")
            print("slug map ok")
    except Exception as e:
        print("slug map skipped:", e)

if __name__ == "__main__":
    main()

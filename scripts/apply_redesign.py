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

    once(
        ROOT / "index.html",
        '${items.map(d=>`<div class="tl-card" onclick="op(\'${d.n.replace(/\'/g,"\\\\\'")}\')">\n'
        "    <div class=\"tl-year\">${d.e}</div>\n"
        "    <div class=\"tl-name\">${d.n}</div>\n"
        "    <span class=\"tl-word\">${d.w}</span>\n"
        "  </div>`).join('')}",
        '${items.map(d=>`<a class="tl-card" href="/i/${encodeURIComponent(slugOf(d.n))}/">\n'
        "    <div class=\"tl-year\">${d.e}</div>\n"
        "    <div class=\"tl-name\">${d.n}</div>\n"
        "    <span class=\"tl-word\">${d.w}</span>\n"
        "  </a>`).join('')}",
        "cards as real /i/ links",
        True,
    )
    once(
        ROOT / "index.html",
        ".tl-card{padding:13px 14px;border-radius:12px;background:var(--white);box-shadow:var(--shadow-card);cursor:pointer;transition:box-shadow var(--dur-base) var(--ease-out-quart)}",
        ".tl-card{padding:13px 14px;border-radius:12px;background:var(--white);box-shadow:var(--shadow-card);cursor:pointer;transition:box-shadow var(--dur-base) var(--ease-out-quart);text-decoration:none;color:inherit;display:block}",
        "card link style",
    )
    once(
        ROOT / "index.html",
        '出自 <button class="dq-link" id="dqOpen" type="button"></button>',
        '出自 <a class="dq-link" id="dqOpen" href="#"></a>',
        "quote source is a real link",
    )
    once(
        ROOT / "index.html",
        'ob.textContent=s.src;ob.onclick=()=>op(s.d.n);',
        "ob.textContent=s.src;ob.href='/i/'+encodeURIComponent(slugOf(s.d.n))+'/';",
        "quote source href",
    )
    once(
        ROOT / "index.html",
        'function dqText(){const s=dqCur();return "「"+s.d.t+"」\\n—— "+s.src+"\\n\\n人类世界生存法则 · https://ourword.ai/";}',
        'function dqText(){const s=dqCur();const u="https://ourword.ai/i/"+encodeURIComponent(slugOf(s.d.n))+"/";'
        'return "「"+s.d.t+"」\\n—— "+s.src+"\\n\\n人类世界生存法则\\n"+u;}',
        "quote share includes person URL",
    )
    once(
        ROOT / "index.html",
        '      <div class="stat">古今中外 · 东西并观</div>\n    </div>\n  </header>',
        '      <div class="stat">古今中外 · 东西并观</div>\n'
        '      <button class="share-btn" type="button" data-share id="hdShare"\n'
        '        data-share-title="人类世界生存法则"\n'
        '        data-share-url="https://ourword.ai/"\n'
        '        data-share-text="人类世界生存法则\\n95 位人物与典籍的生存智慧，跨越 2600 年\\nhttps://ourword.ai/"\n'
        '        aria-label="分享本站">分享</button>\n    </div>\n  </header>',
        "homepage share button",
    )
    once(
        ROOT / "index.html",
        ".hd-stats{display:flex;gap:20px;flex-wrap:wrap}",
        ".hd-stats{display:flex;gap:20px;flex-wrap:wrap;align-items:center}"
        ".share-btn{font:inherit;font-size:12px;font-weight:600;letter-spacing:.06em;"
        "padding:5px 12px;border-radius:999px;border:1px solid var(--line-strong);"
        "background:var(--white);color:var(--ink);cursor:pointer}"
        ".share-btn:active{transform:scale(.97)}",
        "homepage share-btn css",
    )

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
    once(
        ROOT / "seo/geo_kit.py",
        "ul.idx{padding-left:18px}ul.idx li{margin:0 0 10px}\"\n)",
        "ul.idx{padding-left:18px}ul.idx li{margin:0 0 10px}"
        ".share-btn{font:inherit;font-size:13px;font-weight:600;letter-spacing:.04em;"
        "padding:7px 14px;border-radius:999px;border:1px solid rgba(28,25,23,.16);"
        "background:#efe8d8;color:#7a1e26;cursor:pointer}"
        ".share-row{margin:0 0 20px}\"\n)",
        "geo share css",
    )
    once(
        ROOT / "seo/geo_kit.py",
        "        \"<h1>%s</h1>\" % esc(it.t(zh_render)),\n"
        "        '<p class=\"lede\">%s</p>' % esc(it.s(zh_render)),",
        "        \"<h1>%s</h1>\" % esc(it.t(zh_render)),\n"
        "        '<p class=\"share-row\"><button class=\"share-btn\" type=\"button\" data-share '\n"
        "        'data-share-title=\"%s\" data-share-url=\"%s\" data-share-text=\"%s\" '\n"
        "        'aria-label=\"分享本页\">分享</button></p>'\n"
        "        % (esc(title), esc(page_url),\n"
        "           esc(\"%s\\n\\n%s\\n\\n%s\" % (it.t(zh_render), it.s(zh_render), page_url))),\n"
        "        '<p class=\"lede\">%s</p>' % esc(it.s(zh_render)),",
        "geo item share button",
    )
    once(
        ROOT / "index.html",
        "</body>\n</html>",
        '<script src="/assets/hw-share.js" defer></script>\n</body>\n</html>',
        "homepage loads hw-share.js",
    )
    once(
        ROOT / "seo/geo_kit.py",
        "            \"</main>\\n</body>\\n</html>\\n\"",
        "            \"</main>\\n<script src=\\\"/assets/hw-share.js\\\" defer></script>\\n</body>\\n</html>\\n\"",
        "geo share script tag",
    )


if __name__ == "__main__":
    main()

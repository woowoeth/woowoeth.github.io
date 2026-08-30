# -*- coding: utf-8 -*-
"""Child essays hanging off a person/book map page. Not part of D[]."""
import json
import os
import sys
from geo_kit import esc, SITE, sibling_links
import hw_theme

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

SLOGAN = "遇到事了，看看以前的人怎么处理"


HL = '<mark class="hl" style="background:transparent;color:#9d2933;font-weight:700">%s</mark>'
def rich(s):
    parts = str(s or "").split("==")
    out = []
    for i, p in enumerate(parts):
        t = esc(p)
        out.append((HL % t) if i % 2 else t)
    return "".join(out)


# ---------------------------------------------------------------- data loading
# One module per parent under seo/chapters/. A single literal was fine for five
# chapters; at a few hundred it becomes an unreviewable diff every time one line
# changes. Each module exposes PARENT (catalog spec) and CHAPTERS (the essays).
PARENTS, CHAPTERS = {}, []


def _load():
    import importlib
    import pkgutil
    here = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chapters")
    if not os.path.isdir(here):
        return
    for mod in sorted(m.name for m in pkgutil.iter_modules([here])):
        m = importlib.import_module("chapters." + mod)
        spec = dict(getattr(m, "PARENT", {}) or {})
        name = spec.pop("name", "")
        if not name:
            continue
        PARENTS.setdefault(name, spec)
        for ch in getattr(m, "CHAPTERS", []) or []:
            ch.setdefault("parent", name)
            ch.setdefault("parent_slug", spec.get("slug", ""))
            CHAPTERS.append(ch)
    CHAPTERS.sort(key=lambda c: (c["parent_slug"], _order(c)))


def _order(ch):
    items = PARENTS.get(ch["parent"], {}).get("items", [])
    keys = [it["k"] for it in items]
    return keys.index(ch["k"]) if ch["k"] in keys else 99


_load()


def _register_quotes():
    """Tell hw_theme which lines the child essays already carry.

    A chapter is the deep read on exactly that line, so the quote belongs there;
    repeating it in the parent entry's 金句 list makes a reader who follows the
    link meet it twice.
    """
    table = {}
    for ch in CHAPTERS:
        for q in ch["q"]:
            table.setdefault(ch["parent"], set()).add(
                "".join(c for c in str(q).replace("==", "") if c not in hw_theme._STRIP))
    hw_theme.CHAPTER_QUOTES = table


_register_quotes()


def f_span_raw(source, plain_span):
    """Map a span picked from the plain text back onto the ==marked== original.

    The marker is a toggle, not a segment count. Emitting one "==" per segment
    crossed meant a span starting just after a highlight opened with "====",
    which rich() renders as an empty <mark></mark>.
    """
    flat, seg = [], []
    for i, chunk in enumerate(str(source or "").split("==")):
        for ch in chunk:
            flat.append(ch)
            seg.append(i)
    plain = "".join(flat)
    at = plain.find(plain_span)
    if at < 0:
        return plain_span
    out, inside = [], False
    for k in range(at, at + len(plain_span)):
        want = bool(seg[k] % 2)
        if want != inside:
            out.append("==")
            inside = want
        out.append(flat[k])
    if inside:
        out.append("==")
    return "".join(out)


def catalog_html(title):
    spec = PARENTS.get(title)
    if not spec:
        return ""
    live = [it for it in spec["items"] if it.get("ready")]
    if not live:
        return ""
    rows = []
    for it in live:
        href = "/i/%s/%s/" % (spec["slug"], it["k"])
        rows.append(
            '<a class="map-row" href="%s">'
            '<span class="map-n">%s</span>'
            '<span class="map-w">%s</span>'
            '<span class="map-line">%s</span></a>'
            % (esc(href), esc(it["n"]), esc(it["w"]), esc(it["line"]))
        )
    return (
        '<section class="map-cat" id="map">'
        '<h2 class="sec-k">%s</h2>'
        '<div class="map-list">%s</div></section>'
        % (esc(spec["blurb"]), "".join(rows))
    )


def inject_catalog(blocks_html, title):
    if 'class="map-cat"' in (blocks_html or ""):
        return blocks_html
    chunk = catalog_html(title)
    if not chunk:
        return blocks_html
    for mark in ('<section id="contrast"', '<section id="ext"'):
        if mark in blocks_html:
            return blocks_html.replace(mark, chunk + mark, 1)
    return blocks_html + chunk


def _sib(ch, idx):
    prev_html = next_html = ""
    if idx > 0:
        p = CHAPTERS[idx - 1]
        prev_html = (
            '<a href="/i/%s/%s/"><span class="dir">上一篇</span>%s</a>'
            % (p["parent_slug"], p["k"], esc(p["n"]))
        )
    else:
        prev_html = (
            '<a href="/i/%s/"><span class="dir">回</span>%s</a>'
            % (ch["parent_slug"], esc(ch["parent"]))
        )
    if idx < len(CHAPTERS) - 1:
        n = CHAPTERS[idx + 1]
        next_html = (
            '<a href="/i/%s/%s/" style="text-align:right;margin-left:auto">'
            '<span class="dir">下一篇</span>%s</a>'
            % (n["parent_slug"], n["k"], esc(n["n"]))
        )
    else:
        next_html = (
            '<a href="/i/%s/" style="text-align:right;margin-left:auto">'
            '<span class="dir">回</span>%s</a>'
            % (ch["parent_slug"], esc(ch["parent"]))
        )
    return prev_html, next_html


def _chapter_page(ch, idx):
    parent = ch["parent"]
    parent_url = "%s/i/%s/" % (SITE, ch["parent_slug"])
    page_url = "%s/i/%s/%s/" % (SITE, ch["parent_slug"], ch["k"])
    title = "%s — %s — 人类世界生存法则" % (ch["n"], parent)
    points = []
    toc = [("s2", "背后是什么故事")]
    for i, f in enumerate(ch["f"], 1):
        aid = "p%d" % i
        toc.append((aid, f["n"]))
        points.append(
            '<section class="point" id="%s"><h2>%s</h2><p>%s</p>%s</section>'
            % (
                aid, rich(f["n"]), rich(f["d"]),
                ('<p class="eg">%s</p>' % rich(f["eg"])) if f.get("eg") else "",
            )
        )
    # Same rule as the entry pages: a 金句 the reader already met in the body is
    # not worth a second printing at the foot.
    _seen = _bare(ch["story"]) + _bare(ch["dek"]) + "".join(
        _bare(f.get("n", "")) + _bare(f.get("d", "")) + _bare(f.get("eg", ""))
        for f in ch["f"]) + _bare(ch["apply"])
    _keep = [q for q in ch["q"] if _bare(q) and not hw_theme._echoes(q, _seen)]
    quotes = "".join("<blockquote><p>%s</p></blockquote>" % rich(q) for q in _keep)
    toc += [("s7", "今天怎么用")] + ([("quotes", "金句")] if _keep else [])
    # 金句: 1-3 lines lifted from the 分则 they close (option A), plus the full
    # 原文 list restored as a section at the foot.
    import hw_theme as _t
    cands = []
    import re as _re
    for i, f in enumerate(ch["f"]):
        whole = _plain(f["d"]) + _plain(f.get("eg", ""))
        for src, penalty in ((_plain(f["d"]), 0.0), (_plain(f.get("eg", "")), 0.8)):
            for span in _t._spans(src):
                if len(whole) - len(span) < 45:      # excerpt, not the section
                    continue
                if len(src) - len(span) < 20:        # …and not a whole paragraph
                    continue
                own = _re.sub(r"\u300c[^\u300d]*\u300d", "", span)
                if len(own.strip("\u3002\uff0c\u3001\uff01\uff1f\uff1b\uff1a\u2014 ")) < 20:
                    continue
                cands.append((i, span, _t._quotability(span) - penalty))
    want = max(1, min(3, len(ch["f"])))
    shown = {_plain(f["d"]) for f in ch["f"]} | {_plain(f.get("eg", "")) for f in ch["f"]}
    shown |= {x for f in ch["f"] for x in _t._breathe(_plain(f["d"]))}
    chosen = _t._pick_pullquotes([c for c in cands if c[2] > 0 and c[1] not in shown], want)
    after = {}
    for i, span, _sc in chosen:
        raw = f_span_raw(ch["f"][i]["d"], span)
        after[i] = '<blockquote class="say"><p>%s</p></blockquote>' % rich(raw)
    body_points = "\n".join(
        pt + ("\n" + after[i] if i in after else "") for i, pt in enumerate(points))
    apply_paras = "".join("<p>%s</p>" % rich(p)
                          for p in ch["apply"].split("\n") if p.strip())
    toc_html = "".join(
        '<a href="#%s"><span class="i">%02d</span>%s</a>' % (esc(a), i, esc(n))
        for i, (a, n) in enumerate(toc, 1)
    )
    share = hw_theme._share_btn(title, page_url, "%s\n\n%s\n\n%s" % (ch["n"], ch["dek"], page_url))
    prev_html, next_html = _sib(ch, idx)
    body = """
<header class="mast wrap">
  <div class="mast-top">
    %s
    <div class="mast-links">
      <a class="pill" href="%s">回%s</a>
      <a class="pill" href="%s/">首页</a>
    </div>
  </div>
</header>
<div class="wrap">
  <nav class="crumb">
    <a href="%s/">首页</a><span class="sep">/</span>
    <a href="%s">%s</a><span class="sep">/</span>%s
  </nav>
  <div class="layout">
    <article>
      <p class="kicker">%s</p>
      <h1>%s</h1>
      <p class="one">%s</p>
      <p class="src">%s</p>
      <p class="dek">%s</p>
      <div class="meta-row"><span class="chip">%s</span><span class="chip">%s</span>%s</div>
      <section class="sec" id="s2"><h2 class="sec-k">背后是什么故事？</h2>
      <p>%s</p></section>
      %s
      <section class="sec apply" id="s7"><h2 class="sec-k">今天怎么用？</h2>%s</section>
      %s
    </article>
    <aside class="side"><div class="panel"><p class="ph">本篇结构</p><nav class="toc">%s</nav></div></aside>
  </div>
  <nav class="sib">%s%s</nav>
  <footer class="site-foot">
    <p>本页可直接引用 <code>%s</code></p>
    <p>%s</p>
  </footer>
</div>
""" % (
        hw_theme.brand_html(SITE + "/", SLOGAN),
        esc(parent_url), esc(parent), esc(SITE),
        esc(SITE), esc(parent_url), esc(parent), esc(ch["n"]),
        esc(parent), esc(ch["n"]), esc(ch["w"]), esc(ch["src"]), rich(ch["dek"]),
        esc(parent), esc(ch["w"]), share,
        rich(ch["story"]), body_points, apply_paras,
        ('<section class="quotes" id="quotes"><h2 class="sec-k">金句</h2>%s</section>'
         % quotes) if quotes else "",
        toc_html, prev_html, next_html,
        esc(page_url), sibling_links(None, True),
    )
    # Entry pages get og:image / twitter cards / robots from geo_kit's head_block.
    # Chapter pages are built by hand here, so they shipped without any of it and
    # shared as a bare link with no preview card.
    dek = _plain(ch["dek"])
    ld = {
        "@context": "https://schema.org", "@type": "Article",
        "headline": ch["n"], "name": ch["n"], "url": page_url,
        "description": dek, "inLanguage": "zh-Hans",
        "articleSection": "\u6df1\u5ea6\u9605\u8bfb",
        "about": {"@type": "Person", "name": parent, "url": parent_url},
        "isPartOf": {"@type": "WebSite", "name": "\u4eba\u7c7b\u4e16\u754c\u751f\u5b58\u6cd5\u5219",
                     "url": SITE + "/"},
        "publisher": {"@type": "Organization", "name": "OurWord AI", "url": SITE + "/"},
        "mainEntityOfPage": {"@type": "WebPage", "@id": page_url},
    }
    crumbs = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "OurWord AI", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": parent, "item": parent_url},
            {"@type": "ListItem", "position": 3, "name": ch["n"], "item": page_url},
        ],
    }
    head = (
        '<meta name="description" content="%s">\n'
        '<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">\n'
        '<link rel="canonical" href="%s">\n'
        '<meta property="og:type" content="article">\n'
        '<meta property="og:site_name" content="Human World">\n'
        '<meta property="og:locale" content="zh_CN">\n'
        '<meta property="og:title" content="%s">\n'
        '<meta property="og:description" content="%s">\n'
        '<meta property="og:url" content="%s">\n'
        '<meta property="og:image" content="%s/og.png">\n'
        '<meta property="og:image:width" content="1200">\n'
        '<meta property="og:image:height" content="630">\n'
        '<meta property="og:image:alt" content="Human World">\n'
        '<meta name="twitter:card" content="summary_large_image">\n'
        '<meta name="twitter:site" content="@futuredotnews">\n'
        '<meta name="twitter:title" content="%s">\n'
        '<meta name="twitter:description" content="%s">\n'
        '<meta name="twitter:image" content="%s/og.png">\n'
        '<script type="application/ld+json">%s</script>\n'
        '<script type="application/ld+json">%s</script>\n'
        % (esc(dek), page_url, esc(title), esc(dek), page_url, SITE,
           esc(title), esc(dek), SITE,
           json.dumps(ld, ensure_ascii=False), json.dumps(crumbs, ensure_ascii=False))
    )
    return hw_theme._shell("zh-Hans", title, head, body)


def write_chapters(root="."):
    n = 0
    for i, ch in enumerate(CHAPTERS):
        path = os.path.join(root, "i", ch["parent_slug"], ch["k"], "index.html")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w", encoding="utf-8").write(_chapter_page(ch, i))
        n += 1
    return n


# ------------------------------------------------------------------ index layer
# Chapter pages are not in D[], so geo_kit never sees them. Without this block
# they exist but are invisible to sitemap.xml / llms.txt / llms-full.txt / feed.xml
# — i.e. invisible to exactly the crawlers the whole SEO layer exists for.
_BEGIN = "<!-- chapters:begin -->"
_END = "<!-- chapters:end -->"


_STRIP = "\u300c\u300d\u201c\u201d\u3002\uff0c\u3001\uff01\uff1f\uff1b\uff1a\u2014\u2026 .,!?;:"


def _bare(t):
    return "".join(c for c in _plain(t) if c not in _STRIP)


def _plain(s):
    return str(s or "").replace("==", "").strip()


def chapter_url(ch):
    return "%s/i/%s/%s/" % (SITE, ch["parent_slug"], ch["k"])


def chapter_urls():
    """Absolute URLs, for geo_kit.build(extra_urls=...) -> sitemap.xml."""
    return [chapter_url(ch) for ch in CHAPTERS]


def chapter_summary(ch):
    return "%s · %s——%s。%s" % (ch["parent"], ch["n"], ch["w"], _plain(ch["dek"]))


def _llms_block():
    L = ["## Deep reads 深度阅读", "",
         "Long-form chapters hanging off a person page. Not part of the entry index above.",
         ""]
    for ch in CHAPTERS:
        L.append("- [%s · %s](%s): %s"
                 % (ch["parent"], ch["n"], chapter_url(ch), chapter_summary(ch)))
    L.append("")
    return "\n".join(L)


def _llms_full_block():
    F = []
    for ch in CHAPTERS:
        F += ["=" * 72, "## %s · %s" % (ch["parent"], ch["n"]),
              "URL: %s" % chapter_url(ch),
              "Source: %s" % _plain(ch["src"]),
              "Tags: 深度阅读, %s, %s" % (ch["parent"], ch["w"]), "",
              _plain(ch["dek"]), "",
              "### Q：背后是什么故事？", _plain(ch["story"]), ""]
        for f in ch["f"]:
            body = _plain(f["d"])
            if f.get("eg"):
                body += "\n例：" + _plain(f["eg"])
            F += ["### 分则 · %s" % _plain(f["n"]), body, ""]
        F += ["### Q：今天怎么用？", _plain(ch["apply"]), "",
              "### 金句", "\n".join(_plain(q) for q in ch["q"]), ""]
    return "\n".join(F)


def _rss_block():
    xs = []
    for ch in CHAPTERS:
        u = chapter_url(ch)
        xs.append("    <item><title>%s · %s</title><link>%s</link>"
                  "<guid isPermaLink=\"true\">%s</guid><description>%s</description></item>"
                  % (esc(ch["parent"]), esc(ch["n"]), esc(u), esc(u),
                     esc(chapter_summary(ch))))
    return "\n".join(xs)


def _splice(path, block, anchor, before):
    """Idempotent: drop any previous chapters block, then insert a fresh one."""
    if not os.path.exists(path):
        return False
    src = open(path, encoding="utf-8").read()
    cur = src
    if _BEGIN in cur and _END in cur:
        cur = cur[:cur.index(_BEGIN)] + cur[cur.index(_END) + len(_END):]
    chunk = "%s\n%s\n%s\n" % (_BEGIN, block, _END)
    if anchor and anchor in cur:
        at = cur.index(anchor) + (0 if before else len(anchor))
        out = cur[:at] + chunk + cur[at:]
    else:
        out = cur.rstrip("\n") + "\n" + chunk
    if out == src:
        return False
    open(path, "w", encoding="utf-8").write(out)
    return True


def write_indexes(root="."):
    """Fold chapters into the artefacts geo_kit already wrote. Call after build()."""
    return {
        "llms": _splice(os.path.join(root, "llms.txt"),
                        _llms_block(), "## Citing", True),
        "llms_full": _splice(os.path.join(root, "llms-full.txt"),
                             _llms_full_block(), None, False),
        "rss": _splice(os.path.join(root, "feed.xml"),
                       _rss_block(), "    <language>zh-cn</language>\n", False),
    }


def chapter_fingerprints():
    """Content hash per chapter URL key, for the lastmod manifest in build_seo."""
    import hashlib
    out = {}
    for ch in CHAPTERS:
        h = hashlib.sha1()
        for part in (ch["n"], ch["w"], ch["src"], ch["dek"], ch["story"], ch["apply"]):
            h.update(("%s\x00" % _plain(part)).encode("utf-8"))
        for f in ch["f"]:
            for k in ("n", "d", "eg"):
                h.update(("%s\x00" % _plain(f.get(k, ""))).encode("utf-8"))
        for q in ch["q"]:
            h.update(("%s\x00" % _plain(q)).encode("utf-8"))
        out["i/%s/%s/" % (ch["parent_slug"], ch["k"])] = h.hexdigest()[:16]
    return out

# -*- coding: utf-8 -*-
"""Editorial item-page theme for Human World."""
import geo_kit as _gk
from geo_kit import esc, clip, SITE, org_ld, item_ld, breadcrumb_ld, faq_ld
from geo_kit import head_block, ga_block, sibling_links

CSS = ""

SHARE_SVG = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<path d="M12 3v11M12 3 8.5 6.5M12 3l3.5 3.5"/>'
    '<path d="M5 13v6a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-6"/></svg>'
)

def brand_html(home_href, slogan=""):
    extra = ('<span class="slogan">%s</span>' % esc(slogan)) if slogan else ""
    return (
        '<a class="brand" href="%s">'
        '<img class="brand-logo" src="/favicon.svg" width="36" height="36" alt="">'
        '<span class="brand-copy">'
        '<span class="wordmark">人类世界<span class="dot">生存法则</span></span>'
        '%s</span></a>'
    ) % (esc(home_href), extra)

def _paras(text):
    return [p.strip() for p in str(text).split("\n") if p.strip()]

def _share_btn(title, url, text):
    return (
        '<button class="share-btn" type="button" data-share '
        'data-share-title="%s" data-share-url="%s" data-share-text="%s" '
        'aria-label="分享本页">%s 分享</button>'
        % (esc(title), esc(url), esc(text), SHARE_SVG)
    )

def _say(text):
    """One 金句, set into the flow between sections."""
    return '<figure class="say"><blockquote><p>%s</p></blockquote></figure>' % esc(text)


_STRIP = "\u300c\u300d\u201c\u201d\u2018\u2019\u3002\uff0c\u3001\uff01\uff1f\uff1b\uff1a\u2014\u2026 .,!?;:\"'"


def _bare(t):
    return "".join(c for c in str(t or "") if c not in _STRIP)


def _weave(html, slots, quotes, texts):
    """Spread the 金句 evenly over the gaps between sections.

    They used to sit in one block at the very bottom, which nobody scrolls to.
    `slots` are indices into `html` (after the story section and after each
    分则); insert back-to-front so earlier indices stay valid.

    Most 分则 open by quoting the same line that is in q[], so a quote dropped
    next to its own section reads as a stutter. `texts` holds the plain text of
    the section on either side of each slot; a quote already present there is
    nudged to the nearest slot where it is not.
    """
    if not quotes or not slots:
        return html
    quotes = quotes[:len(slots)]
    step = len(slots) / float(len(quotes))
    picked = []
    for i, q in enumerate(quotes):
        want = min(max(int(i * step + step / 2), 0), len(slots) - 1)
        bare = _bare(q)
        order = sorted(range(len(slots)), key=lambda j: (abs(j - want), j))
        choice = None
        for j in order:                       # first pass: no echo, not taken
            if j in picked:
                continue
            near = list(texts[j]) + (list(texts[j + 1]) if j + 1 < len(texts) else [])
            if bare and any(bare in _bare(t) for t in near):
                continue
            choice = j
            break
        if choice is None:                    # fall back to any free slot
            choice = next((j for j in order if j not in picked), want)
        picked.append(choice)
    for q, j in sorted(zip(quotes, picked), key=lambda pair: -pair[1]):
        html.insert(slots[j], _say(q))
    return html


def _render_blocks(it, zh):
    html, toc, first_q, n = [], [], True, 0
    slots, quotes, around = [], [], []
    for h, b in it.b(zh):
        if (h or "").strip() in ("金句", "原话"):
            quotes = _paras(b)
            continue
    for h, b in it.b(zh):
        h = (h or "").strip()
        paras = _paras(b)
        if not paras:
            continue
        if h.startswith("分则"):
            name = h.split("·", 1)[-1].strip() if "·" in h else h
            n += 1
            aid = "p%d" % n
            toc.append((aid, name))
            body, egs = [], []
            for p in paras:
                if p.startswith("例：") or p.startswith("例:"):
                    egs.append(p.split("：", 1)[-1].split(":", 1)[-1])
                else:
                    body.append(p)
            html.append('<section class="point" id="%s">' % aid)
            html.append("<h2>%s</h2>" % esc(name))
            html.extend("<p>%s</p>" % esc(p) for p in body)
            html.extend('<p class="eg">%s</p>' % esc(p) for p in egs)
            html.append("</section>")
            slots.append(len(html))
            around.append([name] + paras)   # heading counts: several 分则 are titled with the quote
            continue
        if h in ("金句", "原话"):
            continue  # woven into the flow by _weave below
        if "对照" in h:
            toc.append(("contrast", "对照着读"))
            html.append('<section id="contrast"><h2 class="sec-k">和谁对照着读</h2><div class="contrast">')
            for p in paras:
                name, why = (p.split("：", 1) + [""])[:2] if "：" in p else (p, "")
                html.append(
                    '<a href="/i/%s/"><span class="n">%s</span><span class="why">%s</span></a>'
                    % (esc(_slug(name)), esc(name), esc(why))
                )
            html.append("</div></section>")
            continue
        if h == "延伸":
            toc.append(("ext", "延伸"))
            html.append('<section id="ext"><h2 class="sec-k">延伸</h2><div class="ext">')
            for p in paras:
                # Entry names may legitimately contain 、 or ，（思考，快与慢 /
                # 枪炮、病菌与钢铁）. Splitting on them produced /i/思考/ and
                # /i/枪炮/ — links to pages that never existed. Only fall back to
                # splitting when the whole line is not itself a known entry.
                # Split on whitespace ONLY. Entry names never contain a space,
                # but two of them contain 、 / ， (思考，快与慢 和
                # 枪炮、病菌与钢铁) — splitting on those produced
                # /i/思考/ and /i/枪炮/, links to pages that never existed.
                for name in (x.strip("·,，、 ") for x in p.split()):
                    if name:
                        html.append('<a href="/i/%s/">%s</a>' % (esc(_slug(name)), esc(name)))
            html.append("</div></section>")
            continue
        label = h
        if label.startswith("Q：") or label.startswith("Q:"):
            label = label.split("：", 1)[-1].split(":", 1)[-1]
        if first_q and ("留下" in h):
            first_q = False
            html.append('<aside class="pull">%s</aside>' % esc(paras[0]))
            if len(paras) > 1:
                html.append('<section class="sec">')
                html.extend("<p>%s</p>" % esc(p) for p in paras[1:])
                html.append("</section>")
            continue
        n += 1
        aid = "s%d" % n
        toc.append((aid, label))
        klass = "sec apply" if "今天" in h else "sec"
        html.append('<section class="%s" id="%s"><h2 class="sec-k">%s</h2>' % (klass, aid, esc(label)))
        html.extend("<p>%s</p>" % esc(p) for p in paras)
        html.append("</section>")
        if klass == "sec":
            slots.append(len(html))
            around.append([label] + paras)
    return "\n".join(_weave(html, slots, quotes, around)), toc

def item_page(site, it, items, idx, zh, hub_of=None):
    zh_render = zh or site.zh()
    page_url = it.page(site, zh)
    alt_url = site.url(("i/%s/" if zh else "zh/i/%s/") % it.slug) if it.has_zh() else ""
    title = clip("%s — %s" % (it.t(zh_render), site.name_zh if zh_render else site.name), 70)
    ld = [org_ld(), item_ld(site, it, zh_render, page_url), breadcrumb_ld(site, it, zh_render)]
    f = faq_ld(it, zh_render)
    if f:
        ld.append(f)
    tags = it.tags or []
    cat = tags[0] if tags else ""
    one = tags[-1] if len(tags) >= 2 else ""
    eras = ("先秦与古典时代", "秦汉至魏晋", "中古", "近世", "工业时代", "现代")
    if one in eras:
        one = ""
    era = next((t for t in tags if t in eras), "")
    share_text = "%s\n\n%s\n\n%s" % (it.t(zh_render), it.s(zh_render), page_url)
    blocks_html, toc = _render_blocks(it, zh_render)
    try:
        import hw_chapters
        blocks_html = hw_chapters.inject_catalog(blocks_html, it.title)
    except Exception:
        pass
    toc_html = ""
    if toc:
        items_t = ['<a href="#%s"><span class="i">%02d</span>%s</a>' % (esc(a), i, esc(n)) for i, (a, n) in enumerate(toc, 1)]
        toc_html = '<aside class="side"><div class="panel"><p class="ph">本篇结构</p><nav class="toc">%s</nav></div></aside>' % "".join(items_t)
    ordered = []
    if era:
        ordered.append(era)
    for t in tags:
        if t not in ordered:
            ordered.append(t)
    chips = []
    for t in ordered:
        sl = _slug(t)
        if hub_of and hub_of.get(sl):
            chips.append('<a class="chip" href="%s">%s</a>' % (esc(site.url("t/%s/" % sl)), esc(t)))
        else:
            chips.append('<span class="chip">%s</span>' % esc(t))
    prev_html = next_html = ""
    if idx > 0:
        p = items[idx - 1]
        prev_html = '<a href="%s"><span class="dir">上一篇</span>%s</a>' % (esc(site.url("i/%s/" % p.slug)), esc(p.t(zh_render)))
    if idx < len(items) - 1:
        nxt = items[idx + 1]
        next_html = '<a href="%s" style="text-align:right;margin-left:auto"><span class="dir">下一篇</span>%s</a>' % (esc(site.url("i/%s/" % nxt.slug)), esc(nxt.t(zh_render)))
    body = """
<header class="mast wrap">
  <div class="mast-top">
    %s
    <div class="mast-links">
      <a class="pill" href="%s">目录</a>
      <a class="pill" href="%s">全部</a>
    </div>
  </div>
</header>
<div class="wrap">
  <nav class="crumb">
    <a href="%s">首页</a><span class="sep">/</span>
    <a href="%s">%s</a><span class="sep">/</span>%s
  </nav>
  <div class="layout">
    <article>
      %s
      <h1>%s</h1>
      %s
      <p class="dek">%s</p>
      <div class="meta-row">%s%s</div>
      %s
    </article>
    %s
  </div>
  <nav class="sib">%s%s</nav>
  <footer class="site-foot">
    <p>本页可直接引用 <code>%s</code></p>
    <p><a href="%s">llms.txt</a> · <a href="%s">llms-full.txt</a></p>
    <p>%s</p>
  </footer>
</div>
""" % (
        brand_html(SITE + "/", site.tagline_zh if zh_render else site.tagline),
        esc(site.base), esc(site.url("all/")),
        esc(SITE + "/"), esc(site.base), esc(site.name_zh if zh_render else site.name),
        esc(it.t(zh_render)),
        ('<p class="kicker">%s</p>' % esc(cat)) if cat else "",
        esc(it.t(zh_render)),
        ('<p class="one">%s</p>' % esc(one)) if one else "",
        esc(it.s(zh_render)),
        "".join(chips),
        _share_btn(title, page_url, share_text),
        blocks_html, toc_html, prev_html, next_html,
        esc(page_url), esc(site.url("llms.txt")), esc(site.url("llms-full.txt")),
        sibling_links(site, zh_render),
    )
    return _shell("zh-Hans" if zh_render else "en", title,
                  head_block(site, page_url, title, it.s(zh_render), zh=zh_render, alt_url=alt_url, ld=ld, item=it),
                  body)

def _shell(lang, title, headhtml, body):
    return (
        "<!DOCTYPE html>\n<html lang=\"%s\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n"
        "<title>%s</title>\n%s\n%s\n"
        "<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n"
        "<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>\n"
        "<link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/css2?"
        "family=Noto+Serif+SC:wght@500;600;700&display=swap\">\n"
        "<link rel=\"stylesheet\" href=\"/assets/hw-entry.css?v=9\">\n"
        "<link rel=\"stylesheet\" href=\"/assets/hw-chapter.css?v=4\">\n"
        "</head>\n<body>\n%s\n"
        "<script src=\"/assets/hw-share.js\" defer></script>\n</body>\n</html>\n"
        % (lang, esc(title), headhtml, ga_block(), body)
    )

def _slug(name):
    """Resolve through geo_kit at CALL time.

    build_seo swaps in a slug map with `G.slugify = ...`, but this module did
    `from geo_kit import slugify` at import, so it kept the original function and
    every 延伸 / 对照 / 标签 link came out as a CJK URL (/i/韩非子/ instead of
    /i/han-feizi/) that only resolved through a legacy redirect stub.
    """
    return _gk.slugify(name)


def _known(name):
    """True when `name` resolves to a real (latin) slug, i.e. it is an entry title."""
    if not name:
        return False
    try:
        import hw_slugs
        sl = hw_slugs.slug_for(name)
    except Exception:
        return False
    return bool(sl) and not any("\u4e00" <= ch <= "\u9fff" for ch in sl)


def install(G):
    G._PAGE_CSS = CSS
    G._shell = _shell
    G.item_page = item_page
    import hw_list
    hw_list.install(G)

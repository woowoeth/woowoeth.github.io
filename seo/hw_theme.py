# -*- coding: utf-8 -*-
"""Editorial item-page theme for Human World."""
from geo_kit import esc, clip, SITE, org_ld, item_ld, breadcrumb_ld, faq_ld
from geo_kit import head_block, ga_block, sibling_links, slugify

CSS = ""

SHARE_SVG = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<path d="M12 3v11M12 3 8.5 6.5M12 3l3.5 3.5"/>'
    '<path d="M5 13v6a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-6"/></svg>'
)

def _paras(text):
    return [p.strip() for p in str(text).split("\n") if p.strip()]

def _share_btn(title, url, text):
    return (
        '<button class="share-btn" type="button" data-share '
        'data-share-title="%s" data-share-url="%s" data-share-text="%s" '
        'aria-label="分享本页">%s 分享</button>'
        % (esc(title), esc(url), esc(text), SHARE_SVG)
    )

def _render_blocks(it, zh):
    html, toc, first_q, n = [], [], True, 0
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
            continue
        if h == "原话":
            toc.append(("quotes", "原话"))
            html.append('<section class="quotes" id="quotes"><h2 class="sec-k">原话</h2>')
            for p in paras:
                html.append("<blockquote><p>%s</p></blockquote>" % esc(p))
            html.append("</section>")
            continue
        if "对照" in h:
            toc.append(("contrast", "对照着读"))
            html.append('<section id="contrast"><h2 class="sec-k">和谁对照着读</h2><div class="contrast">')
            for p in paras:
                name, why = (p.split("：", 1) + [""])[:2] if "：" in p else (p, "")
                html.append(
                    '<a href="/i/%s/"><span class="n">%s</span><span class="why">%s</span></a>'
                    % (esc(slugify(name)), esc(name), esc(why))
                )
            html.append("</div></section>")
            continue
        if h == "延伸":
            toc.append(("ext", "延伸"))
            html.append('<section id="ext"><h2 class="sec-k">延伸</h2><div class="ext">')
            for p in paras:
                for name in p.replace("、", " ").replace("，", " ").split():
                    name = name.strip("·,，、 ")
                    if name:
                        html.append('<a href="/i/%s/">%s</a>' % (esc(slugify(name)), esc(name)))
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
    return "\n".join(html), toc

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
    toc_html = ""
    if toc:
        items_t = ['<a href="#%s"><span class="i">%02d</span>%s</a>' % (esc(a), i, esc(n)) for i, (a, n) in enumerate(toc, 1)]
        toc_html = '<aside class="side"><div class="panel"><p class="ph">本篇结构</p><nav class="toc">%s</nav></div></aside>' % "".join(items_t)
    tag_bits = []
    for t in tags:
        sl = slugify(t)
        if hub_of and hub_of.get(sl):
            tag_bits.append('<a href="%s">%s</a>' % (esc(site.url("t/%s/" % sl)), esc(t)))
        else:
            tag_bits.append("<span>%s</span>" % esc(t))
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
    <a class="brand" href="%s">
      <span class="hw">HUMAN WORLD</span>
      <span class="wordmark">人类世界<span class="dot">生存法则</span></span>
    </a>
    <div class="mast-links">
      <a class="pill" href="%s">目录</a>
      <a class="pill" href="%s">全部</a>
    </div>
  </div>
  <p class="slogan">%s</p>
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
        esc(SITE + "/"), esc(site.base), esc(site.url("all/")),
        esc(site.tagline_zh if zh_render else site.tagline),
        esc(SITE + "/"), esc(site.base), esc(site.name_zh if zh_render else site.name),
        esc(it.t(zh_render)),
        ('<p class="kicker">%s</p>' % esc(cat)) if cat else "",
        esc(it.t(zh_render)),
        ('<p class="one">%s</p>' % esc(one)) if one else "",
        esc(it.s(zh_render)),
        ('<span class="when">%s</span>' % esc(era)) if era else "",
        _share_btn(title, page_url, share_text),
        ('<p class="tags">%s</p>' % "".join(tag_bits)) if tag_bits else "",
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
        "<link rel=\"stylesheet\" href=\"/assets/hw-entry.css\">\n"
        "</head>\n<body>\n%s\n"
        "<script src=\"/assets/hw-share.js\" defer></script>\n</body>\n</html>\n"
        % (lang, esc(title), headhtml, ga_block(), body)
    )

def install(G):
    G._PAGE_CSS = CSS
    G._shell = _shell
    G.item_page = item_page
    import hw_list
    hw_list.install(G)

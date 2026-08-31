# -*- coding: utf-8 -*-
"""Editorial item-page theme for Human World."""
import re
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
    return '<blockquote class="say"><p>%s</p></blockquote>' % esc(text)


_STRIP = "\u300c\u300d\u201c\u201d\u2018\u2019\u3002\uff0c\u3001\uff01\uff1f\uff1b\uff1a\u2014\u2026 .,!?;:\"'"


def _bare(t):
    return "".join(c for c in str(t or "") if c not in _STRIP)


_ENDS = "。！？"
_MIN, _MAX = 18, 145


def _breathe(text, target=120, floor=45):
    """Break a wall of text at sentence boundaries.

    story fields run to 350 characters — twelve lines, close to two phone
    screens, as a single <p>. Nothing is reworded; the paragraph just gets
    somewhere to breathe.
    """
    if len(text) <= 165:
        return [text]
    parts = [x for x in re.split(r"(?<=[\u3002\uff01\uff1f])", text) if x.strip()]
    out, buf = [], ""
    for x in parts:
        buf += x
        if len(buf) >= target:
            out.append(buf)
            buf = ""
    if buf:
        if out and len(buf) < floor:
            out[-1] += buf
        else:
            out.append(buf)
    return out or [text]


def _spans(text):
    """Sentences, plus runs of adjacent sentences, as pull-quote candidates."""
    parts = [x for x in re.split(r"(?<=[%s])" % _ENDS, text) if x.strip()]
    out = []
    for i in range(len(parts)):
        run = ""
        for j in range(i, min(i + 3, len(parts))):
            run += parts[j]
            if _MIN <= len(run) <= _MAX:
                out.append(run.strip())
    return out


def _quotability(t):
    """What makes a line worth blowing up: a quotation inside it, a dash landing
    a verdict, an X-not-Y turn. What kills it: dates, numbers, worked examples."""
    if not (_MIN <= len(t) <= _MAX):
        return -1.0
    s = 0.0
    if "\u300c" in t and "\u300d" in t:
        s += 2.2
    if "\u2014\u2014" in t:
        s += 1.3
    if "\u4e0d\u662f" in t and "\u800c\u662f" in t:
        s += 1.4
    elif "\u4e0d\u662f" in t or "\u800c\u662f" in t:
        s += 0.6
    for w in ("\u53ea\u6709", "\u624d\u7b97", "\u6c38\u8fdc", "\u4ece\u6765",
              "\u672c\u8d28\u4e0a", "\u5b9e\u9645\u4e0a", "\u771f\u6b63"):
        if w in t:
            s += 0.4
    if re.search(r"\d{3,}|\d+\s*[\u5e74\u6708\u4ebf\u4e07%]", t):
        s -= 1.6
    for w in ("\u4f8b\uff1a", "\u6bd4\u5982", "\u4f8b\u5982", "\u516c\u53f8\u7248"):
        if w in t:
            s -= 1.2
    s += min(t.count("\uff0c"), 4) * 0.12
    return s


def _pick_pullquotes(pool, want):
    """1-3 lines, deliberately mixed length: one short, one medium, one long."""
    buckets = ((18, 45), (46, 90), (91, _MAX))
    order = [1, 0, 2] if want <= 2 else [1, 0, 2]
    chosen, used_secs = [], set()
    for b in order[:want]:
        lo, hi = buckets[b]
        best = None
        for sec, span, sc in pool:
            if sec in used_secs or not (lo <= len(span) <= hi):
                continue
            if best is None or sc > best[2]:
                best = (sec, span, sc)
        if best:
            used_secs.add(best[0])
            chosen.append(best)
    for sec, span, sc in sorted(pool, key=lambda x: -x[2]):   # top up if a bucket was empty
        if len(chosen) >= want:
            break
        if sec not in used_secs:
            used_secs.add(sec)
            chosen.append((sec, span, sc))
    return chosen


_OVERLAP = 10


def _echoes(quote, body):
    """True when the quote and the body share a run of _OVERLAP characters.

    Exact containment missed the common case: the body highlights 「先为不可胜，
    以待敌之可胜」 while the 金句 list carries 「昔之善战者，先为不可胜，以待敌之
    可胜。」 — different strings, same line, printed twice.
    """
    q, b = _bare(quote), _bare(body)
    if not q:
        return False
    if len(q) < _OVERLAP:
        return q in b
    return any(q[i:i + _OVERLAP] in b for i in range(len(q) - _OVERLAP + 1))


CHAPTER_QUOTES = {}


def _dek(summary):
    """Standfirst for an entry page.

    it.summary is "名字（年代）——关键词。" + the first 140 chars of d, and d is
    printed in full a few lines below as the pull. Keep the identifying half,
    which carries the only copy of the precise era; drop the rest. About 12,000
    characters of same-page duplication across the site.
    """
    t = str(summary or "")
    if "\u2014\u2014" in t:
        dot = t.find("\u3002", t.index("\u2014\u2014"))
        if dot > 0:
            return t[:dot + 1]
    return t


def _render_blocks(it, zh):
    html, toc, first_q, n = [], [], True, 0
    slots, pool, quote_block = [], [], []
    rendered = set()              # every <p> actually emitted on this page
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
            rendered.add(name)          # a 分则 title is read text too
            html.append("<h2>%s</h2>" % esc(name))
            for para in body:
                for x in _breathe(para):
                    rendered.add(x)
                    html.append("<p>%s</p>" % esc(x))
            for p_ in egs:
                rendered.add(p_)
                html.append('<p class="eg">%s</p>' % esc(p_))
            html.append("</section>")
            si = len(slots)
            # Close the section with its own strongest line rather than opening
            # with it — the span usually IS the section's first sentence, and
            # putting it above means reading the same words twice in a row.
            slots.append(len(html))
            whole = "".join(body + egs)
            # Candidates are generated per paragraph. Spanning the boundary
            # produced quotes that stitched the principle onto the worked
            # example — two visually separate blocks in the page.
            for paras_src, penalty in ((body, 0.0), (egs, 0.8)):
                for para in paras_src:
                    for span in _spans(para):
                        # A callout has to be an EXCERPT. When the span is most
                        # of the section, the reader gets the same paragraph
                        # twice in a row.
                        if len(whole) - len(span) < 45:
                            continue
                        # …and a real excerpt of its OWN paragraph. _breathe
                        # splits long paragraphs on the same sentence
                        # boundaries _spans uses, so a span can come out byte
                        # for byte identical to a rendered paragraph.
                        if len(para) - len(span) < 20:
                            continue
                        # And it has to carry something beyond a 「quotation」
                        # the 金句 section already lists.
                        own = re.sub(r"\u300c[^\u300d]*\u300d", "", span)
                        if len(own.strip("\u3002\uff0c\u3001\uff01\uff1f\uff1b\uff1a\u2014 ")) < 20:
                            continue
                        pool.append((si, span, _quotability(span) - penalty))
            continue
        if h in ("金句", "原话"):
            quote_block = paras          # rendered last, after the body is known
            continue
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
            rendered.add(paras[0])      # the pull is body the reader has read too
            html.append('<aside class="pull">%s</aside>' % esc(paras[0]))
            if len(paras) > 1:
                html.append('<section class="sec">')
                for para in paras[1:]:
                    for x in _breathe(para):
                        rendered.add(x)
                        html.append("<p>%s</p>" % esc(x))
                html.append("</section>")
            continue
        n += 1
        aid = "s%d" % n
        toc.append((aid, label))
        klass = "sec apply" if "今天" in h else "sec"
        rendered.add(label)
        html.append('<section class="%s" id="%s"><h2 class="sec-k">%s</h2>' % (klass, aid, esc(label)))
        for para in paras:
            for x in _breathe(para):
                rendered.add(x)
                html.append("<p>%s</p>" % esc(x))
        html.append("</section>")
        # 「后来怎么了？」整段本来就是提炼过的短句（fail 一段 + 教训三条），
        # 从一个全是金句的段落里再抽金句，抽出来的是把三条教训连成的一串，
        # 紧跟在它们下面重念一遍。和「今天怎么用」同理，排除。
        if klass == "sec" and "今天" not in h and "后来" not in h:
            si = len(slots)
            slots.append(len(html))
            whole = "".join(paras)
            for span in _spans(whole):
                if len(whole) - len(span) < 45:
                    continue
                own = re.sub(r"\u300c[^\u300d]*\u300d", "", span)
                if len(own.strip("\u3002\uff0c\u3001\uff01\uff1f\uff1b\uff1a\u2014 ")) < 20:
                    continue
                pool.append((si, span, _quotability(span)))
    want = max(1, min(3, len(slots) - 1)) if slots else 0
    # 金句 section: 55 of 100 entries opened a 分则 by citing the very line the
    # list repeats at the foot. Keep only the ones the reader has not already
    # met in the body, and drop the section if that leaves nothing.
    seen_body = "".join(rendered)
    in_chapters = CHAPTER_QUOTES.get(it.title, set())
    keep = [q for q in quote_block
            if _bare(q) and not _echoes(q, seen_body)
            and not any(_echoes(q, c) for c in in_chapters)]
    if keep:
        toc.append(("quotes", "金句"))
        html.append('<section class="quotes" id="quotes"><h2 class="sec-k">金句</h2>')
        html.extend("<blockquote><p>%s</p></blockquote>" % esc(q) for q in keep)
        html.append("</section>")
    pool = [c for c in pool if c[2] > 0 and c[1] not in rendered]
    for si, span, _sc in sorted(_pick_pullquotes(pool, want),
                                key=lambda c: -slots[c[0]]):
        html.insert(slots[si], _say(span))
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
        esc(_dek(it.s(zh_render))),
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
        "<link rel=\"stylesheet\" href=\"/assets/hw-entry.css?v=13\">\n"
        "<link rel=\"stylesheet\" href=\"/assets/hw-chapter.css?v=5\">\n"
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

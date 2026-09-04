#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
geo_kit — shared SEO + GEO (generative engine optimization) generator for ourword.ai.

One file, no dependencies, deterministic output (unchanged data => byte-identical
files => no spurious commits). Every ourword.ai site drops this in `seo/` and calls
it from a tiny `seo/build_seo.py` adapter that turns that site's data into Items.

What it produces
  robots.txt        allow-list for search + AI answer engines, points at the sitemap
  sitemap.xml       every page, properly percent-encoded, with per-item lastmod
  llms.txt          short machine card: what this site is, how to read it, how to cite
  llms-full.txt     the ENTIRE corpus as plain text — this is what answer engines ingest
  feed.xml          RSS, linked from every <head> so readers and crawlers find it
  404.html          a real page with links, so a bad URL is not a dead end for a crawler
  /i/<slug>/        one static page per item (answer-first, no JS)
  /zh/i/<slug>/     the Chinese twin — only where there is real Chinese copy to show
  /t/<tag>/         topic hubs, so nothing sits more than two clicks from the root
  /all/             a flat index of everything, for crawl completeness
  index.html        canonical/OG/JSON-LD fixed + an h1 and a lede for JS-less bots

Why it exists: GPTBot, ClaudeBot, PerplexityBot and friends do not execute JavaScript.
A client-rendered board is, to them, a blank page.
"""
import html as _html
import json
import os
import re
import unicodedata
from urllib.parse import quote

SITE = "https://ourword.ai"

# The whole family, so every site can link to its siblings and declare them in schema.
# Cross-site links are what turn eight orphan sites into one crawlable property.
# 只保留确实可访问的兄弟站。原组织被停用时这里删掉了一批取不到的站点；
# idea 与 ai-bubble（泡沫检测仪，迁址后的新路径）已恢复，加回。
# 仍不可访问、故不列入：ai-jobs-20yr-report、portfolio-tracker。
SITES = [
    ("", "Human World", "人类世界生存法则"),
    ("site", "OurWord AI", "OurWord AI 导航"),
    ("skill", "Skill Store", "Skill 商店"),
    ("ai", "AI Bubble Monitor", "AI 泡沫检测仪"),
    ("zouni", "Zouni", "走你"),
]

AI_AGENTS = [
    "GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-Web", "anthropic-ai",
    "PerplexityBot", "Perplexity-User", "Google-Extended", "Googlebot", "Googlebot-Image",
    "Bingbot", "Applebot", "Applebot-Extended", "CCBot", "Amazonbot", "Bytespider",
    "YouBot", "cohere-ai", "Meta-ExternalAgent", "DuckAssistBot", "MistralAI-User",
    "Diffbot", "omgili", "Timpibot", "PetalBot", "Baiduspider", "Sogou web spider",
    "YisouSpider", "360Spider", "HaosouSpider", "YandexBot",
]


# --------------------------------------------------------------------------- utils
def esc(x):
    return _html.escape(str(x or ""), quote=True)


def slugify(s, fallback="item"):
    s = unicodedata.normalize("NFKD", str(s or ""))
    out = []
    for ch in s.lower():
        if ch.isalnum() and ord(ch) < 128:
            out.append(ch)
        elif "一" <= ch <= "鿿":       # keep CJK, they are legal in URLs
            out.append(ch)
        elif ch in " -_/.":
            out.append("-")
    s = re.sub(r"-{2,}", "-", "".join(out)).strip("-")
    return (s or fallback)[:80]


def urlq(u):
    """Percent-encode a URL for XML <loc>, as the sitemap spec requires. Raw CJK in a
    <loc> is a spec violation and some validators reject the whole file over it."""
    return quote(u, safe="/:?=&#%~+,;@!$'()*[]")


def block_text(s):
    """Like plain(), but line breaks survive — blocks are multi-paragraph."""
    s = re.sub(r"<[^>]+>", " ", str(s or ""))
    s = re.sub(r"[ \t\r\f\v]+", " ", s)
    return "\n".join(x.strip() for x in s.split("\n") if x.strip())


def plain(s, limit=None):
    """Strip tags/whitespace down to something safe for a meta description."""
    s = re.sub(r"<[^>]+>", " ", str(s or ""))
    s = re.sub(r"\s+", " ", s).strip()
    return s[:limit].rstrip() if limit else s


def clip(s, limit):
    """Trim to a length without cutting a word in half, and mark the cut."""
    s = plain(s)
    if len(s) <= limit:
        return s
    cut = s[:limit]
    sp = cut.rfind(" ")
    if sp > limit * 0.6:
        cut = cut[:sp]
    return cut.rstrip(" ,;:·—-") + "…"


def _plural(noun, n):
    return noun if n == 1 else (noun + ("es" if noun.endswith(("s", "x", "ch")) else "s"))


def _write(path, text):
    """Write only when changed, so reruns produce no commit noise."""
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            if f.read() == text:
                return False
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return True


# --------------------------------------------------------------------------- model
class Item(object):
    """One indexable thing: an idea, a skill, a person, a route.

    blocks / blocks_zh are [(heading, body_text)] and become the page's sections, the
    FAQ schema, and the llms-full.txt entry. Keep headings question-shaped where it is
    natural — answer engines quote those.

    A Chinese twin page is only minted when there is real Chinese copy behind it.
    Auto-filled boilerplate ("英文简介见下") would otherwise create hundreds of
    near-identical URLs, which is the thin-content pattern that drags a domain down.
    """

    ZH_MIN = 120        # characters of distinct Chinese prose needed to earn its own URL

    def __init__(self, slug, title, summary, blocks=None, title_zh="", summary_zh="",
                 blocks_zh=None, source_url="", updated="", tags=None, extra=None,
                 url_override="", schema_type="", schema_extra=None):
        self.slug = slugify(slug, "item")
        self.title = plain(title)
        self.summary = plain(summary)
        self.blocks = [(plain(h), block_text(b)) for h, b in (blocks or []) if plain(b)]
        self.title_zh = plain(title_zh)
        self.summary_zh = plain(summary_zh)
        self.blocks_zh = [(plain(h), plain(b)) for h, b in (blocks_zh or []) if plain(b)]
        self.source_url = source_url or ""
        self.updated = (updated or "")[:10]
        self.tags = [plain(t) for t in (tags or []) if plain(t)]
        self.extra = extra or {}
        self.url_override = url_override      # single-document sites have no /i/ page
        self.schema_type = schema_type        # Person, Book, TouristTrip, …
        self.schema_extra = schema_extra or {}

    def zh_chars(self):
        if self.blocks_zh == self.blocks:      # mirrored, not translated
            return 0
        body = self.summary_zh + " ".join(b for _, b in self.blocks_zh)
        return sum(1 for c in body if "一" <= c <= "鿿")

    def has_zh(self):
        return self.zh_chars() >= self.ZH_MIN

    def page(self, site, zh=False):
        if self.url_override:
            return self.url_override
        return site.url(("zh/i/%s/" if zh else "i/%s/") % self.slug)

    def t(self, zh):
        return (self.title_zh or self.title) if zh else (self.title or self.title_zh)

    def s(self, zh):
        return (self.summary_zh or self.summary) if zh else (self.summary or self.summary_zh)

    def b(self, zh):
        return (self.blocks_zh or self.blocks) if zh else (self.blocks or self.blocks_zh)


class Site(object):
    def __init__(self, path, name, name_zh, tagline, tagline_zh, description,
                 description_zh, keywords="", item_type="Article", item_noun="entry",
                 item_noun_zh="条目", image="", lang="en", changefreq="daily",
                 hub_min=3, hub_max=40):
        self.path = path.strip("/")                       # "" for the apex
        self.base = SITE + ("/" + self.path + "/" if self.path else "/")
        self.name, self.name_zh = name, name_zh
        self.tagline, self.tagline_zh = tagline, tagline_zh
        self.description, self.description_zh = description, description_zh
        self.keywords = keywords
        self.item_type = item_type
        self.item_noun, self.item_noun_zh = item_noun, item_noun_zh
        self.image = image or (self.base + "og.png")
        self.lang = lang
        self.changefreq = changefreq
        self.hub_min, self.hub_max = hub_min, hub_max

    def url(self, rel=""):
        return self.base + rel.lstrip("/")

    def zh(self):
        return self.lang.startswith("zh")


# --------------------------------------------------------------------- <head> patch
_HEAD_MARK = ("<!--GEO:HEAD:START-->", "<!--GEO:HEAD:END-->")
_BODY_MARK = ("<!--GEO:BODY:START-->", "<!--GEO:BODY:END-->")

LEGACY_HOST = re.compile(r"https?://ourword-ai\.github\.io/")


def canonicalise_host(src):
    """The project sites were built against the github.io host — canonical tags, share
    links and in-page JS constants all pointed there, which is what split each site from
    its own domain. Rewrite every one of them to ourword.ai."""
    return LEGACY_HOST.sub(SITE + "/", src)


CONFLICT = re.compile(r"^(?:<{7}|={7}|>{7})[^\n]*\n?", re.M)


def heal(src):
    """Repair a source file before patching it.

    Three things go wrong in practice and all three are silent:
      * a `git pull --rebase --autostash` conflict gets committed, leaving
        `<<<<<<< / ======= / >>>>>>>` markers *inside the HTML* — visible to visitors
        and to crawlers, and duplicating the whole head block;
      * that duplication leaves two `</head>` tags, so the page ends up with two
        canonicals contradicting each other;
      * an older generated block survives somewhere outside the head.

    When both sides of a conflict are identical (which they are, when the only
    difference was a regenerated block) keeping either one is lossless.
    """
    m = re.search(r"^<{7}[^\n]*\n(.*?)^={7}[^\n]*\n(.*?)^>{7}[^\n]*\n?", src,
                  flags=re.S | re.M)
    while m:
        a, b = m.group(1), m.group(2)
        keep = a if a == b or len(a) >= len(b) else b
        src = src[:m.start()] + keep + src[m.end():]
        m = re.search(r"^<{7}[^\n]*\n(.*?)^={7}[^\n]*\n(.*?)^>{7}[^\n]*\n?", src,
                      flags=re.S | re.M)
    src = CONFLICT.sub("", src)
    # every generated block, wherever it ended up
    src = re.sub(re.escape(_HEAD_MARK[0]) + r".*?" + re.escape(_HEAD_MARK[1]), "",
                 src, flags=re.S)
    src = re.sub(r"<!--SEO:START-->.*?<!--SEO:END-->", "", src, flags=re.S)
    # collapse duplicated </head> before <body>
    bi = src.lower().find("<body")
    if bi > 0:
        headzone = src[:bi]
        if headzone.lower().count("</head>") > 1:
            first = headzone.lower().index("</head>") + len("</head>")
            rest = re.sub(r"</head\s*>", "", headzone[first:], flags=re.I)
            src = headzone[:first] + rest + src[bi:]
    return src


def _assert_sane(path, src):
    """Never publish a page with conflict markers or contradictory canonicals."""
    if CONFLICT.search(src):
        raise SystemExit("%s still contains merge-conflict markers — refusing to write"
                         % path)
    n = len(re.findall(r'<link rel="canonical"', src))
    if n > 1:
        raise SystemExit("%s ended up with %d canonical tags — refusing to write"
                         % (path, n))
    return src


def _strip_legacy(head):
    """Remove the tags we are about to own, so we never emit duplicates."""
    pats = [
        r'<link[^>]+rel=["\']canonical["\'][^>]*>',
        r'<link[^>]+rel=["\']alternate["\'][^>]*>',
        r'<meta[^>]+property=["\']og:[a-z:_]+["\'][^>]*>',
        r'<meta[^>]+name=["\'](description|keywords|robots|author|twitter:[a-z:]+)["\'][^>]*>',
        r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>.*?</script>',
        r"<!--SEO:START-->.*?<!--SEO:END-->",
        _HEAD_MARK[0] + r".*?" + _HEAD_MARK[1],
    ]
    for p in pats:
        head = re.sub(p, "", head, flags=re.S | re.I)
    return head


def head_block(site, page_url, title, description, zh=False, alt_url="",
               ld=None, item=None):
    """The whole <head> contribution: canonical, hreflang, OG/Twitter, RSS, JSON-LD."""
    out = [_HEAD_MARK[0]]
    out.append('<meta name="description" content="%s">' % esc(clip(description, 300)))
    if site.keywords:
        out.append('<meta name="keywords" content="%s">' % esc(site.keywords))
    out.append('<meta name="author" content="OurWord AI">')
    out.append('<meta name="robots" content="index,follow,max-image-preview:large,'
               'max-snippet:-1,max-video-preview:-1">')
    out.append('<link rel="canonical" href="%s">' % esc(page_url))
    if alt_url:
        en_u, zh_u = (alt_url, page_url) if zh else (page_url, alt_url)
        out.append('<link rel="alternate" hreflang="en" href="%s">' % esc(en_u))
        out.append('<link rel="alternate" hreflang="zh-Hans" href="%s">' % esc(zh_u))
        out.append('<link rel="alternate" hreflang="x-default" href="%s">' % esc(en_u))
    out.append('<link rel="alternate" type="application/rss+xml" title="%s" href="%s">'
               % (esc(site.name), esc(site.url("feed.xml"))))
    out.append('<meta property="og:type" content="%s">'
               % ("article" if item else "website"))
    out.append('<meta property="og:site_name" content="%s">' % esc(site.name))
    out.append('<meta property="og:locale" content="%s">' % ("zh_CN" if zh else "en_US"))
    out.append('<meta property="og:title" content="%s">' % esc(clip(title, 95)))
    out.append('<meta property="og:description" content="%s">' % esc(clip(description, 300)))
    out.append('<meta property="og:url" content="%s">' % esc(page_url))
    if site.image:
        out.append('<meta property="og:image" content="%s">' % esc(site.image))
        out.append('<meta property="og:image:width" content="1200">')
        out.append('<meta property="og:image:height" content="630">')
        out.append('<meta property="og:image:alt" content="%s">' % esc(site.name))
    out.append('<meta name="twitter:card" content="summary_large_image">')
    out.append('<meta name="twitter:site" content="@futuredotnews">')
    out.append('<meta name="twitter:title" content="%s">' % esc(clip(title, 95)))
    out.append('<meta name="twitter:description" content="%s">' % esc(clip(description, 200)))
    if site.image:
        out.append('<meta name="twitter:image" content="%s">' % esc(site.image))
    for obj in (ld or []):
        out.append('<script type="application/ld+json">%s</script>'
                   % json.dumps(obj, ensure_ascii=False, separators=(",", ":")))
    out.append(_HEAD_MARK[1])
    return "".join(out)


def patch_index(path, site, items, zh=False, extra_ld=None, hubs=None):
    """Rewrite an existing hand-built index.html's head, and give it an h1 + lede."""
    if not os.path.exists(path):
        return False
    src = heal(canonicalise_host(open(path, encoding="utf-8").read()))
    m = re.search(r"(<head[^>]*>)(.*?)(</head>)", src, flags=re.S | re.I)
    if not m:
        return False
    head = _strip_legacy(m.group(2))

    zh = zh or site.zh()
    title = clip("%s — %s" % (site.name_zh if zh else site.name,
                              site.tagline_zh if zh else site.tagline), 70)
    desc = site.description_zh if zh else site.description
    ld = [org_ld(), website_ld(site, zh)]
    if items:
        ld.append(itemlist_ld(site, items, zh))
    ld += (extra_ld or [])
    head = head + head_block(site, site.url(), title, desc, zh=zh, ld=ld)
    head = _ensure_ga(head, src)
    src = src[:m.start(2)] + head + src[m.end(2):]
    src = _inject_body(src, noscript_index(site, items, zh=zh, hubs=hubs))
    return _write(path, _assert_sane(path, src))


def patch_page(path, site, rel, title, desc, zh=None, ld=None, h1=""):
    """Give a secondary hand-built page (a monitor view, a privacy page) the same
    treatment as the homepage: its own canonical, OG, description and an h1 — otherwise
    it sits in the sitemap as a page with no signals at all."""
    if not os.path.exists(path):
        return False
    zh = site.zh() if zh is None else zh
    src = heal(canonicalise_host(open(path, encoding="utf-8").read()))
    m = re.search(r"(<head[^>]*>)(.*?)(</head>)", src, flags=re.S | re.I)
    if not m:
        return False
    url = site.url(rel)
    head = _strip_legacy(m.group(2)) + head_block(
        site, url, title, desc, zh=zh,
        ld=(ld if ld is not None else [org_ld(), website_ld(site, zh)]))
    head = _ensure_ga(head, src)
    src = src[:m.start(2)] + head + src[m.end(2):]
    if "<h1" not in src:
        src = _inject_body(src, _BODY_MARK[0] +
                           '<noscript><section><h1>%s</h1><p>%s</p>'
                           '<p><a href="%s">%s</a></p><p>%s</p></section></noscript>'
                           % (esc(h1 or title), esc(clip(desc, 400)), esc(site.base),
                              esc(site.name_zh if zh else site.name),
                              sibling_links(site, zh)) + _BODY_MARK[1])
    return _write(path, _assert_sane(path, src))


def _inject_body(src, block):
    if _BODY_MARK[0] in src:
        return re.sub(re.escape(_BODY_MARK[0]) + r".*?" + re.escape(_BODY_MARK[1]),
                      lambda _m: block, src, count=1, flags=re.S)
    return re.sub(r"</body>", block + "\n</body>", src, count=1, flags=re.I)


def sibling_links(site, zh=False):
    return (
        '<a href="%s">人类世界生存法则</a> · '
        '<a href="%s">原声</a> · '
        '<a href="%s">品味</a>'
        % (esc(SITE + "/"), esc(SITE + "/podcast/"), esc(SITE + "/skill/"))
    )


def noscript_index(site, items, zh=False, hubs=None):
    """A crawlable table of contents that JS-less agents (i.e. all of them) can read."""
    rows = ['<li><a href="%s">%s</a> — %s</li>'
            % (esc(it.page(site)), esc(it.t(zh)), esc(clip(it.s(zh), 220))) for it in items]
    hub_html = ""
    if hubs:
        hub_html = "<p>%s %s</p>" % (
            "按主题浏览：" if zh else "Browse by topic:",
            " · ".join('<a href="%s">%s</a>' % (esc(site.url("t/%s/" % s)), esc(n))
                       for s, n, _c in hubs))
    return (_BODY_MARK[0] +
            '<noscript><section id="geo-index"><h1>%s</h1><p>%s</p>%s%s'
            '<p><a href="%s">%s</a> · <a href="%s">llms.txt</a> · '
            '<a href="%s">llms-full.txt</a> · <a href="%s">sitemap.xml</a> · '
            '<a href="%s">feed.xml</a></p><p>%s</p></section></noscript>'
            % (esc("%s — %s" % (site.name_zh if zh else site.name,
                                site.tagline_zh if zh else site.tagline)),
               esc(clip(site.description_zh if zh else site.description, 400)),
               hub_html, ("<ul>%s</ul>" % "".join(rows)) if rows else "",
               esc(site.url("all/")), esc("全部条目" if zh else "All entries"),
               esc(site.url("llms.txt")), esc(site.url("llms-full.txt")),
               esc(site.url("sitemap.xml")), esc(site.url("feed.xml")),
               sibling_links(site, zh))
            + _BODY_MARK[1])


# ------------------------------------------------------------------------ JSON-LD
def org_ld():
    return {"@context": "https://schema.org", "@type": "Organization", "name": "OurWord AI",
            "alternateName": "用 AI 触摸这个世界", "url": SITE + "/",
            "logo": SITE + "/og.png",
            "sameAs": ["https://github.com/woowoeth", "https://x.com/futuredotnews"]
                      + [SITE + "/" + p + "/" for p, _e, _c in SITES if p]}


def website_ld(site, zh=False):
    return {"@context": "https://schema.org", "@type": "WebSite",
            "name": site.name_zh if zh else site.name,
            "alternateName": site.name if zh else site.name_zh,
            "url": site.base, "inLanguage": ["en", "zh-Hans"],
            "description": clip(site.description_zh if zh else site.description, 500),
            "publisher": {"@type": "Organization", "name": "OurWord AI", "url": SITE + "/"}}


def itemlist_ld(site, items, zh=False):
    els = [{"@type": "ListItem", "position": i, "url": it.page(site), "name": it.t(zh)}
           for i, it in enumerate(items, 1)]
    return {"@context": "https://schema.org", "@type": "ItemList",
            "name": "%s — %s" % (site.name_zh if zh else site.name,
                                 site.tagline_zh if zh else site.tagline),
            "url": site.base, "numberOfItems": len(els), "itemListElement": els}


def breadcrumb_ld(site, it, zh):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "OurWord AI", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": site.name_zh if zh else site.name,
         "item": site.base},
        {"@type": "ListItem", "position": 3, "name": it.t(zh),
         "item": it.page(site, zh and it.has_zh())}]}


def item_ld(site, it, zh, page_url):
    t = it.schema_type or site.item_type
    d = {"@context": "https://schema.org", "@type": t,
         "name": it.t(zh), "url": page_url,
         "description": clip(it.s(zh), 500),
         "inLanguage": "zh-Hans" if zh else "en",
         "isPartOf": {"@type": "WebSite", "name": site.name_zh if zh else site.name,
                      "url": site.base},
         "publisher": {"@type": "Organization", "name": "OurWord AI", "url": SITE + "/"}}
    if t in ("Article", "BlogPosting", "Report"):
        d["headline"] = clip(it.t(zh), 110)
        d["author"] = {"@type": "Organization", "name": "OurWord AI", "url": SITE + "/"}
        d["image"] = site.image
    if it.updated:
        d["dateModified"] = it.updated
        d["datePublished"] = it.updated
    if it.tags:
        d["keywords"] = ", ".join(it.tags)
    if it.source_url:
        d["citation"] = it.source_url
        d["sameAs"] = it.source_url
    if t == "SoftwareApplication":
        d["applicationCategory"] = "DeveloperApplication"
        d.setdefault("offers", {"@type": "Offer", "price": "0", "priceCurrency": "USD"})
    d.update(it.schema_extra)
    return d


def faq_ld(it, zh, max_q=12, max_chars=700):
    """Heading/body pairs become a FAQPage — the highest-yield GEO schema there is.

    Capped on purpose: a long report has dozens of sections, and putting all of them in
    the head would mean ~90KB of JSON above the content for no extra benefit. The full
    text is on the page and in llms-full.txt, which is where answer engines read it.
    """
    qs = [{"@type": "Question", "name": clip(h, 180),
           "acceptedAnswer": {"@type": "Answer", "text": clip(b, max_chars)}}
          for h, b in it.b(zh) if h and len(plain(b)) > 40][:max_q]
    if len(qs) < 2:
        return None
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": qs}


# ------------------------------------------------- single long report (no items)
def sections_from_html(path, min_chars=200, levels="h2|h3"):
    """Pull (heading, text) pairs out of a hand-written long-form page.

    For a deep report, splitting it into fragment pages would only create thin, competing
    URLs — so we keep one canonical page and use the sections for the FAQ schema and for
    llms-full.txt, where an answer engine can read the lot.
    """
    if not os.path.exists(path):
        return []
    src = open(path, encoding="utf-8").read()
    src = re.sub(r"<(script|style|nav|footer)\b.*?</\1>", " ", src, flags=re.S | re.I)
    parts = re.split(r"<(?:%s)\b[^>]*>(.*?)</(?:%s)>" % (levels, levels), src, flags=re.S | re.I)
    out = []
    for i in range(1, len(parts) - 1, 2):
        h, body = plain(parts[i]), plain(parts[i + 1])
        if h and len(body) >= min_chars:
            out.append((h, body))
    return out


def article_ld(site, url, title, description, sections, zh=True, updated=""):
    d = {"@context": "https://schema.org", "@type": "Article",
         "headline": clip(title, 110), "name": title, "url": url,
         "description": clip(description, 500),
         "inLanguage": "zh-Hans" if zh else "en",
         "articleSection": [h for h, _ in sections][:20],
         "wordCount": sum(len(b) for _, b in sections),
         "image": site.image,
         "isPartOf": {"@type": "WebSite", "name": site.name_zh if zh else site.name,
                      "url": site.base},
         "author": {"@type": "Organization", "name": "OurWord AI", "url": SITE + "/"},
         "publisher": {"@type": "Organization", "name": "OurWord AI", "url": SITE + "/",
                       "logo": {"@type": "ImageObject", "url": SITE + "/og.png"}}}
    if updated:
        d["dateModified"] = updated
        d["datePublished"] = updated
    return d


# --------------------------------------------------------------------- static pages
_PAGE_CSS = (
    "*{box-sizing:border-box}body{margin:0;background:#f4f0e8;color:#1c1917;"
    "font:16px/1.75 -apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC',"
    "'Noto Sans SC',sans-serif;-webkit-font-smoothing:antialiased}"
    "main{max-width:720px;margin:0 auto;padding:24px 24px 72px}"
    "a{color:#7a1e26}nav.bc{font-size:13px;color:#767c76;margin:8px 0 24px}"
    "nav.bc a{color:#767c76;text-decoration:none}nav.bc a:hover{text-decoration:underline}"
    "h1{font-size:26px;line-height:1.3;margin:0 0 12px;letter-spacing:-.01em}"
    "h2{font-size:13px;letter-spacing:.08em;color:#9d2933;margin:32px 0 8px;font-weight:650}"
    ".lede{font-size:17px;color:#4c524e;margin:0 0 20px}"
    ".meta{font-size:13px;color:#767c76;margin:0 0 24px}"
    ".tags{margin:20px 0 0}.tags a,.tags span{display:inline-block;font-size:12px;"
    "color:#4a4338;background:#efe8d8;border-radius:999px;padding:3px 10px;"
    "margin:0 6px 6px 0;text-decoration:none}"
    "footer{margin-top:40px;padding-top:20px;border-top:1px solid rgba(42,46,44,.12);"
    "font-size:13px;color:#767c76}footer a{color:#4c524e}"
    "p{margin:0 0 14px}.sib{margin-top:28px;font-size:14px}"
    "ul.idx{padding-left:18px}ul.idx li{margin:0 0 10px}.share-btn{font:inherit;font-size:13px;font-weight:600;letter-spacing:.04em;padding:7px 14px;border-radius:999px;border:1px solid rgba(28,25,23,.16);background:#efe8d8;color:#7a1e26;cursor:pointer}.share-row{margin:0 0 20px}"
)


# Google Analytics 4. One property covers every OurWord site; reports split by hostname.
# It MUST live here, in the generator, not be injected into the output afterwards:
# every generated page is rewritten from scratch on each run, so an injected snippet
# survives exactly until the next build. Set OURWORD_GA_ID="" to build without it.
GA_ID = os.environ.get("OURWORD_GA_ID", "G-DHD3WEXQ8T")


def ga_block(ga_id=None):
    """The gtag.js pair, or "" when no measurement id is configured."""
    gid = GA_ID if ga_id is None else ga_id
    if not gid:
        return ""
    return ('<script async src="https://www.googletagmanager.com/gtag/js?id=%s"></script>\n'
            "<script>window.dataLayer=window.dataLayer||[];"
            "function gtag(){dataLayer.push(arguments);}"
            'gtag("js",new Date());gtag("config","%s");</script>' % (gid, gid))


def _ensure_ga(head, src):
    """Hand-built pages keep their own <head>; add gtag only if it is not already there."""
    if GA_ID and GA_ID not in src:
        return head + "\n" + ga_block()
    return head


def _shell(lang, title, headhtml, body):
    return ("<!DOCTYPE html>\n<html lang=\"%s\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n"
            "<title>%s</title>\n%s\n%s\n<style>%s</style>\n</head>\n<body>\n<main>\n%s\n"
            "</main>\n<script src=\"/assets/hw-share.js\" defer></script>\n</body>\n</html>\n"
            % (lang, esc(title), headhtml, ga_block(), _PAGE_CSS, body))


def _sib_links(site, items, idx, zh, zh_url=False):
    pre = "zh/i/%s/" if zh_url else "i/%s/"
    out = []
    if idx > 0:
        p = items[idx - 1]
        out.append('← <a href="%s">%s</a>' % (esc(site.url(pre % p.slug)), esc(p.t(zh))))
    if idx < len(items) - 1:
        n = items[idx + 1]
        out.append('<a href="%s">%s</a> →' % (esc(site.url(pre % n.slug)), esc(n.t(zh))))
    return ('<p class="sib">%s</p>' % " &nbsp;·&nbsp; ".join(out)) if out else ""


def item_page(site, it, items, idx, zh, hub_of=None):
    zh_render = zh or site.zh()
    page_url = it.page(site, zh)
    alt_url = site.url(("i/%s/" if zh else "zh/i/%s/") % it.slug) if it.has_zh() else ""
    title = clip("%s — %s" % (it.t(zh_render), site.name_zh if zh_render else site.name), 70)
    ld = [org_ld(), item_ld(site, it, zh_render, page_url), breadcrumb_ld(site, it, zh_render)]
    f = faq_ld(it, zh_render)
    if f:
        ld.append(f)

    secs = []
    for h, b in it.b(zh_render):
        if h:
            secs.append("<h2>%s</h2>" % esc(h))
        for para in str(b).split("\n"):
            if para.strip():
                secs.append("<p>%s</p>" % esc(para.strip()))

    lbl = {
        True: ("首页", "本页可直接引用", "来源", "更新于", "返回", "英文版", "主题", "全部条目"),
        False: ("Home", "Cite this page", "Source", "Updated", "Back to", "中文版",
                "Topics", "All entries"),
    }[zh_render]

    body = [
        '<nav class="bc"><a href="%s">%s</a> › <a href="%s">%s</a> › %s</nav>'
        % (esc(SITE + "/"), lbl[0], esc(site.base),
           esc(site.name_zh if zh_render else site.name), esc(it.t(zh_render))),
        "<h1>%s</h1>" % esc(it.t(zh_render)),
        '<p class="share-row"><button class="share-btn" type="button" data-share '
        'data-share-title="%s" data-share-url="%s" data-share-text="%s" '
        'aria-label="分享本页">分享</button></p>'
        % (esc(title), esc(page_url),
           esc("%s\n\n%s\n\n%s" % (it.t(zh_render), it.s(zh_render), page_url))),
        '<p class="lede">%s</p>' % esc(it.s(zh_render)),
    ]
    meta = []
    if it.updated:
        meta.append("%s %s" % (lbl[3], esc(it.updated)))
    if it.source_url:
        meta.append('%s <a href="%s" rel="nofollow noopener">%s</a>'
                    % (lbl[2], esc(it.source_url), esc(clip(it.source_url, 70))))
    if alt_url:
        meta.append('<a href="%s">%s</a>' % (esc(alt_url), lbl[5]))
    if meta:
        body.append('<p class="meta">%s</p>' % " · ".join(meta))
    body += secs

    linked = [t for t in it.tags if (hub_of or {}).get(slugify(t))]
    if linked:
        body.append('<p class="tags">%s</p>'
                    % "".join('<a href="%s">%s</a>'
                              % (esc(site.url("t/%s/" % slugify(t))), esc(t)) for t in linked))
    elif it.tags:
        body.append('<p class="tags">%s</p>'
                    % "".join("<span>%s</span>" % esc(t) for t in it.tags))
    body.append(_sib_links(site, items, idx, zh_render, zh))
    body.append('<footer><p>%s <a href="%s">%s</a> · <a href="%s">%s</a></p>'
                '<p>%s: <code>%s</code></p>'
                '<p><a href="%s">llms.txt</a> · <a href="%s">llms-full.txt</a></p>'
                '<p>%s</p></footer>'
                % (lbl[4], esc(site.base), esc(site.name_zh if zh_render else site.name),
                   esc(site.url("all/")), esc(lbl[7]),
                   lbl[1], esc(page_url), esc(site.url("llms.txt")),
                   esc(site.url("llms-full.txt")), sibling_links(site, zh_render)))

    return _shell("zh-Hans" if zh_render else "en", title,
                  head_block(site, page_url, title, it.s(zh_render), zh=zh_render,
                             alt_url=alt_url, ld=ld, item=it),
                  "\n".join(x for x in body if x))


def write_item_pages(site, items, root=".", hub_of=None):
    n = 0
    for i, it in enumerate(items):
        if _write(os.path.join(root, "i", it.slug, "index.html"),
                  item_page(site, it, items, i, False, hub_of)):
            n += 1
        if it.has_zh():
            if _write(os.path.join(root, "zh", "i", it.slug, "index.html"),
                      item_page(site, it, items, i, True, hub_of)):
                n += 1
    return n


# ---------------------------------------------------------------------- topic hubs
def build_hubs(site, items):
    """Group items by tag. Hubs cut crawl depth and give each topic a page that can rank
    on its own; a tag with fewer than hub_min items would just be another thin page, so
    it does not get one."""
    by = {}
    for it in items:
        for t in it.tags:
            s = slugify(t)
            if not s:
                continue
            by.setdefault(s, [t, []])[1].append(it)
    hubs = [(s, n, its) for s, (n, its) in by.items() if len(its) >= site.hub_min]
    hubs.sort(key=lambda h: (-len(h[2]), h[0]))
    return hubs[:site.hub_max]


def hub_page(site, slug, name, its, hubs):
    zh = site.zh()
    page_url = site.url("t/%s/" % slug)
    title = clip("%s — %s" % (name, site.name_zh if zh else site.name), 70)
    desc = (("%s 里关于「%s」的 %d 个%s。" % (site.name_zh, name, len(its), site.item_noun_zh))
            if zh else
            ("%d %s on %s tagged %s." % (len(its), _plural(site.item_noun, len(its)),
                                         site.name, name)))
    ld = [org_ld(),
          {"@context": "https://schema.org", "@type": "CollectionPage", "name": name,
           "url": page_url, "description": desc,
           "isPartOf": {"@type": "WebSite", "name": site.name_zh if zh else site.name,
                        "url": site.base},
           "mainEntity": {"@type": "ItemList", "numberOfItems": len(its),
                          "itemListElement": [
                              {"@type": "ListItem", "position": i, "url": x.page(site),
                               "name": x.t(zh)} for i, x in enumerate(its, 1)]}},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "OurWord AI", "item": SITE + "/"},
              {"@type": "ListItem", "position": 2, "name": site.name_zh if zh else site.name,
               "item": site.base},
              {"@type": "ListItem", "position": 3, "name": name, "item": page_url}]}]
    rows = "".join('<li><a href="%s">%s</a> — %s</li>'
                   % (esc(x.page(site)), esc(x.t(zh)), esc(clip(x.s(zh), 200))) for x in its)
    others = " · ".join('<a href="%s">%s</a>' % (esc(site.url("t/%s/" % s)), esc(n))
                        for s, n, _c in hubs if s != slug)
    body = ('<nav class="bc"><a href="%s">%s</a> › <a href="%s">%s</a> › %s</nav>'
            '<h1>%s</h1><p class="lede">%s</p><ul class="idx">%s</ul>'
            '<p class="sib">%s %s</p>'
            '<footer><p><a href="%s">%s</a> · <a href="%s">%s</a></p><p>%s</p></footer>'
            % (esc(SITE + "/"), "首页" if zh else "Home", esc(site.base),
               esc(site.name_zh if zh else site.name), esc(name), esc(name), esc(desc), rows,
               "其他主题：" if zh else "Other topics:", others,
               esc(site.url("all/")), "全部条目" if zh else "All entries",
               esc(site.base), esc(site.name_zh if zh else site.name),
               sibling_links(site, zh)))
    return _shell("zh-Hans" if zh else "en", title,
                  head_block(site, page_url, title, desc, zh=zh, ld=ld), body)


def all_page(site, items, hubs):
    zh = site.zh()
    page_url = site.url("all/")
    label = "全部条目" if zh else "All entries"
    title = clip("%s — %s" % (label, site.name_zh if zh else site.name), 70)
    desc = (("%s 的全部 %d 个%s，一页列完。" % (site.name_zh, len(items), site.item_noun_zh))
            if zh else "Every one of the %d %s on %s, on one page."
            % (len(items), _plural(site.item_noun, len(items)), site.name))
    ld = [org_ld(), itemlist_ld(site, items, zh),
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "OurWord AI", "item": SITE + "/"},
              {"@type": "ListItem", "position": 2, "name": site.name_zh if zh else site.name,
               "item": site.base},
              {"@type": "ListItem", "position": 3, "name": label, "item": page_url}]}]
    rows = "".join('<li><a href="%s">%s</a> — %s</li>'
                   % (esc(x.page(site)), esc(x.t(zh)), esc(clip(x.s(zh), 180))) for x in items)
    hubline = " · ".join('<a href="%s">%s</a>' % (esc(site.url("t/%s/" % s)), esc(n))
                         for s, n, _c in hubs)
    body = ('<nav class="bc"><a href="%s">%s</a> › <a href="%s">%s</a> › %s</nav>'
            '<h1>%s</h1><p class="lede">%s</p>%s<ul class="idx">%s</ul>'
            '<footer><p><a href="%s">%s</a> · <a href="%s">llms-full.txt</a> · '
            '<a href="%s">sitemap.xml</a></p><p>%s</p></footer>'
            % (esc(SITE + "/"), "首页" if zh else "Home", esc(site.base),
               esc(site.name_zh if zh else site.name), esc(label), esc(label), esc(desc),
               ('<p class="sib">%s %s</p>' % ("按主题：" if zh else "By topic:", hubline))
               if hubline else "",
               rows, esc(site.base), esc(site.name_zh if zh else site.name),
               esc(site.url("llms-full.txt")), esc(site.url("sitemap.xml")),
               sibling_links(site, zh)))
    return _shell("zh-Hans" if zh else "en", title,
                  head_block(site, page_url, title, desc, zh=zh, ld=ld), body)


def page_404(site, hubs):
    """A dead URL should still hand a crawler somewhere to go."""
    zh = site.zh()
    title = "404 — %s" % (site.name_zh if zh else site.name)
    msg = ("这个地址不存在。下面是可以去的地方。" if zh
           else "That address does not exist. Here is where to go instead.")
    links = ('<p><a href="%s">%s</a> · <a href="%s">%s</a> · <a href="%s">OurWord AI</a></p>'
             % (esc(site.base), esc(site.name_zh if zh else site.name),
                esc(site.url("all/")), "全部条目" if zh else "All entries", esc(SITE + "/")))
    hubline = " · ".join('<a href="%s">%s</a>' % (esc(site.url("t/%s/" % s)), esc(n))
                         for s, n, _c in hubs)
    body = ('<h1>404</h1><p class="lede">%s</p>%s%s<p>%s</p>'
            % (esc(msg), links,
               ('<p class="sib">%s %s</p>' % ("主题：" if zh else "Topics:", hubline))
               if hubline else "", sibling_links(site, zh)))
    # 历史地址救援：站点先后住过 ourword.ai/HumanWorld/ 和 ourword.ai/humanworld/，
    # 现在在根。旧链接（含 89 个条目页）会打到这里，前缀剥掉后原样转到新位置。
    # 历史地址救援：①站点先后住过 ourword.ai/HumanWorld/ 与 /humanworld/，现在在根；
    # ②2026-08-17 仓库统一改成单词命名，老路径在这里一次性映射到新路径。
    # 未知路径不跳转，仍然看到这张 404 页。
    rescue = ("<script>(function(){var p=location.pathname,"
              "m=p.match(/^\\/(?:HumanWorld|humanworld)(\\/.*)?$/);"
              "if(m){location.replace((m[1]||'/')+location.search+location.hash);return;}"
              "var R={'ourword-site':'site','ai-bubble':'ai','skill-store':'skill'},"
              "s=p.match(/^\\/([^\\/]+)(\\/.*)?$/);"
              "if(s&&R[s[1]]){location.replace('/'+R[s[1]]+(s[2]||'/')+location.search+location.hash);}"
              "})();</script>")
    head = ('<meta name="robots" content="noindex,follow">'
            '<link rel="canonical" href="%s">%s' % (esc(site.url("404.html")), rescue))
    return _shell("zh-Hans" if zh else "en", title, head, body)


# -------------------------------------------------------------- robots / sitemap
def write_robots(site, root=".", extra_sitemaps=()):
    lines = ["# %s — we want to be crawled, indexed, and cited by search and AI answer engines."
             % site.name,
             "# robots.txt is per-origin: the authoritative one for this domain is",
             "# https://ourword.ai/robots.txt — this copy is here for completeness.", "",
             "User-agent: *",
             "Content-Signal: search=yes,ai-input=yes,ai-train=no,use=reference",
             "Allow: /", ""]
    for a in AI_AGENTS:
        lines += ["User-agent: %s" % a, "Allow: /", ""]
    lines.append("Sitemap: %s" % site.url("sitemap.xml"))
    for s in extra_sitemaps:
        lines.append("Sitemap: %s" % s)
    lines.append("")
    return _write(os.path.join(root, "robots.txt"), "\n".join(lines))


def write_sitemap(site, items, root=".", today="", extra_urls=(), hubs=()):
    """Per-URL lastmod from the item's own date — a sitemap claiming everything changed
    today, every day, is a signal engines learn to discount."""
    urls = [(site.base, "1.0", site.changefreq, today)]
    if items:
        urls.append((site.url("all/"), "0.6", "weekly", today))
    for s, _n, its in hubs:
        urls.append((site.url("t/%s/" % s), "0.6", "weekly",
                     max([x.updated for x in its if x.updated] or [today])))
    for u in extra_urls:
        urls.append((u, "0.7", site.changefreq, today))
    for it in items:
        lm = it.updated or today
        urls.append((it.page(site), "0.8", "weekly", lm))
        if it.has_zh():
            urls.append((site.url("zh/i/%s/" % it.slug), "0.8", "weekly", lm))
    seen, rows = set(), []
    for u, pri, cf, lm in urls:
        if u in seen:
            continue
        seen.add(u)
        rows.append("  <url><loc>%s</loc>%s<changefreq>%s</changefreq>"
                    "<priority>%s</priority></url>"
                    % (esc(urlq(u)), ("<lastmod>%s</lastmod>" % lm) if lm else "", cf, pri))
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    return _write(os.path.join(root, "sitemap.xml"), xml)


# ------------------------------------------------------------------ llms.txt / RSS
def write_llms(site, items, root=".", how_built="", cite_as="", hubs=()):
    L = ["# %s (%s)" % (site.name, site.name_zh), "",
         "> %s" % plain(site.tagline), "> %s" % plain(site.tagline_zh), "",
         plain(site.description), "", plain(site.description_zh), "",
         "## Read it", "",
         "- Site: %s" % site.base,
         "- Everything on one page: %s" % site.url("all/"),
         "- Every %s has its own static page: %si/<slug>/"
         % (site.item_noun, site.base),
         "- Full text of everything, one file: %s" % site.url("llms-full.txt"),
         "- All URLs: %s" % site.url("sitemap.xml"),
         "- RSS: %s" % site.url("feed.xml"), ""]
    if hubs:
        L += ["## Topics", ""]
        L += ["- [%s](%s) — %d" % (n, site.url("t/%s/" % s), len(its)) for s, n, its in hubs]
        L.append("")
    if how_built:
        L += ["## How it is built", "", plain(how_built), ""]
    L += ["## Citing", "",
          cite_as or ("Cite the individual page URL, not the homepage — each %s page is "
                      "stable and dated. Attribute to \"%s (OurWord AI)\"."
                      % (site.item_noun, site.name)), "",
          "## The rest of OurWord AI", ""]
    for p, en, cn in SITES:
        if p == site.path:
            continue
        L.append("- [%s / %s](%s)" % (en, cn, SITE + "/" + (p + "/" if p else "")))
    L += ["", "## Index (%d %s)" % (len(items), _plural(site.item_noun, len(items))), ""]
    for it in items:
        L.append("- [%s](%s): %s" % (it.title or it.title_zh, it.page(site),
                                     clip(it.summary or it.summary_zh, 200)))
    L.append("")
    ok = _write(os.path.join(root, "llms.txt"), "\n".join(L))

    F = ["# %s — %s" % (site.name, site.tagline),
         "# %s — %s" % (site.name_zh, site.tagline_zh),
         "# %s" % site.base,
         "# Full corpus, plain text. %d %s."
         % (len(items), _plural(site.item_noun, len(items))), ""]
    for it in items:
        F += ["=" * 72, "## %s" % (it.title or it.title_zh)]
        if it.title_zh and it.title and it.title_zh != it.title:
            F.append("## %s" % it.title_zh)
        F.append("URL: %s" % it.page(site))
        if it.has_zh() and not it.url_override:
            F.append("URL (中文): %s" % site.url("zh/i/%s/" % it.slug))
        if it.source_url:
            F.append("Source: %s" % it.source_url)
        if it.updated:
            F.append("Updated: %s" % it.updated)
        if it.tags:
            F.append("Tags: %s" % ", ".join(it.tags))
        F.append("")
        if it.summary:
            F += [plain(it.summary), ""]
        for h, b in it.blocks:
            F += ["### %s" % h if h else "", plain(b), ""]
        if it.has_zh():
            F.append("--- 中文 ---")
            if it.summary_zh:
                F += [plain(it.summary_zh), ""]
            for h, b in it.blocks_zh:
                F += ["### %s" % h if h else "", plain(b), ""]
    ok = _write(os.path.join(root, "llms-full.txt"), "\n".join(F)) or ok
    return ok


def write_rss(site, items, root=".", limit=50):
    xs = []
    for it in items[:limit]:
        u = urlq(it.page(site))
        xs.append("    <item><title>%s</title><link>%s</link><guid isPermaLink=\"true\">%s"
                  "</guid><description>%s</description></item>"
                  % (esc(it.title or it.title_zh), esc(u), esc(u),
                     esc(clip(it.summary or it.summary_zh, 400))))
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n  <channel>\n'
           "    <title>%s</title>\n    <link>%s</link>\n"
           '    <atom:link href="%s" rel="self" type="application/rss+xml"/>\n'
           "    <description>%s</description>\n    <language>zh-cn</language>\n%s\n"
           "  </channel>\n</rss>\n"
           % (esc(site.name + " — " + site.tagline), esc(site.base),
              esc(site.url("feed.xml")), esc(clip(site.description, 400)), "\n".join(xs)))
    return _write(os.path.join(root, "feed.xml"), xml)


# ----------------------------------------------------------------------- one call
def build(site, items, root=".", index_files=("index.html",), today="",
          how_built="", cite_as="", extra_urls=(), extra_sitemaps=(),
          item_pages=True, extra_ld=None, robots=True, sitemap=True, hubs=True):
    """Everything, in the right order. Returns a small report dict."""
    hs = build_hubs(site, items) if (hubs and item_pages) else []
    hub_of = {s: True for s, _n, _c in hs}
    rep = {"items": len(items),
           "zh_items": sum(1 for i in items if i.has_zh()),
           "hubs": len(hs),
           "pages": write_item_pages(site, items, root, hub_of) if item_pages else 0}
    n = 0
    for s, name, its in hs:
        if _write(os.path.join(root, "t", s, "index.html"), hub_page(site, s, name, its, hs)):
            n += 1
    rep["hub_pages"] = n
    if item_pages and items:
        rep["all_page"] = _write(os.path.join(root, "all", "index.html"),
                                 all_page(site, items, hs))
    rep["p404"] = _write(os.path.join(root, "404.html"), page_404(site, hs))
    rep["robots"] = write_robots(site, root, extra_sitemaps) if robots else False
    rep["sitemap"] = (write_sitemap(site, items if item_pages else [], root, today,
                                    extra_urls, hs) if sitemap else False)
    rep["llms"] = write_llms(site, items, root, how_built, cite_as, hs)
    rep["rss"] = write_rss(site, items, root)
    rep["index"] = sum(1 for f in index_files
                       if patch_index(os.path.join(root, f), site,
                                      items if item_pages else [], extra_ld=extra_ld,
                                      hubs=hs))
    return rep

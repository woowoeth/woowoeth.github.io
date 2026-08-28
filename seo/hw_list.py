# -*- coding: utf-8 -*-
from geo_kit import esc, clip, SITE, org_ld, itemlist_ld, head_block, sibling_links
from hw_theme import _shell, brand_html

def _mast(site, zh, crumb_last, kicker="", heading="", lede=""):
    return """
<header class=\"mast wrap\">
  <div class=\"mast-top\">
    %s
    <div class=\"mast-links\">
      <a class=\"pill\" href=\"%s\">目录</a>
      <a class=\"pill\" href=\"%s\">全部</a>
    </div>
  </div>
  <p class=\"slogan\">%s</p>
</header>
<div class=\"wrap\">
  <nav class=\"crumb\">
    <a href=\"%s\">首页</a><span class=\"sep\">/</span>
    <a href=\"%s\">%s</a><span class=\"sep\">/</span>%s
  </nav>
  %s
  <h1>%s</h1>
  %s
""" % (
        brand_html(SITE + "/"),
        esc(site.base), esc(site.url("all/")),
        esc(site.tagline_zh if zh else site.tagline),
        esc(SITE + "/"), esc(site.base), esc(site.name_zh if zh else site.name),
        esc(crumb_last),
        ('<p class=\"kicker\">%s</p>' % esc(kicker)) if kicker else "",
        esc(heading),
        ('<p class=\"dek\">%s</p>' % esc(lede)) if lede else "",
    )

def _cards(site, items, zh):
    bits = []
    for x in items:
        tags = x.tags or []
        k = tags[0] if tags else ""
        bits.append(
            '<a href=\"%s\">%s<strong>%s</strong><span class=\"s\">%s</span></a>'
            % (esc(x.page(site)),
               ('<span class=\"k\">%s</span>' % esc(k)) if k else "",
               esc(x.t(zh)), esc(clip(x.s(zh), 90)))
        )
    return '<div class=\"feed\">%s</div>' % "".join(bits)

def all_page(site, items, hubs):
    zh = site.zh()
    page_url = site.url("all/")
    label = "全部条目" if zh else "All entries"
    title = clip("%s — %s" % (label, site.name_zh if zh else site.name), 70)
    desc = "%s 的全部 %d 个%s，一页列完。" % (site.name_zh, len(items), site.item_noun_zh)
    ld = [org_ld(), itemlist_ld(site, items, zh)]
    hubline = "".join('<a href=\"%s\">%s</a>' % (esc(site.url("t/%s/" % s)), esc(n)) for s, n, _c in hubs)
    body = _mast(site, zh, label, heading=label, lede=desc)
    if hubline:
        body += '<nav class=\"hubs\">%s</nav>' % hubline
    body += _cards(site, items, zh)
    body += '<footer class=\"site-foot\"><p>%s</p></footer></div>' % sibling_links(site, zh)
    return _shell("zh-Hans" if zh else "en", title,
                  head_block(site, page_url, title, desc, zh=zh, ld=ld), body)

def hub_page(site, slug, name, its, hubs):
    zh = site.zh()
    page_url = site.url("t/%s/" % slug)
    title = clip("%s — %s" % (name, site.name_zh if zh else site.name), 70)
    desc = "%s 里关于「%s」的 %d 个%s。" % (site.name_zh, name, len(its), site.item_noun_zh)
    others = "".join(
        '<a href=\"%s\"%s>%s</a>' % (esc(site.url("t/%s/" % s)),
                                  ' class=\"on\"' if s == slug else "", esc(n))
        for s, n, _c in hubs)
    body = _mast(site, zh, name, kicker="主题", heading=name, lede=desc)
    if others:
        body += '<nav class=\"hubs\">%s</nav>' % others
    body += _cards(site, its, zh)
    body += '<footer class=\"site-foot\"><p>%s</p></footer></div>' % sibling_links(site, zh)
    return _shell("zh-Hans" if zh else "en", title,
                  head_block(site, page_url, title, desc, zh=zh, ld=[]), body)

def install(G):
    G.all_page = all_page
    G.hub_page = hub_page

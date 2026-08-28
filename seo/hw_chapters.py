# -*- coding: utf-8 -*-
"""Child essays hanging off a person/book map page. Not part of D[]."""
import json
import os
from geo_kit import esc, SITE, sibling_links
import hw_theme

SLOGAN = "100 个人物与典籍的生存智慧，跨越 2600 年"


HL = '<mark class="hl" style="background:transparent;color:#9d2933;font-weight:700;text-decoration:underline;text-decoration-color:#9d2933;text-underline-offset:.16em;text-decoration-thickness:1.5px">%s</mark>'
def rich(s):
    parts = str(s or "").split("==")
    out = []
    for i, p in enumerate(parts):
        t = esc(p)
        out.append((HL % t) if i % 2 else t)
    return "".join(out)


PARENTS = {
    "毛泽东": {
        "slug": "mao",
        "blurb": "深度阅读",
        "items": [
            {"k": "on-contradiction", "n": "矛盾论", "w": "一次只打一个结",
             "line": "一团乱麻里，先找那根一抽全松的线", "ready": True},
            {"k": "on-practice", "n": "实践论", "w": "从事里认识",
             "line": "道理不从书里完成", "ready": True},
            {"k": "on-protracted-war", "n": "论持久战", "w": "时间换力量",
             "line": "弱的一方先改战争的形状", "ready": True},
            {"k": "strategy-of-the-revolution", "n": "中国革命战争的战略问题", "w": "有什么枪打什么仗",
             "line": "别人的条令不能直接搬", "ready": True},
        ],
    }
}

CHAPTERS = [
    {
        "parent": "毛泽东", "parent_slug": "mao",
        "k": "on-contradiction", "n": "矛盾论", "w": "一次只打一个结",
        "src": "《矛盾论》（1937）",
        "dek": "事情同时在响，每件都像急事。这一篇要回答的不是怎么努力，是先打哪一个结：解了它，别的结自己会松。",
        "story": "1937 年在延安，毛把当时的乱局写成一张判断图：一个阶段里同时存在许多矛盾，只有一种起规定作用。抓住它，其余问题跟着改形状；抓错了，力气平摊给十件急事，看起来什么都在做，其实一件都没打穿。后来他打仗、整党、建国，重复的都是这一问：这一阶段的主要矛盾是什么。",
        "f": [
            {"n": "先找总开关",
             "d": "主要矛盾不是最急的事，也不是最难的事。是那件解了它，其他问题跟着改形状的事。没找到之前，动手越多，结打得越死。",
             "eg": "滴滴早期用户少、司机少、产品弱、对手凶，同时在响。总开关是司机够不够。钱全压在补贴司机上，循环才转起来。减肥先管嘴，转行先交出一个作品，都是同一条。"},
            {"n": "找到了还得敢砍",
             "d": "这一则就是==集中优势兵力==。==伤其十指，不如断其一指==。力量平摊等于没有力量。找到重点只是一半，敢为它放掉其他，才算抓住。",
             "eg": "找到重点的人很多。清单仍在变长、主项目仍交不出来的人，多半是还没敢砍。"},
            {"n": "阶段一变，结就变",
             "d": "主要矛盾不是固定的。用上一个阶段的打法，打这一个阶段的仗，必输。",
             "eg": "2021 年双减之后，新东方的主要矛盾从「怎么把教培做好」变成「这群人和这家公司怎么活」。还在旧打法里换马甲的同行越陷越深；承认昨天的仗打完了的那一方，才进了直播间。"},
        ],
        "apply": "局面：几件事同时在响，每件都像不能放。\n先问：只解哪一件，其余大半会自己松？\n用反了：清单还在变长，那件能带动其余的事仍交不出来；季度过了，打法还是上一个阶段的打法。",
        "q": [
            "在复杂的事物的发展过程中，有许多的矛盾存在，其中必有一种是主要的矛盾，由于它的存在和发展规定或影响着其他矛盾的存在和发展。",
            "捉住了这个主要矛盾，一切问题就迎刃而解了。",
            "==伤其十指，不如断其一指。==",
        ],
    },
    {
        "parent": "毛泽东", "parent_slug": "mao",
        "k": "on-practice", "n": "实践论", "w": "从事里认识",
        "src": "《实践论》（1937）",
        "dek": "道理听懂了，局面没变。这一篇要回答的是：认识从哪里来。不从书里完成，从把事做出去的那一步里完成。",
        "story": "和《矛盾论》同一年写于延安。当时队伍里一种人专门背条令、背文件，把别的战场上的结论当成自己的认识；另一种人只凭感觉冲。毛要说的是：真正的认识不做完这两端。它从做里来，做完还得再看，看完还得再做。光会背，叫==本本主义==。",
        "f": [
            {"n": "认识从做里来",
             "d": "听懂不等于会。一个判断没经过事情的反敲，只是一句还没付过账的话。真正留下来的认识，都是在把事做出去之后才硬的。",
             "eg": "会讲产品的人很多。把第一个付费用户拿下来的人很少。前者还在认识外面，后者才进了认识里面。"},
            {"n": "做完还要再看",
             "d": "做一次不够。做完不回头看，留下的只是疲劳。看完不再做，留下的只是感想。认识是一个圈：做——看——再做。",
             "eg": "同一套打法用了三季，指标不动，还在加班加量的团队，多半停在「做了没看」。"},
            {"n": "书不能替代这一步",
             "d": "==反对本本主义==不是反对书，是反对把书当成已经完成的认识。别人写下的结论，只能帮你起步，不能替你走完这一圈。",
             "eg": "照搬别家的战略文档、照搬别人的成功案例，然后怪自己这块地不灵。灵的不是案例，是案例经过了你这块地。"},
        ],
        "apply": "局面：方法论堆了一桌子，第一个真局面还没接手。\n先问：这句话经过哪一件已经发生的事？\n用反了：讲得清的越来越多，交出去的东西越来越少；把别人的复盘当成自己的经验。",
        "q": [
            "实践的观点是辩证认识的真理标准。",
            "你要知道梨子的滋味，你就得变革梨子，亲口吃一吃。",
            "==没有调查，就没有发言权。==",
        ],
    },
    {
        "parent": "毛泽东", "parent_slug": "mao",
        "k": "on-protracted-war", "n": "论持久战", "w": "时间换力量",
        "src": "《论持久战》（1938）",
        "dek": "弱的一方如果按对方的节奏打，必输。这一篇要回答的是：怎么把战争拖成自己能打的形状。",
        "story": "1938 年徐州、南京之后，两种错法同时很响：一种说中国必亡，一种说很快就能打赢。毛在延安把已经发生的仗和还没发生的仗画在同一张图上：战略防御、战略相持、战略反攻。他不是在预言日期，是在规定不能做什么——不能拿主力去换一座城的新闻，不能在拳头还没形成时求决战。",
        "f": [
            {"n": "先活下来，再谈胜",
             "d": "弱者的第一目标不是歼灭，是让对方消灭不了你。主力在，时间就在；主力赌光了，时间立刻归零。",
             "eg": "放弃延安那年，用空间换部队。城丢了，拳头还在，后面才有运动中的歼灭。一城一地都要报捷的打法，看起来积极，其实是在帮对方完成决战。"},
            {"n": "相持不是停，是换规则",
             "d": "中间那段最像「没进展」，其实是战争从对方擅长的速决，改成你擅长的消耗。谁先忍受不了相持，谁就会提前决战。",
             "eg": "对手用钱砸速度时，你若跟着比速度，就是在他的规则里决战。相持期要做的，是让对方占着点却守不住面。"},
            {"n": "反攻要等拳头形成",
             "d": "反攻不是心情好转，是分散的力量收成了可移动的拳头。没形成就反攻，叫送。形成了还装相持，叫把时间浪费在已经消失的阶段上。",
             "eg": "后期转入反攻，靠的不是口号换了，是部队、根据地、补给已经够打运动战。用户口碑还没连成网络就全面开战，是提前毕业。"},
        ],
        "apply": "局面：你比对方弱，对面在逼你这周见分晓。\n先问：这一仗是在买时间，还是在花掉时间？\n用反了：为了证明自己没在拖，开始用主力换可见的小胜；日历上全是战役，没有哪一周在长拳头。",
        "q": [
            "亡国论者和速胜论者都是错的。",
            "抗日战争是持久战，最后胜利属于中国。",
            "武器是战争的重要因素，但不是决定的因素。决定的因素是人不是物。",
        ],
    },
    {
        "parent": "毛泽东", "parent_slug": "mao",
        "k": "strategy-of-the-revolution", "n": "中国革命战争的战略问题",
        "w": "有什么枪打什么仗",
        "src": "《中国革命战争的战略问题》（1936）",
        "dek": "别人的胜仗不能直接搬。这一篇要回答的是：你这块地、这点人、这点枪，打法应该长什么样。",
        "story": "1936 年红军还在西北。队伍里流行两套打法：一套是苏军教范，一套是北伐的记忆。毛把这两套都放下，重新问：中国这块地的战争有什么性质？敌强我弱、敌大我小，打法就不能是对方那套。这篇把==反对本本主义==写成战场规则，把==集中优势兵力==写成操作口令。",
        "f": [
            {"n": "反对本本主义",
             "d": "==反对本本主义==不是反对学，是反对不看自己这块地。苏军怎么打、北伐怎么打，都是别人的答案。搬过来当条令，第一仗就输在地形上。",
             "eg": "公司里照搬互联网巨头的组织架构，互联网公司照搬制造业的排班，都是本本。书可以帮你起步，不能替你打完这一仗。"},
            {"n": "集中优势兵力",
             "d": "==集中优势兵力，各个歼灭敌人==。三个打一个，打完再换一个。平摊开去，看起来到处都在打，其实一处都没打穿。这一则和《矛盾论》里的「敢砍」是同一条，这里写的是打法。",
             "eg": "产品线上五个新功能同时推，没有一个能说服用户为什么留下。先把一个打穿，再打第二个，才是集中。"},
            {"n": "你的战场不是别人的战场",
             "d": "敌强我弱、敌大我小的地方，不能按敌强我强的地方那套打。有什么枪打什么仗，不是自慰，是把打法钉在自己的实力上。",
             "eg": "初创团队照搬上市公司的战役节奏，资金和人手都跟不上。先问自己这点人能打穿哪一块，再决定这周打哪一块。"},
        ],
        "apply": "局面：手上有一份别人赢过的打法，你这块地和他不一样。\n先问：这套打法依赖的条件，我们有几条？\n用反了：仍在用别人的组织图和战役日历；同时开五条线，没有一条打穿。",
        "q": [
            "==没有调查，没有发言权。==",
            "==集中优势兵力，各个歼灭敌人。==",
            "我们的战略方针是以一当十，我们的战术方针是以十当一。",
        ],
    },
]


def f_span_raw(source, plain_span):
    """Map a span picked from the plain text back onto the ==marked== original."""
    import re as _re
    flat, index = [], []
    for i, chunk in enumerate(str(source or "").split("==")):
        for j, chvalue in enumerate(chunk):
            flat.append(chvalue)
            index.append((i, j))
    plain = "".join(flat)
    at = plain.find(plain_span)
    if at < 0:
        return plain_span
    end = at + len(plain_span)
    out, depth = [], 0
    for k in range(at, end):
        seg = index[k][0]
        while depth < seg:
            out.append("==")
            depth += 1
        out.append(flat[k])
    if depth % 2:
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
    toc = [("s1", "这一篇在解决什么局面"), ("s2", "背后是什么故事")]
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
    toc += [("s7", "今天怎么用"), ("quotes", "金句")]
    # 金句: 1-3 lines lifted from the 分则 they close (option A), plus the full
    # 原文 list restored as a section at the foot.
    import hw_theme as _t
    cands = []
    import re as _re
    for i, f in enumerate(ch["f"]):
        whole = _plain(f["d"]) + _plain(f.get("eg", ""))
        for span in _t._spans(whole):
            if len(whole) - len(span) < 45:          # must be an excerpt, not the section
                continue
            own = _re.sub(r"\u300c[^\u300d]*\u300d", "", span)
            if len(own.strip("\u3002\uff0c\u3001\uff01\uff1f\uff1b\uff1a\u2014 ")) < 20:
                continue
            cands.append((i, span, _t._quotability(span)))
    want = max(1, min(3, len(ch["f"])))
    chosen = _t._pick_pullquotes([c for c in cands if c[2] > 0], want)
    after = {}
    for i, span, _sc in chosen:
        raw = f_span_raw(ch["f"][i]["d"], span)
        after[i] = '<blockquote class="say"><p>%s</p></blockquote>' % rich(raw)
    body_points = "\n".join(
        pt + ("\n" + after[i] if i in after else "") for i, pt in enumerate(points))
    quotes = "".join("<blockquote><p>%s</p></blockquote>" % rich(q) for q in ch["q"])
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
      <aside class="pull">%s</aside>
      <section class="sec" id="s1"><h2 class="sec-k">这一篇在解决什么局面</h2>
      <p>%s</p></section>
      <section class="sec" id="s2"><h2 class="sec-k">背后是什么故事？</h2>
      <p>%s</p></section>
      %s
      <section class="sec apply" id="s7"><h2 class="sec-k">今天怎么用？</h2>%s</section>
      <section class="quotes" id="quotes"><h2 class="sec-k">金句</h2>%s</section>
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
        esc(parent), esc(ch["w"]), share, rich(ch["dek"]),
        rich(ch["dek"]), rich(ch["story"]), body_points, apply_paras, quotes,
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

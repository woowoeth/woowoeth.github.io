#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SEO/GEO build for Human World. Run from repo root: python seo/build_seo.py"""
import datetime
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import geo_kit as G
import hw_theme
hw_theme.install(G)
import hw_slugs
import hw_kind
import hw_chapters
import strip_cite

# Remember the pristine function, not whatever is installed now: importing this
# module twice would otherwise wrap the patched slugify around itself and
# recurse until the stack blows.
_orig_slugify = getattr(G, "_hw_orig_slugify", None) or G.slugify
G._hw_orig_slugify = _orig_slugify

def slugify(s, fallback="item"):
    mapped = hw_slugs.slug_for(s)
    if mapped and not any("\u4e00" <= ch <= "\u9fff" for ch in mapped):
        return mapped
    if s in hw_slugs.TAG_SLUGS:
        return hw_slugs.TAG_SLUGS[s]
    key = str(s or "").replace("\u00b7", "")
    if key in hw_slugs.TAG_SLUGS:
        return hw_slugs.TAG_SLUGS[key]
    return _orig_slugify(s, fallback)

G.slugify = slugify

SITE = G.Site(
    path="",
    name="Human World", name_zh="\u4eba\u7c7b\u4e16\u754c\u751f\u5b58\u6cd5\u5219",
    tagline="%(n)d people and books on how the world actually works, across 2,600 years",
    tagline_zh="\u9047\u5230\u4e8b\u4e86\uff0c\u770b\u770b\u4ee5\u524d\u7684\u4eba\u600e\u4e48\u5904\u7406",
    description=(
        "A knowledge base of the durable rules people have worked out about strategy, money, "
        "power, human nature and building things — drawn from %(n)d figures and "
        "classic texts across 2,600 years. Each entry gives the one idea that person is "
        "actually remembered for, the story behind it, the sub-principles with worked "
        "examples, and how it applies today."),
    description_zh=(
        "\u4e00\u4e2a\u5173\u4e8e\u300c\u4e16\u754c\u5230\u5e95\u600e\u4e48\u8fd0\u8f6c\u300d\u7684\u77e5\u8bc6\u5e93\uff1a\u6218\u7565\u3001\u8d22\u5bcc\u3001\u6743\u529b\u3001\u4eba\u6027\u3001\u521b\u4e1a\uff0c\u53d6\u81ea %(n)d \u4f4d"
        "\u4eba\u7269\u4e0e\u5178\u7c4d\uff0c\u8de8\u8d8a 2600 \u5e74\u3002\u6bcf\u4e00\u6761\u90fd\u5199\u6e05\u695a\u8fd9\u4e2a\u4eba\u771f\u6b63\u7559\u4e0b\u7684\u90a3\u4e00\u4e2a\u60f3\u6cd5\u3001\u80cc\u540e\u7684\u6545\u4e8b\u3001"
        "\u62c6\u5f00\u7684\u5206\u5219\u4e0e\u4f8b\u5b50\uff0c\u4ee5\u53ca\u4eca\u5929\u600e\u4e48\u7528\u3002"),
    keywords=("\u751f\u5b58\u667a\u6167, \u6218\u7565\u601d\u7ef4, \u5b59\u5b50\u5175\u6cd5, \u4eba\u6027, \u8d22\u5bcc \u6295\u8d44 \u539f\u5219, \u6743\u529b \u6cbb\u7406, \u521b\u4e1a \u65b9\u6cd5\u8bba, "
              "\u7ecf\u5178 \u89e3\u8bfb, life principles, strategy, human nature, classic texts"),
    item_type="Article", item_noun="entry", item_noun_zh="\u6761\u76ee",
    lang="zh-Hans", changefreq="weekly",
)

HOW = ("Written by hand, one entry per figure or text. Each entry is condensed to the single "
       "idea that person is actually remembered for, then unpacked into sub-principles with "
       "historical and modern worked examples.")

CITE = ("Cite the individual entry page. Quotes from classical texts inside an entry belong to "
        "those texts; attribute the condensation and the modern reading to "
        "\"\u4eba\u7c7b\u4e16\u754c\u751f\u5b58\u6cd5\u5219 (OurWord AI)\".")


def load_array(path="index.html", varname="D"):
    s = open(path, encoding="utf-8").read()
    m = re.search(r"(?:const|let|var)\s+%s\s*=\s*\[" % re.escape(varname), s)
    if not m:
        return []
    j = s.index("[", m.start())
    depth, k = 0, j
    while k < len(s):
        c = s[k]
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
            if depth == 0:
                break
        elif c == '"':
            k += 1
            while k < len(s) and s[k] != '"':
                if s[k] == "\\":
                    k += 1
                k += 1
        k += 1
    raw = s[j:k + 1]
    raw = re.sub(r"([{,]\s*)([A-Za-z_]\w*)\s*:",
                 lambda mm: '%s"%s":' % (mm.group(1), mm.group(2)), raw)
    raw = re.sub(r",\s*([}\]])", r"\1", raw)
    return json.loads(raw)


def flat(v):
    if v is None:
        return ""
    if isinstance(v, str):
        return v
    out = []
    for x in (v if isinstance(v, list) else [v]):
        if isinstance(x, dict):
            head = x.get("n") or x.get("name") or x.get("t") or ""
            body = x.get("why") or x.get("d") or x.get("desc") or x.get("eg") or ""
            out.append(("%s\uff1a%s" % (head, body)).strip("\uff1a") if head or body else "")
        else:
            out.append(str(x))
    return "\n".join(o for o in out if o)


def era_bucket(y):
    try:
        y = int(y)
    except Exception:
        return ""
    for lo, hi, label in ((-3000, -200, "\u5148\u79e6\u4e0e\u53e4\u5178\u65f6\u4ee3"), (-200, 400, "\u79e6\u6c49\u81f3\u9b4f\u664b"),
                          (400, 1400, "\u4e2d\u53e4"), (1400, 1800, "\u8fd1\u4e16"),
                          (1800, 1950, "\u5de5\u4e1a\u65f6\u4ee3"), (1950, 3000, "\u73b0\u4ee3")):
        if lo <= y < hi:
            return label
    return ""


def load_items():
    items = []
    entries = list(load_array())
    rev_l, rev_c = {}, {}
    for e in entries:
        src = e.get("n") or ""
        for x in (e.get("l") or []):
            rev_l.setdefault(x, []).append(src)
        for c in (e.get("contrast") or []):
            if isinstance(c, dict) and c.get("n"):
                rev_c.setdefault(c["n"], []).append({"n": src, "why": c.get("why") or ""})
    missing = []
    for e in entries:
        name = e.get("n") or ""
        sl = hw_slugs.slug_for(name)
        if any("\u4e00" <= ch <= "\u9fff" for ch in sl):
            missing.append(name)
        rel = list(e.get("l") or [])
        seen = set(rel)
        for x in rev_l.get(name, []):
            if x != name and x not in seen:
                seen.add(x)
                rel.append(x)
        ctr = [c for c in (e.get("contrast") or []) if isinstance(c, dict)]
        seen_c = {c.get("n") for c in ctr}
        for c in rev_c.get(name, []):
            if c["n"] != name and c["n"] not in seen_c:
                seen_c.add(c["n"])
                ctr.append(c)
        e_year = e.get("y")
        one = e.get("w") or ""
        era = e.get("e") or ""
        cat = e.get("c") or ""
        blocks = []
        if e.get("d"):
            blocks.append(("Q\uff1a\u8fd9\u4e2a\u4eba\uff08\u8fd9\u672c\u4e66\uff09\u5230\u5e95\u7559\u4e0b\u4e86\u4ec0\u4e48\uff1f", e["d"]))
        if e.get("story"):
            blocks.append(("Q\uff1a\u80cc\u540e\u662f\u4ec0\u4e48\u6545\u4e8b\uff1f", e["story"]))
        for f in (e.get("f") or []):
            if not isinstance(f, dict):
                continue
            body = f.get("d") or ""
            if f.get("eg"):
                body += "\n\u4f8b\uff1a" + f["eg"]
            if body:
                blocks.append(("\u5206\u5219 \u00b7 %s" % (f.get("n") or ""), body))
        # 败局时刻：23 个条目写了 fail/lesson，但从来没有任何一个
        # 渲染器读它们——大概是 2026-08-17 改版后的遗留，
        # 那一次首页卡片从浮层改成跳 /i/<slug>/。
        # 位置在「分则」之后、「今天怎么用」之前：
        # 先看他留下什么，再看它在他自己身上怎么失效的，
        # 然后才轮到你怎么用。标题不用「他」，因为 23 个里有书。
        if e.get("fail") or e.get("lesson"):
            fb = e.get("fail") or ""
            if e.get("lesson"):
                fb = (fb + "\n" + flat(e["lesson"])).strip("\n")
            if fb:
                blocks.append(("Q\uff1a\u540e\u6765\u600e\u4e48\u4e86\uff1f", fb))
        if e.get("apply"):
            blocks.append(("Q\uff1a\u4eca\u5929\u600e\u4e48\u7528\uff1f", flat(e["apply"])))
        if e.get("q"):
            blocks.append(("\u91d1\u53e5", flat(e["q"])))
        if ctr:
            blocks.append(("Q\uff1a\u548c\u8c01\u5bf9\u7167\u7740\u8bfb\uff1f", flat(ctr)))
        if rel:
            blocks.append(("\u5ef6\u4f38", flat(rel)))
        summary = "%s%s\u2014\u2014%s\u3002%s" % (name, ("\uff08%s\uff09" % era if era else ""), one,
                                   G.plain(e.get("d"), 140))
        # 原来靠 name 里的关键词猜（经/论/简史/兵法/书/记/传/录）加两个手工补丁，
        # 140 个条目只认出 11 个——《稀缺》《系统之美》《优秀的绵羊》《老鼠公园》
        # 这些全被打成了 schema.org/Person。改用 hw_kind 的显式表。
        is_text = hw_kind.is_work(name)
        extra = ({"about": one} if one else {})
        if is_text:
            extra["bookFormat"] = "https://schema.org/Hardcover"
        items.append(G.Item(
            slug=sl, title=name, summary=summary,
            blocks=blocks,
            tags=[t for t in [cat, era_bucket(e_year), one] if t],
            updated="",
            schema_type="Book" if is_text else "Person",
            schema_extra=extra,
        ))
    if missing:
        print("warn hw_slugs still CJK:", ", ".join(missing))
    items.sort(key=lambda i: i.title)
    return items


def fill_counts(site, n):
    for attr in ("tagline", "tagline_zh", "description", "description_zh"):
        v = getattr(site, attr, "")
        if "%(n)d" in v:
            setattr(site, attr, v % {"n": n})
    return site


def patch_static_stats(entries, path="index.html"):
    n = len(entries)
    cats = len({e.get("c") for e in entries if e.get("c")})
    src = open(path, encoding="utf-8").read()
    out, hits = src, {}
    for key, val in (("st", n), ("cat-count", cats)):
        pat = re.compile(r'(<b id="%s">)([^<]*)(</b>)' % re.escape(key))
        m = pat.search(out)
        if not m:
            # 页头那排 stats 已经撤掉（和 logo 旁的标语重复），节点不再存在。
            # 首页计数现在由 force_chapter_ui 写进 title 和标语，并由
            # check_integrity 校验，所以这里没有节点是正常的，不该让构建失败。
            hits[key] = "absent"
            continue
        hits[key] = "%s->%s" % (m.group(2) or "empty", val)
        out = pat.sub(lambda mm: "%s%d%s" % (mm.group(1), val, mm.group(3)), out, count=1)
    if out != src:
        open(path, "w", encoding="utf-8").write(out)
    return hits


def _redirect_html(dest, title):
    dest = dest if dest.startswith("http") else "https://ourword.ai" + dest
    return (
        "<!DOCTYPE html>\n<html lang=\"zh-Hans\"><head>\n"
        "<meta charset=\"utf-8\">\n"
        "<meta http-equiv=\"refresh\" content=\"0;url=%s\">\n"
        "<link rel=\"canonical\" href=\"%s\">\n"
        "<title>%s</title>\n"
        "<script>location.replace(%s);</script>\n"
        "</head><body><p><a href=\"%s\">Moved to %s</a></p></body></html>\n"
        % (G.esc(dest), G.esc(dest), G.esc(title), json.dumps(dest), G.esc(dest), G.esc(dest))
    )


def write_legacy_redirects(root="."):
    """已停用。中文路径的旧 URL 从未对外发布过，没有权重需要传递，
    而每次构建都要重写 116 个文件、并让 force_chapter_ui 逐页判断跳过。
    留空函数而不是删掉调用点，是为了让报告里的 legacy_redirects 仍为 0。"""
    return 0
    n = 0
    pairs = list(hw_slugs.SLUGS.items()) + [("\u738b\u5265", "wang-jian"),
                                         ("\u738b\u7fe6", "wang-jian"),
                                         ("\u6731\u5143\u748b", "zhu-yuanzhang")]
    for name, new in pairs:
        old = hw_slugs.cjk_slug(name)
        if not old or old == new:
            continue
        dest = "/i/%s/" % new
        path = os.path.join(root, "i", old, "index.html")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        html = _redirect_html(dest, name)
        if not os.path.exists(path) or open(path, encoding="utf-8").read() != html:
            open(path, "w", encoding="utf-8").write(html)
            n += 1
    seen = set()
    for tag, new in hw_slugs.TAG_SLUGS.items():
        old = hw_slugs.cjk_slug(tag)
        if not old or old == new or old in seen:
            continue
        seen.add(old)
        dest = "/t/%s/" % new
        path = os.path.join(root, "t", old, "index.html")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        html = _redirect_html(dest, tag)
        if not os.path.exists(path) or open(path, encoding="utf-8").read() != html:
            open(path, "w", encoding="utf-8").write(html)
            n += 1
    return n



LASTMOD_DB = os.path.join("seo", "lastmod.json")


def _fingerprint(it):
    """Stable hash of what a page actually shows."""
    h = hashlib.sha1()
    h.update((it.title or "").encode("utf-8"))
    h.update(b"\x00")
    h.update((it.summary or "").encode("utf-8"))
    for head, body in it.blocks:
        h.update(b"\x00")
        h.update(("%s\x01%s" % (head, body)).encode("utf-8"))
    return h.hexdigest()[:16]


def stamp_lastmod(items, today, extra=None):
    """Give every URL a lastmod that reflects the last real content change.

    Items carried updated="" so write_sitemap fell back to the build date: all 119
    URLs claimed they changed today, every day the cron ran. That is both the
    signal geo_kit's own docstring warns engines learn to discount, and a
    guaranteed daily commit with no content behind it. The manifest records a
    content hash per URL and only moves the date when the hash moves.
    """
    try:
        db = json.load(open(LASTMOD_DB, encoding="utf-8"))
    except Exception:
        db = {}
    seen = {}
    for it in items:
        key = "i/%s/" % it.slug
        fp = _fingerprint(it)
        rec = db.get(key)
        date = rec["d"] if (rec and rec.get("h") == fp and rec.get("d")) else today
        seen[key] = {"h": fp, "d": date}
        it.updated = date
    for key, fp in (extra or {}).items():
        rec = db.get(key)
        seen[key] = {"h": fp, "d": rec["d"] if (rec and rec.get("h") == fp and rec.get("d")) else today}
    out = json.dumps(seen, ensure_ascii=False, indent=1, sort_keys=True) + "\n"
    if not os.path.exists(LASTMOD_DB) or open(LASTMOD_DB, encoding="utf-8").read() != out:
        os.makedirs(os.path.dirname(LASTMOD_DB), exist_ok=True)
        open(LASTMOD_DB, "w", encoding="utf-8").write(out)
    return max((v["d"] for v in seen.values()), default=today)


def stamp_feed(root=".", dates=None):
    """RSS shipped with no <pubDate> and no <lastBuildDate>; readers had nothing
    to sort or de-duplicate on."""
    path = os.path.join(root, "feed.xml")
    if not os.path.exists(path):
        return False
    src = open(path, encoding="utf-8").read()
    out = re.sub(r"\s*<pubDate>[^<]*</pubDate>", "", src)
    out = re.sub(r"\s*<lastBuildDate>[^<]*</lastBuildDate>", "", out)

    def rfc822(d):
        try:
            y, m, dd = (int(x) for x in d.split("-"))
        except Exception:
            return ""
        dt = datetime.datetime(y, m, dd, 8, 0, 0)
        return dt.strftime("%a, %d %b %Y %H:%M:%S +0800")

    def add(m):
        chunk = m.group(0)
        link = re.search(r"<link>([^<]+)</link>", chunk)
        key = link.group(1).replace("https://ourword.ai/", "") if link else ""
        d = (dates or {}).get(key)
        stamp = rfc822(d) if d else ""
        return chunk.replace("</item>", "<pubDate>%s</pubDate></item>" % stamp) if stamp else chunk

    out = re.sub(r"<item>.*?</item>", add, out, flags=re.S)
    newest = max((dates or {}).values(), default="")
    if newest:
        out = out.replace("<language>zh-cn</language>",
                          "<language>zh-cn</language>\n    <lastBuildDate>%s</lastBuildDate>"
                          % rfc822(newest), 1)
    if out != src:
        open(path, "w", encoding="utf-8").write(out)
        return True
    return False


def _url_dates(items, ch_fp):
    try:
        db = json.load(open(LASTMOD_DB, encoding="utf-8"))
    except Exception:
        db = {}
    return {k: v.get("d", "") for k, v in db.items() if v.get("d")}


def restamp_sitemap(root="."):
    """把 sitemap 里的 lastmod 换成每个 URL 自己的真实日期。

    geo_kit.write_sitemap 对 extra_urls（319 个章节页）一律盖上构建当天的日期，
    它的 API 没给按 URL 传日期的口子，而 geo_kit.py 是禁改的（CI 会还原）。
    结果是 477 条里 391 条天天标着"今天"——geo_kit 自己的注释就写着，
    一个声称所有页面都变了的 sitemap，引擎学会的是忽略这个字段。

    真实日期在 seo/lastmod.json 里是全的（459 条 = 140 条目 + 319 章节，
    stamp_lastmod 按内容指纹算出来的），这里只是把它们贴回去。
    """
    import re
    sm = os.path.join(root, "sitemap.xml")
    if not os.path.exists(sm):
        return 0
    try:
        db = json.load(open(LASTMOD_DB, encoding="utf-8"))
    except Exception:
        return 0
    base = SITE.base.rstrip("/") + "/"
    src = open(sm, encoding="utf-8").read()
    n = [0]

    def fix(m):
        loc, lm = m.group(1), m.group(2)
        rel = loc[len(base):] if loc.startswith(base) else ""
        real = (db.get(rel) or {}).get("d")
        if real and real != lm:
            n[0] += 1
            return m.group(0).replace(">%s<" % lm, ">%s<" % real, 1)
        return m.group(0)

    out = re.sub(r"<loc>([^<]*)</loc><lastmod>([^<]*)</lastmod>", fix, src)
    if out != src:
        open(sm, "w", encoding="utf-8").write(out)
    return n[0]


def main():
    items = load_items()
    fill_counts(SITE, len(items))
    today = datetime.date.today().isoformat()
    ch_fp = hw_chapters.chapter_fingerprints()
    newest = stamp_lastmod(items, today, extra=ch_fp)
    rep = G.build(SITE, items, root=".", today=newest,
                  how_built=HOW, cite_as=CITE,
                  # robots.txt 只在**域名根**生效 —— /podcast/robots.txt 和
                  # /skill/robots.txt 爬虫根本不看（geo_kit 自己的注释也这么写：
                  # 「the authoritative one for this domain is /robots.txt」）。
                  # 所以三个站、六份 sitemap 都得在这里声明，少一条就是那半个站
                  # 没有被主动提交过地图，只能等爬虫自己撞见。
                  extra_sitemaps=[
                      "https://ourword.ai/tw/sitemap.xml",
                      "https://ourword.ai/podcast/sitemap.xml",
                      "https://ourword.ai/podcast/tw/sitemap.xml",
                      "https://ourword.ai/skill/sitemap.xml",
                      "https://ourword.ai/skill/tw/sitemap.xml",
                  ],
                  extra_urls=hw_chapters.chapter_urls())
    rep["chapters"] = hw_chapters.write_chapters()
    rep["chapter_index"] = hw_chapters.write_indexes()
    rep["strip_cite"] = strip_cite.strip_cite()
    rep["stats"] = patch_static_stats(load_array())
    rep["legacy_redirects"] = write_legacy_redirects()
    rep["feed_dates"] = stamp_feed(".", _url_dates(items, ch_fp))
    rep["sitemap_dates"] = restamp_sitemap(".")
    print("HumanWorld seo/geo:", json.dumps(rep, ensure_ascii=False))
    return rep


if __name__ == "__main__":
    main()

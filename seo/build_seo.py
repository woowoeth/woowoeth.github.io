#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SEO/GEO build for Human World. Run from repo root: python seo/build_seo.py"""
import datetime
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import geo_kit as G
import hw_theme
hw_theme.install(G)
import hw_slugs
import hw_chapters

_orig_slugify = G.slugify

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
    tagline_zh="%(n)d \u4e2a\u4eba\u7269\u4e0e\u5178\u7c4d\u7684\u751f\u5b58\u667a\u6167\uff0c\u8de8\u8d8a 2600 \u5e74",
    description=(
        "A knowledge base of the durable rules people have worked out about strategy, money, "
        "power, human nature and building things — drawn from %(n)d figures and "
        "classic texts across 2,600 years. Each entry gives the one idea that person is "
        "actually remembered for, the story behind it, the sub-principles with worked "
        "examples, and how it applies today."),
    description_zh=(
        "\u4e00\u4e2a\u5173\u4e8e\u300c\u4e16\u754c\u5230\u5e95\u600e\u4e48\u8fd0\u8f6c\u300d\u7684\u77e5\u8bc6\u5e93\uff1a\u6218\u7565\u3001\u8d22\u5bcc\u3001\u6743\u529b\u3001\u4eba\u6027\u3001\u521b\u4e1a\uff0c\u53d6\u81ea %(n)d \u4f4d"
        "\u4eba\u7269\u4e0e\u5178\u7c4d\uff0c\u8de8\u8d8a 2600 \u5e74\u3002\u6bcf\u4e00\u6761\u90fd\u5199\u6e05\u695a\u8fd9\u4e2a\u4eba\u771f正留下的那一个想法、背后的故事、"
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
        if e.get("apply"):
            blocks.append(("Q\uff1a\u4eca\u5929\u600e\u4e48\u7528\uff1f", flat(e["apply"])))
        if e.get("q"):
            blocks.append(("\u539f\u8bdd", flat(e["q"])))
        if ctr:
            blocks.append(("Q\uff1a\u548c\u8c01\u5bf9\u7167\u7740\u8bfb\uff1f", flat(ctr)))
        if rel:
            blocks.append(("\u5ef6\u4f38", flat(rel)))
        summary = "%s%s\u2014\u2014%s\u3002%s" % (name, ("\uff08%s\uff09" % era if era else ""), one,
                                   G.plain(e.get("d"), 140))
        is_text = (cat == "\u5178\u7c4d\u00b7\u6d1e\u89c1") or any(
            k in name for k in ("\u7ecf", "\u8bba", "\u7b80\u53f2", "\u5175\u6cd5", "\u53f2\u8bb0", "\u4e66", "\u8bb0", "\u4f20", "\u5f55"))
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
            raise SystemExit("patch_static_stats: missing <b id=\"%s\">" % key)
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
    n = 0
    pairs = list(hw_slugs.SLUGS.items()) + [("\u738b\u5265", "wang-jian"), ("\u6731\u5143\u748b", "zhu-yuanzhang")]
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


def main():
    items = load_items()
    fill_counts(SITE, len(items))
    _orig_item_page = G.item_page

    def item_page(site, it, items, idx, zh, hub_of=None):
        html = _orig_item_page(site, it, items, idx, zh, hub_of=hub_of)
        chunk = hw_chapters.catalog_html(it.title)
        if chunk and 'id="contrast"' in html:
            html = html.replace('<section id="contrast"', chunk + '<section id="contrast"', 1)
        elif chunk:
            html = html.replace('<nav class="sib">', chunk + '<nav class="sib">', 1)
        return html

    G.item_page = item_page
    hw_theme.item_page = item_page
    rep = G.build(SITE, items, root=".", today=datetime.date.today().isoformat(),
                  how_built=HOW, cite_as=CITE,
                  extra_sitemaps=[])
    rep["chapters"] = hw_chapters.write_chapters()
    rep["stats"] = patch_static_stats(load_array())
    rep["legacy_redirects"] = write_legacy_redirects()
    print("HumanWorld seo/geo:", json.dumps(rep, ensure_ascii=False))
    return rep


if __name__ == "__main__":
    main()

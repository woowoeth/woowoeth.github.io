#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""多语言互链：sitemap 补 <xhtml:link>，页面里指向不存在的 hreflang 就地摘掉。

    python3 scripts/lang_links.py

页面 <head> 里的 hreflang 早就对了（zh-Hans / zh-Hant / en / x-default），
搜索引擎两种都认；sitemap 这份是**第二个信号源**，两处一致时抓取更快、
也更不容易在多语言之间判错主版本。

为什么不改 seo/geo_kit.py 的 write_sitemap：那个函数是几个站共用的
（人类世界、原声、AI 泡沫检测仪、走你），而语言变体是 build_en / build_tw
事后改写出来的，生成时并不知道彼此存在。所以这一步放在构建链末尾做后处理。

规矩：
- 只写**本地真有那个文件**的语言。en/tw 没建出来的页不许硬写（写了就是死链信号）。
- 三份 sitemap 都要写，且互相对称：每一份里都列全部语言，包括它自己（规范要求）。
- x-default 指中文，和页面 <head> 里那条保持一致 —— 两处不一致等于自己跟自己打架。
- 幂等：已经有 xhtml:link 的不重复加。
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "seo"))
import topic_pairs                                    # noqa: E402  唯一的话题对应表

ZH2EN = topic_pairs.pairs()                           # {中文 slug: 英文 slug}
EN2ZH = dict((v, k) for k, v in ZH2EN.items())
SITE = "https://ourword.ai"
NS = "http://www.w3.org/1999/xhtml"
# 语言 → (sitemap 文件, URL 前缀, 本地目录前缀)
LANGS = [("zh-Hans", "sitemap.xml", "", ""),
         ("en", "en/sitemap.xml", "en/", "en/"),
         ("zh-Hant", "tw/sitemap.xml", "tw/", "tw/")]
XDEFAULT = "zh-Hans"


def rest_of(loc, prefix):
    """把 https://ourword.ai/<prefix><rest> 剥成 <rest>。不属于这一语言的返回 None。"""
    head = SITE + "/" + prefix
    if not loc.startswith(head):
        return None
    return loc[len(head):]


TOPIC = re.compile(r"^t/([^/]+)/$")


def to_lang(rest, src, dst):
    """把一种语言下的相对路径换成另一种语言的。话题页要换 slug，别的原样。

    三语的话题 slug 不同（/t/mind/ ↔ /en/t/mind-and-feeling/），
    以前这里是原样套前缀，于是英文话题页的 hreflang 指向 /t/<英文 slug>/ —— 404。
    """
    m = TOPIC.match(rest)
    if not m:
        return rest                                   # 章节页、条目页三语同 slug
    slug = m.group(1)
    if src == "en" and dst != "en":
        slug = EN2ZH.get(slug, slug)
    elif src != "en" and dst == "en":
        slug = ZH2EN.get(slug, slug)
    return "t/%s/" % slug


def exists(prefix, rest):
    """本地真有这一页吗。rest 形如 'i/postman/' 或 ''。"""
    rel = os.path.join(ROOT, prefix, rest)
    return os.path.exists(os.path.join(rel, "index.html")) or os.path.isfile(rel)


LANG_OF = {"": "zh", "en/": "en", "tw/": "zh"}       # slug 口径：繁体跟简体一致


def alt_block(rest, src_prefix, indent="    "):
    src = LANG_OF[src_prefix]
    out = []
    for lang, _f, prefix, dirp in LANGS:
        r = to_lang(rest, src, LANG_OF[prefix])
        if not exists(dirp, r):
            continue
        out.append('%s<xhtml:link rel="alternate" hreflang="%s" href="%s/%s%s"/>'
                   % (indent, lang, SITE, prefix, r))
    xd_dir = dict((l[0], l[3]) for l in LANGS)[XDEFAULT]
    xd_pre = dict((l[0], l[2]) for l in LANGS)[XDEFAULT]
    r = to_lang(rest, src, LANG_OF[xd_pre])
    if out and exists(xd_dir, r):
        out.append('%s<xhtml:link rel="alternate" hreflang="x-default" href="%s/%s%s"/>'
                   % (indent, SITE, xd_pre, r))
    return out


def do(path, prefix):
    p = os.path.join(ROOT, path)
    if not os.path.exists(p):
        return 0, 0, "没有 %s" % path
    t = io.open(p, encoding="utf-8").read()
    # 幂等做法：先把旧标注全摘掉再重建。原来是「有就跳过」，结果对应表改了之后
    # sitemap 永远停在旧答案上 —— 话题页那 16 条一直缺 en。
    t = re.sub(r"\n\s*<xhtml:link rel=\"alternate\"[^>]*/>", "", t)
    t = re.sub(r"\n\s*\n(\s*</url>)", r"\n\1", t)      # 摘干净，别留空行
    t = t.replace('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
                  '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"'
                  ' xmlns:xhtml="%s">' % NS, 1)
    done = [0]

    def one(m):
        whole, loc = m.group(0), m.group(1)
        rest = rest_of(loc, prefix)
        if rest is None:
            return whole
        alts = alt_block(rest, prefix)
        if len(alts) < 3:                      # 只有自己 + x-default 时不写，没有信息量
            return whole
        done[0] += 1
        body = whole[:-len("</url>")]
        return body + "\n" + "\n".join(alts) + "\n  </url>"

    t = re.sub(r"  <url><loc>([^<]+)</loc>.*?</url>", one, t, flags=re.S)
    io.open(p, "w", encoding="utf-8").write(t)
    return done[0], t.count("<url>"), ""


ALT_RE = re.compile(r'\s*<link rel="alternate" hreflang="[^"]*" href="([^"]+)">')


def local_of(url):
    """站内绝对地址换算成本地路径；不是本站的返回 None。"""
    if not url.startswith(SITE + "/"):
        return None
    return os.path.join(ROOT, url[len(SITE) + 1:])


def fix_topic_hreflang():
    """把三语话题页的 hreflang 改成真正互指 —— 治本的那一步。

    以前每页的 hreflang 是「同一个 rest 套三个前缀」，章节页对（三语同 slug），
    话题页错（三语 slug 不同）。现在按 seo/topic_pairs.py 这张唯一的对应表写。
    """
    fixed = 0
    for lang_dir, src in (("", "zh"), ("en", "en"), ("tw", "zh")):
        base = os.path.join(ROOT, lang_dir, "t") if lang_dir else os.path.join(ROOT, "t")
        if not os.path.isdir(base):
            continue
        for slug in sorted(os.listdir(base)):
            p = os.path.join(base, slug, "index.html")
            if not os.path.isfile(p):
                continue
            rest = "t/%s/" % slug
            lines = []
            for lang, _f, prefix, dirp in LANGS:
                r = to_lang(rest, src, LANG_OF[prefix])
                if exists(dirp, r):
                    lines.append('<link rel="alternate" hreflang="%s" href="%s/%s%s">'
                                 % (lang, SITE, prefix, r))
            xd_pre = dict((l[0], l[2]) for l in LANGS)[XDEFAULT]
            xd_dir = dict((l[0], l[3]) for l in LANGS)[XDEFAULT]
            r = to_lang(rest, src, LANG_OF[xd_pre])
            if len(lines) >= 2 and exists(xd_dir, r):
                lines.append('<link rel="alternate" hreflang="x-default" href="%s/%s%s">'
                             % (SITE, xd_pre, r))
            t = io.open(p, encoding="utf-8").read()
            old = ALT_RE.findall(t)
            if not old and not lines:
                continue
            new_block = "".join(lines)
            t2 = ALT_RE.sub("", t, count=len(old)) if old else t
            if lines:
                i = t2.find('<link rel="canonical"')
                if i < 0:
                    i = t2.find("</head>")
                j = t2.find(">", i) + 1 if t2[i:i + 20].startswith("<link rel=\"canon") else i
                t2 = t2[:j] + new_block + t2[j:]
            if t2 != t:
                io.open(p, "w", encoding="utf-8").write(t2)
                fixed += 1
    return fixed


def prune_dead_hreflang():
    """页面 <head> 里指向**不存在的页**的 hreflang，就地摘掉。

    2026-09-16 查出来的：16 个英文话题页（/en/t/<slug>/）的 hreflang 写着
    https://ourword.ai/t/<英文 slug>/ 和 /tw/t/<英文 slug>/ —— **两个都是 404**。
    根因：话题 slug 由 slugify(标签名) 派生，而三种语言的标签名不同
    （中文「心智」→ /t/mind/，英文 Mind and Feeling → /en/t/mind-and-feeling/），
    英文站改写站内地址时把 hreflang 那几行也一并换成了英文 slug。

    **指向 404 的 hreflang 比没有更糟**：搜索引擎会把整组判废。
    这里先把错的摘掉 —— 宁可只声明自己，也不要指一个不存在的页。
    真正的修法是让三语话题页互相指对，那要 build_en 把英文标签和中文标签的
    对应关系传下来。见 FAILURES #34。
    """
    fixed = pages = 0
    for dirp, _dn, fn in os.walk(ROOT):
        if os.sep + "." in dirp:
            continue
        for f in fn:
            if f != "index.html":
                continue
            p = os.path.join(dirp, f)
            t = io.open(p, encoding="utf-8", errors="ignore").read()
            if "hreflang=" not in t:
                continue
            pages += 1
            drop = []
            for m in ALT_RE.finditer(t):
                loc = local_of(m.group(1))
                if loc and not os.path.exists(os.path.join(loc, "index.html")) \
                        and not os.path.isfile(loc):
                    drop.append(m.group(0))
            if drop:
                for d in drop:
                    t = t.replace(d, "", 1)
                io.open(p, "w", encoding="utf-8").write(t)
                fixed += 1
    return fixed, pages


def main():
    rc = 0
    for lang, f, prefix, _d in LANGS:
        n, total, note = do(f, prefix)
        print("  %-16s %4d/%-4d 条加了多语言标注 %s" % (f, n, total, note))
        if note.startswith("没有"):
            rc = 1
    n = fix_topic_hreflang()
    print("  话题页：%d 页的 hreflang 按对应表重写（三语真正互指）" % n)
    fixed, pages = prune_dead_hreflang()
    print("  兜底：%d/%d 页摘掉了指向不存在页面的那几行" % (fixed, pages))
    left_en, left_zh = topic_pairs.missing(ROOT)
    if left_en:
        print("  ！英文话题没有对应关系：%s" % left_en)
        rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main())

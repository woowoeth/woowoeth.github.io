#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""语言站的链接落地检查。

    python3 scripts/check_links.py            # 查 tw/ 和 en/
    python3 scripts/check_links.py en         # 只查一个

为什么要单独一道：已有的「繁简两版链接集合一致」那条**结构上看不见这一类错**。
它把繁体链接里的 /tw/ 去掉再和简体比，所以只要两边一起错，它就一起放行。
一天之内这样漏掉了三个：

① 555 个繁体页的页脚指向 https://ourword.ai/tw/podcast/ —— 姊妹站是独立的站，
   它的繁体版在 /podcast/tw/，主站的语言前缀套不上去。
② build_tw 把 en/ 整棵树当简体内容转了一遍，塞出一堆 tw/en/… 的孤儿页。
③ 繁体页和英文页的 JSON-LD Article.url、页脚「本页可直接引用」那一行，
   都还指着简体页。canonical 改对了，这两处没有 —— 它们不是属性，
   按属性走的重写规则碰不到。

这道闸不比对两版，只问一件事：**这条地址指到的东西，在这个仓库里存在吗**。
两边一起错也躲不过去。

几类地址分别对待：
  · 本站页面     → 必须在构建产物里真有这个文件
  · 资源文件     → 英文站按设计不加前缀（用主站那一份），所以只查存在性
  · 姊妹站路径   → 必须在 lang_urls.SISTER 声明的落地地址里
  · hreflang     → 跳过。它描述的是别的语言版本，本来就指向别处
  · 简体站本来就坏的 → 跳过并单独计数。这道闸只管**翻译造成的**断链；
                      简体站 llms.txt 里 /i/、/ai/、/zouni/ 三条早就是死链，
                      混进来只会淹掉真问题。要治它们是另一件事。
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from lang_urls import SISTER, sister, is_page  # noqa: E402

SITE = "https://ourword.ai"
ALT = re.compile(r'<link rel="alternate"[^>]*>')
# 不要把 llms.txt 里那句 URL 模式说明当成链接：它写的是
# "https://ourword.ai/i/<slug>/"，正则会在 < 处截断，报出一个不存在的 /i/。
URL = re.compile(r'https://ourword\.ai(/[^\s"\'<>)]*)(?![^\s"\'<>)]*<)')
# 这些是「组织在别处的身份」，不是本页的导航，指向规范地址才对
IDENTITY = re.compile(r'"sameAs"\s*:\s*\[[^\]]*\]')


def sister_ok(path):
    for base, langs in SISTER.items():
        if path.startswith(base):
            return path in langs.values() or path == base or path.startswith(base)
    return None


def exists(path):
    """站内路径能不能落到一个真实文件上。"""
    p = path.split("?")[0].split("#")[0]
    full = os.path.join(ROOT, p.lstrip("/"))
    if os.path.isdir(full):
        return os.path.exists(os.path.join(full, "index.html"))
    return os.path.exists(full)


def layer_missing():
    """简体站里漏掉语言层的页。

    这一条守的是「被 walk 静默跳过」那一类：force_chapter_ui 的 _derived()
    第一版按子串比路径，"/two-handles" 里含 "/tw"，于是 5 个页面被当成繁体
    目录整个跳过 —— 没有语言层、没有夜间模式、没有聊天挂件，而构建全程
    一句话都不说。数量对不上也看不出来，因为没人数过。
    """
    out = []
    for dp, _dn, fn in os.walk(ROOT):
        segs = {x for x in os.path.relpath(dp, ROOT).split(os.sep)}
        if segs & {".git", "tw", "en", "node_modules", "__pycache__", "scripts",
                   "seo", "worker", "tests"}:
            continue
        for f in fn:
            if f not in ("index.html", "404.html"):
                continue
            t = open(os.path.join(dp, f), encoding="utf-8", errors="ignore").read()
            if 'http-equiv="refresh"' in t:      # 跳转桩本来就不该有
                continue
            if "<!--HWX:LANG-->" not in t:
                out.append(os.path.relpath(os.path.join(dp, f), ROOT))
    return out


def broken_in_simplified():
    """简体站自己就指不到的地址 —— 这些不算翻译的账。"""
    out = set()
    for f in ("llms.txt", "llms-full.txt", "sitemap.xml", "index.html"):
        p = os.path.join(ROOT, f)
        if not os.path.exists(p):
            continue
        for u in set(URL.findall(open(p, encoding="utf-8", errors="ignore").read())):
            if sister(u, "tw") is None and not exists(u):
                out.add(u)
    return out


def check(lang, assets):
    root = os.path.join(ROOT, lang)
    if not os.path.isdir(root):
        return ["没有 %s/" % lang], 0
    bad, n, old = [], 0, 0
    pre = broken_in_simplified()
    for dp, _dn, fn in os.walk(root):
        for f in fn:
            if not f.endswith((".html", ".xml", ".txt")):
                continue
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
            own = "/" + (rel[:-len("index.html")] if rel.endswith("index.html") else rel)
            s = open(p, encoding="utf-8", errors="ignore").read()
            s = ALT.sub("", s)              # hreflang 指向别的语言版本，跳过
            s = IDENTITY.sub("", s)         # sameAs 是组织身份，跳过
            for u in set(URL.findall(s)):
                n += 1
                sk = sister_ok(u)
                if sk is not None:
                    if not sk:
                        bad.append("%s → 姊妹站地址 %s 不在 lang_urls.SISTER 声明里" % (own, u))
                    continue
                bare = u[len("/" + lang):] if u.startswith("/" + lang + "/") else u
                if bare in pre or u in pre:
                    old += 1                    # 简体站本来就坏，不算翻译的账
                    continue
                if not assets and not is_page(u):
                    if not exists(u):
                        bad.append("%s → 资源 %s 不存在" % (own, u))
                    continue
                if not u.startswith("/" + lang + "/") and u != "/" + lang + "/":
                    bad.append("%s → %s 少了 /%s 前缀（多半是自指地址漏改）"
                               % (own, u, lang))
                elif not exists(u):
                    bad.append("%s → %s 这个页面不存在" % (own, u))
                if len(bad) >= 12:
                    return bad, n, old
    return bad, n, old


def main():
    langs = sys.argv[1:] or ["tw", "en"]
    fail = 0
    miss = layer_missing()
    print("简体站缺语言层的页：%d" % len(miss))
    for m in miss[:8]:
        print("  x %s 没有 <!--HWX:LANG-->（多半被 walk 静默跳过了）" % m)
    fail |= bool(miss)
    # 繁体站整树复制，自带 tw/assets/；英文站只产出 HTML，资源用主站那一份。
    ASSETS = {"tw": True, "en": False}
    for lang in langs:
        bad, n, old = check(lang, ASSETS.get(lang, True))
        print("%s/：校对站内绝对地址 %d 条%s"
              % (lang, n, "（另有 %d 条简体站本来就断，不算这道闸的账）" % old if old else ""))
        for b in bad:
            print("  x " + b)
        fail |= bool(bad)
    if fail:
        return 1
    print("ok — 每条地址都落到真实存在的页面上，姊妹站也指对了语言版本")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the English site into /en/.

    python3 scripts/build_en.py

Why this is not shaped like build_tw.py: the Traditional site is a *conversion*
of the built Simplified tree, so it can be produced by walking the output. The
English site shares no sentences with it — every string is written by hand — so
there is nothing to convert. What it does share is the templates, and those are
worth sharing: a second copy of the renderer would drift from the first within
a month.

So the English site is the ordinary generators pointed at English data:

    seo/chapters_en/*.py     chapters, same shape as seo/chapters/*.py
    scripts/hwx_scenes_en.py the situation layer, the front door for /en/
    scripts/quote_asks_en.py today's line
    seo/en_ui.py             the interface strings

The one trick worth naming: after the English data is rendered, **anything
still in Chinese on the page is interface, by definition** — the content is
already English. That is how seo/en_ui.py was enumerated, and it is why
scripts/check_en.py can fail the build on a single CJK character left in /en/.
No guessing at how many interface strings there are; the page says.

Three rules carried over from the Traditional build, each of which cost
something to learn there:

① URLs must not go through any text substitution. They are stashed behind
   private-use placeholders first. (Not \\x00 — that one truncates C-string
   backends and fills hrefs with body text.)
② canonical and og:url point at this page; hreflang stays identical across all
   language versions, because it describes where the *others* are.
③ Long strings are replaced before short ones. Replacing 分享 before 分享本页
   leaves "Share本页" behind.
"""
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "seo"))

OUT = os.path.join(ROOT, "en")

# URL 长这样，不能进替换
URLISH = re.compile(r"^(https?:|//|/|#|\.\.?/|mailto:|data:)")
ATTR = re.compile(r'\b(href|src|action|srcset|content|data-u|url)\s*=\s*"([^"]*)"')
# 目录白名单里**不能有 en**：ATTR 已经把 href 加过一次 /en 前缀，
# 若 en 在这张表里，JSURL 会认出 "/en/assets/…" 再加一次，变成 /en/en/。
JSURL = re.compile(r"""(fetch\(|import\(|['"])(/(?:assets|i|t|all|api)/[^'"()]*)(['"]|\))""")

# 语言标记：转换碰不到这些，它们是标记不是正文。漏了的后果是搜索引擎和
# 分享卡片把英文页按简体中文归类 —— 页面看着全对，只有翻 head 才看得见。
LOCALE = [
    ('<html lang="zh-Hans"', '<html lang="en"'),
    ('property="og:locale" content="zh_CN"', 'property="og:locale" content="en_US"'),
    ('"inLanguage":["en","zh-Hans"]', '"inLanguage":"en"'),
    ('"inLanguage":"zh-Hans"', '"inLanguage":"en"'),
    ('"inLanguage": "zh-Hans"', '"inLanguage": "en"'),
    ("<language>zh-cn</language>", "<language>en</language>"),
    ("<language>zh-CN</language>", "<language>en</language>"),
    ('"lang": "zh-CN"', '"lang": "en"'),
]

# 思源宋体简体不含合适的西文字形，英文页用 Noto Serif 的拉丁族。
FONT = [("Noto+Serif+SC", "Noto+Serif"), ("Noto Serif SC", "Noto Serif")]


def protect(s):
    keep = []

    def stash(v):
        keep.append(v)
        return "%d" % (len(keep) - 1)

    def attr(m):
        name, val = m.group(1), m.group(2)
        if URLISH.match(val) or "%" in val:
            return '%s="%s"' % (name, stash(val))
        return m.group(0)

    s = ATTR.sub(attr, s)
    s = JSURL.sub(lambda m: m.group(1) + stash(m.group(2)) + m.group(3), s)
    return s, keep


def restore(s, keep):
    return re.sub("(\\d+)", lambda m: keep[int(m.group(1))], s)


from lang_urls import fix_urls, sister, prefix  # noqa: E402

# 英文站不复制资源：CSS、JS、字体、图片一律用主站那一份，所以 assets=False。
# 加了 /en 前缀就指向不存在的 /en/assets/，线上是一页没有样式的裸 HTML，
# 而构建全程不报错。
ASSETS = False


def retarget(s, rel=None):
    """站内地址指到 /en/ 下；hreflang 那几行不动（它说的是别人在哪）。

    姊妹站、资源不加前缀、JSON-LD 三条规则见 scripts/lang_urls.py，
    那三条各自对应一次真实事故。
    """
    def one(m):
        name, val = m.group(1), m.group(2)
        # 跳转桩写的是 content="0;url=https://…"，前面带个秒数，
        # URLISH 认不出它是地址。漏掉的后果：繁体的分类跳转桩
        # tw/t/权力治理/ 把读者弹到**简体**的 /t/power/ 去。
        if name == "content" and re.match(r"^\s*\d+\s*;\s*url=", val, re.I):
            pre, u = re.split(r"(?i)url=", val, 1)
            b = u.replace("https://ourword.ai", "", 1) if u.startswith("https://") else u
            sis = sister(b, "en")
            nb = sis if sis is not None else prefix(b, "en", ASSETS)
            return '%s="%surl=%s"' % (name, pre, u.replace(b, nb, 1))
        bare = val.replace("https://ourword.ai", "", 1) if val.startswith("https://") else val
        sis = sister(bare, "en")
        if sis is not None:
            return '%s="%s"' % (name, val.replace(bare, sis, 1))
        if val.startswith("/"):
            val = prefix(val, "en", ASSETS)
        elif val.startswith("https://ourword.ai/") and "/en/" not in val:
            val = "https://ourword.ai" + prefix(bare, "en", ASSETS)
        return '%s="%s"' % (name, val)

    holes = []
    s = re.sub(r'<link rel="alternate"[^>]*>',
               lambda m: holes.append(m.group(0)) or "\ue002%d\ue003" % (len(holes) - 1), s)
    # 跳转桩的 content="0;url=…" 以数字开头，URLISH 认不出来，
    # 得单独放行进 one() —— 否则上面那段处理它的分支永远不会被调用。
    REFRESH = re.compile(r"^\s*\d+\s*;\s*url=", re.I)
    s = ATTR.sub(lambda m: one(m) if (URLISH.match(m.group(2)) or "%" in m.group(2)
                                      or REFRESH.match(m.group(2)))
                 else m.group(0), s)
    s = JSURL.sub(lambda m: m.group(1) + prefix(m.group(2), "en", ASSETS) + m.group(3), s)
    # 通用的一遍：属性之外的地址（JSON-LD、script、链接文字）也要改。
    # 这里同时把「本页指向自己」那几处改对了，所以不再单独跑 self_url。
    s = fix_urls(s, "en", ASSETS)
    s = re.sub("\ue002(\\d+)\ue003", lambda m: holes[int(m.group(1))], s)
    return s


def finish(s, rel=None):
    """一页渲染好之后统一做的四件事，顺序有意义。"""
    import en_ui
    kept, keep = protect(s)          # ① URL 先藏起来
    kept = en_ui.apply(kept)         # ② 界面串（表内已按长度降序）
    s = restore(kept, keep)
    s = retarget(s, rel)             # ③ 站内地址改指 /en/（含自指地址）
    for a, b in FONT + LOCALE:       # ④ 字体与语言标记
        s = s.replace(a, b)
    return s


def main():
    os.environ["HW_CHAPTERS"] = "chapters_en"
    os.environ["HW_SCENES"] = "hwx_scenes_en"
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)

    cwd = os.getcwd()
    os.chdir(os.path.join(ROOT, "seo"))
    try:
        import hw_chapters
        n_ch = hw_chapters.write_chapters(root=OUT)
    finally:
        os.chdir(cwd)

    # 夜间模式挂件：整块从已构建的简体页里原样搬过来，再由 finish() 统一
    # 翻标签、改资源路径。自己再写一份的话，两边的深色配色迟早对不上。
    src = os.path.join(ROOT, "i", "su-shi", "no-wind-no-rain", "index.html")
    theme = ""
    if os.path.exists(src):
        t = open(src, encoding="utf-8").read()
        a, b = "<!--HWX:THEME-->", "<!--/HWX:THEME-->"
        if a in t and b in t:
            theme = t[t.index(a):t.index(b) + len(b)]
    if theme:
        for dp, _dn, fn in os.walk(OUT):
            for f in fn:
                if f in ("index.html", "404.html"):
                    p_ = os.path.join(dp, f)
                    x = open(p_, encoding="utf-8").read()
                    if "<!--HWX:THEME-->" not in x and "</body>" in x:
                        open(p_, "w", encoding="utf-8").write(
                            x.replace("</body>", theme + "</body>", 1))

    # 三语层：和简体、繁体共用 scripts/hwx_lang.py 的同一份实现。
    # 分成两处写的话 hreflang 迟早走散，而走散了不报错，只是搜索引擎
    # 认不出这几页是同一篇。
    import hwx_lang
    hwx_lang.patch_tree("en")

    n_fix = 0
    for dp, _dn, fn in os.walk(OUT):
        for f in fn:
            if not f.endswith((".html", ".xml", ".txt", ".json")):
                continue
            p = os.path.join(dp, f)
            s = open(p, encoding="utf-8").read()
            rel = os.path.relpath(p, OUT).replace(os.sep, "/")
            rel = "/" + (rel[:-len("index.html")] if rel.endswith("index.html") else rel)
            open(p, "w", encoding="utf-8").write(finish(s, rel))
            n_fix += 1

    print("English site: %d chapter pages rendered, %d files localised" % (n_ch, n_fix))
    return 0


if __name__ == "__main__":
    sys.exit(main())

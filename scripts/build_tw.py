#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把构建好的简体站整树转成繁体，输出到 /tw/。

    python3 scripts/build_tw.py

为什么是「拿构建产物再转一遍」，而不是「从源数据再生成一份繁体站」：

  · 从源数据生成，等于把整条构建链（patch_geo_seo → apply_redesign → build_seo →
    force_chapter_ui → build_chat_index → gen_map）再跑一遍繁体版，每一步都要加
    语言分支，六个脚本各改一处，以后每改一处都要记得改两边。
  · 拿产物转，只有这一个文件知道繁体的事。结构天然一比一 —— 简体站有什么页，
    繁体站就有什么页，不可能漏，也不会多。

三条必须守住的规矩：

① **URL 一个字都不能动。** `/tw/<path>` 与 `/<path>` 必须严格对应，否则 hreflang
   配不上，站内链接也会断。所以转换前先把所有 href/src/action/url() 以及任何
   以 http、/、#、% 开头的属性值挖出来占位，转完再放回去。
   这不是多虑：t/ 下面有 41 个中文目录名（`t/权力治理` 之类的跳转桩）。

② **canonical 和 og:url 要改，hreflang 不能改。** 前者描述「这一页自己是谁」，
   后者描述「这一页的另一个语言版本在哪」—— 后者在两份拷贝里内容本来就一样。

③ **同一份文本，转换只发生一次。** 转换函数不幂等（繁体再转还是繁体，但
   FIX 表里的替换可能在已转文本上误伤），所以只对简体源转，绝不对 /tw/ 再转。
"""
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from tw_convert import convert  # noqa: E402

OUT = os.path.join(ROOT, "tw")

# 不进繁体站的：源码、工具、内部文档，以及 /tw/ 自己
# en 必须在这里：英文站是另一份内容，不是简体站的转换源。漏掉它的话
# build_tw 会把 en/ 整棵树当简体内容转一遍塞进 tw/en/ ——「繁体化」英文
# 是空操作，但地址重写会把姊妹站链接改成 /tw/en/podcast/ 这种不存在的路径。
SKIP_DIRS = {".git", ".github", "scripts", "seo", "worker", "tests", "node_modules",
             "__pycache__", "tw", "en", "site", "HumanWorld"}
# 这些根文件不复制（内部文档 / 只对主站有意义的）
# site.webmanifest 必须复制：页面里写的是相对路径 href="site.webmanifest"，
# 不复制的话繁体页会去要 /tw/site.webmanifest —— 线上实测 404。
SKIP_FILES = {"robots.txt", "CNAME"}
TEXT_EXT = {".html", ".js", ".json", ".txt", ".xml", ".css", ".svg", ".webmanifest"}
# 派生产物里体积大又不带文字的，直接复制不转
BIN_EXT = {".png", ".jpg", ".jpeg", ".ico", ".woff", ".woff2", ".ttf", ".gif", ".webp"}

# 属性值长这样就是 URL，不能转
URLISH = re.compile(r"^(https?:|//|/|#|\.\.?/|mailto:|data:)")
ATTR = re.compile(r'\b(href|src|action|srcset|content|data-u|url)\s*=\s*"([^"]*)"')
JSURL = re.compile(r"""(fetch\(|import\(|['"])(/(?:assets|i|t|all|api)/[^'"()]*)(['"]|\))""")


def protect(s):
    """把 URL 换成占位符，返回 (处理后文本, 还原表)。"""
    keep = []

    def stash(v):
        keep.append(v)
        # 占位符必须用私用区字符，**不能用 \x00**：OpenCC 底层是 C 字符串，
        # 遇到 \x00 直接截断，后面整篇都没了。这个 bug 第一版踩过 ——
        # 转出来的页面里 href="居里 — 人類世界生存法則"，URL 被正文填满。
        return "\ue000%d\ue001" % (len(keep) - 1)

    def attr(m):
        name, val = m.group(1), m.group(2)
        if URLISH.match(val) or "%" in val:
            return '%s="%s"' % (name, stash(val))
        return m.group(0)

    s = ATTR.sub(attr, s)
    s = JSURL.sub(lambda m: m.group(1) + stash(m.group(2)) + m.group(3), s)
    return s, keep


def restore(s, keep):
    return re.sub("\ue000(\\d+)\ue001", lambda m: keep[int(m.group(1))], s)


from lang_urls import fix_urls, sister, prefix  # noqa: E402


def retarget(s, rel=None):
    """站内地址指到 /tw/ 下；hreflang 那几行不动（它说的是别人在哪）。

    姊妹站、JSON-LD、自指地址三条规则见 scripts/lang_urls.py —— 那三条各自
    对应一次真实事故，写在那个文件的开头。
    """
    def one(m):
        name, val = m.group(1), m.group(2)
        # 跳转桩写的是 content="0;url=https://…"，前面带个秒数，
        # URLISH 认不出它是地址。漏掉的后果：繁体的分类跳转桩
        # tw/t/权力治理/ 把读者弹到**简体**的 /t/power/ 去。
        if name == "content" and re.match(r"^\s*\d+\s*;\s*url=", val, re.I):
            pre, u = re.split(r"(?i)url=", val, 1)
            b = u.replace("https://ourword.ai", "", 1) if u.startswith("https://") else u
            sis = sister(b, "tw")
            nb = sis if sis is not None else prefix(b, "tw")
            return '%s="%surl=%s"' % (name, pre, u.replace(b, nb, 1))
        bare = val.replace("https://ourword.ai", "", 1) if val.startswith("https://") else val
        sis = sister(bare, "tw")
        if sis is not None:
            return '%s="%s"' % (name, val.replace(bare, sis, 1))
        if val.startswith("/"):
            val = prefix(val, "tw")
        elif val.startswith("https://ourword.ai/") and "/tw/" not in val:
            val = "https://ourword.ai" + prefix(bare, "tw")
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
    s = JSURL.sub(lambda m: m.group(1) + prefix(m.group(2), "tw") + m.group(3), s)
    # 通用的一遍：属性之外的地址（JSON-LD、script、链接文字）也要改。
    # 这里同时把「本页指向自己」那几处改对了，所以不再单独跑 self_url。
    s = fix_urls(s, "tw")
    s = re.sub("\ue002(\\d+)\ue003", lambda m: holes[int(m.group(1))], s)
    return s


# 语言标记：繁体页必须自报繁体，否则搜索引擎和分享卡片都按简体归类。
# 这几处都是转换转不到的（它们是标记不是正文），只能显式替换。
LOCALE = [
    ('property="og:locale" content="zh_CN"', 'property="og:locale" content="zh_TW"'),
    ('"inLanguage":["en","zh-Hans"]', '"inLanguage":["en","zh-Hant"]'),
    ('"inLanguage":"zh-Hans"', '"inLanguage":"zh-Hant"'),
    ('"inLanguage": "zh-Hans"', '"inLanguage": "zh-Hant"'),
    ("<language>zh-cn</language>", "<language>zh-tw</language>"),
    ("<language>zh-CN</language>", "<language>zh-TW</language>"),
    ('"lang": "zh-CN"', '"lang": "zh-TW"'),
]


# 繁体读者用 AlipayHK 收款码，简体站保持大陆支付宝码。
#
# 为什么分开：大陆个人收款码在境外能不能付，取决于**付款方账户在哪**——
# 大陆支付宝账户在海外照样付得了（那仍是境内转账），绑外卡的账户则不行
# （个人码被判成转账，外卡走不通）。繁体读者多在港台，AlipayHK 直通。
#
# 两处都要换：图，和从码里解出来的深链（点「打开支付宝」走的是链接，不是图）。
# 图是从原始分享卡里裁出来的：只留码区，品牌、金额（9.99 HKD）、说明全去掉，
# 中心那张头像换成红「人」印。裁完逐步验过解码结果与原码**逐字符相同**。
ALIPAY_HK_LINK = ("https://render.alipay.com/p/yuyan/180020010001270667/landing/"
                  "income.html?qrcode=https://qr.alipay.hk/281004010499ha1j0b9kg7PhWd30nLZv4Zfa")
PAY = [
    ("/tw/assets/pay-alipay.png", "/tw/assets/pay-alipayhk.png"),
    ("https://qr.alipay.com/fkx10243q5q41avrifvyj24", ALIPAY_HK_LINK),
    # 港台读者装的是 AlipayHK，不是大陆支付宝——文案得跟着码走，
    # 不然弹窗写着「打開支付寶」而给的是 AlipayHK 码，读者会以为扫错了。
    # 这些是转换之后的繁体写法，所以匹配的是「支付寶」不是「支付宝」。
    # 顺序有意义：先换长的，再换短的。反过来会把长句里的「支付寶」先吃掉，
    # 剩下「AlipayHK收款鏈接」这种缺空格的半成品。
    ("支付寶收款鏈接", "AlipayHK 收款鏈接"),
    ("支付寶收款碼", "AlipayHK 收款碼"),
    ("打開支付寶掃相冊", "開啟 AlipayHK 掃相冊"),
    ("打開支付寶鏈接", "開啟 AlipayHK 鏈接"),
    ("打開支付寶", "開啟 AlipayHK"),
    ("在支付寶裡掃相冊", "在 AlipayHK 裡掃相冊"),
    ("去支付寶", "去 AlipayHK"),
    ("支付寶", "AlipayHK"),
]


# 繁体页换成思源宋体繁体：Noto Serif SC 也含繁体字，但字形是简体地区的写法
# （骨、直、過 这些字的笔画走向不同），繁体读者一眼看得出别扭。
FONT = [("Noto+Serif+SC", "Noto+Serif+TC"), ("Noto Serif SC", "Noto Serif TC")]


# JSON-LD 里的地址是 "url": "…"（冒号），ATTR 那套只认 name="…"（等号），
# 所以碰不到它们。后果是繁体页和英文页的 Article.url 仍然指着简体页 ——
# canonical 和 og:url 都改对了，结构化数据却和它们打架，而搜索引擎两个都读。
#
# 只替换「这一页指向自己」的那一个地址，不做通用重写：同一段 JSON-LD 里
# sameAs 列的是组织在别处的身份（/skill/ 之类），那些指向规范地址才是对的，
# 一律加前缀会把它们一起改错。
def self_url(s, rel, prefix):
    if not rel.startswith("/"):
        rel = "/" + rel
    a = "https://ourword.ai" + rel
    b = "https://ourword.ai" + prefix + rel
    # 两种形态都要换：JSON-LD 里带引号的 "…"，和页脚引用块里的纯文本。
    # 直接替裸串就够了 —— 调用点在 hreflang 还是占位符的时候执行，
    # 那几行里的同一个地址碰不到。
    return s.replace(a + '"', b + '"').replace(a + "<", b + "<").replace(a + " ", b + " ")


def do_text(src, dst):
    s = open(src, encoding="utf-8").read()
    if src.endswith(".html"):
        s = s.replace('<html lang="zh-Hans"', '<html lang="zh-Hant"')
        if 'lang="zh-Hant"' not in s:
            s = re.sub(r"<html\b", '<html lang="zh-Hant"', s, count=1)
    kept, keep = protect(s)
    kept = convert(kept)
    s = restore(kept, keep)
    rel = os.path.relpath(src, ROOT).replace(os.sep, "/")
    rel = "/" + (rel[:-len("index.html")] if rel.endswith("index.html") else rel)
    s = retarget(s, rel)
    # sitemap / feed / llms 里的地址在**元素文本和裸行**里，不是属性，
    # retarget 那套按属性走的规则碰不到它们 —— 第一版 tw/sitemap.xml 里
    # 553 条全是简体站的地址，等于把繁体站的地图指向了别人家。
    if os.path.basename(src) in ("sitemap.xml", "feed.xml", "llms.txt", "llms-full.txt"):
        def _one(m):
            b = m.group(1)
            sis = sister(b, "tw")
            return "https://ourword.ai" + (sis if sis is not None else prefix(b, "tw"))
        s = re.sub(r"https://ourword\.ai(/[^\s\"'<>)]*)", _one, s)
    for a, b in FONT:
        s = s.replace(a, b)
    for a, b in LOCALE:
        s = s.replace(a, b)
    for a, b in PAY:
        s = s.replace(a, b)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    open(dst, "w", encoding="utf-8").write(s)


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    n_t = n_b = 0
    for dp, dn, fn in os.walk(ROOT):
        rel = os.path.relpath(dp, ROOT)
        parts = set(rel.split(os.sep))
        if parts & SKIP_DIRS:
            dn[:] = []
            continue
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for f in fn:
            if f in SKIP_FILES or f.startswith("."):
                continue
            ext = os.path.splitext(f)[1].lower()
            src = os.path.join(dp, f)
            dst = os.path.join(OUT, os.path.relpath(src, ROOT))
            if ext in TEXT_EXT:
                if f.endswith(".md"):
                    continue
                do_text(src, dst)
                n_t += 1
            elif ext in BIN_EXT:
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy2(src, dst)
                n_b += 1
    print("繁体站：文本 %d 个（已转换 + 改指 /tw/），二进制 %d 个（原样复制）" % (n_t, n_b))
    return 0


if __name__ == "__main__":
    sys.exit(main())

# -*- coding: utf-8 -*-
"""语言站的地址改写规则。繁体站和英文站共用这一份。

抽出来是因为这一段今天被抄成两份，然后两份一起错了三次 —— 而且三次都是
「两版一起错，所以对比两版的检查看不见」。scripts/check_links.py 是配套的闸。

三条规则，各来自一次真实事故：

① **姊妹站不套主站的语言前缀。** 原声和品味是各自独立的站，它们的语言版本在
   自己站内：/podcast/tw/、/skill/tw/。而品味的英文版根本不是一条路径，是同一个
   URL 加 ?lang=en（它读 URLSearchParams，且不看浏览器语言 —— 不带这个参数，
   英文读者点过去看到的是中文）。原声还没有英文版，所以退回默认版本。
   没有这一条时，555 个繁体页的页脚指向 https://ourword.ai/tw/podcast/ ——
   一个不存在的地址。

② **资源和页面要分开。** 繁体站是整树复制，自带 tw/assets/；英文站只产出 HTML，
   资源用主站那一份。给资源加 /en 前缀就指向了不存在的 /en/assets/，
   线上是一页没有样式的裸 HTML，而构建全程没有任何报错。

③ **JSON-LD 里的地址也要改。** 它写成 "url": "…"（冒号），按属性走的规则
   （name="…"，等号）碰不到它。后果是繁体页的 Article.url 仍指简体页、繁体首页的
   ItemList 把一百多条都指向简体页 —— canonical 改对了，结构化数据和它打架。
   例外是 sameAs：那列的是组织在别处的身份，指向规范地址才对。
"""
import re

SITE = "https://ourword.ai"

# 同域下**不属于这个仓库**的路径 → 各语言实际存在的落地地址。
# 做出新版本了就往这里加一行；空 dict 表示只有一个版本，任何语言都指它。
#
# ourword.ai 底下每个子路径各归一个独立仓库（/ai/ 是 AI 泡沫检测仪，
# /zouni/ 是走你，/site/ 是导航页，/podcast/ 和 /skill/ 是姊妹站）。
# 它们不在这棵树里，所以：
#   · 不能套主站的语言前缀 —— /tw/ai/ 是不存在的地址
#   · 不能用"文件在不在"判断死活 —— 实测 /ai/ 200、/zouni/ 301、/site/ 200
SISTER = {
    "/podcast/": {"tw": "/podcast/tw/"},
    "/skill/": {"tw": "/skill/tw/", "en": "/skill/?lang=en"},
    "/ai/": {},
    "/zouni/": {},
    "/site/": {},
}


def sister(val, lang):
    """姊妹站地址：返回改好的地址；不是姊妹站返回 None。"""
    for base, langs in SISTER.items():
        if val == base or val.startswith(base):
            rest = val[len(base):]
            if rest.startswith(("tw/", "en/")) or "?" in rest:
                return val                      # 已经带语言了
            if lang not in langs:
                return val                      # 该语言没有版本，退回默认
            if rest:                            # 深层页面只跟目录式映射走
                tgt = langs[lang]
                return (tgt + rest) if tgt.endswith("/") and "?" not in tgt else val
            return langs[lang]
    return None


def is_page(path):
    """页面跟着语言走，文件不跟。以 / 或 .html 结尾、或没有扩展名的算页面。"""
    p = path.split("?")[0].split("#")[0]
    return p.endswith("/") or p.endswith(".html") or "." not in p.rsplit("/", 1)[-1]


def prefix(path, lang, assets=True):
    """给一条站内路径加语言前缀。已经带了、或（assets=False 时）是资源，就不加。"""
    if path.startswith("/%s/" % lang) or path == "/%s/" % lang:
        return path
    if not assets and not is_page(path):
        return path
    return "/" + lang + path


def self_url(s, rel, lang):
    """把「这一页指向自己」的那个简体地址改成本语言版本。

    只替这一个，不做通用重写 —— 同一段 JSON-LD 里 sameAs 列的是组织在别处的
    身份，一律加前缀会把它们改错。
    调用点必须在 hreflang 还是占位符的时候：那几行里也有这个裸地址，
    而它们**必须**继续指向简体页。
    """
    if not rel.startswith("/"):
        rel = "/" + rel
    a = SITE + rel
    b = SITE + "/" + lang + rel
    for tail in ('"', "<", " ", ")"):
        s = s.replace(a + tail, b + tail)
    return s


_SAMEAS = re.compile(r'"sameAs"\s*:\s*\[[^\]]*\]')
_URL = re.compile(r'https://ourword\.ai(/[^"\s\\<>)\']*)')


def fix_urls(s, lang, assets=True):
    """把整页里**剩下的**站内绝对地址改到本语言版本。

    为什么要一遍通用的，而不是只改属性：同一批地址会出现在三种按属性走的规则
    都碰不到的位置，而且三种都真的出过事 ——

      · JSON-LD 里的 "url": "…"（冒号不是等号）
      · 跳转桩里的 <script>location.replace("…")</script>
        —— 这一句会真的执行，繁体读者点分类被弹回简体页
      · 链接的显示文字：<a href="…/tw/t/power/">Moved to …/t/power/</a>
        href 对了，读者看到的地址还是错的

    两个例外：
      · sameAs —— 组织在别处的身份，指向规范地址才对，这里挖走保护
      · hreflang —— 调用点在它们还是占位符的时候，所以碰不到。
        它们**必须**继续指向别的语言版本，那正是它们的用途
    """
    holes = []
    s = _SAMEAS.sub(lambda x: holes.append(x.group(0)) or "\ue004%d\ue005" % (len(holes) - 1), s)

    def one(m):
        path = m.group(1)
        sis = sister(path, lang)
        return SITE + (sis if sis is not None else prefix(path, lang, assets))

    s = _URL.sub(one, s)
    return re.sub("\ue004(\\d+)\ue005", lambda x: holes[int(x.group(1))], s)

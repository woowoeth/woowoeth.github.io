#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""繁体站门禁：结构对得上、没有漏转、歧义字都登记过。

四条判据，各防一类真实发生过的事故：

① **结构一一对应**：简体站每一个页面，/tw/ 下都要有；反过来不能多。
   少一页就是死链，多一页就是没人维护的孤儿。

② **链接集合完全一致**：把两版页面的 href/src 取出来，繁体那份去掉 /tw 前缀后，
   必须和简体那份逐个相同。这一条是冲着一个具体 bug 来的 ——
   第一版拿 \\x00 当占位符，而 OpenCC 底层是 C 字符串、遇 \\x00 直接截断，
   于是 URL 被正文填满（href="居里 — 人類世界生存法則"）。
   页面照样渲染、构建照样通过，只有比链接才看得出来。

③ **没有漏转**：/tw/ 的正文里不该再出现只存在于简体的字（们/这/时/说…）。
   漏转通常不是整页漏，是某个模板分支漏，抽查看不见。

④ **歧义字都登记过**：一简多繁里两边都讲得通的那些字（隻/髮/麵/餘/曆…），
   每一处的三字上下文都必须在 tw_allow.txt 里。出现没登记过的就拦下来，
   人看一眼再登记 —— 写新章节时多出几条要审，这是有意的，不是噪音。
   为什么是三字不是二字：分词错误恰好会造出合法的二字词（「明白髮生」里的
   「白髮」是正经词），二字白名单放它过，抓不到。
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from tw_convert import NEVER, contexts, load_allow  # noqa: E402

TW = os.path.join(ROOT, "tw")
SKIP_DIRS = {".git", ".github", "scripts", "seo", "worker", "tests", "node_modules",
             "__pycache__", "tw", "site", "HumanWorld"}
# 只存在于简体的常用字：出现在 /tw/ 正文里 = 漏转
SIMP_ONLY = "们这时说过还没个来对开关问题实现样种应认识电话车东车马书长门问闻见东丽乐乡习买卖头条"
TAG = re.compile(r"<script.*?</script>|<style.*?</style>", re.S)
LINK = re.compile(r'\b(?:href|src)="([^"]*)"')


def pages(root, skip_tw=True):
    out = {}
    for dp, dn, fn in os.walk(root):
        rel = os.path.relpath(dp, root)
        if set(rel.split(os.sep)) & (SKIP_DIRS if skip_tw else SKIP_DIRS - {"tw"}):
            dn[:] = []
            continue
        for f in fn:
            if f in ("index.html", "404.html"):
                p = os.path.join(dp, f)
                out[os.path.relpath(p, root).replace(os.sep, "/")] = p
    return out


def text_of(s):
    return " ".join(re.findall(r">([^<>]+)<", TAG.sub("", s)))


def main():
    if not os.path.isdir(TW):
        print("✗ 没有 tw/ —— 先跑 python3 scripts/build_tw.py")
        return 1
    sc = pages(ROOT)
    tw = {k: v for k, v in pages(TW, skip_tw=False).items()}
    bad = []

    # ① 结构
    miss = sorted(set(sc) - set(tw))
    extra = sorted(set(tw) - set(sc))
    for m in miss[:8]:
        bad.append("繁体站缺页：%s" % m)
    if len(miss) > 8:
        bad.append("……另有 %d 页缺失" % (len(miss) - 8))
    for e in extra[:8]:
        bad.append("繁体站多出孤儿页：%s" % e)

    # ② 链接集合
    #    hreflang 那三行要单独比：它们在两份拷贝里**本来就一模一样**（各自指向对方），
    #    跟其他链接的归一化规则正好相反，混在一起比会互相打架。
    ALT = re.compile(r'<link rel="alternate"[^>]*>')
    n_link = 0
    for k in sorted(set(sc) & set(tw)):
        sa = open(sc[k], encoding="utf-8").read()
        sb = open(tw[k], encoding="utf-8").read()
        if ALT.findall(sa) != ALT.findall(sb):
            bad.append("hreflang 两版不一致：%s" % k)
        a = LINK.findall(ALT.sub("", sa))
        b = LINK.findall(ALT.sub("", sb))
        # 去掉 /tw 前缀再比：相对路径和绝对 URL 两种写法都要归一化。
        # canonical / og:url 本来就该指向各自的地址，归一化之后才能比出「别的链接有没有被改坏」。
        b = [re.sub(r"^/tw(/|$)", r"\1", x) for x in b]
        b = [x.replace("https://ourword.ai/tw/", "https://ourword.ai/") for x in b]
        # 字体是**有意**换的（SC → TC 字形），不算链接被改坏。
        # 这一条是闸自己抓出来的：换字体那次它报了 500 多页「链接对不上」，
        # 说明②确实在盯着 —— 所以只在这里放行这一处，不放宽整条判据。
        b = [x.replace("Noto+Serif+TC", "Noto+Serif+SC") for x in b]
        if a != b:
            d = [(x, y) for x, y in zip(a, b) if x != y][:2]
            bad.append("链接对不上：%s  %s" % (k, d or "(数量 %d vs %d)" % (len(a), len(b))))
            if len([x for x in bad if x.startswith("链接对不上")]) >= 5:
                break
        n_link += len(a)

    # ③ 漏转
    for k in sorted(set(sc) & set(tw)):
        t = text_of(open(tw[k], encoding="utf-8").read())
        hit = sorted({c for c in t if c in SIMP_ONLY})
        if hit:
            bad.append("疑似漏转：%s 出现简体字 %s" % (k, "".join(hit[:8])))
            if len([x for x in bad if x.startswith("疑似漏转")]) >= 5:
                break

    # ④ 歧义字登记
    allow = load_allow()
    unseen = {}
    for k in sorted(tw):
        t = text_of(open(tw[k], encoding="utf-8").read())
        for c in contexts(t):
            if c not in allow:
                unseen.setdefault(c, k)
    if unseen:
        bad.append("歧义字上下文没登记过 %d 处（看一眼对不对，对就加进 scripts/tw_allow.txt）：" % len(unseen))
        for c, k in sorted(unseen.items())[:30]:
            bad.append("    %s      ← %s" % (c, k))

    # ⑤ 绝不该出现的组合（分词切错的系统性筛子）
    for k in sorted(tw):
        t = text_of(open(tw[k], encoding="utf-8").read())
        for w in NEVER:
            if w in t:
                i = t.index(w)
                bad.append("切错：%s 里出现「%s」 …%s…" % (k, w, t[max(0, i - 12):i + 13]))
                break
        if len([x for x in bad if x.startswith("切错")]) >= 5:
            break

    # ⑥ 地图类文件必须指向繁体站自己
    #    sitemap/feed/llms 里的地址在元素文本和裸行里，不走属性那套重写规则。
    #    第一版漏了，tw/sitemap.xml 里 553 条全指向简体站 —— 页面全对，
    #    只有打开地图文件才看得见，所以要有一条判据专门盯它。
    for f in ("sitemap.xml", "feed.xml", "llms.txt", "llms-full.txt"):
        p_ = os.path.join(TW, f)
        if not os.path.exists(p_):
            continue
        t = open(p_, encoding="utf-8").read()
        stray = len(re.findall(r"https://ourword\.ai/(?!tw/)", t))
        if stray:
            bad.append("tw/%s 里有 %d 条地址指向简体站（应全部是 /tw/）" % (f, stray))

    print("繁体站 %d 页 · 校对链接 %d 条 · 歧义字白名单 %d 条" % (len(tw), n_link, len(allow)))
    if bad:
        print("\n不合格：")
        for b in bad:
            print("  ✗ " + b if not b.startswith("    ") else b)
        return 1
    print("✓ 结构一一对应、链接一致、无漏转、无切错组合、歧义字全部登记、地图指向自己")
    return 0


if __name__ == "__main__":
    sys.exit(main())

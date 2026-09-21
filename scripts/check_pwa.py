#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""三语 PWA 装得上、离线打得开，而且描述不会过期。

为什么要这道闸：2026-09-21 查出三件事 ——
manifest 的描述写死成「75位…7大生存主题」（实际 171 条目 403 章节，早就过期）、
英文站和繁体站的 manifest 是 **404**（三语页面都写相对路径 `href="site.webmanifest"`，
/en/ 下解析成 /en/site.webmanifest）、没有 service worker。

**写死的数字一定会过期**，所以这道闸不查「描述像不像话」，查的是
**描述里的数字等不等于现在的真实数量** —— 一旦有人手改回写死的值，当场红。
"""
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "seo"))

LANGS = [("", "zh-CN"), ("en/", "en"), ("tw/", "zh-Hant")]
SAMPLE = ["index.html", "i/postman/index.html",
          "en/index.html", "en/i/postman/index.html",
          "tw/index.html", "tw/i/postman/index.html"]


def main():
    os.environ.pop("HW_CHAPTERS", None)
    import hw_chapters as C
    people, chapters = len(C.PARENTS), len(C.CHAPTERS)
    bad = []

    for prefix, lang in LANGS:
        p = os.path.join(ROOT, prefix, "site.webmanifest")
        if not os.path.isfile(p):
            bad.append("没有 /%ssite.webmanifest —— 这一语言装不上" % prefix)
            continue
        try:
            m = json.loads(io.open(p, encoding="utf-8").read())
        except ValueError as e:
            bad.append("/%ssite.webmanifest 不是合法 JSON：%s" % (prefix, e))
            continue
        nums = [int(x) for x in re.findall(r"\d+", m.get("description", ""))]
        if sorted(nums) != sorted([people, chapters]):
            bad.append("/%ssite.webmanifest 的描述里是 %s，实际是 %d 个条目 %d 篇章节 —— "
                       "数字写死了就会过期，描述要从内容现算（scripts/gen_pwa.py）"
                       % (prefix, nums or "没有数字", people, chapters))
        if m.get("scope") != "/" + prefix or m.get("start_url") != "/" + prefix:
            bad.append("/%ssite.webmanifest 的 scope/start_url 不是 /%s" % (prefix, prefix))
        if m.get("lang") != lang:
            bad.append("/%ssite.webmanifest 的 lang 是 %r，应为 %r" % (prefix, m.get("lang"), lang))
        for ic in m.get("icons", []):
            src = ic.get("src", "")
            if not src.startswith("/"):
                bad.append("/%ssite.webmanifest 的图标 %r 是相对路径 —— /en/ 下会 404" % (prefix, src))
            elif not os.path.isfile(os.path.join(ROOT, src.lstrip("/"))):
                bad.append("/%ssite.webmanifest 的图标 %s 文件不存在" % (prefix, src))

    for f in ("sw.js", "offline.html"):
        if not os.path.isfile(os.path.join(ROOT, f)):
            bad.append("没有 /%s —— 没有它就没有离线，装到主屏只是个书签" % f)

    for rel in SAMPLE:
        p = os.path.join(ROOT, rel)
        if not os.path.isfile(p):
            continue
        t = io.open(p, encoding="utf-8", errors="ignore").read()
        pre = "en/" if rel.startswith("en/") else ("tw/" if rel.startswith("tw/") else "")
        want = '/%ssite.webmanifest' % pre
        m = re.search(r'<link rel="manifest" href="([^"]+)"', t)
        if not m:
            bad.append("/%s 没有 manifest 链接" % rel)
        elif m.group(1) != want:
            bad.append("/%s 的 manifest 指向 %s，应为 %s（相对路径在子语言下会 404）"
                       % (rel, m.group(1), want))
        if "serviceWorker" not in t:
            bad.append("/%s 没有注册 service worker —— 这一页离线打不开" % rel)

    if bad:
        print("\n  PWA 有问题 %d 处：" % len(bad))
        for b in bad[:10]:
            print("    ✗ " + b)
        return 1
    print("  三语都能装（描述 %d 条目 / %d 章节，现算）· sw.js + offline.html 在 · 抽查 %d 页都挂上了"
          % (people, chapters, len(SAMPLE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

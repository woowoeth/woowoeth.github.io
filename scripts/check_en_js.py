#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英文站的内联脚本必须能解析。

    python3 scripts/check_en_js.py

为什么单独一道：英文站是拿中文页做字符串替换生成的，而替换是**盲的** ——
它不知道自己落在 HTML 文本里还是 JS 单引号字符串里。一个带撇号的英文译文
落进单引号字符串，就会把字符串截断：

    '看完你会换个打法 →'  →  'You'll play it differently after →'
                                  ^ 到这里字符串就结束了

后果是整个 <script> 块语法错误，首页的今日一问、每日金句、处境网格、搜索
全部不渲染 —— 页面打开是空的，而所有既有的闸门（结构、链接、无中文残留）
一条都不会响：它们查的是文本，不是能不能跑。

所以这道闸只问一件事：每个内联脚本，node 能不能解析。
"""
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "en")

SCRIPT = re.compile(r'<script([^>]*)>(.*?)</script>', re.S)


def check(path):
    src = open(path, encoding="utf-8", errors="ignore").read()
    bad = []
    for i, m in enumerate(SCRIPT.finditer(src)):
        attrs, body = m.group(1), m.group(2)
        if "src=" in attrs or "json" in attrs:      # 外链和 ld+json 不是脚本
            continue
        if not body.strip():
            continue
        with tempfile.NamedTemporaryFile("w", suffix=".mjs", delete=False,
                                         encoding="utf-8") as f:
            f.write(body)
            tmp = f.name
        r = subprocess.run(["node", "--check", tmp], capture_output=True, text=True)
        os.unlink(tmp)
        if r.returncode:
            line = next((x.strip() for x in r.stderr.split("\n")
                         if "SyntaxError" in x), "语法错误")
            ctx = next((x.strip()[:90] for x in r.stderr.split("\n")[1:4]
                        if x.strip() and "^" not in x), "")
            bad.append("%s 第 %d 个内联脚本：%s\n      %s"
                       % (os.path.relpath(path, ROOT), i + 1, line, ctx))
    return bad


def main():
    if subprocess.run(["node", "--version"], capture_output=True).returncode:
        print("没有 node，跳过（CI 上有）")
        return 0
    if not os.path.isdir(OUT):
        print("✗ 没有 en/ —— 先跑 python3 scripts/build_en.py")
        return 1
    bad, n = [], 0
    for dp, _dn, fn in os.walk(OUT):
        for f in fn:
            if f.endswith(".html"):
                n += 1
                bad += check(os.path.join(dp, f))
    print("英文站 %d 页 · 内联脚本语法检查" % n)
    if bad:
        print("\n不合格：")
        for b in bad[:8]:
            print("  ✗ " + b)
        return 1
    print("✓ 每一个内联脚本都能解析")
    return 0


if __name__ == "__main__":
    sys.exit(main())

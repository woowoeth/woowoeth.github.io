#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把页面里所有 /assets/... 的 ?v= 换成**该文件当前内容的哈希**。

    python3 scripts/stamp_assets.py

为什么需要这一步：站里的样式表和脚本是带版本号引用的
（`/assets/hw-entry.css?v=15`），而那个数字是**手写的**。改了文件忘了改
数字，URL 就没变 —— 服务器上是新文件，回头客的浏览器和中间的 CDN 却一直
发缓存里那份旧的。

它的表现最难查：**新访客一切正常，只有老用户坏**，而且你自己的开发机通常
是新访客（无痕、清过缓存、换了端口）。用户拿手机截图给你看一个你在本地
怎么也复现不了的样子。这条已经咬过两次（hw-en.css?v=1 一次、
hw-entry.css?v=15 一次），两次都是同一个形状：**判据是「我改了没有」，
而正确的判据是「URL 变了没有」。**

所以不再手写。逐个文件算一次 md5，取前 8 位当版本号：内容变了 URL 必变，
内容没变 URL 不变（不会让缓存白白失效）。手写的数字这里一律被覆盖，
生成器里写什么都不影响结果。

scripts/check_assets.py 是配套的闸：页面里但凡还有一个对不上文件内容的
版本号就拦。
"""
import hashlib
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REF = re.compile(r'(/assets/([A-Za-z0-9._-]+\.(?:css|js)))(\?v=[A-Za-z0-9.]*)?')
SKIP = {".git", "node_modules", "__pycache__"}


def digest(name, _c={}):
    if name not in _c:
        p = os.path.join(ROOT, "assets", name)
        if not os.path.exists(p):
            _c[name] = None
        else:
            _c[name] = hashlib.md5(
                io.open(p, "rb").read()).hexdigest()[:8]
    return _c[name]


def stamp(text):
    def go(m):
        d = digest(m.group(2))
        if not d:
            return m.group(0)          # 仓库里没有这个文件，别乱改
        return "%s?v=%s" % (m.group(1), d)
    return REF.sub(go, text)


def main():
    n_file = n_ref = 0
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in SKIP and not d.startswith(".")]
        for f in fn:
            if not f.endswith((".html", ".xml")):
                continue
            p = os.path.join(dp, f)
            s = io.open(p, encoding="utf-8", errors="ignore").read()
            hits = REF.findall(s)
            if not hits:
                continue
            new = stamp(s)
            if new != s:
                io.open(p, "w", encoding="utf-8").write(new)
                n_file += 1
            n_ref += len(hits)
    print("资源版本号：按内容哈希盖章 %d 处引用，改写 %d 个文件" % (n_ref, n_file))
    return 0


if __name__ == "__main__":
    sys.exit(main())

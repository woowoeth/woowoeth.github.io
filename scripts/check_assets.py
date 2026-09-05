#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""页面里每一个 /assets/ 的版本号，都必须等于那个文件当前内容的哈希。

    python3 scripts/check_assets.py

拦的是这一类事故：改了样式表或脚本，忘了改引用里那个手写的版本号。
服务器上是新文件，回头客的浏览器和 CDN 却一直发缓存里那份旧的 ——
**新访客一切正常，只有老用户坏**，而开发机通常是新访客，所以你自己怎么试
都对，只有用户拿手机截图给你看。

判据落在「URL 和文件内容对不对得上」，不是「我改了没有」。
生成器由 scripts/stamp_assets.py 统一盖章，这里只负责验收。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from stamp_assets import REF, SKIP, digest  # noqa: E402


def main():
    bad, n_ref, n_page = [], 0, 0
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in SKIP and not d.startswith(".")]
        for f in fn:
            if not f.endswith((".html", ".xml")):
                continue
            p = os.path.join(dp, f)
            s = open(p, encoding="utf-8", errors="ignore").read()
            hit = False
            for m in REF.finditer(s):
                name, ver = m.group(2), (m.group(3) or "")
                d = digest(name)
                if d is None:
                    bad.append("%s 引用了不存在的 assets/%s"
                               % (os.path.relpath(p, ROOT), name))
                    continue
                n_ref += 1
                hit = True
                if ver != "?v=%s" % d:
                    bad.append("%s 上 %s 的版本号是 %r，内容哈希是 %r —— "
                               "老用户会一直拿到缓存里那份旧的"
                               % (os.path.relpath(p, ROOT), name,
                                  ver or "(没有)", "?v=" + d))
            if hit:
                n_page += 1
    print("资源版本号：%d 页 · %d 处引用" % (n_page, n_ref))
    if bad:
        print("\n不合格：")
        for b in bad[:12]:
            print("  ✗ " + b)
        if len(bad) > 12:
            print("  … 还有 %d 处" % (len(bad) - 12))
        return 1
    print("✓ 每个版本号都等于文件当前内容的哈希")
    return 0


if __name__ == "__main__":
    sys.exit(main())

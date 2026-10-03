# -*- coding: utf-8 -*-
"""闸门「跳过」的统一出口：本地缺环境可以跳过、说一句；CI 上不许。

本地没装 playwright、断了网，闸门照样得跑完 —— 所以各道闸都留了「跳过」那条路。
可 CI 是专门装齐了环境来跑闸的地方（seo.yml 设 HW_GATE_STRICT=1）：在那里还跳过，
就是 CI 自己配坏了，而跳过的样子是绿的。

2026-10-02 撞见的：CI 从来没装过 playwright，窄屏和英文站的四项渲染检查在 CI 上一直
「（没装 playwright，跳过）」；MCP 那半边的联网探测用 Python 默认 UA，被 Cloudflare 403
（error 1010），于是自称「断网」跳过 —— 同一次运行里别的闸明明连得上网。check_en.py
的注释还写着「CI 上一定跑」。是门禁自检报「这条分支是死的」才露出来（FAILURES #49）。
"""
import os
import sys

# --strict 给门禁自检用：它跑闸时带不了环境变量，靠这个开关验「CI 上跳过即红」这条分支活着。
STRICT = os.environ.get("HW_GATE_STRICT") == "1" or "--strict" in sys.argv


def skip(msg):
    """本地：照原样打印这句跳过说明，返回。CI：打印原因并以 1 退出。"""
    if STRICT:
        print("✗ CI 上不许跳过（HW_GATE_STRICT=1）：%s" % msg.strip())
        sys.exit(1)
    print(msg)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 assets/hw-chat.js 里的简体文案表转成繁体表，写回同一个文件。

    python3 scripts/gen_chat_tw.py

为什么需要这一步：这个挂件是 /assets/ 下的**共用静态资源**，三个语言站
同一个 URL。build_tw.py 只转 tw/ 目录下的文件，转不到它 —— 于是繁体页上
的聊天挂件是简体的：「问」「说说看……」「发送」「今天还能问 5 次」。

（这一条是把文案从页面内联挪进 JS 表时引入的回归。内联的时候，繁体转换
顺带就把它们转了；挪出去之后转换够不着。）

**繁体表由简体表生成，不手写。** 手写的话改一处简体就得记得改另一处，
而记不住的事情迟早会漏。用的是站里同一个转换器（tw_convert），所以挂件
上的字和页面正文的字形完全一致。

scripts/check_chat_tw.py 是配套的闸：它重新生成一次，和文件里的对不上就拦。
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from tw_convert import convert  # noqa: E402

JS = os.path.join(ROOT, "assets", "hw-chat.js")
BEGIN = "  var T = ({\n"
END = "  })[LANG];\n"


def zh_block(src):
    """取出简体那一份表的正文（不含大括号）。"""
    m = re.search(r"\n    zh: \{\n(.*?)\n    \},\n", src, re.S)
    if not m:
        raise SystemExit("hw-chat.js 里找不到 zh 表 —— 结构变了，这个脚本要跟着改")
    return m.group(1)


def main():
    src = io.open(JS, encoding="utf-8").read()
    if BEGIN not in src:
        raise SystemExit("hw-chat.js 还是老结构（T = LANG === 'en' ? … : …），"
                         "先按三语表改造，见本文件顶部说明")
    zh = zh_block(src)
    # 文件里的中文是 \uXXXX 转义写的（保持 ASCII 源文件），所以要先解码、
    # 再转换、再编码回去。直接拿 [一-鿿] 去匹配是找不到东西的 ——
    # 第一版就是这么静默地什么都没转，生成器还报「成功」。
    def dec(t):
        return re.sub(r"\\u([0-9a-fA-F]{4})",
                      lambda m: chr(int(m.group(1), 16)), t)

    def enc(t):
        return "".join(c if ord(c) < 128 else "\\u%04x" % ord(c) for c in t)

    def one(m):
        q, body = m.group(1), m.group(2)
        plain = dec(body)
        if not re.search(r"[一-鿿]", plain):
            return m.group(0)
        return q + enc(convert(plain)) + q

    tw = re.sub(r"(['\"])((?:[^'\"\\\n]|\\.)*)\1", one, zh)
    # 替换串必须走 lambda：文案里有 \u2026 这类转义，直接当模板会被
    # re.sub 解释成反向引用并报 bad escape。
    rep = "\n    tw: {\n" + tw + "\n    },\n"
    # 判据是「正则有没有命中」，不是「文本有没有变」。拿 new == src 当
    # 落点判据，第二次跑（已经是最新的）就会报「找不到落点」——
    # 一个正确的、幂等的运行被当成结构损坏。
    new, k = re.subn(r"\n    tw: \{\n.*?\n    \},\n",
                     lambda _m: rep, src, count=1, flags=re.S)
    if k != 1:
        raise SystemExit("hw-chat.js 里找不到 tw 表的落点")
    io.open(JS, "w", encoding="utf-8").write(new)
    # 量的必须是解码后的字形差异。第一版拿 [一-鿿] 去数 tw（里面全是
    # \uXXXX 转义），永远数出 0 —— 一个永远报 0 的计数器等于没有计数器。
    a, b = dec(zh), dec(tw)
    n = sum(1 for x, y in zip(a, b) if x != y)
    if n == 0:
        raise SystemExit("生成出来的繁体表和简体表一模一样 —— 转换没生效")
    print("聊天挂件繁体表：由简体表生成，%d 处字形不同" % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())

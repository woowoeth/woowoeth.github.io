#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""聊天挂件繁体表门禁：重新生成一次，和文件里的对不上就拦。

    python3 scripts/check_chat_tw.py

防的是「简体改了，繁体忘了跟」。assets/hw-chat.js 是三个语言站共用的
静态资源，build_tw.py 只转 tw/ 目录下的文件，转不到它 —— 文案从页面内联
挪进这个 JS 表的时候，繁体页上的挂件就整块变回了简体：「问」「说说看……」
「发送」「今天还能问 5 次」。内联的年代繁体转换顺带就转了，挪出去之后
转换够不着，而所有闸门照旧报绿。

判据是「重新生成的结果 == 文件里的结果」，也就是繁体表必须是当前简体表
的机器产物。手写一遍也能通过一次，但下次改简体就对不上了 —— 这正是要拦的。
"""
import io
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
JS = os.path.join(ROOT, "assets", "hw-chat.js")


def main():
    before = io.open(JS, encoding="utf-8").read()
    r = subprocess.run([sys.executable, os.path.join(HERE, "gen_chat_tw.py")],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print("✗ 生成器跑不起来：\n" + (r.stdout + r.stderr).strip()[:400])
        return 1
    after = io.open(JS, encoding="utf-8").read()
    if before != after:
        # 已经写回去了，所以现在文件是对的；报出来让人知道刚才是不对的。
        print("✗ 聊天挂件的繁体表和简体表不同步（已就地重新生成一遍）。\n"
              "  多半是改了简体文案没跑 scripts/gen_chat_tw.py。\n"
              "  确认一下 git diff assets/hw-chat.js，然后一起提交。")
        return 1
    print("✓ 聊天挂件繁体表与简体表同步（%d 字节）" % len(after))
    return 0


if __name__ == "__main__":
    sys.exit(main())

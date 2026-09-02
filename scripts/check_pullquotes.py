# -*- coding: utf-8 -*-
"""金句不许在同一页出现两遍。

原来站上是「摘一句放进 blockquote.say」：条目页插在那一节之前当引言，
章节页贴在那一段之后。两种摆法都逃不过同一件事——那句话是紧邻正文的
逐字截取，读者在同一屏内读两遍。全站 1273 处，无一例外。

而这道门禁当时报 0，两个原因叠在一起：
  一是判据写成 `q in ps`（ps 是段落字符串的列表），问的是「金句是否
    **等于**某个完整段落」，而真实情况是「金句是那个段落的**一部分**」；
  二是脚本末尾根本没有 sys.exit，无论抓到多少都返回 0，等于一直空转。

现在改成就地加重（<b class="key">），金句回到它本来在的那一句上。
这道门禁也跟着换成检查新的不变量：
  1) 加重的那段文字，在本页的可见正文里只能出现一次；
  2) 不允许再出现 blockquote.say（那是旧的复读式排版）。
"""
import os, re, sys

STRIP = "「」“”‘’。，、！？；：—…《》 .,!?;:\"'\n\t"
bare = lambda t: "".join(c for c in re.sub(r"<[^>]+>", "", t) if c not in STRIP)


def check(root="."):
    dup, says, total, pages = [], [], 0, 0
    for base in ("i",):
        for dp, dn, fn in os.walk(os.path.join(root, base)):
            if "index.html" not in fn:
                continue
            path = os.path.join(dp, "index.html")
            s = open(path, encoding="utf-8").read()
            if 'http-equiv="refresh"' in s or "<article>" not in s:
                continue
            pages += 1
            body = s[s.index("<article>"):s.index("</article>")]
            if '<blockquote class="say">' in body:
                says.append(path)
            keys = [bare(m.group(1)) for m in
                    re.finditer(r'<b class="key">(.*?)</b>', body, re.S)]
            total += len(keys)
            flat = bare(body)
            for k in keys:
                if len(k) < 12:
                    continue
                # 加重的那段自己算一次；出现两次说明正文别处又抄了一遍
                if flat.count(k) > 1:
                    dup.append((path, k))
    return dup, says, total, pages


dup, says, total, pages = check(sys.argv[1] if len(sys.argv) > 1 else ".")
print("扫了 %d 页，就地加重 %d 处；同页重复：%d 处；旧式 blockquote.say 残留：%d 页"
      % (pages, total, len(dup), len(says)))
for p, q in dup[:10]:
    print("   重复  %-44s %s" % (p, q[:40] + ("…" if len(q) > 40 else "")))
for p in says[:5]:
    print("   残留  %s" % p)
sys.exit(1 if (dup or says) else 0)

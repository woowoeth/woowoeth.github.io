#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""门禁自检：给每一条失败分支注入一个它本该抓到的缺陷，看它拦不拦得下。

只验「好稿能过」等于没验 —— 这是站主定的规矩，这个文件是它的执行体。

三条比「跑一遍看红不红」更严的判据：

① **核对报出来的理由，不只看退出码。**
   只看退出码会被「注入碰巧触发了另一条分支」骗过去 —— 那种情况下目标分支
   依然是死的，自检却显示绿。视频侧我就栽过：注入 `art="artFocus"` 用的是
   全文件第一处替换，而 artFocus 在 p21 就出现过，注入落到了 p21 上、
   目标行根本没动，自检于是误报「这条规则是死的」。锚点必须打准，
   打准与否靠「理由对不对」来验。

② **注入前就不绿 ≠ 这道闸不合格。**
   分开报成「工作区本来就是脏的」，否则会把人引向错误的修复方向。

③ **假设自己随时会被 kill。**
   `finally` 挡不住 SIGKILL，也挡不住 Ctrl-C。所以备份走**固定目录 + 清单**，
   清单先落盘再注入，下次启动先把上次没还原的补上。
   目录名掺仓根哈希 —— 否则同一台机器上跑两个副本（克隆、worktree）会按
   basename 抢同一份备份，"还原"能把另一个仓的内容写进来。这不是假想：
   视频侧就是这么从一个临时 worktree 里把主仓的文件还原了一次。

自检自己没法进自己的用例表（谁来验自检），所以它必须有 preflight 自验：
启动时模拟一次「跑到一半被 kill」，确认残留真的会被还原。见 preflight()。
"""
import hashlib
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

CHAP = os.path.join(ROOT, "seo", "chapters", "curie.py")
SCENES = os.path.join(ROOT, "scripts", "hwx_scenes.py")

# 备份目录掺仓根哈希：同机多副本不再抢同一份备份
_tag = hashlib.md5(ROOT.encode("utf-8")).hexdigest()[:8]
BAK = os.path.join(tempfile.gettempdir(), "ourword_gate_pending_" + _tag)
MANIFEST = os.path.join(BAK, "MANIFEST")


def read(p):
    return io.open(p, encoding="utf-8").read()


def write(p, s):
    io.open(p, "w", encoding="utf-8").write(s)


def recover_pending(quiet=False):
    """把上次没跑完留下的注入还原掉。抽成函数是为了能自动反向验它 —— 见 preflight()。"""
    if not os.path.isfile(MANIFEST):
        return []
    stale = [l for l in read(MANIFEST).split("\n") if l.strip()]
    done = []
    for path in stale:
        b = os.path.join(BAK, os.path.basename(path))
        if os.path.exists(b):
            shutil.copy2(b, path)
            done.append(path)
    os.remove(MANIFEST)
    if done and not quiet:
        print("!! 上一次自检没跑完，%d 个文件还留着注入的缺陷，已还原：" % len(done))
        for p in done:
            print("     ←", os.path.relpath(p, ROOT))
    return done


def arm(path):
    """先备份、先写清单，再回来注入 —— 顺序不能反，反了就挡不住 kill。"""
    os.makedirs(BAK, exist_ok=True)
    shutil.copy2(path, os.path.join(BAK, os.path.basename(path)))
    write(MANIFEST, path + "\n")


def disarm(path):
    b = os.path.join(BAK, os.path.basename(path))
    if os.path.exists(b):
        shutil.copy2(b, path)
    if os.path.exists(MANIFEST):
        os.remove(MANIFEST)


def preflight():
    """反向验「崩溃恢复」本身：假装被 kill，看残留会不会被还原。

    自检没法把自己写进用例表，这是它唯一的替代品。做不到就别声称自己可靠。
    """
    os.makedirs(BAK, exist_ok=True)
    # 探针必须落在 BAK **之外** —— 放里面的话「原件」和「备份」是同一个路径，
    # copy2 直接 SameFileError。第一版就是这么写的，preflight 自己先崩了。
    d = tempfile.mkdtemp(prefix="ourword_probe_")
    probe = os.path.join(d, "probe.txt")
    write(probe, "clean\n")
    shutil.copy2(probe, os.path.join(BAK, os.path.basename(probe)))
    write(MANIFEST, probe + "\n")
    write(probe, "INJECTED\n")                      # 模拟：注入了，然后进程没了
    recover_pending(quiet=True)
    ok = read(probe).strip() == "clean"
    shutil.rmtree(d, ignore_errors=True)
    b = os.path.join(BAK, os.path.basename(probe))
    if os.path.exists(b):
        os.remove(b)
    return ok


# ---------- 注入函数：一条分支一个 ----------
# 锚点一律**从文件当前内容里取**，不写死字面量。写死过一次就再也不写死了：
# 稿子一改锚点就失效，而「用例失效」比「门禁失效」更难发现 —— 它看起来像门禁坏了。

def _first(pat, s):
    m = re.search(pat, s, re.S)
    return m


def _sub_field(field, fn):
    """把 CHAP 里第一处 "<field>": "..." 的值交给 fn 改写。"""
    def go():
        s = read(CHAP)
        m = _first(r'"%s":\s*"((?:[^"\\]|\\.)*)"' % field, s)
        if not m:
            return False
        new = fn(m.group(1))
        write(CHAP, s[:m.start(1)] + new + s[m.end(1):])
        return True
    return go


def _short(n):
    return lambda v: "短" * n


def _mark(v):
    return "==" + v[:6] + "==" + v[6:]


def _drop_list_item(field):
    """从第一处 "<field>": [ ... ] 里删掉最后一项。"""
    def go():
        s = read(CHAP)
        m = _first(r'"%s":\s*\[' % field, s)
        if not m:
            return False
        i, depth = m.end() - 1, 0
        for j in range(m.end() - 1, len(s)):
            if s[j] == "[":
                depth += 1
            elif s[j] == "]":
                depth -= 1
                if depth == 0:
                    i = j
                    break
        body = s[m.end():i]
        # 按顶层逗号切，去掉最后一个非空项
        items, d, cur = [], 0, ""
        for ch in body:
            if ch in "[{(":
                d += 1
            elif ch in "]})":
                d -= 1
            if ch == "," and d == 0:
                items.append(cur)
                cur = ""
            else:
                cur += ch
        if cur.strip():
            items.append(cur)
        items = [x for x in items if x.strip()]
        if len(items) < 2:
            return False
        write(CHAP, s[:m.end()] + ",".join(items[:-1]) + "," + s[i:])
        return True
    return go


def _mark_in_list(field):
    """给第一处 "<field>": [...] 的第一项加红字。"""
    def go():
        s = read(CHAP)
        m = _first(r'"%s":\s*\[\s*\n?\s*"((?:[^"\\]|\\.)*)"' % field, s)
        if not m:
            return False
        write(CHAP, s[:m.start(1)] + _mark(m.group(1)) + s[m.end(1):])
        return True
    return go


def _mark_in_f():
    """给第一个分则的 d 加红字。"""
    def go():
        s = read(CHAP)
        m = _first(r'"d":\s*"((?:[^"\\]|\\.)*)"', s)
        if not m:
            return False
        write(CHAP, s[:m.start(1)] + _mark(m.group(1)) + s[m.end(1):])
        return True
    return go


def _short_d():
    def go():
        s = read(CHAP)
        m = _first(r'"d":\s*"((?:[^"\\]|\\.)*)"', s)
        if not m:
            return False
        write(CHAP, s[:m.start(1)] + "太短" + s[m.end(1):])
        return True
    return go


def _break_apply():
    def go():
        s = read(CHAP)
        m = _first(r'"apply":\s*"((?:[^"\\]|\\.)*)"', s)
        if not m:
            return False
        write(CHAP, s[:m.start(1)] + m.group(1).replace("\\n", "", 1) + s[m.end(1):])
        return True
    return go


def _rename_key():
    """把某一章的 k 改掉 —— 目录里就找不到它了。"""
    def go():
        s = read(CHAP)
        m = _first(r'\n\s*\{\s*\n?\s*"k":\s*"([\w-]+)"', s)
        if not m:
            return False
        write(CHAP, s[:m.start(1)] + "zzz-not-in-catalog" + s[m.end(1):])
        return True
    return go


def _orphan_catalog_item():
    """往目录里加一条 ready 的条目，但不给它写章节。"""
    def go():
        s = read(CHAP)
        m = _first(r'("items":\s*\[)', s)
        if not m:
            return False
        add = ('\n        {"k": "zzz-orphan", "n": "孤儿条目", "w": "只在目录里",\n'
               '         "line": "没有对应的章节", "ready": True},')
        write(CHAP, s[:m.end(1)] + add + s[m.end(1):])
        return True
    return go


def _blank_src():
    def go():
        s = read(CHAP)
        m = _first(r'"src":\s*"((?:[^"\\]|\\.)*)"', s)
        if not m:
            return False
        write(CHAP, s[:m.start(1)] + s[m.end(1):])
        return True
    return go


def _dup_sentence():
    """把本章一句长句复制到同文件另一章的金句里 —— 制造跨章重复。"""
    def go():
        s = read(CHAP)
        qs = re.findall(r'"q":\s*\[\s*\n?\s*"((?:[^"\\]|\\.)*)"', s)
        if len(qs) < 2:
            return False
        src_q, dst_q = qs[0], qs[1]
        i = s.rfind('"%s"' % dst_q)
        if i < 0:
            return False
        write(CHAP, s[:i] + '"%s"' % src_q + s[i + len('"%s"' % dst_q):])
        return True
    return go


# ---------- 问题内容那道闸 ----------

def _q_sub(new):
    """把 hwx_scenes 里第一个问题换成 new。"""
    def go():
        # hwx_scenes 的问题是元组的第一个元素：("问题文本",\n     [(parent, k), ...])
        # 不是 "q": 键 —— 第一版按键名找，五条用例全报「挑不到注入点」。
        s = read(SCENES)
        m = _first(r'\(\s*"([^"\n]{6,40})",\s*\n\s*\[\(', s)
        if not m:
            return False
        write(SCENES, s[:m.start(1)] + new + s[m.end(1):])
        return True
    return go


# ---------- 构建产物那几道闸：注入到已生成的 HTML ----------
# 这几道闸读的是 i/ 下的成品页，不是源码，所以注入点也在成品页上。
# 页面**动态挑**，不写死路径：改一次稿路径就变，而「用例失效」比「门禁失效」更难发现。

MARK = "zzz门禁自检注入的标记串zzz"          # ≥12 字，几道闸的下限都够


def _pick_page(must_have="<article>"):
    for dp, _dn, fn in os.walk(os.path.join(ROOT, "i")):
        if "index.html" not in fn:
            continue
        path = os.path.join(dp, "index.html")
        t = read(path)
        if 'http-equiv="refresh"' in t or "<article>" not in t:
            continue
        if must_have in t:
            return path
    return None


PAGE = _pick_page() or ""
PAGE_Q = _pick_page('<section class="quotes"') or ""
def _pick_chapter_og():
    """必须挑**章节级**的 og.png（i/<条目>/<章节>/og.png）。

    踩过：直接拿 _pick_page() 的目录去取 og.png，挑中的是**条目页**，
    而 check_integrity 第 3 条只查章节那一层 —— 删了条目页的图它当然不报，
    自检于是误判「这条分支是死的」。又是一次用例打偏，不是门禁坏。
    """
    base = os.path.join(ROOT, "i")
    for parent in sorted(os.listdir(base)):
        pd = os.path.join(base, parent)
        if not os.path.isdir(pd):
            continue
        for k in sorted(os.listdir(pd)):
            f = os.path.join(pd, k, "og.png")
            if os.path.isfile(f):
                return f
    return ""


OGPNG = _pick_chapter_og()


def _html_ins(page, html, times=1):
    """在 <article> 之后插入一段 HTML。"""
    def go():
        if not page:
            return False
        t = read(page)
        i = t.index("<article>") + len("<article>")
        write(page, t[:i] + html * times + t[i:])
        return True
    return go


def _quote_overlap():
    """把同一段文字同时塞进正文和文末金句块 —— 制造重叠。"""
    def go():
        if not PAGE_Q:
            return False
        t = read(PAGE_Q)
        i = t.index("<article>") + len("<article>")
        t = t[:i] + "<p>%s</p>" % MARK + t[i:]
        j = t.index('<section class="quotes"')
        k = t.index("<blockquote><p>", j) + len("<blockquote><p>")
        write(PAGE_Q, t[:k] + MARK + t[k:])
        return True
    return go


def _drop_og():
    """删掉一张分享图 —— disarm 会把它拷回来。"""
    def go():
        if not OGPNG or not os.path.exists(OGPNG):
            return False
        os.remove(OGPNG)
        return True
    return go


def _bad_ref():
    """把 hwx_scenes 里第一个 (parent, k) 引用的 k 改成不存在的。"""
    def go():
        t = read(SCENES)
        m = _first(r'\[\(\s*"([\w-]+)",\s*"([\w-]+)"\)', t)
        if not m:
            return False
        write(SCENES, t[:m.start(2)] + "zzz-no-such-chapter" + t[m.end(2):])
        return True
    return go


# ---------- 教训台账那道闸：注入到 FAILURES.md ----------
LEDGER = os.path.join(ROOT, "FAILURES.md")


def _led(fn):
    def go():
        if not os.path.exists(LEDGER):
            return False
        t = read(LEDGER)
        out = fn(t)
        if out is None or out == t:
            return False
        write(LEDGER, out)
        return True
    return go


def _drop_gate_line(t):
    m = re.search(r"^\*\*闸：\*\*.+$", t, re.M)
    return t[:m.start()] + t[m.end():] if m else None


def _strip_reason(t):
    m = re.search(r"^(\*\*闸：\*\*\s*无)\s*——.+$", t, re.M)
    return t[:m.start()] + m.group(1) + t[m.end():] if m else None


def _no_script(t):
    m = re.search(r"^\*\*闸：\*\*\s*`[\w./-]+\.py`.*$", t, re.M)
    return t[:m.start()] + "**闸：** 有的，回头补" + t[m.end():] if m else None


def _ghost_script(t):
    m = re.search(r"^\*\*闸：\*\*\s*`([\w./-]+\.py)`", t, re.M)
    return t[:m.start(1)] + "scripts/zzz_not_here.py" + t[m.end(1):] if m else None


def _unhooked(t):
    """点名一个真实存在、但没挂在 gate.py CHECKS 上的脚本。"""
    m = re.search(r"^\*\*闸：\*\*\s*`([\w./-]+\.py)`", t, re.M)
    return t[:m.start(1)] + "scripts/gen_og.py" + t[m.end(1):] if m else None



# ---------- 繁体站那道闸：注入到 tw/ 下的一个页面 ----------
# 页面动态挑，不写死路径 —— 稿子一改路径就变，而「用例失效」比「门禁失效」更难发现。
def _pick_tw():
    base = os.path.join(ROOT, "tw", "i")
    if not os.path.isdir(base):
        return ""
    for parent in sorted(os.listdir(base)):
        pd = os.path.join(base, parent)
        if not os.path.isdir(pd):
            continue
        for k in sorted(os.listdir(pd)):
            f = os.path.join(pd, k, "index.html")
            if os.path.isfile(f):
                return f
    return ""


TWPAGE = _pick_tw()


def _tw_edit(fn):
    def go():
        if not TWPAGE or not os.path.exists(TWPAGE):
            return False
        t = read(TWPAGE)
        out = fn(t)
        if out is None or out == t:
            return False
        write(TWPAGE, out)
        return True
    return go


def _tw_rm():
    def go():
        if not TWPAGE or not os.path.exists(TWPAGE):
            return False
        os.remove(TWPAGE)          # disarm 会把它拷回来
        return True
    return go


def _tw_link():
    return _tw_edit(lambda t: t.replace('href="/tw/assets/', 'href="/tw/zzz/', 1)
                    if 'href="/tw/assets/' in t else None)


def _tw_simp():
    return _tw_edit(lambda t: t.replace("<h1", "<p>这里是没转过来的简体字说明</p><h1", 1)
                    if "<h1" in t else None)


def _tw_ambig():
    return _tw_edit(lambda t: t.replace("<h1", "<p>明白髮生了什麼</p><h1", 1)
                    if "<h1" in t else None)


def _tw_never():
    # 「核心系统」被切成「核|心系|统」的那一类错，NEVER 表专门筛它
    return _tw_edit(lambda t: t.replace("<h1", "<p>核心繫統</p><h1", 1) if "<h1" in t else None)


def _tw_href():
    return _tw_edit(lambda t: t.replace('hreflang="zh-Hant"', 'hreflang="zh-XX"', 1)
                    if 'hreflang="zh-Hant"' in t else None)



# ── 语言站链接（check_links.py）──────────────────────────────────
# 这道闸防的是「两版一起错，对比两版的检查看不见」那一类，见 FAILURES.md 17。
# 所以注入也得落在**产物**上：闸读的是构建出来的 tw/ 和 en/，不是源码。
def _links_sister():
    """把姊妹站地址改回错的那种写法：/podcast/tw/ → /tw/podcast/。

    这正是线上跑了很久的那个 bug —— 555 个繁体页的页脚都是这个地址，
    而它不存在。旧的「两版链接一致」检查放行它，因为两边一起错。
    """
    return _tw_edit(lambda t: t.replace("https://ourword.ai/podcast/tw/",
                                        "https://ourword.ai/tw/podcast/", 1)
                    if "https://ourword.ai/podcast/tw/" in t else None)


LAYERPAGE = os.path.join(ROOT, "i", "su-shi", "index.html")


def _links_nolayer():
    """把一页的语言层标记拿掉 —— 模拟被 walk 静默跳过。

    _derived() 按子串比路径那次，5 个页面就是这么消失的：没有 hreflang、
    没有夜间模式、没有聊天挂件，而构建一句话都不说。
    """
    def go():
        t = read(LAYERPAGE)
        if "<!--HWX:LANG-->" not in t:
            return None
        write(LAYERPAGE, t.replace("<!--HWX:LANG-->", "<!--HWX:GONE-->", 1))
        return LAYERPAGE

    return go



# ── 英文站（check_en.py / check_en_js.py）────────────────────────
# 两道闸都读**构建产物**，所以注入落在 en/ 下的页面上，和繁体那几条一样。
ENPAGE = os.path.join(ROOT, "en", "i", "su-shi", "index.html")
ENHOME = os.path.join(ROOT, "en", "index.html")


def _en_cjk():
    """往英文页的正文里塞一句中文 —— 模拟界面串漏译。

    界面层那 90 多条就是靠「/en/ 里不许剩中文」这条判据一条条数出来的；
    这条判据自己得先能失败。
    """
    def go():
        t = read(ENPAGE)
        if "<h1" not in t:
            return None
        i = t.index("<h1")
        j = t.index(">", i) + 1
        write(ENPAGE, t[:j] + "\u8fd9\u91cc\u662f\u6ca1\u8bd1\u7684\u754c\u9762\u4e32" + t[j:])
        return ENPAGE

    return go


def _en_js():
    """把一个 JS 单引号字符串截断 —— 模拟盲替换插进了一个撇号。

    真事：'You\'ll play it differently after →' 让整个 script 块语法错误，
    首页打开是空的，而当时所有闸门都报绿 —— 它们查文本，不查能不能跑。
    """
    def go():
        t = read(ENHOME)
        a = "var HWXD="
        if a not in t:
            return None
        i = t.index(a)
        j = t.index("</script>", i)
        # 在这一块的末尾加一句语法上不成立的赋值
        write(ENHOME, t[:j] + "\nvar _hwx_broken='it'll break';\n" + t[j:])
        return ENHOME

    return go


CASES = [
    # (分支名, 门禁命令, 被改的文件, 注入函数, 必须报出的理由)
    ("章节·dek 过短",   "check_chapters.py", CHAP, _sub_field("dek", _short(3)),  "dek"),
    ("章节·story 过短", "check_chapters.py", CHAP, _sub_field("story", _short(3)), "story"),
    ("章节·分则不足",   "check_chapters.py", CHAP, _drop_list_item("f"),          "分则"),
    ("章节·分则 d 过短", "check_chapters.py", CHAP, _short_d(),                   "d 2 chars"),
    ("章节·apply 三行", "check_chapters.py", CHAP, _break_apply(),                "apply is not"),
    ("章节·金句数量",   "check_chapters.py", CHAP, _drop_list_item("q"),          "quotes (want 3)"),
    ("章节·story 红字", "check_chapters.py", CHAP, _sub_field("story", _mark),    "story 有"),
    ("章节·分则红字",   "check_chapters.py", CHAP, _mark_in_f(),                  "分则里有红字"),
    ("章节·金句红字",   "check_chapters.py", CHAP, _mark_in_list("q"),            "金句块里有红字"),
    ("章节·src 为空",   "check_chapters.py", CHAP, _blank_src(),                  "empty src"),
    ("章节·目录有无章", "check_chapters.py", CHAP, _orphan_catalog_item(),        "no chapter"),
    ("章节·章不在目录", "check_chapters.py", CHAP, _rename_key(),                 "not in the catalog"),
    ("章节·跨章重复",   "check_chapters.py", CHAP, _dup_sentence(),               "repeated across"),
    # 这条要**只**命中「查资料语气」：必须以 怎么/如何/该怎么/怎样 开头，
    # 同时得带上人称或情境词，否则会连带触发「无人称无情境」，
    # 报出来的理由就不是这一条了（第一版写「这本书的主要观点是什么」就是这么翻的）。
    ("问题·查资料语气", "check_questions.py", SCENES, _q_sub("怎么才能让自己不那么累"), "查资料语气"),
    ("问题·抽象词",     "check_questions.py", SCENES, _q_sub("我的本质是什么呢"),      "抽象词"),
    ("问题·无人称",     "check_questions.py", SCENES, _q_sub("天气好不好呢哈哈"),      "无人称无情境"),
    ("问题·过短",       "check_questions.py", SCENES, _q_sub("我累了"),              "过短"),
    ("问题·过长",       "check_questions.py", SCENES, _q_sub("我每天都在想这件事情到底该怎么办才好呢真的很累"), "过长"),
    ("覆盖·坏引用",     "check_coverage.py",  SCENES, _bad_ref(),           "引用指向不存在的章节"),
    ("完整·缺分享图",   "check_integrity.py", OGPNG,  _drop_og(),           "章节无分享图"),
    ("重复·同页重块",   "check_repetition.py", PAGE,  _html_ins(PAGE, "<p>%s</p>" % MARK, 2), MARK),
    ("加重·同页重复",   "check_pullquotes.py", PAGE,
     _html_ins(PAGE, '<b class="key">%s</b><p>%s</p>' % (MARK, MARK)),      MARK),
    ("加重·旧式残留",   "check_pullquotes.py", PAGE,
     _html_ins(PAGE, '<blockquote class="say">%s</blockquote>' % MARK),     "残留  "),
    ("金句·正文重叠",   "check_quote_overlap.py . 10", PAGE_Q, _quote_overlap(), MARK),
    ("台账·没写去向",   "wikigate.py", LEDGER, _led(_drop_gate_line),  "没写去向"),
    ("台账·无但没理由", "wikigate.py", LEDGER, _led(_strip_reason),    "没给理由"),
    ("台账·看不出脚本", "wikigate.py", LEDGER, _led(_no_script),       "看不出点名了哪个脚本"),
    ("台账·脚本不存在", "wikigate.py", LEDGER, _led(_ghost_script),    "不存在"),
    ("台账·闸没挂上",   "wikigate.py", LEDGER, _led(_unhooked),        "没挂在 gate.py"),
    ("繁体·缺页",       "check_tw.py", TWPAGE, _tw_rm(),        "繁体站缺页"),
    ("繁体·链接改坏",   "check_tw.py", TWPAGE, _tw_link(),      "链接对不上"),
    ("繁体·漏转",       "check_tw.py", TWPAGE, _tw_simp(),      "疑似漏转"),
    ("繁体·歧义未登记", "check_tw.py", TWPAGE, _tw_ambig(),     "没登记过"),
    ("繁体·切错组合",   "check_tw.py", TWPAGE, _tw_never(),     "切错"),
    ("繁体·hreflang",   "check_tw.py", TWPAGE, _tw_href(),      "hreflang 两版不一致"),
    ("语言站·姊妹站地址", "check_links.py", TWPAGE, _links_sister(), "这个页面不存在"),
    ("语言站·缺语言层",   "check_links.py", LAYERPAGE, _links_nolayer(), "没有 <!--HWX:LANG-->"),
    ("英文站·界面漏译",   "check_en.py", ENPAGE, _en_cjk(), "still has Chinese"),
    ("英文站·脚本被截断", "check_en_js.py", ENHOME, _en_js(), "SyntaxError"),
]


def _drop_pycache():
    """跑门禁前必须清掉 .pyc —— 否则读到的是上一条用例的注入。

    踩过：Python 判断 .pyc 是否新鲜看的是源文件的 (mtime 秒, size)。
    本文件里多数注入恰好都改动 4 个字节（加一对 `==`），如果两条用例落在同一秒内，
    第二次注入的 (mtime, size) 会和第一次**完全一致**，于是 Python 直接加载
    上一条用例编译出来的 .pyc —— 门禁看到的是别人的缺陷。
    症状是「拦下了，但理由不是这一条」；只看退出码的话这一步完全隐形。
    """
    for base in (os.path.join(ROOT, "seo"), os.path.join(ROOT, "scripts")):
        for d, subdirs, _ in os.walk(base):
            if os.path.basename(d) == "__pycache__":
                shutil.rmtree(d, ignore_errors=True)


def run_gate(cmd):
    _drop_pycache()
    parts = cmd.split()
    r = subprocess.run([sys.executable, os.path.join(HERE, parts[0])] + parts[1:],
                       cwd=ROOT, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def main():
    recover_pending()
    if not preflight():
        print("✗ preflight 失败：崩溃恢复机制本身不工作，后面的结果都不可信")
        return 1

    print("门禁自检 · 每条失败分支注入一次，核对**报出的理由**而非仅退出码")
    print("（preflight ✓ 崩溃恢复已自验：模拟被 kill，残留会被还原）\n")

    baseline = {}
    fails = []
    for name, cmd, path, inject, want in CASES:
        gate = cmd.split()[0]
        if gate not in baseline:
            baseline[gate] = run_gate(cmd)[0]
        if baseline[gate] != 0:
            print("  %-16s ✗ 工作区本来就是脏的（不是这道闸的问题）" % name)
            fails.append(name)
            continue
        arm(path)
        try:
            hit = inject()
            rc, out = run_gate(cmd) if hit else (None, "")
        finally:
            disarm(path)
        if not hit:
            mark = "✗ 用例失效（挑不到注入点）"
        elif rc == 0:
            mark = "✗ 这条分支是死的（注入了却放过）"
        elif want not in out:
            mark = "✗ 拦下了，但理由不是这一条（可能撞到了别的分支）"
        else:
            mark = "✓"
        print("  %-16s %s" % (name, mark))
        if mark != "✓":
            fails.append(name)

    # ---- 覆盖反查：gate.py 里的闸，有没有哪一道一条用例都没有 ----
    # 这一步防的是**退化**：以后谁加一道新闸，如果不配反向注入，
    # 整套看起来照样全绿 —— 而那道新闸是不是活的，没人知道。
    # 这正是这套东西要治的病，不能在自己身上再犯一次。
    runner = read(os.path.join(HERE, "gate.py"))
    listed = re.findall(r'\("[^"]+",\s*"([\w.]+\.py)', runner)
    covered = {c[1].split()[0] for c in CASES}
    naked = [g for g in dict.fromkeys(listed) if g not in covered]
    print()
    if naked:
        print("覆盖反查 ✗ 这几道闸挂在 gate.py 上，却一条反向注入都没有：")
        for g in naked:
            print("     ", g)
        fails.append("覆盖反查：" + "、".join(naked))
    else:
        print("覆盖反查 ✓ gate.py 上的 %d 道闸都至少有一条反向注入" % len(set(listed)))

    if fails:
        print("不合格：" + "、".join(fails))
        print("（注入后必须返回 1，且必须报出这条分支自己的理由）")
        return 1
    print("✓ %d 条失败分支都验证过：注入缺陷会被拦下，理由对得上，文件已还原" % len(CASES))
    return 0


if __name__ == "__main__":
    sys.exit(main())

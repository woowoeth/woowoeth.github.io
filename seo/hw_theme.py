# -*- coding: utf-8 -*-
"""Editorial item-page theme for Human World."""
import re
import geo_kit as _gk
from geo_kit import esc, clip, SITE, org_ld, item_ld, breadcrumb_ld, faq_ld
from geo_kit import head_block, ga_block, sibling_links

CSS = ""

SHARE_SVG = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<path d="M12 3v11M12 3 8.5 6.5M12 3l3.5 3.5"/>'
    '<path d="M5 13v6a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-6"/></svg>'
)

def brand_html(home_href, slogan=""):
    extra = ('<span class="slogan">%s</span>' % esc(slogan)) if slogan else ""
    return (
        '<a class="brand" href="%s">'
        '<img class="brand-logo" src="/favicon.svg" width="36" height="36" alt="">'
        '<span class="brand-copy">'
        '<span class="wordmark">人类世界<span class="dot">生存法则</span></span>'
        '%s</span></a>'
    ) % (esc(home_href), extra)

def _paras(text):
    return [p.strip() for p in str(text).split("\n") if p.strip()]

def _share_btn(title, url, text):
    """两份分享文案，用途不同，不能共用一份。

    data-share-text 是**粘贴**用的：末尾带链接，粘到微信、备忘录、任何地方
    都立得住。
    data-share-desc 是**系统分享面板**用的：一句简介，**不带链接** ——
    链接由 navigator.share 的 url 字段单独出一次。

    共用一份的代价：text 末尾的链接和 url 字段是同一个地址，一次分享出现
    两个 URL，微信会把它当成两个条目（原声那边实测到过：文本正常发出，
    URL 另存成一个一百多字节的临时文件跟着发过去）。
    """
    desc = text.split("\n\n")
    desc = desc[1] if len(desc) >= 3 else (desc[0] if desc else "")
    return (
        '<button class="share-btn" type="button" data-share '
        'data-share-title="%s" data-share-url="%s" data-share-desc="%s" '
        'data-share-text="%s" '
        'aria-label="分享本页">%s 分享</button>'
        % (esc(title), esc(url), esc(desc), esc(text), SHARE_SVG)
    )

KEYW = '<b class="key">%s</b>'


def _emph_in(html, start, span):
    """把选中的那一句在它本来所在的段落里加重，而不是另起一块。

    条目页原来把它插在那一节之前当引言（章节页是插在段后），两种摆法
    都逃不过一件事：同一句话读者会读两遍。全站条目页 358 处、
    章节页 902 处，全是紧邻正文的逐字截取。
    找不到就什么都不做——宁可少一处加重，也不要标错位置。
    """
    e = esc(span)
    # slots 记的是这一节在 html 里的插入位置，而那时这一节的段落已经进去了，
    # 所以只往后找是找不到的（第一版就栽在这儿，全站 0 处加重）。整表找。
    order = list(range(start, len(html))) + list(range(start - 1, -1, -1))
    for j in order:
        if e in html[j]:
            html[j] = html[j].replace(e, KEYW % e, 1)
            return True
    return False


_STRIP = "\u300c\u300d\u201c\u201d\u2018\u2019\u3002\uff0c\u3001\uff01\uff1f\uff1b\uff1a\u2014\u2026 .,!?;:\"'"


def _bare(t):
    return "".join(c for c in str(t or "") if c not in _STRIP)


_ENDS = "。！？"
_MIN, _MAX = 18, 145
# 英文按字符算：中文 18-145 字是「一句到一小段」，英文一个词约 5 个
# 字符，同样的区间是 45-190。照搬 18 的话，三个词就算一条金句。
_MIN_EN, _MAX_EN = 45, 190


def _breathe(text, target=120, floor=45):
    """Break a wall of text at sentence boundaries.

    story fields run to 350 characters — twelve lines, close to two phone
    screens, as a single <p>. Nothing is reworded; the paragraph just gets
    somewhere to breathe.
    """
    if len(text) <= 165:
        return [text]
    parts = [x for x in re.split(r"(?<=[\u3002\uff01\uff1f])", text) if x.strip()]
    out, buf = [], ""
    for x in parts:
        buf += x
        if len(buf) >= target:
            out.append(buf)
            buf = ""
    if buf:
        if out and len(buf) < floor:
            out[-1] += buf
        else:
            out.append(buf)
    return out or [text]


# 英文断句：句末标点后面必须跟空白 + 大写字母（或到头），否则
# 「C.S. Lewis」「e.g. 」「1963. 」全会被当成句子边界切开。
_EN_SPLIT = re.compile(r'(?<=[.!?])(?=\s+["\u201c(]?[A-Z0-9])')


def _spans(text):
    """Sentences, plus runs of adjacent sentences, as pull-quote candidates."""
    if _looks_cjk(text):
        parts = [x for x in re.split(r"(?<=[%s])" % _ENDS, text) if x.strip()]
        lo, hi = _MIN, _MAX
    else:
        parts = [x for x in _EN_SPLIT.split(text) if x.strip()]
        lo, hi = _MIN_EN, _MAX_EN
    out = []
    for i in range(len(parts)):
        run = ""
        for j in range(i, min(i + 3, len(parts))):
            run += parts[j]
            if lo <= len(run) <= hi:
                out.append(run.strip())
    return out


def _quotability_en(t):
    """英文那一套打分。中文那套全靠「」、——、不是…而是这些标记，英文文本
    一个都没有，一律 0 分，而门槛是 >0 —— 结果是整个英文站 1477 处就地
    加重一处都没有，中文页每一节都有一句被挑出来加重，英文页从头到尾一片
    均匀的灰。这是两边看起来最不像的一处。

    挑的标准和中文那套是同一个：句子里有没有引语、有没有一个破折号落下
    判断、有没有「不是 X 而是 Y」这种转折。杀掉的也一样：日期、数字、例子。
    """
    if not (_MIN_EN <= len(t) <= _MAX_EN):
        return -1.0
    s = 0.0
    low = t.lower()
    if ('"' in t and t.count('"') >= 2) or ("\u201c" in t and "\u201d" in t):
        s += 2.2
    if " \u2014 " in t or " \u2013 " in t:
        s += 1.3
    if re.search(r"\bnot\b[^.]{0,60}\bbut\b", low):
        s += 1.4
    elif re.search(r"\b(?:not|but|rather than|instead of)\b", low):
        s += 0.6
    for w in ("only", "never", "always", "in fact", "actually", "really",
              "the point is", "what matters", "turns out"):
        if w in low:
            s += 0.4
    if re.search(r"\d{3,}|\d+\s*(?:%|per cent|years|months)", low):
        s -= 1.6
    for w in ("e.g.", "for example", "such as", "for instance"):
        if w in low:
            s -= 1.2
    s += min(t.count(","), 4) * 0.12
    return s


def _quotability(t):
    """What makes a line worth blowing up: a quotation inside it, a dash landing
    a verdict, an X-not-Y turn. What kills it: dates, numbers, worked examples."""
    if not _looks_cjk(t):
        return _quotability_en(t)
    if not (_MIN <= len(t) <= _MAX):
        return -1.0
    s = 0.0
    if "\u300c" in t and "\u300d" in t:
        s += 2.2
    if "\u2014\u2014" in t:
        s += 1.3
    if "\u4e0d\u662f" in t and "\u800c\u662f" in t:
        s += 1.4
    elif "\u4e0d\u662f" in t or "\u800c\u662f" in t:
        s += 0.6
    for w in ("\u53ea\u6709", "\u624d\u7b97", "\u6c38\u8fdc", "\u4ece\u6765",
              "\u672c\u8d28\u4e0a", "\u5b9e\u9645\u4e0a", "\u771f\u6b63"):
        if w in t:
            s += 0.4
    if re.search(r"\d{3,}|\d+\s*[\u5e74\u6708\u4ebf\u4e07%]", t):
        s -= 1.6
    for w in ("\u4f8b\uff1a", "\u6bd4\u5982", "\u4f8b\u5982", "\u516c\u53f8\u7248"):
        if w in t:
            s -= 1.2
    s += min(t.count("\uff0c"), 4) * 0.12
    return s


def _pick_pullquotes(pool, want):
    """1-3 lines, deliberately mixed length: one short, one medium, one long."""
    cjk = any(_looks_cjk(span) for _s, span, _c in pool)
    buckets = (((18, 45), (46, 90), (91, _MAX)) if cjk
               else ((45, 90), (91, 140), (141, _MAX_EN)))
    order = [1, 0, 2] if want <= 2 else [1, 0, 2]
    chosen, used_secs = [], set()
    for b in order[:want]:
        lo, hi = buckets[b]
        best = None
        for sec, span, sc in pool:
            if sec in used_secs or not (lo <= len(span) <= hi):
                continue
            if best is None or sc > best[2]:
                best = (sec, span, sc)
        if best:
            used_secs.add(best[0])
            chosen.append(best)
    for sec, span, sc in sorted(pool, key=lambda x: -x[2]):   # top up if a bucket was empty
        if len(chosen) >= want:
            break
        if sec not in used_secs:
            used_secs.add(sec)
            chosen.append((sec, span, sc))
    return chosen


_OVERLAP = 10
# 英文按字符算。10 个汉字是一整句短语；换算成英文，「一整句短语」大约是
# 45 个字符（九到十个词）。取 30 试过，太松 —— 70 条金句和正文重合 75 个
# 字符以上，等于把同一句话在同一页上印两遍，那正是这个站不许的事。
_OVERLAP_EN = 45


def _echoes(quote, body):
    """True when the quote and the body share a long enough run.

    Exact containment missed the common case: the body highlights 「先为不可胜，
    以待敌之可胜」 while the 金句 list carries 「昔之善战者，先为不可胜，以待敌之
    可胜。」 — different strings, same line, printed twice.

    阈值必须按语言分。10 个**汉字**是一整句短语，重合了就是真的重复；
    10 个**英文字符**只是两个短单词（"predictor " / "contempt i"），
    随便哪句英文金句都能和正文撞上 —— 结果是 6 个英文条目的金句段整段
    消失，而中文同一个条目好好的。英文按 30 个字符（约六个词）算。
    """
    q, b = _bare(quote), _bare(body)
    if not q:
        return False
    n = _OVERLAP if _looks_cjk(q) else _OVERLAP_EN
    if len(q) < n:
        return q in b
    return any(q[i:i + n] in b for i in range(len(q) - n + 1))


CHAPTER_QUOTES = {}


def _whole_sentences(t):
    """砍到最后一个完整句子。

    it.summary 是「名字（年代）——关键词。」+ d 的**前 140 字**，那个 140 是
    硬切的：切在哪个字上纯看运气。它当页面 meta 用没关系（搜索结果本来就
    会再截一次），但它同时是**分享文案** —— 读者转发到微信、X 上的那段字
    就这么断在半句：「…逆境没有摧毁他，反而成」「…a cook」。三种语言都是。
    配套的闸：scripts/check_dek.py 第 ③ 条。
    """
    t = str(t or "").rstrip()
    if not t:
        return t
    # 两套标点都算；引号收尾也算句子结束
    ends = [t.rfind(c) for c in ("\u3002", ".", "!", "?", "\uff01", "\uff1f",
                                 "\u201d", "\u300d")]
    i = max(ends)
    if i > len(t) * 0.4:
        return t[:i + 1]
    # 找不到够靠后的句号（d 的前 140 字里恰好一句都没说完）。第一版这里
    # 原样返回，等于把硬切口当完整句子交出去 —— 那正是要修的东西。
    # 老实打个省略号：读者看得懂「这里还有」，看不懂的是断在半个词上。
    cut = t.rstrip()
    sp = cut.rfind(" ")
    if sp > len(cut) * 0.5:      # 英文按词界砍；中文没有空格，走下一行
        cut = cut[:sp]
    return cut.rstrip(" ,;:\u3001\uff0c\uff1b\u00b7\u2014-") + "\u2026"


def _dek(summary):
    """Standfirst for an entry page.

    it.summary is "名字（年代）——关键词。" + the first 140 chars of d, and d is
    printed in full a few lines below as the pull. Keep the identifying half,
    which carries the only copy of the precise era; drop the rest. About 12,000
    characters of same-page duplication across the site.

    标点必须两套都认。中文是「——」和「。」，英文是「 — 」和「.」——
    只认中文那套的话，英文页上这一裁整块不发生：读者看到的是
    it.summary 里 d[:140] 那个硬切口，「… a cook and a provincial
    governor. He was banished」后面直接没了，而正文几行之下又把同一段
    完整印一遍。共用模板里写死 CJK 标点，就是这么在另一种语言上发作的。
    配套的闸：scripts/check_dek.py。
    """
    t = str(summary or "")
    i = t.find("\u2014")          # 破折号：中文「——」是两个，英文「 — 」是一个
    if i < 0:
        return t
    ends = [j for j in (t.find("\u3002", i), t.find(".", i)) if j > 0]
    return t[:min(ends) + 1] if ends else t


# ── 版块标记：中英两套，两套都认 ──────────────────────────
# _render_blocks 是**按标题文字**认版块类型的：认出「分则」就渲染成
# section.point（带 h2 和例子），认出「金句」就收集起来最后单独成块，
# 「对照」「延伸」各有自己的版式。英文站的标题是 "The parts · …"
# "Lines to keep" "Further"，一个都不认识 —— 于是整页英文条目页塌成
# 一串一模一样的 section.sec，中文那边有的引言框、分则卡片、金句块、
# 对照块、延伸块，英文一个都没有。用户说的「看起来与中文版相差甚远」
# 就是这个。
#
# 不加语言开关：中文页上不会出现 "The parts"，英文页上不会出现「分则」，
# 两套标记同时认不会打架，也就没有「传错语言」这种失败模式。
def _looks_cjk(t):
    return bool(re.search(r"[\u4e00-\u9fff]", t or ""))


def _is_point(h):
    return h.startswith("\u5206\u5219") or h.startswith("The parts")


def _is_quotes(h):
    return h in ("\u91d1\u53e5", "\u539f\u8bdd", "Lines to keep")


def _is_contrast(h):
    return "\u5bf9\u7167" in h or "read alongside" in h


def _is_ext(h):
    return h in ("\u5ef6\u4f38", "Further")


def _is_pull(h):
    return "\u7559\u4e0b" in h or "leave behind" in h


def _is_apply(h):
    return "\u4eca\u5929" in h or "use it today" in h


def _is_after(h):
    return "\u540e\u6765" in h or "actually happened" in h


def _eg_body(p):
    """是不是「例」那一行；是就返回例子本身，不是就返回 None。"""
    for mark in ("\u4f8b\uff1a", "\u4f8b:", "e.g. ", "e.g.: "):
        if p.startswith(mark):
            return p[len(mark):].strip()
    return None


def _render_blocks(it, zh):
    html, toc, first_q, n = [], [], True, 0
    slots, pool, quote_block = [], [], []
    rendered = set()              # every <p> actually emitted on this page
    for h, b in it.b(zh):
        h = (h or "").strip()
        paras = _paras(b)
        if not paras:
            continue
        if _is_point(h):
            name = h.split("\u00b7", 1)[-1].strip() if "\u00b7" in h else h
            n += 1
            aid = "p%d" % n
            toc.append((aid, name))
            body, egs = [], []
            for p in paras:
                eg = _eg_body(p)
                if eg is not None:
                    egs.append(eg)
                else:
                    body.append(p)
            html.append('<section class="point" id="%s">' % aid)
            rendered.add(name)          # a 分则 title is read text too
            html.append("<h2>%s</h2>" % esc(name))
            for para in body:
                for x in _breathe(para):
                    rendered.add(x)
                    html.append("<p>%s</p>" % esc(x))
            for p_ in egs:
                rendered.add(p_)
                html.append('<p class="eg">%s</p>' % esc(p_))
            html.append("</section>")
            si = len(slots)
            # Close the section with its own strongest line rather than opening
            # with it — the span usually IS the section's first sentence, and
            # putting it above means reading the same words twice in a row.
            slots.append(len(html))
            whole = "".join(body + egs)
            # Candidates are generated per paragraph. Spanning the boundary
            # produced quotes that stitched the principle onto the worked
            # example — two visually separate blocks in the page.
            for paras_src, penalty in ((body, 0.0), (egs, 0.8)):
                for para in paras_src:
                    for span in _spans(para):
                        # A callout has to be an EXCERPT. When the span is most
                        # of the section, the reader gets the same paragraph
                        # twice in a row.
                        if len(whole) - len(span) < 45:
                            continue
                        # …and a real excerpt of its OWN paragraph. _breathe
                        # splits long paragraphs on the same sentence
                        # boundaries _spans uses, so a span can come out byte
                        # for byte identical to a rendered paragraph.
                        if len(para) - len(span) < 20:
                            continue
                        # And it has to carry something beyond a 「quotation」
                        # the 金句 section already lists.
                        own = re.sub(r"\u300c[^\u300d]*\u300d", "", span)
                        if len(own.strip("\u3002\uff0c\u3001\uff01\uff1f\uff1b\uff1a\u2014 ")) < 20:
                            continue
                        pool.append((si, span, _quotability(span) - penalty))
            continue
        if _is_quotes(h):
            quote_block = paras          # rendered last, after the body is known
            continue
        if _is_contrast(h):
            toc.append(("contrast", "对照着读"))
            html.append('<section id="contrast"><h2 class="sec-k">和谁对照着读</h2><div class="contrast">')
            for p in paras:
                # 分隔符两套：中文「名字：理由」，英文「Name — why」。
                if "\uff1a" in p:
                    name, why = (p.split("\uff1a", 1) + [""])[:2]
                elif " \u2014 " in p:
                    name, why = (p.split(" \u2014 ", 1) + [""])[:2]
                else:
                    name, why = p, ""
                html.append(
                    '<a href="/i/%s/"><span class="n">%s</span><span class="why">%s</span></a>'
                    % (esc(_slug(name)), esc(name), esc(why))
                )
            html.append("</div></section>")
            continue
        if _is_ext(h):
            toc.append(("ext", "延伸"))
            html.append('<section id="ext"><h2 class="sec-k">延伸</h2><div class="ext">')
            for p in paras:
                # Entry names may legitimately contain 、 or ，（思考，快与慢 /
                # 枪炮、病菌与钢铁）. Splitting on them produced /i/思考/ and
                # /i/枪炮/ — links to pages that never existed. Only fall back to
                # splitting when the whole line is not itself a known entry.
                # Split on whitespace ONLY. Entry names never contain a space,
                # but two of them contain 、 / ， (思考，快与慢 和
                # 枪炮、病菌与钢铁) — splitting on those produced
                # /i/思考/ and /i/枪炮/, links to pages that never existed.
                # 按空格切**只对中文成立**：条目名里从不含空格，所以一行
                # 里的几个名字用空格分开。英文名几乎都含空格
                # （Wang Yangming / C.S. Lewis / Winston Churchill）——
                # 照切会切出 /en/i/wang/ 和 /en/i/yangming/ 这种从不存在的
                # 页面。英文那边一行就是一个名字，整行拿来用。
                names = ([x.strip("\u00b7,\uff0c\u3001 ") for x in p.split()]
                         if _looks_cjk(p) else [p.strip()])
                for name in names:
                    if name:
                        html.append('<a href="/i/%s/">%s</a>' % (esc(_slug(name)), esc(name)))
            html.append("</div></section>")
            continue
        label = h
        if label.startswith("Q：") or label.startswith("Q:"):
            label = label.split("：", 1)[-1].split(":", 1)[-1]
        if first_q and _is_pull(h):
            first_q = False
            rendered.add(paras[0])      # the pull is body the reader has read too
            html.append('<aside class="pull">%s</aside>' % esc(paras[0]))
            if len(paras) > 1:
                html.append('<section class="sec">')
                for para in paras[1:]:
                    for x in _breathe(para):
                        rendered.add(x)
                        html.append("<p>%s</p>" % esc(x))
                html.append("</section>")
            continue
        n += 1
        aid = "s%d" % n
        toc.append((aid, label))
        klass = "sec apply" if _is_apply(h) else "sec"
        rendered.add(label)
        html.append('<section class="%s" id="%s"><h2 class="sec-k">%s</h2>' % (klass, aid, esc(label)))
        for para in paras:
            for x in _breathe(para):
                rendered.add(x)
                html.append("<p>%s</p>" % esc(x))
        html.append("</section>")
        # 「后来怎么了？」整段本来就是提炼过的短句（fail 一段 + 教训三条），
        # 从一个全是金句的段落里再抽金句，抽出来的是把三条教训连成的一串，
        # 紧跟在它们下面重念一遍。和「今天怎么用」同理，排除。
        if klass == "sec" and not _is_apply(h) and not _is_after(h):
            si = len(slots)
            slots.append(len(html))
            whole = "".join(paras)
            for span in _spans(whole):
                if len(whole) - len(span) < 45:
                    continue
                own = re.sub(r"\u300c[^\u300d]*\u300d", "", span)
                if len(own.strip("\u3002\uff0c\u3001\uff01\uff1f\uff1b\uff1a\u2014 ")) < 20:
                    continue
                pool.append((si, span, _quotability(span)))
    want = max(1, min(3, len(slots) - 1)) if slots else 0
    # 金句 section: 55 of 100 entries opened a 分则 by citing the very line the
    # list repeats at the foot. Keep only the ones the reader has not already
    # met in the body, and drop the section if that leaves nothing.
    seen_body = "".join(rendered)
    in_chapters = CHAPTER_QUOTES.get(it.title, set())
    # 同页去重（seen_body）是硬规则：同一页上下重复一遍，读者一眼看得出。
    # 跨页那条（in_chapters）不是——章节金句不出现在条目页上，读者在这一页
    # 并没有见过它。可它原来是硬过滤，代价是 26 个条目的金句段整段消失，
    # 孙子兵法的「知己知彼」、王阳明的「知行合一」这类名句本来就该两边都有。
    # 2026-09-01 降为优先级：先用章节里没有的；一条都不剩时，仍然显示。
    keep = [q for q in quote_block if _bare(q) and not _echoes(q, seen_body)]
    fresh = [q for q in keep if not any(_echoes(q, c) for c in in_chapters)]
    keep = fresh or keep
    if keep:
        toc.append(("quotes", "金句"))
        html.append('<section class="quotes" id="quotes"><h2 class="sec-k">金句</h2>')
        html.extend("<blockquote><p>%s</p></blockquote>" % esc(q) for q in keep)
        html.append("</section>")
    pool = [c for c in pool if c[2] > 0 and c[1] not in rendered]
    for si, span, _sc in sorted(_pick_pullquotes(pool, want),
                                key=lambda c: -slots[c[0]]):
        _emph_in(html, slots[si], span)
    return "\n".join(html), toc

def item_page(site, it, items, idx, zh, hub_of=None):
    zh_render = zh or site.zh()
    page_url = it.page(site, zh)
    alt_url = site.url(("i/%s/" if zh else "zh/i/%s/") % it.slug) if it.has_zh() else ""
    title = clip("%s — %s" % (it.t(zh_render), site.name_zh if zh_render else site.name), 70)
    ld = [org_ld(), item_ld(site, it, zh_render, page_url), breadcrumb_ld(site, it, zh_render)]
    f = faq_ld(it, zh_render)
    if f:
        ld.append(f)
    tags = it.tags or []
    cat = tags[0] if tags else ""
    one = tags[-1] if len(tags) >= 2 else ""
    eras = ("先秦与古典时代", "秦汉至魏晋", "中古", "近世", "工业时代", "现代")
    if one in eras:
        one = ""
    era = next((t for t in tags if t in eras), "")
    share_text = "%s\n\n%s\n\n%s" % (
        it.t(zh_render), _whole_sentences(it.s(zh_render)), page_url)
    blocks_html, toc = _render_blocks(it, zh_render)
    try:
        import hw_chapters
        blocks_html = hw_chapters.inject_catalog(blocks_html, it.title)
    except Exception:
        pass
    toc_html = ""
    if toc:
        items_t = ['<a href="#%s"><span class="i">%02d</span>%s</a>' % (esc(a), i, esc(n)) for i, (a, n) in enumerate(toc, 1)]
        toc_html = '<aside class="side"><div class="panel"><p class="ph">本篇结构</p><nav class="toc">%s</nav></div></aside>' % "".join(items_t)
    ordered = []
    if era:
        ordered.append(era)
    for t in tags:
        if t not in ordered:
            ordered.append(t)
    chips = []
    for t in ordered:
        sl = _slug(t)
        if hub_of and hub_of.get(sl):
            chips.append('<a class="chip" href="%s">%s</a>' % (esc(site.url("t/%s/" % sl)), esc(t)))
        else:
            chips.append('<span class="chip">%s</span>' % esc(t))
    prev_html = next_html = ""
    if idx > 0:
        p = items[idx - 1]
        prev_html = '<a href="%s"><span class="dir">上一篇</span>%s</a>' % (esc(site.url("i/%s/" % p.slug)), esc(p.t(zh_render)))
    if idx < len(items) - 1:
        nxt = items[idx + 1]
        next_html = '<a href="%s" style="text-align:right;margin-left:auto"><span class="dir">下一篇</span>%s</a>' % (esc(site.url("i/%s/" % nxt.slug)), esc(nxt.t(zh_render)))
    body = """
<header class="mast wrap">
  <div class="mast-top">
    %s
    <div class="mast-links">
      <a class="pill" href="%s">目录</a>
      <a class="pill" href="%s">全部</a>
    </div>
  </div>
</header>
<div class="wrap">
  <nav class="crumb">
    <a href="%s">首页</a><span class="sep">/</span>
    <a href="%s">%s</a><span class="sep">/</span>%s
  </nav>
  <div class="layout">
    <article>
      %s
      <h1>%s</h1>
      %s
      <p class="dek">%s</p>
      <div class="meta-row">%s%s</div>
      %s
    </article>
    %s
  </div>
  <nav class="sib">%s%s</nav>
  <footer class="site-foot">
    <p>本页可直接引用 <code>%s</code></p>
    <p><a href="%s">llms.txt</a> · <a href="%s">llms-full.txt</a></p>
    <p>%s</p>
  </footer>
</div>
""" % (
        brand_html(SITE + "/", site.tagline_zh if zh_render else site.tagline),
        esc(site.base), esc(site.url("all/")),
        esc(SITE + "/"), esc(site.base), esc(site.name_zh if zh_render else site.name),
        esc(it.t(zh_render)),
        ('<p class="kicker">%s</p>' % esc(cat)) if cat else "",
        esc(it.t(zh_render)),
        ('<p class="one">%s</p>' % esc(one)) if one else "",
        esc(_dek(it.s(zh_render))),
        "".join(chips),
        _share_btn(title, page_url, share_text),
        blocks_html, toc_html, prev_html, next_html,
        esc(page_url), esc(site.url("llms.txt")), esc(site.url("llms-full.txt")),
        sibling_links(site, zh_render),
    )
    return _shell("zh-Hans" if zh_render else "en", title,
                  head_block(site, page_url, title, it.s(zh_render), zh=zh_render, alt_url=alt_url, ld=ld, item=it),
                  body)

def _shell(lang, title, headhtml, body):
    return (
        "<!DOCTYPE html>\n<html lang=\"%s\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n"
        "<title>%s</title>\n%s\n%s\n"
        "<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n"
        "<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>\n"
        "<link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/css2?"
        "family=Noto+Serif+SC:wght@500;600;700&display=swap\">\n"
        "<link rel=\"stylesheet\" href=\"/assets/hw-entry.css?v=15\">\n"
        "<link rel=\"stylesheet\" href=\"/assets/hw-chapter.css?v=5\">\n"
        "</head>\n<body>\n%s\n"
        "<script src=\"/assets/hw-share.js\" defer></script>\n</body>\n</html>\n"
        % (lang, esc(title), headhtml, ga_block(), body)
    )

def _slug(name):
    """Resolve through geo_kit at CALL time.

    build_seo swaps in a slug map with `G.slugify = ...`, but this module did
    `from geo_kit import slugify` at import, so it kept the original function and
    every 延伸 / 对照 / 标签 link came out as a CJK URL (/i/韩非子/ instead of
    /i/han-feizi/) that only resolved through a legacy redirect stub.
    """
    return _gk.slugify(name)


def _known(name):
    """True when `name` resolves to a real (latin) slug, i.e. it is an entry title."""
    if not name:
        return False
    try:
        import hw_slugs
        sl = hw_slugs.slug_for(name)
    except Exception:
        return False
    return bool(sl) and not any("\u4e00" <= ch <= "\u9fff" for ch in sl)


def install(G):
    G._PAGE_CSS = CSS
    G._shell = _shell
    G.item_page = item_page
    import hw_list
    hw_list.install(G)

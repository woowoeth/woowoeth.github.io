#!/usr/bin/env python3
# Patch generators AND already-built HTML so highlight/sidebar cannot miss.
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SLOGAN_TEXT = "遇到事了，看看以前的人怎么处理"
STYLE = (
    '<style id="hw-force">'
    'mark,mark.hl{background:transparent!important;color:#9d2933!important;'
    'font-weight:700!important;text-decoration:none!important;}'
    '@media (max-width:900px){aside.side{display:none!important}'
    '.layout{grid-template-columns:1fr!important}}'
    '</style>'
)
MARK_OPEN = (
    '<mark class="hl" style="background:transparent;color:#9d2933;font-weight:700;'
    'text-decoration:none">'
)

# 读完之后的收尾块：条目页与章节页共用。
# 文案避开「觉得有用请分享」这种索取式说法——那是替网站要东西。
# 改成把动作说成读者自己的事：他刚获得了一个可用的想法，
# 分享是「把它给到那个正需要的人」，收藏是「下次遇到还找得到」。
OUTRO_CSS = (
    '<style id="hw-outro">'
    '.hw-outro{margin:38px 0 8px;padding:22px 20px;border-radius:16px;'
    'background:var(--surface-2,#f2ece0);text-align:center}'
    '.hw-outro p{font-family:"Noto Serif SC","Songti SC","STSong",serif;'
    'font-size:16px;line-height:1.9;margin:0 0 4px;color:var(--ink)}'
    '.hw-outro small{display:block;font-size:13px;color:var(--muted);'
    'line-height:1.8;margin-bottom:14px}'
    '.hw-outro .acts{display:flex;gap:10px;justify-content:center;flex-wrap:wrap}'
    '.hw-outro .acts button{border:1px solid var(--ink);background:var(--ink);'
    'color:var(--paper,#f7f4ec);border-radius:999px;padding:6px 18px;cursor:pointer;'
    'font-family:"Noto Serif SC","Songti SC",serif;font-size:13px;line-height:1.6}'
    '.hw-outro .acts button:active{transform:scale(.97)}'
    '</style>'
)


def outro_html(title, url, text):
    return (
        '<div class="hw-outro">'
        '<p>这一篇如果说中了你正在经历的事，</p>'
        '<small>转给可能需要的人，或者存下来，下次好找。</small>'
        '<div class="acts">'
        '<button type="button" data-share '
        'data-share-title="%s" data-share-url="%s" data-share-text="%s">分享</button>'
        '</div></div>'
    ) % (title, url, text)


OUTRO_JS = ""   # 收藏按钮已移除，不再需要


def patch_html():
    n = 0
    for path in (ROOT / "i").rglob("index.html") if (ROOT / "i").exists() else []:
        s = path.read_text(encoding="utf-8")
        # Legacy CJK-slug stubs are meta-refresh redirects rewritten byte-for-byte
        # by write_legacy_redirects on every build. Touching them here makes the two
        # scripts fight and produces a fresh commit every single run.
        if 'http-equiv="refresh"' in s:
            continue
        orig = s
        if 'id="hw-force"' not in s:
            s = s.replace("</head>", STYLE + "</head>", 1)
        s = re.sub(r"<mark class=\"hl\"(?: style=\"[^\"]*\")?>", MARK_OPEN, s)
        # 读完之后的收尾块——正文结束处，不是页脚
        if "hw-outro" not in s:
            m = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S)
            _t = re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else "人类世界生存法则"
            _u = "https://ourword.ai" + "/" + str(path.parent.relative_to(ROOT)) + "/"
            _u = _u.replace("//", "/").replace("https:/", "https://")
            _blk = outro_html(_t + " — 人类世界生存法则", _u, _t)
            for _tail in ('</section>\n</article>', '</div>\n</article>', '</article>'):
                if _tail in s:
                    s = s.replace(_tail, _blk + _tail, 1); break
            else:
                s = s.replace("</main>", _blk + "</main>", 1)
            s = s.replace("</head>", OUTRO_CSS + "</head>", 1)
        if s != orig:
            path.write_text(s, encoding="utf-8")
            n += 1
    print("force_chapter_ui html", n)

if __name__ == "__main__":
    patch_html()


# HWX v3: 最新 tab + 瀑布流混排 + 今日三样 + 历史行 + 暗色双主题
HWX_A, HWX_B = "<!--HWX:FIND-->", "<!--/HWX:FIND-->"

import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parent))  # CI 从仓库根调用本脚本
from hwx_scenes import SCENES as HWX_SCENES

# 悬浮球问答的后端地址。空字符串＝功能关闭（前端不渲染任何东西）。
# 2026-09-01 上线。Worker 名字是控制台随机生成的，不好看但只影响这一行；
# 改名要删了重建，不值当。key 存在 Worker 的 HW_CHAT_KEY secret 里，不进浏览器。
# 跨站调用由 Worker 的 Origin 白名单挡（fail-closed），跟同不同源无关。
HW_CHAT_ENDPOINT = "https://wandering-wind-0168.djjian.workers.dev"

HWX_INTROS = {
"sun-tzu":"最早也最完整的战争方法论，被读了两千五百年",
"adler":"把「这是谁的课题」问成一把刀的心理学家",
"csikszentmihalyi":"给几千人配呼叫器，找出人什么时候最投入",
"sapolsky":"在东非看了三十年狒狒，讲清压力如何伤人",
"bj-fogg":"斯坦福行为设计实验室，把习惯缩到不会失败",
"satir":"家庭治疗开创者，让全家站起来摆成雕塑",
"bowen":"提出自我分化：既在关系里，又是自己",
"thomas-gordon":"罗杰斯的学生，把倾听拆成父母能照做的步骤",
"vygotsky":"三十七岁去世，留下最近发展区这个概念",
"dweck":"成长型思维的提出者，效应比流行说法小得多",
"brene-brown":"把羞耻和内疚拆开的人：一个指着行为，一个指着你",
"pu-songling":"考了四十年没中，顺手写的《聊斋》成了——他不知道",
"perel":"伴侣治疗三十年：什么都好、就是没感觉了，是怎么回事",
"maslach":"倦怠量表的提出者：该修的是工作，不是人",
"jung":"把一生分成上午和下午，两段的题目不一样",
"rat-park":"把笼子换成公园，老鼠就不那么想喝吗啡水了",
"kleinman":"照护研究的权威，照顾患病妻子十年才知道有多难",
"murakami":"关了酒吧去写小说，用跑步的办法写了三十年",
"harvard-study":"跟了八十多年：让人晚年好过的不是钱，是关系",
"cacioppo":"孤独研究者：它是信号不是缺陷，像饿一样",
"konnikova":"骗局研究者：骗子不制造信任，他用你已经有的需要",
"granovetter":"弱连接的发现者：机会从不常见面的那些人那儿来",
"scarcity":"缺钱缺时间抢的是同一份脑子：不是不理性，是带宽被占满",
"kristin-neff":"把自我关怀做成可测量的东西：三个零件，少一个就变味",
"hochschild":"把家务和「装出来的情绪」算成劳动的社会学家",
"kevin-kelly":"不用红也能活：一千个铁杆粉丝，前提是中间不能有人",
"excellent-sheep":"在耶鲁教了十年，写下对精英教育的批评",
"cal-newport":"论证专注为何正在变成稀缺能力",
"feynman":"用一杯冰水戳穿NASA几百页报告的物理学家",
"carl-rogers":"第一个把心理治疗全程录音拿来做研究的人",
"attachment-theory":"从婴儿重聚那一刻看出一生关系模板",
"atomic-habits":"把改变拆到每天百分之一的行为设计",
"popper":"用「能不能被推翻」划开科学与空话",
"ericsson":"证明决定水平的是练法不是时长",
"montessori":"用环境替代管教的儿童教育奠基者",
"john-ratey":"把运动重新定义为大脑的药",

"nonviolent-communication":"把吵架拆成四步的沟通课",
"seneca":"在权力核心里写节制的斯多噶派",
"chris-voss":"谈判先处理情绪的FBI首席专家",
"gottman":"用实验室数据预测婚姻存亡的心理学家",
"crucial-conversations":"研究了两万人怎么把难谈的话谈成",
"mao":"从绝对弱势打到全局翻盘的战略操盘手",
"su-yu":"敢三次电报推翻上级部署的战役指挥员","tao-te-ching":"五千字讲透以柔克刚的元典",
"wang-yangming":"把「知道做不到」判为不知道的心学宗师","zeng-guofan":"资质平平、靠笨功夫成大事的标本",
"fan-li":"三次散尽家财三次重来的商圣","han-xin":"用兵如神却死于收场的名将",
"liu-bang":"承认部下都比自己强的开国皇帝","cao-cao":"乱世里只认结果不认出身的组织者",
"sima-yi":"靠熬和忍拿走天下的终局玩家","zhuge-liang":"把承诺执行到死的丞相",
"guan-zhong":"先解决吃饭再谈道德的第一名相","buffett":"把复利和常识做到极致的股东信作者",
"munger":"用上百个思维模型避蠢的巴菲特搭档","li-ka-shing":"九成时间在想失败的华人首富",
"jobs":"靠砍产品线救活苹果的产品独裁者","zhang-yiming":"把延迟满足做成方法的字节创始人",
"duan-yongping":"「本分」二字管一生的企业家","inamori":"两造世界五百强、再救日航的经营者",
"musk":"把一切拆到物理事实重算的造火箭者","huang":"专挑还不存在的市场下注的英伟达掌舵人",
"thiel":"专问「重要而无人同意」问题的逆向投资人","ren-zhengfei":"在最好年景写《华为的冬天》的创始人",
"sovereign-individual":"1997年预言数字货币与远程工作的奇书","zhang-liang":"功成身退教科书级别的帝王师",
"li-bi":"四朝辅政却坚决不要官位的白衣宰相","han-feizi":"不指望人性善的制度设计师",
"huo-qubing":"不读兵书只看战场的少年名将","li-shimin":"把逆耳之言制度化的皇帝",
"socrates":"承认自己无知的提问之父","marcus-aurelius":"一边打仗一边写自省笔记的皇帝",
"machiavelli":"只写人如何做、不写应如何做的政治解剖者","dalio":"把破产教训写成《原则》的桥水创始人",
"taleb":"专研黑天鹅与反脆弱的风险哲学家","naval":"把财富与运气讲成算法的硅谷天使",
"wang-xing":"只看核心、不设边界的美团创始人","strategies-of-the-warring-states":"纵横家的话术与人心案例库",
"analects":"被用了两千年的做人做事底层代码","sapiens":"用「虚构」一词解释人类协作的畅销书",
"wang-jian":"灭楚之前先自污求田宅的老将","xiang-yu":"赢了所有战役、输掉天下的霸王",
"wu-zetian":"破格用人也快速弃人的女皇","zhu-yuanzhang":"缓称王、熬死群雄的开国者",
"zhang-juzheng":"用考成法逼动整个官僚系统的改革家","su-shi":"被贬到哪就把日子过好到哪的大文豪",
"nietzsche":"专拆现成价值观的锤子哲学家","frankl":"从集中营带出意义疗法的心理学家",
"soros":"靠认错速度盈利的宏观投机者","influence":"拆解六种顺从开关的说服科学",
"innovators-dilemma":"解释好公司为何死于好管理的经典","guo-jia":"算人心比算兵力更准的谋士",
"bruce-lee":"把武术拆到「像水」的截拳道创始人","records-of-the-grand-historian":"功过同录的史家绝唱",
"zizhi-tongjian":"写给管理者的一千三百年案例集","gandhi":"用一撮盐动摇帝国的非暴力者",
"einstein":"在专利局改写物理学的问题重构者","shang-yang":"徙木立信再推变法的立规者",
"caesar":"把宽赦用作武器的内战赢家","mandela":"把审判变成讲台的和解者",
"napoleon":"在局部永远保持多数的用兵大师","musashi":"六十余战不败的孤剑客",
"zhuangzi":"把「无用」讲成活路的逍遥派","guo-ziyi":"功高震主却得善终的中兴名将",
"franklin":"把美德排进日程表的自我管理鼻祖","graham":"发明市场先生与安全边际的价值投资之父",
"livermore":"四起四落写下投机圣经的作手","thinking-fast-and-slow":"把人类判断的漏洞列成清单的心理学",
"crowd":"一百年前写透群体失智的社会心理学","bezos":"永远把公司留在第一天的长期主义者",
"thinking-in-systems":"教人先看结构再怪人的系统论入门","old-regime":"解释革命为何在松绑时爆发的史学经典",
"on-war":"把战争定义为政治延续的军事哲学","schelling":"证明自缚双手反而更强的博弈论者",
"hu-xueyan":"靠信用起家也毁于一注的红顶商人","wealth-of-nations":"用晚餐和扣针讲清市场的经济学开山",
"epictetus":"只管自己能控之事的奴隶哲学家","bai-gui":"人弃我取的商业鼻祖",
"grove":"只有偏执狂才能生存的英特尔舵手","technological-revolutions":"证明泡沫写在剧本里的技术史框架",
"marks":"不预测、只定位的周期观察者","feng-dao":"历五代十帝而善终的争议宰相",
"huineng":"不识字却讲透顿悟的禅宗六祖","simons":"让模型代替人交易的量化之王",
"lynch":"在商场里找十倍股的基金经理","art-of-worldly-wisdom":"三百年前的处世三百则",
"why-nations-fail":"用一墙之隔的双城解释贫富的制度经济学","lee-kuan-yew":"只问管不管用的新加坡设计师",
"boyd":"提出OODA循环、终身上校的空战理论家","guiguzi":"教人先听后说的纵横家祖师",
"la-rochefoucauld":"三百年前把人心写成箴言的公爵","paul-graham":"教创业者先做不能规模化之事的YC创始人",
"matsushita":"立志让电器便宜如自来水的经营之神","finite-and-infinite-games":"分清两种游戏的哲学小书",
"guns-germs-steel":"把文明差距归因于起跑线的地理史观","mencius":"把民心定为权力地基的亚圣",
"xunzi":"主张制度驯化人性的现实派儒家","drucker":"发明「管理学」这门学科的人",
"hayek":"证明知识无法集中的经济学家","bismarck":"铁血开国又急刹车的首相",
}

CAT_COLOR = {
    "谋略与竞争":"#a33b2e",
    "权力与组织":"#7d5a3c",
    "财富与风险":"#8a6d2f",
    "创业与产品":"#c26b3f",
    "识人与相处":"#5f7355",
    "心智与情绪":"#4e6b7a",
    "学习与成长":"#4a7c6f",
    "身心与生活":"#7a6a8a",
    "家庭与关系":"#a35f6e",
    "世界如何运转":"#6b5b73",
}

def _tint(hex_color, alpha):
    """把类别色化成极淡的底色——只用来区分门类，不能抢正文。"""
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return "rgba(%d,%d,%d,%.3f)" % (r, g, b, alpha)

CAT_TINT = {k: _tint(v, 0.055) for k, v in CAT_COLOR.items()}      # 亮色底
CAT_TINT_D = {k: _tint(v, 0.16) for k, v in CAT_COLOR.items()}     # 暗色底

# 用户搜的是口语（睡不着、拖延、吵架），内容里写的是书面语。索引只存正文，
# 这类查询必然落空。试过按词频自动关联，结果「拖延」命中张居正和《战争论》——
# 词频匹配不出主题。改为显式指定：一个口语词挂到哪几个条目，人工决定。
SYNONYMS = {
    "睡不着":   ["john-ratey", "cal-newport", "seneca"],
    "失眠":     ["john-ratey", "seneca", "marcus-aurelius"],
    "拖延":     ["atomic-habits", "wang-yangming", "cal-newport", "paul-graham"],
    "摆烂":     ["atomic-habits", "frankl", "inamori"],
    "吵架":     ["nonviolent-communication", "gottman", "crucial-conversations", "adler"],
    "冷战":     ["gottman", "nonviolent-communication", "adler"],
    "分手":     ["gottman", "attachment-theory", "adler"],
    "带娃":     ["montessori", "attachment-theory", "adler", "carl-rogers"],
    "孩子不听话": ["montessori", "adler", "attachment-theory"],
    "内耗":     ["epictetus", "marcus-aurelius", "seneca", "john-ratey"],
    "焦虑":     ["epictetus", "seneca", "john-ratey", "marcus-aurelius"],
    "累":       ["john-ratey", "cal-newport", "seneca"],
    "没动力":   ["frankl", "inamori", "atomic-habits", "adler"],
    "社恐":     ["adler", "carl-rogers", "nonviolent-communication"],
    "被裁":     ["frankl", "su-shi", "nietzsche", "dalio"],
    "加班":     ["cal-newport", "drucker", "jobs"],
    "学不会":   ["feynman", "ericsson", "mao"],
    "记不住":   ["feynman", "ericsson"],
    "选择困难": ["munger", "buffett", "jobs"],
}


def _syn(slug):
    """按 slug 反查它被哪些口语词指向。"""
    return "".join(k for k, slugs in SYNONYMS.items() if slug in slugs)


def _hwx_payload():
    import json, sys as _s, re
    _s.path.insert(0, "seo")
    import hw_chapters as C, hw_slugs, build_seo

    line_by = {}
    for pname, spec in C.PARENTS.items():
        for it in spec.get("items", []):
            line_by[(pname, it["k"])] = it.get("line", "")

    def best_q(ch, maxlen=34):
        qs = [re.sub(r"==", "", q).strip().rstrip("。") for q in ch.get("q", [])]
        fit = [q for q in qs if 8 <= len(q) <= maxlen]
        return max(fit, key=len) if fit else (qs[0] if qs else "")

    def scene_of(ch):
        """apply 里的「局面：…」句——这句话说的正是「什么时候用得上」。"""
        m = re.search(r"局面：(.+?)(?:\n|$)", ch.get("apply", ""))
        return m.group(1).strip().rstrip("。") if m else ""

    def gloss_of(ch):
        """金句解析：一句自然话，说清「什么时候这句话用得上」。

        材料取自章节已有的 apply「局面」句，只补一个「用在……的时候」的壳，
        不另造内容。"""
        sc = scene_of(ch)
        if not sc:
            return {"pt": ch.get("w", ""), "when": "", "gl": ""}
        tail = "" if sc.endswith(("时", "时候")) else "的时候"
        return {"pt": ch.get("w", ""), "when": sc, "gl": "用在" + sc + tail + "。"}

    E, ch_by = [], {}
    for ch in C.CHAPTERS:
        ch_by.setdefault(ch["parent"], []).append((ch["k"], ch["n"], ch["w"]))
    for e in build_seo.load_array():
        slug = hw_slugs.slug_for(e["n"])
        chs = ch_by.get(e["n"], [])
        hook = next((line_by.get((e["n"], k), "") for k, _, _ in chs if line_by.get((e["n"], k))), "")
        it = HWX_INTROS.get(slug, "")
        if not it:
            it = (e.get("d", "").split("。")[0])[:38]
            print("HWX 警告：%s 缺手写介绍" % slug)
        # 搜索索引：并入该条目所有章节的标题、角度、金句与正文关键词，
        # 使「止损」「复利」这类只在正文出现的词也能搜到。
        body = []
        first_ch = next((c for c in C.CHAPTERS if c["parent"] == e["n"]), None)
        for ch in C.CHAPTERS:
            if ch["parent"] != e["n"]:
                continue
            body.append(ch["n"]); body.append(ch.get("w", ""))
            body.append(re.sub(r"==", "", ch.get("story", "")))
            body.append(re.sub(r"==", "", ch.get("apply", "")))
            for f in ch.get("f", []):
                body.append(f.get("n", "")); body.append(f.get("d", ""))
            for q in ch.get("q", []):
                body.append(re.sub(r"==", "", q))
        E.append({"n": e["n"], "s": slug, "c": e["c"], "w": e["w"], "it": it, "hk": hook,
                  "nc": len(chs), "c0": chs[0][1] if chs else "",
                  "cs": [n for _, n, _ in chs[:3]] if len(chs) >= 3 else [],
                  "sc": scene_of(first_ch) if first_ch else "",
                  "pt": first_ch.get("w", "") if first_ch else "",
                  "ix": (re.sub(r"[\s，。、；：！？「」（）——…]+", "", " ".join(body))[:900]
                         + _syn(slug))})

    # 金句池：每章取 8-34 字里最长一条，带出处深链
    QP = []
    for ch in C.CHAPTERS:
        q = best_q(ch)
        if not q: continue
        g = gloss_of(ch)
        QP.append({"q": q, "who": ch["parent"], "cn": ch["n"],
                   "pt": g["pt"], "when": g["when"], "gl": g["gl"],
                   "u": "/i/%s/%s/" % (hw_slugs.slug_for(ch["parent"]), ch["k"])})

    # 问题卡：10 张第一人称问句
    def ref(slug, k):
        ch = next(c for c in C.CHAPTERS if hw_slugs.slug_for(c["parent"]) == slug and c["k"] == k)
        return {"who": ch["parent"], "cn": ch["n"], "u": "/i/%s/%s/" % (slug, k)}
    QQ = [
        {"t": "方案被毙了，还要不要提第二次？", "r": [ref("su-yu","daring-to-state"), ref("franklin","never-say-certainly")]},
        {"t": "连赢三把，加仓还是收手？",      "r": [ref("art-of-worldly-wisdom","quit-while-winning"), ref("bismarck","art-of-the-possible")]},
        {"t": "亏着的仓位，砍还是扛？",        "r": [ref("livermore","hope-and-fear-inverted"), ref("lynch","stomach-not-brain")]},
        {"t": "对面比我强十倍，怎么打？",       "r": [ref("napoleon","decisive-point"), ref("mao","on-protracted-war")]},
        {"t": "被当众激怒，第一反应做什么？",   "r": [ref("epictetus","judgments-not-things"), ref("zhang-liang","picking-up-the-shoe")]},
        {"t": "团队同一个错犯第三遍了，怪谁？", "r": [ref("thinking-in-systems","structure-drives-behavior"), ref("han-feizi","not-counting-on-goodness")]},
        {"t": "看不清方向的时候，先做什么？",   "r": [ref("marks","taking-the-temperature"), ref("einstein","formulating-the-problem")]},
        {"t": "这个人能不能信？",              "r": [ref("analects","see-how"), ref("zeng-guofan","recruit-and-test")]},
        {"t": "从零开始，第一步做重的还是轻的？","r": [ref("paul-graham","dont-scale"), ref("zhu-yuanzhang","delay-the-title")]},
        {"t": "现在是该退场的时候吗？",         "r": [ref("fan-li","leave-at-the-top"), ref("guo-ziyi","open-gates")]},
    ]

    # 处境
    ch_index = {(hw_slugs.slug_for(c["parent"]), c["k"]): c for c in C.CHAPTERS}
    S = []
    for t, grp, questions in HWX_SCENES:
        qs = []
        for qtext, refs in questions:
            answers = []
            for s_, k_ in refs:
                assert (s_, k_) in ch_index, "HWX 场景引用不存在: %s/%s (%s)" % (s_, k_, t)
                c = ch_index[(s_, k_)]
                answers.append({"who": c["parent"], "cn": c["n"],
                                "u": "/i/%s/%s/" % (s_, k_),
                                "hint": line_by.get((c["parent"], k_), "") or c.get("w", "")})
            qs.append({"q": qtext, "a": answers})
        S.append({"t": t, "g": grp, "qs": qs})

    # ASK（apply 里的「先问」句）已删。今日一问改用 QQ 之后它就没有任何读者了，
    # 却仍然随首页发给每一个访客：276 条、114KB 原始 / 45KB gzip，占整页 7%。
    # 和 fail/lesson 是同一种病的反面——那个是写了没人渲染，这个是发了没人读。

    # NC: 40 最新章节（按章节 py 文件 git 首次 commit 时间降序）
    import os, subprocess
    ch_times = {}
    for ch in C.CHAPTERS:
        slug = hw_slugs.slug_for(ch["parent"])
        for cand in ["seo/chapters/%s.py" % slug.replace("-","_"),
                     "seo/chapters/%s.py" % slug.replace("-","")]:
            if os.path.exists(cand):
                try:
                    r = subprocess.run(["git","log","--follow","--format=%at","--",cand],
                                       capture_output=True, text=True)
                    ts = [x for x in r.stdout.strip().split("\n") if x]
                    ch_times[(ch["parent"], ch["k"])] = int(ts[-1]) if ts else 0
                except: ch_times[(ch["parent"], ch["k"])] = 0
                break
    cat_by = {e["n"]: e["c"] for e in build_seo.load_array()}
    recent = sorted(ch_times.items(), key=lambda x: -x[1])[:40]
    NC = []
    for (pname, k), _ in recent:
        ch = next(c for c in C.CHAPTERS if c["parent"] == pname and c["k"] == k)
        slug = hw_slugs.slug_for(pname)
        NC.append({"pn": pname, "cn": ch["n"], "w": ch.get("w",""), "q": best_q(ch),
                   "sc": scene_of(ch),
                   "s": slug, "k": k, "u": "/i/%s/%s/" % (slug, k),
                   "c": cat_by.get(pname,"")})

    # 竖排卡在 158px 窄列里只放得下 4 列，长句会把卡片撑到别人两倍高：
    # 另建一个 ≤24 字的短句池给信息流，长句仍归今日一句与分享卡。
    QS = [q for q in QP if len(q["q"]) <= 20]
    # 问题卡原来只用手写的 10 张，插满就没了。处境层的 114 个问题本身就带答案，
    # 合进来池子扩到 124，频率才提得上去。
    # 问题卡与首页一问共用这个池。补齐 hint（章节一句话）与 sc（apply 的局面句），
    # 手写的那 10 张原本只有 who/cn/u，放到首页大块里会缺两行。
    _apply_sc = {}
    for _c in C.CHAPTERS:
        _m = re.search(r"局面：(.+?)(?:\n|$)", _c.get("apply", ""))
        if _m:
            _apply_sc[(hw_slugs.slug_for(_c["parent"]), _c["k"])] = _m.group(1).strip()
    def _enrich(ans):
        out = []
        for a in ans:
            b = dict(a)
            _key = tuple(a["u"].strip("/").split("/")[1:3])
            if not b.get("hint"):
                _ch = ch_index.get(_key)
                if _ch:
                    b["hint"] = line_by.get((_ch["parent"], _ch["k"]), "") or _ch.get("w", "")
            _sc = _apply_sc.get(_key)
            if _sc:
                b["sc"] = _sc
            out.append(b)
        return out
    QQ_ALL = ([{"t": q["t"], "r": _enrich(q["r"])} for q in QQ]
              + [{"t": q["q"], "r": _enrich(q["a"])} for sc in S for q in sc["qs"]])
    j = json.dumps({"E": E, "QP": QP, "QS": QS, "QQ": QQ_ALL, "S": S,
                    "CC": CAT_COLOR, "CT": CAT_TINT, "CTD": CAT_TINT_D, "NC": NC}, ensure_ascii=False, separators=(",",":")).replace("</","<\\/")
    return j, len(E), len(NC)


def hwx_block():
    j, ne, nnc = _hwx_payload()
    css = r"""
:root{color-scheme:light dark;--paper:#f5f1e8;--ink:#1f1c17;--acc:#a33b2e;--muted:#8a8377;--line:#d8d2c6;--paper2:#eee8da;--card:#faf7f0;--kbg:#1f1c17;--kfg:#f5f1e8;--kmut:#cfc7b8}
@media(prefers-color-scheme:dark){:root{--paper:#171410;--ink:#eae3d4;--acc:#c65f4f;--muted:#9a917f;--line:#3a342a;--paper2:#201c15;--card:#1d1913;--kbg:#eae3d4;--kfg:#171410;--kmut:#5a5344}}
:root[data-theme="light"]{--paper:#f5f1e8;--ink:#1f1c17;--acc:#a33b2e;--muted:#8a8377;--line:#d8d2c6;--paper2:#eee8da;--card:#faf7f0;--kbg:#1f1c17;--kfg:#f5f1e8;--kmut:#cfc7b8}
:root[data-theme="dark"]{--paper:#171410;--ink:#eae3d4;--acc:#c65f4f;--muted:#9a917f;--line:#3a342a;--paper2:#201c15;--card:#1d1913;--kbg:#eae3d4;--kfg:#171410;--kmut:#5a5344}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]){--white:#1d1913;--line-strong:rgba(234,227,212,.22);--ink-30:rgba(234,227,212,.42);--ink-50:rgba(234,227,212,.6)}}
:root[data-theme="dark"]{--white:#1d1913;--line-strong:rgba(234,227,212,.22);--ink-30:rgba(234,227,212,.42);--ink-50:rgba(234,227,212,.6)}
body{background:var(--paper);color:var(--ink)}
.share-btn{background:var(--white)!important;color:var(--ink)!important;border-color:var(--line-strong)!important}
:root[data-theme="dark"] .dot,:root[data-theme="dark"] .hd-en,:root[data-theme="dark"] .kicker,:root[data-theme="dark"] .sec-k{color:#e0705f!important}
:root[data-theme="dark"] body{background:#171410!important;color:#eae3d4!important}
:root[data-theme="dark"] .hd-title,:root[data-theme="dark"] h1,:root[data-theme="dark"] h2,:root[data-theme="dark"] h3{color:#eae3d4!important}
:root[data-theme="dark"] #hwx .tq .dt{color:#e0705f!important}
:root[data-theme="dark"] #hwx .tq .src,:root[data-theme="dark"] #hwx .tq .src a,:root[data-theme="dark"] #hwx .tbox .hint{color:#d9d1c0!important;opacity:1}
:root[data-theme="dark"] #hwx .qc .who,:root[data-theme="dark"] #hwx .pc .it,:root[data-theme="dark"] #hwx .pc .tag,:root[data-theme="dark"] #hwx .pc .ls,:root[data-theme="dark"] #hwx .nc .w,:root[data-theme="dark"] #hwx .nc .pn{color:#a79e8b!important}
:root[data-theme="dark"] #hwx .cf,:root[data-theme="dark"] #hwx .qc .who i,:root[data-theme="dark"] #hwx .nc .pn i,:root[data-theme="dark"] #hwx .seal{color:#ef8b78!important}
:root[data-theme="dark"] #hwx .nb{background:#b8452f!important;color:#fff!important}
:root[data-theme="dark"] #hwx .kc .qm{color:#8a3a2e!important}
#hwx .kc .qm{color:#c4644f}
#hwx-theme{position:fixed;top:14px;right:14px;z-index:9999;width:36px;height:36px;border:1px solid var(--line);background:var(--paper);color:var(--ink);border-radius:50%;font-size:15px;line-height:1;cursor:pointer;display:flex;align-items:center;justify-content:center;box-shadow:0 1px 6px rgba(0,0,0,.10);padding:0}
#hwx-theme:hover{border-color:var(--acc);color:var(--acc)}
#hwx .today{display:grid;grid-template-columns:1.5fr 1fr;gap:14px;margin:18px 0 6px}
@media(max-width:700px){#hwx .today{grid-template-columns:1fr}}
#hwx .tq{border:1px solid var(--line);border-radius:16px;padding:20px 22px;background:transparent;display:flex;flex-direction:column}
#hwx .tq .dt{font-size:12.5px;letter-spacing:.24em;color:var(--acc);font-weight:700;margin-bottom:6px}
#hwx .tq .q{font-family:"Noto Serif SC","Source Han Serif SC","Songti SC","STSong",serif;font-size:clamp(20px,3.6vw,26px);font-weight:700;line-height:1.85;margin-bottom:14px}
#hwx .tq .src{font-size:13.5px;color:var(--muted)}
#hwx .tq .src a{color:var(--acc);text-decoration:none}
#hwx .tq .tgl{font-size:14.5px;line-height:1.75;color:var(--ink);opacity:.72;margin:0 0 10px}
#hwx .tq .acts{display:flex;gap:8px;margin-top:14px}
#hwx .tq .acts button{border:1.5px solid var(--ink);background:transparent;color:var(--ink);border-radius:999px;padding:7px 16px;font-family:inherit;font-size:14px;cursor:pointer}
#hwx .tq .acts .bs{background:var(--ink);color:var(--paper)}
#hwx .askhero{border:1px solid var(--line);border-radius:16px;background:var(--card);padding:20px 18px 16px;margin-bottom:12px}
#hwx .askhero .lb{font-size:11.5px;letter-spacing:.28em;color:var(--acc);font-weight:700;margin-bottom:12px}
#hwx .askhero .said{font-family:"Noto Serif SC","Songti SC",serif;font-size:13px;color:var(--acc);line-height:1.7;margin-bottom:10px}
#hwx .askhero .q{font-family:"Noto Serif SC","Source Han Serif SC","Songti SC","STSong",serif;font-size:21px;font-weight:700;line-height:1.75;margin:0 0 14px}
#hwx .askhero .sc{font-size:13.5px;color:var(--muted);line-height:1.8;margin:0 0 14px;padding-left:12px;border-left:2px solid var(--line)}
#hwx .askhero .go a{display:block;text-decoration:none;color:inherit;border-top:1px dashed var(--line);padding-top:10px;margin-top:8px}
#hwx .askhero .go b{font-family:"Noto Serif SC","Songti SC",serif;font-size:15.5px;display:block}
#hwx .askhero .go i{font-style:normal;font-size:12.5px;color:var(--muted);display:block;margin-top:3px}
#hwx .today .tq{padding:15px 16px}
#hwx .today .tq .q{font-size:17px!important;line-height:1.8!important;margin-bottom:8px!important}
#hwx .today .tq .tgl{display:none}
#hwx .today .tq .acts button{padding:5px 12px;font-size:12.5px;border-width:1px}
#hwx .today .tq .acts .bs{background:var(--ink);color:var(--paper);border-color:var(--ink)}
#hwx .tbox-s{padding:12px 14px}
#hwx .tbox-s b{font-size:15px}
#hwx .tbox-s .hint2{display:none}
#hwx .tcol{display:flex;flex-direction:column;gap:14px}
#hwx .tbox{border:1px solid var(--line);border-radius:16px;padding:14px 16px;flex:1}
#hwx .tbox .lb{font-size:11.5px;letter-spacing:.28em;color:var(--acc);font-weight:700;margin-bottom:6px}
#hwx .tbox a{color:inherit;text-decoration:none;display:block}
#hwx .tbox b{font-family:"Noto Serif SC","Source Han Serif SC","Songti SC","STSong",serif;font-size:16.5px}
#hwx .tbox .hint{display:block;font-size:14.5px;color:var(--ink);opacity:.72;margin-top:4px;line-height:1.65}
#hwx .tbox .hint2{display:block;font-size:14px;color:var(--acc);opacity:.92;margin-top:6px;line-height:1.6}
#hwx .hh{font-family:"Noto Serif SC","Source Han Serif SC","Songti SC","STSong",serif;font-size:21px;font-weight:700;margin:24px 0 10px;letter-spacing:.03em;display:flex;justify-content:space-between;align-items:baseline}
#hwx .hh .ct{font-size:12px;color:var(--muted);font-weight:500}
#hwx .sc{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0 0}
#hwx .scmore{order:9999;flex:0 0 auto;border:1px dashed var(--line);background:transparent;color:var(--acc);border-radius:999px;padding:7px 14px;font-family:inherit;font-size:14.5px;cursor:pointer;white-space:nowrap;line-height:1.6}
#hwx .scmore:hover{border-color:var(--acc)}
/* 组名独占一行。试过与标签同行以省高度，结果组名混在标签流里像半个标签，
   比原来更乱——高度靠「每组只露 2 个」和紧凑的行距来收，不靠挤掉标题。 */
#hwx .scg{flex:0 0 100%;font-family:"Noto Serif SC","Songti SC",serif;font-size:11.5px;color:var(--muted);letter-spacing:.1em;margin:9px 0 -2px;padding:0;line-height:1.4}
#hwx .scg:first-child{margin-top:0}
#hwx .sc{row-gap:7px}
#hwx .sc{flex-wrap:wrap!important;overflow-x:visible!important}
#hwx .sc button{flex:0 0 auto;border:1px solid var(--line);background:transparent;color:inherit;border-radius:999px;padding:7px 14px;font-family:inherit;font-size:14.5px;cursor:pointer;white-space:nowrap}
#hwx .sc button.on{background:var(--ink);color:var(--paper);border-color:var(--ink)}
#hwx .res{display:none;border-left:3px solid var(--acc);padding:4px 0 4px 13px;margin:8px 0 6px}
#hwx .res.on{display:block}
#hwx .res .qz{margin:0 0 14px}
#hwx .res .qz:last-child{margin-bottom:2px}
#hwx .res .qzq{font-family:"Noto Serif SC","Source Han Serif SC","Songti SC","STSong",serif;font-size:16px;font-weight:700;line-height:1.6;margin-bottom:4px}
#hwx .res .qzq::before{content:"？";color:var(--acc);font-weight:900;margin-right:5px}
#hwx .res a{display:block;padding:4px 0 4px 16px;text-decoration:none;color:inherit}
#hwx .res a b{font-family:"Noto Serif SC","Source Han Serif SC","Songti SC","STSong",serif;font-size:15px;font-weight:600}
#hwx .res a span{display:block;font-size:13.5px;color:var(--muted);line-height:1.6}
#hwx .res a:hover b{border-bottom:1px solid}
#hwx .hist{display:none;align-items:center;gap:8px;margin:0 0 14px;font-size:13px}
header.hd{margin-bottom:12px!important}
#hwx .hist .hl{color:var(--acc);font-weight:700;letter-spacing:.1em;flex:0 0 auto}
#hwx .hist .hchips{display:flex;gap:6px;overflow-x:auto;scrollbar-width:none;flex:1}
#hwx .hist .hchips::-webkit-scrollbar{display:none}
#hwx .hist .hchips a{flex:0 0 auto;border:1px solid var(--line);border-radius:999px;padding:4px 11px;color:var(--muted);text-decoration:none;white-space:nowrap}
#hwx .hist .hchips a:hover{color:var(--ink)}
#hwx .hist button{border:none;background:transparent;color:var(--muted);font-family:inherit;font-size:11px;cursor:pointer;flex:0 0 auto}
#hwx .qbar{margin:22px 0 0}
#hwx .qbar input{width:100%;border:1px solid var(--line);background:transparent;color:var(--ink);border-radius:999px;padding:12px 20px;font-family:inherit;font-size:16px;outline:none;transition:border-color .15s}\n#hwx .qbar input:focus{border-color:var(--muted)}
#hwx .qbar input::placeholder{color:var(--muted)}
/* 一行入口：两行结构（标题+计数 / 提示语），替代原先 1049px 的标签目录。
   试过 flex 单行，三段挤在一起且箭头折行——中文没有词间空格，靠 gap 撑不开。 */
#hwx .scline{display:block;width:100%;background:transparent;border:none;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:15px 2px;margin:16px 0 0;cursor:pointer;color:inherit;text-align:left;font-family:inherit}
#hwx .scline b{font-family:"Noto Serif SC","Songti SC",serif;font-size:19px;font-weight:700;margin-right:10px}
#hwx .scline span{font-size:12.5px;color:var(--muted)}
#hwx .scline i{display:block;font-style:normal;margin-top:6px;font-size:13px;color:var(--acc)}
#hwx .tabs2{flex-shrink:0}
#hwx .tabs2{display:flex;gap:0;border-bottom:2px solid var(--line);margin:14px 0 0}
#hwx .tabs2 button{border:none;background:transparent;padding:9px 20px;font-family:"Noto Serif SC","Source Han Serif SC","Songti SC","STSong",serif;font-size:17px;font-weight:600;color:var(--muted);cursor:pointer;border-bottom:3px solid transparent;margin-bottom:-2px}
#hwx .tabs2 button.on{color:var(--ink);border-bottom-color:var(--acc)}
#hwx .cats{display:flex;gap:6px;overflow-x:auto;scrollbar-width:none;margin:10px 0 0}
#hwx .cats::-webkit-scrollbar{display:none}
#hwx .cats button{flex:0 0 auto;border:none;background:transparent;color:var(--muted);font-family:inherit;font-size:14px;cursor:pointer;padding:5px 11px;border-radius:999px}
#hwx .cats button.on{background:var(--line);color:var(--ink)}
/* 处境选择条：两行横滑。76 个处境竖着平铺是 1049px，那正是被废掉的旧目录；
   横滑两行占 78px，一屏能扫到十几个，滑动就能看完全部。
   不放组名——组名与标签同行会混成半个标签（见 DESIGN.md §7），
   改用「按组排序」让相邻的处境自然聚在一起。 */
#hwx .scpick{display:grid;grid-auto-flow:column;grid-template-rows:auto auto;grid-auto-columns:max-content;gap:7px 6px;overflow-x:auto;overscroll-behavior-x:contain;scrollbar-width:none;margin:12px 0 0;padding-bottom:2px}
#hwx .scpick::-webkit-scrollbar{display:none}
#hwx .scpick button{border:1px solid var(--line);background:transparent;color:inherit;border-radius:999px;padding:7px 14px;font-family:inherit;font-size:14.5px;line-height:1.3;cursor:pointer;white-space:nowrap}
#hwx .scpick button.on{background:var(--ink);color:var(--paper);border-color:var(--ink)}
#hwx .feed{columns:150px;column-gap:12px;margin-top:14px}
#hwx .feed>*{break-inside:avoid;width:100%;margin:0 0 12px}
#hwx .nc-feed{columns:150px;column-gap:12px;margin-top:14px}
#hwx .nc-feed>*{break-inside:avoid;width:100%;margin:0 0 12px}
#hwx .pc{display:flex;flex-direction:column;border:1px solid var(--line);border-radius:14px;padding:17px 17px 15px;text-decoration:none;color:inherit;background:var(--tint,var(--card))}
:root[data-theme="dark"] #hwx .pc,:root[data-theme="dark"] #hwx .nc{background:var(--tintd,var(--card))}
/* flex-wrap:wrap 是为了不让右边的小字（条目的 w）把标题挤折行。
   卡片内容宽只有 124px，人名 + 小字超过约 116px 标题就断词——
   而这跟小字多长关系不大：马可·奥勒留(91px)+「克制」(22px) 照样折，
   毛泽东(57px)+「集中优势」(50px) 反而不折。限制小字字数解决不了。
   允许换行之后，放不下的小字自己掉到第二行，标题永远完整。
   实测 60 张卡：折行 9 → 0，卡片中位高 258px 不变。 */
#hwx .pc .r1{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:baseline;gap:8px}
#hwx .pc b{font-family:"Noto Serif SC","Source Han Serif SC","Songti SC","STSong",serif;font-size:19px;line-height:1.45}
#hwx .pc .tag{font-size:12.5px;color:var(--muted);white-space:nowrap;max-width:52%;overflow:hidden;text-overflow:ellipsis;font-style:normal}
#hwx .pc .it{font-size:14px;color:var(--muted);margin:6px 0 9px;line-height:1.65}
#hwx .pc .hk{font-size:15.5px;line-height:1.85;flex:1}
#hwx .pc .hk::before{content:"「"}#hwx .pc .hk::after{content:"」"}
#hwx .pc .ls{font-size:12.5px;color:var(--muted);margin-top:10px;border-top:1px dashed var(--line);padding-top:9px;line-height:1.65}
#hwx .pc .cf{font-size:12.5px;color:var(--acc);margin-top:10px}
#hwx .nc{display:flex;flex-direction:column;border:1px solid var(--line);border-radius:14px;padding:17px 17px 15px;text-decoration:none;color:inherit;background:var(--tint,var(--card))}
#hwx .nc .pn{font-size:13px;color:var(--muted);margin-bottom:5px}
#hwx .nc .pn i{font-style:normal;color:var(--acc)}
#hwx .nc .nb{font-size:11px;background:var(--acc);color:#fff;border-radius:4px;padding:1px 5px;margin-left:5px;vertical-align:1px}
#hwx .nc b{font-family:"Noto Serif SC","Source Han Serif SC","Songti SC","STSong",serif;font-size:19px;line-height:1.45}
#hwx .nc .w{font-size:13px;color:var(--muted);margin:4px 0 10px}
#hwx .nc .q{font-size:15.5px;line-height:1.85}
#hwx .nc .q::before{content:"「"}#hwx .nc .q::after{content:"」"}
#hwx .qc{border-radius:14px;background:var(--paper2);border:1px solid var(--line);padding:17px 15px 14px;display:flex;flex-direction:column;text-decoration:none;color:inherit;position:relative}
#hwx .qc .v{writing-mode:vertical-rl;text-orientation:mixed;height:186px;width:fit-content;max-width:100%;font-family:"Noto Serif SC","Source Han Serif SC","Songti SC","STSong","SimSun",serif;font-size:17px;font-weight:700;line-height:1.85;letter-spacing:.04em;margin:5px auto 12px;overflow:hidden;display:block}
#hwx .qc .v::before{content:"「"}#hwx .qc .v::after{content:"」"}
#hwx .qc .who{font-size:12.5px;color:var(--muted);margin-top:2px}
#hwx .qc .gl{font-size:13px;line-height:1.65;color:var(--ink);opacity:.72;margin:0 0 8px;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
#hwx .qc .who i{font-style:normal;color:var(--acc)}
#hwx .qc .seal{position:absolute;top:13px;right:13px;width:22px;height:22px;border:1.5px solid var(--acc);border-radius:4px;color:var(--acc);font-size:11px;display:flex;align-items:center;justify-content:center}
#hwx .kc{border-radius:14px;background:rgba(163,59,46,.07);border:1px solid rgba(163,59,46,.22);color:var(--ink);padding:16px 16px 14px;display:flex;flex-direction:column}
:root[data-theme="dark"] #hwx .kc{background:rgba(224,112,95,.13);border-color:rgba(224,112,95,.3)}
#hwx .kc{position:relative}
#hwx .kc .seal{position:absolute;top:13px;right:13px;width:22px;height:22px;border:1.5px solid var(--acc);border-radius:4px;color:var(--acc);font-size:11px;display:flex;align-items:center;justify-content:center;font-family:"Noto Serif SC","Songti SC",serif}
#hwx .kc .said{font-size:12px;line-height:1.6;font-family:"Noto Serif SC","Songti SC",serif;margin-bottom:8px;color:var(--acc);padding-right:28px}
#hwx .kc .qm{display:none;font-size:25px;color:var(--acc);font-weight:900;line-height:1}
#hwx .kc .t{font-family:"Noto Serif SC","Source Han Serif SC","Songti SC","STSong",serif;font-size:16.5px;font-weight:700;line-height:1.65;margin:9px 0 12px;flex:1;color:var(--ink)}
#hwx .kc .r a{display:block;font-size:13.5px;color:var(--muted);text-decoration:none;padding:4px 0}
#hwx .kc .r a b{color:var(--ink);font-weight:600}
.dq{display:none!important}
.tabs,#tl-wrap{display:none!important}
.family a{color:inherit;text-decoration:none}
@media(min-width:900px){#hwx .feed,#hwx .nc-feed{columns:230px}}
.hid{display:none!important}
""".strip()

    js = r"""
(function(){
var D=HWXD;
/* 日夜模式：默认跟随系统，点击在 跟随/日间/夜间 之间循环并记住 */
(function(){
  var R=document.documentElement, KEY='hwx_theme';
  function sysDark(){return !!(window.matchMedia&&window.matchMedia('(prefers-color-scheme:dark)').matches)}
  function get(){try{return localStorage.getItem(KEY)||''}catch(e){return ''}}
  function set(v){try{localStorage.setItem(KEY,v)}catch(e){}}
  function eff(){var m=get();return m||(sysDark()?'dark':'light')}
  function paint(){
    var m=eff();
    R.setAttribute('data-theme',m);
    var b=document.getElementById('hwx-theme');
    if(b){b.textContent=(m==='dark'?'\u2600':'\u263e');
          b.setAttribute('title',m==='dark'?'切换到日间':'切换到夜间');}
  }
  paint();
  setTimeout(function(){
    var b=document.getElementById('hwx-theme');
    if(!b)return;
    b.onclick=function(){set(eff()==='dark'?'light':'dark');paint()};
    paint();
  },0);
  if(window.matchMedia){var mq=window.matchMedia('(prefers-color-scheme:dark)');
    if(mq.addEventListener)mq.addEventListener('change',paint);else if(mq.addListener)mq.addListener(paint);}
})();
function esc(s){return(s||'').replace(/&/g,'&amp;').replace(/"/g,'&quot;')}
var _n=new Date(),WD='日一二三四五六';
var day=Math.floor((_n.getTime()-_n.getTimezoneOffset()*60000)/864e5);
/* ── 今日三样 ── */
var qIdx=day%D.QP.length, q1=D.QP[qIdx];
function paintQuote(first){
  q1=D.QP[qIdx];
  /* 页面上不显示日期——它对读者没有用，只是让卡片更花。
     分享卡里仍然带日期，那里日期是有意义的（记录哪天存的）。 */
  document.getElementById('hwx-dt').textContent='今日一句';
  document.getElementById('hwx-tq').textContent='「'+q1.q+'」';
  document.getElementById('hwx-tqs').innerHTML='—— '+q1.who+' · <a href="'+q1.u+'" data-h="'+esc(q1.who+' · '+q1.cn)+'">'+q1.cn+' →</a>';
  var gl=document.getElementById('hwx-tgl');
  if(gl)gl.textContent=q1.gl||'';
}
paintQuote(true);
document.getElementById('hwx-next').onclick=function(){
  qIdx=Math.floor(Math.random()*D.QP.length); paintQuote(false);
};
var p1=D.E[(day*7)%D.E.length];
var tpEl=document.getElementById('hwx-tp');
tpEl.href='/i/'+p1.s+'/';tpEl.setAttribute('data-h',p1.n);
tpEl.innerHTML='<b>'+p1.n+' — '+p1.w+'</b><span class="hint">'+p1.it+'</span>'
  +(p1.sc?'<span class="hint2">什么时候翻开它：'+p1.sc+'</span>':'');
/* 一问不再冲着读者提问，而是「有人也卡在这里」——读者只需认出，不必回答。
   取 QQ 而非 ASK：前者是处境式的人话（「方案被毙了，还要不要提第二次？」），
   后者是 apply 里的自省句（「我真正想缓解的是谁的不安？」），接不上「某某也卡在这里」。 */
var a1=D.QQ[(day*13)%D.QQ.length];
var a1w=(a1.r&&a1.r[0])?a1.r[0].who:'';
document.getElementById('hwx-asaid').textContent=a1w?(a1w+'也卡在同一件事上——'):'有人问：';
document.getElementById('hwx-aq').textContent=a1.t;
/* 局面用第一个答案对应章节的 apply 局面句，没有就不显示 */
var a1sc=(a1.r&&a1.r[0]&&a1.r[0].sc)?a1.r[0].sc:'';
var ascEl=document.getElementById('hwx-asc');
if(a1sc){ascEl.textContent=a1sc;}else{ascEl.style.display='none';}
document.getElementById('hwx-ago').innerHTML=(a1.r||[]).slice(0,2).map(function(r){
  return '<a href="'+r.u+'" data-h="'+esc(r.who+' · '+r.cn)+'"><b>'+r.who+' · '+r.cn+'</b>'
    +(r.hint?'<i>'+r.hint+'</i>':'')+'</a>';}).join('');
/* ── 分享卡 ── */
function drawCard(cb){
  var cv=document.createElement('canvas');cv.width=1080;cv.height=1440;var c=cv.getContext('2d');
  var loaded=0,need=3;function chk(){if(++loaded>=need)render();}
  document.fonts.load('900 128px "Noto Serif SC"').then(chk).catch(chk);
  document.fonts.load('700 58px "Noto Serif SC"').then(chk).catch(chk);
  document.fonts.load('500 34px "Noto Serif SC"').then(chk).catch(chk);
  function render(){
    c.fillStyle='#f5f1e8';c.fillRect(0,0,1080,1440);
    c.strokeStyle='#d8d2c6';c.lineWidth=2;c.strokeRect(46,46,988,1348);
    c.fillStyle='#a33b2e';c.font='900 128px "Noto Serif SC"';c.fillText(String(_n.getDate()),96,232);
    c.fillStyle='#8a8377';c.font='500 34px "Noto Serif SC"';c.fillText((_n.getMonth()+1)+'月 · 星期'+WD[_n.getDay()],100,296);
    c.fillStyle='#9d2933';
    (function(x,y,w){var r=w*0.22;c.beginPath();
      c.moveTo(x+r,y);c.lineTo(x+w-r,y);c.quadraticCurveTo(x+w,y,x+w,y+r);
      c.lineTo(x+w,y+w-r);c.quadraticCurveTo(x+w,y+w,x+w-r,y+w);
      c.lineTo(x+r,y+w);c.quadraticCurveTo(x,y+w,x,y+w-r);
      c.lineTo(x,y+r);c.quadraticCurveTo(x,y,x+r,y);c.closePath();c.fill();})(880,110,104);
    c.fillStyle='#fff';c.font='700 62px "Noto Serif SC"';
    c.textAlign='center';c.fillText('人',932,182);c.textAlign='left';
    c.fillStyle='#1f1c17';c.font='700 58px "Noto Serif SC"';
    var q='「'+q1.q+'」',lines=[],cur='',PUNC='，。、；：！？…」）';
    for(var i=0;i<q.length;i++){var tt=cur+q[i];if(c.measureText(tt).width>880&&PUNC.indexOf(q[i])<0){lines.push(cur);cur=q[i]}else cur=tt}
    if(cur)lines.push(cur);
    var y=560+(5-Math.min(lines.length,5))*46;
    lines.slice(0,6).forEach(function(l){c.fillText(l,100,y);y+=98});
    /* 解析：一句话，画在署名之上；行数按实际内容，不预留空档 */
    var ay=y+46;
    if(q1.gl){
      c.fillStyle='#5f5850';c.font='500 31px "Noto Serif SC"';
      var wl=[],cu='';
      for(var j=0;j<q1.gl.length;j++){var tw=cu+q1.gl[j];
        if(c.measureText(tw).width>860&&PUNC.indexOf(q1.gl[j])<0){wl.push(cu);cu=q1.gl[j]}else cu=tw}
      if(cu)wl.push(cu);
      wl=wl.slice(0,3);
      wl.forEach(function(l){c.fillText(l,100,ay);ay+=46});
    }
    ay+=54;   /* 与上一段空出一行 */
    c.fillStyle='#8a8377';c.font='500 34px "Noto Serif SC"';
    c.textAlign='right';c.fillText('—— '+q1.who+' · '+q1.cn,980,ay);c.textAlign='left';
    c.strokeStyle='#d8d2c6';c.lineWidth=2;c.beginPath();c.moveTo(100,1230);c.lineTo(980,1230);c.stroke();
    c.fillStyle='#1f1c17';c.font='700 34px "Noto Serif SC"';c.fillText('人类世界生存法则',100,1318);
    c.fillStyle='#a33b2e';c.font='500 30px "Noto Serif SC"';c.fillText('OurWord.ai',100,1366);
    var qr=new Image();
    qr.onload=function(){c.drawImage(qr,858,1244,122,122);cv.toBlob(cb,'image/png')};
    qr.onerror=function(){cv.toBlob(cb,'image/png')};
    qr.src='/wechat-qr.png?v=54fb0fdf';
  }
}
document.getElementById('hwx-save').onclick=function(){drawCard(function(b){var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='ourword-'+(_n.getMonth()+1)+'-'+_n.getDate()+'.png';a.click()})};
document.getElementById('hwx-share').onclick=function(){drawCard(function(b){var f=new File([b],'ourword.png',{type:'image/png'});if(navigator.canShare&&navigator.canShare({files:[f]}))navigator.share({files:[f],title:'人类世界生存法则'});else{var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='ourword.png';a.click()}})};
/* ── 处境标签 ── */
var scEl=document.getElementById('hwx-sc'),resEl=document.getElementById('hwx-res');
var scMore=document.getElementById('hwx-scmore');
/* 按组渲染：原来 76 个处境平铺，折叠逻辑按「两行」算，默认只露得出 4 个——
   加多少处境用户都看不见。分组之后每组露前 3 个，默认可见约 30 个。 */
var _seen={};
D.S.forEach(function(s){
  if(s.g && !_seen[s.g]){
    _seen[s.g]=1;
    var h=document.createElement('span');
    h.className='scg';h.textContent=s.g;
    scEl.appendChild(h);
  }
  var b=document.createElement('button');b.type='button';b.textContent=s.t;
  b.dataset.g=s.g||'';
  b._open=function(){
    scEl.querySelectorAll('button').forEach(function(x){x.classList.remove('on')});
    b.classList.add('on');
    resEl.innerHTML=s.qs.map(function(q){
      return '<div class="qz"><div class="qzq">'+q.q+'</div>'
        +q.a.map(function(r){return '<a href="'+r.u+'" data-h="'+esc(r.who+' · '+r.cn)+'"><b>'+r.who+' · '+r.cn+'</b><span>'+(r.hint||'')+'</span></a>'}).join('')
        +'</div>';
    }).join('');
    resEl.classList.add('on');
  };
  b.onclick=function(){
    if(b.classList.contains('on')){          /* 再点已展开的，折叠 */
      b.classList.remove('on');
      resEl.classList.remove('on');resEl.innerHTML='';return;
    }
    b._open();
    resEl.scrollIntoView({behavior:'smooth',block:'nearest'});
  };scEl.appendChild(b);
});

/* 默认只露两行，其余收起 */
(function(){
  var open=false;
  function tags(){return Array.prototype.filter.call(
    scEl.querySelectorAll('button'),function(b){return b!==scMore})}
  function showAll(){tags().forEach(function(b){b.style.display=''})}
  var PER_GROUP=2;   /* 每组默认露几个——14 组 × 3 个占了 1268px，近两屏 */
  function heads(){return Array.prototype.slice.call(scEl.querySelectorAll('.scg'))}
  function fold(){
    if(open){
      showAll();heads().forEach(function(h){h.style.display=''});
      scMore.textContent='收起';return;
    }
    showAll();
    scMore.textContent='展开全部 '+D.S.length+' 个';
    /* 每组只留前 PER_GROUP 个；组标题始终显示，让用户知道底下还有 */
    var count={};
    tags().forEach(function(b){
      var g=b.dataset.g||'';
      count[g]=(count[g]||0)+1;
      if(count[g]>PER_GROUP)b.style.display='none';
    });
    heads().forEach(function(h){h.style.display=''});
  }
  scMore.onclick=function(){open=!open;fold()};
  fold();
  window.addEventListener('resize',function(){if(!open)fold()});
  /* 默认展开第一个处境。用 open() 而不是 click()：
     click 会走「已选中则折叠」这条分支，导致用户点第二个标签时
     第一下只是取消展开，要点两下才切换。 */
  var first=tags()[0]; if(first && first._open) first._open();
})();
/* ── 历史行 ── */
var _mem=[];
function hload(){try{return JSON.parse(localStorage.getItem('hwx_hist')||'[]')}catch(e){return _mem}}
function hsave(a){_mem=a;try{localStorage.setItem('hwx_hist',JSON.stringify(a))}catch(e){}}
function hrender(){
  var a=hload(),el=document.getElementById('hwx-hist');
  if(!a.length){el.style.display='none';return}
  el.style.display='flex';
  document.getElementById('hwx-hchips').innerHTML=a.slice(0,20).map(function(x){return '<a href="'+x.u+'">'+x.t+'</a>'}).join('');
}
document.addEventListener('click',function(ev){
  var a=ev.target.closest&&ev.target.closest('a[data-h]');if(!a)return;
  var rec=hload().filter(function(x){return x.u!==a.getAttribute('href')});
  rec.unshift({u:a.getAttribute('href'),t:a.getAttribute('data-h')});
  hsave(rec.slice(0,50));hrender();
});
document.getElementById('hwx-hclr').onclick=function(){hsave([]);hrender()};
hrender();
/* ── 类别筛选 ── */
var CAT='全部';
var cw=document.getElementById('hwx-cats');
var cats=['全部'];D.E.forEach(function(e){if(cats.indexOf(e.c)<0)cats.push(e.c)});
cats.forEach(function(c){
  var b=document.createElement('button');b.textContent=c;if(c===CAT)b.classList.add('on');
  b.onclick=function(){CAT=c;cw.querySelectorAll('button').forEach(function(x){x.classList.toggle('on',x.textContent===c)});applyFeed()};
  cw.appendChild(b);
});
/* ── CTA 差异化 ── */
function cta(e){
  var T=['拆开看他的 '+e.nc+' 套打法 →','先读「'+(e.c0||'')+'」→','他的答案分 '+e.nc+' 篇讲透 →','进去偷师 →',
         '从「'+(e.c0||'')+'」进 →',e.nc+' 篇，句句能落地 →','看他怎么处理最难的那件事 →','带走 '+e.nc+' 条硬原则 →',
         '深读 '+e.nc+' 篇，够用很久 →','「'+(e.c0||'')+'」值得先看 →','他的方法都在里面 →','读透这 '+e.nc+' 篇再走 →',
         '看完你会换个打法 →',e.nc+' 篇深读备好了 →','从最狠的一篇读起 →','他的路数，'+e.nc+' 篇拆完 →'];
  var h=0;for(var i=0;i<e.s.length;i++)h=(h*31+e.s.charCodeAt(i))>>>0;
  var t=T[h%T.length];
  return(t.indexOf('「」')>=0)?'他的方法都在里面 →':t;
}
/* ── 全部 feed（混排） ── */
/* 金句取用器：按日期确定性洗牌后顺序发牌。
   原来用 (i*步长)%池大小 取句，步长 53 撞上池大小 53 时恒取第一条——
   两个 feed 里十张金句卡全是同一句。改成发牌就不再依赖两个数互质。 */
var _qbag=[], _qi2=0;
(function(){
  var a=D.QS.slice(), seed=day;
  for(var i=a.length-1;i>0;i--){
    seed=(seed*9301+49297)%233280;
    var j=Math.floor(seed/233280*(i+1));
    var t=a[i];a[i]=a[j];a[j]=t;
  }
  _qbag=a;
})();
function pickQ(){ var g=_qbag[_qi2 % _qbag.length]; _qi2++; return g; }
/* 金句卡：竖排金句 + 出处 + 一行解析（角度 · 什么时候用），解析取自章节自身字段 */
function qcard(g,cls){
  var gl = g.gl ? ('<span class="gl">'+g.gl+'</span>') : '';
  return '<a class="qc '+cls+'" href="'+g.u+'" data-h="'+esc(g.who+' · '+g.cn)+'" data-t="'+esc((g.q+g.who+g.cn+(g.gl||'')).toLowerCase())+'">'
    +'<span class="seal">句</span><span class="v">'+g.q+'</span>'
    + gl + '<span class="who"><i>'+g.who+'</i> · '+g.cn+'</span></a>';
}
/* 章节标题与角度并入搜索索引：搜「止损」应命中利弗莫尔等 */
var byNC={};D.NC.forEach(function(n){(byNC[n.pn]=byNC[n.pn]||[]).push(n.cn+' '+n.w+' '+n.q)});
D.S.forEach(function(sc){sc.qs.forEach(function(q){q.a.forEach(function(r){(byNC[r.who]=byNC[r.who]||[]).push(q.q+' '+r.cn+' '+(r.hint||''))})})});
D.QP.forEach(function(q){(byNC[q.who]=byNC[q.who]||[]).push(q.cn+' '+q.q)});
var fullCells=[];
var qi=0,ki=0;
D.E.forEach(function(e,i){
  var chTxt=(byNC[e.n]||[]).join(' ');
  var dt=esc((e.n+' '+e.w+' '+e.c+' '+e.it+' '+e.hk+' '+chTxt+' '+(e.ix||'')).toLowerCase());
  fullCells.push('<a class="pc" href="/i/'+e.s+'/" data-h="'+esc(e.n)+'" data-c="'+e.c+'" data-t="'+dt+'" style="--tint:'+(D.CT[e.c]||'transparent')+';--tintd:'+(D.CTD[e.c]||'transparent')+'"><span class="r1"><b>'+e.n+'</b><i class="tag">'+e.w+'</i></span><span class="it">'+e.it+'</span><span class="hk">'+(e.hk||e.w)+'</span>'+(e.cs.length?'<span class="ls">'+e.cs.join(' / ')+'</span>':'')+'<span class="cf">'+cta(e)+'</span></a>');
  if(i%3===2){var g=pickQ();
    fullCells.push(qcard(g,'xtra'));}
  if(i%5===3){var k=D.QQ[ki++%D.QQ.length];
    fullCells.push('<div class="kc xtra" data-t="'+esc(k.t.toLowerCase())+'"><span class="seal">问</span>'+(k.r&&k.r[0]?'<span class="said">'+esc(k.r[0].who)+'问过</span>':'')+'<span class="t">'+k.t+'</span><span class="r">'+k.r.map(function(r){return '<a href="'+r.u+'" data-h="'+esc(r.who+' · '+r.cn)+'"><b>'+r.who+'</b> · '+r.cn+' →</a>'}).join('')+'</span></div>');}
});
/* ── 最新 feed ── */
/* 最新 tab 混排：每 4 张深度阅读插 1 张人物/书卡、1 张金句卡，每 9 槽插 1 张问题卡 */
var ncCells=[], _seen={}, _pi=0, _qi=0, _ki=0;
var byName={}; D.E.forEach(function(e){byName[e.n]=e});
D.NC.forEach(function(e,i){
  ncCells.push('<a class="nc" href="'+e.u+'" data-h="'+esc(e.pn+' · '+e.cn)+'" style="--tint:'+(D.CT[e.c]||'transparent')+';--tintd:'+(D.CTD[e.c]||'transparent')+'"><span class="pn"><i>'+e.pn+'</i><span class="nb">新</span></span><b>'+e.cn+'</b><span class="w">'+e.w+'</span>'+(e.q?'<span class="q">'+e.q+'</span>':'')+'</a>');
  if(i%4===3){
    var pe=null;
    for(var t=0;t<D.NC.length&&!pe;t++){
      var cand=byName[D.NC[(_pi+t)%D.NC.length].pn];
      if(cand&&!_seen[cand.s]){pe=cand;_pi=(_pi+t+1)%D.NC.length}
    }
    if(pe){_seen[pe.s]=1;
      ncCells.push('<a class="pc" href="/i/'+pe.s+'/" data-h="'+esc(pe.n)+'" style="--sp:'+(D.CC[pe.c]||'#999')+'"><span class="r1"><b>'+pe.n+'</b><i class="tag">'+pe.w+'</i></span><span class="it">'+pe.it+'</span><span class="hk">'+(pe.hk||pe.w)+'</span><span class="cf">'+cta(pe)+'</span></a>');}
    var g=pickQ();
    ncCells.push(qcard(g,''));
  }
  if(i%5===4){var k=D.QQ[_ki++%D.QQ.length];
    ncCells.push('<div class="kc"><span class="seal">问</span>'+(k.r&&k.r[0]?'<span class="said">'+esc(k.r[0].who)+'问过</span>':'')+'<span class="t">'+k.t+'</span><span class="r">'+k.r.map(function(r){return '<a href="'+r.u+'" data-h="'+esc(r.who+' · '+r.cn)+'"><b>'+r.who+'</b> · '+r.cn+' →</a>'}).join('')+'</span></div>');}
});
/* ── 处境 tab：每个问题一张卡，标注所属处境 ──
   原来「按处境找」是 1049px 的标签目录，三步才到答案，
   而这些问题 100% 已经在信息流里以卡片出现过。改成卡片流：
   同一批内容、同一套视觉，扫读即认出，不必先学会我们的分类。 */
var scCells=[],scOwner=[];
D.S.forEach(function(sc){
  sc.qs.forEach(function(q){
    scOwner.push(sc.t);
    scCells.push('<div class="kc" data-t="'+esc((q.q+sc.t).toLowerCase())+'">'
      +'<span class="seal">问</span>'
      +'<span class="said">'+esc(sc.t)+'</span>'
      +'<span class="t">'+q.q+'</span>'
      +'<span class="r">'+q.a.map(function(r){
          return '<a href="'+r.u+'" data-h="'+esc(r.who+' · '+r.cn)+'"><b>'+r.who+'</b> · '+r.cn+' →</a>'
        }).join('')+'</span></div>');
  });
});
/* ── 埋点：只发聚合信息，不发用户输入的原文以外的任何东西 ── */
function trk(name, params){
  try{ if(window.gtag) gtag('event', name, params||{}); }catch(e){}
}
/* ── 标签页切换 ── */
var TAB='新';
var feed=document.getElementById('hwx-feed'), ncfeed=document.getElementById('hwx-ncfeed');
var scfeed=document.getElementById('hwx-scfeed');
var scpick=document.getElementById('hwx-scpick');
/* 选中的处境；空串＝全部。选择保留，切走再切回来还在原来那一格 */
var SCSEL='';
/* 把选中的标签滑进视野：选择会跨 tab 保留，切回来时条子若停在开头，
   卡片是筛过的而标签看着像没选，人会以为坏了。 */
function scReveal(){
  var on=scpick.querySelector('button.on');
  if(on&&on.scrollIntoView)try{on.scrollIntoView({inline:'center',block:'nearest'})}catch(e){}
}
function scRender(){
  var cells=[],n=0;
  for(var i=0;i<scCells.length;i++){
    if(!SCSEL||scOwner[i]===SCSEL){cells.push(scCells[i]);n++;}
  }
  scfeed.innerHTML=cells.join('');
  ct.textContent=n+' 个问题';   /* 处境名由选中的标签表达，不再重复一遍 */
}
function scBuild(){
  var h=['<button type="button" data-s="" class="on">全部</button>'];
  D.S.forEach(function(sc){h.push('<button type="button" data-s="'+esc(sc.t)+'">'+esc(sc.t)+'</button>')});
  scpick.innerHTML=h.join('');
  scpick.querySelectorAll('button').forEach(function(b){
    b.onclick=function(){
      var v=b.getAttribute('data-s');
      SCSEL=(v===SCSEL)?'':v;                       /* 再点一次＝取消，回到全部 */
      scpick.querySelectorAll('button').forEach(function(x){
        x.classList.toggle('on',x.getAttribute('data-s')===SCSEL)});
      trk('situation_pick',{situation:SCSEL||'all'});
      scRender();
    };
  });
}
var ct=document.getElementById('hwx-ct');
var catsRow=document.getElementById('hwx-cats');
function switchTab(t){
  TAB=t;
  document.querySelectorAll('#hwx-tabs2 button').forEach(function(b){b.classList.toggle('on',b.getAttribute('data-t')===t)});
  if(t==='新'){
    feed.style.display='none';scfeed.style.display='none';ncfeed.style.display='';catsRow.style.display='none';
    scpick.style.display='none';
    ncfeed.innerHTML=ncCells.join('');ct.textContent=D.NC.length+' 篇最新';
  }else if(t==='境'){
    ncfeed.style.display='none';feed.style.display='none';catsRow.style.display='none';
    scfeed.style.display='';scpick.style.display='';
    if(!scpick.firstChild)scBuild();
    scRender();scReveal();
  }else{
    ncfeed.style.display='none';scfeed.style.display='none';feed.style.display='';catsRow.style.display='';
    scpick.style.display='none';
    feed.innerHTML=fullCells.join('');applyFeed();
  }
}
document.querySelectorAll('#hwx-tabs2 button').forEach(function(b){
  b.onclick=function(){var t=b.getAttribute('data-t');
    trk('tab_switch',{tab:t==='新'?'latest':(t==='全'?'all':'situations')});
    switchTab(t)};
});
function applyFeed(){
  if(!feed||!ct)return;
  var v=(document.getElementById('q')||{value:''}).value.trim().toLowerCase(),vis=0;
  feed.querySelectorAll('.pc').forEach(function(c){
    var ok=(CAT==='全部'||c.getAttribute('data-c')===CAT)&&(!v||c.getAttribute('data-t').indexOf(v)>=0);
    c.classList.toggle('hid',!ok);if(ok)vis++;
  });
  feed.querySelectorAll('.xtra').forEach(function(c){
    c.classList.toggle('hid',CAT!=='全部'||!!(v&&c.getAttribute('data-t')&&c.getAttribute('data-t').indexOf(v)<0));
  });
  ct.textContent=vis+' 条知识';
}
/* 搜索框接管 */
var qin=document.getElementById('q');
if(qin){qin.oninput=null;
  /* 搜索落空记录：这是三个埋点里最值钱的一个——用户搜了什么、我们没有，
     直接告诉我们该补什么内容，比坐着推理准得多。
     只在停止输入 1.2 秒后发一次，避免把「睡」「睡不」「睡不着」都记下来。 */
  var _mt=null, _lastMiss='';
  qin.addEventListener('input',function(){
    if(qin.value.trim()&&TAB!=='全'){switchTab('全');}   /* 搜索一律在「全部」里进行 */
    else{applyFeed();}
    clearTimeout(_mt);
    _mt=setTimeout(function(){
      var v=qin.value.trim();
      if(v.length<2||v===_lastMiss)return;
      var n=parseInt((document.getElementById('hwx-ct').textContent||'0'),10)||0;
      _lastMiss=v;
      if(n===0) trk('search_miss',{term:v.slice(0,40)});
      else trk('search_hit',{term:v.slice(0,40), results:n});
    },1200);
  });}
/* 初始化 */
/* 一行入口：点它切到「处境」tab，不再就地展开 1049px 的标签目录 */
(function(){
  var line=document.getElementById('hwx-scline');
  if(!line)return;
  var n=0; D.S.forEach(function(x){n+=x.qs.length});
  var c=document.getElementById('hwx-sccount');
  if(c)c.textContent=D.S.length+' 种处境 · '+n+' 个问题';
  line.onclick=function(){
    trk('situation_entry_click',{});
    switchTab('境');
    document.getElementById('hwx-tabs2').scrollIntoView({behavior:'smooth',block:'start'});
  };
})();
/* 卡片点击：用委托，三个 feed 一处覆盖。只记卡片类型和去向，不记内容。 */
['hwx-ncfeed','hwx-feed','hwx-scfeed'].forEach(function(id){
  var el=document.getElementById(id); if(!el)return;
  el.addEventListener('click',function(e){
    var a=e.target.closest('a[href^="/i/"]'); if(!a)return;
    var card=e.target.closest('.pc,.nc,.qc,.kc');
    var kind=card?(card.classList.contains('kc')?'question':
              card.classList.contains('qc')?'quote':
              card.classList.contains('nc')?'chapter':'person'):'other';
    trk('card_click',{card_type:kind, feed:id.replace('hwx-',''), dest:a.getAttribute('href')});
  },true);
});
/* 处境层展开区的答案点击 */
(function(){
  var r=document.getElementById('hwx-res'); if(!r)return;
  r.addEventListener('click',function(e){
    var a=e.target.closest('a[href^="/i/"]'); if(!a)return;
    trk('card_click',{card_type:'situation_answer', feed:'res', dest:a.getAttribute('href')});
  },true);
})();
/* 今日一问的答案点击 */
(function(){
  var g=document.getElementById('hwx-ago'); if(!g)return;
  g.addEventListener('click',function(e){
    var a=e.target.closest('a[href^="/i/"]'); if(!a)return;
    trk('card_click',{card_type:'daily_question', feed:'hero', dest:a.getAttribute('href')});
  },true);
})();
switchTab('新');
})();
""".strip()

    html = (
        HWX_A + "\n"
        "<link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500;600;700;900&display=swap\">\n"
        "<style>" + css + "</style>\n"
        "<section id=\"hwx\">\n"
        "<button id=\"hwx-theme\" type=\"button\" aria-label=\"切换日夜模式\"></button>\n"
        "<div class=\"hist\" id=\"hwx-hist\"><span class=\"hl\">最近看过</span>"
        "<span class=\"hchips\" id=\"hwx-hchips\"></span><button id=\"hwx-hclr\">清空</button></div>"
        "<div class=\"askhero\" id=\"hwx-askhero\">""<div class=\"lb\">今日一问</div>""<div class=\"said\" id=\"hwx-asaid\"></div>""<div class=\"q\" id=\"hwx-aq\"></div>""<div class=\"sc\" id=\"hwx-asc\"></div>""<div class=\"go\" id=\"hwx-ago\"></div>""</div>""<div class=\"today\">"
        "<div class=\"tq\"><div class=\"dt\" id=\"hwx-dt\"></div><div class=\"q\" id=\"hwx-tq\"></div>"
        "<div class=\"tgl\" id=\"hwx-tgl\"></div><div class=\"src\" id=\"hwx-tqs\"></div>"
        "<div class=\"acts\"><button id=\"hwx-next\">换一换</button>"
        "<button class=\"bs\" id=\"hwx-save\">保存卡片</button>"
        "<button id=\"hwx-share\">分享</button></div></div>"
        "<div class=\"tcol\">"
        "<div class=\"tbox tbox-s\"><div class=\"lb\">今日一篇</div><a id=\"hwx-tp\"></a></div>"
        "</div></div>"
        "<button class=\"scline\" id=\"hwx-scline\" type=\"button\">"
        "<b>按处境找</b><span id=\"hwx-sccount\"></span>"
        "<i>「我现在遇到的是……」→</i></button>"
        "<div class=\"sc\" id=\"hwx-sc\" style=\"display:none\">"
        "<button class=\"scmore\" id=\"hwx-scmore\" type=\"button\"></button></div>"
        "<div class=\"res\" id=\"hwx-res\" style=\"display:none\"></div>"
                "<div class=\"qbar\"><input id=\"q\" placeholder=\"搜索：人物、书、一句话、处境…\" aria-label=\"搜索\"></div>"
        "<div style=\"display:flex;align-items:baseline;justify-content:space-between;margin-top:14px\">"
        "<div class=\"tabs2\" id=\"hwx-tabs2\">"
        "<button data-t=\"新\" class=\"on\">最新</button><button data-t=\"全\">全部</button>"
        "<button data-t=\"境\">处境</button></div>"
        "<span class=\"ct\" id=\"hwx-ct\" style=\"font-size:12px;color:var(--muted);white-space:nowrap;flex:0 0 auto\"></span></div>"
        "<div class=\"cats\" id=\"hwx-cats\" style=\"display:none\"></div>"
        "<div class=\"scpick\" id=\"hwx-scpick\" style=\"display:none\" role=\"group\" aria-label=\"按处境筛选\"></div>"
        "<div class=\"nc-feed\" id=\"hwx-ncfeed\"></div>"
        "<div class=\"feed\" id=\"hwx-feed\" style=\"display:none\"></div><div class=\"nc-feed\" id=\"hwx-scfeed\" style=\"display:none\"></div>"
        # 悬浮球问答不在这里注入——它要出现在每一页，由 patch_chat_widget() 统一挂。
        "<script>var HWXD=" + j + ";</script>"
        "<script>" + js + "</script>"
        "\n</section>\n" + HWX_B
    )
    return html


def patch_home_discover():
    import re
    p = "index.html"
    s = open(p, encoding="utf-8").read()
    s = re.sub(r"\n*" + re.escape(HWX_A) + r".*?" + re.escape(HWX_B) + r"\n*", "", s, flags=re.S)
    # 时间轴已隐藏，遗留的 renderTL 仍在找已删除的计数节点并抛错——让它安全空转
    # 时间轴已隐藏；老 renderTL/rTabs 仍在启动时访问被移除的节点并抛错。
    # stub 会被后面的函数声明覆盖，所以直接把函数体改成空转。
    s = s.replace('function renderTL(){\n  rTabs();',
                  'function renderTL(){\n  return;', 1)
    # 655KB 的汇文明朝体只被旧金句卡（.dq，早已隐藏）用到，首页却无条件加载它——
    # 实测拖慢首屏 4.6 秒，而首次绘制其实只要 0.6 秒。改成运行时按需注入：
    # 只有真的要画旧金句卡时才插入 @font-face，平时一个字节都不下载。
    s = s.replace(
        '@font-face{font-family:"Huiwen-mincho";src:url("hw-mincho-subset.woff2") format("woff2");font-display:swap}',
        '')
    if "__hwFont=function" not in s:   # 幂等：重复构建不叠加
        s = s.replace('<body', '<script>window.__hwFont=function(){'
                      'if(window.__hwFontDone)return;window.__hwFontDone=1;'
                      'var st=document.createElement("style");'
                      'st.textContent=\'@font-face{font-family:"Huiwen-mincho";'
                      'src:url("/hw-mincho-subset.woff2") format("woff2");font-display:swap}\';'
                      'document.head.appendChild(st)};</script><body', 1)
    # 旧金句卡真要用时先注入
    if "if(window.__hwFont)window.__hwFont();" not in s:   # 幂等
        s = s.replace("function dqFont(){",
                      "function dqFont(){\n  if(window.__hwFont)window.__hwFont();", 1)
    # .dq 区块早已隐藏，但它的初始化仍在启动时调用 dqFont() 预取 655KB 字体。
    # 首屏因此从 0.6 秒拖到 4.6 秒。去掉这次预取，字体只在真要画卡时才下载。
    s = s.replace("dqRender();dqFont().then(", "dqRender();Promise.resolve().then(", 1)
    # 二维码换新后文件名不变，浏览器会用旧缓存——按内容哈希击穿
    s = re.sub(r'(wechat-qr\.png)(\?v=[0-9a-f]+)?', r'\1?v=54fb0fdf', s)
    # 文案兜底：每轮构建强制生效，防止 rebase / 其他脚本回写旧值
    s = s.replace("95 位人物与典籍", "100 位人物与典籍")
    # 条目数写死过三次（95 → 100 → 现在），每次加条目都漏改。改成按实际数量回写：
    # 详情页的 slogan 早就是自动的，首页却一直是手填的。
    import sys as _s2
    _s2.path.insert(0, "seo")
    import build_seo as _bs
    _n = len(_bs.load_array())
    s = re.sub(r"<title>人类世界生存法则[^<]*</title>",
               "<title>人类世界生存法则 — %d 位人物与典籍的生存智慧</title>" % _n, s)
    # 标语从「装了什么」改成「能拿来干嘛」——前者让人把它归类成一个收藏，
    # 后者才让人知道现在就能用。
    s = re.sub(r"[\d]+ [个位]人物与典籍的生存智慧，跨越 2600 年", "%s" % SLOGAN_TEXT, s)
    s = re.sub(r"[\d]+ [个位]人物与典籍的生存智慧", "%s" % SLOGAN_TEXT, s)
    s = re.sub(r"(\d+) 位人物与典籍(?=[，、])",
               "%d 位人物与典籍" % _n, s)
    s = s.replace("人类文明的坐标，照亮千年的灯塔",
                  SLOGAN_TEXT)
    # logo 旁的标语已经写了「115 个人物与典籍的生存智慧，跨越 2600 年」，
    # 下面那排 stats 是同一句话拆成三块再说一遍——删掉，并收紧页头下方留白。

    # 页头所在的 .wrap 有 80px 下内距（原本给 stats 和旧内容留的），删掉 stats 后
    # 这块空白就孤零零挂在 logo 下面。只收含页头的那一个 wrap。
    s = s.replace('  .wrap{padding:0 24px 80px}', '  .wrap{padding:0 24px 8px}')
    s = s.replace('.hd-stats{display:flex;gap:20px;flex-wrap:wrap;align-items:center}',
                  '.hd-stats{display:none}')
    # stats 撤掉后页头留下一块空白（它原来撑着高度），把页头的上下留白一并收回
    s = s.replace('#hwx .hist{display:none;align-items:center;gap:8px;margin:2px 0 4px;font-size:13px}',
                  '#hwx .hist{display:none;align-items:center;gap:8px;margin:2px 0 4px;font-size:13px}\n'
                  'header.hd{padding:20px 0 4px!important;margin:0 0 6px!important}\n'
                  'header.hd .brand-lockup,header.hd .brand{margin-bottom:0!important}\n'
                  '#hwx{margin-top:0}')
    # 页头样式改了，升版本号击穿浏览器缓存
    s = s.replace("hw-home-lockup.css?v=2", "hw-home-lockup.css?v=3")
    # stats 节点删了，但仍有代码往 #st / #cat-count 写数——加空值保护
    s = s.replace("document.getElementById('st').textContent=D.length",
                  "(document.getElementById('st')||{}).textContent=D.length")
    s = s.replace("document.getElementById('cat-count').textContent=CATS.length-2",
                  "(document.getElementById('cat-count')||{}).textContent=CATS.length-2")
    # 页头精简：删掉「古今中外 · 东西并观」与页头分享按钮，位置让给「最近看过」
    s = re.sub(r'<span[^>]*>\s*古今中外[^<]*</span>', '', s)
    s = re.sub(r'<button class="share-btn"[^>]*>.*?</button>', '', s, flags=re.S, count=1)
    s = s.replace("古今中外 · 东西并观", "")
    # 去掉 hw-share.js 重复加载
    s = re.sub(r'(?:<script src="/assets/hw-share\.js" defer></script>\s*)+',
               '<script src="/assets/hw-share.js" defer></script>\n', s)
    # noscript h1 降 h2
    s = re.sub(r"(<noscript>)(.*?)(</noscript>)",
               lambda m: m.group(1) + m.group(2).replace("<h1","<h2").replace("</h1>","</h2>") + m.group(3),
               s, flags=re.S)
    # 搜索框原本在页面上方的 toolbar 里，改为置于 最新/全部 标签之上：
    # 移除原位置的 toolbar（保留 input 供 HWX 复用，DOM 由 HWX 块内重建）
    s = re.sub(r'<div class="toolbar">.*?</div>\s*', '', s, flags=re.S, count=1)
    anchor = '<div class="tabs" id="tabs"'
    assert anchor in s, "HWX 锚点丢失"
    s = s.replace(anchor, "\n" + hwx_block() + "\n" + anchor, 1)
    open(p, "w", encoding="utf-8").write(s)
    print("HWX v3 注入完成")

patch_home_discover()

# ---------------- 章节页 og:image 指向各自的分享图 ----------------
# scripts/gen_og.py 一次性生成 i/<slug>/<k>/og.png（静态资产，不进 CI 链）。
# 这里在每次构建后把「存在 og.png 的章节页」的 og:image / og:image:alt /
# twitter:image 改写为该页专属图；没有图的页面保持全站图，优雅降级。
def patch_chapter_og():
    import os, re
    n = 0
    for slug in os.listdir("i"):
        d1 = os.path.join("i", slug)
        if not os.path.isdir(d1):
            continue
        for k in os.listdir(d1):
            d2 = os.path.join(d1, k)
            page = os.path.join(d2, "index.html")
            png = os.path.join(d2, "og.png")
            if not (os.path.isdir(d2) and os.path.exists(page) and os.path.exists(png)):
                continue
            s = open(page, encoding="utf-8").read()
            url = "https://ourword.ai/i/%s/%s/og.png" % (slug, k)
            m = re.search(r"<title>([^<|]+)", s)
            alt = (m.group(1).strip() if m else "深度阅读")
            s2 = re.sub(r'(<meta property="og:image" content=")[^"]*(")', r"\g<1>%s\g<2>" % url, s)
            s2 = re.sub(r'(<meta property="og:image:alt" content=")[^"]*(")', r"\g<1>%s\g<2>" % alt.replace("\\", ""), s2)
            s2 = re.sub(r'(<meta name="twitter:image" content=")[^"]*(")', r"\g<1>%s\g<2>" % url, s2)
            if s2 != s:
                open(page, "w", encoding="utf-8").write(s2)
                n += 1
    print("chapter og:image rewired:", n)

patch_chapter_og()

# ---------------- 条目页：手写介绍替换模板句 ----------------
# 原 dek 是 "格雷厄姆（美·1894-1976年）——安全边际·市场先生。"，与上一行 .one 重复、
# 信息量为零。改用 HWX_INTROS 的手写介绍；无手写介绍的条目保留原句。
def patch_entry_intro():
    import os, re, sys
    sys.path.insert(0, "seo")
    import hw_slugs, build_seo
    n = 0
    for e in build_seo.load_array():
        slug = hw_slugs.slug_for(e["n"])
        intro = HWX_INTROS.get(slug)
        page = os.path.join("i", slug, "index.html")
        if not (intro and os.path.exists(page)):
            continue
        s = open(page, encoding="utf-8").read()
        s2 = re.sub(r'<p class="dek">[^<]*</p>',
                    '<p class="dek">%s</p>' % intro, s, count=1)
        if s2 != s:
            open(page, "w", encoding="utf-8").write(s2)
            n += 1
    print("entry intro rewritten:", n)


# ---------------- 全站：日夜切换按钮 ----------------
# 首页的按钮在 HWX 块里；其余页面（条目页/章节页/主题页）在这里统一注入。
HWX_T_A, HWX_T_B = "<!--HWX:THEME-->", "<!--/HWX:THEME-->"

def theme_widget():
    css = (
        # 站点主变量 + hw-entry/hw-chapter 的整套变量（不补全这些，正文会用亮色墨值印在暗底）
        ':root[data-theme="dark"]{--paper:#171410;--ink:#eae3d4;--acc:#c65f4f;'
        '--line:#3a342a;--white:#1d1913;--line-strong:rgba(234,227,212,.22);'
        '--ink-30:rgba(234,227,212,.42);--ink-50:rgba(234,227,212,.6);--paper2:#201c15;'
        '--bg:#171410;--bg-tint:#201c15;--surface:#1d1913;--surface-2:#232019;'
        '--ink-2:#d9d1c0;--muted:#a79e8b;--faint:#8b8371;'
        '--rule:#3a342a;--rule-2:#443d31;--seal:#e0705f;--seal-soft:#3a221f;'
        '--shadow:0 1px 2px rgba(0,0,0,.4),0 10px 28px -18px rgba(0,0,0,.6)}'
        ':root[data-theme="dark"] body{background:var(--bg);color:var(--ink)}'
        ':root[data-theme="dark"] .panel,:root[data-theme="dark"] article{background:transparent}'
        # 正文与次级文本走变量，覆盖硬编码墨色（原来 #3f3a34 在暗底对比度仅 1.63）
        ':root[data-theme="dark"] p,:root[data-theme="dark"] li,:root[data-theme="dark"] .dek,'
        ':root[data-theme="dark"] .one,:root[data-theme="dark"] .f-d,:root[data-theme="dark"] .eg,'
        ':root[data-theme="dark"] blockquote{color:var(--ink-2)}'
        ':root[data-theme="dark"] .src,:root[data-theme="dark"] .why,:root[data-theme="dark"] .meta,'
        ':root[data-theme="dark"] .sub,:root[data-theme="dark"] .crumb{color:var(--muted)}'
        # 朱红提亮：#9d2933 在暗底只有 2.45
        ':root[data-theme="dark"] .kicker,:root[data-theme="dark"] .sec-k,:root[data-theme="dark"] .dot,'
        ':root[data-theme="dark"] mark.hl,:root[data-theme="dark"] .seal,'
        ':root[data-theme="dark"] .chip.on{color:#e0705f}'
        ':root[data-theme="dark"] mark.hl{text-decoration:none}'
        # 浅底区块：背景跟随暗色，否则白底白字（实测对比度 1.26）
        ':root[data-theme="dark"] .card,:root[data-theme="dark"] .map,:root[data-theme="dark"] .rel,'
        ':root[data-theme="dark"] .box,:root[data-theme="dark"] .quote-card,:root[data-theme="dark"] .panel,'
        ':root[data-theme="dark"] .chip,:root[data-theme="dark"] .side .panel'
        '{background:var(--surface);border-color:var(--rule)}'
        ':root[data-theme="dark"] .map-n,:root[data-theme="dark"] .n,'
        ':root[data-theme="dark"] a{color:var(--ink)}'
        ':root[data-theme="dark"] .toc a,:root[data-theme="dark"] .sib a{color:var(--ink-2)}'
        ':root[data-theme="dark"] .share-btn{background:var(--surface);color:var(--ink);border-color:var(--line-strong)}'
        ':root[data-theme="dark"] .sep,:root[data-theme="dark"] .crumb .sep{color:var(--faint)}'
        ':root[data-theme="dark"] mark.hl,:root[data-theme="dark"] article mark.hl{color:#e0705f!important;background:transparent}'
        ':root[data-theme="dark"] .map,:root[data-theme="dark"] .map *,'
        ':root[data-theme="dark"] .rel,:root[data-theme="dark"] .rel *{background-color:transparent}'
        ':root[data-theme="dark"] .map,:root[data-theme="dark"] .rel{background:var(--surface)!important}'
        ':root[data-theme="dark"] .map-cat,:root[data-theme="dark"] .map-list,'
        ':root[data-theme="dark"] .map-row{background:var(--surface)!important;border-color:var(--rule)!important}'
        ':root[data-theme="dark"] .map-n{color:var(--ink)!important}'
        ':root[data-theme="dark"] .map-w,:root[data-theme="dark"] .map-line{color:var(--muted)!important}'
        ':root[data-theme="dark"] .map .why,:root[data-theme="dark"] .rel .why{color:var(--muted)!important}'
        '#hwx-theme{position:fixed;top:14px;right:14px;z-index:9999;width:36px;height:36px;'
        'border:1px solid var(--rule,#d8d2c6);background:var(--paper,#f5f1e8);color:var(--ink,#1f1c17);'
        'border-radius:50%;font-size:15px;line-height:1;cursor:pointer;display:flex;align-items:center;'
        'justify-content:center;box-shadow:0 1px 6px rgba(0,0,0,.10);padding:0}'
        '#hwx-theme:hover{border-color:#9d2933;color:#9d2933}'
    )
    js = (
        "(function(){var R=document.documentElement,K='hwx_theme';"
        "function sd(){return !!(window.matchMedia&&window.matchMedia('(prefers-color-scheme:dark)').matches)}"
        "function g(){try{return localStorage.getItem(K)||''}catch(e){return ''}}"
        "function st(v){try{localStorage.setItem(K,v)}catch(e){}}"
        "function eff(){return g()||(sd()?'dark':'light')}"
        "function paint(){var m=eff();R.setAttribute('data-theme',m);"
        "var b=document.getElementById('hwx-theme');"
        "if(b){b.textContent=(m==='dark'?'\\u2600':'\\u263e');"
        "b.setAttribute('title',m==='dark'?'切换到日间':'切换到夜间')}}"
        "paint();document.addEventListener('DOMContentLoaded',function(){"
        "var b=document.getElementById('hwx-theme');if(!b)return;"
        "b.onclick=function(){st(eff()==='dark'?'light':'dark');paint()};paint()});})();"
    )
    return (HWX_T_A + '<style>' + css + '</style>'
            '<button id="hwx-theme" type="button" aria-label="切换日夜模式"></button>'
            '<script>' + js + '</script>' + HWX_T_B)


def patch_theme_widget():
    import os, re
    n = 0
    for dp, dn, fn in os.walk("."):
        if ".git" in dp or dp.startswith("./assets"):
            continue
        for f in fn:
            if f not in ("index.html", "404.html"):
                continue
            path = os.path.join(dp, f)
            s = open(path, encoding="utf-8").read()
            if 'http-equiv="refresh"' in s:      # 跳转桩跳过
                continue
            if path == "./index.html":           # 首页按钮在 HWX 块里
                continue
            s2 = re.sub(re.escape(HWX_T_A) + r".*?" + re.escape(HWX_T_B), "", s, flags=re.S)
            if "</body>" not in s2:
                continue
            s2 = s2.replace("</body>", theme_widget() + "</body>", 1)
            if s2 != s:
                open(path, "w", encoding="utf-8").write(s2)
                n += 1
    print("theme widget on pages:", n)


patch_entry_intro()
patch_theme_widget()

HWQ_A, HWQ_B = "<!--HWX:CHAT-->", "<!--/HWX:CHAT-->"


def chat_widget():
    """悬浮球问答的注入块。HW_CHAT_ENDPOINT 为空时返回空串——
    前端脚本本来也会 return，但连 <script> 都不发更干净，也省一次请求。"""
    if not HW_CHAT_ENDPOINT:
        return ""
    return (HWQ_A
            + '<script>window.HW_CHAT_ENDPOINT="' + HW_CHAT_ENDPOINT + '";</script>'
            + '<script src="/assets/hw-chat.js?v=7" defer></script>'
            + HWQ_B)


def patch_chat_widget():
    """悬浮球要全局出现，所以走和 patch_theme_widget 一样的全站扫描。

    首页也走这里（不像主题按钮那样特例挂在 HWX 块里）——同一个东西两处注入，
    迟早有一处忘了改。先剥掉旧块再插新块，所以是幂等的；
    把 HW_CHAT_ENDPOINT 改回 "" 再跑一次，全站就干净了。
    """
    import os, re
    n = 0
    block = chat_widget()
    for dp, dn, fn in os.walk("."):
        if ".git" in dp or dp.startswith("./assets"):
            continue
        for f in fn:
            if f not in ("index.html", "404.html"):
                continue
            path = os.path.join(dp, f)
            s = open(path, encoding="utf-8").read()
            if 'http-equiv="refresh"' in s:      # 跳转桩跳过
                continue
            s2 = re.sub(re.escape(HWQ_A) + r".*?" + re.escape(HWQ_B), "", s, flags=re.S)
            if "</body>" not in s2:
                continue
            if block:
                s2 = s2.replace("</body>", block + "</body>", 1)
            if s2 != s:
                open(path, "w", encoding="utf-8").write(s2)
                n += 1
    print("chat widget on pages:", n)


patch_chat_widget()

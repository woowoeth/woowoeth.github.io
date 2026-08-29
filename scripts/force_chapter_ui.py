#!/usr/bin/env python3
# Patch generators AND already-built HTML so highlight/sidebar cannot miss.
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
STYLE = (
    '<style id="hw-force">'
    'mark,mark.hl{background:transparent!important;color:#9d2933!important;'
    'font-weight:700!important;text-decoration:underline!important;'
    'text-decoration-color:#9d2933!important;text-underline-offset:.16em;'
    'text-decoration-thickness:1.5px}'
    '@media (max-width:900px){aside.side{display:none!important}'
    '.layout{grid-template-columns:1fr!important}}'
    '</style>'
)
MARK_OPEN = (
    '<mark class="hl" style="background:transparent;color:#9d2933;font-weight:700;'
    'text-decoration:underline;text-decoration-color:#9d2933;text-underline-offset:.16em;'
    'text-decoration-thickness:1.5px">'
)

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
        if s != orig:
            path.write_text(s, encoding="utf-8")
            n += 1
    print("force_chapter_ui html", n)

if __name__ == "__main__":
    patch_html()


# HWX v3: 最新 tab + 瀑布流混排 + 今日三样 + 历史行 + 暗色双主题
HWX_A, HWX_B = "<!--HWX:FIND-->", "<!--/HWX:FIND-->"

HWX_SCENES = [
    ("要做不可逆的决定",[("caesar","the-rubicon"),("li-ka-shing","knowing-when-to-stop"),("graham","margin-of-safety"),("han-xin","back-to-the-river"),("xiang-yu","sinking-the-boats"),("schelling","binding-yourself")]),
    ("对手比我强",[("napoleon","decisive-point"),("mao","on-protracted-war"),("sun-tzu","form-like-water"),("musashi","no-favorite-weapon"),("li-bi","strike-the-base"),("boyd","ooda")]),
    ("我对，但被否了",[("su-yu","daring-to-state"),("thiel","the-contrarian-question"),("marks","second-level-thinking"),("franklin","never-say-certainly"),("boyd","to-be-or-to-do")]),
    ("连胜，要不要加码",[("art-of-worldly-wisdom","quit-while-winning"),("bismarck","art-of-the-possible"),("buffett","swimming-naked"),("taleb","turkey-problem"),("napoleon","sublime-to-ridiculous"),("zhang-liang","asking-for-less")]),
    ("亏着，砍还是扛",[("livermore","hope-and-fear-inverted"),("livermore","sitting-tight"),("grove","revolving-door"),("huang","strategic-retreat"),("thinking-fast-and-slow","loss-aversion"),("lynch","stomach-not-brain")]),
    ("情绪上头",[("epictetus","judgments-not-things"),("su-shi","no-wind-no-rain"),("zhang-yiming","ordinary-mind"),("marcus-aurelius","morning-preparation"),("zhang-liang","picking-up-the-shoe")]),
    ("谈判与说服",[("schelling","focal-points"),("influence","reciprocity"),("wealth-of-nations","not-benevolence"),("guiguzi","listen-in-reverse"),("caesar","clementia"),("gandhi","salt-march")]),
    ("团队老出同样的问题",[("thinking-in-systems","structure-drives-behavior"),("han-feizi","not-counting-on-goodness"),("grove","inflection-and-cassandras"),("dalio","believability"),("shang-yang","moving-the-pole"),("zhuge-liang","executing-ma-su")]),
    ("看不清方向",[("marks","taking-the-temperature"),("einstein","formulating-the-problem"),("mao","on-contradiction"),("wang-xing","core-not-boundary"),("tao-te-ching","reversal"),("huang","zero-billion-markets")]),
    ("从零开始一件事",[("paul-graham","dont-scale"),("zhu-yuanzhang","delay-the-title"),("thiel","competition-is-for-losers"),("matsushita","tap-water"),("naval","productize-yourself"),("duan-yongping","dare-to-be-last"),("lee-kuan-yew","does-it-work")]),
    ("投资不亏大钱",[("graham","mr-market"),("buffett","circle-of-competence"),("munger","invert"),("taleb","skin-in-the-game"),("lynch","tenbagger-at-the-mall"),("bai-gui","take-what-others-drop")]),
    ("看人与防骗",[("analects","see-how"),("zeng-guofan","recruit-and-test"),("zizhi-tongjian","talent-and-virtue"),("strategies-of-the-warring-states","three-mirrors"),("la-rochefoucauld","memory-vs-judgment"),("crowd","assert-repeat-contaminate"),("influence","social-proof")]),
    ("在低谷",[("frankl","the-last-freedom"),("dalio","pain-plus-reflection"),("nietzsche","what-does-not-kill"),("su-shi","three-exiles"),("marcus-aurelius","obstacle-is-the-way")]),
    ("忙，但心虚",[("wang-xing","escape-from-thinking"),("jobs","focus-is-saying-no"),("drucker","right-things-first"),("bezos","what-wont-change"),("franklin","one-virtue-a-week")]),
    ("交班与退场",[("fan-li","leave-at-the-top"),("lee-kuan-yew","from-my-sickbed"),("guo-ziyi","open-gates"),("wang-jian","asking-for-fields"),("li-bi","no-office")]),
]

HWX_INTROS = {
"sun-tzu":"最早也最完整的战争方法论，被读了两千五百年","mao":"从绝对弱势打到全局翻盘的战略操盘手",
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
    "战略·博弈":"#a33b2e","权力·治理":"#7d5a3c","处世·人际":"#5f7355",
    "心智·哲学":"#4e6b7a","财富·投资":"#8a6d2f","创业·产品":"#c26b3f","典籍·洞察":"#6b5b73",
}

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
        E.append({"n": e["n"], "s": slug, "c": e["c"], "w": e["w"], "it": it, "hk": hook,
                  "nc": len(chs), "c0": chs[0][1] if chs else "",
                  "cs": [n for _, n, _ in chs[:3]] if len(chs) >= 3 else []})

    # 金句池：每章取 8-34 字里最长一条，带出处深链
    QP = []
    for ch in C.CHAPTERS:
        q = best_q(ch)
        if not q: continue
        QP.append({"q": q, "who": ch["parent"], "cn": ch["n"],
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
    valid = {(x["s"], k): True for x in E for k, _, _ in ch_by.get(x["n"], [])}
    S = []
    for t, refs in HWX_SCENES:
        for s_, k_ in refs:
            assert (s_, k_) in valid, "HWX 场景引用不存在: %s/%s (%s)" % (s_, k_, t)
        S.append({"t": t, "r": [{"who": next(c["parent"] for c in C.CHAPTERS if hw_slugs.slug_for(c["parent"])==s_ and c["k"]==k_),
                                  "cn": next(c["n"] for c in C.CHAPTERS if hw_slugs.slug_for(c["parent"])==s_ and c["k"]==k_),
                                  "u": "/i/%s/%s/" % (s_, k_),
                                  "hint": line_by.get((next(c["parent"] for c in C.CHAPTERS if hw_slugs.slug_for(c["parent"])==s_ and c["k"]==k_), k_), "")}
                                 for s_, k_ in refs]})

    # 今日一问池（apply 里的「先问」句）
    ASK = []
    for ch in C.CHAPTERS:
        m = re.search(r"先问：(.+?)(?:\n|$)", ch.get("apply", ""))
        if m:
            ASK.append({"t": m.group(1).strip(), "who": ch["parent"], "cn": ch["n"],
                        "u": "/i/%s/%s/" % (hw_slugs.slug_for(ch["parent"]), ch["k"])})

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
                   "s": slug, "k": k, "u": "/i/%s/%s/" % (slug, k),
                   "c": cat_by.get(pname,"")})

    j = json.dumps({"E": E, "QP": QP, "QQ": QQ, "S": S, "ASK": ASK,
                    "CC": CAT_COLOR, "NC": NC}, ensure_ascii=False, separators=(",",":")).replace("</","<\\/")
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
#hwx-theme{position:fixed;top:14px;right:14px;z-index:9999;width:36px;height:36px;border:1px solid var(--line);background:var(--paper);color:var(--ink);border-radius:50%;font-size:15px;line-height:1;cursor:pointer;display:flex;align-items:center;justify-content:center;box-shadow:0 1px 6px rgba(0,0,0,.10);padding:0}
#hwx-theme:hover{border-color:var(--acc);color:var(--acc)}
#hwx .today{display:grid;grid-template-columns:1.5fr 1fr;gap:14px;margin:18px 0 6px}
@media(max-width:700px){#hwx .today{grid-template-columns:1fr}}
#hwx .tq{border:1px solid var(--line);border-radius:16px;padding:20px 22px;background:var(--paper2);display:flex;flex-direction:column}
#hwx .tq .dt{font-size:11.5px;letter-spacing:.24em;color:var(--acc);font-weight:700;margin-bottom:6px}
#hwx .tq .q{font-size:clamp(18px,3.2vw,24px);font-weight:700;line-height:1.8;margin-bottom:12px}
#hwx .tq .src{font-size:12.5px;color:var(--muted)}
#hwx .tq .src a{color:var(--acc);text-decoration:none}
#hwx .tq .acts{display:flex;gap:8px;margin-top:14px}
#hwx .tq .acts button{border:1.5px solid var(--ink);background:transparent;color:var(--ink);border-radius:999px;padding:5px 14px;font-family:inherit;font-size:12.5px;cursor:pointer}
#hwx .tq .acts .bs{background:var(--ink);color:var(--paper)}
#hwx .tcol{display:flex;flex-direction:column;gap:14px}
#hwx .tbox{border:1px solid var(--line);border-radius:16px;padding:14px 16px;flex:1}
#hwx .tbox .lb{font-size:10.5px;letter-spacing:.28em;color:var(--acc);font-weight:700;margin-bottom:6px}
#hwx .tbox a{color:inherit;text-decoration:none;display:block}
#hwx .tbox b{font-size:14.5px}
#hwx .tbox .hint{display:block;font-size:13px;color:var(--ink);opacity:.72;margin-top:4px;line-height:1.65}
#hwx .hh{font-size:19px;font-weight:700;margin:24px 0 10px;letter-spacing:.03em;display:flex;justify-content:space-between;align-items:baseline}
#hwx .hh .ct{font-size:12px;color:var(--muted);font-weight:500}
#hwx .sc{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0 4px}
@media(max-width:640px){#hwx .sc{flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;padding-bottom:3px}#hwx .sc::-webkit-scrollbar{display:none}}
#hwx .sc button{flex:0 0 auto;border:1px solid var(--line);background:transparent;color:inherit;border-radius:999px;padding:5px 12px;font-family:inherit;font-size:13px;cursor:pointer;white-space:nowrap}
#hwx .sc button.on{background:var(--ink);color:var(--paper);border-color:var(--ink)}
#hwx .res{display:none;border-left:3px solid var(--acc);padding:4px 0 4px 13px;margin:8px 0 6px}
#hwx .res.on{display:block}
#hwx .res a{display:block;padding:5px 0;text-decoration:none;color:inherit}
#hwx .res a b{font-size:14px;font-weight:600}
#hwx .res a span{display:block;font-size:12.5px;color:var(--muted)}
#hwx .res a:hover b{border-bottom:1px solid}
#hwx .hist{display:none;align-items:center;gap:8px;margin:12px 0 2px;font-size:12px}
#hwx .hist .hl{color:var(--acc);font-weight:700;letter-spacing:.1em;flex:0 0 auto}
#hwx .hist .hchips{display:flex;gap:6px;overflow-x:auto;scrollbar-width:none;flex:1}
#hwx .hist .hchips::-webkit-scrollbar{display:none}
#hwx .hist .hchips a{flex:0 0 auto;border:1px solid var(--line);border-radius:999px;padding:2px 9px;color:var(--muted);text-decoration:none;white-space:nowrap}
#hwx .hist .hchips a:hover{color:var(--ink)}
#hwx .hist button{border:none;background:transparent;color:var(--muted);font-family:inherit;font-size:11px;cursor:pointer;flex:0 0 auto}
#hwx .tabs2{display:flex;gap:0;border-bottom:2px solid var(--line);margin:22px 0 0}
#hwx .tabs2 button{border:none;background:transparent;padding:8px 18px;font-family:inherit;font-size:15px;font-weight:600;color:var(--muted);cursor:pointer;border-bottom:3px solid transparent;margin-bottom:-2px}
#hwx .tabs2 button.on{color:var(--ink);border-bottom-color:var(--acc)}
#hwx .cats{display:flex;gap:6px;overflow-x:auto;scrollbar-width:none;margin:10px 0 0}
#hwx .cats::-webkit-scrollbar{display:none}
#hwx .cats button{flex:0 0 auto;border:none;background:transparent;color:var(--muted);font-family:inherit;font-size:12.5px;cursor:pointer;padding:3px 9px;border-radius:999px}
#hwx .cats button.on{background:var(--line);color:var(--ink)}
#hwx .feed{columns:158px;column-gap:11px;margin-top:12px}
#hwx .feed>*{break-inside:avoid;width:100%;margin:0 0 11px}
#hwx .nc-feed{columns:158px;column-gap:11px;margin-top:12px}
#hwx .nc-feed>*{break-inside:avoid;width:100%;margin:0 0 11px}
#hwx .pc{display:flex;flex-direction:column;border:1px solid var(--line);border-left:4px solid var(--sp,var(--line));border-radius:14px;padding:12px 13px 10px;text-decoration:none;color:inherit;background:var(--card)}
#hwx .pc .r1{display:flex;justify-content:space-between;align-items:baseline;gap:8px}
#hwx .pc b{font-size:15.5px}
#hwx .pc .tag{font-size:11px;color:var(--muted);white-space:nowrap;max-width:52%;overflow:hidden;text-overflow:ellipsis;font-style:normal}
#hwx .pc .it{font-size:12.5px;color:var(--muted);margin:4px 0 7px;line-height:1.6}
#hwx .pc .hk{font-size:13px;line-height:1.7;flex:1}
#hwx .pc .hk::before{content:"「"}#hwx .pc .hk::after{content:"」"}
#hwx .pc .ls{font-size:11px;color:var(--muted);margin-top:8px;border-top:1px dashed var(--line);padding-top:7px;line-height:1.6}
#hwx .pc .cf{font-size:11px;color:var(--acc);margin-top:8px}
#hwx .nc{display:flex;flex-direction:column;border:1px solid var(--line);border-left:4px solid var(--line);border-radius:14px;padding:12px 13px 10px;text-decoration:none;color:inherit;background:var(--card)}
#hwx .nc .pn{font-size:12px;color:var(--muted);margin-bottom:3px}
#hwx .nc .pn i{font-style:normal;color:var(--acc)}
#hwx .nc .nb{font-size:10px;background:var(--acc);color:#fff;border-radius:4px;padding:1px 5px;margin-left:5px;vertical-align:1px}
#hwx .nc b{font-size:15px}
#hwx .nc .w{font-size:11.5px;color:var(--muted);margin:2px 0 8px}
#hwx .nc .q{font-size:13px;line-height:1.7}
#hwx .nc .q::before{content:"「"}#hwx .nc .q::after{content:"」"}
#hwx .qc{min-height:150px;border-radius:14px;background:var(--paper2);border:1px solid var(--line);padding:16px 14px 12px;display:flex;flex-direction:column;text-decoration:none;color:inherit;position:relative}
#hwx .qc .v{flex:1;font-size:17px;font-weight:700;line-height:1.85;letter-spacing:.02em;display:flex;align-items:center}
#hwx .qc .v::before{content:"「"}#hwx .qc .v::after{content:"」"}
#hwx .qc .who{font-size:11.5px;color:var(--muted);margin-top:10px}
#hwx .qc .who i{font-style:normal;color:var(--acc)}
#hwx .qc .seal{position:absolute;top:12px;right:12px;width:20px;height:20px;border:1.5px solid var(--acc);border-radius:4px;color:var(--acc);font-size:11px;display:flex;align-items:center;justify-content:center}
#hwx .kc{border-radius:14px;background:var(--kbg);color:var(--kfg);padding:14px 14px 12px;display:flex;flex-direction:column}
#hwx .kc .qm{font-size:22px;color:#d98b7f;font-weight:900;line-height:1}
#hwx .kc .t{font-size:14.5px;font-weight:700;line-height:1.65;margin:7px 0 10px;flex:1}
#hwx .kc .r a{display:block;font-size:12px;color:var(--kmut);text-decoration:none;padding:3px 0}
#hwx .kc .r a b{color:var(--kfg);font-weight:600}
.dq{display:none!important}
.tabs,#tl-wrap{display:none!important}
.family a{color:inherit;text-decoration:none}
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
  document.getElementById('hwx-dt').textContent=(_n.getMonth()+1)+'月'+_n.getDate()+'日 · 星期'+WD[_n.getDay()]+(first?' · 今日一句':' · 换一句');
  document.getElementById('hwx-tq').textContent='「'+q1.q+'」';
  document.getElementById('hwx-tqs').innerHTML='—— '+q1.who+' · <a href="'+q1.u+'" data-h="'+esc(q1.who+' · '+q1.cn)+'">'+q1.cn+' →</a>';
}
paintQuote(true);
document.getElementById('hwx-next').onclick=function(){
  qIdx=Math.floor(Math.random()*D.QP.length); paintQuote(false);
};
var p1=D.E[(day*7)%D.E.length];
var tpEl=document.getElementById('hwx-tp');
tpEl.href='/i/'+p1.s+'/';tpEl.setAttribute('data-h',p1.n);
tpEl.innerHTML='<b>'+p1.n+' — '+p1.w+'</b><span class="hint">'+p1.it+'</span>';
var a1=D.ASK[(day*13)%D.ASK.length];
var taEl=document.getElementById('hwx-ta');
taEl.href=a1.u;taEl.setAttribute('data-h',esc(a1.who+' · '+a1.cn));
taEl.innerHTML='<b>'+a1.t+'</b><span class="hint">答案在：'+a1.who+' · '+a1.cn+' →</span>';
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
    c.fillStyle='#8a8377';c.font='500 34px "Noto Serif SC"';c.fillText('—— '+q1.who+' · '+q1.cn,100,y+40);
    c.strokeStyle='#d8d2c6';c.lineWidth=2;c.beginPath();c.moveTo(100,1230);c.lineTo(980,1230);c.stroke();
    c.fillStyle='#1f1c17';c.font='700 34px "Noto Serif SC"';c.fillText('人类世界生存法则',100,1318);
    c.fillStyle='#a33b2e';c.font='500 30px "Noto Serif SC"';c.fillText('OurWord.ai',100,1366);
    var qr=new Image();
    qr.onload=function(){c.drawImage(qr,858,1244,122,122);cv.toBlob(cb,'image/png')};
    qr.onerror=function(){cv.toBlob(cb,'image/png')};
    qr.src='/wechat-qr.png';
  }
}
document.getElementById('hwx-save').onclick=function(){drawCard(function(b){var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='ourword-'+(_n.getMonth()+1)+'-'+_n.getDate()+'.png';a.click()})};
document.getElementById('hwx-share').onclick=function(){drawCard(function(b){var f=new File([b],'ourword.png',{type:'image/png'});if(navigator.canShare&&navigator.canShare({files:[f]}))navigator.share({files:[f],title:'人类世界生存法则'});else{var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='ourword.png';a.click()}})};
/* ── 处境标签 ── */
var scEl=document.getElementById('hwx-sc'),resEl=document.getElementById('hwx-res');
D.S.forEach(function(s){
  var b=document.createElement('button');b.textContent=s.t;
  b.onclick=function(){
    var on=b.classList.contains('on');
    scEl.querySelectorAll('button').forEach(function(x){x.classList.remove('on')});
    if(on){resEl.classList.remove('on');resEl.innerHTML='';return}
    b.classList.add('on');
    resEl.innerHTML=s.r.map(function(r){return '<a href="'+r.u+'" data-h="'+esc(r.who+' · '+r.cn)+'"><b>'+r.who+' · '+r.cn+'</b><span>'+(r.hint||'')+'</span></a>'}).join('');
    resEl.classList.add('on');
  };scEl.appendChild(b);
});
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
var fullCells=[];
var qi=0,ki=0;
D.E.forEach(function(e,i){
  var dt=esc((e.n+' '+e.w+' '+e.c+' '+e.it+' '+e.hk).toLowerCase());
  fullCells.push('<a class="pc" href="/i/'+e.s+'/" data-h="'+esc(e.n)+'" data-c="'+e.c+'" data-t="'+dt+'" style="--sp:'+(D.CC[e.c]||'#999')+'"><span class="r1"><b>'+e.n+'</b><i class="tag">'+e.w+'</i></span><span class="it">'+e.it+'</span><span class="hk">'+(e.hk||e.w)+'</span>'+(e.cs.length?'<span class="ls">'+e.cs.join(' / ')+'</span>':'')+'<span class="cf">'+cta(e)+'</span></a>');
  if(i%3===2&&qi<D.QP.length){var g=D.QP[(qi*37)%D.QP.length];qi++;
    fullCells.push('<a class="qc xtra" href="'+g.u+'" data-h="'+esc(g.who+' · '+g.cn)+'" data-t="'+esc((g.q+g.who+g.cn).toLowerCase())+'"><span class="seal">句</span><span class="v">'+g.q+'</span><span class="who"><i>'+g.who+'</i> · '+g.cn+'</span></a>');}
  if(i%8===5&&ki<D.QQ.length){var k=D.QQ[ki++];
    fullCells.push('<div class="kc xtra" data-t="'+esc(k.t.toLowerCase())+'"><span class="qm">？</span><span class="t">'+k.t+'</span><span class="r">'+k.r.map(function(r){return '<a href="'+r.u+'" data-h="'+esc(r.who+' · '+r.cn)+'"><b>'+r.who+'</b> · '+r.cn+' →</a>'}).join('')+'</span></div>');}
});
/* ── 最新 feed ── */
/* 最新 tab 混排：每 4 张深度阅读插 1 张人物/书卡、1 张金句卡，每 9 槽插 1 张问题卡 */
var ncCells=[], _seen={}, _pi=0, _qi=0, _ki=0;
var byName={}; D.E.forEach(function(e){byName[e.n]=e});
D.NC.forEach(function(e,i){
  ncCells.push('<a class="nc" href="'+e.u+'" data-h="'+esc(e.pn+' · '+e.cn)+'" style="border-left-color:'+(D.CC[e.c]||'#ccc')+'"><span class="pn"><i>'+e.pn+'</i><span class="nb">新</span></span><b>'+e.cn+'</b><span class="w">'+e.w+'</span>'+(e.q?'<span class="q">'+e.q+'</span>':'')+'</a>');
  if(i%4===3){
    var pe=null;
    for(var t=0;t<D.NC.length&&!pe;t++){
      var cand=byName[D.NC[(_pi+t)%D.NC.length].pn];
      if(cand&&!_seen[cand.s]){pe=cand;_pi=(_pi+t+1)%D.NC.length}
    }
    if(pe){_seen[pe.s]=1;
      ncCells.push('<a class="pc" href="/i/'+pe.s+'/" data-h="'+esc(pe.n)+'" style="--sp:'+(D.CC[pe.c]||'#999')+'"><span class="r1"><b>'+pe.n+'</b><i class="tag">'+pe.w+'</i></span><span class="it">'+pe.it+'</span><span class="hk">'+(pe.hk||pe.w)+'</span><span class="cf">'+cta(pe)+'</span></a>');}
    var g=D.QP[(_qi*53)%D.QP.length];_qi++;
    ncCells.push('<a class="qc" href="'+g.u+'" data-h="'+esc(g.who+' · '+g.cn)+'"><span class="seal">句</span><span class="v">'+g.q+'</span><span class="who"><i>'+g.who+'</i> · '+g.cn+'</span></a>');
  }
  if(i%9===7&&_ki<D.QQ.length){var k=D.QQ[_ki++];
    ncCells.push('<div class="kc"><span class="qm">？</span><span class="t">'+k.t+'</span><span class="r">'+k.r.map(function(r){return '<a href="'+r.u+'" data-h="'+esc(r.who+' · '+r.cn)+'"><b>'+r.who+'</b> · '+r.cn+' →</a>'}).join('')+'</span></div>');}
});
/* ── 标签页切换 ── */
var TAB='新';
var feed=document.getElementById('hwx-feed'), ncfeed=document.getElementById('hwx-ncfeed');
var ct=document.getElementById('hwx-ct');
var catsRow=document.getElementById('hwx-cats');
function switchTab(t){
  TAB=t;
  document.querySelectorAll('#hwx-tabs2 button').forEach(function(b){b.classList.toggle('on',b.getAttribute('data-t')===t)});
  if(t==='新'){
    feed.style.display='none';ncfeed.style.display='';catsRow.style.display='none';
    ncfeed.innerHTML=ncCells.join('');ct.textContent=D.NC.length+' 篇最新';
  }else{
    ncfeed.style.display='none';feed.style.display='';catsRow.style.display='';
    feed.innerHTML=fullCells.join('');applyFeed();
  }
}
document.querySelectorAll('#hwx-tabs2 button').forEach(function(b){
  b.onclick=function(){switchTab(b.getAttribute('data-t'))};
});
function applyFeed(){
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
if(qin){qin.setAttribute('placeholder','搜索：人物、书、一句话、处境…');
  qin.oninput=null;qin.addEventListener('input',function(){if(TAB==='全'){applyFeed()}});}
/* 初始化 */
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
        "<div class=\"today\">"
        "<div class=\"tq\"><div class=\"dt\" id=\"hwx-dt\"></div><div class=\"q\" id=\"hwx-tq\"></div>"
        "<div class=\"src\" id=\"hwx-tqs\"></div>"
        "<div class=\"acts\"><button id=\"hwx-next\">换一换</button>"
        "<button class=\"bs\" id=\"hwx-save\">保存卡片</button>"
        "<button id=\"hwx-share\">分享</button></div></div>"
        "<div class=\"tcol\">"
        "<div class=\"tbox\"><div class=\"lb\">今日一篇</div><a id=\"hwx-tp\"></a></div>"
        "<div class=\"tbox\"><div class=\"lb\">今日一问</div><a id=\"hwx-ta\"></a></div>"
        "</div></div>"
        "<div class=\"hh\">按处境找 <span style=\"font-size:12px;color:var(--muted);font-weight:500\">「我现在遇到的是……」</span></div>"
        "<div class=\"sc\" id=\"hwx-sc\"></div><div class=\"res\" id=\"hwx-res\"></div>"
                "<div style=\"display:flex;align-items:baseline;justify-content:space-between;margin-top:18px\">"
        "<div class=\"tabs2\" id=\"hwx-tabs2\">"
        "<button data-t=\"新\" class=\"on\">最新</button><button data-t=\"全\">全部</button></div>"
        "<span class=\"ct\" id=\"hwx-ct\" style=\"font-size:12px;color:var(--muted)\"></span></div>"
        "<div class=\"cats\" id=\"hwx-cats\" style=\"display:none\"></div>"
        "<div class=\"nc-feed\" id=\"hwx-ncfeed\"></div>"
        "<div class=\"feed\" id=\"hwx-feed\" style=\"display:none\"></div>"
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
    # 文案兜底：每轮构建强制生效，防止 rebase / 其他脚本回写旧值
    s = s.replace("95 位人物与典籍", "100 位人物与典籍")
    s = s.replace("<title>人类世界生存法则 · 知识库</title>",
                  "<title>人类世界生存法则 — 100 位人物与典籍的生存智慧</title>")
    s = s.replace("人类文明的坐标，照亮千年的灯塔",
                  "100 个人物与典籍的生存智慧，跨越 2600 年")
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
        ':root[data-theme="dark"]{--paper:#171410;--ink:#eae3d4;--acc:#c65f4f;--muted:#9a917f;'
        '--line:#3a342a;--rule:#3a342a;--white:#1d1913;--line-strong:rgba(234,227,212,.22);'
        '--ink-30:rgba(234,227,212,.42);--ink-50:rgba(234,227,212,.6);--paper2:#201c15}'
        ':root[data-theme="dark"] body{background:#171410;color:#eae3d4}'
        ':root[data-theme="dark"] .panel,:root[data-theme="dark"] article{background:transparent}'
        ':root[data-theme="dark"] .share-btn{background:#1d1913;color:#eae3d4;border-color:rgba(234,227,212,.22)}'
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

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

# ---------------- HWX v2: 首页「按处境找 + 双列人物流」 ----------------
# v2 依用户反馈：人物入口改小红书式双列卡（名 + 身份一句话 + 钩子句，整卡可点），
# 卡上不再放章节标签（章节直达走处境区和搜索）；新增类别筛选；处境结果附钩子；
# 处境标签在手机上单行横滑。数据每次构建自 hw_chapters 再生，场景引用构建期校验。
HWX_A, HWX_B = "<!--HWX:FIND-->", "<!--/HWX:FIND-->"

HWX_SCENES = [
    ("要做不可逆的决定", [("caesar","the-rubicon"),("li-ka-shing","knowing-when-to-stop"),("graham","margin-of-safety"),("han-xin","back-to-the-river"),("xiang-yu","sinking-the-boats"),("schelling","binding-yourself")]),
    ("对手比我强", [("napoleon","decisive-point"),("mao","on-protracted-war"),("sun-tzu","form-like-water"),("musashi","no-favorite-weapon"),("li-bi","strike-the-base"),("boyd","ooda")]),
    ("我对，但被否了", [("su-yu","daring-to-state"),("thiel","the-contrarian-question"),("marks","second-level-thinking"),("franklin","never-say-certainly"),("boyd","to-be-or-to-do")]),
    ("连胜，要不要加码", [("art-of-worldly-wisdom","quit-while-winning"),("bismarck","art-of-the-possible"),("buffett","swimming-naked"),("taleb","turkey-problem"),("napoleon","sublime-to-ridiculous"),("zhang-liang","asking-for-less")]),
    ("亏着，砍还是扛", [("livermore","hope-and-fear-inverted"),("livermore","sitting-tight"),("grove","revolving-door"),("huang","strategic-retreat"),("thinking-fast-and-slow","loss-aversion"),("lynch","stomach-not-brain")]),
    ("情绪上头", [("epictetus","judgments-not-things"),("su-shi","no-wind-no-rain"),("zhang-yiming","ordinary-mind"),("marcus-aurelius","morning-preparation"),("zhang-liang","picking-up-the-shoe")]),
    ("谈判与说服", [("schelling","focal-points"),("influence","reciprocity"),("wealth-of-nations","not-benevolence"),("guiguzi","listen-in-reverse"),("caesar","clementia"),("gandhi","salt-march")]),
    ("团队老出同样的问题", [("thinking-in-systems","structure-drives-behavior"),("han-feizi","not-counting-on-goodness"),("grove","inflection-and-cassandras"),("dalio","believability"),("shang-yang","moving-the-pole"),("zhuge-liang","executing-ma-su")]),
    ("看不清方向", [("marks","taking-the-temperature"),("einstein","formulating-the-problem"),("mao","on-contradiction"),("wang-xing","core-not-boundary"),("tao-te-ching","reversal"),("huang","zero-billion-markets")]),
    ("从零开始一件事", [("paul-graham","dont-scale"),("zhu-yuanzhang","delay-the-title"),("thiel","competition-is-for-losers"),("matsushita","tap-water"),("naval","productize-yourself"),("duan-yongping","dare-to-be-last"),("lee-kuan-yew","does-it-work")]),
    ("投资不亏大钱", [("graham","mr-market"),("buffett","circle-of-competence"),("munger","invert"),("taleb","skin-in-the-game"),("lynch","tenbagger-at-the-mall"),("bai-gui","take-what-others-drop")]),
    ("看人与防骗", [("analects","see-how"),("zeng-guofan","recruit-and-test"),("zizhi-tongjian","talent-and-virtue"),("strategies-of-the-warring-states","three-mirrors"),("la-rochefoucauld","memory-vs-judgment"),("crowd","assert-repeat-contaminate"),("influence","social-proof")]),
    ("在低谷", [("frankl","the-last-freedom"),("dalio","pain-plus-reflection"),("nietzsche","what-does-not-kill"),("su-shi","three-exiles"),("marcus-aurelius","obstacle-is-the-way")]),
    ("忙，但心虚", [("wang-xing","escape-from-thinking"),("jobs","focus-is-saying-no"),("drucker","right-things-first"),("bezos","what-wont-change"),("franklin","one-virtue-a-week")]),
    ("交班与退场", [("fan-li","leave-at-the-top"),("lee-kuan-yew","from-my-sickbed"),("guo-ziyi","open-gates"),("wang-jian","asking-for-fields"),("li-bi","no-office")]),
]


# 100 条一句话介绍（人工手写，keyed by slug；新条目缺介绍时回落到 d 首句并告警）
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

def _hwx_payload():
    import json, sys as _s
    _s.path.insert(0, "seo")
    import hw_chapters as C, hw_slugs, build_seo
    ch_by, line_by = {}, {}
    for ch in C.CHAPTERS:
        ch_by.setdefault(ch["parent"], []).append((ch["k"], ch["n"], ch["w"]))
    for pname, spec in C.PARENTS.items():
        for it in spec.get("items", []):
            line_by[(pname, it["k"])] = it.get("line", "")
    E = []
    for e in build_seo.load_array():
        slug = hw_slugs.slug_for(e["n"])
        chs = ch_by.get(e["n"], [])
        hook = ""
        for k, _n, _w in chs:
            hook = line_by.get((e["n"], k), "")
            if hook: break
        it = HWX_INTROS.get(slug, "")
        if not it:
            it = (e.get("d", "").split("。")[0])[:38]
            print("HWX 警告：%s 缺手写介绍，回落 d 首句" % slug)
        E.append({"n": e["n"], "s": slug, "c": e["c"], "w": e["w"], "hk": hook, "it": it,
                  "h": [[k, n, w, line_by.get((e["n"], k), "")] for k, n, w in chs]})
    valid = {(x["s"], k) for x in E for k, _, _, _ in x["h"]}
    for t, refs in HWX_SCENES:
        for s_, k_ in refs:
            assert (s_, k_) in valid, "HWX 场景引用不存在: %s/%s (%s)" % (s_, k_, t)
    S = [{"t": t, "r": [list(r) for r in refs]} for t, refs in HWX_SCENES]
    j = json.dumps({"E": E, "S": S}, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return j, len(E), sum(len(x["h"]) for x in E)

def hwx_block():
    j, ne, nc = _hwx_payload()
    css = """
#hwx{margin:24px 0 8px}
#hwx .hwx-h{font-size:19px;letter-spacing:.03em;color:var(--ink,#1f1c17);margin:0 0 12px;font-weight:700}
#hwx .hwx-sc{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:8px}
#hwx .hwx-sc button{border:1px solid var(--line,#d8d2c6);background:transparent;color:inherit;border-radius:999px;padding:6px 13px;font-size:13.5px;cursor:pointer;line-height:1.6;white-space:nowrap}
#hwx .hwx-sc button.on{background:var(--ink,#1f1c17);color:var(--paper,#f5f1e8);border-color:var(--ink,#1f1c17)}
@media(max-width:640px){#hwx .hwx-sc{flex-wrap:nowrap;overflow-x:auto;-webkit-overflow-scrolling:touch;scrollbar-width:none;padding-bottom:2px}#hwx .hwx-sc::-webkit-scrollbar{display:none}}
#hwx .hwx-res{display:none;border-left:3px solid var(--acc,#a33b2e);padding:6px 0 6px 14px;margin:10px 0 16px}
#hwx .hwx-res.on{display:block}
#hwx .hwx-res a{display:block;padding:6px 0;text-decoration:none;color:inherit}
#hwx .hwx-res a b{font-weight:600;font-size:14.5px}
#hwx .hwx-res a .hk{display:block;color:var(--muted,#8a8377);font-size:13px;line-height:1.6;margin-top:1px}
#hwx .hwx-res a:hover b{border-bottom:1px solid currentColor}
#hwx .hwx-bar{display:flex;align-items:baseline;justify-content:space-between;gap:10px;margin:20px 0 8px;flex-wrap:wrap}
#hwx .hwx-cat{display:flex;flex-wrap:wrap;gap:6px}
#hwx .hwx-cat button{border:none;background:transparent;color:var(--muted,#8a8377);font-size:12.5px;cursor:pointer;padding:3px 8px;border-radius:999px;line-height:1.5}
#hwx .hwx-cat button.on{background:var(--line,#d8d2c6);color:var(--ink,#1f1c17)}
@media(max-width:640px){#hwx .hwx-cat{flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;max-width:100%}#hwx .hwx-cat::-webkit-scrollbar{display:none}#hwx .hwx-cat button{white-space:nowrap}}
#hwx .hwx-feed{display:grid;grid-template-columns:repeat(auto-fill,minmax(158px,1fr));gap:10px}
#hwx .hwx-card{display:flex;flex-direction:column;border:1px solid var(--line,#d8d2c6);border-radius:14px;padding:13px 14px 11px;text-decoration:none;color:inherit;background:transparent;transition:border-color .15s}
#hwx .hwx-card:hover{border-color:var(--acc,#a33b2e)}
#hwx .hwx-card .r1{display:flex;align-items:baseline;justify-content:space-between;gap:8px}
#hwx .hwx-card b{font-size:15.5px;line-height:1.4}
#hwx .hwx-card .tag{font-style:normal;font-size:11.5px;color:var(--muted,#8a8377);white-space:nowrap;max-width:52%;overflow:hidden;text-overflow:ellipsis}
#hwx .hwx-card .it{font-size:12.5px;color:var(--muted,#8a8377);margin:4px 0 7px;line-height:1.6}
#hwx .hwx-card .hk{font-size:13px;line-height:1.7;flex:1}
#hwx .hwx-card .hk::before{content:"「"}#hwx .hwx-card .hk::after{content:"」"}
#hwx .hwx-card .cf{font-size:11.5px;color:var(--acc,#a33b2e);margin-top:9px}
#hwx .hwx-hide{display:none!important}
.tabs,#tl-wrap{display:none!important}
.family a{color:inherit;text-decoration:none}
.family a:hover{color:var(--ink,#1f1c17)}
""".strip()
    js = """
(function(){
var D=HWXD, q=document.getElementById('q');
var scWrap=document.getElementById('hwx-sc'), res=document.getElementById('hwx-res');
var feed=document.getElementById('hwx-feed'), catWrap=document.getElementById('hwx-cat');
var byS={}; D.E.forEach(function(e){byS[e.s]=e});
D.S.forEach(function(s){
  var b=document.createElement('button'); b.type='button'; b.textContent=s.t;
  b.onclick=function(){
    var on=b.classList.contains('on');
    scWrap.querySelectorAll('button').forEach(function(x){x.classList.remove('on')});
    if(on){res.classList.remove('on');res.innerHTML='';return}
    b.classList.add('on');
    res.innerHTML=s.r.map(function(r){
      var e=byS[r[0]], ch=e.h.filter(function(h){return h[0]===r[1]})[0];
      var hint=ch[3]||ch[2];
      return '<a href="/i/'+r[0]+'/'+r[1]+'/"><b>'+e.n+' · '+ch[1]+'</b><span class="hk">'+hint+'</span></a>';
    }).join('');
    res.classList.add('on');
  };
  scWrap.appendChild(b);
});
var CAT='全部', cats=['全部'];
D.E.forEach(function(e){if(cats.indexOf(e.c)<0)cats.push(e.c)});
cats.forEach(function(c){
  var b=document.createElement('button'); b.type='button'; b.textContent=c;
  if(c===CAT)b.classList.add('on');
  b.onclick=function(){CAT=c;catWrap.querySelectorAll('button').forEach(function(x){x.classList.toggle('on',x.textContent===c)});apply()};
  catWrap.appendChild(b);
});
feed.innerHTML=D.E.map(function(e){
  var t=(e.n+' '+e.w+' '+e.c+' '+e.it+' '+e.hk+' '+e.h.map(function(h){return h[1]+' '+h[2]+' '+h[3]}).join(' ')).toLowerCase().replace(/"/g,'');
  return '<a class="hwx-card" href="/i/'+e.s+'/" data-c="'+e.c+'" data-t="'+t+'"><span class="r1"><b>'+e.n+'</b><i class="tag">'+e.w+'</i></span><span class="it">'+e.it+'</span><span class="hk">'+(e.hk||e.w)+'</span><span class="cf">'+e.h.length+' 篇深度阅读 →</span></a>';
}).join('');
function apply(){
  var v=q?q.value.trim().toLowerCase():'', vis=0;
  feed.querySelectorAll('.hwx-card').forEach(function(c){
    var ok=(CAT==='全部'||c.getAttribute('data-c')===CAT)&&(!v||c.getAttribute('data-t').indexOf(v)>=0);
    c.classList.toggle('hwx-hide',!ok); if(ok)vis++;
  });
  var ct=document.getElementById('ct'); if(ct)ct.textContent=vis+' 个入口';
}
if(q){q.setAttribute('placeholder','搜索：人物、书、一句话、章节、处境…');q.addEventListener('input',apply);}
window.addEventListener('load',apply);
})();
""".strip()
    return (HWX_A + "\n<section id=\"hwx\" aria-label=\"按处境找\">"
            "<div class=\"hwx-h\">按处境找 ——「我现在遇到的是……」</div>"
            "<div class=\"hwx-sc\" id=\"hwx-sc\"></div><div class=\"hwx-res\" id=\"hwx-res\"></div>"
            "<div class=\"hwx-bar\"><div class=\"hwx-h\" style=\"margin:0\">全部 " + str(ne) + " 个入口</div>"
            "<div class=\"hwx-cat\" id=\"hwx-cat\"></div></div>"
            "<div class=\"hwx-feed\" id=\"hwx-feed\"></div>"
            "<style>" + css + "</style>"
            "<script>var HWXD=" + j + ";</script><script>" + js + "</script>"
            "</section>\n" + HWX_B)

def patch_home_discover():
    import re
    p = "index.html"
    s = open(p, encoding="utf-8").read()
    s = re.sub(r"\n*" + re.escape(HWX_A) + r".*?" + re.escape(HWX_B) + r"\n*", "", s, flags=re.S)
    s = re.sub(r'(?:<script src="/assets/hw-share\.js" defer></script>\s*)+',
               '<script src="/assets/hw-share.js" defer></script>\n', s)
    # noscript 的 GEO 区块自带一个 h1，与可见 h1 重复——爬虫视角一页双 h1，降为 h2
    s = re.sub(r"(<noscript>)(.*?)(</noscript>)",
               lambda m: m.group(1) + m.group(2).replace("<h1", "<h2").replace("</h1>", "</h2>") + m.group(3),
               s, flags=re.S)
    anchor = '<div class="tabs" id="tabs"'
    assert anchor in s, "HWX 锚点丢失：首页结构变了"
    s = s.replace(anchor, "\n" + hwx_block() + "\n" + anchor, 1)
    open(p, "w", encoding="utf-8").write(s)
    print("HWX v2 首页发现层已注入")

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

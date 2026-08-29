# -*- coding: utf-8 -*-
"""「按处境找」的场景定义。

结构：场景名 → 若干第一人称问句 → 每个问句对应 2-3 篇章节。
场景名只说处境，不写问题；问题在点开之后才出现，答案挂在问题下面。
所有 (slug, k) 引用在构建时逐条校验，写错一个就构建失败。
"""

SCENES = [

# ── 决策 ──
("要做不可逆的决定", [
    ("这一步迈出去就收不回来，我该怎么想？",
     [("caesar", "the-rubicon"), ("xiang-yu", "sinking-the-boats")]),
    ("把退路堵死，究竟是勇还是蠢？",
     [("schelling", "binding-yourself"), ("han-xin", "back-to-the-river")]),
    ("怎么给自己留一条不会后悔的底线？",
     [("graham", "margin-of-safety"), ("li-ka-shing", "ninety-percent-failure")]),
]),
("信息不全就得拍板", [
    ("等数据齐了再决定，来得及吗？",
     [("boyd", "ooda"), ("grove", "inflection-and-cassandras")]),
    ("我凭什么相信自己现在的判断？",
     [("mao", "on-practice"), ("dalio", "believability")]),
    ("怎么先问对问题，而不是急着找答案？",
     [("einstein", "formulating-the-problem"), ("socrates", "midwifery")]),
]),
("方案被否了", [
    ("同一个方案，还要不要提第二次？",
     [("su-yu", "daring-to-state"), ("li-shimin", "hearing-all-sides")]),
    ("怎么说才不像是在顶撞？",
     [("zhang-liang", "borrowing-chopsticks"), ("strategies-of-the-warring-states", "three-mirrors")]),
    ("我该坚持，还是该认领这个否定？",
     [("boyd", "to-be-or-to-do"), ("thiel", "the-contrarian-question")]),
]),
("大家都同意，我不安", [
    ("全票通过为什么反而危险？",
     [("li-shimin", "the-first-debate"), ("marks", "second-level-thinking")]),
    ("怎么找到那个没人愿意说的反面？",
     [("munger", "invert"), ("thiel", "the-contrarian-question")]),
    ("我是不是被会议室的气氛带走了？",
     [("crowd", "descent-in-crowds"), ("influence", "social-proof")]),
]),

# ── 竞争 ──
("对手比我强得多", [
    ("整体打不过，从哪里能赢？",
     [("napoleon", "decisive-point"), ("sun-tzu", "form-like-water")]),
    ("这仗要速战，还是要拖？",
     [("mao", "on-protracted-war"), ("sima-yi", "waiting")]),
    ("有没有不打就赢的可能？",
     [("sun-tzu", "win-without-fighting"), ("guan-zhong", "buying-deer")]),
]),
("被对手牵着走", [
    ("对方每出一招我都要接吗？",
     [("zhang-yiming", "ordinary-mind"), ("wang-xing", "core-not-boundary")]),
    ("怎么把节奏抢回自己手里？",
     [("boyd", "ooda"), ("sun-tzu", "orthodox-and-surprise")]),
]),
("要不要进这个红海", [
    ("挤在人堆里做，值得吗？",
     [("thiel", "competition-is-for-losers"), ("huang", "zero-billion-markets")]),
    ("后发者还有机会吗？",
     [("duan-yongping", "dare-to-be-last"), ("guo-jia", "waiting-out-liaodong")]),
]),
("赢了一场，接下来呢", [
    ("乘胜追击还是见好就收？",
     [("art-of-worldly-wisdom", "quit-while-winning"), ("napoleon", "sublime-to-ridiculous")]),
    ("什么情况下应该把战果扩大？",
     [("su-yu", "enlarging-huaihai"), ("bismarck", "art-of-the-possible")]),
    ("连胜之后我最可能栽在哪？",
     [("taleb", "turkey-problem"), ("buffett", "swimming-naked")]),
]),

# ── 钱 ──
("一笔投资在亏", [
    ("该止损还是该扛住？",
     [("livermore", "hope-and-fear-inverted"), ("soros", "knowing-when-wrong")]),
    ("怎么分清是我错了还是市场错了？",
     [("graham", "mr-market"), ("marks", "taking-the-temperature")]),
    ("扛不住的时候，靠什么撑？",
     [("lynch", "stomach-not-brain"), ("livermore", "sitting-tight")]),
]),
("不知道该不该买", [
    ("我到底懂不懂这个东西？",
     [("buffett", "circle-of-competence"), ("munger", "latticework")]),
    ("现在这个价格算贵还是便宜？",
     [("graham", "margin-of-safety"), ("marks", "taking-the-temperature")]),
    ("别人都在买，我该跟吗？",
     [("bai-gui", "take-what-others-drop"), ("technological-revolutions", "bubble-in-the-script")]),
]),
("怕错过机会", [
    ("这一轮不上车，是不是就没了？",
     [("soros", "reflexivity"), ("crowd", "assert-repeat-contaminate")]),
    ("怎么判断这是趋势还是泡沫？",
     [("technological-revolutions", "bubble-in-the-script"), ("marks", "second-level-thinking")]),
]),
("想让钱自己生钱", [
    ("什么样的资产才是真正的资产？",
     [("naval", "assets-while-you-sleep"), ("fan-li", "stock-the-opposite")]),
    ("我的时间怎么才能不按小时卖？",
     [("naval", "productize-yourself"), ("wealth-of-nations", "pin-factory")]),
]),

# ── 人 ──
("要判断一个人可不可信", [
    ("面试或初次合作，看什么最准？",
     [("analects", "see-how"), ("zeng-guofan", "recruit-and-test")]),
    ("有本事但人品存疑，用不用？",
     [("zizhi-tongjian", "talent-and-virtue"), ("cao-cao", "talent-only")]),
    ("怎么判断他说的是真话？",
     [("guiguzi", "sound-out"), ("han-feizi", "form-and-name")]),
]),
("要说服一个人", [
    ("怎么让对方觉得这是他自己的主意？",
     [("guiguzi", "listen-in-reverse"), ("socrates", "midwifery")]),
    ("讲道理没用的时候还能怎么办？",
     [("wealth-of-nations", "not-benevolence"), ("influence", "reciprocity")]),
    ("怎么让一个不认同我的人先听下去？",
     [("mandela", "springbok-jersey"), ("analects", "harmony-not-sameness")]),
]),
("要谈一笔条件", [
    ("怎么让我的承诺显得可信？",
     [("schelling", "binding-yourself"), ("shang-yang", "moving-the-pole")]),
    ("双方僵住了，从哪里破？",
     [("schelling", "focal-points"), ("guiguzi", "open-and-close")]),
]),
("和人起了冲突", [
    ("对方明显有恶意，我要不要反击？",
     [("caesar", "clementia"), ("su-shi", "no-bad-people")]),
    ("怎么不让情绪替我做决定？",
     [("epictetus", "judgments-not-things"), ("zhang-liang", "picking-up-the-shoe")]),
]),
("被人怀疑、被人告状", [
    ("解释还是不解释？",
     [("guo-ziyi", "open-gates"), ("wang-jian", "asking-for-fields")]),
    ("功劳太大反而危险，怎么办？",
     [("fan-li", "leave-at-the-top"), ("han-xin", "neither-nor")]),
]),

# ── 团队 ──
("同一个错反复出现", [
    ("到底是人的问题还是机制的问题？",
     [("thinking-in-systems", "structure-drives-behavior"), ("han-feizi", "not-counting-on-goodness")]),
    ("改哪一处最省力？",
     [("thinking-in-systems", "leverage-points"), ("zhang-juzheng", "kaocheng")]),
]),
("下不了狠手", [
    ("该罚的是自己人，怎么办？",
     [("zhuge-liang", "executing-ma-su"), ("shang-yang", "law-above-rank")]),
    ("要砍掉一块我亲手做起来的业务",
     [("grove", "revolving-door"), ("huang", "strategic-retreat")]),
]),
("团队没劲了", [
    ("怎么让人愿意自己往前跑？",
     [("ren-zhengfei", "sound-of-gunfire"), ("inamori", "the-multiplier")]),
    ("赏罚该怎么给才有用？",
     [("han-feizi", "two-handles"), ("cao-cao", "burning-the-letters")]),
]),
("要招人或换人", [
    ("我该招比我强的人吗？",
     [("liu-bang", "three-i-cannot"), ("simons", "simons-principles")]),
    ("破格提拔的风险怎么控？",
     [("wu-zetian", "promote-and-drop"), ("zhuge-liang", "close-the-worthy")]),
]),
("坏消息传不上来", [
    ("怎么知道一线到底发生了什么？",
     [("grove", "inflection-and-cassandras"), ("li-shimin", "hearing-all-sides")]),
    ("报忧的人上次是什么下场？",
     [("mao", "methods-of-work"), ("li-shimin", "boat-and-water")]),
]),

# ── 做事 ──
("从零开始一件事", [
    ("第一步应该做重还是做轻？",
     [("paul-graham", "dont-scale"), ("zhu-yuanzhang", "delay-the-title")]),
    ("怎么知道这件事到底值不值得做？",
     [("drucker", "create-a-customer"), ("duan-yongping", "right-things-done-right")]),
    ("多久之内必须看到结果？",
     [("paul-graham", "default-alive"), ("zhang-yiming", "delayed-gratification")]),
]),
("事情太多做不完", [
    ("砍掉哪些才是对的？",
     [("jobs", "focus-is-saying-no"), ("drucker", "right-things-first")]),
    ("我是不是在用忙碌逃避思考？",
     [("wang-xing", "escape-from-thinking"), ("zeng-guofan", "self-watch")]),
]),
("卡住了推不动", [
    ("要不要换个方向？",
     [("on-war", "friction"), ("mao", "on-contradiction")]),
    ("笨办法还有没有价值？",
     [("zeng-guofan", "solid-camp-dull-fight"), ("bruce-lee", "one-kick")]),
]),
("要不要扩张", [
    ("边界应该画在哪里？",
     [("wang-xing", "core-not-boundary"), ("bezos", "what-wont-change")]),
    ("摊子铺大了会不会撑不住？",
     [("wang-jian", "sixty-thousand"), ("innovators-dilemma", "small-markets")]),
]),
("成本降不下来", [
    ("从哪里下刀最有效？",
     [("musk", "idiot-index"), ("musk", "first-principles")]),
    ("便宜到什么程度才会改变局面？",
     [("matsushita", "tap-water"), ("wealth-of-nations", "pin-factory")]),
]),
("公司做得好好的，我却慌", [
    ("好日子里该准备什么？",
     [("ren-zhengfei", "huaweis-winter"), ("fan-li", "stock-the-opposite")]),
    ("我们会不会正死于自己的优点？",
     [("innovators-dilemma", "good-management-fails"), ("bezos", "day-one")]),
]),

# ── 自己 ──
("情绪上头", [
    ("为什么这件事这么让我难受？",
     [("epictetus", "judgments-not-things"), ("epictetus", "dichotomy")]),
    ("怎么让自己先冷静下来？",
     [("marcus-aurelius", "view-from-above"), ("su-shi", "no-wind-no-rain")]),
]),
("在低谷里", [
    ("这段日子有什么意义？",
     [("frankl", "the-last-freedom"), ("nietzsche", "what-does-not-kill")]),
    ("怎么把这次失败变成有用的东西？",
     [("dalio", "pain-plus-reflection"), ("su-shi", "three-exiles")]),
    ("最难的时候还剩下什么是我的？",
     [("marcus-aurelius", "obstacle-is-the-way"), ("frankl", "happiness-ensues")]),
]),
("焦虑、想太多", [
    ("担心的事十有八九不会发生，怎么停下来？",
     [("marcus-aurelius", "morning-preparation"), ("epictetus", "dichotomy")]),
    ("怎么把注意力放回能改变的事上？",
     [("wang-yangming", "polish-on-things"), ("huineng", "originally-not-a-thing")]),
]),
("知道该做却做不到", [
    ("道理都懂为什么还是不动？",
     [("wang-yangming", "unity-of-knowing-and-doing"), ("wang-yangming", "bandits-in-the-heart")]),
    ("怎么改一个改不掉的习惯？",
     [("franklin", "one-virtue-a-week"), ("bruce-lee", "one-kick")]),
]),
("想学但学不进去", [
    ("怎么学才真的变成自己的？",
     [("mao", "on-practice"), ("wang-yangming", "polish-on-things")]),
    ("我该不该承认自己不懂？",
     [("analects", "know-what-you-know"), ("socrates", "knowing-not-knowing")]),
    ("有没有更省力的学法？",
     [("xunzi", "borrow-from-things"), ("munger", "latticework")]),
]),
("忙到没有自己的时间", [
    ("什么是真正该留白的？",
     [("tao-te-ching", "usefulness-of-emptiness"), ("zhuangzi", "use-of-uselessness")]),
    ("怎么把事做得省力一点？",
     [("zhuangzi", "ox-carving"), ("tao-te-ching", "wu-wei")]),
]),
("被人比下去了", [
    ("怎么面对比我强的同龄人？",
     [("zhuangzi", "equalizing-things"), ("la-rochefoucauld", "memory-vs-judgment")]),
    ("我该证明自己还是该做成事？",
     [("boyd", "to-be-or-to-do"), ("xiang-yu", "brocade-at-night")]),
]),

# ── 位置 ──
("要不要接这个位置", [
    ("这个位置的风险在哪里？",
     [("li-bi", "no-office"), ("feng-dao", "only-you-can-save")]),
    ("怎么判断自己接不接得住？",
     [("wang-jian", "sixty-thousand"), ("inamori", "pure-motive")]),
]),
("该退场了吗", [
    ("什么时候走最体面？",
     [("fan-li", "leave-at-the-top"), ("li-ka-shing", "knowing-when-to-stop")]),
    ("怎么交出去而不留烂摊子？",
     [("lee-kuan-yew", "from-my-sickbed"), ("zhang-liang", "asking-for-less")]),
]),
("要立规矩", [
    ("新规矩怎么才没人当耳旁风？",
     [("shang-yang", "moving-the-pole"), ("liu-bang", "three-articles")]),
    ("规矩该严还是该宽？",
     [("zhu-yuanzhang", "heavy-law"), ("guan-zhong", "follow-the-people")]),
]),
("看不清大势", [
    ("现在到底处在周期的哪一段？",
     [("marks", "taking-the-temperature"), ("technological-revolutions", "bubble-in-the-script")]),
    ("哪些东西十年后还成立？",
     [("bezos", "what-wont-change"), ("sovereign-individual", "logic-of-violence")]),
    ("为什么有的地方就是发展不起来？",
     [("why-nations-fail", "two-nogales"), ("hayek", "knowledge-is-dispersed")]),
]),
]

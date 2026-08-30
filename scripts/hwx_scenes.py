# -*- coding: utf-8 -*-
"""「按处境找」的场景定义。

结构：场景名 → 若干第一人称问句 → 每个问句对应 2-3 篇章节。
场景名只说处境，不写问题；问题在点开之后才出现，答案挂在问题下面。
所有 (slug, k) 引用在构建时逐条校验，写错一个就构建失败。
"""

SCENES = [

# ── 决策 ──
("情绪上头", [
    ("这件事为什么让我这么难受？",
     [("epictetus", "judgments-not-things"), ("epictetus", "dichotomy")]),
    ("火已经上来了，怎么压住？",
     [("marcus-aurelius", "view-from-above"), ("su-shi", "no-wind-no-rain")]),
]),
("做不完", [
    ("全都重要，我砍哪个都疼。",
     [("jobs", "focus-is-saying-no"), ("drucker", "right-things-first")]),
    ("我是不是在用忙掩盖不想面对的事？",
     [("wang-xing", "escape-from-thinking"), ("zeng-guofan", "self-watch")]),
]),
("起了冲突", [
    ("他明摆着有恶意，我还忍吗？",
     [("caesar", "clementia"), ("su-shi", "no-bad-people")]),
    ("我怕自己在气头上做错决定。",
     [("epictetus", "judgments-not-things"), ("zhang-liang", "picking-up-the-shoe")]),
]),
("拖着不开始", [
    ("总想再准备准备，就是不开始。",
     [("paul-graham", "dont-scale"), ("boyd", "ooda")]),
    ("我知道该做，可就是动不了。",
     [("wang-yangming", "unity-of-knowing-and-doing"), ("franklin", "one-virtue-a-week")]),
]),
("不可逆的决定", [
    ("这一步迈出去就收不回来了。",
     [("caesar", "the-rubicon"), ("xiang-yu", "sinking-the-boats")]),
    ("把退路堵死，是勇还是蠢？",
     [("schelling", "binding-yourself"), ("han-xin", "back-to-the-river")]),
    ("万一错了，我还有退路吗？",
     [("graham", "margin-of-safety"), ("li-ka-shing", "ninety-percent-failure")]),
]),
("信息不全", [
    ("等数据齐了，还来得及吗？",
     [("boyd", "ooda"), ("grove", "inflection-and-cassandras")]),
    ("我凭什么相信自己这次的判断？",
     [("mao", "on-practice"), ("dalio", "believability")]),
    ("我是不是根本问错了问题？",
     [("einstein", "formulating-the-problem"), ("socrates", "midwifery")]),
]),
("方案被否", [
    ("方案被毙了，还提第二次吗？",
     [("su-yu", "daring-to-state"), ("li-shimin", "hearing-all-sides")]),
    ("我怕再提就成了顶撞领导。",
     [("zhang-liang", "borrowing-chopsticks"), ("strategies-of-the-warring-states", "three-mirrors")]),
    ("该坚持，还是该认这个否定？",
     [("boyd", "to-be-or-to-do"), ("thiel", "the-contrarian-question")]),
]),
("全票通过", [
    ("所有人都同意，我反而心虚。",
     [("li-shimin", "the-first-debate"), ("marks", "second-level-thinking")]),
    ("没人反对，我反而不放心。",
     [("munger", "invert"), ("thiel", "the-contrarian-question")]),
    ("我是不是被会上的气氛带走了？",
     [("crowd", "descent-in-crowds"), ("influence", "social-proof")]),
    ("这个说法太顺了，我有点犯嘀咕。",
     [("popper", "falsifiability"), ("feynman", "dont-fool-yourself")]),
]),

# ── 竞争 ──
("对手更强", [
    ("整体拼不过，我还有哪块能赢？",
     [("napoleon", "decisive-point"), ("sun-tzu", "form-like-water")]),
    ("速战速决，还是拖下去？",
     [("mao", "on-protracted-war"), ("sima-yi", "waiting")]),
    ("硬碰肯定输，我还有别的路吗？",
     [("sun-tzu", "win-without-fighting"), ("guan-zhong", "buying-deer")]),
    ("我习惯的那套打法，这次不管用。",
     [("musashi", "no-favorite-weapon"), ("huo-qubing", "no-old-manuals")]),
]),
("被牵着走", [
    ("他每出一招，我都得接吗？",
     [("zhang-yiming", "ordinary-mind"), ("wang-xing", "core-not-boundary")]),
    ("我一直在接招，节奏不在我手里。",
     [("boyd", "ooda"), ("sun-tzu", "orthodox-and-surprise")]),
    ("我盯着眼前，反而看丢了大局。",
     [("musashi", "two-ways-of-seeing"), ("huo-qubing", "feeding-off-the-enemy")]),
]),
("进不进红海", [
    ("这行早挤满了，我还进吗？",
     [("thiel", "competition-is-for-losers"), ("huang", "zero-billion-markets")]),
    ("别人跑在前面，我还来得及吗？",
     [("duan-yongping", "dare-to-be-last"), ("guo-jia", "waiting-out-liaodong")]),
]),
("赢了之后", [
    ("赢了，追下去还是收手？",
     [("art-of-worldly-wisdom", "quit-while-winning"), ("napoleon", "sublime-to-ridiculous")]),
    ("赢了这一把，要不要加码？",
     [("su-yu", "enlarging-huaihai"), ("bismarck", "art-of-the-possible")]),
    ("连着顺了几把，我怕栽跟头。",
     [("taleb", "turkey-problem"), ("buffett", "swimming-naked")]),
]),

# ── 钱 ──
("投资在亏", [
    ("亏着的这笔，砍还是扛？",
     [("livermore", "hope-and-fear-inverted"), ("soros", "knowing-when-wrong")]),
    ("是我看错了，还是还没到时候？",
     [("graham", "mr-market"), ("marks", "taking-the-temperature")]),
    ("我快扛不住了，还要不要扛？",
     [("lynch", "stomach-not-brain"), ("livermore", "sitting-tight")]),
]),
("该不该买", [
    ("买之前，我真的懂它吗？",
     [("buffett", "circle-of-competence"), ("munger", "latticework")]),
    ("这个价，算贵还是算便宜？",
     [("graham", "margin-of-safety"), ("marks", "taking-the-temperature")]),
    ("别人都在买，我跟不跟？",
     [("bai-gui", "take-what-others-drop"), ("technological-revolutions", "bubble-in-the-script")]),
]),
("怕错过", [
    ("这趟不上，是不是就没了？",
     [("soros", "reflexivity"), ("crowd", "assert-repeat-contaminate")]),
    ("这是真机会，还是击鼓传花？",
     [("technological-revolutions", "bubble-in-the-script"), ("marks", "second-level-thinking")]),
]),
("让钱生钱", [
    ("钱放着不动，我心里发慌。",
     [("naval", "assets-while-you-sleep"), ("fan-li", "stock-the-opposite")]),
    ("我的收入完全绑在工时上。",
     [("naval", "productize-yourself"), ("wealth-of-nations", "pin-factory")]),
]),

# ── 人 ──
("这人可信吗", [
    ("第一次打交道，我看什么最准？",
     [("analects", "see-how"), ("zeng-guofan", "recruit-and-test")]),
    ("有本事但我信不过，用不用？",
     [("zizhi-tongjian", "talent-and-virtue"), ("cao-cao", "talent-only")]),
    ("他说得挺好，我有点不敢全信。",
     [("guiguzi", "sound-out"), ("han-feizi", "form-and-name")]),
]),
("要说服人", [
    ("我说了不算，得让他自己想到。",
     [("guiguzi", "listen-in-reverse"), ("socrates", "midwifery")]),
    ("道理都讲完了，还是没用。",
     [("wealth-of-nations", "not-benevolence"), ("influence", "reciprocity")]),
    ("他从一开始就不认同我。",
     [("mandela", "springbok-jersey"), ("analects", "harmony-not-sameness")]),
]),
("谈条件", [
    ("我说的话，他们好像不太当真。",
     [("schelling", "binding-yourself"), ("shang-yang", "moving-the-pole")]),
    ("谈僵了，谁都不肯先动。",
     [("schelling", "focal-points"), ("guiguzi", "open-and-close")]),
]),
("被猜忌", [
    ("越解释越像心虚，说还是不说？",
     [("guo-ziyi", "open-gates"), ("wang-jian", "asking-for-fields")]),
    ("功劳太大，我反而开始不安。",
     [("fan-li", "leave-at-the-top"), ("han-xin", "neither-nor")]),
]),

# ── 团队 ──
("错反复犯", [
    ("同一个坑，我们又掉进去了。",
     [("thinking-in-systems", "structure-drives-behavior"), ("han-feizi", "not-counting-on-goodness")]),
    ("问题一堆，我先动哪一处？",
     [("thinking-in-systems", "leverage-points"), ("zhang-juzheng", "kaocheng")]),
    ("复盘写了，下次还是照样犯。",
     [("records-of-the-grand-historian", "no-praise-no-hiding"), ("hu-xueyan", "the-silk-corner")]),
]),
("下不了手", [
    ("该罚的是跟我最久的人。",
     [("zhuge-liang", "executing-ma-su"), ("shang-yang", "law-above-rank")]),
    ("要砍的是我亲手做起来的。",
     [("grove", "revolving-door"), ("huang", "strategic-retreat")]),
]),
("团队没劲", [
    ("我说了很多遍，团队还是没劲。",
     [("ren-zhengfei", "sound-of-gunfire"), ("inamori", "the-multiplier")]),
    ("奖也发了罚也罚了，好像没用。",
     [("han-feizi", "two-handles"), ("cao-cao", "burning-the-letters")]),
    ("我的人只是照做，没人真的上心。",
     [("mencius", "people-first"), ("hu-xueyan", "no-cheating")]),
]),
("招人换人", [
    ("招个比我强的，我压得住吗？",
     [("liu-bang", "three-i-cannot"), ("simons", "simons-principles")]),
    ("想破格提一个人，又怕压不住。",
     [("wu-zetian", "promote-and-drop"), ("zhuge-liang", "close-the-worthy")]),
]),
("听不到实话", [
    ("汇报都很好，我却总觉得不对。",
     [("grove", "inflection-and-cassandras"), ("li-shimin", "hearing-all-sides")]),
    ("上次说真话的人，后来怎样了？",
     [("mao", "methods-of-work"), ("li-shimin", "boat-and-water")]),
]),

# ── 做事 ──
("从零开始", [
    ("第一步做大还是先试小的？",
     [("paul-graham", "dont-scale"), ("zhu-yuanzhang", "delay-the-title")]),
    ("投进去之前，我怎么知道值不值？",
     [("drucker", "create-a-customer"), ("duan-yongping", "right-things-done-right")]),
    ("多久看不到结果，我就该停？",
     [("paul-graham", "default-alive"), ("zhang-yiming", "delayed-gratification")]),
]),
("推不动", [
    ("推了很久推不动，该换方向吗？",
     [("on-war", "friction"), ("mao", "on-contradiction")]),
    ("只剩笨办法了，还要不要做？",
     [("zeng-guofan", "solid-camp-dull-fight"), ("bruce-lee", "one-kick")]),
    ("一改就出乱子，不改又不行。",
     [("old-regime", "most-dangerous-moment"), ("old-regime", "centralization-survived")]),
]),
("扩不扩张", [
    ("什么该做什么不做，我拿不准。",
     [("wang-xing", "core-not-boundary"), ("bezos", "what-wont-change")]),
    ("摊子越铺越大，我有点怕。",
     [("wang-jian", "sixty-thousand"), ("innovators-dilemma", "small-markets")]),
]),
("成本降不动", [
    ("该降的都降了，还能从哪下刀？",
     [("musk", "idiot-index"), ("musk", "first-principles")]),
    ("我降到多少，局面才会变？",
     [("matsushita", "tap-water"), ("wealth-of-nations", "pin-factory")]),
]),
("顺境里发慌", [
    ("日子正好，我该准备什么？",
     [("ren-zhengfei", "huaweis-winter"), ("fan-li", "stock-the-opposite")]),
    ("我们最强的地方，会不会正是死穴？",
     [("innovators-dilemma", "good-management-fails"), ("bezos", "day-one")]),
    ("摊子铺得太快，我心里没底。",
     [("hu-xueyan", "the-silk-corner"), ("old-regime", "most-dangerous-moment")]),
]),

# ── 自己 ──
("在低谷", [
    ("这段日子，到底熬来了什么？",
     [("frankl", "the-last-freedom"), ("nietzsche", "what-does-not-kill")]),
    ("这次栽了，我能捡回点什么？",
     [("dalio", "pain-plus-reflection"), ("su-shi", "three-exiles")]),
    ("最难的时候，还剩什么是我的？",
     [("marcus-aurelius", "obstacle-is-the-way"), ("frankl", "happiness-ensues")]),
    ("这件事我到现在都没想明白。",
     [("records-of-the-grand-historian", "i-am-confused"), ("mencius", "flood-like-qi")]),
]),
("想太多", [
    ("这事在我脑子里转了二十遍。",
     [("marcus-aurelius", "morning-preparation"), ("epictetus", "dichotomy")]),
    ("我一直在想我改变不了的事。",
     [("wang-yangming", "polish-on-things"), ("huineng", "originally-not-a-thing")]),
]),
("知道做不到", [
    ("道理都懂，可我就是不动。",
     [("wang-yangming", "unity-of-knowing-and-doing"), ("wang-yangming", "bandits-in-the-heart")]),
    ("这个毛病我改了很多次了。",
     [("franklin", "one-virtue-a-week"), ("bruce-lee", "one-kick")]),
    ("练了很久，感觉没什么长进。",
     [("ericsson", "deliberate-practice"), ("ericsson", "not-ten-thousand-hours")]),
]),
("学不进去", [
    ("看了很多，一到用就想不起来。",
     [("mao", "on-practice"), ("wang-yangming", "polish-on-things")]),
    ("我不懂，但不好意思说。",
     [("analects", "know-what-you-know"), ("socrates", "knowing-not-knowing")]),
    ("我是不是一直在用笨办法学？",
     [("xunzi", "borrow-from-things"), ("munger", "latticework")]),
    ("我以为懂了，一讲就卡壳。",
     [("feynman", "teach-to-understand"), ("ericsson", "deliberate-practice")]),
]),
("忙到没自己", [
    ("日程排满了，没一件是我自己的。",
     [("tao-te-ching", "usefulness-of-emptiness"), ("zhuangzi", "use-of-uselessness")]),
    ("同样的事，我总比别人费劲。",
     [("zhuangzi", "ox-carving"), ("tao-te-ching", "wu-wei")]),
]),
("被比下去", [
    ("他什么都比我快一步。",
     [("zhuangzi", "equalizing-things"), ("la-rochefoucauld", "memory-vs-judgment")]),
    ("我到底在证明自己，还是在做事？",
     [("boyd", "to-be-or-to-do"), ("xiang-yu", "brocade-at-night")]),
]),

# ── 位置 ──
("该不该接", [
    ("位置给我了，我看不清风险在哪。",
     [("li-bi", "no-office"), ("feng-dao", "only-you-can-save")]),
    ("机会挺好，就怕我接不住。",
     [("wang-jian", "sixty-thousand"), ("inamori", "pure-motive")]),
]),
("该不该退", [
    ("我该什么时候退，才不难看？",
     [("fan-li", "leave-at-the-top"), ("li-ka-shing", "knowing-when-to-stop")]),
    ("我交出去之后，会不会一团糟？",
     [("lee-kuan-yew", "from-my-sickbed"), ("zhang-liang", "asking-for-less")]),
]),
("要立规矩", [
    ("新规矩定了，没人当回事。",
     [("shang-yang", "moving-the-pole"), ("liu-bang", "three-articles")]),
    ("松了没用，紧了怕逼走人。",
     [("zhu-yuanzhang", "heavy-law"), ("guan-zhong", "follow-the-people")]),
    ("我压得住人，却服不了人。",
     [("mencius", "force-vs-virtue"), ("mencius", "people-first")]),
]),
("看不清大势", [
    ("现在到底是开头还是快结束了？",
     [("marks", "taking-the-temperature"), ("technological-revolutions", "bubble-in-the-script")]),
    ("十年之后，哪些还站得住？",
     [("bezos", "what-wont-change"), ("sovereign-individual", "logic-of-violence")]),
    ("同样的条件，我们差在哪？",
     [("why-nations-fail", "two-nogales"), ("hayek", "knowledge-is-dispersed")]),
    ("我看不出这局面是怎么形成的。",
     [("guns-germs-steel", "axis-of-continents"), ("sapiens", "fictions-that-cooperate")]),
    ("大家都这么做，可我说不出为什么。",
     [("sapiens", "wheat-domesticated-us"), ("mencius", "force-vs-virtue")]),
]),
# ── 本轮新增：补上原先完全没有覆盖的处境 ──
("两个都想要", [
    ("两个我都想要，可只能选一个。",
     [("jobs", "focus-is-saying-no"), ("munger", "invert")]),
    ("看着都好，我到底适合哪个？",
     [("buffett", "circle-of-competence"), ("duan-yongping", "right-things-done-right")]),
]),
("信不信直觉", [
    ("直觉和数据打架，我听哪个？",
     [("thinking-fast-and-slow", "wysiati"), ("simons", "slave-to-the-model")]),
    ("这次的直觉，我信得过吗？",
     [("simons", "simons-principles"), ("wang-yangming", "innate-knowing")]),
    ("我查的资料全都在支持我。",
     [("popper", "seek-refutation"), ("feynman", "dont-fool-yourself")]),
]),
("定不好价", [
    ("东西是好东西，可就是卖不动。",
     [("wealth-of-nations", "not-benevolence"), ("drucker", "create-a-customer")]),
    ("我定多少钱，人才愿意掏？",
     [("matsushita", "tap-water"), ("musk", "idiot-index")]),
]),
("遇上不讲理", [
    ("我跟他讲道理，完全没用。",
     [("epictetus", "dichotomy"), ("machiavelli", "as-it-is")]),
    ("我要不要照他的路数回敬？",
     [("gandhi", "means-are-seeds"), ("su-shi", "no-bad-people")]),
]),
("功劳被抢", [
    ("事是我做的，功是别人的。",
     [("art-of-worldly-wisdom", "do-and-be-seen"), ("xiang-yu", "brocade-at-night")]),
    ("这个功，我要不要去争？",
     [("zhang-liang", "asking-for-less"), ("guo-ziyi", "open-gates")]),
]),
("该不该妥协", [
    ("退这一步，是务实还是没底线？",
     [("bismarck", "art-of-the-possible"), ("lee-kuan-yew", "does-it-work")]),
    ("手段脏了，目的还干净吗？",
     [("gandhi", "means-are-seeds"), ("machiavelli", "as-it-is")]),
]),
("推不动别人", [
    ("别的部门就是不配合我。",
     [("thinking-in-systems", "leverage-points"), ("ren-zhengfei", "sound-of-gunfire")]),
    ("我没有权力，还怎么推动事？",
     [("li-bi", "no-office"), ("zhang-liang", "borrowing-chopsticks")]),
]),
("合伙人闹掰", [
    ("分钱这事，我怕埋雷。",
     [("zhang-liang", "asking-for-less"), ("han-feizi", "two-handles")]),
    ("话都说绝了，还修得回来吗？",
     [("cao-cao", "burning-the-letters"), ("mandela", "springbok-jersey")]),
]),
("觉得没意义", [
    ("每天都一样，我不知道图什么。",
     [("frankl", "happiness-ensues"), ("zhuangzi", "use-of-uselessness")]),
    ("我做这些，到底为了什么？",
     [("inamori", "pure-motive"), ("frankl", "the-last-freedom")]),
    ("赢了这一局，然后呢？",
     [("finite-and-infinite-games", "two-kinds"), ("finite-and-infinite-games", "playing-with-boundaries")]),
]),
("要不要跳槽", [
    ("还待得下去吗，我不确定。",
     [("boyd", "to-be-or-to-do"), ("zhang-yiming", "delayed-gratification")]),
    ("钱和成长，我该先要哪个？",
     [("naval", "productize-yourself"), ("buffett", "circle-of-competence")]),
]),

# ── 家庭与关系 ──
("跟伴侣吵", [
    ("同一件事我们吵了很多次了。",
     [("gottman", "four-horsemen"), ("nonviolent-communication", "needs-behind-blame")]),
    ("话说重了，还修得回来吗？",
     [("gottman", "repair-attempts"), ("crucial-conversations", "safety-first")]),
]),
("孩子不听", [
    ("说了很多遍，他还是不做。",
     [("montessori", "prepared-environment"), ("adler", "separation-of-tasks")]),
    ("我该管到什么程度？",
     [("adler", "separation-of-tasks"), ("montessori", "help-me-do-it-myself")]),
]),
("孩子不说话", [
    ("他什么都不跟我讲了。",
     [("attachment-theory", "strange-situation"), ("carl-rogers", "unconditional-regard")]),
    ("我怎么让他愿意开口？",
     [("carl-rogers", "reflective-listening"), ("nonviolent-communication", "observation-not-evaluation")]),
]),
("被家人的情绪裹着", [
    ("家里一有事，我整个人就乱了。",
     [("seneca", "on-anger"), ("epictetus", "dichotomy")]),
    ("我是该迁就，还是干脆躲远点？",
     [("adler", "separation-of-tasks"), ("attachment-theory", "secure-base")]),
]),
("父母催得紧", [
    ("我每次回家都要吵一轮。",
     [("adler", "separation-of-tasks"), ("nonviolent-communication", "needs-behind-blame")]),
    ("我怎么说才不伤人也不妥协？",
     [("chris-voss", "labeling"), ("crucial-conversations", "start-with-heart")]),
]),
("身边人不敢跟我说真话", [
    ("他们只报好消息给我。",
     [("carl-rogers", "unconditional-regard"), ("attachment-theory", "strange-situation")]),
    ("我上次的反应，是不是把人吓住了？",
     [("crucial-conversations", "safety-first"), ("cao-cao", "burning-the-letters")]),
]),

# ── 身心与生活 ──
("睡不好", [
    ("我一躺下脑子就停不下来。",
     [("john-ratey", "move-before-you-think"), ("seneca", "on-anger")]),
    ("睡够了还是觉得累。",
     [("john-ratey", "exercise-for-the-brain"), ("cal-newport", "attention-residue")]),
]),
("精力跟不上", [
    ("一到下午我就废了。",
     [("john-ratey", "exercise-for-the-brain"), ("cal-newport", "schedule-the-depth")]),
    ("我是不是一直在硬撑？",
     [("seneca", "on-shortness-of-life"), ("john-ratey", "move-before-you-think")]),
]),
("坐不住", [
    ("我一会儿就想去看手机。",
     [("cal-newport", "attention-residue"), ("atomic-habits", "identity-first")]),
    ("整块时间总是被切碎。",
     [("cal-newport", "schedule-the-depth"), ("seneca", "on-shortness-of-life")]),
]),
("想改个习惯", [
    ("我下过很多次决心，每次都断。",
     [("atomic-habits", "identity-first"), ("adler", "teleology")]),
    ("我怎么才能坚持下来？",
     [("atomic-habits", "systems-over-goals"), ("franklin", "one-virtue-a-week")]),
]),
("长期紧绷", [
    ("我好像很久没真正松下来了。",
     [("seneca", "on-shortness-of-life"), ("john-ratey", "move-before-you-think")]),
    ("这样下去我会不会垮？",
     [("john-ratey", "exercise-for-the-brain"), ("epictetus", "dichotomy")]),
]),
("时间不够用", [
    ("一天下来，没一件是我自己的事。",
     [("seneca", "on-shortness-of-life"), ("cal-newport", "schedule-the-depth")]),
    ("我到底该砍掉哪一块？",
     [("franklin", "one-virtue-a-week"), ("atomic-habits", "systems-over-goals")]),
]),

]

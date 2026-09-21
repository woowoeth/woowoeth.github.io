# -*- coding: utf-8 -*-
"""典籍条目：这一部我们不取哪一部分。

**为什么要有这张表。** 收一部典籍，取的从来不是整本。《颜氏家训》里
「妇主中馈……国不可使预政」和它讲治家因果的部分在同一篇里；《易经》讲
进退的那六十四卦，同一套符号也是占卜工具。读者读到我们取的那一半，
迟早会碰到另一半，而那时候他会问：**你是没看见，还是看见了不说。**
这张表就是把这句话提前说掉。

**为什么只对「作品」要求，不对人。** 人物条目的体例本来就是「只写方法论
那一部分」，条目正文里说得出来；而一部书是一个整体，读者会整本去读它。
所以判据的范围钉死在 `hw_kind.WORKS` 上——`check_integrity` 校验这张表的
键和 WORKS **完全一致**，多一个少一个都红。多出来的那种最容易发生：
把一条从 WORKS 挪走了，这里忘了删。

**`None` 是合法答案，而且是多数。**《孙子兵法》《系统之美》《原子习惯》
这些整本就是方法论，没有要声明的部分。写 `None` 不丢人——这张表逼的不是
「每本都得有个免责声明」，是**每本都得被问过这一句**。
（照 wikigate 的口径：不逼你造闸，只逼你把账认了。）

**写的时候：**
  · 指名道姓说是哪一部分，不要写「书中有些内容不适合今天」这种话——
    那种句子对任何一本书都成立，等于没写。
  · 说「我们不取」，不说「这本书错了」。判断是我们的，不是替古人认错。
  · 一到两句。它出现在「今天怎么用」之前，不该把读者拦在那儿。

格式：条目名 → (中文, English) 或 None。
"""

OMIT = {
    # ── 有明确不取的部分 ──────────────────────────────────
    "颜氏家训": (
        "不取它讲男女与门第的那一部分。《治家》篇里「妇主中馈」「国不可使预政，"
        "家不可使干蛊」是六世纪士族的家内秩序，和它讲因果、讲时机、讲兄弟为什么"
        "变远的那几处不是一回事，也不互相支撑。我们取后者。",
        "We leave out the sections on women and on lineage. The passage in "
        "'Managing a Household' confining a wife to food and clothing and "
        "barring her from affairs of state is sixth-century gentry order; it "
        "neither supports nor is supported by the arguments about causation, "
        "timing and why brothers drift. Those are what we take."),
    "易经": (
        "不取占卜。同一套卦爻既是一张「什么时候该动、什么时候该等」的位置图，"
        "也是一套问卜的工具；我们只取前者，也不认为后者能预测什么。"
        "书里那些吉凶断语，在这个站里当成对处境的描述读，不当成结果的预告。",
        "We leave out divination. The same hexagrams serve both as a map of "
        "when to move and when to wait and as an oracle; we take the first "
        "and make no claim for the second. The auspicious and inauspicious "
        "verdicts are read here as descriptions of a position, not "
        "predictions of an outcome."),
    "薄伽梵歌": (
        "不取它的宗教与形上学部分。全篇大半在讲梵我、轮回与神的显现，"
        "那是一套信仰，不在这个站要回答的问题里。我们只取它讲做事的那一面："
        "怎么把注意力从收成搬回动作。",
        "We leave out the religious and metaphysical body of the poem. Most "
        "of it concerns Brahman, rebirth and the manifestation of the divine, "
        "which is a faith and not a question this site answers. We take the "
        "part about acting: how to move attention off the harvest and back "
        "onto the work."),
    "论语": (
        "不取它的礼制细节和等级安排。哪一级用几鼎、丧服该穿多久，这些是周代"
        "社会的具体规定，不是可以搬的道理。我们取的是它讲人怎么对人、"
        "怎么看人、怎么学的那些段落。",
        "We leave out the ritual detail and the ranked social order - how "
        "many vessels a given rank may use, how long mourning dress is worn. "
        "Those are specific Zhou regulations, not portable arguments. We take "
        "the passages on how people treat, read and learn from one another."),
    "战国策": (
        "不取它对权谋本身的欣赏。书里说客的手段常常是骗和挑拨，而叙述的语气"
        "是赞赏的。我们取的是它对「人在什么情势下会怎么选」的观察——"
        "那部分今天仍然成立；欣赏那一层不取。",
        "We leave out its relish for the manoeuvre itself. The persuaders in "
        "it often work by deceit and by setting people against each other, "
        "and the narration admires them for it. We take its observation of "
        "how people choose under pressure, which still holds; the admiration "
        "we do not."),

    # ── 判过，没有要声明的部分 ────────────────────────────
    "孙子兵法": None, "道德经": None, "史记": None, "资治通鉴": None,
    "智慧书": None, "菜根谭": None,
    "主权个人": None, "人类简史": None, "影响力": None, "创新者的窘境": None,
    "思考，快与慢": None, "乌合之众": None, "系统之美": None,
    "旧制度与大革命": None, "战争论": None, "国富论": None,
    "技术革命与金融资本": None, "国家为什么会失败": None,
    "有限与无限的游戏": None, "枪炮、病菌与钢铁": None, "稀缺": None,
    "非暴力沟通": None, "关键对话": None, "依恋理论": None, "原子习惯": None,
    "优秀的绵羊": None, "哈佛成人发展研究": None, "老鼠公园": None,
    "最后一版": None,
}


def zh(name):
    v = OMIT.get(name)
    return v[0] if v else ""


def en(name):
    v = OMIT.get(name)
    return v[1] if v else ""


def _by_slug():
    """slug → 条目名。英文链手上只有 slug，这张表的键是中文名。

    反查 hw_slugs 而不是再维护一份 slug 表：多一份就会漂。
    """
    import hw_slugs
    return {v: k for k, v in hw_slugs.SLUGS.items()}


def en_by_slug(slug):
    return en(_by_slug().get(slug, ""))


def mismatch(works):
    """这张表的键和 WORKS 对不上的地方。多一个少一个都算。"""
    keys = set(OMIT)
    return sorted(works - keys), sorted(keys - works)

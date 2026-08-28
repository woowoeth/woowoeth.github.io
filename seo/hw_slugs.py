# -*- coding: utf-8 -*-
"""Stable English slugs for Human World entries and topic hubs."""
import re
import unicodedata

SLUGS = {
    "孙子兵法": "sun-tzu",
    "毛泽东": "mao",
    "粟裕": "su-yu",
    "道德经": "tao-te-ching",
    "王阳明": "wang-yangming",
    "曾国藩": "zeng-guofan",
    "范蠡": "fan-li",
    "韩信": "han-xin",
    "刘邦": "liu-bang",
    "曹操": "cao-cao",
    "司马懿": "sima-yi",
    "诸葛亮": "zhuge-liang",
    "管仲": "guan-zhong",
    "巴菲特": "buffett",
    "查理·芒格": "munger",
    "李嘉诚": "li-ka-shing",
    "乔布斯": "jobs",
    "张一鸣": "zhang-yiming",
    "段永平": "duan-yongping",
    "稻盛和夫": "inamori",
    "马斯克": "musk",
    "黄仁勋": "huang",
    "彼得·蒂尔": "thiel",
    "任正非": "ren-zhengfei",
    "主权个人": "sovereign-individual",
    "张良": "zhang-liang",
    "李泌": "li-bi",
    "韩非子": "han-feizi",
    "霍去病": "huo-qubing",
    "李世民": "li-shimin",
    "苏格拉底": "socrates",
    "马可·奥勒留": "marcus-aurelius",
    "马基雅维利": "machiavelli",
    "达里奥": "dalio",
    "塔勒布": "taleb",
    "纳瓦尔": "naval",
    "王兴": "wang-xing",
    "战国策": "strategies-of-the-warring-states",
    "论语": "analects",
    "人类简史": "sapiens",
    "项羽": "xiang-yu",
    "武则天": "wu-zetian",
    "张居正": "zhang-juzheng",
    "苏轼": "su-shi",
    "尼采": "nietzsche",
    "弗兰克尔": "frankl",
    "索罗斯": "soros",
    "影响力": "influence",
    "创新者的窘境": "innovators-dilemma",
    "郭嘉": "guo-jia",
    "李小龙": "bruce-lee",
    "史记": "records-of-the-grand-historian",
    "资治通鉴": "zizhi-tongjian",
    "甘地": "gandhi",
    "爱因斯坦": "einstein",
    "商鞅": "shang-yang",
    "凯撒": "caesar",
    "曼德拉": "mandela",
    "拿破仑": "napoleon",
    "宫本武藏": "musashi",
    "庄子": "zhuangzi",
    "郭子仪": "guo-ziyi",
    "富兰克林": "franklin",
    "格雷厄姆": "graham",
    "利弗莫尔": "livermore",
    "思考，快与慢": "thinking-fast-and-slow",
    "乌合之众": "crowd",
    "贝索斯": "bezos",
    "系统之美": "thinking-in-systems",
    "旧制度与大革命": "old-regime",
    "战争论": "on-war",
    "托马斯·谢林": "schelling",
    "胡雪岩": "hu-xueyan",
    "国富论": "wealth-of-nations",
    "爱比克泰德": "epictetus",
    "白圭": "bai-gui",
    "安迪·格鲁夫": "grove",
    "技术革命与金融资本": "technological-revolutions",
    "霍华德·马克斯": "marks",
    "冯道": "feng-dao",
    "六祖慧能": "huineng",
    "吉姆·西蒙斯": "simons",
    "彼得·林奇": "lynch",
    "智慧书": "art-of-worldly-wisdom",
    "国家为什么会失败": "why-nations-fail",
    "李光耀": "lee-kuan-yew",
    "约翰·博伊德": "boyd",
    "鬼谷子": "guiguzi",
    "拉罗什富科": "la-rochefoucauld",
    "保罗·格雷厄姆": "paul-graham",
    "松下幸之助": "matsushita",
    "有限与无限的游戏": "finite-and-infinite-games",
    "枪炮、病菌与钢铁": "guns-germs-steel",
}

TAG_SLUGS = {
    "工业时代": "industrial-age",
    "现代": "modern",
    "先秦与古典时代": "classical-era",
    "典籍·洞见": "classics",
    "典籍洞见": "classics",
    "创业·产品": "startups",
    "创业产品": "startups",
    "处世·人性": "human-nature",
    "处世人性": "human-nature",
    "战略·博弈": "strategy",
    "战略博弈": "strategy",
    "心智·哲学": "mind",
    "心智哲学": "mind",
    "权力·治理": "power",
    "权力治理": "power",
    "财富·投资": "wealth",
    "财富投资": "wealth",
    "中古": "medieval",
    "秦汉至魏晋": "han-wei",
    "近世": "early-modern",
}


def cjk_slug(s, fallback="item"):
    s = unicodedata.normalize("NFKD", str(s or ""))
    out = []
    for ch in s.lower():
        if ch.isalnum() and ord(ch) < 128:
            out.append(ch)
        elif "一" <= ch <= "鿿":
            out.append(ch)
        elif ch in " -_/.":
            out.append("-")
    s = re.sub(r"-{2,}", "-", "".join(out)).strip("-")
    return (s or fallback)[:80]


def slug_for(name):
    if name in SLUGS:
        return SLUGS[name]
    if name in TAG_SLUGS:
        return TAG_SLUGS[name]
    # Glyph-safe aliases (D[] uses rare variants that sometimes mangle in editors)
    if name.startswith("王") and name not in ("王阳明", "王兴") and len(name) == 2:
        return "wang-jian"
    if name.startswith("朱元"):
        return "zhu-yuanzhang"
    return cjk_slug(name)


def js_map():
    pairs = ",".join('"%s":"%s"' % (k.replace("\\", "\\\\").replace('"', '\\"'), v)
                     for k, v in SLUGS.items())
    return "const HW_SLUGS={%s};" % pairs

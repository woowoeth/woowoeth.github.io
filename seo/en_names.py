# -*- coding: utf-8 -*-
"""英文站上每个人（和每本书）的**名字与分类**，一处定死。

为什么要有这个文件：补齐 159 条是并行的活，而条目之间要互相引用
（l / contrast 里写的是名字，不是 slug）。名字各批各起，「Zhuge Liang」
和「Zhu Ge Liang」就会同时存在，交叉引用当场断掉 —— 而每一批单独看都对。
所以名字不是内容，是**接口**，必须先定后写。

分类名也在这里：中文十类，英文十类，一一对应。
scripts/check_batch.py 会拿这张表核对每条新条目的 n 和 c。
"""

# 英文分类名 ← 中文分类名。配色在 scripts/hwx_en.py 的 CAT_COLOR。
CATEGORY = {
    "谋略与竞争": "Strategy and competition",
    "权力与组织": "Power and organisation",
    "创业与产品": "Starting and building",
    "财富与风险": "Money and risk",
    "识人与相处": "Reading people",
    "心智与情绪": "Mind and feeling",
    "学习与成长": "Learning and growth",
    "身心与生活": "Body and daily life",
    "家庭与关系": "Family and relationships",
    "世界如何运转": "How the world works",
}

# slug → (英文名, 英文分类)
NAMES = {
    # ── Power and organisation ──
    "arendt": ("Hannah Arendt", "Power and organisation"),
    "bismarck": ("Otto von Bismarck", "Power and organisation"),
    "cao-cao": ("Cao Cao", "Power and organisation"),
    "feng-dao": ("Feng Dao", "Power and organisation"),
    "guan-zhong": ("Guan Zhong", "Power and organisation"),
    "guo-ziyi": ("Guo Ziyi", "Power and organisation"),
    "lee-kuan-yew": ("Lee Kuan Yew", "Power and organisation"),
    "li-bi": ("Li Bi", "Power and organisation"),
    "li-shimin": ("Li Shimin", "Power and organisation"),
    "liu-bang": ("Liu Bang", "Power and organisation"),
    "mencius": ("Mencius", "Power and organisation"),
    "shang-yang": ("Shang Yang", "Power and organisation"),
    "wu-zetian": ("Wu Zetian", "Power and organisation"),
    "xunzi": ("Xunzi", "Power and organisation"),
    "zhang-juzheng": ("Zhang Juzheng", "Power and organisation"),
    "zhang-liang": ("Zhang Liang", "Power and organisation"),
    "zhu-yuanzhang": ("Zhu Yuanzhang", "Power and organisation"),
    "zhuge-liang": ("Zhuge Liang", "Power and organisation"),
    "zizhi-tongjian": ("The Comprehensive Mirror", "Power and organisation"),
    # ── Strategy and competition ──
    "caesar": ("Julius Caesar", "Strategy and competition"),
    "guo-jia": ("Guo Jia", "Strategy and competition"),
    "han-xin": ("Han Xin", "Strategy and competition"),
    "huo-qubing": ("Huo Qubing", "Strategy and competition"),
    "i-ching": ("The I Ching", "Strategy and competition"),
    "mao": ("Mao Zedong", "Strategy and competition"),
    "musashi": ("Miyamoto Musashi", "Strategy and competition"),
    "napoleon": ("Napoleon", "Strategy and competition"),
    "on-war": ("On War", "Strategy and competition"),
    "schelling": ("Thomas Schelling", "Strategy and competition"),
    "sima-yi": ("Sima Yi", "Strategy and competition"),
    "strategies-of-the-warring-states":
        ("Strategies of the Warring States", "Strategy and competition"),
    "su-yu": ("Su Yu", "Strategy and competition"),
    "wang-jian": ("Wang Jian", "Strategy and competition"),
    "xiang-yu": ("Xiang Yu", "Strategy and competition"),
    # ── Reading people ──
    "analects": ("The Analects", "Reading people"),
    "art-of-worldly-wisdom": ("The Art of Worldly Wisdom", "Reading people"),
    "caigentan": ("Tending the Roots of Wisdom", "Reading people"),
    "chris-voss": ("Chris Voss", "Reading people"),
    "crowd": ("The Crowd", "Reading people"),
    "gandhi": ("Gandhi", "Reading people"),
    "guiguzi": ("Guiguzi", "Reading people"),
    "influence": ("Influence", "Reading people"),
    "konnikova": ("Maria Konnikova", "Reading people"),
    "la-rochefoucauld": ("La Rochefoucauld", "Reading people"),
    "machiavelli": ("Machiavelli", "Reading people"),
    "mandela": ("Nelson Mandela", "Reading people"),
    "nonviolent-communication": ("Nonviolent Communication", "Reading people"),
    "zeng-guofan": ("Zeng Guofan", "Reading people"),
    # ── Starting and building ──
    "chu-shijian": ("Chu Shijian", "Starting and building"),
    "drucker": ("Peter Drucker", "Starting and building"),
    "duan-yongping": ("Duan Yongping", "Starting and building"),
    "grove": ("Andy Grove", "Starting and building"),
    "huang": ("Jensen Huang", "Starting and building"),
    "inamori": ("Kazuo Inamori", "Starting and building"),
    "innovators-dilemma": ("The Innovator's Dilemma", "Starting and building"),
    "kevin-kelly": ("Kevin Kelly", "Starting and building"),
    "matsushita": ("Konosuke Matsushita", "Starting and building"),
    "ohno": ("Taiichi Ohno", "Starting and building"),
    "ren-zhengfei": ("Ren Zhengfei", "Starting and building"),
    "wang-xing": ("Wang Xing", "Starting and building"),
    "zhang-yiming": ("Zhang Yiming", "Starting and building"),
    # ── Mind and feeling ──
    "augustine": ("Augustine", "Mind and feeling"),
    "bhagavad-gita": ("The Bhagavad Gita", "Mind and feeling"),
    "brene-brown": ("Brené Brown", "Mind and feeling"),
    "epictetus": ("Epictetus", "Mind and feeling"),
    "frankl": ("Viktor Frankl", "Mind and feeling"),
    "franklin": ("Benjamin Franklin", "Mind and feeling"),
    "kristin-neff": ("Kristin Neff", "Mind and feeling"),
    "marcus-aurelius": ("Marcus Aurelius", "Mind and feeling"),
    "montaigne": ("Montaigne", "Mind and feeling"),
    "nietzsche": ("Nietzsche", "Mind and feeling"),
    "seneca": ("Seneca", "Mind and feeling"),
    "sima-qian": ("Sima Qian", "Mind and feeling"),
    # ── Money and risk ──
    "bai-gui": ("Bai Gui", "Money and risk"),
    "dalio": ("Ray Dalio", "Money and risk"),
    "graham": ("Benjamin Graham", "Money and risk"),
    "hu-xueyan": ("Hu Xueyan", "Money and risk"),
    "livermore": ("Jesse Livermore", "Money and risk"),
    "lynch": ("Peter Lynch", "Money and risk"),
    "marks": ("Howard Marks", "Money and risk"),
    "scarcity": ("Scarcity", "Money and risk"),
    "simons": ("Jim Simons", "Money and risk"),
    "soros": ("George Soros", "Money and risk"),
    "taleb": ("Nassim Taleb", "Money and risk"),
    "technological-revolutions":
        ("Technological Revolutions", "Money and risk"),
    # ── Learning and growth ──
    "bruce-lee": ("Bruce Lee", "Learning and growth"),
    "einstein": ("Albert Einstein", "Learning and growth"),
    "ericsson": ("Anders Ericsson", "Learning and growth"),
    "feynman": ("Richard Feynman", "Learning and growth"),
    "fukuzawa": ("Fukuzawa Yukichi", "Learning and growth"),
    "hot-metal": ("The Last Hot-Metal Edition", "Learning and growth"),
    "murakami": ("Haruki Murakami", "Learning and growth"),
    "popper": ("Karl Popper", "Learning and growth"),
    "socrates": ("Socrates", "Learning and growth"),
    "thinking-fast-and-slow":
        ("Thinking, Fast and Slow", "Learning and growth"),
    # ── How the world works ──
    "finite-and-infinite-games":
        ("Finite and Infinite Games", "How the world works"),
    "guns-germs-steel": ("Guns, Germs, and Steel", "How the world works"),
    "hayek": ("Friedrich Hayek", "How the world works"),
    "old-regime": ("The Old Regime and the Revolution", "How the world works"),
    "records-of-the-grand-historian":
        ("Records of the Grand Historian", "How the world works"),
    "sapiens": ("Sapiens", "How the world works"),
    "sovereign-individual": ("The Sovereign Individual", "How the world works"),
    "thinking-in-systems": ("Thinking in Systems", "How the world works"),
    "wealth-of-nations": ("The Wealth of Nations", "How the world works"),
    "why-nations-fail": ("Why Nations Fail", "How the world works"),
    # ── Body and daily life ──
    "atomic-habits": ("Atomic Habits", "Body and daily life"),
    "bj-fogg": ("BJ Fogg", "Body and daily life"),
    "cal-newport": ("Cal Newport", "Body and daily life"),
    "csikszentmihalyi":
        ("Mihaly Csikszentmihalyi", "Body and daily life"),
    "du-fu": ("Du Fu", "Body and daily life"),
    "kleinman": ("Arthur Kleinman", "Body and daily life"),
    "shi-tiesheng": ("Shi Tiesheng", "Body and daily life"),
    "tao-yuanming": ("Tao Yuanming", "Body and daily life"),
    # ── Family and relationships ──
    "adler": ("Alfred Adler", "Family and relationships"),
    "attachment-theory": ("Attachment Theory", "Family and relationships"),
    "bowen": ("Murray Bowen", "Family and relationships"),
    "carl-rogers": ("Carl Rogers", "Family and relationships"),
    "crucial-conversations":
        ("Crucial Conversations", "Family and relationships"),
    "satir": ("Virginia Satir", "Family and relationships"),
}

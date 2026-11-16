# -*- coding: utf-8 -*-
"""Daily entry: Lu Buwei.

From DAILY_QUEUE.md row 12. 'I don't know what to charge' holds entries on pricing high, price as a
signal of worth, and setting the price before the costs. None of them says that the same thing is worth
different amounts to different buyers, and that the work is finding the one who lacks it. The second
chapter is hung on 'They've started watching me': dismissed and sent home, he still had envoys on the
road to his door, and the king's letter asked what service and what kinship he had.

Why he qualifies: chancellor of Qin under King Zhuangxiang and the young King Zheng, with his own
biography in Sima Qian's Records of the Grand Historian. Only that biography is used here.

The entry story is his rise to chancellor and Second Father; the chapters are the hostage deal and the
fall. The Annals compiled by his guests have their own page and are not repeated.
"""

ENTRIES = [
    {
        "c": "Money and risk",
        "n": "Lu Buwei",
        "slug": "lu-buwei",
        "e": "Warring States Qin · died 235 BC",
        "w": "The bet", "y": -249,
        "d": "A great merchant of the late Warring States period with his own biography in Sima Qian's Records. In the "
             "Zhao capital he spotted Zichu, a neglected Qin prince held as a hostage, spent a fortune getting the childless "
             "Lady Huayang to adopt him as heir, and became chancellor when Zichu took the throne. Dismissed by the next king, "
             "he died by poison. He is here because no entry yet says a thing's price depends on who lacks it.",
        "story":
            "Zichu took the throne as King Zhuangxiang. In his first year he made Lu Buwei chancellor, ennobled him and "
            "gave him the revenue of a hundred thousand households in Henan. Three years later the king died and the young "
            "crown prince Zheng succeeded, made Lu chancellor of state and called him Second Father. By then Lu's household "
            "had ten thousand servants. Some fifteen years earlier he had been a merchant buying cheap and selling dear.",
        "f": [
            {"n": "Buying cheap and selling dear was his trade",
             "d": "He made his fortune travelling between markets, buying low and selling high. He judged people the same way: get in while nobody rates the thing, and collect once its worth shows.",
             "eg": "Whatever everyone is already scrambling for has already had its price run up."},
            {"n": "My gate grows when yours does",
             "d": "At their first meeting he told Zichu he could make his house great. Zichu laughed and told him to make his own house great first. Lu answered that his house would only grow once Zichu's did. Zichu understood and sat him down to talk.",
             "eg": "When you pitch a partnership, show first that your gain is tied to theirs."},
            {"n": "He staked everything he had",
             "d": "He told Zichu that although he was not rich he would spend a thousand pieces of gold on his behalf. That was the whole fortune his trade had built. The bet paid a hundred thousand households, but it rested on one man.",
             "eg": "Before you put everything on one client or one boss, decide what you do if they go."},
        ],
        "apply": "This week write down your largest stake, money, time or a relationship, and one more line: whose success "
                 "is it riding on, and what would you still hold if that person left?",
        "q": [
            "From merchant to chancellor, with one man in between.",
            "My gate grows when yours does.",
            "Stake everything on one person and you win or lose with them.",
        ],
        "l": ["Fan Li", "Bai Gui", "The Annals of Lu Buwei"],
        "contrast": [
            {"n": "Fan Li", "why": "Fan Li was also a strategist turned merchant, but he left at the height of his success and later gave away his wealth more than once. Lu Buwei stayed on his estate after his dismissal with envoys at his gate and died over one letter from the king. One knew when to take his stake off the table; the other stepped down and left the door open."},
        ],
    },
]

INTROS = {
    "lu-buwei":
        "A Warring States merchant who called a neglected hostage prince a rare commodity, bought him the succession "
        "and became chancellor of Qin - until the next king wrote asking what he had ever done for Qin",
}

SCENES = [
    ("I don't know what to charge", "Dealing with people", [
        ("Nobody here takes it seriously. What do I ask for it?",
         [("lu-buwei", "rare-goods")]),
    ]),
    ("They've started watching me", "Dealing with people", [
        ("I've already stepped down. Why don't they trust me?",
         [("lu-buwei", "what-merit")]),
    ]),
]

ASKS = {
    "lu-buwei/rare-goods": "Nobody here takes it seriously. What do I ask for it?",
    "lu-buwei/what-merit": "I've already stepped down. Why don't they trust me?",
}

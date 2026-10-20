# -*- coding: utf-8 -*-
"""Daily entry: Zichan.

Picked by fan-out. 'They don't believe I mean it' (one of the emptiest) holds
Schelling on binding yourself and Wang Jian on being cut down to half of what
he asked. Nothing on the smaller party facing a bigger one: how to answer when
they price you like a big player, and when they ask for 'only a little' and the
first yes would set the price of every later one.

Why he qualifies: chief minister of Zheng for over twenty years in the sixth
century BC, one of the leading statesmen of the Spring and Autumn period, with
his deeds recorded at length in the Zuo Commentary and a biography in Sima
Qian's Records of the Grand Historian.

The entry story is the street song about him in his first and third years of
office; the chapters are Pingqiu (Duke Zhao 13) and the jade ring (Duke Zhao 16).
"""

ENTRIES = [
    {
        "c": "Power and organisation",
        "n": "Zichan",
        "slug": "zichan",
        "e": "Spring and Autumn · Zheng · d. 522 BC",
        "w": "Standing on the rule", "y": -529,
        "d": "Gongsun Qiao, known as Zichan, ran the state of Zheng for over twenty years in the sixth century BC. "
             "Zheng sat between two great powers, Jin and Chu, and he dealt with both without grovelling to either, "
             "while setting rules at home. The Zuo Commentary records his deeds at length, and Sima Qian gave him a "
             "biography among the 'upright officials'. This page takes one thing from him: how a small state talks "
             "to a far bigger one. Quote a rule the other side already accepts, then state your difficulty, and when "
             "they ask for something small, work out what the first yes will cost every day after it.",
        "story":
            "In his first year running Zheng, the people sang a song against Zichan: take away my clothes and cap, "
            "carve my fields into groups of five households, and whoever kills Zichan, I will join him. In the third "
            "year the words changed: if I have sons, Zichan teaches them; if I have fields, Zichan feeds them; if "
            "Zichan dies, who will take his place?",
        "f": [
            {"n": "Speak from the other side's own rule",
             "d": "At Pingqiu, Jin wanted little Zheng to pay tribute at a marquis's rate. He did not open with hardship. "
                  "He set out the Zhou schedule of tribute by rank, then said Zheng could not meet that figure. The other "
                  "side can dispute your hardship, but it is hard to deny its own rule.",
             "eg": "Given a big-client price, you show the price list they quote to firms your size before you state your budget."},
            {"n": "The first price is every later price",
             "d": "Han Xuanzi wanted a jade ring and others urged giving it. Zichan counted the future: if a great state's "
                  "envoys get whatever they ask for, nothing is left to give later, and a yes followed by a no offends more "
                  "than a no at the start. He refused the way the thing was asked for, not Jin.",
             "eg": "A client gets one free feature from you in the first quarter; by the next, as far as he is concerned, it is in the contract."},
            {"n": "Firm outside because something is done inside",
             "d": "He reorganised the fields and the taxes; for a year the people cursed him and by the third they hoped "
                  "he would not die. A small state's chief minister could argue until dark in front of Jin because "
                  "there were people at home on his side.",
             "eg": "Before you bargain with the people above you, check you hold one finished result they can see."},
        ],
        "apply": "Pick one condition you will negotiate next week and write two lines: the rule the other side already accepts; and, "
                 "if I give way this once, what reason I will have to refuse next time. If you cannot write the second line, do not give way yet.",
        "q": [
            "Covenants are sworn to keep small states alive.",
            "Yield once and refuse once, and the offence is worse.",
            "A state that will not contest is trampled all the same.",
        ],
        "l": ["Yan Ying", "Lin Xiangru", "Strategies of the Warring States", "Guan Zhong"],
        "contrast": [
            {"n": "Thomas Schelling", "why": "Both write about the weaker party in a negotiation. Schelling teaches you to tie your own hands so the other side knows you cannot retreat; Zichan ties nothing, he finds the rule the other side has already accepted so it cannot call him wrong. One works by commitment, the other by the opponent's own words."},
            {"n": "Lin Xiangru", "why": "Both held out for a small state against a great one. Lin Xiangru did it with nerve in a single confrontation in front of the king of Qin; Zichan did it with an old rule and a day-long argument. One is a moment, the other is an afternoon."},
        ],
    },
]

INTROS = {
    "zichan":
        "Chief minister of the small state of Zheng - at a covenant he argued "
        "from noon until dark to cut Jin's tribute demand, citing the rule Jin "
        "itself accepted; and when Jin's envoy asked for one jade ring, he "
        "refused, and cited an oath both sides had sworn",
}

SCENES = [
    ("They don't believe I mean it", "Facing an opponent", [
        ("They price me like a big player, and I am small. How do I bargain?",
         [("zichan", "noon-to-dusk")]),
        ("It is only a small ask. Why not give it once?",
         [("zichan", "the-pair-of-rings")]),
    ]),
]

ASKS = {
    "zichan/noon-to-dusk": "They price me like a big player, and I am small. How do I bargain?",
    "zichan/the-pair-of-rings": "It is only a small ask. Why not give it once?",
}

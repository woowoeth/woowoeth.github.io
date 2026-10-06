# -*- coding: utf-8 -*-
"""Daily entry, day 26: The Duke of Zhou.

Picked by fan-out. 'They've started watching me' (Chinese side 被猜忌, 9),
'Nobody tells me the bad news' (听不到实话, 10) and 'Should I step back'
(该不该退, 12) were among the emptiest. Under suspicion hang Guo Ziyi, Wang
Jian, Han Xin: shrink yourself, or leave. Nobody says what to do when you
cannot leave because the work needs you. Under bad news hang Li Shimin and
the Warring States texts on mirrors; nobody is the person who walks out
mid-bath. Under stepping back hang Fan Li and Lee Kuan Yew on when and how;
nobody says where to stand afterwards. The duke says all three, in Sima Qian.

His standing: regent of early Zhou, brother of King Wu, the figure Confucius
named as the model of a statesman (Analects, Taibo; Records of the Grand
Historian, Hereditary House of the Duke of Zhou of Lu). The last entries were
Keynes (foreign), Xiao He and King Wuling (Chinese), so pick_balance is
green; this is a third Chinese pick.

Three scenes, no overlap: the entry is the prayer found in the vault; chapter
one is the rumour; chapter two the speech to his son; chapter three the
handover. Quoted lines are our renderings of the Chinese. All three
situations already exist, so no SC_BOX.
"""

ENTRIES = [
    {
        "c": "Power and organisation",
        "n": "The Duke of Zhou",
        "slug": "zhou-gong",
        "e": "Early Zhou · c. 11th century BC",
        "w": "Regency",
        "y": -1040,
        "d": "Son of King Wen and brother of King Wu of Zhou, named Dan, "
             "later enfeoffed in the state of Lu. When King Wu died and the "
             "heir was a child, he ran the state in the boy's name, put down "
             "his brothers' revolt, and when the king came of age handed "
             "the rule back. This page takes only three things: how he met "
             "a rumour, how he treated people far below him, and how he "
             "handed over power. It does not discuss his rites and "
             "institutions. He left three methods. When you are suspected, "
             "first tell the people carrying the load with you. The higher "
             "your seat, the more you must keep the door open. Hand over "
             "clean, and let everyone see where you now stand.",
        "story": "According to Sima Qian, when King Cheng was a child and "
                 "gravely ill, the Duke of Zhou cut off his own fingernails "
                 "and sank them in the river, praying that if any spirit "
                 "was offended, it was he, Dan, and not the boy. He put the "
                 "prayer away in the royal archive. Later, after the king "
                 "took charge, someone slandered the duke and he left for "
                 "the south. Cheng opened the archive, found the prayer, "
                 "wept, and brought him back.",
        "f": [
            {"n": "He did not hide, and did not defend himself first",
             "d": "When it was said he meant to harm the king, he neither argued nor left. He went to the two elders carrying the work with him and explained why he could not step aside: if he did, the realm would turn against Zhou.",
             "eg": "People say you are after the project. Sit down with the two or three people who build it with you, then finish the job."},
            {"n": "He kept his door open",
             "d": "He told his son that in one bath he grabbed his hair three times to go out to a visitor, and in one meal he stood up three times. The higher you sit, the less people tell you, so push the cost of seeing you down yourself.",
             "eg": "Keep ninety minutes a week empty, and see whoever turns up."},
            {"n": "He handed over, and stepped back to his place",
             "d": "When the king grew up, the duke gave back the rule and moved from the seat facing south to stand among the ministers. Handing over meant giving up the decisions, and moving his place so everyone could see it.",
             "eg": "At the first meeting after a handover, leave the head of the table to the new lead."},
        ],
        "apply": "Pick one matter where you are suspected and cannot walk away. "
                 "Write three lines: if I step aside, does anyone pick it up; "
                 "which two or three people carrying it with me should hear "
                 "my reasons first; what will let the work speak for me. If "
                 "your seat is already high, count how long it has been since "
                 "someone said what I did not want to hear. His one "
                 "judgement runs through all three: look at the work first, "
                 "and at what people say second.",
        "q": ["I do not step aside because I fear the realm will turn against Zhou.",
              "One bath, three times I seize my hair; one meal, three times I rise.",
              "Bury me at Chengzhou, to show I dare not leave King Cheng."],
        "l": ["Guo Ziyi", "Li Shimin", "Zhang Liang", "Shang Yang"],
        "contrast": [
            {"n": "Guo Ziyi",
             "why": "Both were suspected by their courts. Guo Ziyi made "
                    "himself smaller: he opened his gates and let anyone "
                    "walk in, showing he was harmless. The duke would not "
                    "hide. He told those carrying the work with him, and let "
                    "the finished work answer. One showed he was no threat, "
                    "the other showed the work could not do without him"},
            {"n": "Li Shimin",
             "why": "Both wanted to hear the uncomfortable thing. Li Shimin "
                    "relied on ministers like Wei Zheng and tolerated being "
                    "contradicted. The duke opened the door first and went "
                    "out to meet people with his hair still wet. One relied "
                    "on tolerance, the other on lowering the cost of reaching him"},
        ],
    },
]

INTROS = {
    "zhou-gong": "An early Zhou statesman, brother of a king, who ran the state for "
                 "a boy-king for seven years. When rumours said he wanted the throne, "
                 "he stayed. He went out to meet visitors with his hair still wet. "
                 "When the king grew up, he gave the power back and stood among the ministers.",
}

SCENES = [
    ("They've started watching me", "Dealing with people", [
        ("They say I want the top job. Do I step aside, or stay?",
         [("zhou-gong", "not-stepping-aside")]),
    ]),
    ("Nobody tells me the bad news", "Leading people", [
        ("The higher I climb, the less I hear.",
         [("zhou-gong", "one-wash-three-times")]),
    ]),
    ("Should I step back", "When to step back", [
        ("I handed it over. Where do I stand now?",
         [("zhou-gong", "back-to-the-ministers-place")]),
    ]),
]

ASKS = {
    "zhou-gong/not-stepping-aside":
        "They say I want the top job. Do I step aside, or stay?",
    "zhou-gong/one-wash-three-times":
        "The higher I climb, the less I hear.",
    "zhou-gong/back-to-the-ministers-place":
        "I handed it over. Where do I stand now?",
}

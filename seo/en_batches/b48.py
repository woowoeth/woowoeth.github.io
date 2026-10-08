# -*- coding: utf-8 -*-
"""Daily entry, day 28: Yan Ying.

Picked by fan-out. 'Nobody tells me the bad news' (Chinese side 身边人不敢跟我说真话, 9),
'Persuading someone' (要说服人, 12) and 'Everyone says it's great' (全票通过, 14)
were among the emptiest. Under 'they don't tell me the truth' hang Carl
Rogers, Cao Cao burning the letters and the Warring States on mirrors: how
the person on top should react. Nobody is the minister who has to say it
upward, and nobody is the man who got told to his face and had to answer.
'Harmony is not sameness' is already covered by the Analects, so Yan Ying's
well-known soup speech is left out on purpose; this page takes his other
two scenes.

His standing: chief minister of Qi under three dukes, paired with Guan Zhong
in Sima Qian's Biographies of Guan and Yan; Confucius praised how he kept
friends (Analects 5.17). The last entries were Zhao Wuling, the Duke of Zhou
(Chinese) and Thucydides (foreign), so pick_balance is green.

Three scenes, no overlap: the entry is the charioteer's wife, chapter one the
price of shoes, chapter two the man he ransomed. Quoted lines are our own
renderings of the Zuo Commentary and Sima Qian. Both situations already
exist, so no SC_BOX.
"""

ENTRIES = [
    {
        "c": "Power and organisation",
        "n": "Yan Ying",
        "slug": "yan-ying",
        "e": "Spring and Autumn · Qi · d. 500 BC",
        "w": "Remonstrance",
        "y": -539,
        "d": "Chief minister of the state of Qi under three dukes, paired "
             "with Guan Zhong in Sima Qian's Biographies of Guan and Yan. "
             "This page takes only three things: how he got a truth across "
             "to the man above him, how he took being told to his face that "
             "he was wrong, and how he treated his own seat. It leaves out "
             "his frugality and his diplomatic wit. He left three methods. "
             "To be heard from below, hand over a figure the listener can "
             "check himself. When told you were wrong, listen to the end "
             "and then let the man see that you changed. The higher your "
             "seat, the more you need people who dare to hold up a mirror.",
        "story": "According to Sima Qian, Yan Ying's charioteer drove four "
                 "horses under a tall canopy, swaggering and pleased with "
                 "himself. When he got home, his wife said she was leaving. "
                 "Yan Ying, she said, is under six feet tall and chief "
                 "minister of Qi, famous among the lords, yet when I saw "
                 "him go out he looked like a man who thought he fell "
                 "short. You are eight feet tall and a charioteer, and "
                 "you seem satisfied. The man began to hold himself in. "
                 "Yan Ying noticed, asked, and was told the truth. He "
                 "recommended the charioteer for office.",
        "f": [
            {"n": "He got a truth across with one figure",
             "d": "Duke Jing's punishments were heavy. Yan Ying did not say so; he answered that the shoes for the maimed were dear and ordinary shoes cheap. Criticism makes people defend themselves; a price does not.",
             "eg": "Not 'you squeeze sales too hard,' but 'of the seven who left this quarter, five were in sales.'"},
            {"n": "He listened to the end when told he was wrong",
             "d": "After he ransomed Yue Shifu, the man asked to break off the friendship. Yan Ying straightened his robes, apologised, heard him out and made him an honoured guest. People speak up when your position visibly moves afterwards.",
             "eg": "Someone says you gave him no face last time. Put his point on the next meeting's agenda and let him present it."},
            {"n": "He used the people who could see him",
             "d": "The charioteer's wife had watched the chief minister leave the house looking like he fell short. Yan Ying did not resent a charioteer's wife judging him; he used her eyes, and made her husband an officer.",
             "eg": "Someone says you talk too much in meetings. Ask him which meeting, and which sentence."},
        ],
        "apply": "Pick one thing you want to tell someone above you and fear "
                 "will not land. Write three lines: what figure can he check "
                 "himself; whether it helps me finish the sentence or lets me "
                 "walk around it; whether it points at the real wound. If "
                 "you are the one in the high seat, count how many sentences "
                 "you let someone finish the last time he said you were "
                 "wrong. His one judgement runs through all three: say it "
                 "so that it can be heard, and be someone it can be said to.",
        "q": ["Shoes for the maimed are dear; ordinary shoes are cheap.",
              "To know me and show me no courtesy is worse than a cell.",
              "Were Yan Zi alive, I would gladly hold his whip."],
        "l": ["Guan Zhong", "Li Shimin", "Han Feizi", "The Analects"],
        "contrast": [
            {"n": "Li Shimin",
             "why": "Both are about getting words across between above and "
                    "below. Li Shimin sat above, and with ministers like "
                    "Wei Zheng he could stand to be contradicted. Yan Ying "
                    "stood below, did not contradict, and handed over a "
                    "figure so the man above could see it for himself. One "
                    "teaches how to listen, the other how to speak"},
            {"n": "Han Feizi",
             "why": "Both guard against being walled in by the people "
                    "around you. Han Feizi relies on technique and audit, "
                    "against ministers who hide things. Yan Ying relies on "
                    "being someone people dare to tell, and on hearing the "
                    "man out when he is told he was wrong. One closes the "
                    "gaps from the system, the other opens up in himself first"},
        ],
    },
]

INTROS = {
    "yan-ying": "Chief minister of the state of Qi in the Spring and Autumn "
                "period. When his duke punished too harshly, he did not say "
                "so; he said that in the market shoes for the maimed were "
                "dear, and the duke eased the punishments. When a man he "
                "had ransomed demanded to break off the friendship, he "
                "straightened his robes and apologised first.",
}

SCENES = [
    ("I have one conversation to get right", "Dealing with people", [
        ("I want to tell my boss he's wrong, and I can't afford a head-on clash.",
         [("yan-ying", "price-of-shoes")]),
    ]),
    ("Nobody tells me the bad news", "Leading people", [
        ("They aren't ignorant. They just don't know how to say it to me.",
         [("yan-ying", "price-of-shoes")]),
    ]),
    ("Nobody says what they actually think", "Leading people", [
        ("Someone finally told me to my face I was out of line, and I'm stung.",
         [("yan-ying", "the-man-he-ransomed")]),
    ]),
]

ASKS = {
    "yan-ying/price-of-shoes":
        "I want to tell my boss he's wrong, and I can't afford a head-on clash.",
    "yan-ying/the-man-he-ransomed":
        "Someone finally told me to my face I was out of line, and I'm stung.",
}

# -*- coding: utf-8 -*-
"""Daily entry, day 19: Duke Wen of Jin.

Picked by fan-out. 'Should I leave this job' and 'I was betrayed' were among
the emptiest situations on the Chinese side, both at eight. What hangs under
leaving says how to weigh staying against going (Boyd, Hirschman, Becker);
nothing says that comfort itself is the warning, and that you may need
someone else to push. Under betrayal the pages are about partners (Gottman)
or retaliation (Axelrod); nothing covers the enemy who comes back with
something you need to hear. The third chapter covers backing off first in a
fight with someone you owe.

All quoted lines are our own renderings of the Chinese in the Zuo
Commentary (Duke Xi, years 23, 24 and 28).

Four stories, no overlap: the entry is the clod of earth at Wulu; the
chapters are Lady Jiang in Qi, the eunuch Pi, and the retreat at Chengpu.

All situations already exist, so there is no SC_BOX here.
"""

ENTRIES = [
    {
        "c": "Power and organisation",
        "n": "Duke Wen of Jin",
        "slug": "jin-wengong",
        "e": "Spring and Autumn · died 628 BCE",
        "w": "Taking advice", "y": -636,
        "d": "Ruler of the state of Jin, born Chong'er, a son of Duke Xian. "
             "Driven out in a palace feud, he fled in 655 BCE and spent "
             "nineteen years in exile across half a dozen states before Duke "
             "Mu of Qin escorted him home to take the throne in 636. In 632 "
             "he crushed Chu at Chengpu and became the leading lord of the "
             "age. He was no great strategist. At each turn the Zuo "
             "Commentary records, his first answer was no, and someone close "
             "to him changed his mind.",
        "story":
            "Passing through Wey in exile, Chong'er was treated without "
            "courtesy. At Wulu his party was starving, and they begged food "
            "from a farmer, who handed him a clod of earth. Chong'er was "
            "furious and reached for his whip. His uncle Zifan stopped him: "
            "this is a gift from heaven. Earth is land, and land is a state. "
            "Chong'er bowed, accepted the clod and loaded it on his carriage. "
            "He had already spent twelve years among the Di, and home was "
            "still seven or eight years away.",
        "f": [
            {"n": "Suspect the place you least want to leave",
             "d": "In Qi he was given a wife and eighty horses and settled in. "
                  "His wife told him that longing and ease ruin a name. When "
                  "he still refused, she and Zifan got him drunk and put him "
                  "in a carriage.",
             "eg": "The job is easy and kind, and you haven't asked where you "
                   "meant to go in three years."},
            {"n": "When someone who hurt you knocks, hear him out",
             "d": "The eunuch Pi had hunted him twice and once cut off his "
                  "sleeve. When plotters planned to burn the palace, Pi came "
                  "to warn him. The duke sent him away, then heard his "
                  "argument, saw him and escaped the fire.",
             "eg": "The rival who fought you hardest comes to see you. Hear "
                   "what he has to say before you decide."},
            {"n": "Everyone watches how you treat one person",
             "d": "The servant who ran off with his stores came back asking to "
                  "see him. The duke said he was washing his hair. The servant "
                  "sent word that a ruler's grudge against one small man "
                  "frightens many. The duke saw him at once.",
             "eg": "How you treat the colleague who nearly left is watched by "
                   "everyone else who wavered."},
            {"n": "Pay the debt, then see if they follow",
             "d": "In exile he promised the king of Chu that if their armies "
                  "met, Jin would fall back three stages. At Chengpu it did, "
                  "ninety li. The Chu general pressed on anyway, put himself "
                  "in the wrong, and was routed.",
             "eg": "Before you compete with someone who helped you, settle "
                   "what you owe them openly."},
        ],
        "apply":
            "If someone near you is saying what you don't want to hear, that "
            "you should leave a comfortable place, meet a person you resent, "
            "or give ground before a fight, don't answer no today. Write down "
            "what they said and read it again tomorrow. Ask whether it serves "
            "you or them. The duke did not always listen well; he still "
            "invaded Cao, whose ruler once spied on him in the bath. But he "
            "got home after nineteen years because a few people around him "
            "dared to finish their sentences, and in the end he let them.",
        "q": [
            "Longing and ease ruin a name.",
            "A ruler's command allows no second mind.",
            "When a ruler bears a grudge against a commoner, many are afraid.",
            "We fall back three stages to repay them.",
        ],
        "l": ["Guan Zhong", "Cao Cao", "Xiang Yu", "Feng Yi"],
        "contrast": [
            {"n": "Cao Cao",
             "why": "Both faced people who had wavered. After Guandu, Cao Cao "
                    "found letters his own officers had sent the enemy and "
                    "burned them unread, clearing a whole group at once. Duke "
                    "Wen faced them one at a time at his door, the man who "
                    "had hunted him and the servant who ran off with his "
                    "stores. He shut the door first, and opened it once they "
                    "had made their case."},
            {"n": "Xiang Yu",
             "why": "Both chose between comfort and the long road. Xiang Yu "
                    "took the Qin capital, longed to go home to Chu, and would "
                    "not hear the man who urged him to stay. Chong'er also "
                    "wanted to stay in Qi, and was pushed into a carriage by "
                    "his wife and his uncle. One had nobody able to stop him; "
                    "the other had people who dared."},
        ],
    },
]

INTROS = {
    "jin-wengong":
        "A ruler of ancient Jin who spent nineteen years in exile before "
        "taking his throne - no genius, he said no at every turn, and each "
        "time someone close to him talked him round",
}

SCENES = [
    ("Should I leave this job", "Dealing with people", [
        ("It's so comfortable here that it's starting to worry me.",
         [("jin-wengong", "ease-ruins-a-name")]),
    ]),
    ("Do I change direction now", "Looking back, moving on", [
        ("Life is easy here, and I know I shouldn't stop.",
         [("jin-wengong", "ease-ruins-a-name")]),
    ]),
    ("I was betrayed", "At home", [
        ("The man who once tried to ruin me is at my door.",
         [("jin-wengong", "the-cut-sleeve")]),
    ]),
    ("I trusted the wrong person", "Dealing with people", [
        ("He burned me once. Now he says he's here to help.",
         [("jin-wengong", "the-cut-sleeve")]),
    ]),
    ("It turned into a fight", "Making a call", [
        ("If I back off first, have I already lost?",
         [("jin-wengong", "three-stages-back")]),
        ("I owe him, and now we're about to fall out.",
         [("jin-wengong", "three-stages-back")]),
    ]),
]

ASKS = {
    "jin-wengong/ease-ruins-a-name":
        "It's so comfortable here that it's starting to worry me.",
    "jin-wengong/the-cut-sleeve":
        "The man who once tried to ruin me is at my door.",
    "jin-wengong/three-stages-back":
        "If I back off first, have I already lost?",
}

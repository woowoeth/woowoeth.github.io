# -*- coding: utf-8 -*-
"""Daily entry, day 25: King Wuling of Zhao.

Picked by fan-out. 'I can't keep up with the new thing' and 'Pushing others'
are among the emptiest situations (nine each). Under the first hang Fukuzawa,
Bruce Lee, Csikszentmihalyi, Feynman and Herbert Simon: how to practise, what
to chase, what to skip. Nobody says the shameful thing, that what blocks us
is learning from people we were raised to look down on. Under the second,
Li Bi and Zhang Liang say how to move people without rank, Zhu Yuanzhang
how to use force; nobody says what to do when the one who will not budge is
the elder everyone else is watching. Wuling says both, in Sima Qian.

His standing: ruler of one of the seven Warring States, the king whose
'nomad dress and mounted archery' reform is the textbook case of adopting an
outsider's method (Hereditary House of Zhao, Records of the Grand Historian).
The last entries were Porter, Keynes (foreign), Xiao He (Chinese), so
pick_balance is green with a Chinese pick.

Three scenes, no overlap: the entry is the result years on; chapter one is
the talk with Yi; chapter two is the visit to Prince Cheng. Quoted lines are
our renderings of the Chinese. Both situations already exist, so no SC_BOX.
The Chinese-side 'Pushing others' has no English twin, so chapter two hangs
under 'They said no to my plan'.
"""

ENTRIES = [
    {
        "c": "Power and organisation",
        "n": "King Wuling of Zhao",
        "slug": "zhao-wuling-wang",
        "e": "Warring States · Zhao · d. 295 BC",
        "w": "Nomad dress",
        "y": -307,
        "d": "King of Zhao, one of the seven Warring States, from 325 BC. "
             "He handed the throne to his son in 299 and died in the Shaqiu "
             "coup in 295; this page takes only his reform, not the "
             "succession. From 307 BC he ordered Zhao to adopt the nomads' "
             "short coat and to learn mounted archery, replacing chariots "
             "and foot soldiers with cavalry. It was hard on two sides: "
             "strong neighbours outside, and a court full of elders who held "
             "that ancestral ways must not change. He left two methods. If "
             "a thing works, do not care whom it came from. If you must "
             "change the rules, go first to the weightiest opponent.",
        "story":
            "A few years after Wuling began the reform, Zhao had cavalry of "
            "its own. It beat the Linhu and Loufan peoples to the north, "
            "built a wall along the Yin Mountains and set up three "
            "commanderies there. The north had been the state's soft side "
            "and became the place it expanded from.",
        "f": [
            {"n": "He learned what worked, not what looked proper",
             "d": "He watched the nomads to the north: short coats, easy to "
                  "ride and shoot in, coming and going like the wind. "
                  "Zhao's troops wore long robes and relied on chariots "
                  "and infantry, and could not catch them. His question "
                  "was whether the dress worked, not whether it was "
                  "dignified.",
             "eg": "A colleague finishes in half an hour what took you an "
                   "afternoon. Learn how he sets the tool up before arguing "
                   "whether that counts."},
            {"n": "He did not take laughter as evidence",
             "d": "He told his minister Yi that fools laugh and the wise "
                  "look closer, and that even if the whole world laughed he "
                  "would take the steppe lands. Laughter showed he was "
                  "different, not mistaken. What he looked at was whether "
                  "the thing could succeed.",
             "eg": "You use a method others scorn and get teased. Ask "
                   "whether it solves the one thing you need this year."},
            {"n": "He went to see the hardest man first",
             "d": "His uncle, Prince Cheng, was the weightiest elder and "
                  "pleaded illness. Wuling issued no decree and walked to "
                  "his house, argued that ritual exists to get things done, "
                  "and gave him the nomad coat. Next day the prince wore it "
                  "to court.",
             "eg": "A new process is stuck. Skip the all-hands email and "
                   "talk to the senior colleague everyone watches."},
        ],
        "apply": "Take one thing you have been putting off learning because it "
                 "comes from people you rate lower. Write two lines: what it "
                 "would do for the one thing you must get done this year, and "
                 "whether you are avoiding it because it is useless or "
                 "because learning it would make you look behind. If you are "
                 "the one changing a shared habit, go to the most senior "
                 "opponent in person before you send anything.",
        "q": ["Clothes are for use; ritual is for getting things done.",
              "Fools laugh at it; the wise take a closer look.",
              "An act you doubt achieves nothing."],
        "l": ["Shang Yang", "Fukuzawa Yukichi", "Guan Zhong", "Duke Wen of Jin"],
        "contrast": [
            {"n": "Shang Yang",
             "why": "Both rewrote a state's old rules. Shang Yang put down "
                    "opposition with decrees and heavy penalties, building "
                    "trust first and law second, and did not argue with "
                    "opponents. Wuling walked to the opponent's door and "
                    "argued to the point he cared about"},
            {"n": "Fukuzawa Yukichi",
             "why": "Both learned from the side their own people looked down "
                    "on: Fukuzawa from the West, Wuling from the nomads. "
                    "Fukuzawa wrote to change minds. Wuling put on the coat "
                    "himself and knocked on his uncle's door"},
        ],
    },
]

INTROS = {
    "zhao-wuling-wang": "A king of Zhao in the Warring States period who ordered "
                        "his whole court into the nomads' short coat and onto "
                        "horseback. His best line: clothes are for use, not for "
                        "show. When his uncle refused to wear it, he walked to "
                        "the uncle's house.",
}

SCENES = [
    ("I can't keep up with the new thing", "AI arrived", [
        ("I can't make myself learn from people I think are beneath me.",
         [("zhao-wuling-wang", "learn-from-the-lesser")]),
    ]),
    ("They said no to my plan", "Making a call", [
        ("They say it has always been done this way. How do I move them?",
         [("zhao-wuling-wang", "go-to-the-uncle-first")]),
    ]),
]

ASKS = {
    "zhao-wuling-wang/learn-from-the-lesser":
        "I can't make myself learn from people I think are beneath me.",
    "zhao-wuling-wang/go-to-the-uncle-first":
        "They say it has always been done this way. How do I move them?",
}

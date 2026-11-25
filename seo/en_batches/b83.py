# -*- coding: utf-8 -*-
"""Daily entry: Goujian of Yue.

Picked the old way (the queue in DAILY_QUEUE.md is finished and the next batch is not yet approved).
'Starting over' is among the emptiest scenes, and what hangs there is about age, burned bridges and attitude;
none asks what to drop and what to keep when you fall from a height. 'They have more of everything' is about
where to fight a stronger rival; none asks when, once you are finally ready, you should actually move.

Why he qualifies: the last hegemon of the Spring and Autumn period, defeated, made a vassal, and twenty-odd
years later the conqueror of Wu; his life is told in Sima Qian's Hereditary House of King Goujian of Yue.

Everything follows that chapter. The entry story is the siege at Kuaiji; the chapters are the gall after his
return and the long wait before striking. The killing of Wen Zhong after the conquest belongs to Fan Li's entry.
"""

ENTRIES = [
    {
        "c": "Strategy and competition",
        "n": "Goujian of Yue",
        "slug": "gou-jian",
        "e": "Spring and Autumn · Yue · took the throne 496 BC",
        "w": "Starting over", "y": -496,
        "d": "Goujian became king of Yue in 496 BC. Three years later he attacked Wu against Fan Li's advice, was "
             "crushed, and was besieged on Mount Kuaiji with five thousand men. He survived by becoming the vassal of "
             "King Fuchai of Wu. Over the next twenty-odd years he rebuilt, destroyed Wu, and became the last hegemon "
             "of the Spring and Autumn period. Everything here follows Sima Qian. He is here for two situations: "
             "what to let go of when you start over from a fall, and when to move once you are ready.",
        "story":
            "After the defeat, Goujian retreated with five thousand men to Mount Kuaiji, and Wu surrounded them. "
            "He sent his minister Wen Zhong to the Wu camp to crawl forward on his knees and offer Goujian as Wu's "
            "servant and his wife as a concubine. Wu's adviser Wu Zixu said refuse. Goujian wanted to kill his own "
            "family, burn his treasures and fight to the death. Wen Zhong stopped him and bribed Wu's chief minister "
            "instead, and Wu's king pardoned Yue. Trapped, Goujian sighed: is this where I end? Wen Zhong listed "
            "founders who had been imprisoned or exiled, and all of them later ruled.",
        "f": [
            {"n": "When you did not listen, say so first",
             "d": "In 494 BC he heard Wu was drilling troops day and night and wanted to strike first. Fan Li told him not to. I have decided, he said. After the rout his first words to Fan Li were: this is because I did not listen to you; what now?",
             "eg": "When you push something through and it fails, go back to the person who warned you and say so before asking what next."},
            {"n": "Give the job to whoever fits it",
             "d": "Back home he wanted Fan Li to run the state. Fan Li said: in war, Wen Zhong is not my equal; in calming the country and winning the people, I am not his. Goujian gave the government to Wen Zhong, and Fan Li went to Wu as a hostage for two years.",
             "eg": "In the years of rebuilding, give the key posts to the people who fit them best, not the people closest to you."},
            {"n": "After twenty-two years, the hard part is not relenting",
             "d": "At the end Wu's king, besieged on a hill, sent an envoy stripped to the waist to beg for peace, recalling that he had once spared Goujian. Goujian could not bear it and wanted to agree. Fan Li asked whether twenty-two years of planning should be thrown away in one morning, and drummed the advance.",
             "eg": "When the rival you spent years beating comes to plead, first remember why you needed to win."},
        ],
        "apply": "This week write your most recent fall as one sentence: where you lost, who warned you, and which "
                 "warning you ignored. Put a copy somewhere you open every day, and for a month, each time you see it, "
                 "ask whether today's work has anything to do with that sentence.",
        "q": [
            "This is because I did not listen to you.",
            "Give the key post to whoever fits it best.",
            "At the last step, the hard part is not relenting.",
        ],
        "l": ["Fan Li", "Xiang Yu", "Sima Yi"],
        "contrast": [
            {"n": "Xiang Yu", "why": "Both lost a decisive war down to almost nothing. Goujian, trapped at Kuaiji, bowed as a vassal, went home to farm, and twenty-odd years later destroyed Wu. Xiang Yu, at the Wu River, was urged to cross home and start again; eight thousand men had crossed with him and none returned, he said, and he could not face their elders. One dropped his dignity and started over. The other kept it and did not."},
        ],
    },
]

INTROS = {
    "gou-jian":
        "The last hegemon of ancient China's Spring and Autumn period. Besieged and forced to become his enemy's "
        "vassal, he went home, hung a gall bladder by his seat and farmed with his own hands, then waited until his "
        "enemy's army was away before he struck and destroyed Wu",
}

SCENES = [
    ("Starting over", "A turn in the road", [
        ("Starting again, I can't let go of who I used to be.",
         [("gou-jian", "the-gall")]),
    ]),
    ("They have more of everything", "Facing an opponent", [
        ("I'm finally ready. Is it still too soon to move?",
         [("gou-jian", "hide-the-talons")]),
    ]),
]

ASKS = {
    "gou-jian/the-gall": "Starting again, I can't let go of who I used to be.",
    "gou-jian/hide-the-talons": "I'm finally ready. Is it still too soon to move?",
}

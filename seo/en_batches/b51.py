# -*- coding: utf-8 -*-
"""Li Qingzhao, added so the personality test is not almost all men (2026-10-09).

The site owner named her. Her standing: the greatest woman poet of classical
China, Song dynasty; her lyrics are still taught in every Chinese school.
This page leaves the poems to others and takes three judgements from her
prose: the order in which she shed a collection she could not carry (the
Postface to the Records on Metal and Stone), the tea wager she and her
husband played in their poor years (same source), and how she criticised the
masters of her art (On Lyrics).

All quoted lines are our own renderings, checked against the full Chinese
texts on Wikisource.
"""

ENTRIES = [
    {
        "c": "Mind and feeling",
        "n": "Li Qingzhao",
        "slug": "li-qingzhao",
        "e": "Song · Jinan · 1084-c.1155",
        "w": "The lyric",
        "y": 1084,
        "d": "The greatest woman poet of classical China, from Jinan, "
             "who called herself the Lay Buddhist of Easy Peace. For half "
             "her life she and her husband Zhao Mingcheng collected "
             "books, paintings and bronzes and wrote lyrics to each "
             "other. In her forties the Jin invasion drove them south; "
             "he died on the way and the collection scattered, and she "
             "later wrote it all down in the Postface to the Records on "
             "Metal and Stone. This page leaves her poems aside and takes "
             "three judgements: when you cannot carry it all, decide "
             "the order of what goes; when money is tight, invent a game "
             "for two; to say the masters are wrong, show your standard "
             "first.",
        "story": "After the court fled south she wrote a four-line poem: "
                 "'In life, be a hero among men; in death, a hero among "
                 "ghosts. To this day I think of Xiang Yu, who would not "
                 "cross back east of the river.' Xiang Yu, beaten, refused "
                 "to escape and save himself. Readers ever since have "
                 "taken the poem as her verdict on a court that kept "
                 "retreating.",
        "f": [
            {"n": "Decide the order of what goes",
             "d": "Fleeing south, she and her husband shed twenty years of collecting layer by layer: replaceable printed books first, unique pieces last. It still filled fifteen carts.",
             "eg": "Moving with one suitcase: give away what shops sell, keep the handwritten letters."},
            {"n": "Make a game for two",
             "d": "Poor in their first years, they pawned clothes for rubbings. Later, over tea, they bet on which book and page a passage was on; whoever was right drank first.",
             "eg": "Quiz each other on film lines at dinner; the winner picks next week's film."},
            {"n": "Show the standard first",
             "d": "In On Lyrics she named nearly every master, Su Shi included, but first said what a lyric must do that a poem need not. Disagree, and you must refute the standard.",
             "eg": "Before calling the boss's plan weak, write down the test you are using."},
        ],
        "apply": "Pick one thing you are about to give up, criticise or "
                 "put up with, and write one line each: what can be "
                 "replaced and what cannot; what game the two of you "
                 "could play with what you already have; what standard "
                 "you are judging by. She did all three in prose, and it "
                 "is why her losses are still remembered.",
        "q": [
            "In life, be a hero among men; in death, a hero among ghosts.",
            "Whatever is gathered must scatter. That is the way of things.",
            "The lyric is an art of its own, and few understand it.",
        ],
        "l": ["Su Shi", "Du Fu", "Xiang Yu", "Tao Yuanming"],
        "contrast": [
            {"n": "Su Shi", "why": "Her father was Su Shi's student, and she still wrote that his lyrics often missed the music. Both lived through exile and loss: Su Shi wrote the hard years as breadth of mind, she wrote them as an exact list of what was lost"},
            {"n": "Du Fu", "why": "Both were driven from home by invasion and both wrote one household's ruin more precisely than the history books wrote the war: Du Fu the family on the road, Li Qingzhao the library that scattered"},
        ],
    },
]

INTROS = {
    "li-qingzhao": "The greatest woman poet of classical China. Fleeing "
                   "the Jin invasion, she and her husband shed twenty years "
                   "of collecting in a careful order and still filled "
                   "fifteen carts. In her essay On Lyrics she criticised "
                   "nearly every master of the form, her father's teacher "
                   "Su Shi included.",
}

SCENES = [
    ("I can't cut something I built", "Getting it done", [
        ("Too much to carry. What do I drop first?",
         [("li-qingzhao", "fifteen-carts")]),
    ]),
    ("Years in, nothing left between us", "At home", [
        ("Money is tight. What can the two of us still enjoy?",
         [("li-qingzhao", "the-tea-wager")]),
    ]),
    ("Everyone is saying the same thing", "Dealing with people", [
        ("The masters of my field are doing it wrong. Do I say so?",
         [("li-qingzhao", "a-separate-art")]),
    ]),
]

ASKS = {
    "li-qingzhao/fifteen-carts": "Too much to carry. What do I drop first?",
    "li-qingzhao/the-tea-wager": "Money is tight. What can the two of us still enjoy?",
    "li-qingzhao/a-separate-art": "The masters of my field are doing it wrong. Do I say so?",
}

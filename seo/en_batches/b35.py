# -*- coding: utf-8 -*-
"""Daily entry, day 15: Lin Xiangru.

Picked by fan-out. 'Someone is being unreasonable' was among the emptiest
situations on the Chinese side, and what hangs there is Epictetus (control
what you can), Machiavelli (see it as it is), Gandhi (make their violence
visible) and Su Shi (there are no bad people). None of them says what to do
before the other side has acted: arrange things so that if they cheat, the
wrong is plainly theirs, and keep something you can take back. That is Lin
Xiangru's reasoning over the jade. His second chapter fills 'Should I
compromise' on the Chinese side (no English counterpart exists yet) and
'My partner and I are falling out' here: stepping aside for a rival at home
is not fear when you have held firm against a stronger enemy.

All facts and quoted lines are from Sima Qian's Lives of Lian Po and Lin
Xiangru. The English quotations are our own renderings of the Chinese, not
taken from a published translation.

Three stories, no overlap: the entry is the meeting at Mianchi, the first
chapter is the jade, the second is Lian Po.

All situations already exist, so there is no SC_BOX here.
"""

ENTRIES = [
    {
        "c": "Strategy and competition",
        "n": "Lin Xiangru",
        "slug": "lin-xiangru",
        "e": "Warring States · Zhao · dates unknown",
        "w": "Putting the wrong on their side", "y": -283,
        "d": "Minister of the state of Zhao in the Warring States period, "
             "who began as a retainer in the household of the chief eunuch "
             "Miao Xian. When the King of Qin offered fifteen cities for "
             "Zhao's jade disc, he took it to Qin and brought it back whole. "
             "At the meeting of the two kings at Mianchi he forced the King "
             "of Qin to make music for the King of Zhao, and was raised above "
             "the great general Lian Po, who swore to humiliate him. Lin kept "
             "out of his way until Lian Po came to apologise. Sima Qian wrote "
             "their lives as one. He left two ways of dealing with people: "
             "against a stronger party that will not play fair, arrange "
             "things so the wrong lands on their side; against a provocation "
             "from your own side, ask first whether what you hold together "
             "would survive the fight.",
        "story":
            "The King of Qin invited the King of Zhao to meet at Mianchi. "
            "Well into the drinking he asked the King of Zhao to play the "
            "zither, and Qin's scribe wrote it down: on this day the King of "
            "Qin drank with the King of Zhao and ordered him to play. Lin "
            "Xiangru stepped forward and asked the King of Qin to beat time "
            "on an earthen pot. He refused. Within five paces, Lin said, I "
            "can spatter Your Majesty with the blood of my neck. The guards "
            "reached for their swords; he glared and they fell back. The king "
            "struck the pot once, and Lin had Zhao's scribe write that down "
            "too.",
        "f": [
            {"n": "Let the wrong land on their side",
             "d": "Offered cities for the jade, he did two sums: refuse, and "
                  "Zhao is in the wrong; hand it over and get nothing, and "
                  "Qin is. He chose to agree and push the risk of broken "
                  "faith onto a stronger state that needed a pretext to "
                  "march.",
             "eg": "Offered terms you don't believe, accept them with the "
                   "delivery steps written down, and see whether they walk "
                   "them."},
            {"n": "Keep something you can take back",
             "d": "His promise was that the jade would stay in Qin only if "
                  "the cities came. When the king showed no sign of paying, "
                  "Lin took the jade back on the pretext of pointing out a "
                  "flaw, asked for five days of fasting, and sent it home by "
                  "a back road.",
             "eg": "Send a sample and tie the final payment to acceptance, "
                   "so they take the first step."},
            {"n": "If they write it down, so do you",
             "d": "At Mianchi Qin's scribe recorded that the King of Zhao "
                  "played for the King of Qin. Lin forced the reverse and had "
                  "Zhao's scribe record it. When someone uses the record to "
                  "score a point, answer on the same page with an equal "
                  "entry.",
             "eg": "If the minutes note your concession, make sure the same "
                   "minutes note what they gave in return."},
            {"n": "With your own side, put the steel away",
             "d": "When Lian Po swore to disgrace him, he stayed home on "
                  "court days and turned his carriage aside in the street. "
                  "Qin held off, he said, only because both of them were "
                  "there; two tigers fighting would leave one dead.",
             "eg": "In a clash with a colleague you work shoulder to shoulder "
                   "with, ask who gains most if you two fall out in public."},
        ],
        "apply":
            "If you are facing someone stronger who will not play fair, don't "
            "start by arguing with them, and don't refuse outright. Follow "
            "each path to its end and see where the wrong lands. Take the one "
            "that leaves it with them, but don't give anything away for free: "
            "make their delivery the condition for yours, and keep something "
            "you can take back. If the person picking the fight is on your "
            "own side, don't rush to prove you are not afraid. Ask what the "
            "two of you are holding together, and whether it survives the "
            "fight. Lin Xiangru threatened to smash the jade against a pillar "
            "in Qin's hall, then went out of his way to avoid Lian Po at "
            "home. The nerve and the restraint came from the same "
            "calculation.",
        "q": [
            "Better to agree and leave the wrong with Qin.",
            "Within five paces, I can spatter Your Majesty with my blood.",
            "When two tigers fight, one of them does not survive.",
            "The state's emergency first, my private quarrel second.",
        ],
        "l": ["Guo Ziyi", "Zhang Liang", "Gandhi", "Su Shi"],
        "contrast": [
            {"n": "Gandhi",
             "why": "Both face a stronger party that will not reason and "
                    "neither relies on force: Gandhi puts the other side's "
                    "violence in front of everyone until it loses its "
                    "legitimacy, while Lin moves earlier, choosing before "
                    "anyone acts the path on which a broken promise can only "
                    "be theirs, and keeping something he can take back"},
            {"n": "Zhang Liang",
             "why": "Both step back when they could press their claim: Zhang "
                    "Liang turned down thirty thousand households for one "
                    "small county, yielding to his ruler to disarm suspicion, "
                    "while Lin yielded to a colleague to keep standing the "
                    "one line of defence the two of them held together"},
        ],
    },
]

INTROS = {
    "lin-xiangru":
        "A minister of Zhao who carried a priceless jade into the court of "
        "Qin and brought it home whole, then spent his years at home "
        "stepping out of a jealous general's way - the nerve and the "
        "restraint came from the same calculation",
}

SCENES = [
    ("Someone is being unreasonable", "Dealing with people", [
        ("I don't believe their offer, and refusing puts me in the wrong.",
         [("lin-xiangru", "crooked-on-qin")]),
    ]),
    ("I don't believe what my boss says", "Dealing with people", [
        ("He promises a lot. Do I hand it over first?",
         [("lin-xiangru", "crooked-on-qin")]),
    ]),
    ("My partner and I are falling out", "Dealing with people", [
        ("He's said he'll humiliate me in public. Do I keep avoiding him?",
         [("lin-xiangru", "two-tigers")]),
    ]),
]

ASKS = {
    "lin-xiangru/crooked-on-qin":
        "I don't believe their offer, and refusing puts me in the wrong.",
    "lin-xiangru/two-tigers":
        "He's said he'll humiliate me in public. Do I keep avoiding him?",
}

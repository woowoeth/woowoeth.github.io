# -*- coding: utf-8 -*-
"""Daily entry, day 16: The Book of Rites.

Picked by fan-out. 'I've been tense for a long time' and 'I've run out of
energy' were among the emptiest situations on the Chinese side, and what
hangs there is Sapolsky (stress is a mismatch), Ratey (move first), Seneca
and Epictetus. None of them says that easing off has to be put on the
calendar, together with other people, or it arrives only as guilt. That is
the bowstring passage in 'Miscellaneous Records'. The second chapter, food
given with a 'hey', fills 'It turned into a fight': once the other side has
apologised, what are you still refusing? The third, from the 'Record of
Learning', fills 'My kid won't listen' and 'The team has gone flat': open
the way, and don't walk it to the end for them.

All quoted lines are our own renderings of the Chinese, checked against the
Wikisource text of the three chapters, not taken from a published
translation.

Three stories, no overlap: the entry is the woman at the foot of Mount Tai,
the chapters are the year-end festival, the famine in Qi and the portrait
of bad teaching.

All situations already exist, so there is no SC_BOX here.
"""

ENTRIES = [
    {
        "c": "Body and daily life",
        "n": "The Book of Rites",
        "slug": "liji",
        "e": "Western Han · compiled by Dai Sheng · 49 chapters",
        "w": "One tension, one release", "y": -51,
        "d": "A collection of Confucian writings on ritual, fixed at 49 "
             "chapters by Dai Sheng in the Western Han. Zheng Xuan wrote its "
             "standard commentary in the Eastern Han; the Tang counted it "
             "among the Five Classics, and Zhu Xi in the Song lifted out two "
             "of its chapters, the Great Learning and the Doctrine of the "
             "Mean, for the Four Books. Most of it records procedure: "
             "sacrifice, mourning, capping, marriage, daily conduct. Set "
             "among the procedures are passages asking how people manage to "
             "live. We take three: on easing off, on climbing down, and on "
             "leaving the last steps to the learner.",
        "story":
            "Confucius was passing the foot of Mount Tai when he heard a "
            "woman weeping bitterly at a grave. He leaned on the rail of his "
            "carriage and listened, then sent a disciple to ask. You weep as "
            "if grief had come more than once, the disciple said. It has, she "
            "answered. A tiger killed my husband's father, then my husband, "
            "and now my son. Then why not leave? There is no harsh government "
            "here. Confucius turned to his disciples: remember this. Harsh "
            "government is fiercer than a tiger.",
        "f": [
            {"n": "Among the rules, room for the year",
             "d": "It records rule upon rule, and beside them it often sets a "
                  "line that loosens them. In a bad year, Confucius says in "
                  "'Miscellaneous Records', ride a poor horse and sacrifice a "
                  "lesser animal. The rule follows the harvest, not the other "
                  "way round.",
             "eg": "Money is short this year and the party is still planned "
                   "at last year's scale."},
            {"n": "Not even the sage kings could stay strung",
             "d": "Zigong came back from the year-end festival saying the "
                  "whole state had gone mad. Confucius spoke of a bow: kept "
                  "strung and never unstrung, it was beyond the kings Wen and "
                  "Wu; kept unstrung and never strung, they would not do it. "
                  "Easing off is not a failure of will.",
             "eg": "Six months without a day off messages, and you call it "
                   "building strength."},
            {"n": "At the shout you may leave; after the apology you may eat",
             "d": "In a famine Qian Ao offered food with a 'hey, come and "
                  "eat'. The starving man refused, Qian Ao apologised, and he "
                  "still refused and died. Zengzi's verdict: the shout was "
                  "reason to leave, the apology reason to eat. Dignity guards "
                  "a moment, not every moment after.",
             "eg": "He admitted fault in private and you still won't pick "
                   "the talks back up."},
            {"n": "Open the way, don't walk it to the end",
             "d": "The 'Record of Learning' says good teaching guides without "
                  "dragging, urges without pressing down, and opens the way "
                  "without taking the student to the end. Of those dragged "
                  "through, it says: though they finish the course, they drop "
                  "it quickly.",
             "eg": "Someone asks you what to do. Ask first where they think "
                   "they're stuck."},
        ],
        "apply":
            "If you haven't truly stopped in a long time, don't start by "
            "planning a long holiday. Open next month's calendar and cross "
            "out one day now, agreed with your family or your team: that day "
            "nobody contacts anybody. The release should be like the year-end "
            "festival, set in advance and shared, not sleep caught up alone "
            "after a collapse. Keep a second question for the quarrel you're "
            "still nursing: if they have already come to you and admitted "
            "fault, are you refusing the shout, or the bowl they held out "
            "afterwards? And the next time someone asks you what to do, "
            "don't give the answer first. Ask where they're stuck, open the "
            "door a crack, and let them walk the last steps.",
        "q": [
            "Not even the sage kings could stay strung.",
            "At the shout you may leave; after the apology you may eat.",
            "Open the way. Don't walk it to the end for him.",
            "In a bad year, ride a poor horse.",
        ],
        "l": ["The Analects", "Mencius", "Xunzi",
              "Family Instructions for the Yan Clan", "Robert Sapolsky"],
        "contrast": [
            {"n": "Robert Sapolsky",
             "why": "Both explain why staying tense wears you down. Sapolsky "
                    "is talking about the body: the zebra's stress ends when "
                    "the lion leaves, while ours stays switched on for things "
                    "that haven't happened. The Book of Rites is talking "
                    "about the calendar: release is not something you patch "
                    "in once the body gives out, but a day fixed in advance "
                    "and shared, like the year-end festival."},
            {"n": "The Analects",
             "why": "Both record how Confucius taught. In the Analects he "
                    "will not open up a student who is not yet straining to "
                    "understand, which is about when to speak. The 'Record "
                    "of Learning' goes a step further: even once you speak, "
                    "open the way and stop, and leave the last steps to the "
                    "learner."},
        ],
    },
]

INTROS = {
    "liji":
        "The Confucian book of ritual, fixed at 49 chapters in the Western "
        "Han - we leave the procedures and take three passages set among "
        "them on easing off, climbing down, and letting the learner finish",
}

SCENES = [
    ("I've been tense for a long time", "Body and energy", [
        ("The moment I stop, I feel guilty.",
         [("liji", "one-tension-one-release")]),
    ]),
    ("I've run out of energy", "Body and energy", [
        ("I've been going flat out for six months without a break.",
         [("liji", "one-tension-one-release")]),
    ]),
    ("It turned into a fight", "Making a call", [
        ("He apologised and I still can't let it go.",
         [("liji", "come-and-eat")]),
    ]),
    ("My kid won't listen", "At home", [
        ("I can't stop myself just telling him the answer.",
         [("liji", "open-not-arrive")]),
    ]),
    ("The team has gone flat", "Leading people", [
        ("I hand them every answer and they just do as they're told.",
         [("liji", "open-not-arrive")]),
    ]),
]

ASKS = {
    "liji/one-tension-one-release":
        "The moment I stop, I feel guilty.",
    "liji/come-and-eat":
        "He apologised and I still can't let it go.",
    "liji/open-not-arrive":
        "I can't stop myself just telling him the answer.",
}

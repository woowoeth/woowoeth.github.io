# -*- coding: utf-8 -*-
"""Daily entry: Shun.

Picked the old way (the queue in DAILY_QUEUE.md is finished and the next batch is not yet approved).
Among the emptiest scenes are 'I can't be myself around family' and 'I was betrayed'. The family pieces
are about boundaries and not being swept up; none covers a family that is actively cruel, where the
reader is torn between giving in and cutting off. None of the betrayal pieces is about a relative.

Why he qualifies: one of the Five Emperors in Sima Qian's Basic Annals; 'Yao and Shun' is the standard
Chinese shorthand for a good ruler, and Mencius returns to him again and again.

He belongs to the legendary age; everything is told as the Records of the Grand Historian and the Mencius
tell it. The entry story is Yao's trial of Shun and the places he farmed and fished; the chapters are the
attempts on his life and the fief given to his brother.
"""

ENTRIES = [
    {
        "c": "Family and relationships",
        "n": "Shun",
        "slug": "shun",
        "e": "Legendary age · Records of the Grand Historian",
        "w": "Family", "y": -2200,
        "d": "Shun, one of the legendary Five Emperors. Yao passed the realm to him and he passed it to Yu, and "
             "'Yao and Shun' became the Chinese byword for good rulers. He was born a commoner; his father, his "
             "stepmother and his half-brother Xiang all tried to kill him, and by twenty he was known for devotion "
             "to them. Everything here follows Sima Qian and Mencius. He is here for families that do real harm, "
             "where neither giving in nor cutting off will do.",
        "story":
            "When Yao grew old he asked who could be trusted, and the chiefs of the four quarters named Shun. Yao "
            "gave him his two daughters in marriage, to see how he ran his house, and sent his nine sons to live "
            "beside him, to see how he dealt with others. Where Shun farmed, at Mount Li, people yielded field "
            "boundaries to one another. Where he fished, they yielded the best spots. Where he made pots, no pot was "
            "shoddy. Wherever he settled, in a year it was a village, in two a town, in three a city.",
        "f": [
            {"n": "A thirty-one-year trial",
             "d": "Yao raised him at thirty, had him act for the throne at fifty, and died when Shun was fifty-eight. Shun took the throne at sixty-one. For thirty-one years he was watched and tested before he was given the thing itself.",
             "eg": "The long probation before anyone trusts you is part of the answer, not a delay before it."},
            {"n": "The imperial banner at his father's door",
             "d": "As emperor he went to pay his respects to his father under the imperial banner, with all the care of a son. The ranks between them had turned over; what he did there was still a son's part.",
             "eg": "Once you have the upper hand, you need not go back to collect an apology."},
            {"n": "Not to his own son",
             "d": "His son Shangjun was unworthy, so Shun put Yu forward as his successor. After Shun died and the mourning ended, Yu stepped aside for Shangjun, but the lords all went to Yu, and only then did he take the throne.",
             "eg": "Give the post to the most capable person, not the closest one."},
        ],
        "apply": "This week think of the person at home who is hardest on you. Make two columns: what I can give him "
                 "(time, money, company) and what I will not put in his hands (keys, passwords, decisions about my life). "
                 "Look at the page before you next see him.",
        "q": [
            "Wherever he settled, people gathered.",
            "The ranks turned over; he still played the son.",
            "The post goes to the most capable, not the closest.",
        ],
        "l": ["Mencius", "The Duke of Zhou", "Records of the Grand Historian"],
        "contrast": [
            {"n": "The Duke of Zhou", "why": "Both had brothers who turned on them. Xiang tried to kill Shun, and Shun as emperor gave him a fief but no say in running it. The Duke of Zhou's brothers Guan and Cai joined Wugeng's rising, and the Duke marched against them, executing Guan and exiling Cai. Xiang threatened one man; Guan took up arms against the realm. Once others are hurt, kinship no longer covers it."},
        ],
    },
]

INTROS = {
    "shun":
        "One of the legendary Five Emperors, to whom Yao handed the realm. His father, stepmother and brother all "
        "tried to kill him; he escaped each time and never left them for good, and as emperor he made that "
        "brother a lord who governed no one",
}

SCENES = [
    ("I can't be myself around family", "At home", [
        ("My family is cruel to me. Do I still look after them?",
         [("shun", "never-caught")]),
    ]),
    ("I was betrayed", "At home", [
        ("My own brother cheated me. Do I still help him?",
         [("shun", "rich-not-ruling")]),
    ]),
]

ASKS = {
    "shun/never-caught": "My family is cruel to me. Do I still look after them?",
    "shun/rich-not-ruling": "My own brother cheated me. Do I still help him?",
}

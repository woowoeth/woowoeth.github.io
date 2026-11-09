# -*- coding: utf-8 -*-
"""Daily entry: Emperor Wu of Han.

From DAILY_QUEUE.md row 6. 'Expansion' holds entries on whether to enter a market, how to feed what
you have spread, and what to leave alone. Nobody there says when to stop once you are already spread
out, or what to do with the people and effort afterwards.

Why he qualifies: emperor for fifty-four years, annals in the Book of Han, the ruler who set the
Han frontier and its fiscal state; the Luntai edict is one of the best-known retreats in Chinese history.

The entry story is the full treasury he inherited; the chapters are the edict and its aftermath.
"""

ENTRIES = [
    {
        "c": "Power and organisation",
        "n": "Emperor Wu of Han",
        "slug": "han-wudi",
        "e": "Western Han · 156–87 BCE",
        "w": "Knowing when to stop", "y": -89,
        "d": "Western Han emperor, personal name Liu Che, who took the throne in 141 BCE and ruled for fifty-four "
             "years; his annals are in the Book of Han. For most of his reign he fought the Xiongnu and pushed into "
             "the Western Regions, and at home he put salt and iron under state control and set up recommendation "
             "for office. This page passes no verdict on his life. It takes one late episode: in 89 BCE he was asked "
             "to plant military farms at Luntai, refused, set the cost of the decades before on the table, and turned "
             "the effort back to farming. He is here for the 'expansion' group, which says how to judge whether to "
             "enter and how to feed what you hold, but not when to stop once you are spread out, or what comes next.",
        "story":
            "In the first years of Wu's reign the treasury overflowed. According to Sima Qian's Records of the "
            "Grand Historian, the coin in the capital had piled up until the cords strung through it rotted and "
            "could not be counted, and the grain in the great granary was stacked outdoors, year on year, until "
            "it spoiled. What he took over had been saved by his father and grandfather.",
        "f": [
            {"n": "The savings were somebody else's",
             "d": "The money, grain and horses he went to war with had been put by the two reigns before him. Being able to afford a campaign does not mean every one is worth it. The more room you have, the more it matters to ask whether this one has to be fought.",
             "eg": "A big cash pile in the bank does not make every new business worth funding."},
            {"n": "Later writers counted the cost",
             "d": "In his note on the Zhao emperor's annals, Ban Gu says that after Wu the empire was drained and its registered households halved. The total was counted afterwards. People inside the reign could not see it. Each campaign had reasons on its own; the sum is the number.",
             "eg": "Each monthly top-up has a reason, and at year-end the budget has doubled."},
            {"n": "The hardest thing he did was stop",
             "d": "Late in life he was asked to push one step further west. He refused and admitted fault in an edict. This page splits the edict into two chapters: whose accounts to open when you stop, and where the effort goes afterwards.",
             "eg": "Cutting a three-year project is not the hard part. Saying in the meeting 'I judged this wrong' is."},
        ],
        "apply": "This week, take one thing you are expanding and write down what it has actually cost so far and what it has brought back. "
                 "Then ask: if someone asked tomorrow for another round, what would I use to decide when to stop?",
        "q": [
            "The more room you have, the more you must ask whether it is worth it.",
            "Each item has a reason; the sum is the number.",
            "The hardest step is to stop, so open your own books first.",
        ],
        "l": ["Huo Qubing", "Sima Qian", "Liu Bang"],
        "contrast": [
            {"n": "Liu Xiu", "why": "Both faced the Western Regions. Wu stopped only after decades of campaigns. Liu Xiu, with his own country just settled, was asked by the states there to send a protector-general and declined at the start. One pulled back after spreading out; the other worked out first whether he could carry it."},
        ],
    },
]

INTROS = {
    "han-wudi":
        "Western Han emperor of fifty-four years who fought the Xiongnu for decades - "
        "late in life, asked to garrison Luntai, he refused, admitted the cost "
        "in an edict, and turned the effort back to farming",
}

SCENES = [
    ("Winning is costing too much", "Facing an opponent", [
        ("We've been fighting this for so long. When do I stop?",
         [("han-wudi", "luntai-edict")]),
        ("I've stopped. Where do my people go?",
         [("han-wudi", "after-the-retreat")]),
    ]),
]

ASKS = {
    "han-wudi/luntai-edict": "We've been fighting this for so long. When do I stop?",
    "han-wudi/after-the-retreat": "I've stopped. Where do my people go?",
}

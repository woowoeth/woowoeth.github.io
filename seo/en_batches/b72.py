# -*- coding: utf-8 -*-
"""Daily entry: John C. Bogle.

From DAILY_QUEUE.md row 9. 'Making money work' holds entries on building assets, knowing what you
hold, moving money faster and investing in yourself. None of them says what to look at before you
hand money over: what it costs. The second chapter answers the reader who cannot pick winners.

Why he qualifies: founded Vanguard (1974) and launched the first index fund for ordinary investors
(1976), which created the index-investing industry.

The entry story is his 1974 ouster from Wellington and the founding of Vanguard; the chapters are
the 1976 fund launch and the 1949-51 Princeton thesis.
"""

ENTRIES = [
    {
        "c": "Money and risk",
        "n": "John C. Bogle",
        "slug": "bogle",
        "e": "United States · 1929–2019",
        "w": "Cost", "y": 1976,
        "d": "Founder of Vanguard, who in 1976 launched the first index fund for ordinary investors and so created "
             "the index-investing industry. His case comes down to two points. Before costs, all investors together "
             "earn the market's return, so after costs they must trail it as a group. And if you cannot pick the "
             "winners, own the whole market, keep the costs as low as possible, and leave it alone. He is here for "
             "'Making money work', where nothing yet says what to check before you hand the money over: the cost.",
        "story":
            "In January 1974 Bogle, then forty-four, was removed as head of Wellington Management. The partners he had "
            "pushed to bring in through a merger a few years earlier voted him out at the board. He did not leave. He "
            "proposed a new company to run the administration of Wellington's funds, owned by the funds' own shareholders "
            "and run at cost. He named it after Nelson's flagship at the Battle of the Nile, HMS Vanguard.",
        "f": [
            {"n": "Owned by the people who buy the funds",
             "d": "Other fund companies belong to their own shareholders and live on the fees. Vanguard belongs to the funds it runs, and the funds belong to their investors. It has no separate profit to earn, so the savings go back to the people holding the funds.",
             "eg": "Before buying any fund, ask who the company running it is making money for."},
            {"n": "So cheap the rivals had to follow",
             "d": "Vanguard kept pushing its fees down. Rivals laughed at first, then had to cut their own. He changed more than one company; he moved the floor for what the whole industry charges.",
             "eg": "One shop that prices at cost drags down the prices on the whole street."},
            {"n": "He never became a billionaire",
             "d": "Because the company belonged to its fund holders, he did not take its profits the way his peers did, and his fortune was far smaller than theirs. That was the structure he chose.",
             "eg": "When someone tells you to cut your costs, check how much of your costs they take."},
        ],
        "apply": "This week find the yearly fee on every fund or savings product you hold, write them on one sheet, "
                 "and add up how much they take from you in a year.",
        "q": [
            "Ask who the company managing your money is earning for.",
            "The fee is in the contract. The return is in the advert.",
            "He gave the profit away and got an industry in return.",
        ],
        "l": ["John Maynard Keynes", "Howard Marks", "Charles P. Kindleberger"],
        "contrast": [
            {"n": "John Maynard Keynes", "why": "Running King's College's money, Keynes moved more and more into a few companies he understood: own what you know. Bogle said it does not matter that you cannot tell which company will win; own the whole market. One asks you to know deeply, the other asks you to admit you cannot pick."},
        ],
    },
]

INTROS = {
    "bogle":
        "Founder of Vanguard, whose first index fund in 1976 was mocked as Bogle's Folly - he said if you cannot find "
        "the needle, buy the haystack, then keep the costs as low as they will go",
}

SCENES = [
    ("Making money work", "Money", [
        ("I pick funds by their returns and have never looked at the fees.",
         [("bogle", "humble-arithmetic")]),
        ("I can't tell which one will go up. Should I invest at all?",
         [("bogle", "buy-the-haystack")]),
    ]),
]

ASKS = {
    "bogle/humble-arithmetic": "I pick funds by their returns and have never looked at the fees.",
    "bogle/buy-the-haystack": "I can't tell which one will go up. Should I invest at all?",
}

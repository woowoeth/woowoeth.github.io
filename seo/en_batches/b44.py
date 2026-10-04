# -*- coding: utf-8 -*-
"""Daily entry, day 24: John Maynard Keynes.

Picked by fan-out. 'Making money work' (eight) and 'Do I jump in now' (eight)
are the emptiest situations. Under them hang Naval, Fan Li, Bai Gui, Becker and
Duan Yongping: how to build income that does not stop, and when to be last.
Nobody says what to do when no one can call it, or what to do about holding
cash while you wait, or whether owning a little of everything is protection
or camouflage. Under 'Missing out' the crowd is explained by Soros, Le Bon and
Marks; nobody says the plain thing a professional feels, that being wrong
together is safer than being right alone. Keynes says all three from his own
texts and his own losses.

His standing: founder of macroeconomics (the General Theory, 1936), and a
working investor for a Cambridge college and for insurers. The last three
entries were Coase, Porter (foreign), Xiao He (Chinese), so pick_balance is
green with a foreign pick.

Three stories, no overlap: the entry is the 1920 currency losses; the chapters
are the 1937 paper, the beauty contest, and the 1934 letter. Quoted lines are
his own English, from those texts. Every situation already exists, so there
is no SC_BOX.
"""

ENTRIES = [
    {
        "c": "How the world works",
        "n": "John Maynard Keynes",
        "slug": "keynes",
        "e": "Britain · 1883–1946",
        "w": "Not knowing",
        "y": 1936,
        "d": "British economist, born in Cambridge in 1883, whose General "
             "Theory of 1936 founded macroeconomics. He also handled real "
             "money: he managed funds for a Cambridge college and for "
             "insurance companies, and speculated in currencies for himself, "
             "losing badly and recovering. He asked one question all his "
             "life: how do you decide when you cannot know the future? His "
             "answer had three layers. Some things have no calculable odds. "
             "Most people are guessing what others will guess, and leaning "
             "on the crowd. And the heavy bets belong where you truly "
             "understand.",
        "story":
            "In 1920 Keynes took positions on several currencies on margin "
            "and within months lost almost all his capital; friends and a "
            "banker had to step in to carry him through. The man who would "
            "later write the General Theory was also a man who could be "
            "badly wrong. Afterwards, running money for institutions, he "
            "leaned more and more toward holdings he could see clearly and "
            "sit with.",
        "f": [
            {"n": "What can be counted and what cannot",
             "d": "He drew a line between roulette-type events, where odds "
                  "can be worked out, and things like the price of copper "
                  "twenty years on, where no scientific basis exists for a "
                  "calculable probability. Treat the second as the first "
                  "and the figure looks respectable but adds no certainty.",
             "eg": "Putting next year's industry growth at 8.3 per cent "
                   "pretends you face a roulette wheel."},
            {"n": "Guessing what others will guess",
             "d": "He compared professional investing to a newspaper "
                  "beauty contest: the winner is not the one who picks the "
                  "prettiest face but the one closest to the average pick. "
                  "At the third degree, the clever guess what the crowd "
                  "expects the crowd to think.",
             "eg": "You don't rate a stock, but you're sure everyone expects "
                   "everyone else to buy it, so you buy it too."},
            {"n": "Failing with the crowd is safer",
             "d": "He wrote that for reputation it is better to fail "
                  "conventionally than to succeed unconventionally. Those "
                  "who manage other people's money are judged in short "
                  "windows, so they are more likely to dodge blame than to "
                  "judge value.",
             "eg": "A fund manager who loses with the whole sector says the "
                   "market fell. One who backs something unloved and loses "
                   "explains himself for a year."},
            {"n": "Own what you understand",
             "d": "In 1934 he wrote that spreading money between "
                  "enterprises one knows little about does not limit risk. "
                  "He wanted large sums where he truly understood the "
                  "business and trusted its managers.",
             "eg": "Ten funds in the account, and you can't say what any "
                   "one of them holds."},
        ],
        "apply":
            "Pick a bet you are tempted by. On a sheet, make three columns: "
            "what I can calculate (cost, term, the most I can lose); what I "
            "simply do not know; and whether I want to follow because I "
            "have priced it or because I am afraid of being the only one "
            "who didn't. Then count how many things in your account you "
            "could explain in three sentences, how they earn and why their "
            "managers deserve trust. He left one rule: don't write a guess "
            "like a calculation, don't treat company as judgment, and "
            "don't let a count stand in for understanding.",
        "q": [
            "Of such matters we simply do not know.",
            "Failing conventionally beats succeeding unconventionally, for reputation.",
            "The clever guess what the crowd expects the crowd to think.",
            "Spread wide enough and you still can't spread out ignorance.",
        ],
        "l": ["Nassim Taleb", "George Soros", "Howard Marks",
              "Friedrich Hayek"],
        "contrast": [
            {"n": "Friedrich Hayek",
             "why": "Both accepted that no one can know everything. Hayek "
                    "trusted prices as signals scattered through everyone's "
                    "hands, so each person acts where they know. Keynes "
                    "feared that expectations can lose their footing "
                    "together, and wanted someone to steady demand when "
                    "nobody can see. One gave the not-knowing to prices; "
                    "the other to someone who would stand behind them."},
            {"n": "George Soros",
             "why": "Both saw expectations pushing prices. Soros treated "
                    "that loop as something to trade, riding it and leaving "
                    "the moment he was wrong. Keynes treated it as "
                    "something to be wary of, because the professionals "
                    "were following the crowd to avoid blame, not because "
                    "they had judged worth."},
        ],
    },
]

INTROS = {
    "keynes":
        "British economist who founded macroeconomics with the General "
        "Theory (1936) and also ran real money for a Cambridge college and "
        "for insurers. He said some things have no calculable odds, that "
        "professionals mostly fear being wrong alone more than being wrong, "
        "and that you should own what you understand",
}

SCENES = [
    ("Do I jump in now", "AI arrived", [
        ("Nobody can call it. What am I betting on?",
         [("keynes", "we-simply-do-not-know")]),
    ]),
    ("Making money work", "Money", [
        ("Holding cash makes me feel like a coward.",
         [("keynes", "we-simply-do-not-know")]),
        ("I own a bit of everything and understand none of it.",
         [("keynes", "know-what-you-hold")]),
    ]),
    ("Everyone is piling in", "Money", [
        ("I don't even like it. I just can't be the only one out.",
         [("keynes", "fail-conventionally")]),
    ]),
]

ASKS = {
    "keynes/we-simply-do-not-know":
        "Nobody can call it. What am I betting on?",
    "keynes/fail-conventionally":
        "I don't even like it. I just can't be the only one out.",
    "keynes/know-what-you-hold":
        "I own a bit of everything and understand none of it.",
}

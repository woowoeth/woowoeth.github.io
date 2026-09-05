# -*- coding: utf-8 -*-
"""Thomas Schelling — English.

Schelling wrote in English, so the job here is not translation but rescue: his
two most useful results have been flattened into slogans about burning bridges
and about Grand Central. Both are mechanisms with conditions attached, and the
conditions are the part that decides whether they work for you or against you.
"""

PARENT = {
    "name": "Thomas Schelling",
    "slug": "schelling",
    "blurb": "Deep read",
    "items": [
        {"k": "binding-yourself", "n": "The advantage of tied hands",
         "w": "Trade options away for credibility", "ready": True,
         "line": "The strongest party at the table is often the one who cannot concede"},
        {"k": "focal-points", "n": "The Schelling point",
         "w": "Meeting without being able to talk", "ready": True,
         "line": "Lost in New York, where do you go? Most people said the same place"},
    ],
}

CHAPTERS = [
    {
        "k": "binding-yourself",
        "n": "The advantage of tied hands",
        "w": "Trade options away for credibility",
        "src": "The Strategy of Conflict, chapter 2",
        "dek": "Game theory says more options are better. This is about the "
               "case where Schelling proved the opposite.",
        "story":
            "The Strategy of Conflict sets up a proposition against instinct: "
            "the power to constrain an adversary may depend on the power to "
            "bind oneself. In bargaining, tying yourself to a position and "
            "burning the way back can win. The mechanism is credibility. You "
            "say you will never concede, and what the other side reads is not "
            "your tone but whether you still can. Anyone holding a concession "
            "in reserve has his threats discounted. His extreme case is the "
            "game of chicken: ==the driver who pulls the steering wheel off "
            "and throws it out of the window, in full view, wins.==",
        "f": [
            {"n": "Credibility comes from cannot, not from will not",
             "d": "I do not want to concede is a preference and can change at "
                  "any moment. I cannot concede is a fact the other side has "
                  "to plan around. A strong commitment therefore converts "
                  "preference into structure: a public statement, a clause, "
                  "an agent with no authority to vary. Each welds will not "
                  "into cannot.",
             "eg": "This is my final price convinces nobody. The price is "
                   "locked by head office sends them to the other terms. The "
                   "second is strong because it made you weak."},
            {"n": "Whoever binds first sets the problem",
             "d": "While both sides can still move, bargaining is a two-way "
                  "pull. The moment one side locks itself irreversibly, the "
                  "whole remaining room to adjust belongs to the other, who "
                  "either crashes or goes around. The order of commitment is "
                  "therefore a weapon in its own right.",
             "eg": "A company announcing a shipping date in public has handed "
                   "the question of who adapts to whom to its entire supply "
                   "chain. After that, everyone else bends."},
            {"n": "Bind the wrong hand and it stays bound",
             "d": "The cost is written into the principle: credibility comes "
                  "from irreversibility, so a mistake cannot be walked back. "
                  "Two checks before using it. Is this position worth all of "
                  "your flexibility, and might they prefer to crash? Make "
                  "self-binding a daily posture and you will end up welded to "
                  "something small.",
             "eg": "A public never discount flag looks strong until the "
                   "market turns, share drains away and there is no way down. "
                   "The bargaining edge is repaid with interest."},
        ],
        "q": [
            "The power to constrain an adversary may depend on the power to "
            "bind oneself.",
            "In bargaining, weakness is often strength.",
            "A threat works when they believe you have no choice left.",
        ],
        "apply":
            "Where you are: you need them to believe you will not move.\n"
            "Ask first: can I turn will not into a cannot they can verify, "
            "and is this position worth burning my flexibility for?\n"
            "Where it goes wrong: binding yourself weekly until the word "
            "irreversible means nothing; or tying your hands and quietly "
            "untying them, which is found out once and ends every commitment "
            "you make afterwards.",
    },
    {
        "k": "focal-points",
        "n": "The Schelling point",
        "w": "Meeting without being able to talk",
        "src": "The Strategy of Conflict, chapter 3",
        "dek": "Two people are lost in New York and cannot call each other. "
               "This is about why most of them pick the same spot.",
        "story":
            "Schelling ran a famous informal experiment. You have to meet "
            "someone in New York. Neither of you was told where or when, and "
            "you cannot communicate. Where do you go, and at what hour? The "
            "answers clustered hard: the information booth at Grand Central, "
            "at noon. Nothing makes that place better on any logical test. It "
            "wins on prominence, because everybody guesses that everybody "
            "else will guess it. Schelling called such places focal points: "
            "==when people cannot communicate, they converge on the place "
            "each expects the other to expect.== The force is not in being "
            "reasonable. It is in everyone knowing that everyone knows.",
        "f": [
            {"n": "Coordination runs on shared prominence, not optimality",
             "d": "When several parties must line up without enough "
                  "communication, the winner is not the best option but the "
                  "most visible and the most easily guessed at by everyone "
                  "else: round numbers, precedent, last time's place, first "
                  "on the list. Designing a default means looking for the "
                  "point everyone would blindly point to.",
             "eg": "A team across time zones can never compute the slot that "
                   "suits everyone. Ten on Monday morning is not optimal, and "
                   "everyone can guess it, so it holds."},
            {"n": "Focal points are the hidden floor of a negotiation",
             "d": "Where does haggling actually land? Often on a focal point: "
                  "split it down the middle, a round price, last year's "
                  "terms. Once you move off the focal point every particular "
                  "number needs a reason, and reasons are a new battlefield. "
                  "Controlling a negotiation is sometimes just placing that "
                  "point in advance.",
             "eg": "The gap between asking a hundred and asking ninety-seven "
                   "is not three. A hundred needs no explanation; "
                   "ninety-seven invites why not ninety-five."},
            {"n": "A convention is valuable because it is focal",
             "d": "Plenty of conventions are not defensible on their merits, "
                  "and they are still the point everyone knows everyone "
                  "knows. Abolish one without supplying a new focal point and "
                  "what you get is not an improvement, it is dispersal. Have "
                  "the replacement ready and equally prominent.",
             "eg": "Cancel the weekly report with nothing to replace it and "
                   "information does not move to a better channel. It "
                   "scatters into private messages."},
        ],
        "q": [
            "When people cannot communicate, they converge on what each "
            "expects the other to expect.",
            "A focal point wins on prominence, not on merit.",
            "Meeting in New York? Most said the information booth at noon.",
        ],
        "apply":
            "Where you are: several parties have to line up and the cost of "
            "talking it all through is too high.\n"
            "Ask first: what is the natural focal point here, and can the "
            "answer I want be placed at it?\n"
            "Where it goes wrong: insisting on an optimum nobody would ever "
            "guess; or abusing focal points to dress an unfair split as the "
            "way it has always been done.",
    },
]

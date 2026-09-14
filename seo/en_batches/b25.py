# -*- coding: utf-8 -*-
"""Daily entry, day 5: Charles P. Kindleberger.

Picked by fan-out. Two of the thinnest Chinese situations are 怕错过 and
人人都在喊风口 (6 chapters each); the English equivalents are just as thin
(Everyone is piling in, 3 questions). What hangs there now - Soros, Le Bon,
Perez, Marks - all argue about the market: it is reflexive, crowds are
contagious, bubbles follow a script, price already holds the consensus.
None of them can say the two things Kindleberger says. First, the fuel is
credit rather than optimism, so the question is not is the story true but
whose money is arriving. Second, what actually breaks an individual is not
the market at all: it is one specific person you know who got rich.

Both scenes already exist, so no SC_BOX. The quoted line is his own and is
used verbatim, capitalisation included; every other line here is ours and is
not dressed up as a quotation.

Three stories, no overlap: the entry uses Washington 1947, chapter one the
1978 table of three centuries, chapter two the lecture line and the laugh.
"""

ENTRIES = [
    {
        "c": "Money and risk", "n": "Charles P. Kindleberger",
        "slug": "kindleberger", "e": "United States · 1910-2003",
        "w": "Credit", "y": 1910,
        "d": "An American economist, born in New York in 1910, on the faculty "
             "at MIT from 1948 for half a century, author of more than thirty "
             "books. After the war he served at the State Department and spent "
             "1947 and 1948 as counselor for the European Recovery Program - "
             "the Marshall Plan crossed his desk. He had no patience for "
             "economics that modelled people as accurate calculating machines, "
             "and preferred to work through three hundred years of ledgers. "
             "The World in Depression, 1929-1939 (1973) argued that the slump "
             "ran so deep and so long not because nobody knew what to do, but "
             "because no country was willing to hold the thing up. Manias, "
             "Panics, and Crashes (1978) laid every mania side by side and "
             "found one shape: something real begins it, credit inflates it, "
             "then euphoria, distress, revulsion. The most quoted line in that "
             "book is not about money at all. It is about the person sitting "
             "next to you.",
        "story":
            "Washington, 1947. Kindleberger is thirty-seven, advising on the "
            "European Recovery Program at the State Department, and the work "
            "is concrete: how much coal this country is short of, how much "
            "grain, how many dollars. One thing from fifteen years earlier "
            "never left him. After 1929 no country would step forward and hold "
            "the world up - Britain could no longer, America would not yet - "
            "and a panic stretched into a decade. In 1973 he wrote that "
            "explanation into a book. His subject was never equilibrium. It "
            "was plumbing: which pipe the money runs through, and the day it "
            "stops.",
        "f": [
            {"n": "A mania runs to a timetable",
             "d": "Displacement, credit expansion, euphoria, distress, "
                  "revulsion. He fitted three centuries of collapse into those "
                  "five and the order held. Knowing the order will not tell "
                  "you where the top is. It tells you roughly which step you "
                  "are standing on.",
             "eg": "When you hear this time is different, ask where in the "
                   "sequence that sentence usually turns up."},
            {"n": "The real thing is the starting point, not the case",
             "d": "Every mania opens with something genuinely good: a new "
                  "technology, a new market, a new route. So the fundamentals "
                  "are real can never prove the price is sane. It is the "
                  "standard opening of every bubble ever recorded.",
             "eg": "Railways were real. The internet was real. Both were real, "
                   "and both collapsed once anyway."},
            {"n": "Credit is the accelerant",
             "d": "He shared Minsky's judgment: prices leave the ground on "
                  "borrowed money, not on mood. Mood only makes the talk "
                  "bigger; borrowing makes the position bigger. Tighten the "
                  "money and the finest story will not hold it up.",
             "eg": "The same hot sector bought with cash and bought on margin "
                   "are two entirely different things."},
            {"n": "What breaks you is the person next to you",
             "d": "The line he polished for decades says that what disturbs "
                  "judgment is not the market but seeing a friend get rich. "
                  "That is not a flourish. It is his mechanism for why "
                  "euphoria accelerates: comparison bites harder than greed.",
             "eg": "A stranger's windfall leaves you cold. One screenshot in "
                   "the class group chat keeps you up."},
            {"n": "The lender of last resort",
             "d": "How deep the wreck goes depends on whether anyone both able "
                  "and willing steps in. His point was that nothing here is "
                  "automatic: who acts, when, and how far are decided by "
                  "people, every single time.",
             "eg": "Whether a crisis lasts weeks or ten years often forks in "
                   "the first few days, on a handful of decisions."},
        ],
        "apply":
            "Next time you feel the pull, put the chart away and write three "
            "lines. One: what is the real thing here, specific enough to name "
            "who is actually earning more because of it. Two: where is the new "
            "money coming from, their own or borrowed. Three: who is the "
            "person making you restless today. Most people find the third line "
            "is the real question - not is this worth it, but am I going to "
            "lose to them. The two questions often have opposite answers.",
        "q": [
            "What turns something real into a mania is credit, not optimism.",
            "Every mania opens with something genuinely real. That is the trap.",
            "Prices leave the ground on borrowed money, not on mood.",
            "How long a crisis lasts depends on who is willing.",
        ],
        "l": ["George Soros", "Howard Marks", "Technological Revolutions",
              "The Crowd", "Jesse Livermore"],
        "contrast": [
            {"n": "Howard Marks",
             "why": "Both take the market's temperature: Marks reads where "
                    "sentiment sits on the pendulum, Kindleberger counts how "
                    "much of the money in the room was borrowed"},
            {"n": "Technological Revolutions",
             "why": "Both say bubbles follow a script. Perez times hers by the "
                    "installation phase of a technology, Kindleberger times "
                    "his by the looseness of credit - one mania, two rulers"},
        ],
    },
]

INTROS = {
    "kindleberger": "Economist who laid three centuries of manias side by side "
                    "and found credit, not optimism, underneath",
}

SCENES = [
    ("Everyone is piling in", "Money", [
        ("Someone I know got rich on this and I can't sit still.",
         [("kindleberger", "a-friend-gets-rich")]),
        ("People are borrowing to get in. Is that the signal?",
         [("kindleberger", "credit-is-the-fuel")]),
    ]),
    ("It dropped and I want out", "Money", [
        ("One firm blew up and everyone says it's a one-off.",
         [("kindleberger", "credit-is-the-fuel")]),
    ]),
]

ASKS = {
    "kindleberger/a-friend-gets-rich":
        "Someone I know got rich on this and I can't sit still.",
    "kindleberger/credit-is-the-fuel":
        "People are borrowing to get in. Is that the signal?",
}

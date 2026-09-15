# -*- coding: utf-8 -*-
"""C. Northcote Parkinson - English.

English readers meet Parkinson's Law as an office joke. This page takes the
two claims underneath it seriously: the amount of work is not fixed, and an
organisation grows at a rate unhooked from the work it has. Quoted lines are
his own wording, from the 1955 Economist article and from Parkinson's Law:
The Pursuit of Progress (1957).
"""

PARENT = {
    "name": "C. Northcote Parkinson",
    "slug": "parkinson",
    "blurb": "Deep read",
    "items": [
        {"k": "work-expands", "n": "Work expands to fill the time",
         "w": "You are not disorganised. The container is too big", "ready": True,
         "line": "A postcard takes three minutes, or it takes a whole day"},
        {"k": "officials-make-work", "n": "Officials make work for each other",
         "w": "An office grows whatever the work", "ready": True,
         "line": "Two-thirds fewer ships, eighty per cent more men administering them"},
    ],
}

CHAPTERS = [
    {
        "k": "work-expands",
        "n": "Work expands to fill the time",
        "w": "You are not disorganised. The container is too big",
        "src": "Parkinson's Law (1957), chapter 1, first published in The Economist, 19 November 1955",
        "dek": "You think you are short of time. This chapter argues the amount of "
               "work is set by the time you give it.",
        "story":
            "In November 1955 The Economist ran an unsigned piece by a naval "
            "historian teaching in Singapore. Its opening sentence finished the "
            "argument: ==work expands so as to fill the time available for its "
            "completion==. His example is an elderly lady with nothing else to "
            "do, who spends an entire day sending one postcard to her niece in "
            "Bognor Regis: finding the card, finding her glasses, hunting for "
            "the address, drafting the sentence, wondering whether to take an "
            "umbrella. A busy man posts the same card in three minutes.",
        "f": [
            {"n": "The amount of work is not given",
             "d": "Most advice about time assumes the workload is fixed and the "
                  "only variable is your speed. Parkinson turns that over. Work "
                  "behaves like a gas: it expands to whatever container you hand "
                  "it, and the hand is yours.",
             "eg": "The same weekly report is a forty-minute job tonight and a "
                   "whole afternoon if it is due on Friday."},
            {"n": "Change the container, not your willpower",
             "d": "If the expansion is automatic, working faster buys nothing - "
                  "the same task eats the saved hours back. What works is a "
                  "smaller container: an earlier deadline, a twenty-five minute "
                  "meeting, a headcount fixed before the work starts.",
             "eg": "Move a deadline from two weeks to three days and what arrives "
                   "is usually no worse."},
            {"n": "The emptiest diary complains loudest",
             "d": "What swells is not only the hours but the weight of the thing. "
                  "Someone with a single task will brood over it, over-prepare it, "
                  "revise it six times, and be genuinely exhausted by evening. "
                  "Busyness tracks load far more weakly than people assume.",
             "eg": "The person juggling five things is often the one who answers "
                   "you fastest."},
            {"n": "This is not an argument for a full diary",
             "d": "Booking every slot is the law doing its work for you: once "
                  "booked, each task swells to fill its slot. He is talking about "
                  "sizing the job, not about the density of the calendar. White "
                  "space is the only place you can hold expansion down.",
             "eg": "After your most tightly booked week, you cannot name the one "
                   "thing that actually moved."},
        ],
        "apply":
            "Where you are: the day ends and none of it was yours, so you blame "
            "the shortage of hours.\n"
            "Ask first: if this were due at three this afternoon, which steps "
            "would I cut - and who asked for those steps?\n"
            "Where it goes wrong: using it to squeeze somebody else's deadline. "
            "A smaller container only works if you also cut what is inside it; "
            "shrink the date alone and the expansion moves into their evening.",
        "q": [
            "Work expands so as to fill the time available for its completion.",
            "Give a task an afternoon and it takes an afternoon.",
            "White space is not waste. It is the only brake.",
        ],
    },
    {
        "k": "officials-make-work",
        "n": "Officials make work for each other",
        "w": "An office grows whatever the work",
        "src": "Parkinson's Law (1957), chapter 1, on the Admiralty establishment tables; the bicycle shed is from the chapter on high finance",
        "dek": "Your team is drowning and you are about to hire two more. This "
               "chapter asks whether the new people make new work.",
        "story":
            "Parkinson read the old Admiralty establishment tables. Between 1914 "
            "and 1928 the Royal Navy's capital ships fell from sixty-two to "
            "twenty and its sailors were cut as well, while Admiralty officials "
            "rose from two thousand to 3,569, close to eighty per cent more. "
            "Two-thirds fewer ships; eighty per cent more men administering them. "
            "He found the same curve at the Colonial Office: less territory to "
            "govern each year, a larger office each year. ==An organisation grows "
            "at a rate unrelated to the work it has to do==.",
        "f": [
            {"n": "Two nearly instinctive rules",
             "d": "He reduced the bloat to two lines: an official wants to "
                  "multiply subordinates, not rivals; and officials make work for "
                  "each other. The first explains why an overloaded manager never "
                  "asks for a peer. The second explains why the new hires really "
                  "are busy.",
             "eg": "The two new people need a weekly report, an alignment meeting "
                   "and a review. None of it existed before they arrived."},
            {"n": "The growth rate holds whatever the workload",
             "d": "He measured the curve: staff climbed by roughly five to six per "
                  "cent a year whether the work grew or shrank. The sting sits in "
                  "the second half. It is not that more work brought more people. "
                  "The two are simply unhooked.",
             "eg": "Cut a product line and the meeting built around it often keeps "
                   "circulating minutes."},
            {"n": "The smaller the sum, the longer the debate",
             "d": "One committee waved a ten-million-pound reactor through in two "
                  "and a half minutes, argued for forty-five over a bicycle shed "
                  "costing three hundred and fifty, and spent longer still on "
                  "twenty-one pounds of refreshments without settling it. Nobody "
                  "feels competent about the large number.",
             "eg": "The loudest item in a budget meeting is usually the one "
                   "everybody in the room can picture."},
            {"n": "Before hiring, separate two kinds of hire",
             "d": "You really are short-handed, and new people really do generate "
                  "new work. Both hold at once. What decides it is whether the "
                  "person does the job or manages the people doing the job. The "
                  "second kind grows the busyness straight back.",
             "eg": "Three months in, count how much of the new role's output ever "
                   "leaves the building."},
        ],
        "apply":
            "Where you are: the team says it is drowning and two new headcount "
            "are already approved.\n"
            "Ask first: once they arrive, who assigns their work and who reads "
            "their output - and how many hours does that take from those people?\n"
            "Where it goes wrong: reading it as never hire. He measured an office "
            "that grew with no work to do; he never claimed you always have "
            "enough hands.",
        "q": [
            "An official wants to multiply subordinates, not rivals.",
            "Officials make work for each other.",
            "The smaller the sum, the longer the meeting.",
        ],
    },
]

# -*- coding: utf-8 -*-
"""Daily entry, day 6: C. Northcote Parkinson.

Picked by fan-out. The thinnest Chinese situation is 时间不够用 (six
chapters); what hangs there now - Seneca, Cal Newport, Franklin, Atomic
Habits, Hochschild - all treat the workload as fixed and the reader's
discipline as the variable. Parkinson reverses the two: the work is the
variable, it inflates to whatever container it is given, so the fix is the
container, not the willpower. The second chapter carries that into
organisations, where the emptiest situations are hiring and cost cutting.

All four English situations already exist, so there is no SC_BOX here.
Quoted lines are his own wording. The law of triviality reads 18 words in
the original, over the quote limit, so it appears inside a section rather
than as a pull quote.

Three stories, no overlap: the entry is the desk of establishment tables in
Singapore, chapter one the opening sentence and the postcard, chapter two
the Admiralty numbers.
"""

ENTRIES = [
    {
        "c": "Power and organisation", "n": "C. Northcote Parkinson",
        "slug": "parkinson", "e": "United Kingdom · 1909-1993",
        "w": "Expansion", "y": 1909,
        "d": "A British historian, born in 1909, a specialist in British naval "
             "history who held the Raffles Chair of History at the University "
             "of Malaya in Singapore from 1950. On 19 November 1955 The "
             "Economist ran an unsigned article whose first sentence became the "
             "most quoted line in management writing: work keeps swelling until "
             "it has taken every hour you gave it. Two years later he collected "
             "that piece with a set of equally dry observations as Parkinson's "
             "Law, which sold in the millions. His evidence was not theory but "
             "ledgers: Admiralty establishment tables, Colonial Office "
             "headcounts, committee minutes. Out of them came a second and less "
             "comfortable finding: an organisation grows at its own steady rate, "
             "unrelated to how much work it actually has. He called all of it "
             "satire to the end of his life. Anyone who has worked inside a "
             "large institution reads it as reporting.",
        "story":
            "Singapore, 1955. Parkinson is forty-six and his working material "
            "is stacks of old establishment tables: how many ships in a given "
            "year, how many officers, how many men behind desks. To a historian "
            "they are sources. To him they read as a joke - fewer ships every "
            "year, more administrators every year, and the increase "
            "suspiciously regular. He posted under two thousand sardonic words "
            "to The Economist, unsigned. Two years later it was a book selling "
            "in the millions, and he spent the rest of his life insisting it "
            "had been a joke.",
        "f": [
            {"n": "A task takes the time you give it",
             "d": "His famous line is not a claim that people are lazy. It is a "
                  "claim that the duration of a job is not a fixed quantity: it "
                  "grows to the size of the container. So saving time starts "
                  "with the container, not with hurrying.",
             "eg": "The same document, due tonight or due next Wednesday, comes "
                   "back at two completely different thicknesses."},
            {"n": "An office grows on its own schedule",
             "d": "Between 1914 and 1928 the Royal Navy's capital ships fell "
                  "from sixty-two to twenty while Admiralty officials rose from "
                  "two thousand to 3,569. His conclusion was awkward: the growth "
                  "rate is steady and has nothing to do with the workload.",
             "eg": "Cut a product line and the standing meeting built around it "
                   "often survives it."},
            {"n": "Subordinates, not rivals",
             "d": "The mechanism is two sentences: an official wants to multiply "
                  "subordinates, not rivals, and those subordinates then make "
                  "work for one another. An overloaded manager almost never asks "
                  "for a peer to take half. He asks for two people of his own.",
             "eg": "A new role's first month of output is mostly process and "
                   "reporting aimed inward."},
            {"n": "The smallest number gets the longest debate",
             "d": "In one committee a ten-million-pound reactor went through in "
                  "two and a half minutes, a bicycle shed costing three hundred "
                  "and fifty took forty-five, and twenty-one pounds of "
                  "refreshments took longer again and was deferred. Nobody feels "
                  "competent about the large number.",
             "eg": "Look at the largest sum on the agenda. It will probably be "
                   "waved through first."},
            {"n": "He wrote satire and was read as doctrine",
             "d": "The book is a joke throughout and the formulas are half "
                  "serious. It has lasted seventy years because its target has "
                  "not moved: wherever people prove their worth by managing "
                  "others rather than by producing anything, both laws still run.",
             "eg": "Judge a new process by asking whether it adds output, or "
                   "adds things that must be managed."},
        ],
        "apply":
            "Take one thing you have been busy with all week and cannot say what "
            "moved on. Do two things. First, resize it: if it were due at three "
            "tomorrow, which steps would you cut? Write them down, then ask of "
            "each who originally required it - half will have no answer. Second, "
            "recall your last meeting and pair each item with the money it "
            "involved and the minutes it took. If those two run opposite, you "
            "have just watched the law of triviality happen in front of you.",
        "q": [
            "Work expands so as to fill the time available for its completion.",
            "Headcount climbs every year whatever the work happens to be.",
            "What he wants is subordinates, never a rival.",
            "The smaller the sum, the longer the meeting.",
        ],
        "l": ["Peter Drucker", "Andy Grove", "Taiichi Ohno", "Cal Newport",
              "Seneca"],
        "contrast": [
            {"n": "Cal Newport",
             "why": "Two places to cut into the same problem: Newport puts deep "
                    "work into the calendar, Parkinson says the block you booked "
                    "will swell to fill itself unless you make it smaller"},
            {"n": "Taiichi Ohno",
             "why": "Both say slack fills itself in: Ohno watches inventory hide "
                    "the problem, Parkinson watches time and headcount hide it"},
        ],
    },
]

INTROS = {
    "parkinson": "Naval historian who read two laws off old establishment "
                 "tables: work fills the time, and offices grow by themselves",
}

SCENES = [
    ("There's never enough time", "Body and energy", [
        ("I gave it the whole week and it took the whole week.",
         [("parkinson", "work-expands")]),
    ]),
    ("Everything is urgent at once", "Getting it done", [
        ("Nothing is due yet and nothing is finished either.",
         [("parkinson", "work-expands")]),
    ]),
    ("Everyone says it can't be done cheaper", "Getting it done", [
        ("We added people and the costs went up, not the work.",
         [("parkinson", "officials-make-work")]),
    ]),
    ("The spend nobody can justify", "Money", [
        ("We argue for an hour over the smallest line.",
         [("parkinson", "officials-make-work")]),
    ]),
]

ASKS = {
    "parkinson/work-expands":
        "I gave it the whole week and it took the whole week.",
    "parkinson/officials-make-work":
        "We added people and the costs went up, not the work.",
}

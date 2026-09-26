# -*- coding: utf-8 -*-
"""Herbert Simon — English.

The English reader may know "satisficing" as a word from a management
course, usually heard as a polite name for settling. The first page is
there to show it is a rule with two moving parts - a line set in advance,
and a line that moves with how hard the search turns out to be - taken from
his own house-selling example. The second page takes the sentence about a
poverty of attention, which is quoted everywhere and almost always without
the design test that follows it.

Sources: "A Behavioral Model of Rational Choice", Quarterly Journal of
Economics, 1955; "Rational Choice and the Structure of the Environment",
Psychological Review, 1956; "Invariants of Human Behavior", Annual Review of
Psychology, 1990, for the scissors; "Designing Organizations for an
Information-Rich World", in Martin Greenberger (ed.), Computers,
Communications, and the Public Interest, 1971, pp. 40-41; and The Sciences
of the Artificial, 1969, for the ant. Quoted lines keep his American
spelling.
"""

PARENT = {
    "name": "Herbert Simon",
    "slug": "herbert-simon",
    "blurb": "Deep read",
    "items": [
        {"k": "good-enough", "n": "The best one was never going to arrive",
         "w": "Buyers come one at a time, never all at once",
         "ready": True,
         "line": "The seller has a price in mind and takes the first offer "
                 "that meets it"},
        {"k": "poverty-of-attention",
         "n": "The more information, the poorer you are",
         "w": "What runs short is never the news, it is the reader",
         "ready": True,
         "line": "A new system earns its place by what it keeps away from "
                 "you"},
    ],
}

CHAPTERS = [
    {
        "k": "good-enough",
        "n": "The best one was never going to arrive",
        "w": "Buyers come one at a time, never all at once",
        "src": "\"A Behavioral Model of Rational Choice\", Quarterly Journal "
               "of Economics, 1955; \"Rational Choice and the Structure of "
               "the Environment\", Psychological Review, 1956",
        "dek": "Both options are fine, I have compared them for weeks, and I "
               "am still waiting for a better one. When do you stop looking?",
        "story":
            "In 1955 Simon used the sale of a house to make his point. The "
            "rational man of the textbooks lines up every possible buyer and "
            "every possible offer, then takes the highest. A real seller "
            "cannot wait for every buyer: they arrive one at a time, and the "
            "one turned away today may be gone tomorrow. So the seller fixes "
            "a price he will accept and takes the first offer that reaches "
            "it; if none does for a while, he lowers the price a little. "
            "==That is not laziness. It is the only kind of rationality a "
            "limited mind can finish computing.==",
        "f": [
            {"n": "Optimising needs three things you never have",
             "d": "To pick the best you must know every alternative, every "
                  "consequence of each, and how to rank those consequences. "
                  "Simon's point was that real people have none of the three "
                  "in full. He called it bounded rationality: people are not "
                  "unreasonable, reasoning just costs more than they have.",
             "eg": "You have seen twenty flats and want to see one more. The "
                   "first good one has already been let."},
            {"n": "He gave the habit a name",
             "d": "In the 1956 paper he modelled a small animal hunting for "
                  "food and able to see only a short way ahead, and showed "
                  "that a very simple rule kept it alive without any "
                  "optimising. He called the rule satisficing: clear the "
                  "line, then stop.",
             "eg": "Write down three hard requirements for the hire and make "
                   "an offer to the first candidate who meets all three."},
            {"n": "The line moves by itself",
             "d": "The line is not fixed. When satisfactory options turn up "
                  "easily, aspiration rises; when they will not turn up at "
                  "all, it falls. Good enough is not a number you bring to the "
                  "search. It is the number the search and the world agree on.",
             "eg": "Thirty applications and not a single reply means the line "
                   "should move, not that you should send thirty more."},
            {"n": "A pair of scissors",
             "d": "In 1990 he put it another way: human rational behaviour is "
                  "shaped by \"a scissors whose two blades are the structure "
                  "of task environments and the computational capabilities of "
                  "the actor.\" When you cannot choose, stop sharpening your "
                  "own blade and work on the other.",
             "eg": "Eight plans are too many to compare. Set a rule that cuts "
                   "five, then compare the three left."},
        ],
        "apply":
            "Where you are: two good options, two weeks of comparing, and a "
            "quiet hope that a third will turn up.\n"
            "Ask first: which few things do I actually need - written down, "
            "with the ones I cannot do without marked - and has one of the "
            "options in front of me already cleared all of them.\n"
            "Where it goes wrong: reading it as settle for whatever. He never "
            "says the line should be low. It should be set first, written "
            "down, and moved with how hard the search proves to be - and the "
            "less reversible the choice, the higher it sits and the longer "
            "you look.",
        "q": [
            "Draw the line first. Then see who clears it.",
            "Easy to find, raise the line. Hard to find, lower it.",
            "When you cannot compare them all, change the problem.",
        ],
    },
    {
        "k": "poverty-of-attention",
        "n": "The more information, the poorer you are",
        "w": "What runs short is never the news, it is the reader",
        "src": "\"Designing Organizations for an Information-Rich World\", in "
               "Computers, Communications, and the Public Interest, 1971; "
               "The Sciences of the Artificial, 1969",
        "dek": "I am afraid of missing anything new, so I try to read all of "
               "it. Why does more reading leave me more scattered?",
        "story":
            "By the late 1960s computers were moving into offices and "
            "government departments, and the talk was mostly of getting more "
            "information to the people who made decisions. Simon, writing "
            "about how organisations should be designed, turned the question "
            "round. Information consumes something: the attention of whoever "
            "receives it. So plenty of information means attention has "
            "become scarce. ==By that reckoning, a new system is worth "
            "installing only if it keeps more away from you than it hands "
            "you.==",
        "f": [
            {"n": "Information has an appetite",
             "d": "His words: what information consumes \"is rather obvious: "
                  "it consumes the attention of its recipients. Hence a "
                  "wealth of information creates a poverty of attention\", "
                  "and with it the need to decide where that attention goes.",
             "eg": "Three hundred messages read in a day, and by evening not "
                   "one of them comes back to you."},
            {"n": "Judge it by what it absorbs",
             "d": "He pushed the point into design. A new processing unit, "
                  "whether a computer or a new department, saves the rest of "
                  "the organisation attention only if it absorbs more "
                  "information than it produces. If it adds a stack of "
                  "reports every day, it is one more thing to read.",
             "eg": "A tool that summarises your feed and then sends you ten "
                   "extra items a day is a tap, not a filter."},
            {"n": "Decide first what not to read",
             "d": "If attention is the scarce thing, the task is not to get "
                  "a little more information but to ration attention: which "
                  "sources may claim it, and which get not even a glance. The "
                  "answer is cutting, not speed reading, and not another "
                  "aggregator.",
             "eg": "Someone subscribed to twenty channels gains more by "
                   "leaving fifteen than by learning to skim."},
            {"n": "The ant is simple, the beach is not",
             "d": "In The Sciences of the Artificial he describes an ant "
                  "crossing a beach on a winding path. The ant is simple: "
                  "\"The apparent complexity of its behavior over time is "
                  "largely a reflection of the complexity of the environment "
                  "in which it finds itself.\"",
             "eg": "On a day with every notification switched on, the path "
                   "you walk is bound to come out in pieces."},
        ],
        "apply":
            "Where you are: something new appears every day, you are afraid "
            "of missing it, you chase each one, and nothing stays.\n"
            "Ask first: of what I read this week, which items actually "
            "changed a decision I made - and how many hours did the rest "
            "take.\n"
            "Where it goes wrong: reading it as ignore anything new. He is "
            "describing a filter, and the test of a filter is that it keeps "
            "out more than it lets in. Reading less is not the goal; keeping "
            "attention for the few decisions that need it is.",
        "q": [
            "Information eats something, and what it eats is attention.",
            "A filter must keep out more than it lets in.",
            "A scattered day may be the ground, not you.",
        ],
    },
]

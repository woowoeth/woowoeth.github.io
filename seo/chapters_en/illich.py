# -*- coding: utf-8 -*-
"""Ivan Illich — English.

He wrote in English and the two books are short, so the job here is not to
introduce him but to keep the arithmetic intact. Both chapters rest on a
number he actually published, and both numbers are the reason the argument
survives being disagreed with: you can reject his politics and still have
to answer the division.
"""

PARENT = {
    "name": "Ivan Illich",
    "slug": "illich",
    "blurb": "Deep read",
    "items": [
        {"k": "two-watersheds", "n": "The two watersheds",
         "w": "A tool that starts eating its own purpose", "ready": True,
         "line": "Past the second one, medicine begins producing patients"},
        {"k": "effective-speed", "n": "Count what the tool costs you",
         "w": "Time saved and time spent belong on one ledger", "ready": True,
         "line": "Include the hours worked to pay for the car and the speed is five miles an hour"},
    ],
}

CHAPTERS = [
    {
        "k": "two-watersheds",
        "n": "The two watersheds",
        "w": "A tool that starts eating its own purpose",
        "src": "Tools for Conviviality (1973); Medical Nemesis (1975)",
        "dek": "Everyone says tools are neutral and it depends how you use "
               "them. What is worth reading is why he says they are not.",
        "story":
            "Every tool, he argued, crosses two watersheds. Before the "
            "first it solves a real problem: antibiotics keep alive "
            "people who would have died. Between the two it is steadily "
            "useful. ==Past the second it begins producing the thing it "
            "was built to remove.== He gave the medical version a name, "
            "iatrogenesis — illness produced by the treatment. The claim "
            "is not that doctors are bad, but that a system at scale "
            "acquires an appetite: it needs patients, so more of an "
            "ordinary life gets redefined as a condition requiring care. "
            "Schooling runs the same way — the more education is "
            "institutionalised, the more learning means being taught.",
        "f": [
            {"n": "The question is not whether it works",
             "d": "Between the watersheds a tool is a benefactor; past the "
                  "second it is a creditor. So does it work has no useful "
                  "answer — it does, and has since the first watershed. The "
                  "question is when what you pay to keep it began to exceed "
                  "what it gives you.",
             "eg": "The group chat saved ten emails the week it started. At "
                   "two hundred people you spend an hour a day reading it "
                   "and anything real still arrives privately."},
            {"n": "The signal is that it starts producing the opposite",
             "d": "Not inefficiency — the reverse of the original purpose. "
                  "Medicine producing illness, transport producing distance, "
                  "school producing a sense of ignorance. That signal is far "
                  "more sensitive than any efficiency number, because "
                  "efficiency often keeps climbing after the crossing.",
             "eg": "After the project tool went in, the time reporting got "
                   "beautiful and people began splitting tasks to make the "
                   "board look right. What the tool wants is replacing the "
                   "work."},
            {"n": "He wants a ceiling on tools, not a bonfire",
             "d": "Illich is not against technology. He is against "
                  "technology without an upper bound. A convivial tool is "
                  "one an ordinary person can master, repair and decline. "
                  "The test is whether it lets you leave: the higher the "
                  "exit cost, the less it is your tool and the more you are "
                  "its.",
             "eg": "A system you can export everything from and a system you "
                   "renegotiate with once you are locked in can have "
                   "identical features. The difference is whether you can "
                   "still walk."},
        ],
        "q": [
            "Past the second watershed a tool produces what it was meant to "
            "remove.",
            "Illness produced by the treatment itself I call iatrogenesis.",
            "A convivial tool is one you can master, repair, and do without.",
        ],
        "apply":
            "Where you are: a tool that genuinely saved effort at first, and "
            "you can no longer say whether it helps you or occupies you.\n"
            "Ask first: how many hours a week go into keeping it? Has it "
            "started producing the opposite of what it was for? What would "
            "leaving cost?\n"
            "Where it goes wrong: reading past the watershed as a reason to "
            "burn everything. Before the first watershed the tool is a real "
            "benefactor; he wants a ceiling, not a zero.",
    },
    {
        "k": "effective-speed",
        "n": "Count what the tool costs you",
        "w": "Time saved and time spent belong on one ledger",
        "src": "Energy and Equity (1974)",
        "dek": "An arithmetic problem about cars, and the reason it applies "
               "without modification to the tools on your machine.",
        "story":
            "He did the sum. A typical American man spends more than "
            "sixteen hundred hours a year on his car — driving, sitting "
            "in traffic, taking it to be repaired, and **working to pay "
            "for it**: purchase, petrol, insurance, loan. Those sixteen "
            "hundred hours buy him about seven and a half thousand miles. "
            "==Divide, and it comes to under five miles an hour — roughly "
            "walking pace.== The point is not that cars are useless. It "
            "is that we count the hours spent travelling and never the "
            "hours spent earning the thing. Savings go on one ledger and "
            "costs on another, which is how every tool saves time.",
        "f": [
            {"n": "Put both ledgers on one page and the answer often flips",
             "d": "Every tool advertises the time it saves. The real cost "
                  "also includes learning it, maintaining it, firefighting "
                  "when it fails, working to pay for it, and getting back "
                  "into the work after it has interrupted you. Those land on "
                  "different days, which is why nobody adds them up.",
             "eg": "Convert the monthly fee into your own hours, then add "
                   "the weekly maintenance. A surprising number of tools "
                   "stop making sense at that step."},
            {"n": "Fragmented time costs more than occupied time",
             "d": "A five-minute interruption does not cost five minutes. In "
                  "his arithmetic the working-to-pay-for-it hours are the "
                  "visible cost; the larger hidden cost of a modern tool is "
                  "that it cuts the day into pieces, and anything requiring "
                  "real thought can only be done in a whole one. Fragments "
                  "do not add up to it.",
             "eg": "Six fifteen-minute meetings occupy ninety minutes and "
                   "take the day, because no remaining stretch is long "
                   "enough to get in."},
            {"n": "Measure first, then decide; do not pick a side first",
             "d": "The value of the method is that it is arithmetic rather "
                  "than attitude. He did not say stop driving; he published "
                  "a division anyone can run again. Run it on a specific "
                  "tool and the answer is sometimes worth it and sometimes "
                  "I have been working for this thing. Both beat a position.",
             "eg": "Run it on the three tools you lean on hardest: total "
                   "hours in, divided by what it actually finished for you. "
                   "The worst score is the one to renegotiate."},
        ],
        "q": [
            "Count the hours worked to pay for it: five miles an hour.",
            "Savings on one ledger, costs on another: that is how tools "
            "save time.",
            "Work that needs thought happens in whole hours, never in "
            "fragments.",
        ],
        "apply":
            "Where you are: you have installed a stack of things that save "
            "time and your days are fuller than before.\n"
            "Ask first: adding the hours to learn it, maintain it, pay for "
            "it and recover from its interruptions — how much did it "
            "actually save?\n"
            "Where it goes wrong: using the sum to dismiss tools in general. "
            "He calculated a specific number, not a stance; whatever comes "
            "out ahead deserves to be used harder.",
    },
]

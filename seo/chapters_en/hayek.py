# -*- coding: utf-8 -*-
"""Friedrich Hayek — English.

For most English readers the name arrives pre-loaded with a politics, which
is the fastest way to stop reading. These two pages leave the politics alone
and take the engineering claim underneath it: knowledge that cannot be moved,
and the discipline that follows for anyone who has the authority to redesign
something.
"""

PARENT = {
    "name": "Friedrich Hayek",
    "slug": "hayek",
    "blurb": "Deep read",
    "items": [
        {"k": "knowledge-is-dispersed", "n": "Knowledge is dispersed",
         "w": "Nobody can hold the whole picture", "ready": True,
         "line": "A price is a telegraph system with the reasons stripped out"},
        {"k": "fatal-conceit", "n": "The fatal conceit",
         "w": "The curious task of economics", "ready": True,
         "line": "Show people how little they know about what they think they "
                 "design"},
    ],
}

CHAPTERS = [
    {
        "k": "knowledge-is-dispersed",
        "n": "Knowledge is dispersed",
        "w": "Nobody can hold the whole picture",
        "src": "The Use of Knowledge in Society (1945)",
        "dek": "A paper of a dozen pages, later voted one of the century's "
               "most important in economics. What assumption it destroyed.",
        "story":
            "The 1945 paper attacks an assumption everybody was making: "
            "collect the data centrally and the centre can compute the best "
            "allocation. His refutation takes the ground out from under it. "
            "==The knowledge we must make use of never exists in concentrated "
            "or integrated form==, only as dispersed, incomplete and often "
            "contradictory bits held by separate individuals. The kind that "
            "matters most is knowledge of the particular circumstances of "
            "time and place, which cannot be reported upward without going "
            "stale. Prices solve that: when tin is short, users need no "
            "reason, only the new number.",
        "f": [
            {"n": "Local knowledge goes false on the way up",
             "d": "What the front line holds is immediate, specific and "
                  "attached to a situation. Each level of aggregation strips "
                  "out the time and the detail, so what arrives at the top is "
                  "a stale average. An organisation that waits for reports "
                  "steers today with yesterday's blur.",
             "eg": "Sales knew the real reason that account left on "
                   "Wednesday. By the time it reads as satisfaction down two "
                   "per cent in the monthly, the available move is a "
                   "different one."},
            {"n": "Move the decision to where the knowledge already is",
             "d": "His conclusion follows: since that knowledge cannot "
                  "travel, send the authority to it and let whoever stands in "
                  "the situation decide inside a mandate. The centre's job is "
                  "not to decide for them but to supply signals — price, "
                  "cost, priority — that carry the wider picture.",
             "eg": "Rather than have a shop queue for promotion approval, "
                   "give it a margin floor and live costs. The manager knows "
                   "it is raining and the shop opposite is clearing stock."},
            {"n": "Inside the organisation you also need something priced",
             "d": "The beauty of a price is compression: it explains nothing "
                  "and transmits weight. Most internal coordination fails "
                  "because what gets passed around is reasons and stories "
                  "with no shared measure of importance. Put a number on a "
                  "scarce resource and the scramble turns into arithmetic.",
             "eg": "Compute, design and legal are demanded infinitely while "
                   "they are free. Give them an internal transfer price and "
                   "every team cuts its own optional requests."},
        ],
        "q": [
            "The knowledge we must make use of never exists in concentrated "
            "or integrated form.",
            "The price system is a mechanism for communicating information.",
            "A telegraph system: it carries the weight and not the reason.",
        ],
        "apply":
            "Where you are: you are designing a mechanism where all the "
            "information is gathered centrally and then decided on "
            "centrally.\n"
            "Ask first: how much of the knowledge this depends on is local "
            "knowledge that expires the moment it is reported?\n"
            "Where it goes wrong: turning delegation into abandonment with no "
            "signal to align on, or setting internal prices and then letting "
            "people go around them by relationship.",
    },
    {
        "k": "fatal-conceit",
        "n": "The fatal conceit",
        "w": "The curious task of economics",
        "src": "The Fatal Conceit (1988)",
        "dek": "He defined his own discipline's task as pouring cold water, "
               "not forecasting. Why the cleverest people need that water "
               "most.",
        "story":
            "The title of his last book is the diagnosis: the fatal conceit, "
            "the idea that man can shape the world around him according to "
            "his wishes. His definition of the discipline became the famous "
            "line. ==The curious task of economics is to demonstrate how "
            "little men really know about what they imagine they can "
            "design.== Markets, language, law and morals all work, and none "
            "of them was designed; they grew through countless trials. The "
            "designer's fatal position is that he has to pretend to hold "
            "knowledge scattered across millions of heads.",
        "f": [
            {"n": "A grown order has load-bearing walls you cannot see",
             "d": "Each clause in a set of old rules may be holding up a "
                  "problem you never meet. They were filtered by elimination "
                  "rather than argued into place. The rebuilder's risk is not "
                  "a shortage of ideas; it is being unable to tell which wall "
                  "is carrying weight.",
             "eg": "The new manager cuts an obviously redundant old process. "
                   "Three months later it turns out to have been the only "
                   "gate against one class of accident, and whoever built it "
                   "left years ago."},
            {"n": "The cleverer you are, the further you push design",
             "d": "Conceit scales with intelligence: the better you are at "
                  "running a system through in your head, the easier it is to "
                  "forget the variables the real one contains. His cold water "
                  "is aimed at clever people. Design is legitimate over the "
                  "patch where you genuinely hold the relevant knowledge.",
             "eg": "The most meticulous five-year plan dies worst, because "
                   "its own rigour left no room for the world outside it. A "
                   "rough map with quarterly corrections survives."},
            {"n": "The alternative is to make trial and error run",
             "d": "Accepting that knowledge cannot be centralised is not an "
                  "argument for doing nothing. It swaps designing the best "
                  "solution for designing an environment that sorts "
                  "solutions: parallel attempts allowed, failure made cheap, "
                  "winners left free to spread. You design the track, not the "
                  "result.",
             "eg": "Instead of one head-office store layout for the country, "
                   "let a hundred shops adjust and rank them on sales per "
                   "square metre. What grows in six months nobody could have "
                   "drawn."},
        ],
        "q": [
            "The curious task of economics is to demonstrate how little men "
            "really know.",
            "How little they know about what they imagine they can design.",
            "The extended order our civilisation rests on was designed by "
            "nobody.",
        ],
        "apply":
            "Where you are: you have both the ability and the authority to "
            "redesign an entire system.\n"
            "Ask first: which clauses of the old one can I not explain the "
            "original purpose of? Where is the edge of what I actually know?\n"
            "Where it goes wrong: using orders grow, they are not made to "
            "block every reform including the rotten walls, or hiding behind "
            "trial and error where the arithmetic was available all along.",
    },
]

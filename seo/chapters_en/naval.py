# -*- coding: utf-8 -*-
"""Naval Ravikant — English.

The tweetstorm is aphoristic by design, which is why in English it gets
read as motivation and forgotten by lunchtime. Each chapter here takes one
of the aphorisms and does the thing the format cannot: says what it rules
out. Wealth versus status is a test you can run on your own last year.
Specific knowledge has a stated detection method. Neither is advice about
attitude.
"""

PARENT = {
    "name": "Naval Ravikant",
    "slug": "naval",
    "blurb": "Deep read",
    "items": [
        {"k": "assets-while-you-sleep", "n": "Assets that earn while you sleep",
         "w": "Wealth is not money", "ready": True,
         "line": "Stop for three months. Is it still producing"},
        {"k": "productize-yourself", "n": "Productise yourself",
         "w": "Specific knowledge times leverage", "ready": True,
         "line": "It feels like play to you and looks like work to everyone else"},
    ],
}

CHAPTERS = [
    {
        "k": "assets-while-you-sleep",
        "n": "Assets that earn while you sleep",
        "w": "Wealth is not money",
        "src": "How to Get Rich (Without Getting Lucky), the tweetstorm",
        "dek": "The first line cuts one word into three. What matters is "
               "where each of the three leads.",
        "story":
            "The storm opens: seek wealth, not money or status. Each is "
            "defined. ==Wealth is assets that earn while you sleep== — "
            "businesses, code, content, equity. Money is how we transfer "
            "wealth. Status is your place in the social hierarchy. What "
            "matters is the kind of game each is. Creating wealth is "
            "positive sum: everyone can get richer. Status is zero sum — "
            "for you to rise somebody falls, which is why people "
            "attacking wealth creators are usually playing status. And "
            "there is one road to the first: ownership. You will not get "
            "rich renting out your time, because time does not copy.",
        "f": [
            {"n": "Work out which game you are actually playing",
             "d": "A great deal of hard work leads to status rather than "
                  "wealth: titles, visibility, rankings. Those prizes "
                  "produce no cash flow and require you to keep showing "
                  "up to hold them. One test: stop for three months. Is "
                  "it still producing? If yes it is an asset.",
             "eg": "Two people work equally hard for a year. One accumulates "
                   "a title and photographs with useful people; the other "
                   "accumulates a tool with subscription revenue. The "
                   "difference shows itself the first time either takes a "
                   "holiday."},
            {"n": "Selling time has a ceiling because time will not copy",
             "d": "Work priced by the hour earns rate times hours. Both "
                  "factors are hard-capped, and the whole thing goes to zero "
                  "while you sleep. The way out is not raising the rate, it "
                  "is changing the formula — detaching output from duration. "
                  "Things made once and sold many times: code, content, "
                  "courses, systems, equity.",
             "eg": "A top consultant and an ordinary one differ by rate. A "
                   "consultant and someone who turned the method into "
                   "software differ by formula. The first is optimisation, "
                   "the second is a different race."},
            {"n": "Recognising a status attack saves you the reply",
             "d": "Anyone who does something visible attracts a portion of "
                  "criticism whose purpose is not correction but position — "
                  "pushing you down in a zero-sum game. Separating the two "
                  "kinds matters practically: the first deserves a careful "
                  "answer, and answering the second is scoring a point in "
                  "somebody else's game.",
             "eg": "Feedback after a launch splits in two. Specific problems "
                   "go on the fix list. Insinuations about your motives and "
                   "your standing are best left where they are."},
        ],
        "q": [
            "Seek wealth, not money or status.",
            "Wealth is assets that earn while you sleep.",
            "You will not get rich renting out your time. You need "
            "equity.",
        ],
        "apply":
            "Where you are: busy, doing reasonably well, and it all stops the "
            "moment you do.\n"
            "Ask first: of what I built this past year, what keeps producing "
            "when I am not there? What proportion?\n"
            "Where it goes wrong: using not playing status games to excuse "
            "being bad at people — reputation and relationships are "
            "themselves assets. What is worth avoiding is ranking for its own "
            "sake.",
    },
    {
        "k": "productize-yourself",
        "n": "Productise yourself",
        "w": "Specific knowledge times leverage",
        "src": "The How to Get Rich tweetstorm; The Almanack of Naval "
               "Ravikant",
        "dek": "He compresses the whole method into two words. What each of "
               "the two refers to, and why the new leverage is different in "
               "kind.",
        "story":
            "The formula collapses into a phrase: ==productise "
            "yourself.== Yourself means specific knowledge — the kind you "
            "cannot be trained for, growing out of your temperament, "
            "obsessions and history; it feels like play to you and looks "
            "like work to others. Productise means putting leverage on "
            "it. Labour and capital are the old kinds and both need "
            "somebody's permission. The new kind replicates at zero "
            "marginal cost: code and media, which need permission from "
            "nobody. What you wrote keeps working while you sleep.",
        "f": [
            {"n": "Specific knowledge is not on any syllabus",
             "d": "Any skill taught in a standard way is supplied in "
                  "unlimited quantity and priced accordingly. Specific "
                  "knowledge comes from the part that cannot be "
                  "standardised: your combination of oddities, the "
                  "crossings between fields, an obsession out of "
                  "proportion to its subject. The detection method is his "
                  "own line — play to you, labour to others.",
             "eg": "Someone technical who can also make complicated things "
                   "funny; someone clinical who is compulsive about "
                   "spreadsheets. Each piece is ordinary. The combination has "
                   "no second supplier."},
            {"n": "Permissionless means you can start today",
             "d": "The bottleneck in the old leverage is persuasion: nothing "
                  "moves until you have hired someone or raised something. "
                  "Code and media delete that step. Writing, recording, "
                  "publishing — live today, at the cost of time rather than "
                  "consent. The opportunity of this generation is essentially "
                  "that the entry price of leverage fell to zero.",
             "eg": "The same insight can wait for funding and a team, or go "
                   "out as a public series of posts that grows an audience. "
                   "The second needs nobody's approval, and frequently "
                   "produces the first."},
            {"n": "Productising means taking yourself out of delivery",
             "d": "Where the two words end up: packaging your judgement, "
                  "taste and method into something that delivers without you "
                  "present. The test is replication — each additional user "
                  "should cost you an amount of time approaching zero. Until "
                  "then what you own is a good job. After it, an asset.",
             "eg": "Five years of consulting turned into a book, a course, a "
                   "self-serve tool. The same knowledge moves from sold by "
                   "the occasion to permanently on sale."},
        ],
        "q": [
            "Productise yourself.",
            "Specific knowledge feels like play to you but looks like work to "
            "others.",
            "Code and media are permissionless leverage.",
        ],
        "apply":
            "Where you are: capable, and your income is welded to your hours.\n"
            "Ask first: what do I do that is play to me and labour to others? "
            "Can it be packaged as code or as content and published without "
            "anyone's permission?\n"
            "Where it goes wrong: reading productise as everyone should sell "
            "a course — without specific knowledge, leverage only amplifies "
            "the average. And do not use polishing the knowledge to postpone "
            "publishing forever; leverage only counts what shipped.",
    },
]

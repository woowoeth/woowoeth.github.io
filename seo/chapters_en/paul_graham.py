# -*- coding: utf-8 -*-
"""Paul Graham — English.

Both essays are online, short, and better written than anything a summary
of them can be, so the page does not try to replace them. What it adds is
the thing readers of the first essay most often get wrong — that the
handmade phase is a stage with an exit condition, not a virtue — and, for
the second, the reason the question belongs before every other question
rather than somewhere in the finance section.
"""

PARENT = {
    "name": "Paul Graham",
    "slug": "paul-graham",
    "blurb": "Deep read",
    "items": [
        {"k": "dont-scale", "n": "Do things that do not scale",
         "w": "The early work is meant to be handmade", "ready": True,
         "line": "They flew to New York and photographed the apartments themselves"},
        {"k": "default-alive", "n": "Default alive or default dead",
         "w": "Run this number before anything else", "ready": True,
         "line": "Most founders do not know which one they are"},
    ],
}

CHAPTERS = [
    {
        "k": "dont-scale",
        "n": "Do things that do not scale",
        "w": "The early work is meant to be handmade",
        "src": "Do Things That Don't Scale, 2013",
        "dek": "Founders think about scale constantly. He argues for the "
               "opposite direction — and is specific about what the handmade "
               "phase actually buys.",
        "story":
            "The essay opens against the instinct: ==startups do not take "
            "off by themselves; the founders make them take off.== The "
            "common mistake is chasing something scalable on day one, "
            "when the early period calls for recruiting users by hand. "
            "Airbnb had stalled, so the founders flew to New York week "
            "after week, knocked on hosts' doors and photographed their "
            "apartments themselves. Completely unscalable — and it found "
            "the switch that moved conversion. The output of that phase "
            "is not the handful of users; it is an unusually concentrated "
            "understanding of them, plus people so over-served they will "
            "tell others.",
        "f": [
            {"n": "Doing it by hand is the highest-bandwidth research there is",
             "d": "Surveys and dashboards show the shadow a behaviour "
                  "casts; being in the room shows the behaviour. In "
                  "people's living rooms it turned out photograph quality "
                  "was the bottleneck — an insight the analytics could "
                  "only ever have shown as low conversion. The expensive "
                  "thing early on is not slow growth, it is understanding "
                  "wrongly.",
             "eg": "Have the founders deliver the first hundred customers "
                   "personally. Every one is a piece of research arriving "
                   "with its full context. Time saved by delegating it comes "
                   "back doubled on the wrong roadmap."},
            {"n": "Over-serving is how you manufacture the first advocates",
             "d": "If early users get service indistinguishable from a "
                  "large company's, they have no reason to speak about "
                  "you. The handmade phase gives what no scaled operation "
                  "could — a founder replying in minutes, the product "
                  "bent around one person. That unreasonable care is the "
                  "raw material of word of mouth.",
             "eg": "Answering the first cohort at any cost brings customers "
                   "later that are cheaper than any advertising, because the "
                   "story they tell cannot be bought."},
            {"n": "Unscalable is a stage, not a creed",
             "d": "The essay gets quoted in halves. The correct loop is: do "
                  "it by hand, extract the one move that was actually doing "
                  "the work, then build that move into the product or the "
                  "process. Airbnb turned professional photography into a "
                  "platform feature. Handwork without extraction is diligence "
                  "covering for an absence of leverage.",
             "eg": "After three months of founders closing deals personally, "
                   "the deliverable is a list of the three actions that "
                   "decide a sale — then those get standardised. Not a fourth "
                   "month of closing deals."},
        ],
        "q": [
            "Startups do not take off by themselves. The founders make them "
            "take off.",
            "In the early days you have to recruit users manually.",
            "They went door to door photographing the hosts' apartments "
            "themselves.",
        ],
        "apply":
            "Where you are: the product just launched and you are torn "
            "between building growth machinery and serving users by hand.\n"
            "Ask first: is our understanding of why people buy or leave at "
            "dashboard level or living-room level?\n"
            "Where it goes wrong: keeping it handmade past the point of "
            "scale, so founders are still carrying the business on their "
            "backs; or doing it by hand for a long time and never extracting "
            "the repeatable move.",
    },
    {
        "k": "default-alive",
        "n": "Default alive or default dead",
        "w": "Run this number before anything else",
        "src": "Default Alive or Default Dead?, 2015",
        "dek": "He asks founders one question first, and most of them cannot "
               "answer it. Why it comes before every other conversation.",
        "story":
            "The first thing he asks a startup is ==are you default alive "
            "or default dead?== The definition is hard-edged: assuming "
            "expenses stay constant and growth continues as it has been, "
            "do you reach profitability on the money you have left? If "
            "yes, default alive. If no, default dead. What surprised him "
            "is how many founders do not know which they are. It comes "
            "first because it sets the character of every other "
            "conversation: a default alive company can talk about "
            "ambition; a default dead one has a single agenda item, "
            "getting out of that state — and is usually still discussing "
            "hiring, assuming the next round will arrive.",
        "f": [
            {"n": "You have to run it yourself, because nothing raises an alarm",
             "d": "A default dead company looks entirely normal from "
                  "inside: the product ships, the team grows, there is "
                  "money in the account. Death is scheduled months out on "
                  "a calendar nobody turns to. The question brings that "
                  "date forward to today — three numbers, ten minutes.",
             "eg": "Put the current answer and the death date on this "
                   "trajectory as page one of the monthly meeting. The "
                   "existence of that page reorders everything after it."},
            {"n": "Counting on the next round outsources your survival to a mood",
             "d": "He names the standard consolation: investor appetite "
                  "swings with the market and your death date does not. "
                  "The right move when default dead is not to fundraise "
                  "harder but to move the two variables under your "
                  "control — expenses and growth — until you are back on "
                  "the living side.",
             "eg": "A survival plan with raise a B round written into it has "
                   "handed the switch to somebody else's fund cycle. Cut to "
                   "within reach of break-even first; the negotiation even "
                   "smells different."},
            {"n": "The usual cause is hiring too early",
             "d": "His first-named cause of default dead is over-hiring — "
                  "using growth needs people to raise the burn ahead of "
                  "growth that then does not arrive. The remedy is "
                  "counter-intuitive: early growth comes far more from "
                  "founders making the product better than from headcount. "
                  "People should be added when growth is dragging you into "
                  "adding them.",
             "eg": "Build the team and wait for the business bets a fixed "
                   "cost on a forecast. Let the pain of growth force each new "
                   "hire instead, and the company stays on the living side."},
        ],
        "q": [
            "Are you default alive or default dead?",
            "With expenses flat and growth as it is, do you reach "
            "profitability in time?",
            "What surprises me is how many founders do not know the answer.",
        ],
        "apply":
            "Where you are: things are running normally and you cannot say "
            "where the cash-flow threshold is.\n"
            "Ask first: flat expenses, current growth — profitable before the "
            "money runs out? If the answer is no, today's agenda should be "
            "replaced entirely.\n"
            "Where it goes wrong: using default alive as an excuse not to "
            "grow — safe and stationary. The question protects the floor; the "
            "ceiling still takes ambition.",
    },
]

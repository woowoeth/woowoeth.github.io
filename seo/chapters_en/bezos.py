# -*- coding: utf-8 -*-
"""Jeff Bezos — English.

The shareholder letters are the primary source and they are public, which
means the English reader can check every line here against the original in
about a minute. That is a constraint worth taking seriously: the page has
to be accurate about what the letters actually say, and useful about the
part they leave implicit — which is that Day 1 is not a mood, it is four
named components with a mechanism behind each.
"""

PARENT = {
    "name": "Jeff Bezos",
    "slug": "bezos",
    "blurb": "Deep read",
    "items": [
        {"k": "day-one", "n": "Always Day 1", "w": "What Day 2 looks like",
         "ready": True,
         "line": "Day 2 is stasis, then irrelevance, then decline, then death"},
        {"k": "what-wont-change", "n": "Bet on what will not change",
         "w": "The question almost nobody asks", "ready": True,
         "line": "Nobody will ever ask for higher prices and slower delivery"},
    ],
}

CHAPTERS = [
    {
        "k": "day-one",
        "n": "Always Day 1",
        "w": "What Day 2 looks like",
        "src": "Amazon shareholder letters, 2016 and 2015",
        "dek": "Someone asked what Day 2 would look like. The answer, and the "
               "four parts he installed to keep it away.",
        "story":
            "He named the headquarters Day 1. In 2016 somebody asked what "
            "Day 2 looks like, and he answered in the shareholder letter: "
            "==Day 2 is stasis. Followed by irrelevance. Followed by "
            "excruciating, painful decline. Followed by death. And that "
            "is why it is always Day 1.== What follows is not a slogan "
            "but a recipe: customer obsession, resisting proxies, "
            "embracing external trends, high-velocity decisions. The last "
            "is the most quoted — most decisions are two-way doors you "
            "can walk back through, so they belong to small teams moving "
            "fast, at seventy per cent of the information you wish you "
            "had.",
        "f": [
            {"n": "Day 2 starts when process takes over from outcome",
             "d": "The first thing he names is the proxy: as an organisation "
                  "grows, people start checking whether the process was "
                  "followed rather than whether the customer was served. The "
                  "process is not the thing, and it is a young manager's "
                  "easiest confusion. When we followed the process becomes a "
                  "defence, Day 2 has already begun.",
             "eg": "When we went through every required review is treated as "
                   "the conclusion of a post-mortem rather than the start of "
                   "one, the process is now signing off on outcomes."},
            {"n": "Sort the door before you set the speed",
             "d": "One-way doors — irreversible — should be slow and "
                  "heavy; two-way doors fast and light. Most "
                  "organisations apply one-way approval to everything and "
                  "drag reversible decisions out for months. Sorting is "
                  "step one; step two is handing the two-way ones to "
                  "whoever is closest.",
             "eg": "Label every proposal one-way or two-way. On the two-way "
                   "ones cut two layers of approval and cap it at forty-eight "
                   "hours. Speed itself grows a culture willing to try."},
            {"n": "Customer obsession is the vaccine because customers are "
                  "never satisfied",
             "d": "He ranks this first, and the reason is mechanical: "
                  "customers are divinely discontent even when they say "
                  "they are happy. Obsession with competitors goes "
                  "mediocre as the competitors do; obsession with process "
                  "calcifies. Only discontent is an engine that never "
                  "stops.",
             "eg": "Change the quarterly goal from beat the competitor to "
                   "remove an annoyance the customer has stopped complaining "
                   "about. The first has a finish line; the second does not, "
                   "and only goals without one keep you young."},
        ],
        "q": [
            "Day 2 is stasis, followed by irrelevance, then decline, then "
            "death.",
            "Most decisions belong at seventy per cent of the information "
            "you wish you had.",
            "Customers are divinely discontent, even when they report being "
            "happy.",
        ],
        "apply":
            "Where you are: the company has grown, everything is orderly, and "
            "it feels slower.\n"
            "Ask first: of the last three significant decisions, which were "
            "one-way and which two-way? For the two-way ones, how long did "
            "they take and through how many layers?\n"
            "Where it goes wrong: applying high velocity to the irreversible "
            "ones, or turning customer obsession into support scripts while "
            "the actual obsession stays on the dashboard.",
    },
    {
        "k": "what-wont-change",
        "n": "Bet on what will not change",
        "w": "The question almost nobody asks",
        "src": "Public interviews (re:Invent 2012 among others); the 1997 "
               "shareholder letter",
        "dek": "Everyone asks him what the next ten years will change. He "
               "says the more useful question is the one he almost never "
               "gets.",
        "story":
            "He is asked constantly what will change in the next ten "
            "years. He says he is almost never asked ==what is not going "
            "to change== — and that the second question matters more, "
            "because you can build a strategy around what is stable. His "
            "own answer is unglamorous: in ten years customers will still "
            "want lower prices, faster delivery, more selection. Nobody "
            "will ever say, I love Amazon, I just wish the prices were "
            "higher and the delivery slower. Every dollar put into those "
            "is still paying interest a decade on.",
        "f": [
            {"n": "Change is news; constancy is foundation",
             "d": "A strategy that chases change is rebuilt every two years. "
                  "Investment in a need that does not move compounds for "
                  "twenty. The sorting question is easy to run: list what you "
                  "are currently funding and ask whether customers will still "
                  "want it in ten years. Two piles. The resources belong on "
                  "the certain one.",
             "eg": "Channels, formats and algorithms change annually. Cheaper, "
                   "faster, less hassle never do. Re-sort the budget on that "
                   "test and most companies find they have bet the wrong way."},
            {"n": "A need that does not change has no ceiling",
             "d": "Faster can always be faster; cheaper can always be "
                  "cheaper. Improvements aimed at those never reach a day "
                  "when they are done, so the moat can keep deepening "
                  "indefinitely. An advantage built on a trend has a shelf "
                  "life by construction: when the trend passes, the "
                  "accumulation resets to zero.",
             "eg": "Three days to next day to same day — each layer built on "
                   "the last. Growth from riding a hot format starts over "
                   "when the format does."},
            {"n": "Long term does not mean slow, it means willing to look bad",
             "d": "The 1997 letter says it outright: decisions are made "
                  "on long-term market leadership, not short-term profit "
                  "or Wall Street's reaction. Betting on what does not "
                  "change means years of putting profit back into "
                  "logistics, with ugly statements and steady ridicule. "
                  "The ticket price is sitting through that stretch.",
             "eg": "Declaring long-term thinking while reviewing teams "
                   "quarterly on short-term profit asks people to run a "
                   "marathon on a sprinter's breathing. Until the review "
                   "cycle changes, the strategy is wall decoration."},
        ],
        "q": [
            "You can build a strategy around the things that are stable over "
            "time.",
            "No customer will ever ask for higher prices and slower delivery.",
            "We make decisions on long-term market leadership, not short-term "
            "reactions.",
        ],
        "apply":
            "Where you are: the strategy meeting is all new trends and new "
            "tactics.\n"
            "Ask first: what three things will our customers certainly still "
            "want in ten years, and what share of current spending is aimed "
            "at those three?\n"
            "Where it goes wrong: using constancy as an excuse to ignore "
            "trends — embracing external trends is one of his own four. What "
            "does not change is the need; how you meet it has to change "
            "constantly.",
    },
]

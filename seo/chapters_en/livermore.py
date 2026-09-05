# -*- coding: utf-8 -*-
"""Jesse Livermore — English.

Reminiscences of a Stock Operator sits on the English trading shelf as a book
of hard maxims, quoted for speed and nerve. Both chapters here take the other
line: the fastest operator of his age credited his money to sitting still,
and the rule he wrote about hope and fear is one he suspended often enough to
go broke four times.
"""

PARENT = {
    "name": "Jesse Livermore",
    "slug": "livermore",
    "blurb": "Deep read",
    "items": [
        {"k": "sitting-tight", "n": "Sitting tight",
         "w": "Being right was never the hard part", "ready": True,
         "line": "It never was my thinking that made the big money"},
        {"k": "hope-and-fear-inverted", "n": "Hope and fear, the wrong way "
         "round", "w": "The instinct points in the wrong direction",
         "ready": True,
         "line": "Fear when you should hope; hope when you should fear"},
    ],
}

CHAPTERS = [
    {
        "k": "sitting-tight",
        "n": "Sitting tight",
        "w": "Being right was never the hard part",
        "src": "Reminiscences of a Stock Operator, chapter 5",
        "dek": "A speculator famous for speed put the credit somewhere "
               "unexpected. The chapter explains why sitting is harder than "
               "being right.",
        "story":
            "His own summary is not what anyone expects from him. It never "
            "was his thinking that made the big money, he says; it was his "
            "sitting. He had watched the alternative all his life: men who "
            "saw the move coming and made nothing from it, shaken out by "
            "every pullback or cashing a small gain early. ==Men who can both "
            "be right and sit tight are uncommon, he concludes, and that is "
            "the whole difficulty.== The hard part is not the analysis. It is "
            "that every day of sitting is a day of refusing to act.",
        "f": [
            {"n": "The money lives in the back half of the hold",
             "d": "A large move does not pay out evenly. The early stretch is "
                  "the choppiest and the most testing; the compounding "
                  "happens later. Getting off partway takes the "
                  "uncomfortable section and hands over the valuable one, "
                  "which is how people are right about direction and collect "
                  "almost nothing.",
             "eg": "Eight months into the direction you chose, nothing has "
                   "moved, so you switch. It works in month fourteen and your "
                   "successor collects the degree you paid for."},
            {"n": "Not moving is an action that needs defending",
             "d": "Sitting is not the easy option; it is continuous "
                  "resistance. The news, the swings and every friend's better "
                  "idea all argue for a change. So it needs fortification: "
                  "write the original thesis and the conditions that would "
                  "falsify it, and permit movement only when one of those "
                  "trips.",
             "eg": "Set a hard rule for the long position: look once a "
                   "quarter, and only against the three reasons you wrote at "
                   "the start. Red or green is not a reason."},
            {"n": "Sitting only protects a judgement that is right",
             "d": "The sentence says right and sitting tight, and the two "
                  "conditions are joined by an and. Using it to keep a broken "
                  "position alive is the expensive misreading. Patience and "
                  "stubbornness look identical from outside; the only test is "
                  "whether the written thesis still stands.",
             "eg": "Two of the three reasons you bought have already failed "
                   "and you are still holding on. That is not sitting tight. "
                   "That is refusing to be wrong."},
        ],
        "q": [
            "It never was my thinking that made the big money for me.",
            "It always was my sitting. Got that? My sitting tight!",
            "Men who can both be right and sit tight are uncommon.",
        ],
        "apply":
            "Where you are: the direction looks right and the wobbles are "
            "making your hands itch.\n"
            "Ask first: has the thesis I wrote at the start actually broken? "
            "If not, is this urge coming from evidence or from discomfort?\n"
            "Where it goes wrong: applying it to a position already "
            "falsified, or never writing a falsifier at all, so holding on "
            "becomes not looking.",
    },
    {
        "k": "hope-and-fear-inverted",
        "n": "Hope and fear, the wrong way round",
        "w": "The instinct points in the wrong direction",
        "src": "Reminiscences of a Stock Operator, chapter 10",
        "dek": "Four fortunes and several bankruptcies, distilled into one "
               "rule about two emotions pointing the wrong way.",
        "story":
            "He traced his losses to a single inversion. When the position "
            "goes against a man he hopes, waiting for it to come back, and "
            "the loss grows. When it goes his way he becomes afraid of losing "
            "the profit, so he takes it early. His rule swaps them outright. "
            "==Instead of hoping he must fear; instead of fearing he must "
            "hope.== Fear the small loss becoming a large one and cut. Hope "
            "the small gain becomes a large one and hold. And he adds why it "
            "never stops working: speculation is as old as the hills, because "
            "people are not new.",
        "f": [
            {"n": "The instinct runs exactly backwards",
             "d": "Hoping over a loss and fearing over a gain is not a "
                  "character flaw; it is the factory setting for humans "
                  "facing gains and losses. Losses make people gamble and "
                  "gains make people lock in. So the inversion cannot be run "
                  "on reminders. It has to be run by mechanism.",
             "eg": "Automate the exit on the downside and use a trailing stop "
                   "instead of a manual sale on the upside. In the moment you "
                   "will always side with the instinct."},
            {"n": "Cut fast, because a loss accrues interest",
             "d": "Hope applied to a loss compounds. Every extra day adds "
                  "sunk cost, makes the admission harder, and raises the "
                  "stake required to get back to level. That is where the "
                  "fear belongs: not fear of this loss, but of the version "
                  "that starts dictating every later decision.",
             "eg": "Every month you extend the project that is missing its "
                   "numbers, killing it gets harder: more spent, more "
                   "promised, nobody willing to say it. The first cut is "
                   "cheapest."},
            {"n": "The rule does not excuse you from the work",
             "d": "Cutting losses and running winners assumes you can say "
                  "what counts as going against you. Without a thesis set in "
                  "advance, the inversion degrades into buying strength and "
                  "selling weakness. His own ruin came in the stretches when "
                  "he broke his rules, and a rule cannot save the man who "
                  "suspends it.",
             "eg": "Cut it when it drops, applied by someone with no entry "
                   "thesis, means being stopped out by every ordinary "
                   "fluctuation. Discipline cannot stand in for judgement."},
        ],
        "q": [
            "Instead of hoping he must fear; instead of fearing he must hope.",
            "He must fear that his loss may develop into a much bigger loss.",
            "There is nothing new in Wall Street. Speculation is as old as the "
            "hills.",
        ],
        "apply":
            "Where you are: one position is losing and you want to wait, "
            "another is winning and you want to bank it.\n"
            "Ask first: which emotion is speaking in each case, and does the "
            "rule say to swap them?\n"
            "Where it goes wrong: running it as blind momentum chasing, or "
            "knowing the rule and granting yourself exceptions, which is "
            "exactly how he went broke.",
    },
]

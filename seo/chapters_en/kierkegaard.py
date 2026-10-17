# -*- coding: utf-8 -*-
"""Søren Kierkegaard — English.

English readers arrive with the label "father of existentialism" and a
suspicion that he is gloomy. This page does the plainer thing: it takes one
aphorism from Either/Or (1843) and one journal entry from the same year and
puts them on a reader holding two options, or waiting to understand first.

Only phrases that are the same in every translation are quoted (you will regret
it either way; understood backwards; lived forwards). Everything else is our
wording. His theology is not what we draw on here.
"""

PARENT = {
    "name": "Søren Kierkegaard",
    "slug": "kierkegaard",
    "blurb": "Deep read",
    "items": [
        {"k": "regret-either-way", "n": "Regret Comes Either Way",
         "w": "You cannot choose by regret, because it turns up whichever you pick",
         "ready": True,
         "line": "Marry and you will regret it, do not marry and you will regret that too: the question is taken from both sides at once"},
        {"k": "lived-forwards", "n": "Waiting Until You Understand",
         "w": "Life is understood looking back, but it can only be lived looking ahead",
         "ready": True,
         "line": "He wrote in his journal that people forget the other half: life has to be lived forwards"},
    ],
}

CHAPTERS = [
    {
        "k": "regret-either-way", "n": "Regret Comes Either Way",
        "w": "You cannot choose by regret, because it turns up whichever you pick",
        "src": "Either/Or (1843), Part One, 'Diapsalmata'; only the phrase common to the translations is quoted, the rest is our wording",
        "dek": "You want both and dread regretting the one you give up. Kierkegaard asks whether \"will I regret it?\" can decide anything.",
        "story":
            "In 1843 Kierkegaard published Either/Or under an editor's "
            "invented name. Part One opens with scattered sayings by a young "
            "man who believes he has seen through everything. One runs: marry "
            "and you will regret it, do not marry and you will regret that "
            "too, and whether you marry or not, \"you will regret it either "
            "way\". The same pattern is then run on laughing at the world's "
            "follies and on weeping over them. ==The joke is that the "
            "question \"will I regret it?\" has been taken away from both "
            "sides at once.==",
        "f": [
            {"n": "Regret comes from both sides",
             "d": "Whichever you pick, you will find reasons to wish you had picked the other. So \"will I regret it?\" cannot tell the two apart. It does not measure which is better; it measures how afraid you are.",
             "eg": "Two job offers: take the first and you miss the pay of the second; take the second and you miss the colleagues of the first."},
            {"n": "Fearing regret is asking for a guarantee",
             "d": "Choosing by what you will not regret is asking for insurance before you act, and nobody sells it. What you can ask beforehand is different: which one am I willing to answer for, and can I really live without the other?",
             "eg": "You rent the south-facing flat and it is noisy; you rent the quiet one and it is dark. The question is which you can stand, not which has no fault."},
            {"n": "He does not choose for you",
             "d": "Even the title gives no answer; Either/Or only sets both ends side by side. The judge who writes Part Two says, roughly, that what matters is not only which you pick but the seriousness with which you pick it. A choice starts to count once it is made.",
             "eg": "Once you decide, put away the file on the other option instead of opening it every night."},
        ],
        "q": [
            "Regret comes from both sides; it cannot rank them.",
            "Fearing regret is wanting a guarantee before you act.",
            "A choice starts to count once it is made.",
        ],
        "apply":
            "Where you are: You want both, you have compared them for weeks, and every comparison ends at \"I will regret either one\".\n"
            "Ask first: With \"afraid of regret\" crossed out, which one am I more willing to answer for? Write it down, and once you pick, act.\n"
            "Where it goes wrong: Using it to say the two are the same and you may as well toss a coin. He does not say they are equal. He says regret cannot rank them, so rank them by what each costs you in money, time and what you give up.",
    },
    {
        "k": "lived-forwards", "n": "Waiting Until You Understand",
        "w": "Life is understood looking back, but it can only be lived looking ahead",
        "src": "Journals, entry IV A 164 (1843); only the phrases common to the translations are quoted, the rest is our wording",
        "dek": "You want to understand it fully before you choose. Kierkegaard asks why that moment never arrives.",
        "story":
            "In 1843 Kierkegaard noted in his journal that philosophy is "
            "right to say life must be \"understood backwards\". But, he "
            "added, people forget the other proposition: that it must be "
            "\"lived forwards\". The entry is only a few lines long. "
            "==You have to decide while you still cannot see, because seeing "
            "clearly comes after the doing.== Which means \"I will decide "
            "when I have thought it through\" is itself a decision.",
        "f": [
            {"n": "Two ways of reading, each half the job",
             "d": "Looking back, events join up, so \"the signs were obvious\" feels like plain fact. The person looking ahead has no such line, only a scatter of points that have not yet joined.",
             "eg": "At the interview you cannot tell which firm will fold; three years later colleagues say there were signs."},
            {"n": "Waiting for a moment that does not come",
             "d": "The moment when things are clear always sits after the doing. Someone who keeps waiting is not getting clearer; they are handing the decision to time, and what time picks for you is often \"not chosen\".",
             "eg": "The career change you put off for two years: others in your field have made it work or hit a wall, and you have learned nothing from either."},
            {"n": "Move, and keep reading backwards",
             "d": "He does not say stop thinking. He wants both: take a step on the part you already understand, then look back over it, and only then is there something to read for the next step.",
             "eg": "Try it for three months, and on the last day write one page: what I only understand now."},
        ],
        "q": [
            "Looking back makes sense of it; only going forward gets you there.",
            "Seeing clearly comes after the doing.",
            "Waiting is letting time choose for you.",
        ],
        "apply":
            "Where you are: You have thought about it for a long time and feel a little more clarity would settle it.\n"
            "Ask first: Is the information I still lack something I can look up, or something I can only learn by going? Look up the first within three days; for the second, pick a direction you can undo and take one step.\n"
            "Where it goes wrong: Using it to say stop thinking and just jump. He means thinking and going take turns, not that going replaces thinking.",
    },
]

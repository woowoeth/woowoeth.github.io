# -*- coding: utf-8 -*-
"""Jim Simons — English.

The English reader knows the number — the best long-run record anyone has —
and expects the page to be about mathematics. It is not. Both chapters are
about where human judgement is allowed to stand: out of the trade and inside
the model, and, in the second, on the people you hire and the taste you have
built up.
"""

PARENT = {
    "name": "Jim Simons",
    "slug": "simons",
    "blurb": "Deep read",
    "items": [
        {"k": "slave-to-the-model", "n": "Slaves to the model",
         "w": "Discipline handed to the system", "ready": True,
         "line": "People change the model, never the individual decision"},
        {"k": "simons-principles", "n": "Beauty, and the best people",
         "w": "He published his own principles", "ready": True,
         "line": "Five principles, and not one of them is about mathematics"},
    ],
}

CHAPTERS = [
    {
        "k": "slave-to-the-model",
        "n": "Slaves to the model",
        "w": "Discipline handed to the system",
        "src": "Simons in public interviews, on how Medallion is run",
        "dek": "The best-returning fund on record forbids its brilliant "
               "people from improvising. This piece asks who that rule is "
               "actually protecting against.",
        "story":
            "Medallion has compounded at better than thirty-nine per cent a "
            "year after fees for decades, and Simons described the method in "
            "one rule. ==If you're going to trade using models, you just "
            "slavishly use the models; you do whatever the hell it says, no "
            "matter how smart or dumb you think it is.== The reason is "
            "mechanical. Allow one override and you can never again say "
            "whether a loss belonged to the model or to the person, so the "
            "system stops improving. And the urge to override peaks exactly "
            "when the model most needs leaving alone.",
        "f": [
            {"n": "One override and attribution is dead",
             "d": "Improvement depends on clean attribution: was this loss "
                  "the model or the execution? The moment a person "
                  "intervenes the two are inseparable, every loss can be "
                  "blamed on the other party, and nothing gets changed. The "
                  "rule's real job is protecting traceability.",
             "eg": "Operations tweaked the agreed campaign parameters three "
                   "times. At the quarterly review nobody could say whether "
                   "the strategy or the tweaking produced the result, so the "
                   "quarter taught nothing."},
            {"n": "Write the rule when calm, run it when frightened",
             "d": "The urge to intervene scales with how extreme things get, "
                  "and extreme is precisely when the system most needs to be "
                  "trusted. So the authority has to be fixed in advance: what "
                  "lets a person touch it — a code error, corrupted data — "
                  "and what never does.",
             "eg": "Put the three conditions that permit manual intervention "
                   "on the wall in writing. On the day it crashes, check the "
                   "list. Fear is not on the list."},
            {"n": "People move out of execution and into improvement",
             "d": "This division of labour is not an insult to judgement, it "
                  "is a promotion for it. Instead of a thousand decisions "
                  "taken while emotional, you make one change to the model "
                  "that alters a thousand decisions. The leverage sits in the "
                  "system, not in the seat.",
             "eg": "Reviewing a hundred tickets a day by hand consumes "
                   "judgement. Spending a week turning that review into a "
                   "written rule copies it instead."},
        ],
        "q": [
            "Slavishly use the model, however smart or dumb it looks today.",
            "Override it once and you never learn what actually failed.",
            "We do not overrule the model. We improve the model.",
        ],
        "apply":
            "Where you are: the system's answer conflicts with your instinct "
            "right now, and you want to override it just this once.\n"
            "Ask first: am I changing this decision or the model? Can the "
            "reason I would override be written as a rule that applies every "
            "time from now on?\n"
            "Where it goes wrong: turning follow the model into never "
            "servicing the model, so a bad rule runs forever; or applying the "
            "discipline to everyone except yourself.",
    },
    {
        "k": "simons-principles",
        "n": "Beauty, and the best people",
        "w": "He published his own principles",
        "src": "Simons, Mathematics, Common Sense and Good Luck, MIT 2010",
        "dek": "A man who made his fortune out of algorithms summed up a "
               "career in five principles. Not one of them is about "
               "mathematics.",
        "story":
            "In 2010 Simons went back to MIT and compressed a career into a "
            "short list. Work with the smartest people you can find, ideally "
            "smarter than you are. ==Be guided by beauty== — he said it "
            "applies not only to theorems but to a company that runs well or "
            "a problem solved elegantly, and that following it rarely goes "
            "wrong. Don't give up easily: the paper he wrote with Chern took "
            "years. And the last one he refused to dress up. Hope for good "
            "luck. The room laughed. He said he meant it.",
        "f": [
            {"n": "Hiring above yourself is a rule, not a pose",
             "d": "The first teams he built after leaving academia were "
                  "mathematicians, astronomers and speech-recognition "
                  "scientists, none of whom knew finance. He was betting on "
                  "raw problem-solving power, not domain experience. The rule "
                  "has a hard test: if you are always the sharpest person "
                  "present, you are not following it.",
             "eg": "Ask of every hire whether there is a part of the job they "
                   "are visibly better at than you. A year of hires with "
                   "nobody intimidating in it means the bar has slipped."},
            {"n": "Beauty is compressed experience",
             "d": "Be guided by beauty sounds mystical and works as a fast "
                  "classifier. After years in a field, a solution that is "
                  "spare and well-jointed registers as beautiful, and one "
                  "patched on top of patches registers as wrong, before the "
                  "argument is finished. The signal is not proof. It says "
                  "where to dig.",
             "eg": "Two architectures both work. One feels right to the old "
                   "engineer, the other feels off and he cannot say why. Dig "
                   "into the second one first."},
            {"n": "Putting luck on the list is honest and also strategic",
             "d": "Admitting how much was luck stops you filing a random "
                  "success under personal genius. The outward consequence is "
                  "that if luck matters you should enlarge the surface you "
                  "expose to it: more attempts, more years still in the game, "
                  "more time near well-informed people.",
             "eg": "Give every success post-mortem a column for tailwinds you "
                   "did not control. Teams that can fill it in do not despair "
                   "the first time the wind turns."},
        ],
        "q": [
            "Be guided by beauty.",
            "Work with the smartest people you can find, ideally smarter than "
            "you.",
            "Don't give up easily, and hope for some good luck.",
        ],
        "apply":
            "Where you are: you are writing down your own method and the list "
            "is all technique.\n"
            "Ask first: do people, taste and luck appear anywhere on it? When "
            "did I last work beside somebody clearly better than me?\n"
            "Where it goes wrong: using beauty to veto anything unfamiliar; "
            "or using luck matters as cover for not having done the work.",
    },
]

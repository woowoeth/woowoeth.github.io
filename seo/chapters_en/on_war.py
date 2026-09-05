# -*- coding: utf-8 -*-
"""On War — English.

The English reader knows one sentence from this book and usually reads it as
cynicism: war is politics by other means. It is the opposite of cynicism. It
is a restraining clause, and the other idea worth having, friction, is the
reason the book is still read by people who will never command anything.
Quotations follow the standard English translations of the German.
"""

PARENT = {
    "name": "On War",
    "slug": "on-war",
    "blurb": "Deep read",
    "items": [
        {"k": "continuation-of-politics", "n": "The continuation of policy",
         "w": "You fight in order to settle", "ready": True,
         "line": "A war that forgets why it began is not won by being won"},
        {"k": "friction", "n": "Friction",
         "w": "Even the simplest thing is difficult", "ready": True,
         "line": "Between the plan on paper and the soaked column lies friction"},
    ],
}

CHAPTERS = [
    {
        "k": "continuation-of-politics",
        "n": "The continuation of policy",
        "w": "You fight in order to settle",
        "src": "On War, Book One, Chapter One",
        "dek": "The most famous line in the book gets read as a cynical "
               "observation. It is in fact a restraining clause.",
        "story":
            "Clausewitz defines war on two levels. First its nature: an act "
            "of force to compel the enemy to do our will, and force left to "
            "its own logic escalates without limit. Then the rein: ==war is "
            "merely the continuation of policy by other means.== The second "
            "statement exists to bind the first. War is not a thing standing "
            "on its own. It is begun by a political purpose and serves one. "
            "The political object is the goal, war is the means, and the "
            "means can never be considered apart from the goal. He spent his "
            "life warning soldiers that the longer a war runs, the easier "
            "this is to forget.",
        "f": [
            {"n": "A means left alone starts eating the end",
             "d": "War has an internal logic, win this one and then the next, "
                  "and once running it powers itself until the fighting is "
                  "the point. Every strong instrument behaves this way: price "
                  "wars, litigation, public campaigns. They demand "
                  "continuation once started, so the rein goes on at the "
                  "beginning or not at all.",
             "eg": "A price war opened to force them to the table becomes, by "
                   "the third month, a matter of not losing face. Nobody "
                   "remembers the table."},
            {"n": "Audit every step against the purpose",
             "d": "The working version of the means never being separable "
                  "from the goal: each move has to answer whether it brings "
                  "the political outcome nearer. Taking a city that makes the "
                  "negotiation harder is a military success and a net loss. "
                  "The test is the purpose, not the spoils.",
             "eg": "You won the case and wrecked your standing in the "
                   "industry. You took the share and taught them your whole "
                   "method. Re-audit each move against the original aim."},
            {"n": "When the aim changes, resize the means",
             "d": "The political object determines the effort and the scale "
                  "it warrants, so limited aims call for a limited war. Aims "
                  "shifting mid-course is ordinary. The danger is the scale "
                  "of the means not being reset with them, a small aim "
                  "carrying a large war, or the reverse.",
             "eg": "A project meant only to test a market rolls on under its "
                   "own momentum until the scale no longer matches the word "
                   "test. Resize it, or admit the aim changed."},
        ],
        "q": [
            "War is merely the continuation of policy by other means.",
            "The political object is the goal, war is the means.",
            "War is an act of force to compel the enemy to do our will.",
        ],
        "apply":
            "Where you are: a contest has been running a long time and each "
            "round is fiercer than the last.\n"
            "Ask first: what was this opened for, and is the next step still "
            "bringing that outcome nearer?\n"
            "Where it goes wrong: letting the means take over the end and "
            "fighting for its own sake; or using everything serves the big "
            "goal to license any escalation, which turns the rein into a "
            "whip.",
    },
    {
        "k": "friction",
        "n": "Friction",
        "w": "Even the simplest thing is difficult",
        "src": "On War, Book One, Chapter Seven",
        "dek": "He borrowed a word from physics for the study of war. This is "
               "where friction comes from and why it can only be budgeted "
               "for.",
        "story":
            "In the seventh chapter he coins it: ==everything in war is very "
            "simple, but the simplest thing is difficult.== The difficulties "
            "accumulate and produce a friction that nobody who has not seen "
            "war can imagine. His picture of it is concrete. The machine is "
            "made of individuals, each of whom keeps his own friction: an "
            "order passes through hundreds of people who get tired, "
            "frightened, or misunderstand it, and on top of that come "
            "weather, ground and false reports. Friction makes what looks "
            "easy hard. It is, he says, the one concept that distinguishes "
            "real war from war on paper.",
        "f": [
            {"n": "Friction comes from a plan having to pass through people",
             "d": "A plan is a frictionless abstraction; execution is "
                  "warm-blooded transmission, and each person it crosses adds "
                  "a layer of fatigue, misreading, self-interest and delay. "
                  "So the complexity of a plan is not counted in logical "
                  "steps but in how many people it must pass through.",
             "eg": "A three-step process spanning five teams is harder than a "
                   "ten-step one closed inside a single group. Count handoffs "
                   "before you count steps."},
            {"n": "Friction cannot be removed, only allowed for",
             "d": "He does not teach you to eliminate it, because it cannot "
                  "be eliminated. He teaches conversion. The good commander "
                  "prices friction into the plan and leaves slack at every "
                  "link. Scheduling to the theoretical limit is not "
                  "efficiency; it is never having been in the field.",
             "eg": "A timeline summed from each stage's best case declares "
                   "that one head cold gives the whole line a fever. Old "
                   "hands plan at eighty per cent and call the rest "
                   "friction."},
            {"n": "What resists friction is habit, not willpower",
             "d": "The only lubricant, he says, is the habit of war: drill "
                  "and combat grinding a force until difficulty is the "
                  "default. Willpower in the moment does not hold against "
                  "systematic friction. Only rehearsing the common failures "
                  "into muscle keeps friction from eating your decisions.",
             "eg": "The teams that hold up are not the ones with high morale. "
                   "They are the ones that have rehearsed a rollback, run a "
                   "degraded mode and sat through a night shift."},
        ],
        "q": [
            "Everything in war is very simple, but the simplest thing is "
            "difficult.",
            "Friction is what distinguishes real war from war on paper.",
            "Three quarters of the factors in war lie in a fog.",
        ],
        "apply":
            "Where you are: a plan that is simple on paper, and you are about "
            "to schedule it along the ideal path.\n"
            "Ask first: how many people does it have to pass through, and "
            "where exactly did I leave slack?\n"
            "Where it goes wrong: treating friction as an excuse and refusing "
            "every claim of it; or using it to excuse all delay while never "
            "drilling the habit that absorbs it.",
    },
]

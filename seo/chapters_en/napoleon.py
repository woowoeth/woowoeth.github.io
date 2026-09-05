# -*- coding: utf-8 -*-
"""Napoleon — English.

Every English reader already has a Napoleon: the short man, the hand in the
coat, Waterloo. None of that is any use. The two things worth taking from him
are an arithmetic trick that let a smaller army be the larger one at every
point of contact, and the campaign that showed what happens when a bet of that
size has no exit written into it.
"""

PARENT = {
    "name": "Napoleon",
    "slug": "napoleon",
    "blurb": "Deep read",
    "items": [
        {"k": "decisive-point", "n": "More men where it is decided",
         "w": "Being outnumbered overall is fine", "ready": True,
         "line": "Outnumbered on the ledger, stronger everywhere they actually met"},
        {"k": "sublime-to-ridiculous", "n": "One step from the sublime",
         "w": "A success with no exit condition", "ready": True,
         "line": "He said it on the road back from Moscow, more than once"},
    ],
}

CHAPTERS = [
    {
        "k": "decisive-point",
        "n": "More men where it is decided",
        "w": "Being outnumbered overall is fine",
        "src": "Maxims of War",
        "dek": "He usually fought with fewer men and was usually the stronger "
               "side at the moment of contact. This is how.",
        "story":
            "One of his maxims holds the whole method: ==the art of war "
            "consists in always having more force than the enemy at the point "
            "attacked or defended, even when the army as a whole is "
            "weaker.== The Italian campaign of 1796 is the textbook case. He "
            "had a little over thirty thousand men against nearly seventy "
            "thousand Austrians and Piedmontese, but they came in separate "
            "columns, and he used his interior position to move between them "
            "and meet each part with everything he had. On the ledger he was "
            "the weaker side. At every place they actually met, he was the "
            "stronger one.",
        "f": [
            {"n": "A shortfall in total can be traded away by movement",
             "d": "Resource comparisons are a summary table; outcomes happen "
                  "at particular points of contact. The smaller side can "
                  "still be larger at each point, and the price is moving "
                  "faster than the other side and giving up the idea of "
                  "holding everything at once.",
             "eg": "A small team cannot compete across a market and can "
                   "outspend a large company inside one account. At that "
                   "point you are the big company."},
            {"n": "Their dispersal is something you can cause",
             "d": "The allied columns were not only careless. His line of "
                  "march threatened several objectives at once and forced "
                  "them to garrison each. Making the other side afraid to "
                  "leave anything uncovered is the same act as making him too "
                  "weak everywhere. Splitting him and massing yourself are "
                  "one movement.",
             "eg": "Put visible probes into three directions and their "
                   "defensive budget divides three ways. You mean to attack "
                   "one; they have to hold all of it."},
            {"n": "The method runs on a time difference",
             "d": "Beating two forces in turn requires that finishing the "
                  "first and turning on the second is faster than the two "
                  "joining. Slow the movement down with longer supply or more "
                  "layers of approval and the interior position inverts into "
                  "encirclement. That is how it later failed in his own "
                  "hands.",
             "eg": "Any strategy living off a timing gap loses a beat for "
                   "every layer the organisation adds. The old lightning "
                   "method, run through a long chain, walks into the trap."},
        ],
        "q": [
            "Have more force at the point attacked, even when weaker overall.",
            "Splitting him and massing yourself are the same movement.",
            "In war, the moral is to the physical as three to one.",
        ],
        "apply":
            "Where you are: your total resources are plainly smaller than "
            "theirs.\n"
            "Ask first: at which few points is this actually decided, and can "
            "I be the larger side at one of them?\n"
            "Where it goes wrong: turning concentration into one throw you "
            "cannot survive losing; and running a timing-gap method after the "
            "organisation has slowed down.",
    },
    {
        "k": "sublime-to-ridiculous",
        "n": "One step from the sublime",
        "w": "A success with no exit condition",
        "src": "De Pradt, on words spoken at Warsaw in December 1812",
        "dek": "The witticism has an origin that is not witty at all. This is "
               "about the road he was on when he said it.",
        "story":
            "In December 1812 he left what remained of his army in the "
            "Russian snow and went back to Paris by sleigh. Passing through "
            "Warsaw he said it to the ambassador de Pradt, more than once: "
            "==from the sublime to the ridiculous there is only one step.== "
            "Six months earlier he had crossed the Niemen with over six "
            "hundred thousand men, and fewer than a tenth came back. He lost "
            "no major battle on that campaign. He entered Moscow. He lost the "
            "war for having no plan at all for winning while the other side "
            "refuses to concede. Moscow was empty, the Tsar would not "
            "negotiate, winter arrived.",
        "f": [
            {"n": "You can win every battle and lose the war",
             "d": "His script assumed that holding Moscow was victory, but "
                  "the definition of victory sat with the other side. They "
                  "declined, and the occupation became merely a long way in. "
                  "Any victory condition that requires your opponent's "
                  "cooperation is not a condition you control.",
             "eg": "Winning the price war and taking the share assumes they "
                   "withdraw. If a parent company keeps funding them, every "
                   "round you win deepens your own drain."},
            {"n": "Write the way home before you leave",
             "d": "A supply line two thousand li long for six hundred "
                  "thousand men only works inside a quick-victory script. He "
                  "set no automatic stop for a war still running in October. "
                  "Every large bet needs an exit that does not depend on "
                  "judgement, because by then judgement is the thing most "
                  "heavily committed.",
             "eg": "Before entering a market, write down the date and the "
                   "number at which you withdraw. Write it while clear, "
                   "because later one more push will feel obvious."},
            {"n": "There is no buffer between sublime and ridiculous",
             "d": "The exact word is step. Collapse was not gradual. "
                  "Authority built on continuous victory cannot structurally "
                  "survive one large defeat: the loyalty of the client "
                  "states, the mood of the army and the politics of Paris "
                  "were all premised on his being unbeatable.",
             "eg": "A person or a team sold on never missing falls hardest "
                   "the first time they publicly miss. Keeping a visible "
                   "record of failures is what makes a fall survivable."},
        ],
        "q": [
            "From the sublime to the ridiculous there is only one step.",
            "A victory condition that needs their agreement is not yours.",
            "Write the exit while you are still clear-headed.",
        ],
        "apply":
            "Where you are: an operation far bigger than anything you have "
            "run, and the early stretch has gone well.\n"
            "Ask first: does my victory condition need them to cooperate, and "
            "is my stop a fixed date or a we will see?\n"
            "Where it goes wrong: reading never having lost as cannot lose; "
            "and using the good start to add investment until the resources "
            "for the way home are committed too.",
    },
]

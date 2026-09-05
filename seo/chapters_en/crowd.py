# -*- coding: utf-8 -*-
"""The Crowd — English.

The English reader tends to arrive with the book already labelled: an 1895
Frenchman being rude about the masses, quoted mostly by people who think they
are not in a crowd. What the page keeps is the part that is still testable —
three mechanisms and three verbs — and it keeps the reader inside the crowd
rather than above it, which is where Le Bon's own defence has to be used.
"""

PARENT = {
    "name": "The Crowd",
    "slug": "crowd",
    "blurb": "Deep read",
    "items": [
        {"k": "descent-in-crowds", "n": "The person who walks into a crowd",
         "w": "The steps all go downward", "ready": True,
         "line": "A group of clever people can do what none of them would do alone"},
        {"k": "assert-repeat-contaminate", "n": "Affirm, repeat, infect",
         "w": "The three moves that persuade a crowd", "ready": True,
         "line": "What works on a crowd was never the argument"},
    ],
}

CHAPTERS = [
    {
        "k": "descent-in-crowds",
        "n": "The person who walks into a crowd",
        "w": "The steps all go downward",
        "src": "The Crowd, Book One",
        "dek": "Why do decent people in a group do things none of them would "
               "do alone? Le Bon lays out three steps down.",
        "story":
            "Le Bon's central observation is that a person inside a crowd "
            "switches to a different operating system. What accumulates in a "
            "crowd, he writes, is stupidity and not mother wit, because a "
            "group can only meet on what its members share, and what they "
            "share is instinct rather than expertise. He names three "
            "mechanisms: numbers dissolve personal responsibility, feeling "
            "spreads like an infection, and continuous suggestion produces "
            "something close to hypnosis. Three steps down, and ==isolated, "
            "he may be a cultivated individual; in a crowd, he is a "
            "barbarian==.",
        "f": [
            {"n": "A crowd meets at the lowest shared layer",
             "d": "Ten specialists in a room hold expertise that does not add "
                  "up, because almost none of it overlaps. What does overlap "
                  "is emotion, instinct and group identity, so the level of "
                  "the discussion drifts downward unless a structure draws "
                  "each person's expertise out separately.",
             "eg": "Ten executives talking freely often produce less than two "
                   "of them talking properly, unless the chair goes round "
                   "taking one judgement per field."},
            {"n": "Anonymity sets the level of responsibility",
             "d": "The modern form of safety in numbers is that the harder a "
                  "person's contribution is to identify, the looser the "
                  "restraint. This is not moral decay, it is a structural "
                  "variable: the same people give different opinions in a "
                  "signed review and an anonymous poll.",
             "eg": "The people piling on in a group chat are reasonable in a "
                   "direct message. For opinions someone owns, put a name on "
                   "every one."},
            {"n": "Do not decide while the crowd is still in the room",
             "d": "The observation converts into a rule: crowds are good for "
                  "mobilising and bad for deciding. The rally, the "
                  "celebration dinner and the crisis room are the moments of "
                  "highest energy and lowest judgement. Move the decision to "
                  "after everyone has gone home.",
             "eg": "Money committed on stage at a launch, expansion promised "
                   "over dinner. Sleep on anything large and let the crowd "
                   "state drain out first."},
        ],
        "q": [
            "In crowds it is stupidity and not mother wit that is "
            "accumulated.",
            "Isolated, he may be a cultivated individual; in a crowd, he is a "
            "barbarian.",
            "A crowd is quick to act and slow to reason.",
        ],
        "apply":
            "Where you are: a room full of capable people, and the "
            "conclusions keep getting cruder.\n"
            "Ask first: are we speaking from our separate expertise, or "
            "resonating on a shared feeling?\n"
            "Where it goes wrong: blaming the members for what the structure "
            "did; or swinging the other way into one-man rule and cancelling "
            "the occasions where a crowd is the right instrument.",
    },
    {
        "k": "assert-repeat-contaminate",
        "n": "Affirm, repeat, infect",
        "w": "The three moves that persuade a crowd",
        "src": "The Crowd, Book Two",
        "dek": "He reduced the demagogue's method to three verbs. This is why "
               "the recipe works, and what defence is left.",
        "story":
            "In his second book Le Bon compresses the means of persuading a "
            "crowd into three words. First affirmation: a plain assertion, "
            "free of all reasoning and all proof, is among the surest ways to "
            "get an idea into the mind of a crowd. Second repetition: the "
            "thing affirmed comes by repetition to fix itself in the mind, "
            "until people forget the source and take it for their own "
            "conclusion. Third contagion: ==in a crowd every sentiment and act "
            "is contagious==. On proof he is just as clear. It is not what "
            "moves a crowd.",
        "f": [
            {"n": "An assertion spares the listener the thinking",
             "d": "An argued claim asks the listener to pay a cost in "
                  "attention. A bare assertion asks nothing at all. It hands "
                  "over the conclusion, and the shorter it is the more it "
                  "sounds like truth. So careful phrasing loses to blunt "
                  "phrasing by default.",
             "eg": "That direction will never work does more damage in a "
                   "meeting than a page of analysis. The reflex on hearing it "
                   "should be to ask what it rests on."},
            {"n": "Repetition impersonates consensus",
             "d": "A sentence heard for the fifth time is processed more "
                  "easily, and the ease gets misread as soundness. Repetition "
                  "also manufactures the impression that many people are "
                  "saying it, when one person may have said it many times. "
                  "The counter is to trace it.",
             "eg": "Everyone says that company is finished. Follow it back "
                   "and every version turns out to come from the same "
                   "article. Volume is not sources."},
            {"n": "The recipe itself is neutral",
             "d": "Nothing in the mechanism picks sides, and public health "
                  "campaigns run on affirmation and repetition too. The line "
                  "falls on whether a way to check is left open. Repetition "
                  "that keeps sources and objections reachable is teaching. "
                  "Repetition that seals them is handling.",
             "eg": "Push a new internal standard with a short slogan and high "
                   "frequency, but publish the data and a route for "
                   "objections alongside it."},
        ],
        "q": [
            "Affirmation pure and simple, kept free of all reasoning and all "
            "proof.",
            "The thing affirmed comes by repetition to fix itself in the "
            "mind.",
            "In a crowd every sentiment and act is contagious.",
        ],
        "apply":
            "Where you are: a claim you keep hearing has started to feel "
            "true.\n"
            "Ask first: where did it first come from, and apart from the "
            "number of repetitions, have you seen one independent piece of "
            "evidence?\n"
            "Where it goes wrong: spotting the recipe and accusing everyone "
            "of manipulation; or using the recipe yourself while quietly "
            "removing the way to check.",
    },
]

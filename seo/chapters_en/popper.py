# -*- coding: utf-8 -*-
"""Karl Popper — English.

Falsifiable has become a word people reach for to win arguments, and black
swan now belongs to somebody else's book jacket. Both were narrower and more
demanding than the versions in circulation. These two pages put the criterion
back where Popper left it: not a way of dismissing what you dislike, but a
standing obligation to say in advance what would make you drop your own view.
"""

PARENT = {
    "name": "Karl Popper",
    "slug": "popper",
    "blurb": "Deep read",
    "items": [
        {"k": "falsifiability", "n": "Can it be shown wrong",
         "w": "A theory that explains everything explains nothing",
         "ready": True,
         "line": "Say in advance what would make you admit you were wrong"},
        {"k": "seek-refutation", "n": "Go looking for the counter-example",
         "w": "One black swan beats a hundred white ones", "ready": True,
         "line": "No pile of confirming instances can establish the rule"},
    ],
}

CHAPTERS = [
    {
        "k": "falsifiability",
        "n": "Can it be shown wrong",
        "w": "A theory that explains everything explains nothing",
        "src": "Conjectures and Refutations",
        "dek": "Astrology explains events and so does physics. This page is "
               "about the line Popper drew between them.",
        "story":
            "As a teenager in Vienna he was reading Einstein alongside the "
            "theories then in fashion, whose followers could account for any "
            "case at all and treated that as proof of strength. General "
            "relativity did the opposite. It predicted that starlight passing "
            "the sun would bend by a specific amount, and a different "
            "measurement would have finished it. The 1919 eclipse matched. "
            "==A theory which is not refutable by any conceivable event is "
            "non-scientific,== he concluded, and irrefutability is a vice "
            "rather than a virtue. The difference was never explanatory "
            "power.",
        "f": [
            {"n": "Ask what would refute it, not what supports it",
             "d": "Facing any claim, the useful question is not what evidence "
                  "there is but what observation would make you drop it. If "
                  "nothing would, the claim carries no testable content, and "
                  "being internally consistent does not make up for that.",
             "eg": "Market sentiment drove the rise. And the fall? Also "
                   "sentiment. It covers every outcome, which is exactly why "
                   "it tells you nothing."},
            {"n": "The refuting condition has to be written down first",
             "d": "People are extremely good at reading any result as "
                  "support. The only reliable antidote is to nail the "
                  "criterion in place before the result arrives. Setting the "
                  "standard afterwards leaves you a position that cannot "
                  "lose, which is the same as one that cannot inform.",
             "eg": "Before launch, write down that if this number has not "
                   "moved in two weeks the assumption was wrong. In advance, "
                   "so there is nothing left to renegotiate."},
            {"n": "Being refuted is not the same as being discarded",
             "d": "The common misreading is that a falsified theory goes in "
                  "the bin. His demand is that a theory be exposed to serious "
                  "attempts to break it, and good ones usually come out "
                  "stronger. What matters is whether you genuinely tried.",
             "eg": "Every quarter, go hunting for the strongest case against "
                   "your central judgement. If you look hard and find "
                   "nothing, that is when it is worth trusting."},
        ],
        "q": [
            "A theory which is not refutable by any conceivable event is "
            "non-scientific.",
            "Irrefutability is not a virtue of a theory but a vice.",
            "Say in advance what would make you admit you were wrong.",
        ],
        "apply":
            "Where you are: somebody has handed you a claim that sounds "
            "thoroughly reasonable.\n"
            "Ask first: under what circumstances would this be false, and can "
            "they answer that at all?\n"
            "Where it goes wrong: using the criterion to dismiss every field "
            "that cannot be measured, or as a debating move that leaves "
            "nobody able to conclude anything.",
    },
    {
        "k": "seek-refutation",
        "n": "Go looking for the counter-example",
        "w": "One black swan beats a hundred white ones",
        "src": "The Logic of Scientific Discovery",
        "dek": "No number of white swans settles the question. This page is "
               "about what you should be collecting instead.",
        "story":
            "The swan is his illustration of the problem of induction. "
            "==However many white swans you observe, none of it establishes "
            "that all swans are white, and a single black one settles it.== "
            "Evidence is wildly asymmetric. A confirming instance carries "
            "almost no information; a refuting one is decisive. People run "
            "the other way by default, gathering supportive cases and feeling "
            "steadier at the hundredth than at the first. So his method: "
            "propose boldly, then attack your own proposal as hard as you "
            "can.",
        "f": [
            {"n": "Go and ask the people who left",
             "d": "Where you take the sample decides the answer. Ask current "
                  "users whether they like it and the reply is close to "
                  "guaranteed. The information lives with the ones who "
                  "stopped. This is the most practical thing that falls out "
                  "of Popper.",
             "eg": "To test whether customers love the feature, do not survey "
                   "the ones still using it. Interview three who cancelled."},
            {"n": "Bold conjectures, severe attempts to refute",
             "d": "He is not asking for cautious hypotheses. He wants large "
                  "ones, paired with serious efforts to destroy them. The two "
                  "halves go together: conjecture without refutation is "
                  "daydreaming, refutation without conjecture is timidity.",
             "eg": "Put forward the aggressive plan, and name the three "
                   "observations that would show the route is closed. Then go "
                   "and look for them."},
            {"n": "Confirmation bias is the factory setting",
             "d": "Hunting for support is pleasant and fast, because the "
                  "motive sits on that side. Good intentions do not correct "
                  "it. Only procedure does: make finding the counter-example "
                  "a step on the checklist rather than something you remember "
                  "to do.",
             "eg": "Add a permanent field to the review template for the "
                   "strongest argument against, and require the proposer to "
                   "fill it in himself."},
        ],
        "q": [
            "No number of white swans establishes that all swans are white.",
            "One black swan is enough to settle it.",
            "It is easy to obtain confirmations for nearly every theory, if "
            "we look.",
        ],
        "apply":
            "Where you are: the more you check, the more certain you get.\n"
            "Ask first: in the last hour, were you collecting support or "
            "hunting a counter-example? What is the strongest evidence "
            "against, and did you look for it?\n"
            "Where it goes wrong: making refutation a way of never deciding — "
            "the point is a judgement you can rely on, not a paralysed one.",
    },
]

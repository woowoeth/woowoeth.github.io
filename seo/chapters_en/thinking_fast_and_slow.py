# -*- coding: utf-8 -*-
"""Thinking, Fast and Slow — English.

System 1 and System 2 have been absorbed into office vocabulary, where they
are used as though the brain had two departments and naming the culprit were
the same as fixing it. Kahneman was careful that they are fictitious
characters. These two pages take the parts that actually change decisions —
the missing information that never announces itself, and the asymmetry
between losing and winning.
"""

PARENT = {
    "name": "Thinking, Fast and Slow",
    "slug": "thinking-fast-and-slow",
    "blurb": "Deep read",
    "items": [
        {"k": "wysiati", "n": "What you see is all there is",
         "w": "Nothing announces the missing information", "ready": True,
         "line": "The mind never asks about the evidence it does not have"},
        {"k": "loss-aversion", "n": "Losses loom larger",
         "w": "Losing hurts about twice as much", "ready": True,
         "line": "The same sum lost hurts roughly twice what winning it "
                 "pleases"},
    ],
}

CHAPTERS = [
    {
        "k": "wysiati",
        "n": "What you see is all there is",
        "w": "Nothing announces the missing information",
        "src": "Thinking, Fast and Slow, chapter 7",
        "dek": "Kahneman gave the mind's largest defect an acronym. This page "
               "is about why ignorance produces no sensation at all.",
        "story":
            "He named it WYSIATI: ==what you see is all there is.== The fast, "
            "associative part of the mind builds the most coherent story "
            "available out of whatever material is to hand, and never "
            "enquires about what is missing. Confidence then reads off the "
            "smoothness of that story rather than the amount or quality of "
            "evidence behind it, which is why less information often produces "
            "more certainty. There is less to contradict. He was careful, "
            "too, that System 1 and System 2 are fictitious characters, not "
            "departments you can address.",
        "f": [
            {"n": "Certainty measures coherence, not evidence",
             "d": "The feeling of being sure is a reading of narrative fit, "
                  "not of proof. Three facts that happen to form a causal "
                  "chain generate more conviction than ten that conflict. So "
                  "weigh a judgement by counting what stands behind it, never "
                  "by its tone.",
             "eg": "Twenty minutes with a candidate and the interviewer just "
                   "knows. Twenty minutes is exactly little enough to "
                   "assemble an impression with no contradictions in it."},
            {"n": "Nothing in you flags the gap",
             "d": "There is no internal alarm for what you have not seen. The "
                  "story simply closes over the hole. The repair has to come "
                  "from outside: a fixed list forcing you to name what this "
                  "decision needs, what you hold, and how the missing pieces "
                  "would change the answer.",
             "eg": "Add one line to the template: key information not yet "
                   "obtained. It usually fills with three items, and one of "
                   "them turns the decision around."},
            {"n": "Whatever arrives first becomes the foundation",
             "d": "Because the story is assembled from what is present, the "
                  "earliest information lays the foundations and later "
                  "evidence can only be fitted around them. The order of "
                  "reporting is therefore a form of power. Whoever speaks "
                  "first has framed it for everybody.",
             "eg": "In a serious dispute the side heard first usually wins. "
                   "Have both put it in writing, submitted at the same time, "
                   "and opened together."},
        ],
        "q": [
            "What you see is all there is.",
            "A remarkable aspect of your mental life is that you are rarely "
            "stumped.",
            "Naming which system is speaking does not stop it speaking.",
        ],
        "apply":
            "Where you are: you feel very sure about a judgement.\n"
            "Ask first: is the certainty coming from the quantity of evidence "
            "or the smoothness of the story? Can you name three things this "
            "judgement is missing?\n"
            "Where it goes wrong: treating never having complete information "
            "as a reason never to decide, or running the audit only on other "
            "people's confidence.",
    },
    {
        "k": "loss-aversion",
        "n": "Losses loom larger",
        "w": "Losing hurts about twice as much",
        "src": "Thinking, Fast and Slow, chapters 26 to 28",
        "dek": "The same hundred hurts about twice as much going out as "
               "coming in. This page is about what that decides for you.",
        "story":
            "The hardest finding in prospect theory is that ==losses loom "
            "larger than gains, by a factor most experiments put between one "
            "and a half and two and a half.== Kahneman measures it with a "
            "coin toss: tails and you lose a hundred, so how much must heads "
            "pay before you will play? Most people want about two hundred. A "
            "chain of behaviour follows. People take the safe option over "
            "gains and gamble to avoid losses, they overvalue whatever they "
            "already hold, and every result is counted from a reference "
            "point.",
        "f": [
            {"n": "The double weight is a thumb on the status quo",
             "d": "Any proposal that changes things has its possible losses "
                  "silently doubled while its possible gains are counted at "
                  "face value. Two options of identical expected value are "
                  "not judged equally. To give change a fair hearing, put the "
                  "cost of standing still on the table.",
             "eg": "The case for replacing the old system counted migration "
                   "risk and left out what another year of maintenance and "
                   "forgone work costs. Written as a number, the scales "
                   "level."},
            {"n": "People who are behind start gambling",
             "d": "Faced with a certain loss, most people prefer a larger "
                  "uncertain one for the chance of getting back to even. That "
                  "is not weak character, it is the standard output of the "
                  "mechanism, which makes an unrealised loss the most "
                  "dangerous moment there is.",
             "eg": "Three million down, and another two might save it sounds "
                   "like resolve. Bring in somebody carrying none of the sunk "
                   "cost to judge it."},
            {"n": "Reference points can be set",
             "d": "Gain and loss are always relative to something. A bonus "
                  "rumoured at thirty and paid at forty is a delight; "
                  "rumoured at fifty and paid at forty it is an insult. Same "
                  "money. Whoever controls the comparison controls what the "
                  "fact feels like.",
             "eg": "Quote high, then give the real price, and the client "
                   "experiences a saving. Give the real price first and they "
                   "experience a cost. Identical number."},
        ],
        "q": [
            "Losses loom larger than gains.",
            "Facing gains people take the safe option; facing losses they "
            "gamble.",
            "A slow procedure catches what a fast individual cannot.",
        ],
        "apply":
            "Where you are: a proposal to change something feels far too "
            "risky.\n"
            "Ask first: have you counted what staying costs? And are you "
            "sitting inside a loss right now?\n"
            "Where it goes wrong: learning that reference points move and "
            "using it only on other people, or citing loss aversion as a "
            "reason never to change anything.",
    },
]

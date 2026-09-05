# -*- coding: utf-8 -*-
"""Ray Dalio — English.

Principles is on a lot of English shelves, and Bridgewater is known as the
place that tapes its meetings, which usually gets filed under eccentric
culture. The job of this page is to show the two halves as one machine: a
formula for converting failure into a rule, and a way of deciding whose
opinion carries weight — both of which came out of a single bankruptcy.
"""

PARENT = {
    "name": "Ray Dalio",
    "slug": "dalio",
    "blurb": "Deep read",
    "items": [
        {"k": "pain-plus-reflection", "n": "Pain plus reflection",
         "w": "What 1982 actually cost him", "ready": True,
         "line": "He got the crisis right and lost the firm anyway"},
        {"k": "believability", "n": "Weigh the opinion, do not count it",
         "w": "Neither a vote nor a verdict", "ready": True,
         "line": "Everyone speaks; not everyone's vote weighs the same"},
    ],
}

CHAPTERS = [
    {
        "k": "pain-plus-reflection",
        "n": "Pain plus reflection",
        "w": "What 1982 actually cost him",
        "src": "Principles, Part One",
        "dek": "He destroyed his own firm and later called it one of the best "
               "things that ever happened to him. The step in between is the "
               "point.",
        "story":
            "In 1982 he said publicly that a Mexican default would tip the "
            "United States into depression. Mexico defaulted. The market did "
            "the opposite and began a long bull run. Bridgewater shrank to "
            "one employee, and he borrowed four thousand dollars from his "
            "father to pay the bills. Years later he named the mechanism: "
            "==Pain + Reflection = Progress.== The reflection was specific. "
            "He stopped asking whether he was right and started asking how he "
            "knew he was right, and began writing his decision rules down "
            "where they could be tested.",
        "f": [
            {"n": "Neither term works alone",
             "d": "Pain without reflection leaves damage and avoidance. "
                  "Reflection without pain stays theoretical, because a "
                  "review that costs nothing rarely changes behaviour. The "
                  "value of that particular failure was that it hurt enough "
                  "to force the second term, and the second term changed how "
                  "the work was done.",
             "eg": "Two teams take the same expensive mistake. One writes it "
                   "into how decisions are made, the other says be careful "
                   "next time. In two years they are different companies."},
            {"n": "Review the machine, not the answer",
             "d": "His 1982 call was half right: the default happened. What "
                  "was wrong was the rule that being right justified the size "
                  "of the bet. A review that stops at which forecast failed "
                  "corrects one opinion. Going after how the certainty formed "
                  "corrects the thing that produces every opinion.",
             "eg": "Asking why the forecast was wrong buys one lesson. Asking "
                   "who dissented and why it went nowhere buys a change to "
                   "the process."},
            {"n": "Pain is a signal, not a discipline",
             "d": "His later habit was to treat the feeling as a pointer to "
                  "something worth learning and go towards it. Read the other "
                  "way it becomes a cult of suffering. The instruction is not "
                  "to manufacture pain, and pain with no reflection behind it "
                  "is simply pain.",
             "eg": "The afternoon a customer took your work apart in front of "
                   "you is the densest information of the quarter, but only "
                   "if you open it that evening."},
        ],
        "q": [
            "Pain + Reflection = Progress.",
            "I went from thinking I'm right to asking how do I know I'm "
            "right?",
            "It gave me the humility I needed to balance my aggressiveness.",
        ],
        "apply":
            "Where you are: an expensive failure has just finished "
            "happening.\n"
            "Ask first: besides what the wrong call was, how did the "
            "certainty form, and where did dissent get stopped?\n"
            "Where it goes wrong: reading the formula as suffering builds "
            "character and skipping the second term, or reflecting on the "
            "conclusion and leaving the machine that produced it untouched.",
    },
    {
        "k": "believability",
        "n": "Weigh the opinion, do not count it",
        "w": "Neither a vote nor a verdict",
        "src": "Principles, the work principles",
        "dek": "He rejects the boss deciding and he rejects one person one "
               "vote. What replaces them is a weighting, and it needs a "
               "record to run on.",
        "story":
            "Two familiar ways to decide badly: autocracy, where the boss "
            "rules and information cannot get in, and democracy, where one "
            "vote each lets ten amateurs outweigh one expert. Bridgewater "
            "runs a third. ==Everyone gets to speak, and opinions are "
            "weighted by the speaker's track record in that particular "
            "field.== Someone who has called currencies right three times "
            "carries more weight on currencies. The foundation is the taping "
            "and the public scoring, because without a record a track record "
            "cannot be checked. The aim is that the best idea wins whoever it "
            "comes from.",
        "f": [
            {"n": "Equal airtime, unequal weight",
             "d": "Letting everyone speak and letting every opinion count the "
                  "same are different policies. The first lets information "
                  "in. The second lets ten hunches outvote one informed "
                  "judgement. Splitting them is the whole design: speaking is "
                  "universal, weight is earned inside a field.",
             "eg": "An intern should be able to challenge the technical call, "
                   "and the two objections should not weigh the same. On what "
                   "young users like, the weighting may invert."},
            {"n": "Weight hangs on records, or it hangs on rank",
             "d": "With no record of who judged what and how it turned out, "
                  "believability quietly becomes a synonym for seniority. "
                  "That is why the transparency is not a cultural gesture. It "
                  "is the data layer the weighting runs on, and without it "
                  "the system reverts to hierarchy.",
             "eg": "Start logging big calls in three columns: prediction, "
                   "reasoning, outcome. Six months on, the loudest voice and "
                   "the most accurate one are rarely the same person."},
            {"n": "Weight resets at the edge of the field",
             "d": "Believability is domain-bound. An investing record does "
                  "not confer weight on a hiring decision, and technical "
                  "authority does not confer weight on pricing. The usual "
                  "failure is halo spill, where the person who is excellent "
                  "at one thing carries the most weight in every meeting.",
             "eg": "A founder's word on the product is backed by a record. On "
                   "legal exposure and pay bands, his instinct should queue "
                   "with everyone else's."},
        ],
        "q": [
            "An idea meritocracy is a system in which the best ideas win out.",
            "Everyone speaks. Not everyone's vote weighs the same.",
            "Believability is earned in one field at a time.",
        ],
        "apply":
            "Where you are: an important disagreement just got settled by "
            "whoever outranked the room.\n"
            "Ask first: in this specific field, whose track record can "
            "actually be looked up? Are we weighing evidence or status?\n"
            "Where it goes wrong: using believability to freeze the old guard "
            "in place so newcomers never build a first record, or invoking "
            "the weighting with no log to compute it from.",
    },
]

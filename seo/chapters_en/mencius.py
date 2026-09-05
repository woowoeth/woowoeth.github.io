# -*- coding: utf-8 -*-
"""Mencius — English.

To an English reader Mencius arrives as the softer Confucian, the one with
the line about human nature being good, which makes him sound like a moral
encourager. The three chapters here take the opposite line: he is the writer
who turned benevolence from a virtue into a condition of staying in power,
and every one of his famous sentences is a piece of that argument.
"""

PARENT = {
    "name": "Mencius",
    "slug": "mencius",
    "blurb": "Deep read",
    "items": [
        {"k": "people-first", "n": "The people come first",
         "w": "Where the ground under power actually is", "ready": True,
         "line": "What a ruler counts is consent, and consent can be withdrawn"},
        {"k": "force-vs-virtue", "n": "Two different ways of being obeyed",
         "w": "Compliance and conviction look identical", "ready": True,
         "line": "Force has to be applied every day. Nothing else does"},
        {"k": "flood-like-qi", "n": "The flood-like breath",
         "w": "It accumulates, and it cannot be hurried", "ready": True,
         "line": "Nerve is a deposit account. Nobody can lend you theirs"},
    ],
}

CHAPTERS = [
    {
        "k": "people-first",
        "n": "The people come first",
        "w": "Where the ground under power actually is",
        "src": "Mencius, Jin Xin II and Li Lou I",
        "dek": "Read for two thousand years as ancient humanism. It reads "
               "better as a technical claim about where a government's power "
               "comes from.",
        "story":
            "==The people are the most important; the altars of grain and "
            "land come next; the ruler counts least.== He ranked all three, "
            "and put the ruler at the bottom. This is not a plea for "
            "kindness, it is his judgement about what keeps a regime "
            "standing. Elsewhere he is blunter. There is a way to gain the "
            "empire: gain the people. There is a way to gain the people: "
            "gain their hearts. So benevolent government, in Mencius, is not "
            "the ruler's private virtue. It is the condition of his "
            "continuing to be the ruler.",
        "f": [
            {"n": "Consent is a thing that gets withdrawn",
             "d": "The heart of the people is not affection, it is consent. "
                  "People rarely revolt at the moment they turn; they stop "
                  "cooperating first. The tax gets harder to collect, the "
                  "levy comes up short, the order goes down and nobody "
                  "carries it out with care. The power is already hollow "
                  "while the name is intact.",
             "eg": "Nobody objects in the meeting, nothing moves afterwards, "
                   "the reports start being padded, and the people leaving "
                   "give a reason that is not the reason."},
            {"n": "The order cannot be inverted",
             "d": "Put the institution, or the man at the top, in front of "
                  "the people who carry the cost, and you get one specific "
                  "family of bad decisions: the ones that protect a "
                  "reputation or an earlier judgement by charging somebody "
                  "else for it. Authority holds. The ground under it goes.",
             "eg": "Rather than admit the last decision was wrong, the team "
                   "spends another month filling the hole. The authority "
                   "survives; half the people worth keeping do not."},
            {"n": "Tax, service and punishment are three measurable lines",
             "d": "He never leaves benevolence at the level of a concept. The "
                  "items are specific: do not take men away in the farming "
                  "season, keep the taxes light, keep the punishments few. "
                  "All three are countable, and all three are set by the "
                  "person in charge, alone.",
             "eg": "Judge any new policy with two questions. What did it give "
                   "the people doing the work, and what did it take? Run the "
                   "ratio over a year, not a week."},
        ],
        "q": [
            "The people come first, the altars of the state next, the ruler "
            "last.",
            "Gather for them what they want; do not impose what they hate.",
            "Treat them as your hands and feet and they treat you as their "
            "heart.",
        ],
        "apply":
            "Where you are: a decision that is easy to justify upwards and "
            "hard on the people who have to carry it.\n"
            "Ask first: will the side paying for this still cooperate with "
            "the next thing you ask? That, not the objection, is the reading "
            "you want.\n"
            "Where it goes wrong: reading silence as agreement; or defending "
            "a judgement you have already made by having other people keep "
            "paying for it.",
    },
    {
        "k": "force-vs-virtue",
        "n": "Two different ways of being obeyed",
        "w": "Compliance and conviction look identical",
        "src": "Mencius, Gongsun Chou I",
        "dek": "Two people are doing what you asked, and the two cases have "
               "nothing in common. This is how to tell which one you have.",
        "story":
            "He sets them side by side. ==Those subdued by force do not "
            "submit in their hearts; they submit because their strength is "
            "not enough.== Those won over by virtue are pleased in the heart "
            "and submit in earnest. Then the mechanical detail: obedience "
            "bought by force has to be paid for continuously, and the moment "
            "the balance of strength shifts it disappears. Which is why he "
            "adds that a man using force under a borrowed name becomes a "
            "hegemon, and a hegemon needs a large state, while one who acts "
            "from virtue becomes a king, and a king need not be large.",
        "f": [
            {"n": "The measurement is taken while you are away",
             "d": "In your presence the two kinds of obedience are "
                  "indistinguishable, which is why watching harder tells you "
                  "nothing. The difference only appears in your absence, so "
                  "the test is simple: over the stretch when nobody was "
                  "checking, did the standard hold or drop?",
             "eg": "Take the two weeks of leave and look at what shipped "
                   "while you were gone. It is a better instrument than any "
                   "engagement survey."},
            {"n": "Force costs the same every day, then more",
             "d": "Their strength is not enough names the property that "
                  "matters: force has to keep being applied. Supervision, "
                  "scoring and checking never get cheaper with time, and "
                  "they get dearer as people learn to handle them. "
                  "Conviction costs most at the start and then tends "
                  "towards nothing.",
             "eg": "The clock-in system works for a month. By month three "
                   "there are workarounds, and somebody is being paid to "
                   "design defences against them."},
            {"n": "A king need not be large",
             "d": "Force needs mass behind it, so the smaller party always "
                  "loses that contest. Conviction does not. This is the "
                  "route Mencius leaves open to the weaker side: you cannot "
                  "become stronger than them this year, but you can become "
                  "more worth following than them this year.",
             "eg": "A small firm cannot beat the salary. It can offer real "
                   "say in decisions, a visible path, and promises that get "
                   "kept. None of that costs money. All of it has to be "
                   "honoured."},
        ],
        "q": [
            "Those subdued by force submit for lack of strength, not in "
            "their hearts.",
            "The hegemon needs a large state. The true king does not.",
            "Heaven's timing yields to ground; ground yields to people in "
            "accord.",
        ],
        "apply":
            "Where you are: the team looks disciplined and you cannot tell "
            "whether it is real or propped up.\n"
            "Ask first: over the last stretch when you were not watching, how "
            "far did the standard fall? Measure it before you add anything.\n"
            "Where it goes wrong: answering a delivery problem with more "
            "supervision, which prices upward for ever; or taking the absence "
            "of complaints as evidence of agreement.",
    },
    {
        "k": "flood-like-qi",
        "n": "The flood-like breath",
        "w": "It accumulates, and it cannot be hurried",
        "src": "Mencius, Gongsun Chou I",
        "dek": "Asked what the flood-like breath was, he said it is hard to "
               "put into words. Here is where it comes from, and how it "
               "leaks away.",
        "story":
            "He calls it vast and unbending, and then says where it comes "
            "from: ==it is produced by an accumulation of right acts, and is "
            "not seized by one righteous act from outside.== Then the "
            "counter-example. A man of Song, impatient at how slowly his "
            "rice was coming on, went through the field pulling every shoot "
            "up a little, and came home saying he was worn out from helping "
            "the rice to grow. His son ran out to look. The whole crop had "
            "withered. The breath cannot be hurried.",
        "f": [
            {"n": "Accumulated, never acquired",
             "d": "Steadiness comes out of the record of things you have "
                  "actually got right, one at a time. That is why it cannot "
                  "be rushed and cannot be borrowed. Confidence somebody "
                  "else hands you does not survive contact with the first "
                  "real pressure; the sort you banked yourself does.",
             "eg": "The first contract you closed alone, the first outage you "
                   "carried on your own. Ten talks about composure replace "
                   "neither of them."},
            {"n": "One thing done against yourself and it leaks",
             "d": "Do a thing your own heart cannot approve, he says, and the "
                  "breath starves. The mechanism is practical rather than "
                  "mystical: next time you have to hold a line, you know "
                  "about the exception, and so does everyone who watched you "
                  "make it.",
             "eg": "You waved through one soft number to make a date. The "
                   "next time you ask the team to hold the standard, the "
                   "sentence comes out a shade quieter."},
            {"n": "Do not pull the shoots",
             "d": "The opposite failure is impatience: pressure, slogans and "
                  "short-term targets used to force a state of mind into "
                  "existence. The shoots do look taller. His instruction is "
                  "to always have the work in hand, never to forget it, and "
                  "never to help it along.",
             "eg": "To get a new hire up to speed you hand him a project well "
                   "past his reach. It looks like an opportunity and ends as "
                   "a person somebody else has to repair."},
        ],
        "q": [
            "It is produced by accumulated rightness, not seized by one act "
            "from outside.",
            "Do a thing your heart cannot approve, and the breath starves.",
            "Keep the work in hand. Do not forget it. Do not help it grow.",
        ],
        "apply":
            "Where you are: under pressure you find there is nothing solid "
            "underneath you, and you want to fix that quickly.\n"
            "Ask first: in the last six months, how many things did you carry "
            "from beginning to end yourself? That number is the account "
            "balance.\n"
            "Where it goes wrong: substituting encouragement and slogans for "
            "real completed work; or accelerating somebody by putting him "
            "somewhere far beyond his reach.",
    },
]

# -*- coding: utf-8 -*-
"""La Rochefoucauld — English.

The English reader files him as the cynic, which is a way of not having to
answer him. The page takes the opposite line: read as a confession rather
than an accusation, written by a man who had performed every vanity he
dissects, the maxims stop being clever and start being usable — two of them
here, one about the fault nobody will admit and one about what a disguise
tells you about the place you are standing in.
"""

PARENT = {
    "name": "La Rochefoucauld",
    "slug": "la-rochefoucauld",
    "blurb": "Deep read",
    "items": [
        {"k": "memory-vs-judgment", "n": "Nobody complains about their judgement",
         "w": "The shape of the blind spot", "ready": True,
         "line": "Everyone says their memory is poor. Nobody says their eye is"},
        {"k": "vice-pays-tribute", "n": "Hypocrisy is a tribute",
         "w": "The disguise tells you the exchange rate", "ready": True,
         "line": "Even the bad have to look good, which is what makes good the currency"},
    ],
}

CHAPTERS = [
    {
        "k": "memory-vs-judgment",
        "n": "Nobody complains about their judgement",
        "w": "The shape of the blind spot",
        "src": "Maxims, numbers 89, 31 and 149",
        "dek": "One sentence draws the border of self-knowledge. This is why "
               "the first admission is easy and the second nearly "
               "impossible.",
        "story":
            "La Rochefoucauld was a defeated nobleman of the Fronde who spent "
            "his later years turning what he had seen at court and in the "
            "field into a few hundred maxims. Number 89: ==everyone complains "
            "of his memory, no one complains of his judgment==. Admitting "
            "a poor memory costs nothing, since it is a hardware fault. "
            "Admitting poor judgement concedes that the ground under every "
            "past decision was unsound, and nobody can carry that. Number 31 "
            "travels with it: if we had no faults, we would not enjoy "
            "noticing them in others.",
        "f": [
            {"n": "People only admit faults that leave the base intact",
             "d": "Memory, stamina, a weak second language: these cost "
                  "nothing to concede, because none of them disturbs the "
                  "belief that you are a person who sees clearly. The real "
                  "blind spots sit in the class nobody will own. A "
                  "volunteered fault can usually be crossed off the list.",
             "eg": "Asked for a weakness in an interview, the candidate who "
                   "says they are too much of a perfectionist has told you "
                   "nothing. Listen to how they explain their last failure."},
            {"n": "Failures of judgement get rewritten by memory",
             "d": "After a bad call, memory quietly adds a layer of "
                  "narrative: the information was thin, someone misled us, "
                  "the luck was strange. A few rewrites later, no misjudgement "
                  "has ever occurred. The only defence is writing the call "
                  "and the reasons down at the time.",
             "eg": "Before a major decision, write one page: what you expect "
                   "to happen and why. Read it six months later. Most people "
                   "are startled the first time."},
            {"n": "Finding fault in others is a painkiller",
             "d": "Number 31 names the payoff in eager correction. Attention "
                  "on somebody else's defects gives temporary relief from "
                  "noticing your own. So the moment your urge to criticise "
                  "runs hottest deserves suspicion: it tracks your position, "
                  "not their error rate.",
             "eg": "In the weeks your own project is stuck, every proposal "
                   "that crosses your desk looks full of holes."},
        ],
        "q": [
            "Everyone complains of his memory, no one complains of his "
            "judgment.",
            "If we had no faults, we would not enjoy noticing them in others.",
            "The refusal of praise is only the wish to be praised twice.",
        ],
        "apply":
            "Where you are: you are reviewing what happened, and the "
            "conclusion has landed on external factors again.\n"
            "Ask first: in this account, what percentage is your own "
            "judgement? And in the one before it?\n"
            "Where it goes wrong: letting self-suspicion paralyse every "
            "decision; or using the maxim only as an instrument for reading "
            "other people.",
    },
    {
        "k": "vice-pays-tribute",
        "n": "Hypocrisy is a tribute",
        "w": "The disguise tells you the exchange rate",
        "src": "Maxims, number 218",
        "dek": "He wrote hypocrisy up as an act of homage. Inside the sneer "
               "there is a working method for reading a place.",
        "story":
            "Number 218: ==hypocrisy is the homage vice pays to virtue==. "
            "Vice has to dress as virtue in order to circulate, and that fact "
            "alone proves virtue is the hard currency there, since nobody "
            "disguises themselves as something worthless. The whole book runs "
            "this operation. Our virtues, he writes, are most frequently but "
            "vices disguised. Neither the sun nor death can be looked at "
            "steadily. He is not arguing that people are wholly bad. He is "
            "taking the wrapping off so the structure of the exchange "
            "underneath becomes visible.",
        "f": [
            {"n": "What people fake tells you what the place pays for",
             "d": "Whatever people imitate is the currency of that "
                  "environment. Where everyone performs long hours for the "
                  "boss, hours are money. Where everyone competes to sound "
                  "profound in meetings, talk outranks delivery. The "
                  "direction of the pretence reads truer than the values on "
                  "the wall.",
             "eg": "To learn what a company actually rewards, skip the "
                   "culture handbook and watch what a new hire has learned to "
                   "perform by month three."},
            {"n": "The existence of the disguise is worth more than exposing it",
             "d": "If vice has to dress as virtue to pass, then the norm "
                  "requiring the dress has real value, because it constrains "
                  "the surface of behaviour. A place where nobody bothers to "
                  "pretend has stopped treating virtue as currency, and that "
                  "is the deeper rot.",
             "eg": "Somebody gives to charity for the reputation. Unmasking "
                   "them gains nothing. The rule that reputation follows good "
                   "deeds is the part worth defending."},
            {"n": "Run the same operation on yourself",
             "d": "The hardest thing about the book is that it exempts "
                  "nobody, the author included. Taking apart one of your own "
                  "moral positions to see the interest underneath is not "
                  "self-abasement. It lets you predict where you will wobble "
                  "when the interest moves.",
             "eg": "A principle you hold has always happened to pay you. Work "
                   "out now what will be left of it on the day it starts "
                   "costing you."},
        ],
        "q": [
            "Hypocrisy is the homage vice pays to virtue.",
            "Our virtues are most frequently but vices disguised.",
            "Neither the sun nor death can be looked at steadily.",
        ],
        "apply":
            "Where you are: you have noticed that someone's good deed has an "
            "interest sitting behind it.\n"
            "Ask first: what does the shape they chose to fake tell you about "
            "what this place rewards, and what will you do with that?\n"
            "Where it goes wrong: making a career of unmasking, so that every "
            "decent act becomes suspect; or running the operation only on "
            "other people and never on yourself.",
    },
]

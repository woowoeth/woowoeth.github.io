# -*- coding: utf-8 -*-
"""Thinking in Systems — English.

Systems thinking reaches most English readers as a vocabulary: feedback,
emergence, holistic. Vocabulary changes nothing. Meadows wrote a manual with
two operational parts — a diagnostic order that stops you reaching for the
people first, and a ranked list of twelve places to intervene, with the
uncomfortable finding that the strongest ones sit empty. This page keeps both
parts and the arithmetic under them.
"""

PARENT = {
    "name": "Thinking in Systems",
    "slug": "thinking-in-systems",
    "blurb": "Deep read",
    "items": [
        {"k": "structure-drives-behavior", "n": "Structure drives behaviour",
         "w": "Stop blaming the parts", "ready": True,
         "line": "Three people held the job and it failed the same way each time"},
        {"k": "leverage-points", "n": "Leverage points",
         "w": "Right place, wrong direction", "ready": True,
         "line": "People find the leverage point and then push it the wrong way"},
    ],
}

CHAPTERS = [
    {
        "k": "structure-drives-behavior",
        "n": "Structure drives behaviour",
        "w": "Stop blaming the parts",
        "src": "Thinking in Systems, chapters 1 and 4",
        "dek": "The same problem has now survived three different people. This "
               "is Meadows on why that is the moment to stop blaming anyone.",
        "story":
            "Meadows builds the whole book on one sentence: ==system "
            "structure is the source of system behavior==. She "
            "demonstrates it with a car dealer who orders new stock from "
            "what he sold last week. Deliveries take three days, he waits "
            "a few days before believing a change is real, and the result "
            "is a showroom that swings between empty and overflowing. "
            "Nothing in the model is a bad decision. Every order is "
            "sensible on the day it is placed; the oscillation lives in "
            "the delays. Replace the manager and the same graph comes "
            "back. Stocks, flows and loops decide what a system does, "
            "whatever the parts are made of.",
        "f": [
            {"n": "A problem that keeps returning is a structural signal",
             "d": "A one-off can be put down to a person or to luck. A "
                  "problem that recurs and survives a change of personnel "
                  "cannot: it means a loop in the structure is producing it "
                  "reliably. Handling the person is swapping a part, and the "
                  "part goes back into the same machine.",
             "eg": "Three people have left this role inside a year. Before "
                   "the fourth advert goes out, draw who this job answers to "
                   "and what it is allowed to decide."},
            {"n": "Look at the pattern, not at the events",
             "d": "Events are waves on the surface; patterns are the current "
                  "beneath. Meadows tells you to stretch the time axis and "
                  "ask what shape this number has made over two years — "
                  "oscillation, exponential rise, an S-curve, overshoot and "
                  "collapse. Each shape belongs to a particular arrangement "
                  "of loops.",
             "eg": "Stock keeps swinging from famine to glut. Auditing orders "
                   "one by one never ends. Plot two years, recognise the "
                   "standard oscillation, and go looking for the delay."},
            {"n": "Structure is not an alibi",
             "d": "No separate villains is easily heard as nobody is "
                  "accountable. Meadows means the reverse. Precisely because "
                  "structure produces behaviour, whoever can change the "
                  "structure carries the most responsibility: whoever sets "
                  "targets, writes the process and decides what information "
                  "reaches whom is writing what this system will do.",
             "eg": "Salespeople keep overpromising and no amount of policing "
                   "stops it. The person most responsible is whoever made "
                   "signed revenue this quarter the only measure."},
        ],
        "q": [
            "System structure is the source of system behavior.",
            "A system's behaviour cannot be known from its elements alone.",
            "A chronic problem is not a bad person. It is a loop.",
        ],
        "apply":
            "Where you are: the same problem has been handled several times, "
            "the people have changed, and it is still here.\n"
            "Ask first: which loop produces this behaviour, and who has the "
            "authority to change that loop?\n"
            "Where it goes wrong: using structure to excuse everybody; or "
            "drawing the diagram and then still intervening only at the level "
            "of the parts.",
    },
    {
        "k": "leverage-points",
        "n": "Leverage points",
        "w": "Right place, wrong direction",
        "src": "Meadows, Leverage Points: Places to Intervene in a System",
        "dek": "She ranked twelve places to intervene in a system, weakest to "
               "strongest. This is why almost nobody uses the strong ones.",
        "story":
            "Her famous essay puts the twelve in order. Weakest are the "
            "numbers — tax rates, budgets, thresholds — the dials everyone "
            "spends the day turning while the system carries on doing what it "
            "did. Above them sit feedback loops and flows of information. "
            "Higher still are the rules and the goals, and ==the strongest "
            "place of all is the goal of the system and the paradigm "
            "underneath it==. Then comes the line that stings: people know "
            "intuitively where the leverage points are, and push them in the "
            "wrong direction. The dials are crowded because they are easy. "
            "The paradigm is empty because it is not.",
        "f": [
            {"n": "Numbers are the busiest and the weakest lever",
             "d": "Moving a target, adding or cutting budget, shifting a "
                  "threshold: instant to do, instant to see, which is why "
                  "they absorb nearly all management attention. But while the "
                  "loop structure holds, the system absorbs the change and a "
                  "few months later the old behaviour is back.",
             "eg": "Cut the response deadline from twenty-four hours to "
                   "twelve. Compliance rises for a fortnight, then everyone "
                   "learns to send a holding reply. The dial moved; the "
                   "behaviour did not."},
            {"n": "Information flow is the best value on the list",
             "d": "Putting a piece of information where it was previously "
                  "absent often beats changing the rules, because being seen "
                  "changes conduct by itself. Meadows keeps a Dutch housing "
                  "estate as her example: identical houses, meters in the "
                  "hall instead of the basement, and a third less electricity "
                  "used.",
             "eg": "Show each team the live cost of the calls it makes to an "
                   "internal service. Set no quota at all. Wasteful traffic "
                   "halves within a quarter."},
            {"n": "Wrong direction is commoner than wrong place",
             "d": "Her sharpest observation is that people find the point and "
                  "then push the wrong way. Growth too fast, so the instinct "
                  "is more control, when the lever is often less fuel in the "
                  "growth loop. Morale low, so the instinct is more "
                  "incentive, when the lever is removing a punishing "
                  "feedback.",
             "eg": "Too many meetings means coordination demand is high. "
                   "Banning meetings pushes it into private messages and "
                   "makes it worse. The lever is the coupling that requires "
                   "coordinating."},
        ],
        "q": [
            "People know intuitively where leverage points are, then push the "
            "wrong way.",
            "The weakest leverage points are numbers, constants and "
            "parameters.",
            "The paradigm out of which a system arises is the strongest "
            "lever.",
        ],
        "apply":
            "Where you are: you want to shift a stubborn system behaviour and "
            "your hand is already on one of the switches.\n"
            "Ask first: where does this switch sit in the twelve, is there a "
            "higher place for the same effort, and am I sure the push goes "
            "this way rather than that?\n"
            "Where it goes wrong: talking about paradigms while every actual "
            "action is a parameter; or turning information transparency into "
            "surveillance, so being seen becomes being watched.",
    },
]

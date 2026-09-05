# -*- coding: utf-8 -*-
"""Tao Te Ching — English."""

PARENT = {
    "name": "Tao Te Ching",
    "slug": "tao-te-ching",
    "blurb": "Deep read",
    "items": [
        {"k": "reversal", "n": "Whatever peaks, turns",
         "w": "The top is where to start worrying", "ready": True,
         "line": "At the top, look for what is already turning"},
        {"k": "wu-wei", "n": "The part you don't do",
         "w": "A list of moves to leave out", "ready": True,
         "line": "Every prohibition creates a reason to route around it"},
        {"k": "water", "n": "Go to the low ground",
         "w": "Not competing is a choice of location", "ready": True,
         "line": "Things flow to you because you are lower, not because you asked"},
        {"k": "usefulness-of-emptiness", "n": "The empty part is the useful part",
         "w": "What you left out is doing the work", "ready": True,
         "line": "The hole in the hub belongs to no spoke, which is why it turns"},
    ],
}

CHAPTERS = [
    {
        "k": "reversal",
        "n": "Whatever peaks, turns",
        "w": "The top is where to start worrying",
        "src": "Tao Te Ching 40",
        "dek": "Usually read as comfort for bad times. It is more useful as "
               "an instrument, and it is sharpest when things are going well.",
        "story":
            "Four characters: reversal is the movement of the way. The claim "
            "is not that things get better, nor that they get worse. It is "
            "that anything carried to its extreme starts producing its "
            "opposite. ==Which means the most dangerous moment is not the "
            "trough — it is the peak, because that is where nobody is "
            "looking for the turn.== In the trough the rule is working for "
            "you and nothing needs to be done about it.",
        "f": [
            {"n": "Read it at the top, not at the bottom",
             "d": "In a bad stretch the line reads as reassurance and asks "
                  "nothing of you. In a good stretch it asks a question you "
                  "would rather not answer: which of the things carrying us "
                  "right now is at full stretch, and what happens when it "
                  "stops.",
             "eg": "The year revenue doubled is the year nobody asked what "
                   "share of it came through one partner."},
            {"n": "Extremes, not durations",
             "d": "It says nothing about how long anything lasts. A thing at "
                  "moderate stretch can run for decades. What turns is what "
                  "has been pushed as far as it goes — margin at its "
                  "thinnest, hours at their longest, patience at its end.",
             "eg": "The team was not tired because two years had passed. It "
                   "was tired because the last four months had run at the "
                   "rate of a launch week."},
            {"n": "The move is to give something back early",
             "d": "If the turn is structural, the cheap version is to stop "
                  "short of the extreme on purpose: take some off the table, "
                  "keep the slack, decline the last increment. The expensive "
                  "version is to have it taken from you at the turn.",
             "eg": "He cut his own hours in the good quarter, which cost "
                   "output, and was the reason he was still there for the "
                   "bad one."},
        ],
        "q": [
            "Reversal is the movement of the way.",
            "The dangerous moment is the peak, because nobody is looking for "
            "the turn there.",
            "Stop short of the extreme on purpose, or have it taken at the "
            "turn.",
        ],
        "apply":
            "Where you are: something is going unusually well and you are "
            "being asked to push it further.\n"
            "Ask first: what is at full stretch right now, and what breaks "
            "when it stops?\n"
            "Where it goes wrong: reading it as fatalism, or as a reason not "
            "to grow — it is about not running any single thing to its "
            "limit, not about staying small.",
    },
    {
        "k": "wu-wei",
        "n": "The part you don't do",
        "w": "A list of moves to leave out",
        "src": "Tao Te Ching 37, 57, 63",
        "dek": "Usually translated as non-action and read as passivity. It is "
               "closer to a list of the moves that make things worse.",
        "story":
            "His verdict on governing is cold: ==the more prohibitions there "
            "are, the poorer the people; the more laws are published, the "
            "more thieves there are.== The alternative he offers is not "
            "letting go. It is: I do nothing and they transform themselves, I "
            "stay still and they correct themselves, I leave them alone and "
            "they prosper. The load-bearing word is themselves. The point is "
            "not to stop things happening; it is to stop being the thing that "
            "prevents them.",
        "f": [
            {"n": "Subtracting moves, not making none",
             "d": "In learning you gain daily; in the way you lose daily. "
                  "Getting good at running something is largely removing the "
                  "actions that look like management and function as "
                  "interference. Take out enough and the thing moves on its "
                  "own.",
             "eg": "Cancelling the weekly status meeting is what finally got "
                   "the status written down where anyone could read it."},
            {"n": "There is a mechanism behind more rules, more problems",
             "d": "Every prohibition creates an incentive to route around it, "
                  "and every correction leaves room for the next deviation. "
                  "This is not a claim about morality; it is that a control "
                  "grows the behaviour it was built to stop.",
             "eg": "The expense policy got three pages longer and the number "
                   "of creatively categorised dinners went up."},
            {"n": "Act while it is still small",
             "d": "Deal with the difficult while it is easy, the large while "
                  "it is small. Non-action is not never acting — it is moving "
                  "the action earlier, when a small one is enough. Wait and "
                  "you need a large one, and large ones have consequences of "
                  "their own.",
             "eg": "A ten-minute conversation in March, or a reorganisation "
                   "in September. It was the same problem."},
        ],
        "q": [
            "The more laws are published, the more thieves there are.",
            "Every prohibition creates a reason to route around it.",
            "Deal with the difficult while it is easy.",
        ],
        "apply":
            "Where you are: about to add a rule, a process or a meeting to "
            "fix something.\n"
            "Ask first: which existing action is producing this problem, and "
            "what happens if you remove it instead?\n"
            "Where it goes wrong: reading it as never intervene — it argues "
            "for intervening earlier and smaller, not less.",
    },
    {
        "k": "water",
        "n": "Go to the low ground",
        "w": "Not competing is a choice of location",
        "src": "Tao Te Ching 8, 66",
        "dek": "Water has been praised for two thousand years. The text "
               "credits it with one specific thing, and it is about position.",
        "story":
            "He gives water two lines, and both are needed. It benefits all "
            "things without contending — and ==it settles in the places "
            "people find distasteful.== The second is what makes the first "
            "possible: not contending is not a posture, it is a choice of "
            "site. He is blunter later — the reason the rivers and seas are "
            "king of the hundred valleys is that they are good at being "
            "below them. Things flow to you because you are lower.",
        "f": [
            {"n": "Not contending means standing where nobody is",
             "d": "The line is usually read as moral advice and is closer to "
                  "geometry: if the position you are in is one nobody wants, "
                  "the act of contending does not arise. It is settled at the "
                  "siting stage, not in the fight.",
             "eg": "Everyone was building the assistant. He built the boring "
                   "importer that all of them needed and none of them wanted "
                   "to own."},
            {"n": "The places people find distasteful",
             "d": "Low competitive density hides in the work that is dirty, "
                  "slow, or takes years to show a result. Those positions are "
                  "empty precisely because they look bad and produce nothing "
                  "reportable for a long time.",
             "eg": "Nobody wanted the migration. The person who took it ended "
                   "up the only one who understood how the whole thing "
                   "worked."},
            {"n": "Height stops the flow",
             "d": "If you want people, information or resources to come to "
                  "you, you have to be positioned below them. This is most "
                  "visible with information: the higher the posture, the less "
                  "of what is actually happening reaches you.",
             "eg": "Nobody brought him bad news for a year, and he took that "
                   "as evidence there wasn't any."},
        ],
        "q": [
            "It benefits all things without contending, and settles where "
            "people find distasteful.",
            "The rivers rule the valleys by being below them.",
            "The higher the posture, the less of what is happening reaches "
            "you.",
        ],
        "apply":
            "Where you are: choosing what to work on, in a space where "
            "everyone is going for the same thing.\n"
            "Ask first: which necessary job is empty because it looks "
            "unrewarding, and what would being there let you see?\n"
            "Where it goes wrong: mistaking it for accepting bad treatment — "
            "the low ground is a position, not a status.",
    },
    {
        "k": "usefulness-of-emptiness",
        "n": "The empty part is the useful part",
        "w": "What you left out is doing the work",
        "src": "Tao Te Ching 11",
        "dek": "Which part of a wheel is doing the work? The chapter is short "
               "enough to be a definition and it underwrites the whole book.",
        "story":
            "Three parallel examples: thirty spokes share one hub, and "
            "==because of the nothing at its centre the cart is useful==; "
            "clay is worked into a vessel, and because of the space inside it "
            "holds; doors and windows are cut for a room, and the emptiness is "
            "what you live in. One conclusion: what is there provides the "
            "advantage, what is not there provides the use. The visible part "
            "gets the credit. The gap does the job.",
        "f": [
            {"n": "Slack is not waste",
             "d": "The schedule with every slot filled, the interface with "
                  "every field used, the plant run at full capacity — all "
                  "have removed the room that absorbs surprise. One thing "
                  "goes off plan and there is nowhere for it to go.",
             "eg": "The team with two unbooked afternoons absorbed the "
                   "outage. The fully booked one moved every deadline by a "
                   "week."},
            {"n": "The empty place belongs to nobody",
             "d": "The hole in the hub is not owned by any spoke, and that is "
                  "exactly why the wheel turns. Organisations need the same "
                  "thing: capacity that belongs to no department, available "
                  "for whatever actually turns up.",
             "eg": "The unassigned engineer was the reason the incident was "
                   "handled the same day instead of entering a queue."},
            {"n": "Less is what makes it usable",
             "d": "Function is not improved by addition. Everything added "
                  "spends someone's understanding and someone's maintenance. "
                  "The hard judgement is never what else could go in; it is "
                  "what should be left out.",
             "eg": "Removing four of the seven options doubled the number of "
                   "people who finished the setup."},
        ],
        "q": [
            "What is there provides the advantage. What is not there provides "
            "the use.",
            "The hole in the hub belongs to no spoke, which is why it turns.",
            "The hard judgement is what to leave out.",
        ],
        "apply":
            "Where you are: a plan, a schedule or a product that is full.\n"
            "Ask first: where is the room for the thing you did not predict? "
            "If there is none, the plan only works if nothing surprises you.\n"
            "Where it goes wrong: using it to defend doing less — the point "
            "is deliberate space, not low effort.",
    },
]

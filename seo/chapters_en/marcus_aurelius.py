# -*- coding: utf-8 -*-
"""Marcus Aurelius — English.

The English reader almost certainly arrives holding one sentence already:
what stands in the way becomes the way. It has been on posters, gym walls
and book jackets for a decade. The job of this page is to take that line
back off the poster and set it down in Book Five, next to the fire it
belongs to and next to the man who wrote it in a tent on the Danube.
"""

PARENT = {
    "name": "Marcus Aurelius",
    "slug": "marcus-aurelius",
    "blurb": "Deep read",
    "items": [
        {"k": "obstacle-is-the-way", "n": "What stands in the way becomes the way",
         "w": "The line, and the mechanism under it", "ready": True,
         "line": "A fire turns whatever is thrown into it into flame"},
        {"k": "view-from-above", "n": "The view from above",
         "w": "Pull the scale back", "ready": True,
         "line": "Change the timescale and most emergencies shrink"},
        {"k": "morning-preparation", "n": "The morning rehearsal",
         "w": "Go through the people you will meet today", "ready": True,
         "line": "Offence you saw coming does half the damage"},
    ],
}

CHAPTERS = [
    {
        "k": "obstacle-is-the-way",
        "n": "What stands in the way becomes the way",
        "w": "The line, and the mechanism under it",
        "src": "Meditations, Book 5",
        "dek": "The most quoted line in the book, and the only one many "
               "English readers ever meet. Here is what surrounds it.",
        "story":
            "He wrote it as emperor, in a reign with almost no quiet year in "
            "it: plague, war on the Danube frontier, a trusted general in "
            "revolt. The note reads: ==the impediment to action advances "
            "action; what stands in the way becomes the way.== The mechanism "
            "is in the lines around it. The mind turns whatever blocks it to "
            "its own purpose, the way a fire takes what is thrown on it and "
            "makes flame out of it. The obstacle is not removed. It is "
            "burned.",
        "f": [
            {"n": "What is blocked is the route, not the destination",
             "d": "Almost always the thing in the way has closed one "
                  "particular path you had imagined. Separate the path from "
                  "the goal and most obstacles change from this cannot be "
                  "done into take another road. People who cannot separate "
                  "them read a route failure as a goal failure.",
             "eg": "If the goal was customers through that channel, the "
                   "channel closing ends it. If the goal was customers, it "
                   "moved you out of something already getting expensive."},
            {"n": "The fire image is about capacity",
             "d": "A small fire is smothered by a large log; a big one turns "
                  "the log into more of itself. So the same setback lands "
                  "differently on different people, and the difference is "
                  "not in the setback but in how much was already burning. "
                  "What you absorb depends on what you stocked.",
             "eg": "One public criticism costs one person three months and "
                   "another an afternoon of rewriting. The gap was built "
                   "earlier."},
            {"n": "The conversion has to name an action",
             "d": "Turn adversity into fuel is a slogan until it produces a "
                  "next step. His use is concrete. This thing has blocked "
                  "one route, so ask what it exposed, what it freed up, and "
                  "whose real attitude it just showed. All three questions "
                  "have specific answers.",
             "eg": "Losing the biggest account exposed a hole in renewals, "
                   "freed the delivery team it monopolised, and showed who "
                   "in the building actually cared."},
        ],
        "q": [
            "The impediment to action advances action. What stands in the "
            "way becomes the way.",
            "A fire makes flame and brightness out of everything thrown into "
            "it.",
            "The obstacle is not removed. It is burned.",
        ],
        "apply":
            "Where you are: something you planned has been shut down by "
            "something outside you.\n"
            "Ask first: is it the goal that has been blocked, or only the "
            "route you chose for it?\n"
            "Where it goes wrong: reading a route failure as a goal failure; "
            "or saying this is an opportunity and then producing no next "
            "step.",
    },
    {
        "k": "view-from-above",
        "n": "The view from above",
        "w": "Pull the scale back",
        "src": "Meditations, Books 6, 9 and 12",
        "dek": "A year from now most of this will be gone from memory. The "
               "exercise is how to borrow that later view now.",
        "story":
            "He runs the same drill over and over: pull the eye back until "
            "the thing in front of him is small. ==Asia and Europe are "
            "corners of the universe, he writes, and the whole ocean a "
            "drop.== He reminds himself that the men with the loudest names "
            "are long gone, and so are the people who remembered them. This "
            "is not nihilism, it is calibration. He was the emperor. "
            "Everything on his desk was described to him as gravely "
            "important, and he needed a ruler that could tell him which ones "
            "really were.",
        "f": [
            {"n": "Urgency is mostly proximity",
             "d": "A thing looks enormous largely because it is close. "
                  "Stretch the timescale to a year or five and nearly "
                  "everything currently costing you sleep shrinks to its "
                  "right size. The two or three that do not shrink are the "
                  "ones worth the whole week.",
             "eg": "Re-sort this week's list by will anyone remember this in "
                   "a year. Two of your top three usually move."},
            {"n": "Pulling back is not opting out",
             "d": "The point of the wide view is to allocate attention, not "
                  "to cancel action. He kept governing and went to the front "
                  "in person. The exercise hands out weights, not excuses, "
                  "and using it to prove that nothing matters is using it "
                  "backwards.",
             "eg": "In the long run none of it matters is escape. This gets "
                   "thirty minutes, not three hours, is allocation."},
            {"n": "Use the same ruler on people",
             "d": "He turns it on whoever has just offended him: in a few "
                  "decades that person is gone and so are you. It does not "
                  "delete the offence. It lowers the volume of the response, "
                  "and the response is usually where the actual damage comes "
                  "from.",
             "eg": "Being contradicted in a meeting costs far less than "
                   "firing back does. Widen the frame and you will wait."},
        ],
        "q": [
            "Asia and Europe are corners of the universe; the ocean, a drop.",
            "Not the thing disturbs you, but your judgement about it.",
            "Everything you are looking at is already changing.",
        ],
        "apply":
            "Where you are: one thing has taken over and you cannot work on "
            "anything else.\n"
            "Ask first: will this still be on my list a year from now?\n"
            "Where it goes wrong: using the long view to argue that nothing "
            "needs doing; or widening the frame for events and never for the "
            "person who offended you.",
    },
    {
        "k": "morning-preparation",
        "n": "The morning rehearsal",
        "w": "Go through the people you will meet today",
        "src": "Meditations, Book 2",
        "dek": "Book Two opens with a preparation, not a reflection. The "
               "claim is that offence you expected does about half the "
               "damage.",
        "story":
            "The first line of Book Two is a script to be said on waking: "
            "==today I shall meet with the busybody, the ungrateful, the "
            "arrogant, the deceitful, the envious, the unsocial.== Then the "
            "reasoning. They are like this because they cannot tell good "
            "from harm; I can, so they cannot injure me and I will not be "
            "angry with them, since we were made to work together, like "
            "hands, like feet, like the two rows of teeth. It is a daily "
            "rehearsal, not a one-off complaint.",
        "f": [
            {"n": "Expected offence lands at half strength",
             "d": "Most of the force in anger comes from surprise rather "
                  "than from the event. Walk through the difficult turns the "
                  "day may take, and when one arrives you are in of course "
                  "rather than in how dare they. That gap is where a choice "
                  "about the response fits.",
             "eg": "Before the negotiation, write the three hardest things "
                   "they could raise. Then you are answering, not reeling."},
            {"n": "Rehearse your own move, not their behaviour",
             "d": "You cannot make the other person easier. The whole "
                  "preparation lands on your side of the table: how I intend "
                  "to answer, when I do not answer at all, where the line "
                  "is. Turned into a list of grievances about them, it does "
                  "the opposite of its job.",
             "eg": "He will dodge the blame again is useless. When he does, "
                   "I state the facts and do not defend is usable."},
            {"n": "Assume they do not know, not that they are bad",
             "d": "His attribution is ignorance, not malice. The practical "
                  "value is that ignorance and conflicting interests are "
                  "both things you can work on, whereas once you decide the "
                  "other person is bad the only move left is to fight him.",
             "eg": "If a colleague keeps crossing a line, assume he cannot "
                   "see it and say where it is. Then judge."},
        ],
        "q": [
            "Today I shall meet the busybody, the ungrateful, the arrogant, "
            "the deceitful.",
            "They are like this because they cannot tell good from harm.",
            "We were made to work together, like the two rows of teeth.",
        ],
        "apply":
            "Where you are: there is a meeting today that you already expect "
            "to go badly.\n"
            "Ask first: what is he most likely to do, and what exactly do I "
            "intend to do at that moment?\n"
            "Where it goes wrong: writing the rehearsal as a list of "
            "complaints about them; or starting from malice, which leaves "
            "only one move available.",
    },
]

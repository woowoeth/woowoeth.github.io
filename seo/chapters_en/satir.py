# -*- coding: utf-8 -*-
"""Virginia Satir — English.

She is remembered in English mostly as a warm presence with a set of exercises,
which is why the sharp part gets missed. Both of her instruments are diagnostic:
one tells you which layer an argument is actually happening on, the other tells
you which of four automatic postures the two of you have fallen into.
"""

PARENT = {
    "name": "Virginia Satir",
    "slug": "satir",
    "blurb": "Deep read",
    "items": [
        {"k": "iceberg", "n": "The iceberg: layers under the act",
         "w": "The fight is happening on the surface", "ready": True,
         "line": "Under the anger is disappointment, under that an expectation"},
        {"k": "coping-stances", "n": "Four stances under pressure",
         "w": "Placate, blame, compute, distract", "ready": True,
         "line": "All four are ways of not being in the room"},
    ],
}

CHAPTERS = [
    {
        "k": "iceberg",
        "n": "The iceberg: layers under the act",
        "w": "The fight is happening on the surface",
        "src": "The Satir model",
        "dek": "The same argument for ten years and no movement. The reason "
               "is that it is being had on the wrong layer.",
        "story":
            "Satir splits a person into the behaviour above the waterline "
            "and, below it, feelings, perceptions, expectations, yearnings "
            "and the self. Conflict happens almost entirely on the surface "
            "and is settled underneath: his anger is behaviour, under it sits "
            "disappointment, and under that sits I want to be treated as "
            "though I matter. Argue about who is right at the surface and it "
            "never ends, because the sentence at the surface was never the "
            "point. ==The problem is not the problem; coping is the "
            "problem== is her own summary of the whole method.",
        "f": [
            {"n": "Look for the expectation under the words",
             "d": "A partner complains that you come home late. On the face "
                  "of it this is scheduling; underneath it is usually where "
                  "do I rank in this house. Answer the face of it and you are "
                  "in an argument about calendars. Answer the expectation and "
                  "the conversation turns.",
             "eg": "All you care about is work does not want the reply that "
                   "is not true. It wants: have you been feeling left behind "
                   "lately?"},
            {"n": "Under the feeling there is a reading",
             "d": "Many people think naming the feeling is the end of the "
                  "work, but feelings are produced by readings. The same late "
                  "arrival, read as he does not care about me and read as he "
                  "is flat out today, makes two different feelings. What "
                  "often needs changing is the reading.",
             "eg": "A remark that ruined your whole day: ask what you took it "
                   "to mean, and whether a second reading also fits the same "
                   "facts."},
            {"n": "The yearning layer is common ground",
             "d": "The further down you go the more alike people are: to be "
                  "loved, accepted, of some worth. Two people locked in "
                  "opposition at the surface usually want the same thing "
                  "three layers down. Seeing that layer takes the hostility "
                  "out of a room faster than any argument.",
             "eg": "Parents pushing marriage and a child refusing look like "
                   "enemies. Below: I want your life to go well, and I want "
                   "to be treated as an adult."},
        ],
        "q": [
            "The problem is not the problem; coping is the problem.",
            "The conflict is on the surface. The solution is underneath.",
            "Further down we are alike: loved, accepted, worth something.",
        ],
        "apply":
            "Where you are: the same argument keeps coming back and reasoning "
            "does not touch it.\n"
            "Ask first: what feeling sits under that sentence, and what "
            "expectation sits under the feeling? Which layer am I answering?\n"
            "Where it goes wrong: using the iceberg to analyse the other "
            "person. What you really want is attention is a verdict, not "
            "understanding.",
    },
    {
        "k": "coping-stances",
        "n": "Four stances under pressure",
        "w": "Placate, blame, compute, distract",
        "src": "Satir on communication stances",
        "dek": "In a fight people turn into somebody else. This is the list "
               "of who they turn into.",
        "story":
            "==Under pressure, Satir found, people fall back into placating, "
            "blaming, being super-reasonable or distracting.== Placating "
            "gives up the self, blaming gives up the other, super-reasonable "
            "gives up both and keeps the logic, distracting gives up the "
            "subject. All four are automatic and all four avoid what is "
            "actually happening. She proposed a fifth, congruence, holding "
            "self, other and situation at once, and insisted it is trained "
            "rather than inherited. She would also stand a family up as a "
            "sculpture: who is near whom, who has their back turned. Set it "
            "up, she said, and everyone sees it at once.",
        "f": [
            {"n": "The stances set each other off",
             "d": "Blaming usually pulls placating or super-reasonable out of "
                  "the other person; distracting pulls harder blame. So "
                  "escalation is not a question of who went too far, it is "
                  "two stances locking together. Reading the pair is more use "
                  "than establishing who started.",
             "eg": "The more carefully you set out the logic, the louder he "
                   "gets: that is super-reasonable meeting blame, and neither "
                   "of you is in the room."},
            {"n": "Placating has the best-hidden bill",
             "d": "Placating costs least in the moment, which is why it so "
                  "often passes for maturity. What it does is take your own "
                  "needs out of the account, and the account gets settled "
                  "somewhere else: in a sudden detonation, or in years of "
                  "quiet distance.",
             "eg": "Fine, whatever you want, for years, and then one small "
                   "thing sets off the whole backlog, and the other person "
                   "genuinely cannot see where it came from."},
            {"n": "Congruence is not saying whatever you feel",
             "d": "Congruence holds three things together: what I feel, where "
                  "the other person is, and what this occasion is. Drop any "
                  "one and it is not congruence. Only yourself is venting, "
                  "only the other is placating, only the occasion is being "
                  "super-reasonable.",
             "eg": "Contradicted by a junior colleague in public, the "
                   "congruent move is neither crushing it there nor "
                   "pretending it did not happen, but saying your piece to "
                   "him afterwards."},
        ],
        "q": [
            "Under pressure people placate, blame, go super-reasonable, or "
            "distract.",
            "Congruence holds three things: myself, the other person, the "
            "situation.",
            "A family's real structure cannot be said. Stand it up and "
            "everyone sees.",
        ],
        "apply":
            "Where you are: the conflict starts and both of you turn into "
            "somebody else.\n"
            "Ask first: which stance did I fall back into? Which one is he "
            "in? Are the two of them setting each other off?\n"
            "Where it goes wrong: using the four as labels for people. You "
            "are just a blamer is itself blaming.",
    },
]

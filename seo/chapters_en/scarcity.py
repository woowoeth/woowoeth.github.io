# -*- coding: utf-8 -*-
"""Scarcity — English.

The English reader has usually met this book as the IQ-points headline, and
that specific number is the part that has been contested since. So the page
keeps the mechanism and drops the figure: what scarcity does to attention,
why money trouble and time trouble draw on the same account, and what
follows from that for design rather than for self-blame.
"""

PARENT = {
    "name": "Scarcity",
    "slug": "scarcity",
    "blurb": "Deep read",
    "items": [
        {"k": "bandwidth-tax", "n": "The bandwidth tax",
         "w": "Every shortage takes the same mind", "ready": True,
         "line": "Not irrational — the bandwidth is already occupied"},
        {"k": "tunneling", "n": "Tunnelling",
         "w": "The urgent crowds out the important", "ready": True,
         "line": "The narrowing is not a flaw, it is what scarcity produces"},
    ],
}

CHAPTERS = [
    {
        "k": "bandwidth-tax",
        "n": "The bandwidth tax",
        "w": "Every shortage takes the same mind",
        "src": "Mullainathan and Shafir, Scarcity (2013); the Indian "
               "sugarcane study",
        "dek": "People short of money get called short-sighted. This piece "
               "asks whether that is a character trait or a description of "
               "the situation.",
        "story":
            "They tested Indian sugarcane farmers twice: the same men before "
            "the harvest, when money was tight, and after it, when the money "
            "had arrived. The same person scored differently on the same "
            "cognitive tests. They call it the bandwidth tax — scarcity "
            "captures the mind, and what it captures is not available for "
            "anything else. ==So being short-sighted may be a consequence of "
            "having no money rather than the cause of it.== The size of that "
            "effect has been contested since. This piece takes the direction "
            "and leaves the number alone.",
        "f": [
            {"n": "One bandwidth, and both shortages draw on it",
             "d": "This is the model's most useful move: it folds two "
                  "apparently unrelated troubles into one. Doing the month's "
                  "arithmetic and racing a deadline draw on the same "
                  "attention, which is why the two arriving together are so "
                  "much worse than either alone. Not weak will. Bandwidth "
                  "pulled from both ends.",
             "eg": "Working out how far short this month is while finishing a "
                   "proposal, and doing both badly. That is not laziness."},
            {"n": "The test is whether he does it when things are loose",
             "d": "Swapping a character explanation for a situational one "
                  "needs something you can check. The sugarcane study is "
                  "strong precisely because it compares one group of men at "
                  "two moments, instead of comparing poor people with rich "
                  "ones.",
             "eg": "A mistake that stops happening after the harvest does not "
                   "belong on that man's personality."},
            {"n": "The conclusion is for institutions, not for self-blame",
             "d": "The real use of this model is in design: take away things "
                  "a stretched person has to remember, forms to fill in, "
                  "decisions to make. That beats telling him to think more "
                  "clearly. Turned on yourself it is a reminder, not an "
                  "amnesty.",
             "eg": "Setting the repayment to leave the account automatically "
                   "beats reminding yourself every month not to forget it."},
        ],
        "q": [
            "Scarcity captures the mind.",
            "Being short of money and short of time draw on one bandwidth.",
            "This model is built for designing systems, not for blaming "
            "yourself.",
        ],
        "apply":
            "Where you are: money or time is tight, and you keep making "
            "decisions that look stupid a week later.\n"
            "Ask first: would I make these mistakes when things were loose? "
            "If not, stop trying to fix your character and start removing "
            "things that occupy the bandwidth.\n"
            "Where it goes wrong: using it as an amnesty for every lapse; or "
            "turning it outward to label somebody else. It explains a "
            "situation, it does not classify a person.",
    },
    {
        "k": "tunneling",
        "n": "Tunnelling",
        "w": "The urgent crowds out the important",
        "src": "Scarcity: the twin concepts of tunneling and slack",
        "dek": "The busier you get, the less the important things get done. "
               "This piece argues that is a mechanism rather than bad "
               "planning.",
        "story":
            "Scarcity narrows attention, and the narrowing has a name: "
            "==tunneling==. The most urgent thing is lit brilliantly, and "
            "everything outside the tunnel — the check-up, the insurance, the "
            "repayment plan, the call you owe somebody — goes dark. It is not "
            "purely a loss; focus inside the tunnel genuinely rescues the "
            "emergency. The cost simply lands outside it, and lands late. "
            "Their companion idea is slack: with slack, one small accident "
            "stays one small accident. Without it, the same accident "
            "capsizes you.",
        "f": [
            {"n": "The efficiency inside the tunnel is real, and so is the "
                  "bill",
             "d": "People genuinely work faster and sharper near a deadline. "
                  "That speed is borrowed: it is drawn from attention that "
                  "belonged outside the tunnel, and the loan comes due in "
                  "weeks or in years. Run it as a normal operating mode and "
                  "every quarter goes on clearing the last one.",
             "eg": "The output a deadline forces out of you usually costs a "
                   "stretch with no check-ups, no replies and no long-term "
                   "decisions taken at all."},
            {"n": "Slack is not waste, it is room to be wrong",
             "d": "Filling the calendar and the account to the last unit "
                  "looks like maximum efficiency. It is actually setting your "
                  "tolerance for error to zero. With room, one surprise stays "
                  "one surprise. Without it the same surprise chains: "
                  "borrowing, penalties, the real work missed.",
             "eg": "An emergency fund you are not allowed to touch is not "
                   "there for the return. It is there so that one accident "
                   "does not turn into five."},
            {"n": "You fix a tunnel with structure, not with reminders",
             "d": "Reminders fail inside the tunnel, because you did not "
                  "forget — at that moment you could not see it. What works "
                  "is moving the important thing somewhere that needs no "
                  "attention: the automatic payment, the appointment already "
                  "booked, the schedule somebody else watches for you.",
             "eg": "A check-up already booked and already paid for is more "
                   "reliable than intending to arrange one when things calm "
                   "down."},
        ],
        "q": [
            "The urgent is lit up; everything outside the tunnel goes dark.",
            "Slack is not waste. It is room to be wrong.",
            "The same mistake costs the poorer side far more.",
        ],
        "apply":
            "Where you are: everything lately is firefighting, and nothing "
            "important but unurgent has moved at all.\n"
            "Ask first: which of the things being squeezed out becomes the "
            "next fire if it waits? Move that one into a form that does not "
            "need you to remember it.\n"
            "Where it goes wrong: using tunnelling as a reason not to plan; "
            "or building so much slack that you stop putting out the fire "
            "actually in front of you.",
    },
]

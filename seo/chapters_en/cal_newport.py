# -*- coding: utf-8 -*-
"""Cal Newport — English.

Deep Work is usually remembered as advice about turning off notifications,
which makes it sound like a matter of self-discipline. Newport's actual
claim is the opposite: relying on self-discipline in an interruptible
environment is a design failure, and the two working parts of the book are
a cost you cannot feel and a block you have to take rather than wait for.
"""

PARENT = {
    "name": "Cal Newport",
    "slug": "cal-newport",
    "blurb": "Deep read",
    "items": [
        {"k": "attention-residue", "n": "Attention Residue",
         "w": "The cost is not those few minutes", "ready": True,
         "line": "You answered one message, and the next half hour is "
                 "discounted"},
        {"k": "schedule-the-depth", "n": "Book the Block",
         "w": "The gap will not appear on its own", "ready": True,
         "line": "Put the deep hours in the diary the way a meeting goes in"},
    ],
}

CHAPTERS = [
    {
        "k": "attention-residue",
        "n": "Attention Residue",
        "w": "The cost is not those few minutes",
        "src": "Deep Work, chapter two",
        "dek": "What one quick look actually costs. How the account should be "
               "worked out.",
        "story":
            "Newport gives a counter-example: a manager who required the team "
            "to be reachable at all times. They looked extremely productive, "
            "messages answered instantly, meetings back to back, and after a "
            "year they had produced nothing that required sustained thought. "
            "The mechanism he names is ==attention residue==: after you "
            "switch tasks, part of your attention is still hooked on the last "
            "one and needs time to move across. So the real cost of the "
            "interruption is not the five minutes, it is the poor half hour "
            "that follows, and that part is nearly invisible, because when "
            "you return to the work you feel focused.",
        "f": [
            {"n": "The loss happens where you cannot see it",
             "d": "The feeling of concentration and the quality of the "
                  "thinking are not the same thing. After a switch you "
                  "register immediately that you are back, while the drop in "
                  "output only shows up afterwards. That is why the price of "
                  "one quick look is systematically underestimated.",
             "eg": "Answer a message midway through a proposal and the next "
                   "twenty minutes of writing usually need rewriting when you "
                   "read it the next day."},
            {"n": "Fragments do not add up to a block",
             "d": "Four fifteens are not an hour, because each one pays the "
                  "switching cost again and deep thinking needs a climb. It "
                  "explains why someone whose diary is cut up by meetings "
                  "cannot produce work requiring continuity even when the "
                  "total hours are there.",
             "eg": "The forty minutes between two meetings is hard to think "
                   "in. Most people can only spend it on small chores."},
            {"n": "Always available is a default, not a requirement",
             "d": "Most demands for an instant reply have never actually been "
                  "tested. Newport suggests treating response time as a "
                  "negotiable parameter: state your rhythm plainly, and in "
                  "most settings the other side is entirely fine with it.",
             "eg": "Put I do not read messages before noon and reply in one "
                   "batch in the afternoon in your signature. Far fewer "
                   "people object than you expect."},
        ],
        "q": [
            "Attention residue keeps you off full speed long after you "
            "switch.",
            "Deep work is becoming rare exactly as it becomes valuable.",
            "Four fifteen-minute pieces do not make an hour.",
        ],
        "apply":
            "Where you are: the day was full and nothing that needed thinking "
            "moved.\n"
            "Ask first: was there a stretch of more than ninety minutes today "
            "with no interruption? If not, who cut it up?\n"
            "Where it goes wrong: using it as a reason to refuse to "
            "collaborate. Deep work is for the tasks that need depth, which "
            "is not all of them.",
    },
    {
        "k": "schedule-the-depth",
        "n": "Book the Block",
        "w": "The gap will not appear on its own",
        "src": "Deep Work, part three",
        "dek": "The thing you will do when you have time never starts. How to "
               "take the time instead.",
        "story":
            "Newport's central operational advice is to schedule deep work "
            "the way you schedule a meeting: in the diary, announced to other "
            "people, entered when the time comes, rather than waited for. The "
            "reason is blunt. ==A gap never appears by itself==, and shallow "
            "work expands like a gas to fill whatever space is available. He "
            "also argues for capping shallow work and handling it in batches, "
            "so what remains can join up into blocks. None of it relies on "
            "willpower: holding attention by self-control in a place where "
            "anyone can interrupt you is a design failure.",
        "f": [
            {"n": "Taking the time works better than managing the will",
             "d": "Self-control is consumable; a diary is not. Fix the deep "
                  "block the way a meeting is fixed and you no longer have to "
                  "make the decision about whether to concentrate today. "
                  "Making that decision is itself what wears people out.",
             "eg": "Marking two hours each morning as unbookable is more "
                   "reliable than asking yourself every morning when you will "
                   "write."},
            {"n": "Cap the shallow work; do not try to abolish it",
             "d": "Mail, coordination and meetings are necessary and they "
                  "build no new capability. Newport does not propose removing "
                  "them. He proposes a ceiling and a fixed slot: the total is "
                  "unchanged, and the block survives.",
             "eg": "Handle mail at ten in the morning and four in the "
                   "afternoon rather than whenever it lands."},
            {"n": "Boredom is trained",
             "d": "If every gap gets filled with a phone, the brain grows "
                  "used to a constant supply of novelty, and anything "
                  "demanding a long sit afterwards becomes unusually painful. "
                  "So part of training attention is letting yourself be "
                  "bored.",
             "eg": "Two minutes waiting for the lift with the phone in your "
                   "pocket. Small moments like that decide whether you can "
                   "sit an hour."},
        ],
        "q": [
            "A gap never appears by itself. You have to schedule it.",
            "Fill every gap with stimulation and you lose the ability to "
            "concentrate.",
            "You have a finite amount of willpower that becomes depleted as "
            "you use it.",
        ],
        "apply":
            "Where you are: the important and non-urgent thing never gets "
            "in.\n"
            "Ask first: does it have a slot in my diary? If not, what exactly "
            "is the gap I am waiting for going to arrive from?\n"
            "Where it goes wrong: filling the diary with deep blocks and "
            "executing none of them. Hold one, do it, then add.",
    },
]

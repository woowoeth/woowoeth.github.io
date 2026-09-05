# -*- coding: utf-8 -*-
"""Xunzi — English.

The English reader arrives, if at all, with one line: human nature is evil.
It is a bad translation of a claim about engineering, and it makes him sound
like a moralist when he is the opposite. The job of this page is to put the
claim back where he made it — rules come from scarcity, groups come from
division, and the sky is a shared input that explains nothing.
"""

PARENT = {
    "name": "Xunzi",
    "slug": "xunzi",
    "blurb": "Deep read",
    "items": [
        {"k": "origin-of-rites", "n": "Where the rules came from",
         "w": "Scarcity wrote them, not virtue", "ready": True,
         "line": "Not morality first and then rules. It runs the other way"},
        {"k": "borrow-from-things", "n": "Borrow the horse, don't grow legs",
         "w": "Leverage beats effort", "ready": True,
         "line": "The one who got further borrowed something. He did not grow legs"},
        {"k": "division-makes-groups", "n": "A group is a set of clear lines",
         "w": "Headcount without division is a crowd", "ready": True,
         "line": "A team with no lines drawn will come apart on its own"},
        {"k": "constant-heaven", "n": "Heaven runs to its own schedule",
         "w": "Sort the fixed from the movable", "ready": True,
         "line": "The sky is a shared input. It cannot explain the difference"},
    ],
}

CHAPTERS = [
    {
        "k": "origin-of-rites",
        "n": "Where the rules came from",
        "w": "Scarcity wrote them, not virtue",
        "src": "Xunzi, Discourse on Ritual; Human Nature is Bad",
        "dek": "Rules feel like morality handed down. His answer names no "
               "morality at all: only wants, shortage, and no line drawn.",
        "story":
            "The Discourse on Ritual opens with a question and answers it in "
            "one breath: where do rites come from? ==People are born with "
            "wants; wanting and not getting, they cannot help seeking; "
            "seeking without measure or division, they cannot help "
            "fighting.== Fighting brings disorder, disorder brings poverty. "
            "The former kings hated the disorder, so they set out rites to "
            "draw the lines — to feed the wants and supply the seeking, so "
            "that wants and goods grow up supporting each other. Nowhere in "
            "the chain does anyone turn bad.",
        "f": [
            {"n": "The fight is in the missing line, not in the person",
             "d": "Blaming someone's character is the cheapest diagnosis "
                  "available and the least useful one. His diagnosis is "
                  "seeking without measure or division: nobody drew the "
                  "boundary. Replace the people and the same argument arrives "
                  "with the new ones.",
             "eg": "Two teams have fought over the same budget for a year. "
                   "Write down who gets it under which conditions and the "
                   "fighting stops that week."},
            {"n": "Rites feed the want; they do not forbid it",
             "d": "Rites exist to feed the wants and supply the seeking. "
                  "Desire is treated as legitimate and given a channel, not a "
                  "fence. A rule that only makes the wanted thing harder to "
                  "reach gets routed around; a rule that makes the honest "
                  "route the fast one gets used.",
             "eg": "An expenses policy that only makes spending difficult "
                   "gets bypassed. One that makes compliant spending fast and "
                   "legible gets followed without anyone being told twice."},
            {"n": "Deliberate effort, not hypocrisy",
             "d": "Human nature is bad; what is good in people is deliberate "
                  "effort. The word usually translated as artifice means "
                  "made, worked, put there on purpose. Cooperative order is "
                  "not native to anyone. That cancels the expectation of "
                  "self-motivation and hands the job back to whoever designs "
                  "the rules.",
             "eg": "Complaining that nobody takes ownership is waiting for "
                   "something innate. The real question is what behaviour the "
                   "current incentives are actually manufacturing."},
        ],
        "q": [
            "People are born with wants, and wanting without division ends in "
            "fighting.",
            "Rites were made to feed the wants and supply the seeking.",
            "Human nature is bad; what is good in people is deliberate effort.",
        ],
        "apply":
            "Where you are: the same conflict keeps coming back and you have "
            "already changed the people.\n"
            "Ask first: is there a written division of this boundary that "
            "both sides have read?\n"
            "Where it goes wrong: treating a boundary problem as a character "
            "problem; designing rules that only make things harder instead of "
            "making the right route smooth.",
    },
    {
        "k": "borrow-from-things",
        "n": "Borrow the horse, don't grow legs",
        "w": "Leverage beats effort",
        "src": "Xunzi, An Exhortation to Learning",
        "dek": "Two people of equal ability, and one of them gets much "
               "further. He says the difference is not in the person.",
        "story":
            "The chapter on learning stops midway for an oddly practical "
            "observation. A man who borrows a horse and carriage has not "
            "grown faster feet, yet he reaches a thousand li; a man who "
            "borrows a boat and oars cannot swim, yet he crosses rivers. The "
            "conclusion: ==the gentleman is not different by birth; he is "
            "good at borrowing from things.== The whole chapter is called An "
            "Exhortation to Learning and lands almost entirely on tools, "
            "surroundings and accumulation. Talent is barely mentioned.",
        "f": [
            {"n": "Look for the lever before you look for more effort",
             "d": "Native ability improves slowly and tools improve in steps. "
                  "So the first response to work that will not move should be "
                  "what can I borrow, not I must try harder. Borrowing a "
                  "horse does not make the feet quicker; it still covers the "
                  "thousand li.",
             "eg": "Checking three thousand rows by hand takes two days; a "
                   "short script takes twenty minutes. The person working "
                   "until midnight moved his effort before he moved his "
                   "tools."},
            {"n": "Your surroundings are the strongest tool you own",
             "d": "Mugwort growing in a hemp field stands straight without "
                  "being tied. Environment is the most powerful instrument "
                  "available because it works every hour and costs no "
                  "willpower. Choosing the setting is far cheaper than "
                  "disciplining yourself inside a bad one.",
             "eg": "Putting the phone in another room beats reminding "
                   "yourself not to reach for it. One changes the "
                   "surroundings; the other spends will you need elsewhere."},
            {"n": "Accumulation is the cheapest leverage there is",
             "d": "Without piling up small steps you never reach a thousand "
                  "li. He sets the thoroughbred against the nag: a fine horse "
                  "cannot clear ten paces in one leap, a poor one pulling for "
                  "ten days arrives. Talent sets the single output; "
                  "persistence sets the total.",
             "eg": "Three hundred words a day is a hundred thousand in a "
                   "year. The person waiting for one inspired weekend usually "
                   "has nothing at all."},
        ],
        "q": [
            "The gentleman is not different by birth. He is good at borrowing.",
            "Borrowing a horse, his feet are no quicker, yet he arrives.",
            "A fine horse cannot leap ten paces; a nag walking ten days "
            "arrives.",
        ],
        "apply":
            "Where you are: you have worked hard at this and it still will "
            "not move.\n"
            "Ask first: what tool, whose experience, or which change of "
            "setting could carry part of it for you?\n"
            "Where it goes wrong: adding hours instead of finding leverage; "
            "fighting your surroundings with willpower rather than changing "
            "them.",
    },
    {
        "k": "division-makes-groups",
        "n": "A group is a set of clear lines",
        "w": "Headcount without division is a crowd",
        "src": "Xunzi, The Regulations of a King",
        "dek": "Slower than an ox and weaker than a tiger, people use both. "
               "The one-word answer he gives, and what follows from it.",
        "story":
            "In The Regulations of a King he asks why oxen and horses, "
            "stronger and faster than any man, end up in harness. ==Because "
            "people can form groups and they cannot.== Then the follow-up: "
            "how are people able to form groups? By division. And what makes "
            "division hold? A shared sense of what is right. He runs it out "
            "as a chain — divide and there is harmony, harmony makes one "
            "body, one body has strength, strength overcomes things. The "
            "fighting power of any organisation begins at how clearly the "
            "work is split.",
        "f": [
            {"n": "A group is not a number of people",
             "d": "Putting people together does not generate force on its "
                  "own. Divide and there is harmony; harmony makes one body; "
                  "only then is there strength. Where the division is "
                  "unclear, more people means more friction, and the added "
                  "force is negative.",
             "eg": "A project of ten with nobody named against each piece "
                   "often ships less than three did. The extra seven spend "
                   "their days confirming and waiting."},
            {"n": "The division needs a reason people accept",
             "d": "He says division holds by a shared sense of what is right "
                  "— meaning the split has to look defensible, not simply "
                  "reflect who pushed hardest. Without a stated basis, every "
                  "allocation is challenged again next quarter and the org "
                  "chart is decoration.",
             "eg": "Split resources by seniority or by results, either can "
                   "work. What cannot work is a split nobody can say the "
                   "reason for out loud."},
            {"n": "Name an owner for the gaps",
             "d": "The hard part of dividing work is never the core duties, "
                  "it is the border. Everyone competes for the centre and "
                  "everyone pushes away the edge. So the real task is "
                  "assigning the things that fall between two people to one "
                  "of them.",
             "eg": "Who follows a live incident after release? Engineering "
                   "says testing, testing says operations. That empty square "
                   "is why response time never comes down."},
        ],
        "q": [
            "People can form groups and animals cannot. How? By division.",
            "Divide and there is harmony; harmony makes one body; one body "
            "has strength.",
            "Everyone competes for the centre and everyone pushes away the "
            "edge.",
        ],
        "apply":
            "Where you are: you added people and the output did not follow.\n"
            "Ask first: is each new person's boundary written down, and who "
            "owns the things that fall between them?\n"
            "Where it goes wrong: throwing headcount at a coordination "
            "problem; dividing the core duties and leaving every gap "
            "unassigned.",
    },
    {
        "k": "constant-heaven",
        "n": "Heaven runs to its own schedule",
        "w": "Sort the fixed from the movable",
        "src": "Xunzi, Discourse on Heaven",
        "dek": "Bad year, bad market, bad luck. He closed this exit two "
               "thousand years ago, and not by denying the conditions.",
        "story":
            "The Discourse on Heaven opens hard: ==heaven's course is "
            "constant; it did not persist for the sage king Yao and it did "
            "not vanish for the tyrant Jie.== Nature does what it does "
            "regardless of who is on the throne. Respond to it with order and "
            "the result is good fortune; respond with disorder and the result "
            "is ruin. Then the famous line: rather than revering heaven and "
            "longing for it, why not master its workings and use them? He "
            "does not deny that outside conditions have force. He denies that "
            "they are an explanation.",
        "f": [
            {"n": "Constant means predictable, not unstoppable",
             "d": "Having a constant course means having a regularity. The "
                  "regularity will not listen to you, but precisely because "
                  "it is stable it can be used. Calling an outside condition "
                  "an act of God is usually a way of not having studied its "
                  "pattern.",
             "eg": "Industries have cycles, and that is the constant. Firms "
                   "that know it bank cash at the top and hire at the bottom; "
                   "firms that call it weather miss both ends."},
            {"n": "Same sky, different response",
             "d": "His contrast is blunt: respond with order and it goes "
                  "well, respond with disorder and it goes badly. Heaven did "
                  "not move; the response did. A post-mortem that stops at "
                  "the external condition has surrendered the only half that "
                  "was ever adjustable.",
             "eg": "Same year, same market: one company closes and another "
                   "takes share. A shared input cannot account for the "
                   "difference between them."},
            {"n": "Master it and use it",
             "d": "Rather than revering heaven and longing for it, master its "
                  "workings and use them. This is where he parts company with "
                  "everyone around him: attention moves from petition to "
                  "command of the mechanism. The posture is startlingly "
                  "modern and entirely practical.",
             "eg": "Instead of waiting for the rules to settle, work through "
                   "the part already settled and adjust to it. The waiters "
                   "watch; the users have the first move."},
        ],
        "q": [
            "Heaven's course did not persist for Yao nor vanish for Jie.",
            "Respond with order and it goes well; with disorder, badly.",
            "Rather than revering heaven, master its workings and use them.",
        ],
        "apply":
            "Where you are: the results are poor and the handiest explanation "
            "is the environment.\n"
            "Ask first: in that same environment, what did the one who did "
            "well do differently?\n"
            "Where it goes wrong: treating an external condition as an "
            "explanation rather than an input; refusing to study a pattern "
            "because you cannot change it.",
    },
]

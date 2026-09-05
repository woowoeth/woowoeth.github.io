# -*- coding: utf-8 -*-
"""Richard Feynman — English.

The English reader arrives with the Feynman Technique, a four-step study
hack sold on productivity blogs, usually attached to a sentence about
explaining things simply that does not appear anywhere in his writing.
What he actually left is harder and more useful: a rule about who the first
liar is, and a test he ran on himself and failed in public.
"""

PARENT = {
    "name": "Richard Feynman",
    "slug": "feynman",
    "blurb": "Deep read",
    "items": [
        {"k": "dont-fool-yourself", "n": "The first person not to fool is you",
         "w": "And you are the easiest one", "ready": True,
         "line": "The first principle is that you must not fool yourself"},
        {"k": "teach-to-understand",
         "n": "If you cannot teach it, you have not got it",
         "w": "Jargon is where the hole hides", "ready": True,
         "line": "Where you stall is where the understanding stops"},
    ],
}

CHAPTERS = [
    {
        "k": "dont-fool-yourself",
        "n": "The first person not to fool is you",
        "w": "And you are the easiest one",
        "src": "Caltech commencement address, 1974; Appendix F to the "
               "Challenger report, 1986",
        "dek": "He put this ahead of every method in science. This page is "
               "about why the first line of defence points inward.",
        "story":
            "At the 1974 Caltech commencement he gave the graduates one rule "
            "and called it the first principle: ==you must not fool yourself, "
            "and you are the easiest person to fool.== Twelve "
            "years later he sat on the Challenger commission, asked for a "
            "glass of ice water at a televised hearing, clamped a piece of "
            "the O-ring rubber, dropped it in for a few seconds and took it "
            "out. It did not spring back. NASA had hundreds of pages arguing "
            "the launch was sound. His appendix said reality must take "
            "precedence over public relations.",
        "f": [
            {"n": "The bias sits wherever your interest sits",
             "d": "Fooling yourself takes no dishonesty, only a stake. "
                  "Wherever you would prefer a conclusion, your efficiency at "
                  "finding supporting evidence rises sharply. So the check is "
                  "not how honest you feel. It is whether the answer pays "
                  "you.",
             "eg": "Positive evidence is unusually easy to find about the "
                   "project you sponsored. That is the moment to hand it to "
                   "somebody whose bonus does not depend on it."},
            {"n": "Write the disconfirming column first",
             "d": "The order changes the content. Write down what would show "
                  "you are wrong before you write the support, and both "
                  "columns come out more honest. Reverse it and you have "
                  "already chosen a side by the time the second column "
                  "starts.",
             "eg": "Put the falsifying evidence in the first column of the "
                   "review template. Same person, same week, same facts, "
                   "different conclusion."},
            {"n": "When the report and the world disagree, change the report",
             "d": "Challenger was not a shortage of engineering. It was an "
                  "organisation that preferred a document. This holds "
                  "anywhere there is a reporting line: if the reflex when "
                  "numbers look bad is to adjust the wording, the problem has "
                  "simply been forwarded.",
             "eg": "The metric missed. Ask whether you are revising the "
                   "conclusion or the phrasing. Revised phrasing clears this "
                   "review and is still there at the next one."},
        ],
        "q": [
            "The first principle is that you must not fool yourself.",
            "And you are the easiest person to fool.",
            "Reality must take precedence over public relations, for Nature "
            "cannot be fooled.",
        ],
        "apply":
            "Where you are: assessing something you have a stake in.\n"
            "Ask first: does this conclusion pay me? If it does, how hard "
            "have I actually looked for the evidence against it?\n"
            "Where it goes wrong: turning it into never concluding anything, "
            "or aiming the principle exclusively at other people.",
    },
    {
        "k": "teach-to-understand",
        "n": "If you cannot teach it, you have not got it",
        "w": "Jargon is where the hole hides",
        "src": "His teaching at Caltech, as recorded by David Goodstein",
        "dek": "The internet sells this as a study hack in four steps. This "
               "page is about the harder claim sitting underneath it.",
        "story":
            "David Goodstein once asked him to explain why spin one-half "
            "particles obey Fermi-Dirac statistics. Feynman sized up his "
            "listener and said he would prepare a freshman lecture on it. He "
            "came back a few days later. ==I couldn't reduce it to the "
            "freshman level, he said, and that means we don't really "
            "understand it.== The sentence everyone quotes about explaining "
            "things simply is not in his writing. What is documented is this, "
            "and the line found on his blackboard when he died: what I cannot "
            "create, I do not understand.",
        "f": [
            {"n": "Ban the jargon and the hole shows at once",
             "d": "A technical term is a compression, and compression only "
                  "works if both sides can unpack it. Forbid the term and you "
                  "have to unpack it yourself. Wherever you cannot, you were "
                  "storing a label rather than an understanding.",
             "eg": "Explain your job to someone at home. Every point where "
                   "you fall back on the trade word is a point you have not "
                   "thought through."},
            {"n": "Deriving it once beats memorising it ten times",
             "d": "A remembered conclusion works on the question it came "
                  "from. A derivation works on the whole class of questions, "
                  "because on the way through you collide with why it could "
                  "not have been otherwise. Those collisions are the "
                  "structure of understanding.",
             "eg": "Rather than memorising when the formula applies, work out "
                   "once where it comes from. After that the conditions are "
                   "obvious and need no memorising."},
            {"n": "Teaching is the test, not the favour",
             "d": "The usual reading is that explaining helps the listener. "
                  "His use runs the other way: he explained in order to find "
                  "out whether he knew. Which means the more ignorant the "
                  "audience, the better the instrument.",
             "eg": "A colleague silently repairs the steps you skipped. "
                   "Somebody outside the field stops dead at the first vague "
                   "sentence, which is the reading you wanted."},
        ],
        "q": [
            "I couldn't reduce it to the freshman level.",
            "That means we don't really understand it.",
            "What I cannot create, I do not understand.",
        ],
        "apply":
            "Where you are: you think you understand something and are not "
            "certain.\n"
            "Ask first: without one term of art, can you take an outsider to "
            "the point of nodding? Which sentences do you stall on?\n"
            "Where it goes wrong: confusing simple with shallow — what gets "
            "simplified is the telling, never the content.",
    },
]

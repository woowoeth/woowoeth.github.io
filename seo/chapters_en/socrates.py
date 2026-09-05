# -*- coding: utf-8 -*-
"""Socrates — English.

Two things arrive ahead of him: a poster saying he knew that he knew nothing,
and the Socratic method as a law-school interrogation or a coaching gimmick.
Neither is what the dialogues say. What he claims in the Apology is narrower
and much more usable, and the midwife passage in the Theaetetus has a second
half that the coaching version drops entirely.
"""

PARENT = {
    "name": "Socrates",
    "slug": "socrates",
    "blurb": "Deep read",
    "items": [
        {"k": "knowing-not-knowing", "n": "Not supposing that you know",
         "w": "The whole margin is that thin", "ready": True,
         "line": "He never claimed to know nothing, only not to suppose he "
                 "knew"},
        {"k": "midwifery", "n": "The midwife's trade",
         "w": "No answers, only delivery", "ready": True,
         "line": "An answer counts only if it came out of the other person"},
    ],
}

CHAPTERS = [
    {
        "k": "knowing-not-knowing",
        "n": "Not supposing that you know",
        "w": "The whole margin is that thin",
        "src": "Plato, Apology",
        "dek": "The poster says he knew that he knew nothing. This page is "
               "about the narrower and far more useful thing he said.",
        "story":
            "A friend asked the oracle at Delphi whether anybody was wiser "
            "than Socrates, and was told nobody was. Socrates did not believe "
            "it, so he went out to test it: politicians, poets, craftsmen, "
            "one after another, questioning each. The result came back the "
            "same every time. They supposed they knew things they did not. "
            "==I do not think I know what I do not know,== he says, and that "
            "thin margin is the whole of his advantage. He kept questioning "
            "until Athens executed him for it.",
        "f": [
            {"n": "His response to good news was to go and test it",
             "d": "He was handed a judgement flattering to himself and his "
                  "first move was to look for a counter-example rather than "
                  "to accept it. The habit is independent of content: the "
                  "more agreeable a conclusion, the earlier you should go "
                  "looking for what would break it.",
             "eg": "When the research comes back entirely positive, go and "
                   "find three people who left. Confirming cases are "
                   "unlimited; one counter-example saves half a year."},
            {"n": "Competence in one place leaks into confidence everywhere",
             "d": "He found the craftsmen genuinely expert, and precisely "
                  "because of it convinced they were wise about the greatest "
                  "matters too. Somebody whose judgement has been repeatedly "
                  "validated in one domain is the least able to say I do not "
                  "know in another.",
             "eg": "A founder whose technical calls are excellent rules on "
                   "pricing, contracts and hiring with identical confidence. "
                   "The record in the first is the risk in the rest."},
            {"n": "Examination is a procedure, not a posture",
             "d": "His examining had a fixed shape: make the other person "
                  "define the term they are using, then test that definition "
                  "against concrete cases. Modesty can be performed. A "
                  "procedure produces something every time, either a "
                  "definition that holds or a gap that opens.",
             "eg": "Are we confident about this is an attitude. Which three "
                   "assumptions is it resting on, and which is weakest, is "
                   "examination, and it always yields an answer."},
        ],
        "q": [
            "I do not think I know what I do not know.",
            "The unexamined life is not worth living.",
            "Good at their craft, they supposed themselves wise about "
            "everything.",
        ],
        "apply":
            "Where you are: about to give a confident verdict outside the "
            "field you are good at.\n"
            "Ask first: is the confidence coming from this question, or from "
            "your record somewhere else?\n"
            "Where it goes wrong: wearing modesty as a manner with no "
            "procedure attached, or examining only the conclusions you "
            "dislike.",
    },
    {
        "k": "midwifery",
        "n": "The midwife's trade",
        "w": "No answers, only delivery",
        "src": "Plato, Theaetetus",
        "dek": "His mother delivered babies and he said he had inherited the "
               "trade. This page is about why he withheld answers.",
        "story":
            "In the Theaetetus he explains his own method outright. ==My art "
            "of midwifery is in general like theirs, except that my patients "
            "are men, and my concern is with the soul in travail rather than "
            "the body.== The god compels him to act as midwife and never "
            "allows him to bring forth. The young men who come to him seem to "
            "know nothing at first and later produce a great deal, all of it "
            "found in themselves. He keeps the other half of the craft too: "
            "telling a real child from a wind-egg, and disposing of the false "
            "one.",
        "f": [
            {"n": "A given answer has no roots",
             "d": "Tell somebody the conclusion and they hold a sentence they "
                  "can repeat. Bring them to it by questions and they hold a "
                  "route they walked. The first gets dropped at the first "
                  "counter-example. The second gets defended, because it is "
                  "theirs.",
             "eg": "Point out the flaw and he fixes that one line. Ask three "
                   "questions until he sees the flaw and he fixes the two "
                   "others like it."},
            {"n": "Delivery is slower and harder than handing it over",
             "d": "The answer takes ten seconds; questioning somebody into "
                  "producing it can take an hour. The slowness buys a filter. "
                  "Only what is already forming in them can be delivered, and "
                  "if nothing comes, telling them would not have helped "
                  "either.",
             "eg": "What you have explained four times and they still cannot "
                   "do is rarely explained badly. There is nothing yet for it "
                   "to attach to. Let them hit the wall once, then explain."},
            {"n": "The false one has to be removed on the spot",
             "d": "The second half of the craft is judgement. What gets "
                  "produced is not automatically true, so he tests his "
                  "interlocutor's own conclusions against counter-examples "
                  "and throws out what fails. Delivery without inspection "
                  "manufactures confident error.",
             "eg": "Make whoever proposed the idea answer the three hardest "
                   "questions immediately. Drop what cannot stand, before it "
                   "acquires the protection of being the group's."},
        ],
        "q": [
            "My art of midwifery is in general like theirs.",
            "They have never learned anything from me.",
            "An answer counts only when it came out of the other person.",
        ],
        "apply":
            "Where you are: you can see the answer and are about to say it.\n"
            "Ask first: has he anything for this answer to attach to, and "
            "could three questions get him there himself?\n"
            "Where it goes wrong: turning questions into a guessing game with "
            "the answer already locked, or delivering without ever inspecting "
            "what came out.",
    },
]

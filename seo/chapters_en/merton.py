# -*- coding: utf-8 -*-
"""Robert K. Merton - English.

English readers meet Merton as a footnote: the man who happened to coin
"self-fulfilling prophecy" and "role model". These two chapters treat the
coinages as machinery rather than vocabulary - how a false belief builds the
evidence for itself, and why recognition is paid out on reputation already
held. Quoted lines are his own or the ones he quotes; the spelling inside
quotation marks is left exactly as printed.
"""

PARENT = {
    "name": "Robert K. Merton",
    "slug": "merton",
    "blurb": "Deep read",
    "items": [
        {"k": "self-fulfilling-prophecy", "n": "How a false story makes itself true",
         "w": "Suspicion manufactures the evidence for itself", "ready": True,
         "line": "First they guard themselves against you, then there is a reason to"},
        {"k": "matthew-effect", "n": "To every one that hath",
         "w": "Credit is paid on reputation, not on effort", "ready": True,
         "line": "The same contribution, two names, two very different memories"},
    ],
}

CHAPTERS = [
    {
        "k": "self-fulfilling-prophecy",
        "n": "How a false story makes itself true",
        "w": "Suspicion manufactures the evidence for itself",
        "src": "'The Self-Fulfilling Prophecy', The Antioch Review, Summer 1948; "
               "collected in Social Theory and Social Structure",
        "dek": "People have begun guarding themselves against you and explaining "
               "makes it worse. How the loop closes, and where it can be cut.",
        "story":
            "Merton invents a bank. It is Wednesday afternoon and the Last "
            "National Bank is sound: not much cash on hand, but every loan it "
            "holds is good. Then the lobby fills. Somebody says the word "
            "insolvent. The rumour travels, depositors queue to withdraw what "
            "they are owed, and by closing time a bank that could have paid "
            "everyone has failed. ==The statement was false when it was made "
            "and the actions it provoked made it true==. His own sentence for "
            "this: a false definition of the situation evoking a new behavior "
            "which makes the original false conception come true.",
        "f": [
            {"n": "The definition arrives before the fact",
             "d": "He opens with the Thomas theorem: if men define situations as "
                  "real, they are real in their consequences. A false reading "
                  "does not stay in anyone's head. It issues instructions, and "
                  "what people then do is entirely real.",
             "eg": "A rumour of redundancies, and the people with options leave "
                   "first, which is what finally sinks the place."},
            {"n": "Once the loop closes, the prophet is always right",
             "d": "Afterwards the person who said it points at the wreckage as "
                  "proof of foresight, and the pointing is hard to argue with, "
                  "because the wreckage is there. What nobody can see is that "
                  "the saying came first.",
             "eg": "The man who says he always knew she would fail is usually the "
                   "one who stopped giving her anything to do."},
            {"n": "Every move you have is already spoken for",
             "d": "The suspected person holds the worst position in the loop. "
                  "Working normally reads as cover, explaining reads as guilt, "
                  "silence reads as admission. The definition has assigned a "
                  "meaning to every action available to you in advance.",
             "eg": "Copying four people into every email to prove you are open "
                   "just looks like building a paper trail."},
            {"n": "What cuts it is not effort but a new definition",
             "d": "His conclusion is institutional, not personal: the loop runs "
                  "where nobody has deliberately built controls against it. Bank "
                  "runs did not end because depositors grew calm. They ended "
                  "when deposit insurance changed what queueing was worth.",
             "eg": "Rather than explaining again, put the numbers and the access "
                   "rights somewhere neither side has to trust the other."},
        ],
        "apply":
            "Where you are: a colleague is keeping something back from you, and "
            "you have not done the thing they are guarding against.\n"
            "Ask first: who said the sentence that put me here, and when - am I "
            "arguing with the sentence, or with the pile of reactions it "
            "produced?\n"
            "Where it goes wrong: using it to prove every suspicion of you is "
            "invented. He shows that false definitions can come true, not that "
            "all definitions are false.",
        "q": [
            "If men define situations as real, they are real in their consequences.",
            "The specious validity of the self-fulfilling prophecy perpetuates a reign of error.",
            "The false definition comes first. The facts that confirm it arrive later.",
            "What breaks the loop is a new definition, not a better explanation.",
        ],
    },
    {
        "k": "matthew-effect",
        "n": "To every one that hath",
        "w": "Credit is paid on reputation, not on effort",
        "src": "'The Matthew Effect in Science', Science, 5 January 1968; "
               "the sequel in Isis, 1988",
        "dek": "You did the work and another name is the one people kept. Why "
               "this is usually allocation rather than theft.",
        "story":
            "In the 1960s Merton's student Harriet Zuckerman interviewed "
            "American Nobel laureates one by one. They kept returning, "
            "uncomfortably, to the same thing: co-author a paper with someone "
            "obscure and almost all the credit lands on the famous name, even "
            "when the obscure one did more of the work. Merton gave the pattern "
            "a name from Matthew's gospel - for unto every one that hath shall "
            "be given. ==The extra portion is paid out on reputation, not on "
            "contribution==.",
        "f": [
            {"n": "The same contribution, two different names",
             "d": "His definition is cool about it: contributions by scientists "
                  "of standing collect extra recognition, and the same work by "
                  "someone who has not yet made a name has that recognition "
                  "withheld. The difference sits in the byline, not the work.",
             "eg": "One proposal is clear thinking under the director's name and "
                   "worth another pass under the new hire's."},
            {"n": "The forty-first chair",
             "d": "The French Academy seats forty. Merton used the forty-first "
                  "chair for those who plainly deserved a seat and never got "
                  "one - Descartes, Pascal, Moliere, Bayle, Rousseau, Saint-Simon, "
                  "Diderot, Stendhal, Flaubert, Zola, Proust. What excluded them "
                  "was the count, not the quality.",
             "eg": "Three awards exist. The gap between fourth and third is a "
                   "different kind of gap from fourth to tenth."},
            {"n": "A small lead grows itself",
             "d": "He later called it cumulative advantage. An early edge buys "
                  "better resources, better collaborators and more chances to be "
                  "seen, so the distance widens each round. Outsiders see only "
                  "the final distance and read all of it as talent.",
             "eg": "The first customer makes the second one easy. The first one "
                   "is the only hard one."},
            {"n": "He walked into it himself",
             "d": "The 1968 paper rests entirely on Zuckerman's interviews and "
                  "carries his name alone. Twenty years later, in the sequel, he "
                  "wrote the correction: it should have appeared under joint "
                  "authorship. The effect runs without anyone intending harm, "
                  "which is the point.",
             "eg": "Last time you said the team did it, did the room remember the "
                   "team or the person standing in front of it?"},
            {"n": "What you can change is where your name sits",
             "d": "If recognition is allocated on standing, the move is not to "
                  "fight over one instance of credit. It is to attach your name "
                  "early to a piece of work only you could have done, so that "
                  "people can reach you rather than the box you sit in.",
             "eg": "Write up the one debugging trail nobody else has, publish it, "
                   "and the next person with that problem finds you."},
        ],
        "apply":
            "Where you are: you did most of the work and the name that travelled "
            "out of the room was somebody else's.\n"
            "Ask first: do I want this instance of credit back, or do I want the "
            "next piece of work to arrive at me directly - because those are two "
            "different sets of moves.\n"
            "Where it goes wrong: reading it as proof that effort is pointless "
            "because fame decides everything. He measured how recognition is "
            "distributed, not whether the work was worth doing.",
        "q": [
            "For unto every one that hath shall be given, and he shall have abundance",
            "The extra portion is paid on reputation, not on contribution.",
            "The forty-first chair is not occupied by people who fell short.",
            "An early lead compounds; outsiders see only the final distance.",
        ],
    },
]

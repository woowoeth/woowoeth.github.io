# -*- coding: utf-8 -*-
"""Daily entry, day 30: Donald Winnicott.

Picked by fan-out. 'My kid stopped talking to me' (5 on the English side, 9 on
the Chinese), 'I can't stop pleasing people' (3) and 'Years in, nothing left
between us' were among the emptiest. Under the first hang Rogers, Gordon, Satir
and Bowlby: how to get him to open up, how to listen so that he does. Nobody
says the other half: that the closed door can be healthy, and that what a child
fears is not hiding but hiding and not being found.

His standing: a paediatrician for four decades and a founding figure of the
British object-relations school; 'good enough mother', 'transitional object',
'true and false self' and 'the capacity to be alone' are in every developmental
and psychoanalytic textbook. Recent entries were Xu Xiake, Yan Ying, Xiao He
(Chinese) and Porter, Keynes (foreign), so pick_balance is green.

Three scenes, no overlap: the entry is the threadbare blanket, chapter one is
hide-and-seek, chapter two the child who learns to read the adult's face,
chapter three the child building blocks with his mother reading. The only
verbatim quotation is the hide-and-seek line from 'Communicating and Not
Communicating' (1963). Everything else is our own rendering. All situations
already exist, so no SC_BOX.
"""

ENTRIES = [
    {
        "c": "Family and relationships",
        "n": "Donald Winnicott",
        "slug": "winnicott",
        "e": "Britain · 1896–1971",
        "w": "Good enough",
        "y": 1896,
        "d": "A British paediatrician who became a psychoanalyst. He worked "
             "in a London children's hospital for forty years, listening "
             "to mothers as much as examining their children, and during the "
             "war he spoke to ordinary mothers on the radio. His best-known "
             "terms, the good-enough mother, the transitional object, the "
             "true and false self, the capacity to be alone, all come from "
             "one observation: a child becomes himself next to a particular, "
             "imperfect person. He is often quoted as saying there is no "
             "such thing as a baby, meaning that wherever you find a baby you "
             "find someone caring for it. This page takes only his account "
             "of how a person becomes herself in someone else's company, and "
             "leaves out his clinical stages of infancy.",
        "story": "In the clinic he saw one scene over and over: a "
                 "two-year-old gripping a filthy, threadbare blanket and "
                 "refusing to put it down even in the consulting room. The "
                 "grown-ups wanted to wash it, and the child crumpled in "
                 "tears. Winnicott called it a transitional object, the "
                 "first possession that is neither me nor mother, and held "
                 "that it carries the child across to being alone. His advice "
                 "was plain: do not wash it, at least not before the child "
                 "is ready. To you it is a rag. To the child it holds all of "
                 "his sense of safety.",
        "f": [
            {"n": "Good enough is not second best; it fails by degrees",
             "d": "His good-enough mother starts out adapting almost completely to the baby, then fails a little at a time, within what the child can bear. Those small failures are how a child learns to wait, and learns that the world does not revolve around him. Perfect care would not raise someone who can face disappointment.",
             "eg": "Your child wants you to look at his drawing this second, and you are cooking. You say 'when I turn off the heat.' He waits a minute and learns that he matters and so does everything else."},
            {"n": "The old blanket is a bridge",
             "d": "The child chooses the transitional object, and nobody else can replace it. It is old and dirty because he never lets go of it, and washing out its smell cuts something in his experience. Your job is to recognise how much it matters and carry it along.",
             "eg": "Going on a long trip, pack the worn rabbit before any of the new toys."},
            {"n": "Holding: take all of it and do not change your face",
             "d": "He used 'holding' for a carer who takes everything the child does, the crying, the rage, the mess, steadily in her hands, without flinching or turning cold. A child who has been held dares to hand over the parts of himself that are not pretty, because it has not made anyone leave.",
             "eg": "He is so angry he throws a cup. Stop his hand, do not call him bad, and talk about the cup when he has calmed down."},
            {"n": "Look at the people around him before the child",
             "d": "'There is no such thing as a baby' means do not look at the child alone. How a child is doing is largely how he and his carer are doing together. Before changing him, ask whether the person looking after him is tired, whether she can bear it, and whether anyone is looking after her.",
             "eg": "The child has been unusually clingy for two weeks. Before correcting him, check whether someone at home has been worn out."},
        ],
        "apply": "Pick something you have lately felt a child, partner or "
                 "colleague was getting wrong. Write three lines: am I "
                 "helping him bear this, or removing it for him; am I "
                 "present in mind as well as in the room; have I walked "
                 "into the small patch he has just marked out for himself "
                 "because I could not stand not knowing. Then add one thing "
                 "for today that is presence without interference, such as "
                 "sitting beside him and asking nothing.",
        "q": ["Perfect care does not raise someone who can face disappointment.",
              "The blanket a child clutches is a bridge to being alone.",
              "To change the child, first ask who is holding him up."],
        "l": ["Attachment Theory", "Carl Rogers", "Virginia Satir", "Alfred Adler"],
        "contrast": [
            {"n": "Attachment Theory",
             "why": "Both are about having someone near in early life. "
                    "Bowlby asks whether that person is reliable, so the "
                    "child dares to go far; Winnicott asks whether, when "
                    "she is there, she can leave him room to be alone for a "
                    "while"},
            {"n": "Carl Rogers",
             "why": "Rogers teaches you to step toward the other person and "
                    "say back what he feels, so he feels understood. "
                    "Winnicott adds a line: sometimes the right thing is not "
                    "to ask, but to let him know someone is outside the door "
                    "and willing to wait until he comes out himself"},
        ],
    },
]

INTROS = {
    "winnicott": "A British paediatrician turned psychoanalyst who spent "
                 "forty years in a children's hospital clinic. He wrote that "
                 "it is a joy for a child to be hidden and a disaster not to "
                 "be found; that a good-enough mother is not one who never "
                 "fails but one who lets the child learn to wait; and that "
                 "the ability to be alone is something a person is given by "
                 "being quietly accompanied.",
}

SCENES = [
    ("My kid stopped talking to me", "At home", [
        ("He shut his door. Does that mean he doesn't want me?",
         [("winnicott", "joy-to-be-hidden")]),
        ("He won't say anything, and I'm scared to read his phone.",
         [("winnicott", "joy-to-be-hidden")]),
    ]),
    ("I'm at the bottom", "How you're doing", [
        ("I tell people to leave me alone, but I'm hoping someone knocks.",
         [("winnicott", "joy-to-be-hidden")]),
    ]),
    ("I can't stop pleasing people", "Dealing with people", [
        ("I say 'anything's fine,' and it isn't.",
         [("winnicott", "the-compliant-self")]),
    ]),
    ("Straight A's, then no more grades", "Starting out", [
        ("I'm good at everything, and I can't tell what I want.",
         [("winnicott", "the-compliant-self")]),
    ]),
    ("They'll find out I can't do this", "Things you don't say out loud", [
        ("I'm always polished, and it doesn't feel like me.",
         [("winnicott", "the-compliant-self")]),
    ]),
    ("Years in, nothing left between us", "At home", [
        ("We each do our own thing. Has it gone cold?",
         [("winnicott", "alone-in-company")]),
        ("When he's alone, I feel left behind.",
         [("winnicott", "alone-in-company")]),
    ]),
]

ASKS = {
    "winnicott/joy-to-be-hidden":
        "He shut his door. Does that mean he doesn't want me?",
    "winnicott/the-compliant-self":
        "I say 'anything's fine,' and it isn't.",
    "winnicott/alone-in-company":
        "We each do our own thing. Has it gone cold?",
}

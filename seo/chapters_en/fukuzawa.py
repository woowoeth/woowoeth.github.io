# -*- coding: utf-8 -*-
"""Fukuzawa Yukichi — English.

The English reader mostly meets him, if at all, as the face on the ten
thousand yen note or as a name in the Meiji modernisation story. That framing
makes him a national figure and hides the thing that is actually useful here:
his two best-known books are a beginner's manual. What to study when your
training turns out to be the wrong training, what to study first when you have
no time, and what to do with the suspicion that you were born with less.

Sources: The Autobiography of Fukuzawa Yukichi (1899, Eiichi Kiyooka's
translation) for the 1859 Yokohama visit; An Encouragement of Learning
(1872-1876, seventeen parts, over three million copies sold at the time) for
the opening line and the section on practical learning. The opening line is
given in the standard English rendering, not translated back from Chinese.
"""

PARENT = {
    "name": "Fukuzawa Yukichi",
    "slug": "fukuzawa",
    "blurb": "Deep read",
    "items": [
        {"k": "signs-in-yokohama", "n": "The signs in Yokohama",
         "w": "Years of study, and not one word legible", "ready": True,
         "line": "He started the new language the following day"},
        {"k": "practical-learning", "n": "Practical learning",
         "w": "Learn what you will use tomorrow first", "ready": True,
         "line": "The abacus and the ledger came before the classics"},
        {"k": "no-one-above", "n": "Heaven creates no man above another",
         "w": "The gap is in study, not in birth", "ready": True,
         "line": "Born with less is the one explanation he refused"},
    ],
}

CHAPTERS = [
    {
        "k": "signs-in-yokohama",
        "n": "The signs in Yokohama",
        "w": "Years of study, and not one word legible",
        "src": "Fukuzawa Yukichi, The Autobiography of Fukuzawa Yukichi, "
               "1899, on his 1859 visit to Yokohama",
        "dek": "Years of hard study turn out to be the wrong thing. What he "
               "did the day after he found out.",
        "story":
            "He was in his early twenties in Osaka, studying Dutch, which was "
            "then Japan's only window on the West, and he was very good at "
            "it. In 1859 he walked into the newly opened port of Yokohama and "
            "==could not read a single sign on the street==. They were all in "
            "English. He wrote later that it landed like a blow to the head: "
            "years of work, useless in this harbour. He did not go back to "
            "his Dutch. The next day he began hunting for English textbooks "
            "and started again from nothing.",
        "f": [
            {"n": "Useless is information, not a verdict",
             "d": "He did not write those years off, and he did not defend "
                  "them by studying harder. He read the signs as a report on "
                  "the wind: what has changed is the direction, not your "
                  "capacity. Once the direction is clear, where the effort "
                  "should go is obvious.",
             "eg": "When what you trained for stops matching the work, ask "
                   "what it tells you about direction before you mourn the "
                   "years."},
            {"n": "Switch the same week, not next year",
             "d": "He began the day after he got home. Years of sunk cost "
                  "make the instinct to give the old thing a little longer "
                  "almost irresistible, and every day of waiting adds another "
                  "chip to the track you are leaving. He simply started the "
                  "new one at once.",
             "eg": "Begin the new thing on the day you see the direction "
                   "change, even ten minutes a day. Do not let the sunk cost "
                   "keep growing."},
            {"n": "The old study was not wasted; refusing to switch is",
             "d": "He said afterwards that what he had built learning Dutch "
                  "carried straight over: how to take a sentence apart, how "
                  "to hold vocabulary, how to find someone to practise on. "
                  "The content of a craft expires. The method you built while "
                  "learning it does not.",
             "eg": "What expires is the material, not your way of learning. "
                   "The second is portable. Carry it across and replace the "
                   "first."},
        ],
        "q": [
            "What is useless tells you the direction, not your capacity.",
            "Every day of waiting adds another chip to the old track.",
            "The content expires. Your way of learning does not.",
        ],
        "apply":
            "Where you are: you spent years on a body of skill that does not "
            "fit where you now work.\n"
            "Ask first: what direction is this telling me, and have I started "
            "the new thing, or am I waiting for the old one to be useful "
            "again? What did I build while learning it that transfers "
            "directly?\n"
            "Where it goes wrong: reading it as throw away everything you "
            "learned. His Dutch is exactly why his English came fast. Change "
            "the content, keep the method.",
    },
    {
        "k": "practical-learning",
        "n": "Practical learning",
        "w": "Learn what you will use tomorrow first",
        "src": "Fukuzawa Yukichi, An Encouragement of Learning, first part, "
               "1872",
        "dek": "What to study, and whether to keep studying. What he put "
               "ahead of the Confucian classics, and the reason he gave.",
        "story":
            "An Encouragement of Learning opens by asking what learning even "
            "is. Not the memorising of difficult old texts, he answers, but "
            "practical learning: letter writing, bookkeeping, the abacus, "
            "reading a map, some physics and economics, ==the things you need "
            "every single day==. He put those ahead of the Confucian "
            "classics, and his reason was blunt. A person has to be able to "
            "feed himself and finish what is in front of him before anything "
            "else is worth discussing. The pamphlets sold over three million "
            "copies, mostly to young people who did not know what to study.",
        "f": [
            {"n": "Sort by how often you will use it",
             "d": "His ordering rule has one term in it: frequency of use. "
                  "Daily first, once a year later, someday last. He is not "
                  "saying the later ones do not matter. He is saying a "
                  "beginner has limited hours and should get fluent in the "
                  "daily ones first.",
             "eg": "When you cannot decide what to practise, write down the "
                   "three things you will need at work tomorrow morning and "
                   "practise those."},
            {"n": "Feeding yourself is the first gate",
             "d": "Independence is the word he keeps returning to. Someone "
                  "who does not live off other people can afford to have his "
                  "own judgement. So what you learn early should serve that "
                  "one thing: earn, deliver, ask nobody. Past that gate, "
                  "nothing you study is frightening.",
             "eg": "Learn what lets you stand up first. Learn what lets you "
                   "go far after you are standing."},
            {"n": "Keep reading only if it lands in your hands",
             "d": "He is not against books. He is against reading something "
                  "you cannot use and calling that study. Whether to continue "
                  "is not settled by the level of the qualification but by "
                  "whether the reading arrives as something you can now do.",
             "eg": "Before signing up for more study, answer one question. "
                   "When this ends, what can I do that I could not do "
                   "before?"},
        ],
        "q": [
            "Learn what you need tomorrow first. Once a year can wait.",
            "Learn what lets you stand, then what lets you travel.",
            "If reading leaves nothing in your hands, it was not study.",
        ],
        "apply":
            "Where you are: you cannot tell what to practise, or whether to "
            "go back for another qualification.\n"
            "Ask first: what three things will I need tomorrow morning, and "
            "am I fluent in them? Of what I am studying now, which part lands "
            "in my hands?\n"
            "Where it goes wrong: reading it as only ever study useful "
            "things. He read all his life. This is the ordering for a "
            "beginner, not the ordering for a lifetime.",
    },
    {
        "k": "no-one-above",
        "n": "Heaven creates no man above another",
        "w": "The gap is in study, not in birth",
        "src": "Fukuzawa Yukichi, An Encouragement of Learning, opening "
               "lines, 1872",
        "dek": "You suspect you were born with less. Why the book opens on "
               "that sentence, and what its second half actually claims.",
        "story":
            "The first line of An Encouragement of Learning: ==Heaven does "
            "not create one man above or below another man.== Nobody arrives "
            "ranked. But he goes straight to the harder question. Then why is "
            "the real world so unequal? His answer is not consolation. He "
            "puts the cause somewhere a person can reach: the difference "
            "comes down to whether you studied. Not fate, not birth. In 1872 "
            "Japan this was incendiary, since the hereditary status system "
            "had only just been abolished and most people still believed in "
            "ranks. The gap was made after birth, which is why it can be "
            "closed.",
        "f": [
            {"n": "Move the cause somewhere you can reach",
             "d": "The worst thing about I was born with less is not that it "
                  "might be false. It is that it parks the cause where "
                  "nothing can be done. He moves it to whether you studied. "
                  "That may not be the whole truth, but it moves, and a "
                  "movable cause gives you work.",
             "eg": "When you feel outmatched, move the cause from I am simply "
                   "like this to which part have I not trained. Only the "
                   "second has a next step."},
            {"n": "He is better usually means he is earlier",
             "d": "Most of the difference he saw came from the order in which "
                  "people met things, not from what they were born with. "
                  "Someone looks steady because they practised something "
                  "three years before you did. Translate stronger into "
                  "earlier and most of the anxiety goes.",
             "eg": "When someone is a step ahead of you on everything, first "
                   "ask whether they met all of it a few years before you "
                   "did."},
            {"n": "Born with less is the cheapest explanation, so watch it",
             "d": "The moment that explanation is accepted, nothing further "
                  "is required of you, because it was settled at birth. He "
                  "objects to it not only because it is wrong but because it "
                  "is so convenient. The more effortless an explanation, the "
                  "more it deserves suspicion.",
             "eg": "An explanation that leaves you with nothing to do is "
                   "usually not the true one. It is the comfortable one."},
        ],
        "q": [
            "Heaven does not create one man above or below another man.",
            "The gap was made after birth, so it can be closed.",
            "Translate stronger into earlier and most of the anxiety goes.",
            "An explanation that asks nothing of you is comfortable, not "
            "true.",
        ],
        "apply":
            "Where you are: everyone around you seems steadier and faster, "
            "and you suspect you were simply born with less.\n"
            "Ask first: the things I lose on, were they born knowing them or "
            "did they meet them three years before me? Is my cause parked "
            "somewhere I can reach?\n"
            "Where it goes wrong: reading it as effort closes any gap. He "
            "says the gap was made after birth, not that every such gap can "
            "be closed. And it is a line to say to yourself, not one to use "
            "on someone doing worse than you.",
    },
]

# -*- coding: utf-8 -*-
"""Daily entry: The Yellow Emperor's Inner Classic.

Picked by fan-out. 'I've run out of energy', 'I've been tense for a long time'
and 'I can't be myself around family' were among the emptiest situations on
the Chinese side. What hangs under the first two is mostly Sapolsky, Ratey
and the Book of Rites: why tension wears you down, move first, schedule rest.
None of them says that the time to act is before anything has shown. That is
the well dug in thirst. The second chapter fills 'My head won't stop at
night': remove the one thing you do daily that you know will keep you awake
before you train calm. The third fills 'A row at home leaves me tight for
days': a feeling has a path through the body, and brooding is the one that
stays.

It is a classic of medicine, so the entry leaves out the medicine: pulse,
needles, prescriptions, the five-phase matching of organs. Nothing on the
page is medical advice.

All quoted lines are our own renderings of the Chinese, checked against the
Wikisource text of the Basic Questions, not taken from a published
translation.

Three stories, no overlap: the entry is the Emperor's opening question, the
chapters are the closing paragraph of 'Four Seasons', Qi Bo's two pictures,
and the opening of 'On Pain'.

All situations already exist, so there is no SC_BOX here.
"""

ENTRIES = [
    {
        "c": "Body and daily life",
        "n": "The Yellow Emperor's Inner Classic",
        "slug": "huangdi-neijing",
        "e": "Warring States to Western Han · attributed to the Yellow Emperor",
        "w": "Treat what is not yet ill", "y": -100,
        "d": "A medical classic written as questions from the Yellow Emperor "
             "and answers from Qi Bo and others, put together between the "
             "Warring States and the Western Han. It survives in two parts, "
             "the Basic Questions and the Spirit Pivot, and after the Han it "
             "was treated as the root text of Chinese medicine. Most of it "
             "is about diagnosis, channels, needles and herbs. We leave all "
             "that out. A smaller part asks how people should live so that "
             "they do not fall ill, and from the Basic Questions we take "
             "three passages: act before illness comes, put routine before "
             "calm, and feeling travels through the body.",
        "story":
            "The Yellow Emperor sat down and put a question to Qi Bo. I have "
            "heard that people of high antiquity passed a hundred years and "
            "their movements did not fail; people now fail at fifty. Has the "
            "age changed, or have people let something slip? The question "
            "opens the first chapter of the Basic Questions; what Qi Bo says "
            "next is a whole chapter on routine and the spirit.",
        "f": [
            {"n": "The first question asks about people, not about the age",
             "d": "The Emperor asks whether the age has changed or people have lost something. The first question of the whole book puts the weight on how people live, not on fate or luck.",
             "eg": "Your body isn't what it was. Before you blame age, ask what these two years have left out of your days."},
            {"n": "Digging the well when you are thirsty",
             "d": "The closing paragraph of 'Four Seasons' says medicine after illness is like digging a well once thirsty. Neither medicine nor repair is wrong. The sage acts before the illness, while it can still be adjusted.",
             "eg": "Hollow by mid-afternoon is the time to act, not to wait a bit longer."},
            {"n": "Make the careless a habit, keep no routine",
             "d": "Qi Bo's answer is not a great disaster but a way of living: wine for water, the random made the routine, no regular hours, so they fail at fifty. The people of antiquity kept measure and regular hours, and body and spirit stayed together.",
             "eg": "Every Friday to three a.m. for three months: once was a break, now it is a routine."},
            {"n": "A hundred ills come from qi",
             "d": "'On Pain' has the Emperor say that a hundred ills come from qi. Anger sends it up, joy slackens it, brooding ties it in a knot. Feeling does not stay in the heart; it travels the body, and joy is among the nine.",
             "eg": "After the row your neck stayed stiff for three days, and then you noticed it hadn't left."},
        ],
        "apply": "Today, do one small thing. Think about the last three weeks and ask whether anything has been wearing you down that you keep calling bearable. Pick one and deal with it today: that is acting before thirst. Keep a second for the night you can't sleep: before you try to train calm, find the one thing you do on purpose that keeps you up, and drop it. Keep a third for after a row: don't tell yourself to stop thinking, first find where in the body the sentence still sits. If you have real symptoms, see a doctor; these passages are not a diagnosis.",
        "q": [
            "Medicine after illness is a well dug in thirst.",
            "The random, made the routine, is why fifty fails.",
            "A hundred ills come from qi: feeling travels the body.",
            "Toil is fine. It is weariness that matters.",
        ],
        "l": ["The Book of Rites", "Zhuangzi", "Robert Sapolsky",
              "Seneca", "John Ratey"],
        "contrast": [
            {"n": "Robert Sapolsky", "why": "Both ask why staying tense wears you down. Sapolsky is about the stress response: the zebra's ends when the lion leaves, ours stays switched on for things that have not happened. The Inner Classic is about timing: don't wait until thirst to dig the well, act while it can still be adjusted"},
            {"n": "Seneca", "why": "Both write about anger. Seneca is about how to stop it in the moment it rises; the Inner Classic is about where it goes when it can't be stopped: anger sends qi up, travels the body, and stays"},
        ],
    },
]

INTROS = {
    "huangdi-neijing":
        "The medical classic framed as the Yellow Emperor questioning Qi Bo, "
        "put together from the Warring States to the Western Han - we leave "
        "out the needles and herbs and take three passages from the Basic "
        "Questions on how to live",
}

SCENES = [
    ("I've run out of energy", "Body and energy", [
        ("I'm not ill yet. Is it too early to stop?",
         [("huangdi-neijing", "water-before-thirst")]),
    ]),
    ("I've been tense for a long time", "Body and energy", [
        ("I've lain down and my head still won't stop.",
         [("huangdi-neijing", "mind-kept-within")]),
    ]),
    ("I can't be myself around family", "At home", [
        ("After a row at home my chest is tight for days.",
         [("huangdi-neijing", "nine-qi")]),
    ]),
]

ASKS = {
    "huangdi-neijing/water-before-thirst": "I'm not ill yet. Is it too early to stop?",
    "huangdi-neijing/mind-kept-within": "I've lain down and my head still won't stop.",
    "huangdi-neijing/nine-qi": "After a row at home my chest is tight for days.",
}

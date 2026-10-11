# -*- coding: utf-8 -*-
"""The Yellow Emperor's Inner Classic - English.

An English reader who knows this book at all knows it as the root text of
Chinese medicine: meridians, needles, herbs. We leave all of that out. These
three chapters take passages from the Basic Questions that talk about how to
live: when to act on a body that is not yet ill, how routine comes before
calm, and how a feeling travels through the body.

The quoted lines are our own renderings of the Chinese, checked against the
Wikisource text of the three chapters, not taken from a published
translation. Nothing here is medical advice.
"""

PARENT = {
    "name": "The Yellow Emperor's Inner Classic",
    "slug": "huangdi-neijing",
    "blurb": "Deep read",
    "items": [
        {"k": "water-before-thirst",
         "n": "Digging the well once you're thirsty is too late",
         "w": "Treat what is not yet ill: the time to act is before anything breaks",
         "ready": True,
         "line": "To reach for medicine after illness is to dig a well once you are thirsty"},
        {"k": "mind-kept-within",
         "n": "Failing at fifty: making the careless a habit",
         "w": "Keep a steady routine, keep the mind within: order the days first, then seek calm",
         "ready": True,
         "line": "He asked why people now fail at fifty; the answer began with how they live"},
        {"k": "nine-qi",
         "n": "Anger sends it up, brooding ties it in a knot",
         "w": "A hundred ills come from qi: feeling does not stay in the heart, it travels the body",
         "ready": True,
         "line": "Nine kinds of qi, each going its own way, and even joy is among them"},
    ],
}

CHAPTERS = [
    {
        "k": "water-before-thirst",
        "n": "Digging the well once you're thirsty is too late",
        "w": "Treat what is not yet ill: the time to act is before anything breaks",
        "src": "Basic Questions, 'Regulating the Spirit through the Four Seasons', closing paragraph",
        "dek": "I'm not ill yet, so is it too early to stop? This chapter asks whether there is a right moment to act before the body gives out.",
        "story":
            "Most of this chapter goes season by season, saying how a person "
            "should rise and rest and tend the spirit in each. At the end the "
            "tone changes. The sage, it says, does not treat the illness that "
            "has come but the one that has not; not the disorder that has "
            "come but the one that has not. Why? To give medicine once the "
            "illness has formed, to set things right once disorder has formed, "
            "is ==like digging a well when you are thirsty==, and it asks: is that not late?",
        "f": [
            {"n": "The mistake is the order, not the medicine",
             "d": "Medicine after illness, repair after disorder. Nothing in the passage says the medicine is wrong or the repair is pointless. A well is a good thing to dig. The fault lies in the timing: the water arrives after you needed it.",
             "eg": "You see a doctor only when you can't sleep, after six months without a single day off."},
            {"n": "'Not yet ill' is the stretch you can still adjust",
             "d": "Not yet ill does not mean no signs at all. It means signs small enough to listen to advice. The word for disorder works the same way: anywhere order slips, in body, routine or household. That stretch is the shortest and the cheapest.",
             "eg": "Hollow by mid-afternoon, propped up by coffee: this is the part you can still adjust."},
            {"n": "Adjust along the seasons",
             "d": "The chapter's title means regulating the spirit through the four seasons: a rhythm that follows what is outside, set before anything needs patching. The rhythm of your days should not be set by mood or workload, but by something bigger than both.",
             "eg": "Dark by five in winter, and you still run the summer timetable on willpower."},
        ],
        "apply":
            "Where you are: nothing has shown up on a test, but you are hollow "
            "by afternoon, struggle out of bed, and keep telling yourself "
            "you'll sort it out once this busy stretch ends.\n"
            "Ask first: am I thirsty yet? Not whether you are ill, but whether "
            "one small thing has repeated for three weeks while you called it "
            "bearable. Deal with that one today, nothing else yet.\n"
            "Where it goes wrong: reading it as 'watch for illness every day', "
            "which breeds anxiety, or as 'no need for a doctor if I live "
            "well'. It says do not wait until thirst, not do not dig the well. "
            "If symptoms have started, see a doctor.",
        "q": [
            "Medicine after illness is a well dug in thirst.",
            "Not yet ill: the stretch you can still adjust.",
            "Dig the well before you are thirsty.",
        ],
    },
    {
        "k": "mind-kept-within",
        "n": "Failing at fifty: making the careless a habit",
        "w": "Keep a steady routine, keep the mind within: order the days first, then seek calm",
        "src": "Basic Questions, 'On the Primal Truth of High Antiquity', the opening exchange",
        "dek": "I lie down and my head won't stop. Which should come first, the body or the mind?",
        "story":
            "The sage Qi Bo answered the Emperor with two pictures. In the "
            "first, people of high antiquity who knew how to live followed "
            "the yin and yang, ate and drank in measure, kept regular hours "
            "and did not toil at random, so body and spirit stayed together "
            "and they lived out their years. In the second, people now "
            "==make wine their water and the random their routine==, do not "
            "know how to keep a vessel full, and keep no regular hours, so "
            "they fail at fifty.",
        "f": [
            {"n": "Body and spirit together: neither may drop",
             "d": "The first picture ends with the body and the spirit staying together. The text lists routine first and the mind second, but it does not mean to tend only one. Enough sleep with the mind still hanging off a phone does not count as together.",
             "eg": "You slept eight hours, and your first act on waking is checking messages."},
            {"n": "No great vice, only a run of small indulgences",
             "d": "The list for people now is wine for water, the random made the routine, no keeping a vessel full, no timing for the spirit, chasing a quick heart. None of it is a great vice: each is a bit of quick pleasure, made daily. Random plus routine is where the failing comes from.",
             "eg": "A Friday night to three a.m. is a break. Every Friday for three months is a routine."},
            {"n": "Dodge what is outside first, then keep the mind within",
             "d": "The sages taught that a harmful wind should be avoided in its season; then, with a calm and empty mind, true qi follows; keep the spirit within and how can illness come? The order is outside first, then inside. After that: the body toils without growing weary.",
             "eg": "A day of hard work that leaves you settled differs from a day of idling that leaves you restless."},
        ],
        "apply":
            "Where you are: you lie down, your head still turning over "
            "today's problem past midnight, and you push through the next "
            "day on nerve.\n"
            "Ask first: is there one thing tonight that I know will keep me "
            "awake, yet do every day? That is my 'random'. Remove it before "
            "you try to train a calm mind.\n"
            "Where it goes wrong: reading 'few desires' as 'don't want "
            "anything', or demanding that your mind turn to still water at "
            "once. The text puts avoiding the harmful wind before the calm "
            "and empty mind: do what can be avoided outside first, and the "
            "mind comes after.",
        "q": [
            "The random, made the routine, is why fifty fails.",
            "Toil is fine. It is weariness that matters.",
            "Dodge what you can outside, then keep the mind within.",
        ],
    },
    {
        "k": "nine-qi",
        "n": "Anger sends it up, brooding ties it in a knot",
        "w": "A hundred ills come from qi: feeling does not stay in the heart, it travels the body",
        "src": "Basic Questions, 'On Pain', opening",
        "dek": "After a row at home my chest is tight for days. What does a feeling leave behind in the body once it has passed?",
        "story":
            "The Emperor opens this chapter by setting a rule. One who speaks "
            "well of heaven must show it in people, one who speaks well of "
            "the past must show it fits today, one who speaks well of people "
            "must find it holds in himself. Then he says what he has "
            "concluded: ==a hundred ills come from qi==. Anger sends it up, "
            "joy slackens it, grief wears it away, fear sinks it, shock "
            "scatters it, and brooding ties it in a knot.",
        "f": [
            {"n": "It has to hold in you",
             "d": "The Emperor states the test before the conclusion: one who speaks well of people must find it holds in himself. A line about people counts only if you can check it against yourself. Anger sends qi against its course, and in the worst case, the text says, blood is vomited.",
             "eg": "Reading 'anger sends it up', you recall your neck and shoulders stiff for days after the last row."},
            {"n": "Of nine kinds, even joy is one",
             "d": "Anger, grief and fear are on the list, but so are joy, cold, heat and toil. Of joy it says the qi eases and the spirit reaches its goal: good news, yet still a shift. Nine kinds go nine different ways; it is not only the bad feelings that cost you.",
             "eg": "A whole week of busy happy events, and you still collapse on Saturday."},
            {"n": "Brooding ties it in a knot",
             "d": "When the heart holds a thing, the spirit settles on it, and right qi lingers and does not move, so the qi is knotted. The one closest to daily life: not rage, not tears, but one sentence turned over again and again.",
             "eg": "You replay what was said in the afternoon thirty times at night; next morning your chest is still tight."},
        ],
        "apply":
            "Where you are: a row at home is over, but you are not: chest "
            "tight, no appetite, awake at three.\n"
            "Ask first: where in my body does that sentence still sit? Name "
            "which of the nine it is, anger, grief or brooding, before telling "
            "yourself to stop thinking about it.\n"
            "Where it goes wrong: treating it as a diagnosis and writing "
            "yourself a prescription: 'my qi is knotted, so...'. The text "
            "says feeling and body are in traffic, not what to take for it. "
            "If you have real symptoms, see a doctor.",
        "q": [
            "One who speaks of people must find it holds in himself.",
            "Brooding ties it in a knot: one sentence, turned over.",
            "Joy is among the nine, and it costs too.",
        ],
    },
]

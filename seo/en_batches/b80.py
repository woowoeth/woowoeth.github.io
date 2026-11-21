# -*- coding: utf-8 -*-
"""Daily entry: William James.

The queue (DAILY_QUEUE.md) is finished, so this one was picked the old way. 'I want to change a habit'
and 'I've been tense for a long time' are among the emptiest scenes. The habit pieces are about systems,
identity and tiny steps; none says what a single lapse costs. The tension pieces are about stress
physiology and rest; none says the tension may be a learned manner rather than a response to the load.

Why he qualifies: founder of American psychology; The Principles of Psychology (1890).

The entry story is the diary entry of spring 1870 after reading Renouvier (transcribed in Harvard's
Houghton Library exhibition); the chapters are the habit maxims of 1890 and 'The Gospel of Relaxation'
of 1899.
"""

ENTRIES = [
    {
        "c": "Body and daily life",
        "n": "William James",
        "slug": "william-james",
        "e": "United States · 1842–1910",
        "w": "Habit", "y": 1890,
        "d": "American psychologist and philosopher, founder of psychology as a science in the United States. Trained "
             "as a doctor, he began teaching psychology at Harvard in the 1870s, and in 1890 published the two "
             "volumes of The Principles of Psychology, whose chapters on habit, attention, emotion and will are still "
             "quoted. He is here for two everyday things: why habits break on 'just this once', and why people stay "
             "tense when the work is not that heavy.",
        "story":
            "In 1869 James, twenty-seven, took his medical degree at Harvard and was ill, listless and unsure what "
            "to do; that winter his diary is full of misery. In the spring of 1870 he read the French philosopher "
            "Charles Renouvier on free will and wrote that he would assume, at least until next year, that it was no "
            "illusion: \"My first act of free will shall be to believe in free will.\" He did not wait for a proof. "
            "Three years later his father wrote that William credited his recovery to reading Renouvier.",
        "f": [
            {"n": "Act the feeling first",
             "d": "He held that feeling follows the body more than we think. To recover lost cheerfulness, sit up cheerfully, look round cheerfully, and speak as if it were already there. To feel brave, act as if you were. Wrestling with a bad feeling only pins your attention on it.",
             "eg": "Before meeting someone you resent, say the friendly sentence out loud first."},
            {"n": "Hand the routine to habit",
             "d": "The great thing in education, he wrote, is to make the nervous system an ally instead of an enemy. The more daily detail is left to habit, the more the mind is free for real work. The most miserable person is one in whom nothing is habitual but indecision.",
             "eg": "Fix the hour you get up and the hour you start, so mornings are not a negotiation."},
            {"n": "A little gratuitous effort",
             "d": "His prescription for the will: every day or two, do something for no other reason than that you would rather not. It is like insurance on a house. The premium does no good at the time and may never pay out, but if the fire comes it saves you.",
             "eg": "When both stairs and lift will do, take the stairs."},
        ],
        "apply": "This week fix one small thing you currently decide afresh every day: when you get up, when you start, "
                 "what you do first when you sit down. Once it is fixed, stop negotiating, and spend the saved effort on what needs thought.",
        "q": [
            "To feel cheerful, sit up as if you already were.",
            "Nothing habitual but indecision: the most miserable state.",
            "A little needless effort is insurance for the will.",
        ],
        "l": ["Benjamin Franklin", "Atomic Habits", "BJ Fogg"],
        "contrast": [
            {"n": "Benjamin Franklin", "why": "Both taught people to change their habits. Franklin listed thirteen virtues, watched one a week, marked each fault with a black spot in a little book, and admitted he never reached the perfection he wanted, only became better and happier. James said to allow no exception until a new habit has rooted, because every lapse is counted. One tolerates daily marks and lets them shrink; the other refuses the first gap."},
        ],
    },
]

INTROS = {
    "william-james":
        "The founder of American psychology. He said that when you excuse a lapse with 'this time doesn't count', "
        "your nerves count it anyway; and that people break down less from the amount of work than from the tension "
        "they carry while doing it",
}

SCENES = [
    ("I want to change a habit", "Body and energy", [
        ("I keep telling myself this one time doesn't count.",
         [("william-james", "no-exceptions")]),
    ]),
    ("I've been tense for a long time", "Body and energy", [
        ("Whenever I work I rush, as if someone were chasing me.",
         [("william-james", "unclamp")]),
    ]),
]

ASKS = {
    "william-james/no-exceptions": "I keep telling myself this one time doesn't count.",
    "william-james/unclamp": "Whenever I work I rush, as if someone were chasing me.",
}

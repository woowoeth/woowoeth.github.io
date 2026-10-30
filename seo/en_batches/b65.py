# -*- coding: utf-8 -*-
"""Daily entry: Su Qin.

From DAILY_QUEUE.md row 2. 'I can't land work' holds Kevin Kelly, Paul Graham,
Graham and Merton on audiences, margins and who gets noticed. Nothing on what
to do after ten refusals in a row, and nothing on whether the person across the
table lacks the need. 'Nobody is looking at my work' has nothing on pitching to
the wrong audience.

Why he qualifies: the foremost strategist-persuader of the Warring States, with
a biography in the Records of the Grand Historian.

The entry story is the return through Luoyang (the sister-in-law who served him
at table, the two fields); the chapters are the failed audience in Qin and the
turn to Yan.
"""

ENTRIES = [
    {
        "c": "Reading people",
        "n": "Su Qin",
        "slug": "su-qin",
        "e": "Warring States · dates unknown",
        "w": "Fix one thing first", "y": -334,
        "d": "A Warring States strategist with a biography in the Records of the Grand Historian, which says he "
             "studied under Master Guigu, argued for an alliance of the six states against Qin, and for a time wore "
             "the seals of office of all six. His worst year, by the Records, was ten failed letters to the King of "
             "Qin, then home in a worn coat with the money gone to a family that would not speak to him. This page "
             "takes two things: what to fix after a refusal, and whether to change the buyer. The Mawangdui silk "
             "manuscripts give a different Su Qin from the Records in dates and deeds, and this page follows the Records.",
        "story":
            "According to the Records, years later Su Qin passed through his home town of Luoyang with so many "
            "carriages and so much baggage that it looked like a king's progress, and envoys from several states "
            "came to see him off. The brothers and wife and sister-in-law who had refused him food stood with "
            "lowered eyes and served him at table on their knees. He asked his sister-in-law, smiling, why she had "
            "been so proud before and was so humble now. Because your rank is high and you have much gold, she said. "
            "He sighed: had he owned two good fields outside Luoyang, would he ever have worn six seals? Then he "
            "gave a thousand in gold to his clan and friends.",
        "f": [
            {"n": "After a refusal, fix one thing",
             "d": "After ten failed letters to the King of Qin he went home, opened the old books and gave himself a year. What he practised was seeing what one person wanted and how to speak to it. He fixed one specific thing, not more books.",
             "eg": "Ten applications and no replies: do not blame the market yet. Look at your portfolio for the page least like what they asked for."},
            {"n": "The strongest may need you least",
             "d": "He spoke to the King of Qin about swallowing the other states, and the king did not want it. In Yan he spoke about not being swallowed and settled it in one audience. He did not change his skill, only who was across the table.",
             "eg": "The same tool: big companies say they already have one, and a team of a dozen has the owner asking the price on the spot."},
            {"n": "A soft fallback can hold you back",
             "d": "He said it himself later: with two good fields he would never have worn the seals. That is no case for being poor. It is a prompt to notice when comfort began making your decisions.",
             "eg": "A side project stays a side project because the day job pays the bills, and being able to afford it may be the reason you stop pushing."},
        ],
        "apply": "This week dig out one refusal on record (a quote, an application, a proposal). Write down which "
                 "part they did not want, then name one person who has the problem you can solve and go to them next week.",
        "q": [
            "After a refusal, fix one thing, then go out again.",
            "The biggest player is often the one that needs you least.",
            "When the fallback is comfortable, ask if you still want to leave.",
        ],
        "l": ["Guiguzi", "Strategies of the Warring States", "Sun Tzu"],
        "contrast": [
            {"n": "Guiguzi", "why": "One school of thought, two lives. The master put it into a book and stayed in the mountains; his pupil took the book out into the market and was refused ten times. One guarded the method, the other tested it in the field."},
        ],
    },
]

INTROS = {
    "su-qin":
        "Warring States strategist - after ten failed letters to the King of "
        "Qin he went home to a family that would not speak to him, studied for "
        "a year, then took the same skill to the state most afraid of being "
        "swallowed",
}

SCENES = [
    ("It still hasn't worked", "Nothing's moving", [
        ("Ten tries, no deal, and my family has stopped believing in me.",
         [("su-qin", "ten-pitches")]),
    ]),
    ("Nobody is looking at my work", "Getting it done", [
        ("My offer is fine. Am I pitching the wrong people?",
         [("su-qin", "wrong-buyer")]),
    ]),
]

ASKS = {
    "su-qin/ten-pitches": "Ten tries, no deal, and my family has stopped believing in me.",
    "su-qin/wrong-buyer": "My offer is fine. Am I pitching the wrong people?",
}

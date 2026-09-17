# -*- coding: utf-8 -*-
"""Daily entry, day 9: Bai Juyi.

Picked to break a streak, then by fan-out inside the half that was being
skipped. The first eight daily entries were all Western; the selection rule
had been drifting that way because the emptiest situations are the modern
psychological ones, which is Western social science's home ground. See
scripts/pick_balance.py.

Inside that constraint the usual test still applies - which sentence does he
add. On 不想卷但怕掉队 the site offers Zhuangzi's uselessness, Buffett's circle
of competence, the Analects on harmony without sameness, Xunzi and Naval on
leverage: all either a frame of mind or a change of track. None of them hands
you a position you can actually sit in for years, with a salary and a title.
On 主线没成副业成了 it offers Pu Songling, whose main work failed and whose
side work survived - but he died believing the examinations were the real
thing. Bai Juyi knew in his own lifetime that readers loved what he ranked
lowest, and did not reorder his list.

All four English situations already exist, so there is no SC_BOX here.
Quoted matter is from his own poem and his own letter; the widely repeated
stories about him reading drafts to an old woman come from much later
collections and are not used.

Three stories, no overlap: the entry is the house at Luoyang, chapter one is
the sinecure he asked for in 829, chapter two is the letter from Jiangzhou.
"""

ENTRIES = [
    {
        "c": "Body and daily life", "n": "Bai Juyi",
        "slug": "bai-juyi", "e": "Tang · 772-846",
        "w": "The middle setting", "y": 829,
        "d": "A Tang poet whose work circulated more widely in his own lifetime "
             "than almost anyone's - and who did not rate most highly the poems "
             "that travelled. He passed the civil examinations at twenty-eight, "
             "was demoted to a provincial post at forty-four, governed Hangzhou "
             "and Suzhou, and at fifty-eight asked for an office that carried "
             "rank and salary and almost no duties. He moved to Luoyang and "
             "stayed eighteen years. What he left is not only poems: he turned "
             "the problem of not being able to continue and not daring to stop "
             "into a concrete arrangement, and he wrote down, while in disgrace, "
             "that what readers keep is never quite what the writer worked "
             "hardest on.",
        "story":
            "He wrote about his own house like a man doing his accounts: ten mu "
            "of grounds, five of garden, one pool of water, a thousand stems of "
            "bamboo. This was Luoyang, where he lived from fifty-eight onwards. "
            "There was a small tower by the pool and a boat below it. He did not "
            "attend court, had almost no official business, and drew his salary "
            "every month. A man who had passed the examinations young, governed "
            "two of the richest cities in the empire and seen his poems copied "
            "everywhere had settled himself in neither the hills nor the court, "
            "but between them.",
        "f": [
            {"n": "He picked a third way of living",
             "d": "His poem sorts people in three: the great recluse hides in the "
                  "marketplace, the lesser in the hills. Both are refused - too "
                  "loud, too bleak - and he takes the middle, hiding inside a post "
                  "that has standing and pay but no daily grind.",
             "eg": "All in or hand in your notice: most people are stuck because "
                   "those are the only two options they can see."},
            {"n": "He says what the setting runs on",
             "d": "The lines are blunt about money: no toil of mind or body, no "
                  "hunger or cold, no business all year, a salary every month. "
                  "The middle setting is not a mood. It is rank and income that "
                  "other people recognise, and without both it collapses.",
             "eg": "Before taking on less, check the year still balances without "
                   "that income; if it does not, you will be pulled back in."},
            {"n": "He never called it the ideal",
             "d": "The poem closes by putting him between hardship and success, "
                  "between plenty and want. He is not offering the best answer "
                  "but one that can be occupied for years. Read as transcendence, "
                  "it loses the word he wrote: between.",
             "eg": "Accepting a few years of neither excelling nor falling behind "
                   "costs less than swinging between the two."},
            {"n": "He knew in his lifetime what readers preferred",
             "d": "Demoted to Jiangzhou, he wrote to his friend Yuan Zhen sorting "
                  "his poems into four kinds. He rated the satires on ordinary "
                  "hardship highest; readers wanted the long narrative poem. His "
                  "conclusion: what the age values is what I rank low.",
             "eg": "The proposal you were proudest of goes unmentioned; a diagram "
                   "you knocked out is forwarded everywhere."},
            {"n": "Knowing it, he left his own order alone",
             "d": "He neither stopped writing satires to suit the audience nor "
                  "argued that they were better. The same letter gives his "
                  "resolution: the ambition is to serve everyone, the practice is "
                  "to keep oneself in order - two different sizes, kept apart.",
             "eg": "If you still rate the work nobody applauded, do not strike it "
                   "off your own list because nobody applauded."},
        ],
        "apply":
            "If you are stuck between cannot go on and dare not leave, stop "
            "choosing a side and write down what the third setting would need: "
            "where the income comes from, what it is called, and who recognises "
            "it. His post had rank and pay, and he could only reach it after a "
            "career as a senior governor; without those the middle setting is "
            "idleness with no money. Then do the second thing: keep two lists, "
            "the order of what the world takes and the order in your own head. "
            "That the work you laboured over went unwanted is not a reason to "
            "strike it off your own list. He did exactly this, and he did it in "
            "the year he was demoted.",
        "q": [
            "The hills are too bleak and the marketplace too loud.",
            "It resembles serving and it resembles withdrawing.",
            "Rank and salary hold the setting up, not a state of mind.",
            "What the age values is what I rank low.",
        ],
        "l": ["Tao Yuanming", "Su Shi", "Feng Dao", "Pu Songling", "Zhuangzi"],
        "contrast": [
            {"n": "Tao Yuanming",
             "why": "One problem, two answers: Tao Yuanming would not bend for "
                    "five pecks of rice and resigned the same day, while Bai Juyi "
                    "kept the rice and cut the bending down to the minimum"},
            {"n": "Pu Songling",
             "why": "Both got the wrong success: Pu Songling died believing the "
                    "examinations were the real work and the tales were a "
                    "sideline, while Bai Juyi laid both lists out in his own "
                    "lifetime and said which one was his"},
        ],
    },
]

INTROS = {
    "bai-juyi": "Tang poet who at fifty-eight took an office with rank, salary "
                "and no duties, and wrote up that middle setting as a third "
                "option between racing and quitting",
}

SCENES = [
    ("I don't want to race but I'm scared to stop", "How you're doing", [
        ("I want to slow down and I'm afraid of losing my place.",
         [("bai-juyi", "middle-hiding")]),
    ]),
    ("Should I step back", "When to step back", [
        ("Grind on or walk out. Is there nothing else?",
         [("bai-juyi", "middle-hiding")]),
    ]),
    ("The side thing worked, the main thing didn't", "Looking back, moving on", [
        ("What they love is not what I worked hardest on.",
         [("bai-juyi", "what-i-rank-low")]),
    ]),
    ("It still hasn't worked", "Nothing's moving", [
        ("Nothing I say moves it. Do I keep saying it?",
         [("bai-juyi", "what-i-rank-low")]),
    ]),
]

ASKS = {
    "bai-juyi/middle-hiding":
        "I want to slow down and I'm afraid of losing my place.",
    "bai-juyi/what-i-rank-low":
        "What they love is not what I worked hardest on.",
}

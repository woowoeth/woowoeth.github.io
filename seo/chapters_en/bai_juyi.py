# -*- coding: utf-8 -*-
"""Bai Juyi - English.

English readers who meet Bai Juyi at all meet him as the author of a long
narrative poem about an emperor and his concubine. These two chapters use
what he wrote about his own life instead: the third position he arranged for
himself between striving and quitting, and the letter in which he says, while
in disgrace, that what readers love is not what he ranks highest. Both come
from his own texts; the famous anecdotes about him testing poems on an old
woman are from much later collections and are not used here.
"""

PARENT = {
    "name": "Bai Juyi",
    "slug": "bai-juyi",
    "blurb": "Deep read",
    "items": [
        {"k": "middle-hiding", "n": "There is a setting between all-in and out",
         "w": "He arranged a salary and a title for that setting",
         "ready": True,
         "line": "The hills too bleak, the court too loud, so he took the middle post"},
        {"k": "what-i-rank-low", "n": "What the world keeps is not what you worked hardest on",
         "w": "He knew it in his lifetime and did not reorder his list",
         "ready": True,
         "line": "The poems everyone loved were the ones he himself rated lowest"},
    ],
}

CHAPTERS = [
    {
        "k": "middle-hiding",
        "n": "There is a setting between all-in and out",
        "w": "He arranged a salary and a title for that setting",
        "src": "'Middle Hiding', from his collected works; the sinecure at Luoyang "
               "taken in 829",
        "dek": "You cannot keep going like this and cannot afford to stop. Whether "
               "a liveable third position exists between them.",
        "story":
            "In 829, at fifty-eight, Bai Juyi asked for a post called Adviser to "
            "the Heir Apparent, attached to the secondary capital. It carried "
            "rank and a monthly salary, required no court attendance and almost "
            "no work. He moved to Luoyang and stayed eighteen years, until he "
            "died. He wrote a poem for the arrangement, sorting people into "
            "three kinds: the great recluse hides in the marketplace, the lesser "
            "one in the hills. ==The hills are too bleak and the market too "
            "loud, so he took the middle kind and hid inside an office==.",
        "f": [
            {"n": "Both extremes are refused first",
             "d": "The opening rejects each side on its own terms: the hills are "
                  "too desolate, the court too noisy. He does not make retreat "
                  "noble or office corrupt. Only once both are admitted to be "
                  "unliveable does a third option have a reason to exist.",
             "eg": "Go flat out or hand in your notice - most people are stuck "
                   "because those are the only two they can see."},
            {"n": "Neither quite in nor quite out",
             "d": "His description is a run of negatives: it resembles serving "
                  "and also withdrawing, is neither busy nor idle. That is not "
                  "vagueness. The whole value is that it belongs fully to neither "
                  "side, so neither side's price is charged in full.",
             "eg": "A role with no promotion track and nobody calling at "
                   "midnight; you cannot say if it is a step up or down."},
            {"n": "He states what holds the setting up",
             "d": "The next lines are blunt about the economics: no toil of mind "
                  "or body, no hunger or cold, no official business all year, and "
                  "a salary every month. This is not a frame of mind. It is rank "
                  "and money that other people recognise.",
             "eg": "Before taking on less work, check whether the year still "
                   "works without that income. If it does not, you will be pulled "
                   "back."},
            {"n": "He calls it a compromise, never an ideal",
             "d": "The poem ends by placing him between hardship and success, "
                  "between plenty and want. He is not offering the best answer, "
                  "he is offering one that can be occupied for years. Read as "
                  "transcendence, it loses the word he actually wrote: between.",
             "eg": "Accepting that these few years will be neither outstanding "
                   "nor falling behind costs less than swinging between the two."},
            {"n": "He did not reason his way there first",
             "d": "The poem was written in Luoyang, and by then he had been "
                  "demoted to Jiangzhou, moved to Zhongzhou and governed both "
                  "Hangzhou and Suzhou. The middle position is where he landed "
                  "after all of that, not an insight he had while young.",
             "eg": "People who have stopped competing have usually competed "
                   "first, and lost, which is how they learned which slot they "
                   "want."},
        ],
        "apply":
            "Where you are: you cannot keep going at this pace, and stopping "
            "altogether frightens you.\n"
            "Ask first: am I looking for a break or for a different setting - "
            "because if it is the second, where does the money for that setting "
            "come from, and who recognises the title?\n"
            "Where it goes wrong: using it as a licence to coast. His post had "
            "rank, salary and standing, and he could only reach it after a career "
            "as a senior governor. Without those, the middle position is just "
            "idleness with no income.",
        "q": [
            "The hills are too bleak and the marketplace too loud.",
            "It resembles serving and it resembles withdrawing.",
            "Neither busy nor idle, and that is the whole point.",
            "Rank and salary hold the setting up, not a state of mind.",
        ],
    },
    {
        "k": "what-i-rank-low",
        "n": "What the world keeps is not what you worked hardest on",
        "w": "He knew it in his lifetime and did not reorder his list",
        "src": "'Letter to Yuan Zhen', written in 815 while demoted to Jiangzhou",
        "dek": "The work you laboured over goes unread and the offhand piece "
               "travels. What to do once you know that.",
        "story":
            "In 815 Bai Juyi was demoted and sent to Jiangzhou. That year he "
            "wrote a long letter to his friend Yuan Zhen, sorting his own poems "
            "into four kinds. The ones he ranked highest were the satirical "
            "poems, written about ordinary people's hardship. The ones readers "
            "actually loved were his long narrative poem and his occasional "
            "verse. ==What the age values, he wrote, is what I rank low==. Then "
            "he gave the reason: the satires are urgent in feeling and plain in "
            "language, and plainness is not what people warm to.",
        "f": [
            {"n": "He knew it at the time, not in hindsight",
             "d": "Usually this only becomes visible decades later. He had it "
                  "written down in his thirties: what they love and what I rate "
                  "are not the same set. He even diagnosed why - that kind of "
                  "poem speaks bluntly and runs hot, which is unpleasant.",
             "eg": "The proposal you were proudest of goes unmentioned while a "
                   "diagram you knocked out gets forwarded everywhere."},
            {"n": "Knowing it, he still did not reorder the list",
             "d": "The harder part is what comes next. He neither stopped writing "
                  "satires to suit his readers nor spent his life proving they "
                  "were better. He simply kept them first in his own ranking. The "
                  "order of the takings and the order in your head can differ.",
             "eg": "If you still rate the thing nobody applauded, do not strike "
                   "it off your own list because nobody applauded."},
            {"n": "Aim wide, act narrow",
             "d": "In the same letter he sets out his own resolution: the "
                  "ambition is to serve everyone, the practice is to keep himself "
                  "in order. That is not retreat. It separates two sizes, so "
                  "falling short of the ambition stops counting as abandoning it.",
             "eg": "You cannot fix the whole industry, but you can make your own "
                   "corner of it into something others can copy."},
            {"n": "The part they kept is also yours",
             "d": "He rated the long narrative poem low, but he wrote it. What "
                  "the world picked out came off the same bench as everything "
                  "else; it simply is not top of his own list. Granting that, you "
                  "need not disown the thing that did land.",
             "eg": "The work people remember may not be your favourite, and it is "
                   "still yours. Both can hold at once."},
            {"n": "He wrote it from the lowest point he reached",
             "d": "The letter dates from the year of his disgrace, not from a "
                  "comfortable retrospective. When least recognised, people tend "
                  "either to write themselves off or to write the world off. He "
                  "did neither. He totted up the account and went on writing.",
             "eg": "The judgement you record right after being turned down is "
                   "often worth more than the one you record on a good day."},
        ],
        "apply":
            "Where you are: the work you laboured over goes unwanted while "
            "something you tossed off is passed around.\n"
            "Ask first: is the ranking in my head still mine, or has the "
            "reception quietly rewritten it - because those two lists are allowed "
            "to differ.\n"
            "Where it goes wrong: using it to prove that whatever gets applause "
            "is shallow. He never says the public's taste is wrong. He says there "
            "are two lists, and that he knows which one is his.",
        "q": [
            "What the age values is what I rank low.",
            "The ambition is to serve everyone; the practice is to keep oneself in order.",
            "The order of the takings need not be the order in your head.",
            "He wrote it in the year he was demoted, not in a good one.",
        ],
    },
]

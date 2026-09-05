# -*- coding: utf-8 -*-
"""Records of the Grand Historian — English.

Sima Qian the man has his own page, and it is about why he chose to stay
alive long enough to finish this. These two pages are about the book instead
— the standard it set for what a record is allowed to leave out, and the one
place where it writes down that the author could not work something out.
"""

PARENT = {
    "name": "Records of the Grand Historian",
    "slug": "records-of-the-grand-historian",
    "blurb": "Deep read",
    "items": [
        {"k": "no-praise-no-hiding", "n": "No empty praise, nothing concealed",
         "w": "The credit and the damage in one paragraph", "ready": True,
         "line": "He wrote the men he admired, and how they wrecked things"},
        {"k": "i-am-confused", "n": "I find myself in much perplexity",
         "w": "Write down what you could not work out", "ready": True,
         "line": "The most honest sentence in the whole history"},
    ],
}

CHAPTERS = [
    {
        "k": "no-praise-no-hiding",
        "n": "No empty praise, nothing concealed",
        "w": "The credit and the damage in one paragraph",
        "src": "Ban Gu's assessment in the History of the Han; the "
               "biographies",
        "dek": "Six characters from a later historian, and still the standard "
               "for the form. What makes doing it so hard.",
        "story":
            "Ban Gu's verdict on the Records: the writing is straight, the "
            "facts checked, ==no empty praise and no concealment of evil, and "
            "so it may be called a true record.== The weight of that shows "
            "only in the entries. He wrote Li Guang as the general beneath "
            "whom a path wore itself smooth, and also as the man who put "
            "eight hundred men who had surrendered to death, and who cut his "
            "own throat after losing the way and missing the rendezvous. He "
            "wrote Huo Qubing's indifference to his soldiers. He wrote his "
            "own emperor hunting immortality.",
        "f": [
            {"n": "Concealing nothing is hardest about your own side",
             "d": "Recording the faults of people you dislike is easy. "
                  "Recording the faults of people you admire is very hard, "
                  "because it amounts to admitting your own judgement was not "
                  "pure. He plainly sympathised with Li Guang and set the "
                  "problems down anyway.",
             "eg": "Reviewing a project you pushed for, the part most easily "
                   "skipped is how badly the reasons you gave at the time "
                   "have aged."},
            {"n": "No empty praise is a protection for the reader",
             "d": "Write someone as flawless and the reader takes nothing "
                  "usable away, because flawless people do not exist and "
                  "there is no way to tell which part to copy. Set out where "
                  "a person was strong and how exactly they wrecked things, "
                  "and the record becomes usable.",
             "eg": "An internal case study with only the good parts teaches "
                   "nothing. Put the holes and the near-miss back in and it "
                   "turns into an asset."},
            {"n": "The standard has to bind the most powerful subject too",
             "d": "He wrote Emperor Wu while serving under Emperor Wu, "
                  "including the cost of the sacrifices, the magicians and "
                  "the campaigns. The credibility of any recording system is "
                  "decided by whether it still applies to the one person you "
                  "cannot afford to offend.",
             "eg": "Every incident review drives to root cause, except where "
                   "a senior executive's decision is involved and it becomes "
                   "external factors. After that, no review is worth "
                   "reading."},
        ],
        "q": [
            "No empty praise, no concealment of evil: therefore, a true "
            "record.",
            "Peach and plum trees do not speak, yet a path forms beneath "
            "them.",
            "Objectivity that stops at your own side is only selection.",
        ],
        "apply":
            "Where you are: you have to write something up, and a person or a "
            "decision you backed is inside it.\n"
            "Ask first: is there a line in this record I would rather not put "
            "down?\n"
            "Where it goes wrong: reading objectivity as severity towards "
            "enemies, and making one exception for the person you cannot "
            "afford to offend.",
    },
    {
        "k": "i-am-confused",
        "n": "I find myself in much perplexity",
        "w": "Write down what you could not work out",
        "src": "Records of the Grand Historian, Biography of Bo Yi",
        "dek": "He admits in the first of the biographies that he cannot work "
               "it out. Why those words outrank any conclusion.",
        "story":
            "In the Biography of Bo Yi he lays out a problem he cannot solve. "
            "The saying goes that Heaven's way has no favourites and always "
            "sides with the good man. Yet Bo Yi and Shu Qi, who kept "
            "themselves clean, starved to death; Yan Hui, who loved learning, "
            "died young; Robber Zhi killed innocent men daily, gathered "
            "thousands and ranged over the empire, and died of old age. So he "
            "writes: ==I find myself in much perplexity. Is this so-called "
            "Way of Heaven right, or is it wrong?== He supplies no answer.",
        "f": [
            {"n": "Admitting there is no answer beats supplying a false one",
             "d": "Forcing an unexplained thing into an existing explanation "
                  "is the cheapest move available and the most damaging, "
                  "because everyone after you will assume the matter is "
                  "settled and stop asking. Writing down that you do not "
                  "understand hands the question on intact.",
             "eg": "A post-mortem concluding that the main cause was poor "
                   "execution does far more harm than one saying the cause is "
                   "not yet understood. The first closes the file; the second "
                   "leaves a door."},
            {"n": "A perplexity has to be specific enough to be checked",
             "d": "His is not abstract doubt. It is three concrete cases held "
                  "against each other: Bo Yi, Yan Hui, Robber Zhi. Being "
                  "specific is what lets later people carry the question "
                  "forward. A vague sense that life is unfair is not a "
                  "question, only a sigh.",
             "eg": "Why do users not renew is a sigh. These three churned "
                   "accounts behaved in their final month exactly like the "
                   "ones who stayed is something you can chase."},
            {"n": "He put it first",
             "d": "Seventy biographies, and the one with no answer opens the "
                  "sequence. The placement is itself a statement: what "
                  "follows deals with a world where even basic cause and "
                  "effect is uncertain. Declare what you do not know first "
                  "and the rest can be trusted.",
             "eg": "An analysis that opens with which data are missing and "
                   "which conclusions are guesses is the one whose judgements "
                   "people dare to act on."},
        ],
        "q": [
            "I find myself in much perplexity.",
            "Is this so-called Way of Heaven right, or is it wrong?",
            "Robber Zhi killed the innocent daily and died of old age.",
        ],
        "apply":
            "Where you are: a review or an analysis contains a stretch you "
            "have not actually worked out.\n"
            "Ask first: am I about to give it a presentable explanation, or "
            "mark it and leave it for whoever comes next?\n"
            "Where it goes wrong: closing the inquiry with an all-purpose "
            "cause, or writing the perplexity as a sigh instead of as a "
            "comparison somebody could check.",
    },
]

# -*- coding: utf-8 -*-
"""Daily entry: Wei Zheng.

Picked by fan-out. 'Should I leave this job' was among the emptiest
situations on the Chinese side, and what hangs there is about whether to go,
what it is worth, and what you will become. Nothing says what to say when the
people you are joining ask about the time you were against them. Wei Zheng,
asked by Li Shimin why he had set brothers against each other, answered with
the one sentence he had actually said. The second chapter fills 'I don't
believe what my boss says' from the other end: the envoy who frees a prisoner
so that the pardon is true. The third fills 'Things are going well and it
scares me': a list of ten things to ask oneself, kept for good times.

The Li Shimin page already has Wei Zheng as the censor and has 'Hear all
sides' and 'the boat and the water'; none of those is repeated here.

All quoted lines are our own renderings of the Chinese, checked against the
Wikisource text of the Old Book of Tang, juan 71.

Three stories, no overlap: the entry is the banquet at the Danxiao tower; the
chapters are the question after Jiancheng's fall, the road at Cizhou and the
memorial on ten thoughts.

All situations already exist, so there is no SC_BOX here.
"""

ENTRIES = [
    {
        "c": "Power and organisation",
        "n": "Wei Zheng",
        "slug": "wei-zheng",
        "e": "Tang · 580–643",
        "w": "Plain speaking", "y": 580,
        "d": "A leading minister of the early Tang, with biographies in both "
             "Tang histories. He served Li Mi and Dou Jiande before ending "
             "up in the household of the Crown Prince Jiancheng, whom he "
             "urged to act early against Li Shimin. When Jiancheng fell, Li "
             "Shimin did not kill him but kept him as a censor, and over "
             "the years he made more than two hundred remonstrances. The "
             "Li Shimin page is about how a ruler listens; this one is "
             "about how Wei Zheng spoke: what to answer when an old "
             "position is held against you, what to do when a pardon is "
             "being broken below, and where people slacken first once "
             "things go well.",
        "story":
            "At a banquet, with the wine going round, Li Shimin said to "
            "Zhangsun Wuji: when I will not take Wei Zheng's advice, he "
            "stops answering me. Why? Wei Zheng said: I speak because "
            "the thing is wrong; if I answered every time you ignored me, "
            "it would be taken as agreed and done. Li Shimin said: you "
            "could agree for now and raise it again later. Wei Zheng "
            "quoted Shun's charge to his ministers, not to nod in "
            "the court and complain afterwards. If I agreed to your face "
            "and then remonstrated, that is complaining afterwards. Li "
            "Shimin laughed. People say Wei Zheng is rough in manner, he "
            "said; I only find him charming.",
        "f": [
            {"n": "Making a man dare to speak takes two people",
             "d": "After that answer Wei Zheng added: it is because you draw me out that I dare to speak; if you did not accept it, how would I dare to touch the dragon's scales again and again? He credited half of his courage to the other man's willingness to hear it.",
             "eg": "If you want people below you to tell the truth, look at how you reacted the last time someone pushed back."},
            {"n": "Say it to his face; do not just comply",
             "d": "He would not agree on the spot and raise it later, because that is two speeches. His way was: if he disagreed, he did not answer on the spot, so the other man knew the matter was still open.",
             "eg": "If you disagree in a meeting, do not nod and then send an objection afterwards. Say so while the room is still there."},
            {"n": "Use a precedent as a ladder",
             "d": "When the princess Changle was to marry, Taizong meant her dowry to be double that of her aunt, Princess Yongjia. Wei Zheng did not say no; he cited Emperor Ming of Han, who had said his sons could not equal those of the founder. Taizong gave way, and Empress Zhangsun sent four hundred thousand coins and four hundred bolts of silk to Wei Zheng's house.",
             "eg": "To stop your boss going over budget, do not argue principle: show him the rule he set himself last year."},
        ],
        "apply": "Pick one thing you recently disagreed with and nodded at. Go back and write down what you would have said out loud, not 'sure'. Then pick the last time someone told you no, and write down your first reaction; if you want him to do it again, that is the thing to change. Wei Zheng did both: not agreeing meant not answering, and when others disagreed he heard them out.",
        "q": [
            "It is because you draw me out that I dare to speak.",
            "Do not nod to his face and complain behind his back.",
            "They say he is rough in manner; I only find him charming.",
        ],
        "l": ["Li Shimin", "Yan Ying", "Duke Wen of Jin", "Xiao He"],
        "contrast": [
            {"n": "Yan Ying", "why": "Both said unwelcome things to their lords. Yan Ying went round it: the market price of crutches against shoes, and the duke cut the punishments himself. Wei Zheng said it to his face, and could, because Taizong was willing to be pushed and let him go on"},
            {"n": "Duke Wen of Jin", "why": "Duke Wen is the man whose old enemy comes knocking; Wei Zheng is the one who knocks, asked by Li Shimin about the past. The two pages look at the same meeting from either end"},
        ],
    },
]

INTROS = {
    "wei-zheng":
        "An early Tang minister who had once urged his prince to move against "
        "Li Shimin, and was kept by him as a censor - asked why he set "
        "brothers against each other, he said: if the prince had listened "
        "to me, there would be no disaster today",
}

SCENES = [
    ("Should I leave this job", "Dealing with people", [
        ("The new firm asks why I was against them.",
         [("wei-zheng", "if-he-had-listened")]),
    ]),
    ("I don't believe what my boss says", "Dealing with people", [
        ("They said no reprisals, and I see old scores being settled.",
         [("wei-zheng", "the-pardon-at-cizhou")]),
    ]),
    ("Things are going well and it scares me", "Getting it done", [
        ("I held on in the hard years; now that it is easier I am slackening.",
         [("wei-zheng", "begin-well-end-well")]),
    ]),
]

ASKS = {
    "wei-zheng/if-he-had-listened": "The new firm asks why I was against them.",
    "wei-zheng/the-pardon-at-cizhou": "They said no reprisals, and I see old scores being settled.",
    "wei-zheng/begin-well-end-well": "I held on in the hard years; now that it is easier I am slackening.",
}

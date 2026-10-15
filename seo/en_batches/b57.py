# -*- coding: utf-8 -*-
"""Daily entry: Liu Xiu (Emperor Guangwu of Han).

Picked by fan-out, on the Chinese side (the last Chinese entry was Wei Zheng,
three days ago, and the balance check is green). 'The one who has to go has
been with me longest' (9 pieces) had two answers, punish the old hand (Zhuge
Liang) or put the law above rank (Shang Yang); neither says what to do when
the answer is neither punishment nor dismissal but taking back power and
leaving rank. 'I can't find anyone good' had nothing on absorbing people
who have just joined and are all on guard against you.

Why he qualifies: founder of the Eastern Han, restored the Han dynasty; the
annals of Guangwu in the Book of the Later Han are a standard history.

Quoted lines are our own renderings of the Chinese in the Book of the Later
Han (annals of Guangwu; biographies of Jia Fu, Kou Xun and Liu Long).
Three stories, no overlap: the entry is Kou Xun and Jia Fu; the chapters are
the Tongma camps, the generals' commands and the clerk's tablet.
"""

ENTRIES = [
    {
        "c": "Power and organisation",
        "n": "Liu Xiu",
        "slug": "liu-xiu",
        "e": "Eastern Han · 5 BC–AD 57",
        "w": "Absorbing", "y": -5,
        "d": "Founder of the Eastern Han, known as Emperor Guangwu; his annals are in the Book of the Later Han. A distant kinsman of the Han house from Caiyang in Nanyang, he farmed before he took up arms. He took the throne in AD 25 and defeated Gongsun Shu in 36, and the empire was largely whole again. This page is not about his campaigns but about how he handled people: surrendered troops, veterans whose power had to be taken back, and a rule that was to check everyone.",
        "story":
            "A general of Jia Fu's killed a man in Yingchuan. Kou Xun, the "
            "prefect, arrested him and put him to death in the market. Jia Fu "
            "took it as an insult and said that when he met Kou Xun he would "
            "kill him with his own hands. Kou Xun refused to meet him and had "
            "every county on the way lay in food and wine, two portions per "
            "man. He rode out, greeted the column and went home sick. Jia Fu's "
            "soldiers were drunk and could not give chase. Guangwu summoned both. "
            "Jia Fu was already in the room and half rose to leave. The emperor "
            "told him that with the realm not yet settled, two tigers could not "
            "be left to bite each other in private, and that he would part them "
            "himself. They sat down together in good humour and left in one cart, "
            "friends.",
        "f": [
            {"n": "Find out what they fear before you act",
             "d": "After the Tongma surrender the men feared reprisals and being broken up. Liu Xiu did not begin with a speech; he rode through their camps. He dealt with what they were afraid of, not with what he wanted to say.",
             "eg": "After a merger, new colleagues are not unwilling; they do not know if their posts remain. Settle that first, then talk about targets."},
            {"n": "Take the power, not the man",
             "d": "In the thirteenth year of Jianwu the Left and Right Generals were abolished and 365 veterans had their fiefs raised or reassigned. Jia Fu and Deng Yu laid down their commands and received marquisates, Special Advancement and a seat in counsel. The army was taken; dignity and a voice were given.",
             "eg": "A co-founder steps back from the front line but keeps a board seat and the quarterly strategy meeting."},
            {"n": "Two key men are enemies: do not let them fight it out",
             "d": "He did not decide who was right. He first put the two in one room, then in one cart. The quarrel was over a man's life, and what he wanted was that it should not be carried outside.",
             "eg": "Two department heads will not give way: put them in one meeting before each starts lining up supporters in the group chats."},
            {"n": "The door left open in a rule",
             "d": "In the land survey he saw 'not to be asked' written on a clerk's tablet, pressed it, and found that the capital and his home region had been quietly left out. The result was uneven: a dozen officials died in prison, and the veteran Liu Long was only reduced to commoner. The gap in a rule tends to be nearest its author.",
             "eg": "A firm audits every department but nobody opens the founders' accounts."},
        ],
        "apply": "Pick someone you have meant to deal with and not done. Write down which one thing he most fears losing: power, rank or face. Then decide which of the three you must take, and whether the other two can be left intact. Jia Fu and Deng Yu gave up their commands and kept rank and voice; Liu Long was dismissed and kept his life.",
        "q": [
            "With the realm unsettled, two tigers must not fight in private. I part you today.",
            "The Prince of Xiao has put his heart in our bellies.",
            "Yingchuan and Hongnong may be questioned; Henan and Nanyang may not.",
        ],
        "l": ["Liu Bang", "Xiao He", "Feng Yi", "Zhuge Liang", "Wei Zheng"],
        "contrast": [
            {"n": "Liu Bang", "why": "Both were founders who had to deal with veterans. Under Liu Bang Han Xin was killed, Peng Yue was minced and Ying Bu was executed; under Liu Xiu Jia Fu and Deng Yu gave up their armies and got marquisates, Special Advancement and a seat in counsel. Liu Bang's page is about using people better than yourself; this one is about what to do with them afterwards"},
            {"n": "Zhuge Liang", "why": "Both acted against someone close: Zhuge Liang executed Ma Su, whom he valued, to keep military law; Liu Xiu, in the same survey, struck hard at governors without merit and left the veteran Liu Long a way out. One is about no favourites; the other about how closeness makes holes in a rule"},
        ],
    },
]

INTROS = {
    "liu-xiu":
        "Founder of the Eastern Han: when surrendered rebels were uneasy "
        "he rode through their camps with a light escort and they said he "
        "had put his heart in their bellies; when the war ended, his "
        "veterans gave up their commands for marquisates and a voice in "
        "counsel; and in a land survey he followed up a clerk's line saying "
        "two commanderies were not to be questioned",
}

SCENES = [
    ("The team has gone flat", "Leading people", [
        ("The people I took over are all guarding against me.",
         [("liu-xiu", "bare-heart")]),
    ]),
    ("Nobody believes there are consequences", "Leading people", [
        ("He has been with me longest and the post no longer fits.",
         [("liu-xiu", "retiring-the-generals")]),
        ("The rule I wrote first catches someone on my own side.",
         [("liu-xiu", "the-unaskable-counties")]),
    ]),
]

ASKS = {
    "liu-xiu/bare-heart": "The people I took over are all guarding against me.",
    "liu-xiu/retiring-the-generals": "He has been with me longest and the post no longer fits.",
    "liu-xiu/the-unaskable-counties": "The rule I wrote first catches someone on my own side.",
}

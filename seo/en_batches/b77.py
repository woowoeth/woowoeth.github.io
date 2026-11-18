# -*- coding: utf-8 -*-
"""Daily entry: Zigong.

From DAILY_QUEUE.md row 14. 'Too many paths' holds entries on cutting one option to keep the other
(Jobs, Simon, Kierkegaard). None says that money and purpose may not be a choice at all, and that the
question is what the money is for. The first chapter hangs there. The second chapter, on the ransom
he refused, hangs under 'I'm managing it and it's getting worse': a rule-by-example set so high that
nobody can follow it.

Why he qualifies: Duanmu Ci, styled Zigong, has his own biography in Sima Qian's Records (Disciples of
Confucius), is one of the ten leading disciples, was chief minister in Lu and Wei, and is named in the
Records' chapter on money-makers as the richest of the seventy disciples.

The entry story is his visit to the poor classmate Yuan Xian (Records, Disciples of Confucius); the
chapters are Analects 1.15 and the Lüshi Chunqiu ransom story. No translator's wording is quoted.
"""

ENTRIES = [
    {
        "c": "Money and risk",
        "n": "Zigong",
        "slug": "zigong",
        "e": "Spring and Autumn · Wei · born 520 BC",
        "w": "Money and purpose", "y": -480,
        "d": "Duanmu Ci, styled Zigong, a man of Wei thirty-one years younger than Confucius and one of his ten leading "
             "disciples. He was a fine speaker, served as chief minister in Lu and Wei, and traded on the side, buying "
             "low and selling with the times until his family held a thousand pieces of gold. Sima Qian calls him the "
             "richest of the seventy disciples. When Confucius died the others mourned three years and left; Zigong "
             "stayed by the grave three more. He is here because he did not choose between learning and money.",
        "story":
            "After Confucius died, his student Yuan Xian went to live in the wilds. Zigong, by then chief minister of Wei, "
            "came with a train of carriages, pushed through the weeds into the poor lane and called on him. Yuan Xian came "
            "out in a worn cap and robe. Zigong, embarrassed for him, asked whether he was ill. Yuan Xian said he had "
            "heard that having no money is called poverty, and learning the Way without living it is called illness. "
            "He was poor, not ill. Zigong left ashamed, and was ashamed of that remark for the rest of his life.",
        "f": [
            {"n": "He would not accept his lot",
             "d": "Confucius set him beside Yan Hui. Yan Hui was nearly there, and often had nothing at all. Zigong would not accept his lot, went into trade, and his guesses about the market were often right. Confucius did not call him vulgar; he said the two had taken different roads.",
             "eg": "Refusing to accept your lot and going out to earn is nothing to be ashamed of."},
            {"n": "Money spent on making his teacher seen",
             "d": "He travelled with teams of horses and bolts of silk as gifts to the lords, and wherever he went rulers received him as an equal. Sima Qian says it was Zigong, going ahead and following behind, who spread Confucius's name across the world.",
             "eg": "Let some of what you earn pave the way for the thing you care about most."},
            {"n": "My wall only comes to the shoulder",
             "d": "When a Lu minister said at court that Zigong was better than Confucius, Zigong used a wall. Mine reaches the shoulder, so anyone can look over and see the fine rooms. My teacher's is many times a man's height; without finding the gate you never see the temple or the officials inside.",
             "eg": "When someone says you have outgrown your teacher, ask whether they only saw the part outside the wall."},
        ],
        "apply": "This week write the thing you earn from and the thing you care about most on the same page, with a line "
                 "between them. Is the first doing anything for the second? If not, move a little money or time across.",
        "q": [
            "Poor is not the same as ill.",
            "Learning the Way without living it: that is illness.",
            "A wall to the shoulder lets everyone see in.",
        ],
        "l": ["The Analects", "Fan Li", "Bai Gui"],
        "contrast": [
            {"n": "Lu Buwei", "why": "Both were great merchants who spent money on lords. Lu Buwei staked everything on one man and was paid in power at the Qin court. Zigong spent his on spreading his teacher's name and stayed Confucius's student to the end. One bought a position; the other paved the way for something bigger than himself."},
        ],
    },
]

INTROS = {
    "zigong":
        "The richest of Confucius's students, a merchant and chief minister in Lu and Wei. He asked whether being rich "
        "without arrogance was enough and was told it was only a pass; he refused a ransom refund and was told he had "
        "got that wrong too",
}

SCENES = [
    ("Too many paths", "Looking back, moving on", [
        ("I want to earn more without becoming shallow.",
         [("zigong", "rich-and-courteous")]),
    ]),
    ("I'm managing it and it's getting worse", "Getting it done", [
        ("I led by working unpaid. Why has nobody followed?",
         [("zigong", "ransom-money")]),
    ]),
]

ASKS = {
    "zigong/rich-and-courteous": "I want to earn more without becoming shallow.",
    "zigong/ransom-money": "I led by working unpaid. Why has nobody followed?",
}

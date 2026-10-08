# -*- coding: utf-8 -*-
"""Xu Xiake, added for the personality test (2026-10-08).

The site owner asked for Xu Xiake by name. His standing: the Ming traveller
whose dated diaries of thirty years on the road became The Travel Diaries of
Xu Xiake; China's National Tourism Day (19 May) is the date of its first
entry. Two new situations: 'something went badly wrong halfway, do I turn
back?' and 'he is gone, do I still finish what he hoped for?'.

Three scenes, no overlap: the entry is the first day of the diary (stopping
for tigers), chapter one the robbery on the Xiang, chapter two Jingwen's
bones. All quoted lines are our own renderings of the diaries, checked
against the full text (Project Gutenberg #23876).
"""

ENTRIES = [
    {
        "c": "Learning and growth",
        "n": "Xu Xiake",
        "slug": "xu-xiake",
        "e": "Ming · Jiangyin · 1587-1641",
        "w": "The long road",
        "y": 1587,
        "d": "A Ming-dynasty traveller from Jiangyin who never took office. "
             "From his early twenties he set out on foot, and over thirty "
             "years crossed most of China, writing a dated diary of "
             "mountains, caves and rivers that became The Travel Diaries "
             "of Xu Xiake. This page leaves his geography aside and takes "
             "three judgements he made on the road: when disaster strikes "
             "halfway, ask whether you could ever leave again if you went "
             "home; when a companion falls, finish what he wanted, his "
             "way; and know which night to stop, so the road can be long. "
             "The surviving diary has no ending. It stops on an ordinary "
             "morning on Chicken Foot Mountain: cheese, pepper oil, plum "
             "vinegar, 'not lavish, but with a certain grace.'",
        "story": "His diary opens on the last day of the third month of "
                 "1613, leaving Ninghai by the west gate for Mount "
                 "Tiantai: the clouds scattered, the sun was bright, and "
                 "both the travellers and the hills looked glad. Thirty "
                 "li on, at Lianghuang Mountain, he heard that tigers on "
                 "the road were mauling dozens of people a month, so he "
                 "stopped for the night. The next morning it rained, and "
                 "he went on. That day is now China's National Tourism Day.",
        "f": [
            {"n": "He asked whether he could leave again",
             "d": "Robbed of everything on the Xiang river, he was told to go home and raise money. He reasoned that his family would never let him go again, borrowed in Hengzhou instead, and boarded another boat.",
             "eg": "Your project loses half its budget. Before pausing it, ask whether anyone will approve it again next year."},
            {"n": "He finished what his companion wanted",
             "d": "The monk Jingwen died in Nanning wishing to rest on Chicken Foot Mountain. Xu carried his bones for another year and buried them there, on the mountain Jingwen chose, not one on the way.",
             "eg": "Finishing a departed colleague's project, ship it to his design, not the version that is easier for you."},
            {"n": "He knew which night to stop",
             "d": "On the first day of a thirty-year journey he walked only thirty li and stopped because of tigers. Hold the direction firmly; let the pace stop whenever it must.",
             "eg": "A fever the night before your marathon? Pulling out costs one race, not the running."},
        ],
        "apply": "Pick something you have long wanted to set out on and "
                 "never started. Write three lines: how far the first day "
                 "has to go to count; what would make me stop for a night, "
                 "and what would make me turn back; and if I turned back, "
                 "could I ever leave again. He used the same judgement "
                 "every time: the direction rarely changes, the pace can "
                 "stop at any time.",
        "q": [
            "The clouds scattered, the sun was bright, the hills looked glad.",
            "If I go home now, my family will never let me leave again.",
            "To plan to come back for his bones was not his wish.",
        ],
        "l": ["Sima Qian", "Su Shi", "Zhuangzi", "Tao Yuanming"],
        "contrast": [
            {"n": "Sima Qian", "why": "Both crossed much of China and both turned their worst years into a book. Sima Qian travelled widely from the age of twenty and finished his history after castration; Xu was robbed and lost his companion and kept writing day by day. One recorded people, the other mountains and rivers"},
            {"n": "Tao Yuanming", "why": "Neither took the road of office. Tao went back to his own fields so as not to live against his heart; Xu went outward so as to see with his own eyes. One turned inward, the other set out, and both began by knowing what they wanted"},
        ],
    },
]

INTROS = {
    "xu-xiake": "A Ming-dynasty traveller who walked most of China over "
                "thirty years and kept a daily diary of it. Robbed of "
                "everything on the Xiang river, he borrowed money and got "
                "back on a boat instead of going home. When the monk who "
                "travelled with him died, he carried the bones for a year "
                "to the mountain the monk had wanted.",
}

SCENES = [
    ("Do I change direction now", "Looking back, moving on", [
        ("Something went badly wrong halfway. Do I turn back or keep going?",
         [("xu-xiake", "robbed-on-the-xiang")]),
    ]),
    ("Someone I needed is gone", "A turn in the road", [
        ("He's gone. Do I still finish the thing he was hoping for?",
         [("xu-xiake", "jingwens-bones")]),
    ]),
    ("Do I trust my gut", "Dealing with people", [
        ("Something felt off and I never said it out loud.",
         [("xu-xiake", "the-crying-child")]),
    ]),
    ("I'm the one who did wrong", "Things you don't say out loud", [
        ("Something I was trusted to look after got destroyed on my watch.",
         [("xu-xiake", "the-burned-books")]),
    ]),
    ("They've started watching me", "Dealing with people", [
        ("Everyone blamed me for holding them up.",
         [("xu-xiake", "the-night-we-waited")]),
    ]),
    ("I overthink everything", "How you're doing", [
        ("The road is long and I'm testing every single step.",
         [("xu-xiake", "step-by-step-in-snow")]),
    ]),
    ("Everyone is saying the same thing", "Dealing with people", [
        ("Everyone has said it for years, but it's not what I saw.",
         [("xu-xiake", "the-gazetteer-was-wrong")]),
    ]),
    ("I'm building something nobody asked for", "Getting it done", [
        ("Everyone else glances and moves on. I want to go all the way in.",
         [("xu-xiake", "beyond-the-guide")]),
    ]),
]

ASKS = {
    "xu-xiake/robbed-on-the-xiang":
        "Something went badly wrong halfway. Do I turn back or keep going?",
    "xu-xiake/jingwens-bones":
        "He's gone. Do I still finish the thing he was hoping for?",
    "xu-xiake/the-crying-child": "Something felt off and I never said it out loud.",
    "xu-xiake/the-burned-books": "Something I was trusted to look after got destroyed on my watch.",
    "xu-xiake/the-night-we-waited": "Everyone blamed me for holding them up.",
    "xu-xiake/step-by-step-in-snow": "The road is long and I'm testing every single step.",
    "xu-xiake/the-gazetteer-was-wrong": "Everyone has said it for years, but it's not what I saw.",
    "xu-xiake/beyond-the-guide": "Everyone else glances and moves on. I want to go all the way in.",
}

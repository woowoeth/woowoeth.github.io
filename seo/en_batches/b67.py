# -*- coding: utf-8 -*-
"""Daily entry: Chen Ping.

From DAILY_QUEUE.md row 4. 'Should I leave this job' holds Boyd, Zhang Yiming,
Hirschman, Becker, Wei Zheng and others on whether to go and what you are worth. Nothing on
how to walk out, or on what to say when the next place asks why you keep changing sides.

Why he qualifies: Han dynasty chancellor with his own hereditary house in the Records of the
Grand Historian, one of the founding strategists of the Han.

The entry story is the village sacrifice where he divided the meat; the chapters are the escape
and the cross-examination.
"""

ENTRIES = [
    {
        "c": "Reading people",
        "n": "Chen Ping",
        "slug": "chen-ping",
        "e": "Western Han · d. 178 BC",
        "w": "Leaving clean", "y": -205,
        "d": "Chancellor of the early Han, with a hereditary house of his own in the Records of the Grand "
             "Historian. He served the king of Wei, then Xiang Yu, then Liu Bang, advised Liu Bang in the war "
             "against Xiang Yu, and after the empress dowager Lü died he joined Zhou Bo in destroying her clan "
             "and installing Emperor Wen. This page takes one stretch only: how he left Xiang Yu, and how he "
             "answered, in Liu Bang's camp, the charge that he changed sides too often.",
        "story":
            "Chen Ping grew up on thirty mu of land, with his elder brother farming while he studied. One year, "
            "at the village sacrifice, he was put in charge of carving the meat, and he divided it so evenly "
            "that the elders praised him. He sighed and said that if he were given the running of the "
            "world, he would divide it just like this meat.",
        "f": [
            {"n": "Leave what is not yours",
             "d": "He sealed the gold and seal of office his old master gave him and sent them back. Nothing of Xiang Yu's went with him, which left his old master one less thing to say about him.",
             "eg": "Hand over accounts, files and client lists before you go."},
            {"n": "Answer suspicion where they can see",
             "d": "A boatman suspected him of carrying valuables, and he took his clothes off to help pole the boat. Doubt cannot be talked away; it has to be answered with something the other person's eyes can check.",
             "eg": "If they suspect you took data, go through the handover list with them."},
            {"n": "Have something to be tested on",
             "d": "Liu Bang asked why he should be trusted, and Chen Ping said to use his plans if useful and hand the gold in if not. He could say it because he really had plans to deliver.",
             "eg": "Say you will deliver one concrete thing in your first three months."},
        ],
        "apply": "This week, list the things you hold that were given to you by someone else: accounts, files, keys, "
                 "client lists. If you ever leave, that list is your sealed gold and seal.",
        "q": [
            "Hand back what is not yours before you go.",
            "When they doubt you, let them see for themselves.",
            "Have something to be checked before you invite the check.",
        ],
        "l": ["Liu Bang", "Zhang Liang", "Fan Li"],
        "contrast": [
            {"n": "Fan Li", "why": "Fan Li left at the top, with the work done and the time of his choosing. Chen Ping left in fear, with nothing but his clothes. For one, leaving was about when; for the other, only how."},
        ],
    },
]

INTROS = {
    "chen-ping":
        "Strategist of the early Han - afraid of Xiang Yu, he sealed up the "
        "gold and seal he had been given, sent them back and fled to Liu Bang",
}

SCENES = [
    ("Should I leave this job", "Dealing with people", [
        ("I'm leaving. How do I go without handing them anything to say about me?",
         [("chen-ping", "return-the-seal")]),
        ("I've changed jobs a few times. Why should my new boss trust me?",
         [("chen-ping", "let-them-check")]),
    ]),
]

ASKS = {
    "chen-ping/return-the-seal": "I'm leaving. How do I go without handing them anything to say about me?",
    "chen-ping/let-them-check": "I've changed jobs a few times. Why should my new boss trust me?",
}

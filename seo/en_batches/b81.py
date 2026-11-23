# -*- coding: utf-8 -*-
"""Daily entry: Duke Huan of Qi.

Picked the old way (the queue in DAILY_QUEUE.md is finished and the next batch is not yet approved).
Among the emptiest scenes are 'Someone is being unreasonable' and 'I trusted the wrong person'. None of the
unreasonable-people pieces asks whether a promise extracted by force still binds; none of the trust pieces
names devotion that costs someone their own family as the warning sign.

Why he qualifies: the first hegemon of the Spring and Autumn period, who with Guan Zhong 'gathered the lords
nine times and set the realm in order'; his life is told in Sima Qian's Hereditary House of Taigong of Qi.

Everything follows that chapter. The entry story is the arrow that struck his belt hook and his race home;
the chapters are the covenant at Ke and Guan Zhong's deathbed warning.
"""

ENTRIES = [
    {
        "c": "Power and organisation",
        "n": "Duke Huan of Qi",
        "slug": "qi-huangong",
        "e": "Spring and Autumn · Qi · died 643 BC",
        "w": "Keeping faith", "y": -685,
        "d": "Duke Huan of Qi, personal name Xiaobai, ruled the state of Qi for forty-three years from 685 BC. He made "
             "Guan Zhong, the man who had once shot an arrow at him, his chief minister, and became the first "
             "hegemon of the Spring and Autumn period. Everything here follows Sima Qian. He is here for two "
             "situations: whether a promise forced out of you still binds, and what to make of someone who is "
             "too devoted. He got the first right and the second wrong.",
        "story":
            "Qi was in turmoil, its rulers killed one after another, and two exiled princes raced home to claim it. "
            "Lu sent Guan Zhong with troops to block the road, and his arrow struck Prince Xiaobai on the belt hook. "
            "Xiaobai played dead. Guan Zhong sent word to Lu, and the party escorting the rival prince slowed down; "
            "by the time it arrived six days later, Xiaobai was already in the capital and on the throne. He then "
            "demanded that Lu hand Guan Zhong over so he could have him chopped to pieces. What he actually meant "
            "to do was employ him.",
        "f": [
            {"n": "One sentence changed his mind",
             "d": "Bao Shuya told him: to govern Qi, Gao Xi and I are enough; to lead the realm, you need Guan Zhong. The duke let go of the arrow, made Guan Zhong a high officer and handed him the government.",
             "eg": "The person you most want to punish may be the one the job most needs. Decide which you are after."},
            {"n": "When they say you need not bow",
             "d": "At the gathering at Kuiqiu the Zhou king sent sacrificial meat and said the duke need not bow. He was ready to accept it so; Guan Zhong said no, and he bowed. Later that year, Sima Qian says, he grew prouder, and lords began to drift away.",
             "eg": "When a superior says there is no need for formality between you, keep the formality anyway."},
            {"n": "The moment he wanted a ceremony",
             "d": "He counted his achievements, nine gatherings of the lords and the realm set right, and wanted to perform the great sacrifice at Mount Tai. Guan Zhong argued and failed, then said the rite needed rare tribute from distant lands first. Only then did the duke drop it.",
             "eg": "The moment you most want to celebrate yourself is when you most need someone willing to stop you."},
        ],
        "apply": "This week list the three people around you who agree with you most. Beside each, write when they last "
                 "told you something would not work. For the one you cannot remember, take them a decision you are unsure "
                 "about next week and see whether they dare say no.",
        "q": [
            "The man who shot at him became his minister.",
            "When they say you need not bow, bow anyway.",
            "The urge to celebrate is when you need a brake.",
        ],
        "l": ["Guan Zhong", "Duke Wen of Jin", "Records of the Grand Historian"],
        "contrast": [
            {"n": "Duke Wen of Jin", "why": "Both were hegemons, and both employed men who had tried to harm them: Guan Zhong's arrow hit Xiaobai's belt hook, the eunuch Pi cut off Chong'er's sleeve. They part on listening. Chong'er kept listening to the people who pushed back. Duke Huan listened to Guan Zhong for forty years and ignored him the one time it mattered most, keeping only the men who pleased him."},
        ],
    },
]

INTROS = {
    "qi-huangong":
        "The first hegemon of ancient China. Guan Zhong once shot him and he made Guan Zhong his minister; forced "
        "at knife point to give back land, he gave it back; warned on Guan Zhong's deathbed against three "
        "favourites, he kept them, and his body lay unburied for sixty-seven days",
}

SCENES = [
    ("Someone is being unreasonable", "Dealing with people", [
        ("I was forced into agreeing. Do I still have to keep it?",
         [("qi-huangong", "forced-promise")]),
    ]),
    ("I trusted the wrong person", "Dealing with people", [
        ("He was too good to me. Why didn't I see it?",
         [("qi-huangong", "against-nature")]),
    ]),
]

ASKS = {
    "qi-huangong/forced-promise": "I was forced into agreeing. Do I still have to keep it?",
    "qi-huangong/against-nature": "He was too good to me. Why didn't I see it?",
}

# -*- coding: utf-8 -*-
"""Chen Ping — English.

English readers rarely meet him; those who do know a schemer of the Han founding. This page
takes one stretch of Sima Qian's Records, his move from Xiang Yu to Liu Bang, and asks two
plain questions: how do you leave when you have to, and what do you say when the new place asks
why you have changed sides so often. Everything here is paraphrase of the Records; no
translation is quoted.
"""

PARENT = {
    "name": "Chen Ping",
    "slug": "chen-ping",
    "blurb": "Deep read",
    "items": [
        {"k": "return-the-seal", "n": "Seal the Gold and Send It Back",
         "w": "When you have to leave, leave behind what is not yours",
         "ready": True,
         "line": "Afraid Xiang Yu would kill him, he sealed up the gold and seal of office, sent them back and fled alone"},
        {"k": "let-them-check", "n": "The Gold Is All Here",
         "w": "Asked why you keep changing sides, hand over something they can check",
         "ready": True,
         "line": "Called unreliable by the old generals, he swore no oath and offered to hand in the gold if his plans failed"},
    ],
}

CHAPTERS = [
    {
        "k": "return-the-seal", "n": "Seal the Gold and Send It Back",
        "w": "When you have to leave, leave behind what is not yours",
        "src": "Sima Qian, Records of the Grand Historian, 'Hereditary House of Chancellor Chen'",
        "dek": "He ran because he was frightened. This asks how to leave when you have no choice.",
        "story":
            "Chen Ping served Xiang Yu and was rewarded with gold after a campaign. "
            "Soon the Han king took the same territory, and Xiang Yu, furious, "
            "moved to punish the officers who had won it. Chen Ping panicked. He sealed "
            "up the gold and his seal of office, sent them back, and slipped away alone "
            "with a sword to join Liu Bang. Crossing a river, the boatman took him for a "
            "deserter with valuables and eyed him for the kill. "
            "==Chen Ping stripped off his clothes and helped pole the boat==, and the boatman, "
            "seeing he carried nothing, let it go.",
        "f": [
            {"n": "Do not carry off what your old master gave you",
             "d": "The gold and the seal were Xiang Yu's. Taking them would make him a man who ran with the goods. He sent them back and left with nothing of his old master's. Whether he planned it as insurance, the Records do not say.",
             "eg": "Before you resign, hand over accounts, files and client lists and leave them behind."},
            {"n": "Suspicion is answered with what people can see",
             "d": "Saying he had no money would only have sounded like hiding it. He took his clothes off and let the boatman see. Suspicion lives in the eyes, so it has to be answered where the eyes can reach.",
             "eg": "If someone suspects you of taking data, put the handover list on the table and go through it line by line."},
            {"n": "Leaving cleanly is not the same as leaving well",
             "d": "He left out of fear, not because he had worked out where to go. In Liu Bang's camp he had to prove himself all over again, which is the next chapter. This one takes only how he went, not why.",
             "eg": "A tidy exit from one job does not mean you chose the next one well; ask both questions."},
        ],
        "apply":
            "Where you are: you have decided to go, or you are being pushed.\n"
            "Ask first: what do I hold that this place gave me and that is not mine? Is there anything people might say I took?\n"
            "Where it goes wrong: treating a clean exit as the whole job. He ran from danger, not toward a plan, and a new set of doubters was waiting.",
        "q": [
            "Hand back what is not yours before you go.",
            "Answer suspicion with what they can see.",
            "A clean exit is not a good destination.",
        ],
    },
    {
        "k": "let-them-check", "n": "The Gold Is All Here",
        "w": "Asked why you keep changing sides, hand over something they can check",
        "src": "Sima Qian, Records of the Grand Historian, 'Hereditary House of Chancellor Chen'",
        "dek": "The new camp thought he changed masters too often. This asks what to say when they ask why they should trust you.",
        "story":
            "Chen Ping joined Liu Bang and was made a commander that same day, overseeing the generals. "
            "The veterans erupted: a deserter from yesterday! Zhou Bo and Guan Ying added that he looked "
            "fine but was hollow inside, was rumoured to have wronged his sister-in-law, and had already "
            "left Wei and Chu. Liu Bang asked him directly. ==Chen Ping swore nothing. His old masters "
            "could not use him, he said; he took the gold for lack of money; use his plans if they were "
            "good, and if not, the gold was all there, to be sealed and handed in.== Liu Bang apologised "
            "and gave him charge of all the generals.",
        "f": [
            {"n": "A reference speaks to skill, not character",
             "d": "Wei Wuzhi, who had recommended him, told Liu Bang he had vouched for ability, while Liu Bang was asking about conduct, and in a war conduct does not decide the outcome. Use the line with care: he was saying what the moment needed, not that character does not matter.",
             "eg": "Asked why you changed jobs, state what each move produced and what you can bring, rather than only saying you are steady."},
            {"n": "Speak of your old place only in checkable terms",
             "d": "He said Wei's king would not use his advice and Xiang Yu trusted no one outside his own clan. That is about how they used people, not about their character, and Liu Bang could verify it by asking around. He did not deny taking gold; he explained why.",
             "eg": "Asked why you left, say that team had no use for the work you do best, not that the boss was bad."},
            {"n": "Hand them the means to check you",
             "d": "His last words: use my plans if they are useful; if not, seal the gold, hand it in and let me go. Keep me if I am of use, send me off if not, money returned. He gave the other side the switch. It stood because he really did have plans to deliver.",
             "eg": "At the start of a job, say you will hand over one concrete result in three months and they can decide on that."},
        ],
        "apply":
            "Where you are: you have changed jobs several times and the new people murmur about it.\n"
            "Ask first: what are they really afraid of, and can I hand them one thing they can check themselves?\n"
            "Where it goes wrong: using this as licence to run down the old employer, or to deny everything. He admitted taking the gold and made nothing up, and he had plans to deliver. With nothing to check, do not offer the line.",
        "q": [
            "They fear misjudging you, not your CV.",
            "Speak of the old place only as far as they can check.",
            "Have something to test before you invite the test.",
        ],
    },
]

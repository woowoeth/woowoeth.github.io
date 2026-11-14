# -*- coding: utf-8 -*-
"""Daily entry: Zhang Qian.

From DAILY_QUEUE.md row 10. 'Do I jump in now' holds entries on whether to follow the crowd, go now or
wait, enter a small market, arrive late, bet without certainty, and test a claim. None of them says what
is left if you go in first and the original goal turns out to be impossible. The second chapter is hung
on 'It still hasn't worked': ten years stuck halfway, and what he kept.

Why he qualifies: biography in Sima Qian's Records of the Grand Historian (ch. 123) and the Book of Han;
the first Han envoy to the Western Regions, whose journey Sima Qian called 'opening the void'.

The entry story is his second mission (to the Wusun) and its aftermath; the chapters are the first
journey's outcome and his years as a captive.
"""

ENTRIES = [
    {
        "c": "Starting and building",
        "n": "Zhang Qian",
        "slug": "zhang-qian",
        "e": "Western Han · d. 114 BCE",
        "w": "Going first", "y": -123,
        "d": "Western Han envoy who went west twice, with a biography in Sima Qian's Records of the Grand "
             "Historian. Sent by Emperor Wu to recruit the Yuezhi against the Xiongnu, he was held captive for "
             "over ten years, escaped, found the Yuezhi unwilling to fight, and came home with an account of "
             "a dozen kingdoms nobody in Han had seen. He is here for 'Do I jump in now', where nothing yet "
             "says what is left when you go in first and the original goal fails.",
        "story":
            "Arriving late to a battle against the Xiongnu, Zhang Qian was sentenced to death, paid a ransom, "
            "and lost his title. He then proposed to the emperor that the Wusun in the far west could be won "
            "over. He was sent again with three hundred men, two horses each, herds in the tens of thousands "
            "and a fortune in gold and silk. The Wusun would not move east, so he sent his deputies on to other "
            "kingdoms. He died about a year after returning. A year later the deputies began arriving with "
            "envoys from those kingdoms.",
        "f": [
            {"n": "Others travelled under his name",
             "d": "After his death, Han envoys going west all called themselves by his title, the Marquis of Bowang, to win trust abroad, and it worked. The first one through leaves a road and also a credit others can borrow.",
             "eg": "In a new industry, the first firm known for keeping its word lets later firms skip rounds of negotiation by citing it."},
            {"n": "A road inferred from a walking stick",
             "d": "In Bactria he saw bamboo canes and cloth from Shu, in the southwest of Han, and was told merchants bought them in India. He reasoned that India could not be far from Shu. The emperor sent men to find that road; hill peoples blocked them and it was never opened.",
             "eg": "On a shelf in a foreign market, notice the thing that should not be there, and ask how it arrived."},
            {"n": "After the disgrace, his knowledge was the asset",
             "d": "Stripped of his title, he did not recover by begging. He recovered because he knew better than anyone which kingdoms lay west and how each stood with the Xiongnu. What the failed first trip gathered paid for the second.",
             "eg": "When the project dies and the role goes with it, what you learned on the front line is often what you still own."},
        ],
        "apply": "Today, write three lines about the new thing you are working on: the original goal; if it fails, "
                 "what this trip can still bring back; and where you are recording what you see.",
        "q": [
            "Every envoy after him spoke in his name.",
            "The first one through leaves trust behind.",
            "He lost the title and kept the map.",
        ],
        "l": ["Emperor Wu of Han", "Duan Yongping", "Xu Xiake"],
        "contrast": [
            {"n": "Duan Yongping", "why": "Duan Yongping prefers to come second, entering only once the ground is clear. Zhang Qian went first, when even the Yuezhi's location was hearsay. One warns you off racing to be first; the other says that if you do go first, expect the original goal to fail and be ready to live on what you recorded along the way."},
        ],
    },
]

INTROS = {
    "zhang-qian":
        "Han envoy sent west to recruit an ally against the Xiongnu - held captive for over ten years, he "
        "never gave up the envoy's tally, found the ally unwilling, and brought back the first account of a dozen kingdoms",
}

SCENES = [
    ("Do I jump in now", "AI arrived", [
        ("Nobody has gone this way. What if I go and it's for nothing?",
         [("zhang-qian", "two-came-back")]),
    ]),
    ("It still hasn't worked", "Nothing's moving", [
        ("I've been stuck halfway for years. Do I still go on?",
         [("zhang-qian", "hold-the-tally")]),
    ]),
]

ASKS = {
    "zhang-qian/two-came-back": "Nobody has gone this way. What if I go and it's for nothing?",
    "zhang-qian/hold-the-tally": "I've been stuck halfway for years. Do I still go on?",
}

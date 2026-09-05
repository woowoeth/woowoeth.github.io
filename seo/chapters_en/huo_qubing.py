# -*- coding: utf-8 -*-
"""Huo Qubing — English.

The English reader arrives, if at all, with a Chinese boy-general anecdote and
no way to test it. This page is not a biography. It takes the two operational
choices the sources actually record — refusing the received manuals, and
cutting the supply line loose — and treats them as decisions with prices,
including the one the same chapter records him failing to pay.
"""

PARENT = {
    "name": "Huo Qubing",
    "slug": "huo-qubing",
    "blurb": "Deep read",
    "items": [
        {"k": "no-old-manuals", "n": "Never mind the old manuals",
         "w": "Read the ground, not the book", "ready": True,
         "line": "The emperor offered to teach him the classics. He said they would not help"},
        {"k": "feeding-off-the-enemy", "n": "Feed off the enemy",
         "w": "A supply line is also a leash", "ready": True,
         "line": "Carry no grain and you can reach where nobody else can"},
    ],
}

CHAPTERS = [
    {
        "k": "no-old-manuals",
        "n": "Never mind the old manuals",
        "w": "Read the ground, not the book",
        "src": "Records of the Grand Historian, Wei Qing and Huo Qubing",
        "dek": "The emperor offered to teach him the classics of war and he "
               "declined. The question is whether that was arrogance or "
               "judgement.",
        "story":
            "Emperor Wu wanted to teach him Sun Tzu and Wu Qi. Huo Qubing "
            "answered that ==what matters is how the plan for this campaign "
            "is drawn, and there is no need to study the old military "
            "texts.== The line has been read as a boy's arrogance for two "
            "thousand years. His campaigns say otherwise. At seventeen he "
            "took eight hundred riders hundreds of li beyond the main army; "
            "at nineteen he ran two long flanking marches through the Hexi "
            "corridor; at twenty-one he reached Mount Langjuxu. Han doctrine "
            "was infantry and cavalry together, advancing along a grain road. "
            "His war was all cavalry, long range, and had no rear.",
        "f": [
            {"n": "A manual encodes the last generation's constraints",
             "d": "Sun Tzu and Wu Qi were written when the mass of an army "
                  "was infantry and chariots and the grain road set the "
                  "marching radius. Huo Qubing had decades of imperial "
                  "horse-breeding behind him. The tools had changed, so the "
                  "best answer had changed, and the book holds the old one.",
             "eg": "The growth playbook everyone copies was built when "
                   "attention was cheap. Copy it faithfully now and you fail "
                   "faithfully."},
            {"n": "Refusing the template is not refusing to think",
             "d": "The weight of his answer falls on the word plan. He did "
                  "not fight on instinct; he drew a fresh scheme for every "
                  "campaign. What he threw out was the general template, not "
                  "the work. People collapse the two, and only the second is "
                  "actually arrogance.",
             "eg": "We ignore the competition and go our own way is a "
                   "judgement when a worked-out model sits behind it, and "
                   "laziness when nothing does."},
            {"n": "The method came with the man attached",
             "d": "No rear, high intensity, raids run back to back: this asks "
                  "for a body and a tolerance of risk almost nobody has, and "
                  "it forbids caution. Which is why it never transferred. "
                  "Hand the same tactics to an older and steadier general and "
                  "they do not execute.",
             "eg": "The punishing pace a founder can carry usually stops "
                   "working once the team doubles and the original people "
                   "have gone."},
        ],
        "q": [
            "What matters is the plan for this campaign, not the old texts.",
            "A manual is the best answer to a problem you no longer have.",
            "Refusing the template is not the same as refusing to think.",
        ],
        "apply":
            "Where you are: a ready-made methodology is sitting there and "
            "something about it feels wrong.\n"
            "Ask first: are the conditions that made this method work still "
            "in place today? Name them one by one and check.\n"
            "Where it goes wrong: treating not copying as not needing a plan; "
            "and pushing a method welded to one particular person as though "
            "it were general.",
    },
    {
        "k": "feeding-off-the-enemy",
        "n": "Feed off the enemy",
        "w": "A supply line is also a leash",
        "src": "Records of the Grand Historian, Wei Qing and Huo Qubing",
        "dek": "The hard limit on any long march is grain. This one is about "
               "how he took the limit away altogether.",
        "story":
            "The Records compress his method into one line: ==he took his "
            "food from the enemy, and so marched extraordinarily far without "
            "his grain ever running out.== Han expeditions were governed by "
            "the grain road, and the marching radius was set by the distance "
            "from the rear. He swapped the constraint out: no baggage train, "
            "resupply from the Xiongnu camps he broke on the way. That is "
            "what made a raid of two thousand li possible. The same chapter "
            "records the other half of him. Sent out with dozens of carts of "
            "palace food, he came home throwing away fine grain and meat "
            "while his own soldiers went hungry.",
        "f": [
            {"n": "A supply line is a lifeline and a tether",
             "d": "A grain road gives you a radius, and a radius gives the "
                  "other side a number he can compute. Giving it up costs you "
                  "safety and buys something else: he can no longer predict "
                  "you. He deploys against your supply capacity, and you "
                  "appear where his arithmetic says you cannot be.",
             "eg": "A branch that clears every move with head office moves at "
                   "head office tempo, which a rival can read straight off a "
                   "calendar."},
            {"n": "Living off the land means winning every time",
             "d": "The hidden premise is that every encounter must be won, "
                  "won quickly, and won with enough taken. Lose once, or win "
                  "slowly, and the column starves within days. So it is not "
                  "the easy option. It moves the risk out of logistics and "
                  "into fighting strength.",
             "eg": "Funding expansion from the cash each new market throws "
                   "off works only while every market turns positive fast. "
                   "One that does not breaks the whole chain."},
            {"n": "The same chapter records what he was bad at",
             "d": "Raised at court, high-born, careless of his men: he did "
                  "not know what the ranks were going through, and threw good "
                  "food away rather than share it. Extreme tactical skill and "
                  "neglect of the people carrying it sat inside one man, and "
                  "the historian let both stand.",
             "eg": "The manager with the best numbers on the floor can also "
                   "have the worst attrition. Read only one of those facts "
                   "and you will staff the next team wrong."},
        ],
        "q": [
            "He took his food from the enemy and never ran short.",
            "A supply line gives you a radius. A radius can be computed.",
            "This is not the safe option. The risk has only moved.",
        ],
        "apply":
            "Where you are: an expansion is about to stretch the supply line "
            "and you are working out how far it will reach.\n"
            "Ask first: if this had to live off what it takes, could I "
            "guarantee a fast win every single time?\n"
            "Where it goes wrong: assuming that carrying no grain has only "
            "upsides; and letting one person's results settle the question of "
            "how he runs a team.",
    },
]

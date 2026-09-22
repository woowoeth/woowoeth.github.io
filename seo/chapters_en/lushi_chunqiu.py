# -*- coding: utf-8 -*-
"""The Annals of Lu Buwei - English.

An English reader who has heard of this book at all has heard of it as a
Qin-dynasty curiosity: a compendium bankrolled by a merchant-minister, hung
on a market gate with a thousand gold pieces on top. These three chapters do
something else with it. They take the places where the book stops compiling
and starts insisting on a single move - do not trust the impression, do not
trust the sentence you were handed, do not trust your own last survey.
"""

PARENT = {
    "name": "The Annals of Lu Buwei",
    "slug": "lushi-chunqiu",
    "blurb": "Deep read",
    "items": [
        {"k": "eight-observations",
         "n": "Stop reading the impression; change his position",
         "w": "Eight observations and six tests, and the cheap ones come last",
         "ready": True,
         "line": "Six of them wait until he has something to give; two cost you nothing"},
        {"k": "hearing-must-be-checked",
         "n": "Nobody lied and the sentence is still false",
         "w": "Passed along, white turns black: the distortion rides on the telling",
         "ready": True,
         "line": "A dog resembles a macaque, a macaque a monkey, a monkey a man"},
        {"k": "the-water-has-risen",
         "n": "What you know is last season's water level",
         "w": "Wading by old markers: the homework was done and it expired",
         "ready": True,
         "line": "They set the markers themselves, and the markers were right when set"},
    ],
}

CHAPTERS = [
    {
        "k": "eight-observations",
        "n": "Stop reading the impression; change his position",
        "w": "Eight observations and six tests, and the cheap ones come last",
        "src": "The Annals of Lu Buwei, 'Judging Men', in the almanac of the third month of spring",
        "dek": "I keep misreading people and see the tells only afterwards. This chapter says an impression is not evidence.",
        "story":
            "'Judging Men' offers no art of reading faces. It offers a list "
            "of positions. When a man is prosperous, watch whom he treats "
            "with ceremony; when honoured, whom he puts forward; when rich, "
            "whom he keeps; when listened to, what he does; at rest, what he "
            "enjoys; among intimates, what he says. All six wait until he "
            "has something to give. The cheap two come last: ==when he is "
            "poor, watch what he refuses; when he is low, watch what he will "
            "not do==.",
        "f": [
            {"n": "It asks about the position, not the character",
             "d": "Not one clause in the list rates the man as good or bad. "
                  "Each asks where he is standing right now and which face "
                  "that position pulls out of him. Change the position and "
                  "you change what is worth watching.",
             "eg": "His first six months after a promotion tell you more "
                   "than his whole CV."},
            {"n": "The two cheapest tests are the last two",
             "d": "The first six wait for him to have something to give, to "
                  "recommend, to keep, which is expensive to arrange. These "
                  "two only watch what he turns down when money is tight and "
                  "what he will not do from a low seat. They cost nothing "
                  "and are hard to fake for long.",
             "eg": "Before the deal starts, see whether he will report a "
                   "number that hurts him."},
            {"n": "Six tests: feeling is the developer",
             "d": "Delight tests what he holds to, pleasure what he leans "
                  "towards, anger his restraint, fear his singularity, grief "
                  "his humanity, hardship his resolve. Everyone is decent "
                  "while calm. It does not ask you to provoke anyone, only "
                  "not to miss the moments that arrive on their own.",
             "eg": "The week the project died, you saw the truest version of "
                   "him."},
            {"n": "Before the eight outside, ask the few inside",
             "d": "The chapter adds six kin and four confidants: father, "
                  "mother, brothers, wife, children, then friends, old "
                  "acquaintances, neighbours and dependants. Nearest and "
                  "furthest are used together, for a plain reason. The outer "
                  "layer is the part that can be performed for you.",
             "eg": "What three years of colleagues say beats three hours of "
                   "interview."},
            {"n": "It assumes from the start that you will be wrong",
             "d": "The premise is not that the method makes you infallible "
                  "but that one look does not count. Eight positions and six "
                  "feelings are fourteen samples that do not depend on each "
                  "other. No single one is enough; what you want is "
                  "agreement among them.",
             "eg": "You have only seen him with the wind behind him, so hold "
                   "the verdict."},
        ],
        "apply":
            "Where you are: someone burned you once, and now you hold "
            "something back from everybody, which is both tiring and "
            "costly.\n"
            "Ask first: how many different kinds of occasion does my read of "
            "him come from - if they are all one kind, that is one sample, "
            "not five.\n"
            "Where it goes wrong: read as a script for catching people out, "
            "aimed at the two clauses about poverty and low station. It "
            "describes watching, not staging. Manufacture a hardship to test "
            "someone and what you learn is about you.",
        "q": [
            "What he wants is easy to fake; what he refuses is not.",
            "A face seen only in good weather is one sample.",
            "One correct read is luck; fourteen samples is a judgement.",
        ],
    },
    {
        "k": "hearing-must-be-checked",
        "n": "Nobody lied and the sentence is still false",
        "w": "Passed along, white turns black: the distortion rides on the telling",
        "src": "The Annals of Lu Buwei, 'Examining What Is Transmitted', in the discourses on circumspect conduct",
        "dek": "Everything reported to me is true and something is still wrong. This chapter says sentences deform in transit.",
        "story":
            "A Ding family in Song had no well and kept one person "
            "permanently outside fetching water. When they finally dug one, "
            "the head of the house said: we dug a well and got one man. A "
            "hearer passed it on as the Dings dug a well and found a man in "
            "it. The whole state repeated it until it reached the ruler, who "
            "sent to ask. The family answered: ==we got the use of one man, "
            "not a man out of the well==. Nobody along that road lied.",
        "f": [
            {"n": "The distortion rides on the telling",
             "d": "What you are told must be examined, because passed along "
                  "often enough white becomes black. The mechanism is given "
                  "as a chain: a dog resembles a macaque, a macaque a "
                  "monkey, a monkey a man, and a man is nothing like a dog.",
             "eg": "Four people later, only the most striking half of the "
                   "sentence survives."},
            {"n": "Unexamined, better not to have heard it",
             "d": "Heard and examined it is a blessing; heard and "
                  "unexamined, better unheard. Duke Huan of Qi and King "
                  "Zhuang of Chu both checked the men recommended to them, "
                  "and led their age. The King of Wu and Zhi Bo did not, and "
                  "lost state and life.",
             "eg": "The thirty seconds before you forward it decide that "
                   "message's whole later life."},
            {"n": "Much of what is false is one character misread",
             "d": "Zixia, passing through Wei, heard someone read out that "
                  "the Jin army crossed the river with three pigs. He said "
                  "it was the jihai day: the graphs for three and ji are "
                  "close, and pig and hai are alike. In Jin they confirmed "
                  "it. Nobody meant to deceive.",
             "eg": "That figure looks absurd, so go back and check the unit "
                   "first."},
            {"n": "How to check: against the thing, and against people",
             "d": "The remedy is not to chase every claim back to its "
                  "source. It is to reason from the nature of the thing and "
                  "the nature of people. A man dug out of a well fits "
                  "neither; one man's labour saved fits both.",
             "eg": "When a sentence sounds strange, ask first whether it is "
                   "even possible."},
        ],
        "apply":
            "Where you are: only good news comes up the line, you are always "
            "last to hear of trouble, and you cannot find who is hiding "
            "it.\n"
            "Ask first: how many people did this sentence pass through "
            "before me - past two, stop asking who lied and go get the "
            "original wording.\n"
            "Where it goes wrong: read as a rule that everything must be "
            "traced to its source. It asks for sorting, not for verifying "
            "everything: check what is strange, much handled, or convenient "
            "to somebody, and hear the rest as usual.",
        "q": [
            "White becomes black with no liar anywhere, just hands.",
            "Heard and unexamined is worse than never hearing it.",
            "Reason it out first, then go looking for who said it.",
        ],
    },
    {
        "k": "the-water-has-risen",
        "n": "What you know is last season's water level",
        "w": "Wading by old markers: the homework was done and it expired",
        "src": "The Annals of Lu Buwei, 'Examining the Present', in the surveys on prudence in great matters",
        "dek": "I never got the full picture and the deadline is here. This chapter says stale beats incomplete for danger.",
        "story":
            "Jing meant to raid Song, so they sent men ahead to mark the "
            "fords of the Yong and measure where it could be crossed. Then "
            "the river rose suddenly and Jing did not know. At night they "
            "waded by the daytime markers and ==more than a thousand men "
            "drowned==, the army breaking up as if a quarter of the capital "
            "had fallen in. The homework had been done. They set those "
            "markers themselves and the markers were right when set. What "
            "changed in between was the water, while the markers stood where "
            "they were, looking as reliable as ever.",
        "f": [
            {"n": "Expired information looks exactly like live information",
             "d": "With nothing in hand a person is careful; with one old "
                  "survey in hand a person relaxes. The markers will not "
                  "fall over to tell you the river has risen. They stand "
                  "there looking identical to the day they were set, which "
                  "is what makes them worse than a blank.",
             "eg": "You are still working from the customer research you did "
                   "last year."},
            {"n": "The notch was accurate; what it was cut into was not",
             "d": "A man of Chu crossing the river dropped his sword and cut "
                  "a notch in the boat where it went in. When the boat "
                  "moored he went down from the notch to look. A judgement "
                  "matters less by its own accuracy than by what it is "
                  "attached to.",
             "eg": "Your expertise is bolted to an old employer's process "
                   "and does not travel."},
            {"n": "Keeping the law unchanged is its own disorder",
             "d": "Without law a state falls into disorder; keeping the law "
                  "and never changing it falls into perversity, and neither "
                  "can hold a state. Times shift, so laws should. Having no "
                  "rule and never revising one are two illnesses, and the "
                  "second is the quieter.",
             "eg": "The rule set three years ago now needs a weekly "
                   "exception."},
            {"n": "It hands you the illness, not the prescription",
             "d": "Like a good doctor: the illness changes ten thousand "
                  "times, so the medicine changes ten thousand times. So the "
                  "laws of former kings are not to be copied. Ask instead "
                  "why that one was made, and whether the reason still "
                  "holds.",
             "eg": "Before copying another firm's practice, ask what problem "
                   "it solved for them."},
        ],
        "apply":
            "Where you are: the deadline is on you, you never got the whole "
            "picture, and you have to decide on what is in front of you.\n"
            "Ask first: when was this gathered, and has anything happened "
            "since that would move it - incomplete and out of date are "
            "different holes and take different patches.\n"
            "Where it goes wrong: read as a demand to research everything "
            "again. It has no quarrel with old experience; it wants the "
            "reason behind it dug out. If the reason holds, use it. If it is "
            "gone, the most careful notch is still cut into a moving boat.",
        "q": [
            "A blank makes you careful; an old file makes you comfortable.",
            "However exact the notch, look at what it is cut into.",
            "No rule fails loudly; an unchanged rule fails late.",
        ],
    },
]

# -*- coding: utf-8 -*-
"""Family Instructions for the Yan Clan - English.

The English reader who has heard of this book at all has heard of it as a
Confucian conduct manual, which suggests piety and hierarchy and not much
else. What it actually contains is closer to operating advice: where a
household's behaviour originates, when a rule can still be set cheaply, and
why brothers who were inseparable at ten are distant at forty. Yan Zhitui
(born 531) served Liang, Northern Qi, Northern Zhou and Sui, and wrote the
book for his own sons late in life.

Sources, checked line by line against the Wikisource text of scroll one:
'Managing a Household' for the opening on custom travelling downward, its
reverse clause, and the passage on correction lapsing; 'Teaching Children'
for the three grades of learner, the passage on love without instruction,
the formula of severity with kindness, the unequal-affection passage, and
the paired households of Lady Wei and the scholar under Emperor Yuan of
Liang; 'Brothers' for one form and one breath, the square base and round
lid, the death of the parents, the chain down to the servants, and the
question about being gracious to the world and short with a brother.
"""

PARENT = {
    "name": "Family Instructions for the Yan Clan",
    "slug": "yanshi-jiaxun",
    "blurb": "Deep read",
    "items": [
        {"k": "wind-blows-down",
         "n": "They stopped telling you the truth at your end",
         "w": "Custom runs downward, and the inch you can move is upstream",
         "ready": True,
         "line": "He says an unkind father gets an unfilial son, then "
                 "refuses to let you overstate it"},
        {"k": "teach-before-it-sets",
         "n": "Love without teaching buries the trouble for later",
         "w": "Set the rule while the relationship is still new",
         "ready": True,
         "line": "What should be warned is rewarded, what should be rebuked "
                 "is laughed at"},
        {"k": "brothers-drift-apart",
         "n": "Brothers drift apart on their own, and nobody turned bad",
         "w": "Once each has his own wife and children, feeling will not "
              "hold it",
         "ready": True,
         "line": "Could not fail to love as children, could not fail to cool "
                 "as men"},
    ],
}

CHAPTERS = [
    {
        "k": "wind-blows-down",
        "n": "They stopped telling you the truth at your end",
        "w": "Custom runs downward, and the inch you can move is upstream",
        "src": "Family Instructions for the Yan Clan, late sixth century - "
               "'Managing a Household', opening passage and the lines on "
               "correction lapsing",
        "dek": "Nobody at home tells you anything straight. This chapter "
               "says the switch is not on their end of the line.",
        "story":
            "The chapter on running a household does not open with rules. It "
            "opens with a direction: custom travels downward and forward, "
            "from those above to those below, from those who came first to "
            "those who follow. So an unkind father gets an unfilial son, an "
            "unfriendly elder brother a rude younger one. Having put the "
            "whole account on the senior party, Yan Zhitui at once adds the "
            "reverse. ==If the father was kind and the son is defiant "
            "anyway, that is a matter for punishment, not something teaching "
            "can move.==",
        "f": [
            {"n": "He turns the arrow round",
             "d": "The usual question is why they will not speak. His "
                  "question is who produced this end of it, and when. The "
                  "opening of the household chapter fixes the order, so "
                  "'unkind father, unfilial son' is not a scolding but a "
                  "causal claim.",
             "eg": "One honest remark batted down in public, and the next "
                   "one gets weighed first."},
            {"n": "He refuses to overstate it",
             "d": "The reverse follows immediately. Where the senior side "
                  "has done its part and the junior side is defiant anyway, "
                  "that belongs to the law rather than to instruction. The "
                  "clause turns a slogan back into a question you can "
                  "actually answer.",
             "eg": "Fill in your own column first, then argue about whether "
                   "they are impossible."},
            {"n": "Where the measure lapses, faults show up first",
             "d": "Another line from the same chapter: drop correction at "
                  "home and a boy's faults appear at once, while correction "
                  "applied badly leaves people with nowhere to put hand or "
                  "foot. He weighs a household on the scale he weighs a "
                  "state on. Too loose and too tight both fail.",
             "eg": "The things a household never takes seriously are usually "
                   "the things that blow up."},
            {"n": "Almost every tool in your hand is downstream",
             "d": "Phrase it better, pick the moment, listen more. Those are "
                  "downstream tools and they spring back. He is pointing "
                  "upstream: your first reaction to bad news, the remark you "
                  "shot down in front of other people last week.",
             "eg": "Same sentence, and your reaction last week decides "
                   "whether it gets said this week."},
        ],
        "apply":
            "Where you are: nobody at home, or on your team, brings you bad "
            "news, and by the time you hear it the thing has broken.\n"
            "Ask first: the last time someone told you an unwelcome truth, "
            "what did your face do in the first three seconds - not what you "
            "concluded afterwards.\n"
            "Where it goes wrong: reading it as 'it is all my fault'. The "
            "reverse clause exists to stop that. If your end is done and "
            "they still say nothing, the problem is not instruction, and "
            "what needs changing is the arrangement.",
        "q": [
            "Wind blows down from above, so look at your own end first.",
            "He is quiet now because of what happened the last time.",
            "Downstream fixes spring back; the inch that moves is upstream.",
        ],
    },
    {
        "k": "teach-before-it-sets",
        "n": "Love without teaching buries the trouble for later",
        "w": "Set the rule while the relationship is still new",
        "src": "Family Instructions for the Yan Clan - 'Teaching Children', "
               "on love without instruction, with the households of Lady Wei "
               "and the scholar under Emperor Yuan of Liang",
        "dek": "You have said it a hundred times and nothing moves. This "
               "chapter says the bill was set the time you laughed instead.",
        "story":
            "Yan Zhitui sets two households side by side. Wang Sengbian's "
            "mother, Lady Wei, was severe: her son commanded three thousand "
            "men at Pencheng and was past forty, and she beat him still when "
            "he fell short. He became a great general. In the other house a "
            "brilliant young scholar was indulged by his father. ==One apt "
            "remark and the father told everyone he met and praised it for a "
            "year; one wrong act and he covered it over, hoping the boy "
            "would mend it himself.== By the time that son married and took "
            "office, careless speech got him killed.",
        "f": [
            {"n": "He admits the book is for the middle",
             "d": "The chapter opens by sorting people: the highest need no "
                  "teaching, the lowest gain nothing from it, and the "
                  "ordinary do not know unless taught. He is not writing for "
                  "prodigies or for lost causes, and in the middle group "
                  "teaching is the whole difference.",
             "eg": "'He is bright, he will work it out' is true of very few "
                   "people."},
            {"n": "Love without teaching",
             "d": "He says he has seen too many houses with affection and no "
                  "instruction. What should be warned is rewarded, what "
                  "should be rebuked is laughed at. By the time the child "
                  "understands anything he assumes the rules always looked "
                  "like this.",
             "eg": "What you find charming at three is what you will shout "
                   "about at thirteen."},
            {"n": "Once arrogance sets, force buys nothing",
             "d": "Come back to it after the habit has formed and his "
                  "verdict is blunt: beat him to death and you hold no "
                  "authority, while anger and resentment rise together. The "
                  "cost does not climb evenly. Past that stretch the same "
                  "thing takes ten times the effort.",
             "eg": "The same 'no' takes three seconds at two and three "
                   "months at sixteen."},
            {"n": "Severity and warmth are one prescription",
             "d": "His formula is that parents who are stern and also kind "
                  "get children who are careful and grow up dutiful. Not "
                  "harsh and not soft: a line that does not move, and a "
                  "place to come when it hurts. A line alone is fear, a "
                  "place alone is chaos.",
             "eg": "Say both on the day you set it: this one is fixed, and "
                   "come to me when it stings."},
            {"n": "Uneven love is the expensive kind",
             "d": "He notes that few parents love their children equally and "
                  "that it has always been so. The able attract affection, "
                  "the dull deserve pity, and the parent who favours one "
                  "means to do him good and does him harm instead.",
             "eg": "The favourite in the house is often the last to learn "
                   "how refusal feels."},
        ],
        "apply":
            "Where you are: you have said the same thing many times, he "
            "still does not do it, and you have begun to suspect you are "
            "simply nagging.\n"
            "Ask first: when did this first happen, and what did you do that "
            "time - did you close it off on the spot, or laugh and let it "
            "pass.\n"
            "Where it goes wrong: reading it as a case for hitting children. "
            "What he wants is the first half of the pair present, not force, "
            "and his variable is timing rather than strength. While the "
            "window is open one sentence will do; once it shuts, raising the "
            "pressure will not.",
        "q": [
            "Affection without instruction buries the trouble for him to "
            "find later.",
            "Once the window shuts, more force only buys resentment.",
            "Stern and kind are one prescription; half a dose harms.",
        ],
    },
    {
        "k": "brothers-drift-apart",
        "n": "Brothers drift apart on their own, and nobody turned bad",
        "w": "Once each has his own wife and children, feeling will not hold "
             "it",
        "src": "Family Instructions for the Yan Clan - 'Brothers', on those "
               "who share one form and one breath",
        "dek": "You were raised by the same parents, so how did it get here. "
               "This chapter says the decay is structural.",
        "story":
            "Yan Zhitui writes about brothers by starting with childhood: a "
            "parent leading one by each hand, one clutching the front of the "
            "robe and one the hem, the same table at meals, clothes handed "
            "down, lessons taken together, outings shared. Two people raised "
            "like that, he says, could not fail to love each other however "
            "bad their tempers. Then comes the second half. ==Once grown, "
            "each with his own wife and his own children, they could not "
            "fail to cool a little however decent their tempers.==",
        "f": [
            {"n": "Two impossibilities, pointing opposite ways",
             "d": "Could not fail to love; could not fail to cool. He uses "
                  "the same construction twice in opposite directions. "
                  "Nobody turned bad in between; what changed is that each "
                  "acquired a household. Blaming character finds the wrong "
                  "cause and therefore the wrong remedy.",
             "eg": "Your last long conversation was years ago and you never "
                   "had a row."},
            {"n": "The people who arrive keep separate books",
             "d": "Wives of brothers, he says, stand further apart than the "
                  "brothers do; measuring a close bond by a distant one is a "
                  "square base under a round lid and will never fit. The "
                  "later it gets, the less any of it is about two people.",
             "eg": "An account two brothers settle in a sentence needs other "
                   "arithmetic between two households."},
            {"n": "When the parents go, so does the buffer",
             "d": "Once both parents are dead, he writes, brothers looking "
                  "at each other should be as form to shadow and sound to "
                  "echo. That is not sentiment. While the parents lived they "
                  "absorbed a great deal in the middle; afterwards the "
                  "brothers settle up directly, and that is when it breaks.",
             "eg": "Settle what needs settling while the old people are "
                   "still alive."},
            {"n": "He follows the collapse all the way down",
             "d": "Brothers at odds and their sons are not close; sons not "
                  "close and the cousins grow distant; cousins distant and "
                  "even the servants turn into enemies. Layer after layer "
                  "goes, until strangers can walk over you and nobody comes.",
             "eg": "What one generation left unsaid, the next carries on as "
                   "not speaking."},
            {"n": "Gracious to the world, short with your brother",
             "d": "He puts a question rather than an argument: a man keeps "
                  "company with the finest people everywhere and is warm to "
                  "all of them, yet fails in respect towards his own elder "
                  "brother. How can he manage the many and not the few.",
             "eg": "The patience you spend on colleagues runs out in the "
                   "last three steps home."},
        ],
        "apply":
            "Where you are: there are several of you, your parents' care "
            "falls on you alone, the others cannot be moved, and you resent "
            "it and cannot say so.\n"
            "Ask first: how much of 'how did he become like this' is really "
            "'he has a household of his own now' - take that part off the "
            "account before working out what is left to discuss.\n"
            "Where it goes wrong: reading it as permission to give up "
            "because cooling is natural. He argues the opposite. Precisely "
            "because it cools by itself, feeling cannot be left to hold it: "
            "settle things while the parents are alive, and put the visits "
            "in the calendar.",
        "q": [
            "Once each has his own household, staying close is the surprise.",
            "A matter between brothers is never only between two people.",
            "The patience left over from strangers is what comes home.",
        ],
    },
]

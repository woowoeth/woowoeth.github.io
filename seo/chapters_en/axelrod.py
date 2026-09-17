# -*- coding: utf-8 -*-
"""Robert Axelrod - English.

English readers usually arrive knowing the punchline - "tit for tat wins" -
and take it as a licence to retaliate. These two chapters restore the other
half of the rule and the condition it runs on: never defect first, answer
once and return immediately, and expect none of it to hold where the two of
you will not meet again. Sources are the two tournaments in chapters 2-3 of
The Evolution of Cooperation and the trench truce in chapter 4.
"""

PARENT = {
    "name": "Robert Axelrod",
    "slug": "axelrod",
    "blurb": "Deep read",
    "items": [
        {"k": "tit-for-tat", "n": "Hit back once, then come straight back",
         "w": "The winner was not the meanest, it was the quickest to resume",
         "ready": True,
         "line": "A two-hundred-round tournament settled whether to hit back"},
        {"k": "shadow-of-the-future", "n": "What keeps his word is not his character",
         "w": "It is how many rounds the two of you have left",
         "ready": True,
         "line": "Neither side in the trench truce trusted the other"},
    ],
}

CHAPTERS = [
    {
        "k": "tit-for-tat",
        "n": "Hit back once, then come straight back",
        "w": "The winner was not the meanest, it was the quickest to resume",
        "src": "The Evolution of Cooperation, 1984, chapters 2-3: the two "
               "computer tournaments",
        "dek": "Someone has crossed you and you are deciding whether to hit back, "
               "and how often. A tournament worked the answer out.",
        "story":
            "In 1980 Axelrod wrote to game theorists around the world: send your "
            "best strategy as a program and I will play them all against each "
            "other over two hundred rounds. Fourteen arrived, some hundreds of "
            "lines long, modelling the opponent and probing for weakness. The "
            "winner was the shortest program submitted - TIT FOR TAT, four "
            "lines, from Anatol Rapoport in Toronto. Cooperate on the first "
            "move, then copy whatever the other side just did. ==The second "
            "tournament drew sixty-two programs whose authors all knew it would "
            "win, and not one of them could beat it==.",
        "f": [
            {"n": "None of the leaders moved first",
             "d": "Rank the first tournament and the clean dividing line is not "
                  "sophistication, it is whether a program ever defected first. "
                  "The top eight never did. They passed up every chance to take "
                  "advantage and still scored highest.",
             "eg": "The colleague who wins every small negotiation is usually the "
                   "one with the fewest people left to call."},
            {"n": "Retaliate at once, once only, then return",
             "d": "It answers a defection on the very next move, and the moment "
                  "the other side cooperates again it cooperates again too - no "
                  "arrears, no ledger. Programs that punished forever scored "
                  "badly. They turned one accident into a permanent deadlock.",
             "eg": "He missed one commitment, you went cold for six months, and "
                   "the six months cost more than the commitment did."},
            {"n": "It never won a single match",
             "d": "TIT FOR TAT cannot outscore anyone head to head. It always "
                  "defects a move later and takes one hit more, so a draw is its "
                  "ceiling. Its total was still the highest, because of what it "
                  "drew out of the other side.",
             "eg": "Keep score against your colleague and the thing the two of "
                   "you could have built goes unbuilt."},
            {"n": "Don't be too clever",
             "d": "The elaborate programs that modelled their opponent and "
                  "hunted for a quiet advantage all lost. The problem was not "
                  "accuracy. A player whose behaviour shows no pattern is "
                  "indistinguishable from noise, and nobody cooperates with "
                  "noise.",
             "eg": "When your standard changes every time, people stop reading "
                   "you and default to the most cautious thing available."},
            {"n": "Its real weakness is misunderstanding",
             "d": "Add noise and the rule breaks: one misread move sends two TIT "
                  "FOR TAT players into endless recrimination. Axelrod and Dion "
                  "returned to this in Science in 1988 - where errors are "
                  "certain, the rule needs room to let one go.",
             "eg": "An unanswered message is not always a snub, and strict "
                   "reciprocity will run you both off the road."},
        ],
        "apply":
            "Where you are: someone has taken a piece out of you, and you are "
            "choosing between letting it go and never dealing with them again.\n"
            "Ask first: after I answer this, is there a clear route back to "
            "working together - because without one I have not answered once, I "
            "have set the relationship permanently to retaliation.\n"
            "Where it goes wrong: reading it as a warrant for grudges. The same "
            "rule forbids you to move first and requires you to stop the instant "
            "they do; neither half stands without the other.",
        "q": [
            "None of the leading programs was ever the first to defect.",
            "Hit back once, then come straight back. No ledger.",
            "It never outscored a single opponent and still finished first.",
            "Don't be envious, and don't be the first to defect.",
        ],
    },
    {
        "k": "shadow-of-the-future",
        "n": "What keeps his word is not his character",
        "w": "It is how many rounds the two of you have left",
        "src": "The Evolution of Cooperation, 1984, chapter 4, drawing on Tony "
               "Ashworth's study of trench warfare",
        "dek": "You cannot tell whether his promise will hold. What decides it is "
               "usually not character but how many rounds remain.",
        "story":
            "A truce grew by itself in the trenches of the Western Front. The men "
            "on either side had never met, were under orders to shoot each other, "
            "and had no referee between them. Working from diaries and regimental "
            "histories, Tony Ashworth found artillery shelling the same patch of "
            "ground at the same hour each day, so the other side knew when to be "
            "elsewhere. Headquarters broke the habit with compulsory raids, which "
            "had to produce prisoners or bodies and so could not be faked. ==What "
            "held them was not goodwill but knowing the same men would face each "
            "other again tomorrow==.",
        "f": [
            {"n": "The shadow of the future",
             "d": "His name for it. Played once, defection always pays; played "
                  "many times with the next round weighing enough, the gain is "
                  "clawed back later. Cooperation is not the nobler choice, it is "
                  "the better arithmetic.",
             "eg": "The stall selling to tourists once shorts the weight. The one "
                   "serving the same street does not."},
            {"n": "No friendship, no enforcer required",
             "d": "He keeps lowering the bar: cooperation needs no friendship, no "
                  "central authority to punish, not even foresight or rationality "
                  "in the players. The trenches are the extreme proof, because "
                  "nothing else was there.",
             "eg": "Two firms in the same building settle a dispute far more "
                   "easily than two on different continents."},
            {"n": "So change the structure, not the person",
             "d": "To get something honoured, stop auditing the other person's "
                  "character and make the thing repeat: split it into "
                  "instalments, leave a record both sides can see, put the two of "
                  "you inside a circle you both have to stay in.",
             "eg": "Turn one payment into monthly ones and the other side's "
                   "manner usually changes by the second month."},
            {"n": "Remove the future and cooperation goes with it",
             "d": "Headquarters understood this exactly. It did not break the "
                  "trench truce by lecturing. It rotated units constantly and "
                  "ordered raids that had to show results. Once tomorrow no "
                  "longer holds the same two people, yesterday's understanding "
                  "expires.",
             "eg": "Reorganise the team every quarter and nobody owes anybody "
                   "anything six months out."},
        ],
        "apply":
            "Where you are: the promise sounded fine and you still cannot decide "
            "whether to hand the thing over.\n"
            "Ask first: once this is done, do the two of us have a next time - "
            "because if not, what needs changing is the shape of the deal, not my "
            "method for reading people.\n"
            "Where it goes wrong: taking it to mean that people you know well are "
            "safe. He is measuring how much the next meeting weighs, not how "
            "familiar you are; two people who see each other daily and want "
            "nothing further are under no constraint at all.",
        "q": [
            "Credibility rests on the rounds still to come, not on character.",
            "Neither side in the trench truce trusted the other.",
            "To get cooperation, turn a one-off into something that repeats.",
        ],
    },
]

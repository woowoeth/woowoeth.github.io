# -*- coding: utf-8 -*-
"""Sun Tzu — English.

The English reader has met this book already, usually as a airport-shelf
source of aggressive one-liners. The job of the English page is the opposite
of introduction: it has to take the most famous sentence back off the poster
and put it where it belongs, which is a claim about preparation.
"""

PARENT = {
    "name": "Sun Tzu",
    "slug": "sun-tzu",
    "blurb": "Deep read",
    "items": [
        {"k": "win-before-fighting", "n": "Win first, then fight",
         "w": "The work happens before the clash", "ready": True,
         "line": "The winner had already won when the fighting started"},
        {"k": "know-both", "n": "Know both, and know which is harder",
         "w": "Your own numbers are the flattered ones", "ready": True,
         "line": "Theirs is outside and findable. Yours has been through people"},
        {"k": "win-without-fighting", "n": "The best fight is the one nobody has",
         "w": "Winning a hundred times is not the top of the list", "ready": True,
         "line": "Every win you take spends people, money, time and trust"},
        {"k": "orthodox-and-surprise", "n": "The flank only works if the front holds",
         "w": "A clever move on its own is a donation", "ready": True,
         "line": "Used once, the surprise becomes the thing they expect"},
        {"k": "form-like-water", "n": "Take the shape of what you meet",
         "w": "Avoiding the strong part is the hard half", "ready": True,
         "line": "Water has no shape of its own. That is the whole point"},
    ],
}

CHAPTERS = [
    {
        "k": "win-before-fighting",
        "n": "Win first, then fight",
        "w": "The work happens before the clash",
        "src": "Art of War, Form",
        "dek": "Everyone quotes it as bravado. Read slowly it says the "
               "opposite: by the time you are fighting, it is mostly decided.",
        "story":
            "The line is four characters longer in Chinese than in any "
            "translation, and it is built as a pair: the victorious army wins "
            "first and seeks battle afterwards, the defeated army fights "
            "first and looks for the win afterwards. ==It is not advice about "
            "how to fight. It is a claim about when the outcome is set.== "
            "The book spends its early chapters on measurement — ground, "
            "numbers, supply, weather, the character of the commander — "
            "because that is where the decision actually happens.",
        "f": [
            {"n": "Preparation is not the same as planning",
             "d": "A plan is a description of what you intend to do. "
                  "Preparation is changing the conditions until the intended "
                  "thing becomes easy. The first can be done at a desk in an "
                  "afternoon; the second takes months and shows up as very "
                  "little visible activity.",
             "eg": "The negotiation that went well was decided in the six "
                   "weeks of getting a second supplier to the point of being "
                   "usable."},
            {"n": "If it needs courage, something upstream went wrong",
             "d": "Reaching for nerve is usually the sign that the conditions "
                  "were not set. Sometimes there is no choice. But treating "
                  "courage as the plan converts an upstream failure into a "
                  "personal one, and hides the part that could have been "
                  "fixed.",
             "eg": "He had to wing the board meeting because the numbers had "
                   "not been reconciled the week before, and afterwards told "
                   "himself he was bad under pressure."},
            {"n": "Not starting is a move",
             "d": "If the conditions are not there, the strongest available "
                  "action is to not begin yet. This is the hardest part to "
                  "practise, because waiting looks identical to doing "
                  "nothing, and only one of them has a reason.",
             "eg": "They held the launch a quarter and shipped into a market "
                   "that had already heard of them, instead of into silence."},
        ],
        "q": [
            "The victorious army wins first and seeks battle afterwards.",
            "The defeated army fights first and looks for the win afterwards.",
            "If it takes nerve, look at what was left undone upstream.",
        ],
        "apply":
            "Where you are: something is coming that you are bracing for.\n"
            "Ask first: what would have to already be true for this to go "
            "well? Write the list, and see how much of it is still available "
            "to change.\n"
            "Where it goes wrong: reading it as never act until certain — the "
            "book is about setting conditions, not about waiting; and the "
            "conditions include a deadline.",
    },
    {
        "k": "know-both",
        "n": "Know both, and know which is harder",
        "w": "Your own numbers are the flattered ones",
        "src": "Art of War, Attack by Stratagem / Estimates",
        "dek": "Quoted for two thousand years, usually as a case for research. "
               "The half everybody skips is the one about yourself.",
        "story":
            "The Estimates chapter is not a maxim, it is a form to fill in: "
            "five dimensions and seven comparisons — whose ruler has the way, "
            "whose commanders are abler, who has the ground and the season, "
            "whose discipline is enforced, whose troops are stronger, whose "
            "are better drilled, whose rewards and punishments are clear. "
            "Then a coldly practical conclusion: if the count comes out "
            "favourable, fight; if it does not, don't. ==He called it "
            "reckoning in the temple — settle it before you decide whether to "
            "go at all.==",
        "f": [
            {"n": "Knowing is a filled-in table, not an impression",
             "d": "'I have a rough sense of the competition' is not knowing. "
                  "The value of a list of comparisons is that it forces out "
                  "the row you cannot answer, and the row you cannot answer "
                  "is usually the one that decides it.",
             "eg": "Nobody could say what their support costs per account "
                   "were. That empty cell was the entire margin difference."},
            {"n": "Your own side is the harder half",
             "d": "Their information is outside you and can be gone and "
                  "found. Yours has been through several people who each had "
                  "a reason to round it kindly. The order in the sentence "
                  "puts them first; the difficulty runs the other way.",
             "eg": "The competitor's timeline came from their own blog. His "
                   "own timeline came from a manager reporting to the person "
                   "who set it."},
            {"n": "The count has to be allowed to say no",
             "d": "More reckoning wins, less reckoning loses. The point of "
                  "the exercise is not to find a way to win; it is that it "
                  "can output 'this one should not be fought'. A process "
                  "that ends in action whatever it computes is not a "
                  "decision, it is a ceremony.",
             "eg": "Every quarterly review ended with the same launch date. "
                   "The review was not deciding anything and everyone knew "
                   "it."},
        ],
        "q": [
            "More reckoning wins. Less reckoning loses.",
            "Theirs is outside and findable. Yours has been through people.",
            "A process that ends in action whatever it computes is a "
            "ceremony.",
        ],
        "apply":
            "Where you are: about to commit to something competitive on the "
            "strength of a general sense.\n"
            "Ask first: which rows can you actually fill in, and which is "
            "blank? Go and fill the blank one before anything else.\n"
            "Where it goes wrong: turning it into endless analysis — the "
            "count has a deadline, and 'we cannot know' is itself a row.",
    },
    {
        "k": "win-without-fighting",
        "n": "The best fight is the one nobody has",
        "w": "Winning a hundred times is not the top of the list",
        "src": "Art of War, Attack by Stratagem",
        "dek": "A hundred victories sounds like the ceiling. He says it "
               "isn't, and the reason is arithmetic rather than modesty.",
        "story":
            "The chapter gives a ranked list that runs against instinct: "
            "attack the enemy's plan first, his alliances second, his army "
            "third, and his walled cities last. Each step down costs more and "
            "returns less. On sieges he is unusually specific — three months "
            "to prepare the engines, three more for the ramps, and a "
            "commander who loses patience and sends men up the walls like "
            "ants, ==a third of them dead and the city still standing.== He "
            "calls that the disaster of assault.",
        "f": [
            {"n": "Winning is also spending",
             "d": "A hundred victories is not the height of skill; subduing "
                  "the enemy without fighting is. Every win costs people, "
                  "money, time and trust. The side that won five times can "
                  "easily be stronger than the side that won a hundred.",
             "eg": "They won the pricing war and came out of it with a team "
                   "that had shipped nothing new for a year."},
            {"n": "Plan, then alliances, then force",
             "d": "Attacking the plan means making their approach stop making "
                  "sense on its own terms. Attacking alliances means removing "
                  "the support it rests on. Neither requires contact. By the "
                  "time only fighting is left, the first two were skipped or "
                  "botched.",
             "eg": "The integration deal with the distributor ended the "
                   "competitor's route to market without a single price "
                   "change."},
            {"n": "The most expensive move is the one you take personally",
             "d": "Assault happens when there is nothing else left, or when "
                  "someone cannot stand to walk away. He singles out the "
                  "commander who attacks in anger. Losing a third of your "
                  "strength to a wall you did not need is a decision made by "
                  "a mood.",
             "eg": "The lawsuit was about being right. Two years and a "
                   "quarter of the budget later, it was still about being "
                   "right."},
        ],
        "q": [
            "Winning a hundred battles is not the height of skill.",
            "Every win you take spends people, money, time and trust.",
            "A third of your strength on a wall you did not need.",
        ],
        "apply":
            "Where you are: locked into a fight you expect to win.\n"
            "Ask first: what does winning this cost, and what would have to "
            "be true for it not to be necessary at all?\n"
            "Where it goes wrong: reading it as avoid all conflict — the "
            "ranking has fighting on it; it is just not at the top.",
    },
    {
        "k": "orthodox-and-surprise",
        "n": "The flank only works if the front holds",
        "w": "A clever move on its own is a donation",
        "src": "Art of War, Energy",
        "dek": "Everyone wants the unexpected move. The chapter is mostly "
               "about the unglamorous thing it has to stand on.",
        "story":
            "The Energy chapter asks why the same troops behave like a "
            "rolling log one day and a scattered crowd the next. His answer "
            "is the pairing: ==engage with the orthodox, win with the "
            "extraordinary.== The orthodox is the part that meets them head "
            "on and holds; the extraordinary is what comes from the side. He "
            "insists the two convert into each other endlessly — which means "
            "today's surprise, once used, becomes tomorrow's front.",
        "f": [
            {"n": "Without the front, the flank hits air",
             "d": "The surprise works because the other side is already "
                  "gripped and cannot turn. Let the front go slack and the "
                  "clever move lands on nothing, with your best people "
                  "stranded out in the open.",
             "eg": "The campaign was inventive and the sales team could not "
                   "answer the second question, so it produced attention and "
                   "no orders."},
            {"n": "A surprise used once becomes the expected thing",
             "d": "Any unexpected move, once used and written up, enters the "
                  "other side's expectations and becomes part of the front. "
                  "Planning to live for years off one trick is spending a "
                  "one-time resource as if it were income.",
             "eg": "The referral loop worked brilliantly, was copied within "
                   "two quarters, and is now the baseline everyone has."},
            {"n": "Position, not heroics",
             "d": "The chapter ends not on cleverness but on structure: put "
                  "the rock at the top of a thousand-foot mountain and the "
                  "force of it coming down is not the rock's. Seek it in the "
                  "position, and do not demand it of the people.",
             "eg": "Before asking the team to try harder, someone should ask "
                   "why the same work takes three approvals."},
        ],
        "q": [
            "Engage with the orthodox, win with the extraordinary.",
            "Used once, the surprise becomes the thing they expect.",
            "Seek it in the position; do not demand it of the people.",
        ],
        "apply":
            "Where you are: pinning your hopes on one inventive move.\n"
            "Ask first: what is holding the front while that move happens, "
            "and is it actually holding?\n"
            "Where it goes wrong: concluding that only the basics matter — "
            "the front alone defends and never wins.",
    },
    {
        "k": "form-like-water",
        "n": "Take the shape of what you meet",
        "w": "Avoiding the strong part is the hard half",
        "src": "Art of War, Weak Points and Strong",
        "dek": "'Be like water' became a poster. The chapter is stricter "
               "than the poster, and most of it is about what not to do.",
        "story":
            "The chapter is about who is setting the terms: ==bring the enemy "
            "to you; do not be brought to him.== Strike what he must defend "
            "and he has to come. Decline the engagement and he cannot force "
            "it. Then the image everybody knows: water has no constant shape, "
            "it avoids the heights and runs to the low ground, and an army "
            "has no constant form either — it avoids what is solid and "
            "strikes what is hollow.",
        "f": [
            {"n": "Having no fixed shape is the point",
             "d": "What water resembles is not softness, it is the absence of "
                  "a preset form. Its shape is decided entirely by what it "
                  "meets. Which makes 'what is our style of competing' a "
                  "question with a flaw built into it.",
             "eg": "The playbook that won the first market was applied "
                   "unchanged to the second, where the constraint was "
                   "regulatory rather than technical."},
            {"n": "Avoiding the solid part is discipline, not opportunism",
             "d": "The hard half is the avoiding. The places that look most "
                  "worth taking, most prestigious, most expected of you are "
                  "usually exactly where they are thickest. Declining them "
                  "means absorbing internal pressure, which is harder than "
                  "spotting the gap.",
             "eg": "Everyone wanted the flagship account. The three unglamorous "
                   "ones nobody was fighting over paid for the year."},
            {"n": "Who wrote this week's calendar",
             "d": "Initiative is not moving first. It is that the other side "
                  "has to answer at your tempo. There is a simple test: look "
                  "at the week you just had and ask whether you scheduled it, "
                  "or whether their moves did.",
             "eg": "Four of the five priorities were reactions to a "
                   "competitor's announcement, and nobody had decided that "
                   "was the plan."},
        ],
        "q": [
            "Bring the enemy to you; do not be brought to him.",
            "Water has no constant shape. That is what it is being praised "
            "for.",
            "Did you write this week's calendar, or did their moves?",
        ],
        "apply":
            "Where you are: reacting to a competitor, or defending the "
            "position you are proudest of.\n"
            "Ask first: where are they actually thin, and what would it cost "
            "you internally to walk away from the thick part?\n"
            "Where it goes wrong: using it to justify having no strategy at "
            "all — no fixed shape is not the same as no direction.",
    },
]

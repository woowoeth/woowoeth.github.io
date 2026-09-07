# -*- coding: utf-8 -*-
"""Neil Postman — English.

He wrote in English, so both chapters restore his own sentences: the trade-off
line and the not-additive-but-ecological line are from the 1998 talk, the clock
and Thamus are from the first chapter of Technopoly. English readers arrive
thinking this is an argument against technology. It is not one. It is two
questions to ask before signing.
"""

PARENT = {
    "name": "Neil Postman",
    "slug": "postman",
    "blurb": "Deep read",
    "items": [
        {"k": "ecological-change", "n": "It does not get added",
         "w": "A new technology replaces the environment", "ready": True,
         "line": "Europe after the printing press was not old Europe with a machine in it"},
        {"k": "faustian-bargain", "n": "The Faustian bargain",
         "w": "What it gives and what it takes land on different people",
         "ready": True,
         "line": "Monks built the clock for prayer; it served the men billing by the hour"},
    ],
}

CHAPTERS = [
    {
        "k": "ecological-change",
        "n": "It does not get added",
        "w": "A new technology replaces the environment",
        "src": "Technopoly (1992); Five Things We Need to Know About "
               "Technological Change (1998)",
        "dek": "Everyone says it is one more tool and using it is up to you. "
               "Why he says there is no such thing as one more.",
        "story":
            "His example: after the printing press, Europe was not the old "
            "Europe with a machine added to it. It was a different Europe "
            "— ==what counted as knowledge, who counted as learned, at what "
            "age a child began to read, whether the Church still had the "
            "last word, all shifted position.== He called this ecological "
            "change, against the additive kind everyone assumes. Drop red "
            "ink into a jar of water and you do not have water plus a drop "
            "of ink. You have a jar of pale red water.",
        "f": [
            {"n": "You expect arithmetic and get ecology",
             "d": "Installing something new, people expect addition: the day "
                  "carries on and one chore gets cheaper. What happens "
                  "instead is that everything around it moves a little, "
                  "including the line marking when a piece of work is "
                  "finished.",
             "eg": "The group chat saved you the emails. What actually "
                   "changed was how long a reply may take: a day became ten "
                   "minutes."},
            {"n": "The hours you saved were taken by the new standard",
             "d": "So a fuller day after installing more tools is not only a "
                  "ledger error. The tool also raises the line for what "
                  "counts as enough, and the hours saved are collected by "
                  "the raised line before you get to see them.",
             "eg": "A first draft takes half a day now instead of three "
                   "days. The ask moved from one draft to three and pick."},
            {"n": "Used long enough, it stops looking like technology",
             "d": "His fifth point: once something has been around long "
                  "enough it is taken not as an invention but as the way "
                  "things are, and nobody asks who installed it or why. The "
                  "alphabet, the clock and exam scores all sit there now.",
             "eg": "Nobody in the meeting asks why this gets measured in "
                   "hours. The clock stopped looking like an invention."},
        ],
        "q": [
            "A new medium does not add something; it changes everything.",
            "Technological change is not additive; it is ecological.",
            "Media tend to become mythic.",
        ],
        "apply":
            "Where you are: you only added a tool, and the whole rhythm "
            "feels different without your being able to say where.\n"
            "Ask first: which line moved when it arrived? Who sets what "
            "counts as prompt now, and what counts as enough?\n"
            "Where it goes wrong: reading this as a case against tools. He "
            "wants you to see what the environment became before you decide "
            "whether to work inside it.",
    },
    {
        "k": "faustian-bargain",
        "n": "The Faustian bargain",
        "w": "What it gives and what it takes land on different people",
        "src": "Technopoly (1992), chapter one; Five Things We Need to Know "
               "About Technological Change (1998)",
        "dek": "A new tool is in front of you. The question is not whether "
               "it is good, but which two questions to ask about it.",
        "story":
            "Benedictine monks built the mechanical clock in the thirteenth "
            "century to get the hours of prayer exactly right — seven times "
            "a day, not by the look of the sky. ==Centuries later the people "
            "who found the thing most useful were merchants paying wages by "
            "the hour and interest by the day.== The clock did not lie; it "
            "kept time accurately. But once keeping time accurately was "
            "possible, who it would serve was no longer for its makers to "
            "decide.",
        "f": [
            {"n": "It is a bargain, not a gift",
             "d": "His first point: technology is never free. He calls it a "
                  "Faustian bargain — it hands you one thing and takes "
                  "another, and no receipt is ever issued for the thing "
                  "taken. So is it any good has no answer. Ask what it gives "
                  "and what it cancels.",
             "eg": "Navigation freed you from remembering the route and took "
                   "your sense of the city's map. One is on the feature "
                   "list, the other is nowhere."},
            {"n": "The people who gain are not the people who pay",
             "d": "The second point is harder: advantages and costs are "
                  "never spread evenly. A technology is often pure gain for "
                  "one group and pure loss for another, and the group "
                  "deciding to adopt it is usually the one gaining.",
             "eg": "Typesetting software saved the publisher an entire "
                   "hot-metal floor. None of the saving went to the "
                   "compositors, who lost a trade."},
            {"n": "Its makers are not the right judges of it",
             "d": "This is what he took from the story Plato recorded: an "
                  "inventor is fond of his invention and sees what it can "
                  "do rather than what it removes. So the case for and "
                  "against a tool should not rest on the people who know it "
                  "best.",
             "eg": "The clearest account of what a system costs rarely comes "
                   "from whoever designed it. It comes from whoever is "
                   "blocked by it daily."},
        ],
        "q": [
            "All technological change is a trade-off.",
            "The advantages and disadvantages of new technologies are never "
            "distributed evenly among the population.",
            "It is a mistake to suppose that any technological innovation "
            "has a one-sided effect.",
        ],
        "apply":
            "Where you are: a new tool is in front of you, everyone is "
            "saying how good it is, and you cannot name what is off.\n"
            "Ask first: what does it give and what does it cancel? Who is "
            "pure gain here, who is pure loss, and which side am I on?\n"
            "Where it goes wrong: treating a cost as a reason to decline. "
            "Faustian bargains are often worth signing; he only wants both "
            "columns filled in first.",
    },
]

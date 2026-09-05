# -*- coding: utf-8 -*-
"""Nassim Taleb — English.

Everyone arrives here already owning the phrase black swan, which is exactly
the problem: it has become a word for anything unpleasant and unforeseen. Both
chapters put the weight back on structure — what a clean safety record does
and does not prove, and what a person has staked on the advice they are
giving you.
"""

PARENT = {
    "name": "Nassim Taleb",
    "slug": "taleb",
    "blurb": "Deep read",
    "items": [
        {"k": "turkey-problem", "n": "The turkey problem",
         "w": "The evidence peaks just before the break", "ready": True,
         "line": "A thousand days of feeding, and the confidence peaks in "
                 "November"},
        {"k": "skin-in-the-game", "n": "Skin in the game",
         "w": "Read the position, not the opinion", "ready": True,
         "line": "Don't tell me what you think, tell me what you hold"},
    ],
}

CHAPTERS = [
    {
        "k": "turkey-problem",
        "n": "The turkey problem",
        "w": "The evidence peaks just before the break",
        "src": "The Black Swan, chapter four",
        "dek": "What conclusion does a turkey reach if it thinks "
               "statistically? This piece asks why the day with the most "
               "evidence is the day before the accident.",
        "story":
            "Taleb borrows Russell's turkey to show where induction dies. "
            "Consider a turkey that is fed every day. Every feeding "
            "strengthens its belief that human beings are looking out for its "
            "interests. The data is clean, the sample is large, there is not "
            "one counter-example, and ==its confidence reaches its maximum on "
            "the afternoon before Thanksgiving==. The point is the asymmetry: "
            "what is a Black Swan for the turkey is not one for the butcher. "
            "Surprise belongs to whoever held the wrong model. Calm is not "
            "proof of safety. It can be the incubation.",
        "f": [
            {"n": "A clean record does not prove safety",
             "d": "A thousand days without an incident has two readings: the "
                  "system is genuinely robust, or the risk is accumulating "
                  "and has not detonated. The two histories look identical. "
                  "You separate them by looking at structure — hidden "
                  "leverage, single points of failure, volatility suppressed "
                  "rather than released.",
             "eg": "Ten years with this supplier and never a missed shipment "
                   "is the turkey's thousand days. Look at where their "
                   "capacity sits and who is upstream, not at the record."},
            {"n": "Ask whether you are the turkey or the butcher",
             "d": "The same event is a different species depending on where "
                  "you stand, and Thanksgiving is written plainly in the "
                  "butcher's calendar. So when something surprises you, ask "
                  "who it did not surprise, and what structure they could see "
                  "from there that you could not see from here.",
             "eg": "The platform policy change blindsided you and the "
                   "platform had prepared it for six months. Your Black Swan "
                   "is their roadmap. Read their hiring and their filings."},
            {"n": "The dangerous moment is when confidence rises with the "
                  "data",
             "d": "The turkey's structure is three lines climbing together: "
                  "evidence accumulating, vigilance falling, exposure "
                  "growing, all settled at once at the break. So risk "
                  "discipline has to be hung backwards. The longer the calm "
                  "runs, the more drills and redundancy, not fewer.",
             "eg": "Three years with no incident, so the drill budget and the "
                   "backups get cut. From the day of that cut you are on the "
                   "turkey's nine-hundredth morning."},
        ],
        "q": [
            "Consider a turkey that is fed every day.",
            "A Black Swan for the turkey is not one for the butcher.",
            "Past knowledge is trusted most on the day it is worth least.",
        ],
        "apply":
            "Where you are: something has been stable for a long time and "
            "somebody is proposing to cut the protection around it.\n"
            "Ask first: is this calm produced by the structure, or is the "
            "risk simply not due yet? And who is this not a surprise to?\n"
            "Where it goes wrong: reading the turkey as an argument for "
            "distrusting all data; or agreeing about Black Swans in "
            "conversation while reducing nothing about your actual exposure.",
    },
    {
        "k": "skin-in-the-game",
        "n": "Skin in the game",
        "w": "Read the position, not the opinion",
        "src": "Skin in the Game; the doctor heuristic Taleb credits to Gerd "
               "Gigerenzer",
        "dek": "He revived a very old filter. This piece asks why advice from "
               "someone who bears none of the consequences should be "
               "discounted automatically.",
        "story":
            "Taleb puts it crudely and clearly: don't tell me what you think, "
            "tell me what you have in your portfolio. The book argues one "
            "thing — a judgement is credible only when the person judging "
            "shares the consequences. The doctor heuristic quoted there he "
            "credits to the psychologist Gerd Gigerenzer. His historical "
            "exhibit is Hammurabi: ==if a builder builds a house and it "
            "collapses and kills the owner, that builder shall be put to "
            "death.== The builder knows where the flaws are hidden better "
            "than any inspector ever will.",
        "f": [
            {"n": "Asymmetry is where bad advice breeds",
             "d": "When the upside belongs to the adviser and the cost to the "
                  "listener, advice drifts systematically towards the "
                  "aggressive and the complicated: being wrong does not hurt, "
                  "being right gets credit. So the first filter is not the "
                  "content, it is the structure. What has this person staked?",
             "eg": "Ask the consultant whether half the fee can ride on the "
                   "outcome of the plan they are recommending. The plans of "
                   "those who say yes get simple very fast."},
            {"n": "Ask what they would do, not what you should do",
             "d": "What should I do puts the other person into persuasion "
                  "mode: thorough, respectable, liability-free. What would "
                  "you do puts them into survival mode. The same expert often "
                  "gives two different answers, and only the second one is "
                  "worth anything to you.",
             "eg": "Asking a surgeon whether to have the operation, and "
                   "asking whether he would have it done to his own mother, "
                   "frequently produce different answers."},
            {"n": "Declare your own position before you speak",
             "d": "The principle is only complete when you turn it inward. "
                  "Pushing a large recommendation, say what you have staked "
                  "and what you carry if it fails. A strong opinion with no "
                  "consequence attached deserves your own discount too. That "
                  "is signal-to-noise, not virtue.",
             "eg": "Push hard for a direction and ask in the same breath to "
                   "have your own review tied to it. A team hears the "
                   "difference immediately."},
        ],
        "q": [
            "Don't tell me what you think, tell me what you have in your "
            "portfolio.",
            "Those who don't take risks should never be involved in making "
            "decisions.",
            "Make the builder sleep in the house he built.",
        ],
        "apply":
            "Where you are: you have been handed advice that sounds "
            "thoroughly professional.\n"
            "Ask first: what has this person staked in the outcome? Does the "
            "answer change when you ask instead what they would do "
            "themselves?\n"
            "Where it goes wrong: using skin in the game to dismiss every "
            "outside view. Having no position is not the same as having no "
            "information. It only means a discount.",
    },
]

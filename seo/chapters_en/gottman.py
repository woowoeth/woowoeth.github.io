# -*- coding: utf-8 -*-
"""John Gottman — English."""

PARENT = {
    "name": "John Gottman",
    "slug": "gottman",
    "blurb": "Deep read",
    "items": [
        {"k": "four-horsemen", "n": "The four horsemen",
         "w": "Four signals that predict a breakup", "ready": True,
         "line": "Fifteen minutes of one argument, over ninety per cent accurate"},
        {"k": "repair-attempts", "n": "Repair attempts",
         "w": "Whether you fight matters less than whether you stop", "ready": True,
         "line": "Happy couples fight. Someone reaches the brake"},
    ],
}

CHAPTERS = [
    {
        "k": "four-horsemen",
        "n": "The four horsemen",
        "w": "Four signals that predict a breakup",
        "src": "The Gottman marriage lab; The Seven Principles for Making "
               "Marriage Work",
        "dek": "He watches fifteen minutes of one argument. This piece is "
               "about what he is actually watching.",
        "story":
            "Gottman recorded thousands of couples talking, coded expression, "
            "tone and heart rate frame by frame, then tracked who divorced "
            "years later. What predicted a breakup wasn't how fiercely they "
            "fought but whether four signals appeared, which he called the "
            "four horsemen: criticism (attacking the person, not the act), "
            "contempt (sarcasm, eye-rolling), defensiveness (returning the "
            "blame) and stonewalling (shutting the other out). ==The single "
            "strongest predictor of divorce is contempt== — and the research "
            "found it affects the recipient's immune function.",
        "f": [
            {"n": "Criticism and complaint are different things",
             "d": "A complaint targets behaviour: you didn't do the washing "
                  "up and I'm exhausted. Criticism targets character: you're "
                  "just lazy. The first can be solved; the second can only be "
                  "defended. Many people think they're raising an issue while "
                  "every sentence defines the other person, and so the same "
                  "problem runs ten years.",
             "eg": "Swap 'you never deal with the kids' for 'I did all three "
                   "pickups this week'. Same event, and the second can be "
                   "caught."},
            {"n": "Contempt is a slow poison, not venting",
             "d": "Eye-rolling, mockery, mimicking their tone — all of it "
                  "says I am above you. It differs from anger: anger is about "
                  "the event, contempt says the person is unworthy. It's the "
                  "strongest single predictor in his data because it "
                  "destroys the foundation, not one conversation.",
             "eg": "'What would you know' and 'fine, you're always right' "
                   "need correcting on the spot. That isn't arguing, it's "
                   "demolition."},
            {"n": "Defensiveness returns the ball, it doesn't clarify",
             "d": "'I've been busy, and so have you' looks like explaining "
                  "and is a counter-attack. Its function is to refuse any "
                  "share of responsibility, and once both sides are "
                  "defending, the conversation becomes mutual evidence and "
                  "never reaches a solution.",
             "eg": "When the pickups come up, take the part you can admit — "
                   "'you did do all three' — before explaining your side."},
        ],
        "apply":
            "Where you are: the same thing gets fought about and every round "
            "escalates.\n"
            "Ask first: was that last sentence about the event or about the "
            "person? Any sarcasm or eye-rolling? Am I explaining or returning "
            "the ball?\n"
            "Where it goes wrong: using the four horsemen to charge the other "
            "person — 'that's contempt' is itself an attack. It's a checklist "
            "for yourself, not a verdict.",
        "q": [
            "The strongest single predictor of divorce is contempt.",
            "Criticism targets the person. A complaint targets the act.",
            "The more often the four appear, the likelier the breakup.",
        ],
    },
    {
        "k": "repair-attempts",
        "n": "Repair attempts",
        "w": "Whether you fight matters less than whether you stop",
        "src": "The Gottman marriage lab",
        "dek": "Healthy relationships argue fiercely too. So where do they "
               "differ from the ones that break.",
        "story":
            "One of Gottman's counterintuitive findings: ==happy couples "
            "aren't the ones who don't fight, they're the ones who repair "
            "while fighting==. He called the move of reaching for the brake "
            "mid-escalation a repair attempt — a joke, an offered way out, a "
            "'wait, we've gone off topic'. In stable relationships repair "
            "attempts succeed more often, and not because the technique is "
            "better: because the other person is willing to take it. That "
            "willingness depends on the balance built up beforehand. He put a "
            "number on it — in stable relationships positive interactions run "
            "about five to one against negative.",
        "f": [
            {"n": "Repair succeeds or fails on the ordinary days",
             "d": "The same joke defuses things in a relationship with a "
                  "healthy balance and reads as not taking it seriously in "
                  "one that's overdrawn. So what decides whether a conflict "
                  "can be stopped is the unremarkable responses, presence and "
                  "small concessions of the past weeks. Technique in the "
                  "moment mostly fails.",
             "eg": "'Let's not fight' after three months of silence rarely "
                   "works. What would have worked is what wasn't done in "
                   "those three months."},
            {"n": "Taking the offered way out is harder than offering it",
             "d": "Offering it risks being refused; taking it means giving up "
                  "winning this round. Most relationships stick on the "
                  "second: they heard it, and 'why should I be the one to let "
                  "it go' stops them. Insisting on winning wins the round and "
                  "loses the relationship.",
             "eg": "'Have we gone a bit far?' — answering 'yeah, a bit' is "
                   "worth more than another round of evidence."},
            {"n": "Five to one is a balance, not a formula",
             "d": "The ratio gets misused as licence to say one cruel thing "
                  "per five kind ones. Gottman means the everyday texture of "
                  "the relationship should be mostly positive, not that "
                  "praise offsets attacks. An attack costs far more than "
                  "praise pays — that's why the ratio is lopsided.",
             "eg": "Use it as a check: over the past week, was the texture "
                   "between us warm or cold? Not 'have I complimented them "
                   "five times'."},
        ],
        "apply":
            "Where you are: mid-argument, both waiting for the other to give "
            "way first.\n"
            "Ask first: did they offer a way out that I didn't take? Is our "
            "balance healthy enough to cover this overdraft?\n"
            "Where it goes wrong: making repair something the same person "
            "always does. That isn't repair, it's one-sided depletion.",
        "q": [
            "Happy couples aren't the ones who don't fight. They repair.",
            "In stable relationships, positives run about five to one.",
            "Whether a repair works depends on the account built beforehand.",
        ],
    },
]

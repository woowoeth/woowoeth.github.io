# -*- coding: utf-8 -*-
"""Zhang Yiming — English.

He built the company behind TikTok and said almost nothing in public while
doing it, so outside China there is a product everyone knows and a founder
nobody has read. The two texts here are the ones his own staff were given: an
answer he keeps repeating about which trait he hires for, and an anniversary
speech that is mostly a list of ways attention goes wrong.
"""

PARENT = {
    "name": "Zhang Yiming",
    "slug": "zhang-yiming",
    "blurb": "Deep read",
    "items": [
        {"k": "delayed-gratification", "n": "Delayed gratification",
         "w": "The trait he rates highest", "ready": True,
         "line": "Most people want too badly to win the round in front of "
                 "them"},
        {"k": "ordinary-mind",
         "n": "An ordinary mind for extraordinary things",
         "w": "The ninth-anniversary speech", "ready": True,
         "line": "Watching your rival and watching yourself are both "
                 "interference"},
    ],
}

CHAPTERS = [
    {
        "k": "delayed-gratification",
        "n": "Delayed gratification",
        "w": "The trait he rates highest",
        "src": "Interview with Caijing, 2016, and his early microblog posts",
        "dek": "Asked which quality he values, he keeps giving one answer. "
               "What the phrase actually means in his hands.",
        "story":
            "In interviews Zhang Yiming has said that ==delayed gratification "
            "is one of the qualities I value most==, and that graduates who "
            "put never losing out first are spending themselves in advance. "
            "In his usage the phrase covers three layers. Choosing work: do "
            "not trade the fastest-growing seat for this year's salary. "
            "Building product: hold off monetising, as early Toutiao pushed "
            "commercialisation back and worked the recommendation engine and "
            "retention first. For the company: refuse to be satisfied by the "
            "result of the current fight. His own gloss on the reverse side "
            "is that most people want too badly to win the round in front of "
            "them.",
        "f": [
            {"n": "What is delayed is the payout, not the feedback",
             "d": "The common misuse is to invoke it while enduring years "
                  "with no signal at all. In his practice the feedback is "
                  "immediate, data watched daily, retention chased daily, and "
                  "only the conversion into money and reputation is "
                  "postponed. Delay with feedback is investment; delay "
                  "without it is self-admiration.",
             "eg": "Holding revenue back while growing, with the retention "
                   "curve checked every day. Without that curve it is not "
                   "delayed gratification, it is drifting."},
            {"n": "Cashing in early has a hidden price: compounding stops",
             "d": "The cost of early monetising never shows on the statement. "
                  "Damage the experience for this period's revenue and you "
                  "shrink the base that every later period grows from. The "
                  "trait is really a compound-interest sum: move the payout "
                  "later so the principal turns more times. People who can do "
                  "the arithmetic need no willpower.",
             "eg": "One more ad slot on the home screen lifts this month and "
                   "is deducted from retention three months out. Put both "
                   "curves on one chart and restraint stops being a virtue."},
            {"n": "It is a filter for choosing people, not only a private "
                  "discipline",
             "d": "He applies the trait in hiring, by looking at a "
                  "candidate's past choices: always the highest current pay, "
                  "or sometimes the steepest slope? Every move on a "
                  "curriculum vitae is a delayed-gratification question "
                  "already answered, and it answers more honestly than an "
                  "interview does.",
             "eg": "Two records: one where each move added thirty per cent of "
                   "salary and no capability, one with two pay cuts to change "
                   "field and real command now."},
        ],
        "q": [
            "Delayed gratification is one of the qualities I value most.",
            "Most people want too badly to win the round in front of them.",
            "Graduates who put never losing out first are spending themselves "
            "in advance.",
        ],
        "apply":
            "Where you are: a payout now and a steeper growth slope are "
            "sitting side by side.\n"
            "Ask first: during the delay, do I have a signal I can observe, "
            "and what does the compound arithmetic say the gap is?\n"
            "Where it goes wrong: using delayed gratification to grind "
            "through a dead end with no feedback; or delaying for ever and "
            "leaving the fruit to rot on the tree.",
    },
    {
        "k": "ordinary-mind",
        "n": "An ordinary mind for extraordinary things",
        "w": "The ninth-anniversary speech",
        "src": "ByteDance ninth-anniversary all-hands speech, March 2021",
        "dek": "A company known for ferocity spent its ninth anniversary on "
               "composure. The specific kinds of interference he named.",
        "story":
            "At ByteDance's ninth anniversary in 2021 Zhang Yiming's "
            "all-hands had a single theme: ==keep an ordinary mind while "
            "doing extraordinary things==. He named the common distortions. "
            "Toward the past, vanity about achievements or self-pity about "
            "setbacks. Toward competition, watching the rival so closely that "
            "the rival leads you. Toward the future, targets set so far from "
            "reality that anxiety eats the effort. His argument is that "
            "lifting attention off the patterns and the noise and seeing the "
            "present as it is produces better judgement. Extraordinary "
            "results come from an ordinary state of mind held at the "
            "decisive moments.",
        "f": [
            {"n": "Watching the rival hands over the steering wheel",
             "d": "Excess attention to competition means the agenda gets "
                  "taken over: they ship and you answer, they attack and you "
                  "defend. It looks like fighting back, but you are already "
                  "executing their strategy for them. Composure here is "
                  "concrete. A rival's move is one input, and its weight "
                  "should not exceed your own user data.",
             "eg": "A team that calls an emergency alignment for every "
                   "competitor launch finds a year later that the roadmap was "
                   "written by the other side. Make it a monthly review."},
            {"n": "Vanity and self-pity are the same coin",
             "d": "Pairing them is exact. Pride in past success and grief "
                  "over a setback run on the same mechanism, with attention "
                  "locked on me rather than on the thing. Decisions made in "
                  "either state serve a self-image: one proving it still has "
                  "it, the other proving it was unfair.",
             "eg": "After a winning streak you cannot kill a project you "
                   "started; after a loss you rush a comeback. Opposite "
                   "moves, one driver."},
            {"n": "Targets within reach keep anxiety from taking over",
             "d": "A target detached from reality does not produce drive, it "
                  "produces anxiety, and anxiety distorts judgement "
                  "systematically: short horizons inflated, fundamentals "
                  "skipped, remedies grabbed at random. Composure is not the "
                  "absence of ambition. It is ambition cut to a scale you can "
                  "reach on tiptoe.",
             "eg": "Break number one in three years into two verifiable "
                   "milestones this quarter. Same ambition: one phrasing "
                   "manufactures anxiety, the other manufactures progress."},
        ],
        "q": [
            "Keep an ordinary mind while doing extraordinary things.",
            "Watch your rival too closely and you end up being led.",
            "See the present as it is and judgement improves.",
        ],
        "apply":
            "Where you are: competition is white-hot and the team swings "
            "between elation and dread.\n"
            "Ask first: how much of this week's agenda was set by the other "
            "side, and are we looking at the thing or at ourselves?\n"
            "Where it goes wrong: reading composure as refusing to fight the "
            "fights that have to be fought; or saying ordinary mind while the "
            "targets and the review cycle are still designed by anxiety.",
    },
]

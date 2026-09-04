# -*- coding: utf-8 -*-
"""Han Feizi — English."""

PARENT = {
    "name": "Han Feizi",
    "slug": "han-feizi",
    "blurb": "Deep read",
    "items": [
        {"k": "not-counting-on-goodness", "n": "Don't build a system that needs good people",
         "w": "Make the right move the cheap one", "ready": True,
         "line": "Rules aren't there to improve anyone"},
        {"k": "two-handles", "n": "The two handles",
         "w": "Reward and punishment can't be lent out", "ready": True,
         "line": "Hand those over and the seat is empty"},
        {"k": "form-and-name", "n": "Match the deed to the word",
         "w": "What was said, what was done", "ready": True,
         "line": "The gap between them is where the problem is"},
    ],
}

CHAPTERS = [
    {
        "k": "not-counting-on-goodness",
        "n": "Don't build a system that needs good people",
        "w": "Make the right move the cheap one",
        "src": "Han Feizi, Eminent Learning; The Five Vermin",
        "dek": "A system that only runs when people are conscientious hasn't "
               "started working yet. How to design rules that don't need it.",
        "story":
            "Han Feizi puts it coldly: ==I do not count on people being good "
            "to me; I make it so they cannot do wrong.== He offers an "
            "arithmetic. Wait for arrow shafts that straighten themselves and "
            "in a hundred generations you get no arrows; wait for wood that "
            "rounds itself and in a thousand you get no wheels. Yet everyone "
            "has arrows and wheels, because someone invented the jig that "
            "straightens them. His conclusion: government cannot wait for "
            "sages. It builds tools.",
        "f": [
            {"n": "Conscientiousness is scarce and can't be the foundation",
             "d": "Depending on people to be conscientious stakes the "
                  "system's stability on its least controllable variable. His "
                  "alternative is the jig — the tool that straightens timber. "
                  "Rules don't exist to improve people. They exist so that "
                  "ordinary people produce acceptable results.",
             "eg": "'Everyone please follow the style guide' won't converge "
                   "in ten years. A linter converges it in a day. Not "
                   "conscience — tooling."},
            {"n": "Make the right road the least effortful one",
             "d": "The practical version of 'make it so they cannot do wrong' "
                  "is to build the non-compliant road so it costs more than "
                  "the compliant one. If going round the process is faster "
                  "than going through it, no amount of exhortation matters. "
                  "People are choosing the cheaper path.",
             "eg": "Expenses take five steps and three signatures, and paying "
                   "yourself back later takes one. Somebody will pay "
                   "themselves back later."},
            {"n": "Don't design for the rare case",
             "d": "The commonest misuse is constraining everyone to stop one "
                  "or two. Han Feizi is describing universal tools, not "
                  "patches aimed at individuals. The cost of a rule is borne "
                  "by everybody and the benefit accrues against a few. That "
                  "ledger rarely balances.",
             "eg": "One faked claim, so now every claim needs three photos. "
                   "The faker adapts; several hundred people lose two hours a "
                   "month."},
        ],
        "apply":
            "Where you are: the same class of problem keeps recurring and "
            "you've raised it many times.\n"
            "Ask first: is the right road currently more effort than the "
            "wrong one?\n"
            "Where it goes wrong: substituting announcements for tools; "
            "making everyone pay a cost in order to block a handful.",
        "q": [
            "I do not count on people being good. I make wrong impossible.",
            "Wait for arrows that straighten themselves and you get no "
            "arrows.",
            "Rules don't make people better. They make ordinary work "
            "acceptable.",
        ],
    },
    {
        "k": "two-handles",
        "n": "The two handles",
        "w": "Reward and punishment can't be lent out",
        "src": "Han Feizi, The Two Handles",
        "dek": "What power actually consists of. It turns out to be two "
               "things, and neither can be handed to anyone.",
        "story":
            "Han Feizi states it like a definition: ==the ruler controls his "
            "ministers by two handles, and the two handles are punishment and "
            "favour==. Killing is punishment; reward is favour. His example "
            "is the state of Qi, where the minister Tian Chang obtained ranks "
            "and stipends from the ruler to distribute to the officials, and "
            "lent grain by a large measure while collecting by a small one, "
            "putting the people in his debt. The ruler ended up hollow. His "
            "verdict: Tian Chang wasn't too strong. The ruler gave away the "
            "handle of favour.",
        "f": [
            {"n": "Power's substance is reward and consequence",
             "d": "Titles, grades and reporting lines are the form. What "
                  "actually decides who listens to whom is who can grant good "
                  "outcomes and who can bring bad ones. Everything else can "
                  "be delegated; hand over these two and the seat is empty. "
                  "The name remains and nobody is looking at you.",
             "eg": "You're nominally in charge, and raises, promotions and "
                   "ratings are decided elsewhere. The team aligns to the "
                   "other person. That's structure, not loyalty."},
            {"n": "Lending them out is easy; taking them back is not",
             "d": "Once one person exercises reward and punishment for long "
                  "enough, the organisation re-forms around them. Taking it "
                  "back is no longer a question of authority — you face a "
                  "network of dependence, and everyone who benefited will "
                  "instinctively defend them.",
             "eg": "One senior person has allocated resources for years. "
                   "Moving them means moving everyone they lifted."},
            {"n": "Deliver both yourself",
             "d": "Letting someone else announce the good news and carrying "
                  "the bad yourself sounds considerate. It gives away the "
                  "favour and keeps the punishment. Han Feizi advises the "
                  "opposite: both must come from you, or people only remember "
                  "whoever handed them the good thing.",
             "eg": "HR announces the raise and the manager delivers the "
                   "criticism. Gratitude goes to the company, resentment to "
                   "the manager."},
        ],
        "apply":
            "Where you are: you're nominally responsible for something and "
            "can't move it.\n"
            "Ask first: on this, who currently decides the good outcomes and "
            "the bad ones?\n"
            "Where it goes wrong: delegating reward and punishment as though "
            "they were admin; letting others announce good news while you "
            "absorb the bad.",
        "q": [
            "The ruler controls by two handles: punishment and favour.",
            "A tiger masters a dog by claws. Lend them out and it reverses.",
            "Everything else can be delegated. These two empty the seat.",
        ],
    },
    {
        "k": "form-and-name",
        "n": "Match the deed to the word",
        "w": "What was said, what was done",
        "src": "Han Feizi, The Way of the Ruler; The Two Handles",
        "dek": "The hard part of review isn't setting standards. It's what "
               "you do when the standard and the facts disagree.",
        "story":
            "Han Feizi's method is ==matching form to name==: the official "
            "states what he will accomplish (the name), and you check it "
            "against what was actually produced (the form). His extreme "
            "example: Marquis Zhao of Han fell asleep drunk, and the keeper "
            "of the hat, seeing him cold, covered him with a robe. On waking "
            "the marquis punished both the keeper of the robes and the keeper "
            "of the hat — one for neglect, one for overstepping. Overstepping "
            "is the worse harm, because it dissolves the boundary. The "
            "principle being established: your own words are the measure.",
        "f": [
            {"n": "The standard comes out of his mouth",
             "d": "Let the name define itself and the task define itself. Not "
                  "a target imposed from above but a commitment stated by the "
                  "person carrying it. At review there is then no arguing "
                  "about whether the standard was reasonable — he set it. The "
                  "only question left is whether it was met.",
             "eg": "Rather than assigning a number, have them write what they "
                   "will deliver this quarter and how it will be judged. "
                   "Review only that page."},
            {"n": "Overshooting counts too",
             "d": "Form exceeding name is also pursued. Doing more looks "
                  "good, and it means the judgement at commitment time was "
                  "wrong, and it usually consumed someone else's resources. A "
                  "system that punishes only shortfalls trains everyone to "
                  "commit as low as possible.",
             "eg": "Everyone sets targets at what they can certainly hit and "
                   "exceeds them yearly. That organisation no longer knows "
                   "its own capacity."},
            {"n": "Reconcile against the page agreed beforehand",
             "d": "If the ruler is chosen at review time, the whole thing "
                  "becomes retroactive approval. Matching requires the name "
                  "first and the form after, with no change in between. "
                  "Change it once and the system reverts to personal "
                  "favour.",
             "eg": "Swap the criteria at quarter end, however reasonably, and "
                   "nobody writes a serious commitment next quarter."},
        ],
        "apply":
            "Where you are: it's review time and the two of you disagree on "
            "whether it counts as done.\n"
            "Ask first: before this started, what standard did he write down "
            "himself?\n"
            "Where it goes wrong: chasing only shortfalls and never "
            "overshoots, which pushes everyone to commit low; deciding which "
            "ruler to use only after the fact.",
        "q": [
            "Let the name define itself, and the task define itself.",
            "Deed fits the task and task fits the words: reward. Otherwise: "
            "punish.",
            "Change the ruler at review and nobody writes a real commitment "
            "again.",
        ],
    },
]

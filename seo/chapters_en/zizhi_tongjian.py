# -*- coding: utf-8 -*-
"""The Comprehensive Mirror — English.

An English reader who has heard of any Chinese history book has heard of the
Records of the Grand Historian, and expects a second one to be more of the
same. It is not: this is a work of systems analysis with a single stated
selection rule, written for one reader. The two chapters take that rule and
the argument the whole thing opens with, both of which are about choosing.
"""

PARENT = {
    "name": "The Comprehensive Mirror",
    "slug": "zizhi-tongjian",
    "blurb": "Deep read",
    "items": [
        {"k": "talent-and-virtue", "n": "Talent and character",
         "w": "The dangerous man is the able one", "ready": True,
         "line": "Better a fool than a man of talent with no character"},
        {"k": "what-to-keep", "n": "Worth copying, worth avoiding",
         "w": "Fix the selection rule first", "ready": True,
         "line": "Nineteen years, and one rule for what got in"},
    ],
}

CHAPTERS = [
    {
        "k": "talent-and-virtue",
        "n": "Talent and character",
        "w": "The dangerous man is the able one",
        "src": "The Comprehensive Mirror, Zhou chronicles, book one",
        "dek": "The first argument in the first book of the whole work is "
               "about choosing people. This is about why it sits there.",
        "story":
            "The book opens with the partition of Jin, and its first great "
            "event is the fall of Zhibo. Zhibo had five qualities above other "
            "men — bearing, horsemanship, skill, eloquence, decision — and one "
            "lack: he was not humane. On this Sima Guang hangs the first of "
            "his own comments. Talent is the resource of character; character "
            "is the commander of talent. He sorts people into four: both "
            "complete is a sage, both absent is a fool, ==character over "
            "talent is a gentleman, talent over character is a small man.== "
            "Then blunt advice: failing a sage or a gentleman, take the fool.",
        "f": [
            {"n": "Talent is an amplifier; character sets the direction",
             "d": "Character commands, talent supplies — the image means "
                  "talent has no direction of its own. The same ability "
                  "doubles the return in a right direction and doubles the "
                  "loss in a wrong one. So the stronger the person, the larger "
                  "the damage when the direction is wrong. That is arithmetic, "
                  "not moralising.",
             "eg": "An outstanding engineer who disagrees with the "
                   "architecture accrues technical debt faster than three "
                   "ordinary ones, because he writes more and writes it "
                   "faster."},
            {"n": "A fool's damage has a ceiling",
             "d": "His reasoning is utilitarian. A fool who wants to do harm "
                  "lacks the means and is easy to guard against; a capable man "
                  "of bad character does harm nobody can stop. Where you "
                  "cannot judge conduct, choosing the lower ceiling of ability "
                  "is a way of capping the worst case.",
             "eg": "In a critical seat, a middling person with clear "
                   "boundaries beats a brilliant one who keeps crossing them. "
                   "The first has a low ceiling and a high floor."},
            {"n": "The trouble is that we see talent first",
             "d": "He names the root: talent is easy to see and character is "
                  "not. An interview can measure ability and cannot measure "
                  "where someone stops; a record can list the wins and not how "
                  "they were obtained. The bias is therefore systematic, not "
                  "occasional.",
             "eg": "Every selection process leans towards demonstrable "
                   "ability. To balance it you have to design a stage that "
                   "examines conduct, and not hope one appears."},
        ],
        "q": [
            "Talent is the resource of character; character is the commander "
            "of talent.",
            "Character over talent is a gentleman, talent over character a "
            "small man.",
            "Rather than get a small man, get a fool.",
        ],
        "apply":
            "Where you are: a candidate is clearly the strongest and something "
            "about how they operate worries you.\n"
            "Ask first: if they turn that ability in a direction I do not "
            "want, can I stop them?\n"
            "Where it goes wrong: reading it as a sermon about virtue; testing "
            "only ability at interview and never designing a stage that tests "
            "where someone stops.",
    },
    {
        "k": "what-to-keep",
        "n": "Worth copying, worth avoiding",
        "w": "Fix the selection rule first",
        "src": "Sima Guang, memorial on presenting the Comprehensive Mirror",
        "dek": "One thousand three hundred and sixty-two years of events. This "
               "is about the single rule that decided what went in.",
        "story":
            "He ran the compilation for nineteen years and the finished work "
            "runs to two hundred and ninety-four volumes. In the memorial "
            "presenting it he set out how he chose: cut what was long-winded, "
            "gather what was essential, ==take only what bears on the rise and "
            "fall of the state, on whether the people prospered or suffered, "
            "what is good enough to copy and bad enough to warn.== Shenzong, "
            "naming it, called it a mirror of what has been, useful to the art "
            "of governing. One rule throughout, which is why there is almost "
            "no ornament and almost nothing kept for completeness.",
        "f": [
            {"n": "Set the rule first or you never finish",
             "d": "Nineteen years, thirteen centuries of material: without a "
                  "selection rule you can apply mechanically, the work is "
                  "infinite. Take only is the condition that let the book be "
                  "completed. He did not know what to write; he knew clearly "
                  "what not to.",
             "eg": "A survey with no stated exclusion rule never ends, because "
                   "any new material looks worth one more look. Write down "
                   "what you will not read and progress starts existing."},
            {"n": "The rule has to admit the bad",
             "d": "Bad enough to warn stands beside good enough to copy. A "
                  "library of successes only teaches that there is one road "
                  "that works. Failures usually carry more information, "
                  "because a success can be accidental in many ways and a "
                  "failure's mechanism is generally clearer.",
             "eg": "A company that records best practice and never records "
                   "post-mortems teaches new people a method assembled "
                   "entirely from survivors."},
            {"n": "The rule has to be executable by someone else",
             "d": "The work was divided between Liu Ban, Liu Shu and Fan Zuyu, "
                  "with Sima Guang over the whole. A taste that exists only in "
                  "the editor's head cannot be divided. Only a rule written "
                  "down and applied identically by three people will hold for "
                  "nineteen years.",
             "eg": "If the content standard lives only with the editor, "
                   "quality collapses the moment the team grows. Write it as "
                   "three rules another person can apply."},
        ],
        "q": [
            "Cut what is long-winded; gather what is essential.",
            "Good enough to copy, bad enough to warn.",
            "A mirror of what has been, useful to the art of governing.",
        ],
        "apply":
            "Where you are: there is too much material and you are hesitating "
            "over what to include.\n"
            "Ask first: what is my selection rule, and can I write it as one "
            "sentence someone else could apply?\n"
            "Where it goes wrong: keeping only the successes; leaving the rule "
            "in your own head, where it cannot be divided up.",
    },
]

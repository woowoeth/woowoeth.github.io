# -*- coding: utf-8 -*-
"""Anders Ericsson — English.

The English reader arrives holding a number: ten thousand hours. It is not
his, he spent the last fifteen years of his life saying so, and the number
quietly replaced the finding it came from. The job of these two pages is to
give the finding back — that what the hours contain decides the level, and
that hours on their own are only correlated with it.
"""

PARENT = {
    "name": "Anders Ericsson",
    "slug": "ericsson",
    "blurb": "Deep read",
    "items": [
        {"k": "deliberate-practice",
         "n": "Practising what you can already do is rest",
         "w": "Stay at the edge of what you cannot do", "ready": True,
         "line": "The best students spent their hours on the bars they could "
                 "not play"},
        {"k": "not-ten-thousand-hours",
         "n": "Ten thousand hours is a misreading",
         "w": "He spent years saying so", "ready": True,
         "line": "Ten years of experience can be one year lived ten times"},
    ],
}

CHAPTERS = [
    {
        "k": "deliberate-practice",
        "n": "Practising what you can already do is rest",
        "w": "Stay at the edge of what you cannot do",
        "src": "The Berlin violin study, 1993; Peak",
        "dek": "Two people practise three hours each. One improves and one "
               "does not. This page is about what the hours contained.",
        "story":
            "Ericsson and his colleagues sorted the violin students at the "
            "Berlin academy of music by how good they were, and the top group "
            "had indeed accumulated more hours. The interesting difference "
            "was inside the hours. The average students played through pieces "
            "they could already play, enjoying the fluency. The best ones "
            "spent their time on the few bars they could not play, stopping "
            "and repeating and stopping again. ==Purposeful practice happens "
            "outside the comfort zone, and it needs feedback that arrives "
            "while you can still use it.== Fluency feels like progress. It is "
            "the sensation of not improving.",
        "f": [
            {"n": "Comfortable practice is a performance for yourself",
             "d": "Fluency is a signal of competence already reached, not of "
                  "competence being built. The test is blunt: how much of the "
                  "hour did you spend failing and going back? If none of it, "
                  "you were not practising, you were rehearsing.",
             "eg": "An hour of playing pieces you know is an hour of "
                   "listening to yourself. The three bars you always fumble "
                   "are the practice."},
            {"n": "Blind repetition makes the wrong version stick",
             "d": "If you cannot tell which attempt was wrong, repeating it "
                  "only makes the wrong version more automatic. This is why "
                  "thirty years of driving does not produce a better driver: "
                  "nobody has ever told him which turn was bad. Feedback "
                  "ranks above hours.",
             "eg": "Writing more does not make you write better. Someone has "
                   "to say which paragraph they stopped reading, or you leave "
                   "it a week and become that someone."},
            {"n": "Experts run on mental representations",
             "d": "Ericsson's term for what a specialist actually owns is a "
                  "mental representation: a detailed internal model of the "
                  "domain. A chess player sees a position, not pieces. Models "
                  "get built by failing against real problems, and cannot be "
                  "read into place.",
             "eg": "Watching a hundred games buys impressions. Playing ten "
                   "and going back through each one afterwards builds the "
                   "model."},
        ],
        "q": [
            "If you never push yourself beyond your comfort zone, you will "
            "never improve.",
            "Repetition without feedback engraves the error instead of "
            "removing it.",
            "The best students spent their hours on the bars they could not "
            "play.",
        ],
        "apply":
            "Where you are: you have practised for months and cannot see the "
            "difference.\n"
            "Ask first: how much of the last hour went on something you could "
            "not do, and who told you which part was wrong?\n"
            "Where it goes wrong: hearing it has to hurt as grind until you "
            "break — his subjects practised in short intense blocks and slept "
            "more than anybody.",
    },
    {
        "k": "not-ten-thousand-hours",
        "n": "Ten thousand hours is a misreading",
        "w": "He spent years saying so",
        "src": "Ericsson's own corrections to the ten-thousand-hour rule; Peak",
        "dek": "The number travelled much further than the research it came "
               "from. This page is about what it got wrong.",
        "story":
            "The rule comes from Outliers, not from Ericsson, and he spent "
            "the rest of his life correcting it. Ten thousand was an average "
            "for the best group at age twenty, and half of that group had not "
            "reached it. Thresholds differ enormously between fields. Worse, "
            "the number quietly replaced the finding. ==What the research "
            "showed is that the manner of practice decides the level; hours "
            "are only correlated with it.== A demanding result became a "
            "comfortable permit: put the time in and you qualify. That is "
            "precisely the half he was arguing against.",
        "f": [
            {"n": "Ten years of experience, or one year ten times",
             "d": "Time served is not skill. Most roles stop generating new "
                  "difficulty after the first year or two, and the years "
                  "after that are repetition wearing a longer title. The "
                  "honest question about anybody's growth is when they were "
                  "last out of their depth.",
             "eg": "Ask a candidate what they could not do a year ago and can "
                   "do now. It carries more information than the number of "
                   "years on the CV."},
            {"n": "The threshold is different in every field",
             "d": "Deliberate practice is strongest where the rules hold "
                  "still and the feedback comes back fast: instruments, "
                  "chess, surgery. Where results arrive late and luck is "
                  "loud, hours explain much less. One number cannot cross "
                  "those boundaries.",
             "eg": "Applying put the hours in to investing is the expensive "
                   "version of the mistake. The feedback is slow and mostly "
                   "noise, so repetition alone builds nothing."},
            {"n": "Change the method before you add the hours",
             "d": "The practical damage of the rule is that it sends people "
                  "to spend more rather than to practise differently. When "
                  "you are stuck, the variable with room left in it is the "
                  "structure of the session, not its length.",
             "eg": "Three years of flashcards and no progress will not be "
                   "fixed by a fourth. Using the language badly in front of "
                   "someone who corrects you will."},
        ],
        "q": [
            "There is nothing special or magical about ten thousand hours.",
            "The manner of practice decides the level. Hours are only "
            "correlated.",
            "Growth shows up as when you were last out of your depth.",
        ],
        "apply":
            "Where you are: you have put a long stretch into something and "
            "the results are flat.\n"
            "Ask first: when were you last genuinely stuck? How fast does "
            "this field answer you back? Is the fix more hours or a different "
            "session?\n"
            "Where it goes wrong: using the misreading as permission to stop "
            "accumulating — he wanted high-quality hours over years, not "
            "fewer of them.",
    },
]

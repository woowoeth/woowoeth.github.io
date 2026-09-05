# -*- coding: utf-8 -*-
"""Learning and growth 第 18 批：Anders Ericsson、Richard Feynman、
Karl Popper、Socrates、Thinking, Fast and Slow。

这五个人在英文读者那里都先被一层二手包装挡住了：deliberate practice 变成
「一万小时」，System 1/2 变成办公室黑话，Feynman technique 变成学习法卖点，
falsifiable 变成吵架用词，苏格拉底变成海报上那句「我知道我一无所知」。
英文页的活儿是把那层拆掉，回到原作者到底说了什么 —— 所以引语一律还原英文
原句（Ericsson、Feynman、Kahneman 本来就是英文），希腊文用通行英译。
"""

ENTRIES = [
    {
        "c": "Learning and growth", "n": "Anders Ericsson", "slug": "ericsson",
        "e": "1993 · the violin study", "w": "Method over hours",
        "y": 1993,
        "d": "A psychologist who spent a career on how the best in any field "
             "actually got there. His best-known research reached the public "
             "as the ten-thousand-hour rule, which is the one thing he then "
             "spent the rest of his life denying. What decides the level is "
             "not the hours but what happens inside them: work at the edge of "
             "what you cannot yet do, with a specific goal and feedback fast "
             "enough to use. He called it deliberate practice. Repeating what "
             "you can already do is rest with better posture.",
        "story":
            "Before the violinists there was a college student the papers "
            "call SF. Ericsson and William Chase sat him down several times a "
            "week and read him digits to repeat back. He started where "
            "everybody starts, at about seven. He was a distance runner, and "
            "began hearing strings of numbers as running times, so that 3492 "
            "became a near-record mile. Two years and a couple of hundred "
            "hours later he could hold eighty-two digits. His memory for "
            "letters stayed exactly average. Nothing general had improved. He "
            "had built one structure, and it fitted one thing.",
        "f": [
            {"n": "Practising what you can do is rest",
             "d": "Fluency is pleasant and it is the feeling of not "
                  "improving. Progress happens in the region where you keep "
                  "failing, which looks inefficient from outside and is the "
                  "only part that changes what you are capable of.",
             "eg": "An hour of familiar pieces is an hour of enjoying "
                   "yourself. What needed the hour was the passage you keep "
                   "getting wrong."},
            {"n": "Feedback outranks hours",
             "d": "Repetition without correction does not teach. It makes the "
                  "wrong version automatic. Thirty years of driving produces "
                  "a driver of exactly the same standard, because nobody has "
                  "ever told him which turn was bad.",
             "eg": "If nobody will say which paragraph they stopped reading, "
                   "build the feedback yourself: put it away a week, then "
                   "read it as a stranger."},
            {"n": "Experts hold models, not memories",
             "d": "What a specialist owns is a mental representation of the "
                  "field, built by failing against real problems. A chess "
                  "player sees a position rather than pieces. Watching and "
                  "memorising do not construct one.",
             "eg": "Ten games played and gone back through afterwards teach "
                   "more than a hundred watched."},
            {"n": "Ten thousand hours was never the finding",
             "d": "The number was an average for one group in one field, and "
                  "half that group had not reached it. He objected to it for "
                  "the rest of his life, because it converts a demanding "
                  "result into permission to simply wait.",
             "eg": "Ten years in the job is not ten years of experience. It "
                   "is often one year, repeated, under a longer title."},
        ],
        "apply":
            "Split your last practice hour in two: the part you could already "
            "do, and the part you kept failing at. If the second part is "
            "small, that is your answer. Then find out what is going to tell "
            "you which attempts were wrong. If nothing is, build that before "
            "you add another hour.",
        "q": [
            "Purposeful practice means working just past what you can do.",
            "Feedback ranks above hours. Without it, repetition teaches "
            "nothing.",
            "What an expert owns is a model of the field, not a memory.",
        ],
        "l": ["Bruce Lee", "Carol Dweck", "Lev Vygotsky", "Miyamoto Musashi"],
        "contrast": [
            {"n": "Bruce Lee",
             "why": "Both refuse to count repetitions: Lee practises one kick "
                    "ten thousand times, Ericsson says those ten thousand "
                    "only count if something corrects them"},
            {"n": "Carol Dweck",
             "why": "She works on how a failure gets read, he works on "
                    "whether the task was hard enough to produce one"},
        ],
    },
    {
        "c": "Learning and growth", "n": "Richard Feynman", "slug": "feynman",
        "e": "1918–1988 · United States", "w": "Do not fool yourself",
        "y": 1918,
        "d": "Nobel physicist, Manhattan Project, and the member of the "
             "Challenger commission who insisted his own dissenting appendix "
             "be printed with the report. What he left people outside physics "
             "is larger than what he left inside it: a set of tests for "
             "whether you actually understand something. The standard is "
             "close to rude. If you cannot get a first-year student to follow "
             "it, you have not got it. He held science itself to the same "
             "line: the first principle is not to fool yourself, and you are "
             "the easiest person available to fool.",
        "story":
            "He taught for a year in Rio and found students who could recite "
            "everything and use none of it. In a lecture he read out a "
            "definition of triboluminescence, the light emitted when crystals "
            "are crushed, and the room recognised it instantly. Then he asked "
            "why, when you crush a lump of sugar in the dark, you see a "
            "flash. Nobody connected the two. At the end of the year he told "
            "the assembled faculty and the education ministry that no science "
            "was being taught in Brazil at all.",
        "f": [
            {"n": "If you cannot teach it, you have not got it",
             "d": "A technical term compresses. Forbid it and you have to "
                  "unpack the idea yourself, and the places you cannot unpack "
                  "are the places you were storing a label. It is the "
                  "cheapest accurate self-test there is.",
             "eg": "Describe your work to a relative. Each time you retreat "
                   "into the trade word, mark it. That list is your real "
                   "syllabus."},
            {"n": "The easiest person to fool is you",
             "d": "Fooling yourself takes no bad faith, only a stake in the "
                  "answer. When you want a conclusion, evidence for it "
                  "becomes strangely easy to find. So honesty here is a "
                  "method requirement rather than a moral one.",
             "eg": "Before the review, write the case against your own "
                   "proposal first. Written second, that column always comes "
                   "out shorter."},
            {"n": "Reality before public relations",
             "d": "Challenger was not an engineering shortfall. It was an "
                  "organisation that preferred a good-looking argument to a "
                  "cold seal. Wherever people report upward, the same "
                  "substitution is on offer every week.",
             "eg": "When the numbers disappoint, notice whether you are "
                   "changing the judgement or the sentence. The sentence gets "
                   "you through this meeting only."},
            {"n": "Derive it once instead of remembering it ten times",
             "d": "His way of learning was to throw the result away and "
                  "rebuild it, going back whenever he got stuck. Slow, and "
                  "what comes out transfers. A remembered answer serves only "
                  "the question it came from.",
             "eg": "Rather than learn the conditions under which a formula "
                   "holds, reconstruct once where it came from. The "
                   "conditions then explain themselves."},
        ],
        "apply":
            "Take one thing you believe you understand and explain it aloud "
            "to somebody outside your field, using no terms of art. Mark "
            "every place you stall; that list is what you have to go back to. "
            "And before any judgement where you gain if it goes your way, "
            "write the case against it first.",
        "q": [
            "After you've not fooled yourself, it's easy not to fool other "
            "scientists.",
            "Nature cannot be fooled.",
            "Knowing the name of a thing is not knowing the thing.",
        ],
        "l": ["Albert Einstein", "Socrates", "Charlie Munger", "Karl Popper"],
        "contrast": [
            {"n": "Albert Einstein",
             "why": "Two physicists' habits: Einstein restated the problem "
                    "until it turned simple, Feynman rebuilt the answer until "
                    "it was his"},
            {"n": "Socrates",
             "why": "Both use questions to force ignorance into the open. "
                    "Socrates aims them at other people, Feynman at himself"},
        ],
    },
    {
        "c": "Learning and growth", "n": "Karl Popper", "slug": "popper",
        "e": "1902–1994 · Vienna and London",
        "w": "It has to be refutable", "y": 1902,
        "d": "A philosopher of science whose opening question was ordinary "
             "and whose answer changed the subject. Astrology explains events "
             "and so does physics, so what separates them? Not explanatory "
             "power. A theory that no observation could contradict is not "
             "strong, it is empty. The test carries straight over into "
             "everyday judgement: a claim that fits every outcome has told "
             "you nothing about any of them.",
        "story":
            "In 1919, before any of the philosophy, he was volunteering in "
            "Vienna's child guidance clinics. He brought Alfred Adler a case "
            "that did not look to him like an Adlerian one, and Adler "
            "explained it in terms of inferiority feelings without "
            "difficulty, and without having seen the child. Popper, uneasy, "
            "asked how he could be so certain. Because of my thousandfold "
            "experience, Adler said. Popper could not stop himself: and with "
            "this new case, I suppose, your experience has become "
            "thousand-and-one-fold. What struck him was not that Adler was "
            "wrong. It was that nothing could have counted against him.",
        "f": [
            {"n": "Explaining everything explains nothing",
             "d": "If any result at all can be absorbed by a theory, the "
                  "theory carries no information. The way to check is to ask "
                  "what observation would make its holder abandon it. No "
                  "answer means no test, and no test means no reason to lean "
                  "on it.",
             "eg": "Sentiment drove the rise. And the fall? Sentiment again. "
                   "It accounts for every outcome and therefore accounts for "
                   "none."},
            {"n": "Write the refuting condition before the result",
             "d": "People are remarkably able to read any outcome as support. "
                  "The only defence is to fix the criterion in advance. "
                  "Standards set afterwards give you a position that cannot "
                  "lose, and therefore cannot teach.",
             "eg": "Before shipping, write down the number that would mean "
                   "the assumption was wrong, and the date on which you will "
                   "go and look at it."},
            {"n": "Refuted is not the same as discarded",
             "d": "The usual misreading is that a theory shown wrong is "
                  "finished. His demand was the opposite: that it be exposed "
                  "to serious attempts to break it. Good ideas mostly get "
                  "stronger by surviving those attempts.",
             "eg": "Once a quarter, go looking for the strongest evidence "
                   "against your main position. Failing to find it is the "
                   "only real endorsement."},
            {"n": "Collect counter-examples, not confirmations",
             "d": "The default is to gather cases that agree, and the "
                  "hundredth one adds close to nothing. A single case that "
                  "disagrees is decisive. So the productive hour goes on "
                  "finding the exception, not extending the list.",
             "eg": "To find out whether people like the product, do not "
                   "survey the people still using it. Talk to three who "
                   "left."},
        ],
        "apply":
            "Next time somebody hands you a confident claim, ask what would "
            "have to happen for it to be wrong. If nothing would, treat it as "
            "a story rather than a finding. And before your own next bet, "
            "write down the condition that would make you drop it, with a "
            "date attached.",
        "q": [
            "We cannot prove a theory true. We can only fail to refute it.",
            "A claim that fits every outcome has told you nothing.",
            "One counter-example outweighs a hundred supporting cases.",
        ],
        "l": ["Richard Feynman", "Albert Einstein", "Socrates",
              "Thinking, Fast and Slow"],
        "contrast": [
            {"n": "Richard Feynman",
             "why": "The same rule from two sides: Popper gives the logical "
                    "criterion, Feynman the psychological warning about who "
                    "breaks it first"},
            {"n": "Thinking, Fast and Slow",
             "why": "Popper says what a careful mind should do; Kahneman "
                    "measures how far an ordinary one departs from it"},
        ],
    },
    {
        "c": "Learning and growth", "n": "Socrates", "slug": "socrates",
        "e": "Athens · 470–399 BC", "w": "Knowing you do not know",
        "y": -470,
        "d": "He wrote nothing. Everything we have comes through other "
             "people's dialogues. He charged no fees, which made him the "
             "poorest professional philosopher in Athens, and spent his days "
             "in the marketplace asking questions. The city executed him for "
             "corrupting the young and impiety, which in practice meant that "
             "his questions embarrassed people who could not afford to be "
             "embarrassed. His pupils arranged an escape and he refused it.",
        "story":
            "Crito came to the prison before dawn with everything arranged: "
            "guards paid, a ship waiting, a household abroad ready to take "
            "him. Socrates would not argue about whether the verdict had been "
            "just. He asked instead whether a private citizen may set aside a "
            "judgement he dislikes, and what a city would be if everybody "
            "did. Crito had to agree that it could not stand. Then leaving, "
            "Socrates said, would teach exactly that, and would do Athens "
            "more harm than anything he stood accused of. He stayed, and "
            "drank the hemlock.",
        "f": [
            {"n": "Not knowing, and not pretending to know",
             "d": "The line on the posters says he knew nothing. What he "
                  "actually claims is smaller and far more usable: about the "
                  "things he does not know, he does not suppose that he knows "
                  "them. That gap is the whole advantage.",
             "eg": "Say I have not checked that, and people bring you "
                   "answers. Say I know, and people bring you agreement, "
                   "which contains no information."},
            {"n": "Being good at one thing makes you sure about everything",
             "d": "He found the craftsmen genuinely skilled and, because of "
                  "that skill, convinced they understood the largest "
                  "questions too. A validated record in one domain is the "
                  "hardest thing to leave at the door of another.",
             "eg": "The strongest technical judgement in the room decides the "
                   "pricing as well, at the same volume, on none of the "
                   "evidence."},
            {"n": "He questioned rather than answered",
             "d": "He compared himself to a midwife: unable to give birth to "
                  "anything himself, only to help others deliver. A "
                  "conclusion somebody reaches under questioning gets "
                  "defended by them. One handed over gets dropped at the "
                  "first objection.",
             "eg": "Show him the flaw and one line changes. Ask until he "
                   "finds it and the same flaw gets fixed everywhere else in "
                   "the document."},
            {"n": "The examined life had a price and he paid it",
             "d": "Offered silence or exile instead of death, he took death, "
                  "on the ground that leaving would teach the city that "
                  "inconvenient judgements may be ignored. Consistency "
                  "between what he said and what he did cost him everything "
                  "it could cost.",
             "eg": "Any rule you announce and then quietly exempt yourself "
                   "from is not a rule. It is a preference with a press "
                   "office."},
        ],
        "apply":
            "Next time you are certain, run the three questions: what is this "
            "judgement resting on, under what conditions would it fail, and "
            "what have I not looked at? Run them especially when the "
            "conclusion suits you. Either the certainty gets firmer or a hole "
            "opens, and both are worth ten minutes.",
        "q": [
            "The unexamined life is not worth living.",
            "Wisdom begins in not pretending to know what you do not.",
            "An answer handed over gets dropped. One delivered gets defended.",
        ],
        "l": ["Wang Yangming", "Tao Te Ching", "Charlie Munger", "Ray Dalio"],
        "contrast": [
            {"n": "Wang Yangming",
             "why": "Two thousand years apart and the same move: Socrates "
                    "delivers what is already in you, Wang Yangming says the "
                    "knowing was there all along and only obscured"},
            {"n": "Machiavelli",
             "why": "The two ends of philosophy: one died for a principle, "
                    "the other wrote the manual for staying alive inside "
                    "power"},
        ],
    },
    {
        "c": "Learning and growth", "n": "Thinking, Fast and Slow",
        "slug": "thinking-fast-and-slow",
        "e": "2011 · Daniel Kahneman", "w": "Fast mind, slow mind",
        "y": 2011,
        "d": "Daniel Kahneman's summary of forty years of work with Amos "
             "Tversky, and the founding text of behavioural economics. He is "
             "the only psychologist to have won the Nobel in economics, in "
             "2002. The frame everybody took from it: a fast, automatic, "
             "associative mind and a slow, effortful, reluctant one. The "
             "frame he warned about in the same book: they are fictitious "
             "characters, not parts of the brain, and naming which one is "
             "speaking does not stop it speaking.",
        "story":
            "Teaching flight instructors in the Israeli Air Force, he said "
            "that praise works better than punishment. A senior instructor "
            "objected from experience: praise a cadet for a clean manoeuvre "
            "and the next one is worse, shout at a bad one and the next is "
            "better. Kahneman saw that the man had been watching regression "
            "to the mean and reading it as cause. An unusually good or bad "
            "flight is partly luck, and luck does not repeat. He called it "
            "the most important insight of his life: the mind will not leave "
            "a fluctuation alone without attaching a reason to it.",
        "f": [
            {"n": "Two systems, and one of them is lazy",
             "d": "The fast system answers almost everything and rarely "
                  "reports difficulty. The slow one is expensive and avoids "
                  "being started. The failure is not that the fast one errs. "
                  "It is that the slow one signs off instead of checking.",
             "eg": "A bat and ball cost a dollar ten, and the bat costs a "
                   "dollar more than the ball. Almost everybody says ten "
                   "cents. It is five."},
            {"n": "Losses weigh about twice as much",
             "d": "Losing a hundred hurts roughly as much as winning two "
                  "hundred pleases. It explains holding losers and selling "
                  "winners, why you will lose this beats you could gain that, "
                  "and why any reform meets more anger than gratitude.",
             "eg": "The people who lose from a change turn up to say so. The "
                   "people who gain are busy, and mostly do not know yet that "
                   "they gained."},
            {"n": "Anchoring, and where the first number came from",
             "d": "A number that arrives first shapes everything after it, "
                  "even when it is plainly irrelevant. Opening offers, list "
                  "prices before a discount, the tone set at the start of a "
                  "review: one mechanism, used on purpose.",
             "eg": "Ask what you would have estimated if you had never heard "
                   "their figure. The distance between the two answers is the "
                   "anchor."},
            {"n": "The premortem",
             "d": "Plans get built from the inside, where this project is "
                  "special, and ignore the base rate of comparable ones. The "
                  "fix is to gather everybody before starting, assume it has "
                  "already failed a year from now, and have each person write "
                  "down why.",
             "eg": "His own textbook team estimated two years. Comparable "
                   "projects ran seven to ten, with heavy attrition. It took "
                   "eight."},
        ],
        "apply":
            "Put three gates in front of any decision that matters. Sleep on "
            "it, so the fast answer loses its heat. Run a premortem: it is a "
            "year later and this failed, so write down why. And look up how "
            "comparable attempts actually went before you explain why yours "
            "is different.",
        "q": [
            "We can be blind to the obvious, and we are also blind to our "
            "blindness.",
            "Nothing in life is as important as you think it is, while you "
            "are thinking about it.",
            "The mind will not leave a fluctuation without a cause attached.",
        ],
        "l": ["Influence", "Charlie Munger", "Nassim Taleb", "George Soros"],
        "contrast": [
            {"n": "Influence",
             "why": "Two sides of one thing: Cialdini shows how the gaps get "
                    "used on you, Kahneman shows why the gaps are there"},
            {"n": "Sun Tzu",
             "why": "Reckoning in the temple is a forced start-up of the slow "
                    "system: settle the count before deciding whether to "
                    "fight at all"},
        ],
    },
]

INTROS = {
    "ericsson": "Spent his last years correcting the one number everybody "
                "learned from his research",
    "feynman": "Nobel physicist who treated not fooling yourself as a "
               "technical requirement, not a virtue",
    "popper": "Asked what separates physics from astrology, and answered with "
              "a single question",
    "socrates": "Wrote nothing, charged nothing, asked questions until Athens "
                "executed him",
    "thinking-fast-and-slow": "The psychologist who won the Nobel in "
                              "economics, on how judgement actually works",
}

SCENES = [
    ("I might be fooling myself", "Making a call", [
        ("Everything I find supports me. Should that worry me?",
         [("popper", "seek-refutation")]),
        ("I want this to be true, and I'm the one checking it.",
         [("feynman", "dont-fool-yourself")]),
        ("The numbers came out badly. Do I fix them or fix my view?",
         [("feynman", "dont-fool-yourself")]),
        ("What would have to happen for me to admit I was wrong?",
         [("popper", "falsifiability")]),
        ("I'm certain, and I can't say where the certainty came from.",
         [("thinking-fast-and-slow", "wysiati")]),
        ("Being right elsewhere has made me quick to be sure here.",
         [("socrates", "knowing-not-knowing")]),
    ]),
    ("Nothing I study stays", "How you're doing", [
        ("I do the same drill every day and nothing moves.",
         [("ericsson", "deliberate-practice")]),
        ("I keep adding hours. Should I be changing the method instead?",
         [("ericsson", "not-ten-thousand-hours")]),
        ("I can repeat it back and I couldn't rebuild it.",
         [("feynman", "teach-to-understand")]),
    ]),
    ("I don't know what to practice anymore", "AI arrived", [
        ("The hours go in. I can't tell whether any of it is practice.",
         [("ericsson", "deliberate-practice")]),
    ]),
    ("It still hasn't worked", "Nothing's moving", [
        ("Ten years of this. I'm not sure any of it counted.",
         [("ericsson", "not-ten-thousand-hours")]),
        ("I'm behind, so I keep putting more in.",
         [("thinking-fast-and-slow", "loss-aversion")]),
    ]),
    ("I don't have enough information", "Making a call", [
        ("It explains everything that happened. Why does that bother me?",
         [("popper", "falsifiability")]),
        ("I'm sure about this and it isn't my field.",
         [("socrates", "knowing-not-knowing")]),
    ]),
    ("I'm building something nobody asked for", "Getting it done", [
        ("Everyone still using it says they like it. Who am I not asking?",
         [("popper", "seek-refutation")]),
    ]),
    ("They'll find out I can't do this", "Things you don't say out loud", [
        ("I sound fluent in the meeting and I couldn't teach it.",
         [("feynman", "teach-to-understand")]),
    ]),
    ("The same mistakes keep happening", "Leading people", [
        ("I told him what was wrong. He fixed only that.",
         [("socrates", "midwifery")]),
    ]),
    ("The team has gone flat", "Leading people", [
        ("I hand out answers all day and nothing takes root.",
         [("socrates", "midwifery")]),
    ]),
    ("Do I trust my gut", "Dealing with people", [
        ("It all fits together. Is that evidence or is that a story?",
         [("thinking-fast-and-slow", "wysiati")]),
    ]),
    ("Do I change direction now", "Looking back, moving on", [
        ("Walking away costs me everything so far. Does staying cost nothing?",
         [("thinking-fast-and-slow", "loss-aversion")]),
    ]),
]

ASKS = {
    "ericsson/deliberate-practice":
        "I do the same drill every day and nothing moves.",
    "ericsson/not-ten-thousand-hours":
        "Ten years of this. I'm not sure any of it counted.",
    "feynman/dont-fool-yourself":
        "I want this to be true, and I'm the one checking it.",
    "feynman/teach-to-understand":
        "I sound fluent in the meeting and I couldn't teach it.",
    "popper/falsifiability":
        "What would have to happen for me to admit I was wrong?",
    "popper/seek-refutation":
        "Everything I find supports me. Should that worry me?",
    "socrates/knowing-not-knowing":
        "I'm sure about this and it isn't my field.",
    "socrates/midwifery":
        "I told him what was wrong. He fixed only that.",
    "thinking-fast-and-slow/wysiati":
        "I'm certain, and I can't say where the certainty came from.",
    "thinking-fast-and-slow/loss-aversion":
        "Walking away costs me everything so far. Does staying cost nothing?",
}

SC_BOX = {
    "I might be fooling myself":
        "Everything lines up neatly and the person who put it together was "
        "me. What is the honest way to check it?",
}

SC_SHORT = {
    "I might be fooling myself": "Fooling myself",
}

# -*- coding: utf-8 -*-
"""Reading people 第 6 批：论语、菜根谭、鬼谷子、马基雅维利、曾国藩。

英文站上这一类原来一条都没有，所以芯片条上通往它的路要靠这一批开。
新开三个处境（都在 Leading people / Dealing with people 两组之下），
其余十三章一律挂在已有处境上。
"""

ENTRIES = [
    {
        "c": "Reading people", "n": "The Analects", "slug": "analects",
        "e": "Spring and Autumn · 551–479 BC",
        "w": "The answer fits the asker", "y": -551,
        "d": "A record of a teacher answering particular students, compiled "
             "after his death. In English it usually arrives as loose maxims, "
             "which loses the thing that makes it usable: almost every line "
             "was said to one named person in one situation, and the same "
             "question gets different answers depending on who is asking. "
             "Later dynasties packaged it as a philosophy of obedience, which "
             "is close to the opposite of what he did — he resigned, he "
             "travelled for years looking for a ruler worth serving, and he "
             "criticised the ones he met. He was an unsuccessful politician "
             "and the most successful teacher in Chinese history.",
        "story":
            "At fifty-five he set out with his students to find a ruler who "
            "would use him, and for fourteen years none would. Between Chen "
            "and Cai the party was cut off and the provisions ran out; seven "
            "days with nothing to eat, and some of the students began to give "
            "way. Zilu came to him angry: does a gentleman also come to the "
            "end of his rope? He does, Confucius said. The gentleman holds "
            "when he is cornered; the small man, cornered, will do anything "
            "at all. He went home to Lu in the end and spent what was left of "
            "his life putting the old texts in order.",
        "f": [
            {"n": "Every answer has a name attached",
             "d": "He was asked what ren is more than a hundred times and "
                  "answered differently nearly every time, because the answer "
                  "was cut to the person asking. Read the answers with the "
                  "askers deleted and you get a bag of contradictions. Read "
                  "them with the askers restored and you get a method.",
             "eg": "The impulsive student is told to restrain himself and "
                   "return to form. The plodding one is told, simply, to love "
                   "people. Same question, different prescriptions."},
            {"n": "Say what you do not know",
             "d": "Knowing what you know and knowing what you do not know is "
                  "what he calls knowledge. He held to it himself: asked "
                  "something by a countryman, he said his mind went blank and "
                  "all he could do was work in from both extremes of the "
                  "question.",
             "eg": "Guessing at a number in a meeting costs nothing that "
                   "morning and costs three teams two weeks once they have "
                   "planned against it."},
            {"n": "Three layers for reading a person",
             "d": "See what he does, mark his motives, examine where he "
                  "rests. Behaviour can be staged for as long as somebody is "
                  "watching, the route he took to get here is expensive to "
                  "stage, and what he is comfortable with when nothing is at "
                  "stake can hardly be staged at all.",
             "eg": "Two people hit the same number. One spent next year's "
                   "budget to do it. The route, not the number, predicts the "
                   "next quarter."},
            {"n": "Harmony is not sameness",
             "d": "The gentleman harmonises without conforming; the small man "
                  "conforms without harmony. A room in complete agreement "
                  "about something complicated has usually not agreed. The "
                  "disagreement has moved outside the meeting, where nothing "
                  "can be done with it.",
             "eg": "No questions at the review, and then the problems arrive "
                   "one by one after launch — each of them seen by somebody "
                   "beforehand."},
            {"n": "One rule for a lifetime, and it is a prohibition",
             "d": "Asked for a single word to act on all one's life, he gave "
                  "reciprocity: what you do not want done to yourself, do not "
                  "do to others. The negative form is the point. It needs no "
                  "knowledge of the other person, only honesty about "
                  "yourself.",
             "eg": "Read the hard email once as if it had landed in your own "
                   "inbox before you send it."},
        ],
        "apply":
            "Pick the last decision you made that landed on somebody who had "
            "no vote in it, and run the one test: would you have accepted it "
            "if it had been done to you, in that manner, on that notice? "
            "Where the answer is no, the part that has to change is usually "
            "not the decision but how it was delivered.",
        "q": [
            "Knowing what you know and what you do not: that is knowledge.",
            "See what he does. Mark his motives. Examine where he rests.",
            "What you do not want done to yourself, do not do to others.",
            "The gentleman harmonises without conforming; the small man "
            "conforms without harmony.",
        ],
        "l": ["Wang Yangming", "Zeng Guofan", "Tao Te Ching", "Socrates",
              "Mencius"],
        "contrast": [
            {"n": "Tao Te Ching",
             "why": "The two main lines of Chinese thought: Confucius adds "
                    "— cultivate, practise, take part — where Laozi "
                    "subtracts. Neither is complete without the other"},
            {"n": "Socrates",
             "why": "Near contemporaries who both taught by asking rather "
                    "than telling, and both paid for holding a position "
                    "against the people in power"},
        ],
    },
    {
        "c": "Reading people", "n": "Tending the Roots of Wisdom",
        "slug": "caigentan", "e": "Ming · c. 1590s",
        "w": "A method of ease", "y": 1590,
        "d": "Three hundred-odd short entries by Hong Yingming, written in "
             "the Wanli years of the Ming, on how to live among other people. "
             "It reads at first like an aphorism collection about being "
             "gracious, and it is not: each entry names a self-interested "
             "reason. Leaving a step for someone on a narrow path is filed "
             "under a method of ease, not under virtue. Keeping your skill "
             "out of sight is called a place to hide in, not modesty. And the "
             "sourness you feel when someone near you does well is traced not "
             "to their gift but to your own empty square.",
        "story":
            "Almost nothing survives about Hong Yingming beyond a studio name "
            "and the decades he wrote in. What survives is the title, "
            "borrowed from a line by the Song scholar Wang Xinmin: a man who "
            "can chew through vegetable roots can do anything. Vegetable "
            "roots are what is left when there is nothing else — bitter, "
            "stringy, what the poor ate. The book never once promises that "
            "things will go your way. It assumes they will not, and then "
            "works on what is still yours: how much you show, how much you "
            "give up, and what you do with the ache when somebody else "
            "succeeds.",
        "f": [
            {"n": "Give way for your own sake, not theirs",
             "d": "Where the path is narrow, leave a step for others to pass. "
                  "Two people wedged against each other on a narrow path "
                  "means nobody passes. Whoever has to be first at everything "
                  "wins each occasion and loses the next, because the man "
                  "opposite braces on sight from then on.",
             "eg": "Enduring for somebody else's sake keeps a ledger and "
                   "presents the bill later. Giving way so you need not stay "
                   "braced is over when it is over."},
            {"n": "Three parts off, not the whole dish",
             "d": "The instruction is measured: a step, three parts. "
                  "Whoever hands everything over ends up living on the other "
                  "person's conscience, which is no steadier a position than "
                  "having to win every time. Seven parts stay with you, and "
                  "that is what makes it repeatable.",
             "eg": "Put a figure on the concession before you make it: how "
                   "much this time, and what is still mine afterwards."},
            {"n": "The fear of exposure is an arithmetic problem",
             "d": "Being afraid of being found out means more has been put on "
                  "display than is actually held. What wants treating is the "
                  "gap, not the fear: fill in what you have, or take back "
                  "part of what you showed. Both beat holding up a front that "
                  "must never be tested.",
             "eg": "Do not exhibit your single best performance as the normal "
                   "one. Expectations settle at whatever height you showed."},
            {"n": "Envy starts in your gap, not in their gift",
             "d": "Do not use your own strength to throw another's weakness "
                  "into relief; do not let your own clumsiness turn into "
                  "resentment of another's skill. Two clauses, one thing: "
                  "hurrying to look strong and being unable to bear good news "
                  "run off the same root.",
             "eg": "You can make someone smaller without a single hard word, "
                   "simply by steering every conversation back onto the "
                   "ground you are best on."},
        ],
        "apply":
            "Take the next concession you are about to make and put a number "
            "on it before you make it: is this three parts or all of it, and "
            "am I doing it for him or so that I can stop holding myself "
            "tight? The measured version is the one you will still be able to "
            "do in a year.",
        "q": [
            "Where the path is narrow, leave a step for others to pass.",
            "He calls it a method of ease, not a virtue.",
            "Hide skill in clumsiness; be bright by seeming dim.",
            "Not that he is too good, but that this square of yours is empty.",
        ],
        "l": ["Brené Brown", "The Art of Worldly Wisdom", "Feng Dao",
              "La Rochefoucauld", "Tao Te Ching"],
        "contrast": [
            {"n": "The Art of Worldly Wisdom",
             "why": "Two collections of maxims on showing and hiding, written "
                    "a generation apart at opposite ends of the world: "
                    "Gracián teaches how to be seen well, this one how not to "
                    "need to be seen"},
            {"n": "Brené Brown",
             "why": "Both work on the fear of being found out. Her answer is "
                    "to say it aloud so shame cannot survive being spoken; "
                    "his is to stop putting so much on display"},
        ],
    },
    {
        "c": "Reading people", "n": "Guiguzi", "slug": "guiguzi",
        "e": "Warring States · c. 400–320 BC",
        "w": "Open, close, sound out", "y": -400,
        "d": "The founding text of the Warring States persuaders, attributed "
             "to a recluse of Ghost Valley about whom nothing verifiable "
             "survives. It is the one Chinese classic that is a systematic "
             "handbook on moving a single specific person: not whether a "
             "thing ought to be said, only how speech should be opened, "
             "closed, tested and locked. Orthodox scholars called it a book "
             "for small men and had it suppressed repeatedly. It never "
             "disappeared, because anyone whose work depends on getting one "
             "other person to move ends up needing what is in it.",
        "story":
            "Tradition sends both Su Qin and Zhang Yi to the same teacher in "
            "Ghost Valley. Su Qin then sold the vertical alliance, six states "
            "banded against Qin; Zhang Yi sold the horizontal one, six states "
            "each cutting its own deal with Qin. One school, two men on "
            "exactly opposite sides, each carrying a chancellor's seal, "
            "fighting each other for half a lifetime. It is usually told "
            "against him, as proof that the school had no position. That is "
            "the point of the book. Vertical and horizontal are two faces of "
            "one technique, and which face gets used is decided by the "
            "situation. The silk manuscripts found at Mawangdui place Su Qin "
            "a generation after Zhang Yi, so the shared classroom is probably "
            "a later reconstruction; the story lasted anyway, because it "
            "names the thing accurately.",
        "f": [
            {"n": "Opening and closing are a pair of tools",
             "d": "To open is to speak, to close is to keep silent, and the "
                  "mouth is the door of the heart. Speech and silence are two "
                  "weapons rather than one default state. Most people's "
                  "problem is not that they cannot speak; it is that they "
                  "cannot stop.",
             "eg": "The most expensive sentence in a negotiation is usually "
                   "the one that breaks the silence after your own price."},
            {"n": "To hear him speak, be silent",
             "d": "Four reversals: to hear him, be silent; to have him open "
                  "out, draw in; to stand high, stand low; to take, first "
                  "give. Each of them is a sequence rather than a posture — "
                  "nothing is exchanged until something has been put down "
                  "first.",
             "eg": "Want their timeline? Give yours. Most people match it, "
                   "and it is information you cannot get by asking for it "
                   "directly."},
            {"n": "Weigh the hard facts, then sound out the wants",
             "d": "Two separate operations. Weighing is the countable side — "
                  "what he holds, where he stands, what his fallback is. "
                  "Sounding is the other one: what he actually wants and what "
                  "he is actually afraid of, read at the moments when he has "
                  "no attention left for editing.",
             "eg": "Diligence before terms and terms before diligence are two "
                   "different transactions. The second argues price over an "
                   "assumption nobody checked."},
            {"n": "Knowing begins with yourself",
             "d": "Know yourself and then you know others. Every judgement "
                  "you make about a person passes through your own "
                  "instrument, and an uncalibrated instrument adds the same "
                  "error to everything it measures. This is the precondition "
                  "the manipulation reading skips.",
             "eg": "If slow talkers always strike you as unreliable, that is "
                   "a fixed offset, not a talent for reading people."},
            {"n": "Hold the initiative rather than be held",
             "d": "The whole book lands here: it is better to control others "
                  "than to be controlled by them. Whoever defines the "
                  "question, sets the tempo and decides when it ends is "
                  "holding the exchange, whatever the stated agenda says.",
             "eg": "Look at last week. Did you write the calendar, or did "
                   "their moves write it for you?"},
        ],
        "apply":
            "Before the next conversation that matters, write down two lines "
            "instead of a script: what am I putting down first, and what does "
            "not have to be given at this stage. Then ask your question and "
            "count to five before saying anything else. The silence will "
            "return more than the follow-up would have.",
        "q": [
            "The mouth is the door of the heart.",
            "To hear him speak, be silent. To take, first give.",
            "Knowing begins with yourself; know yourself, then you know "
            "others.",
            "It is better to control others than to be controlled by them.",
        ],
        "l": ["Strategies of the Warring States", "Han Feizi", "Influence",
              "The Art of Worldly Wisdom", "Zhang Liang"],
        "contrast": [
            {"n": "Influence",
             "why": "The same set of human switches, approached from "
                    "opposite ends: Cialdini runs experiments and teaches you "
                    "to spot them being pulled, Guiguzi writes the operating "
                    "manual"},
            {"n": "The Analects",
             "why": "Confucius asks whether a thing should be said at all; "
                    "Guiguzi asks only how to say it so that it works. The "
                    "avowed and the suppressed halves of the same tradition"},
        ],
    },
    {
        "c": "Reading people", "n": "Machiavelli", "slug": "machiavelli",
        "e": "Florence · 1469–1527", "w": "What is done", "y": 1469,
        "d": "A Florentine diplomat, secretary of the republic's second "
             "chancery, and the author of The Prince. He was not teaching "
             "people to be "
             "wicked; he was the first to detach politics from moral "
             "instruction and study it on its own. The adjective made from "
             "his name now means unscrupulous, which flattens what he "
             "actually did: he wrote down how power behaves whether or not "
             "anyone approves, and he attached limits to it that the famous "
             "quotations leave out. His conclusions and Han Feizi's line up "
             "across seventeen hundred years, not because both men were "
             "sinister but because the mechanics repeat.",
        "story":
            "In 1512 the Medici returned to Florence, and the man who had run "
            "the republic's second chancery was arrested, put to the rope, "
            "and released into the countryside. He spent his days among "
            "farmers and "
            "card players. In the evening, he wrote to a friend, he took off "
            "the mud-caked working clothes, put on court dress, and entered "
            "the courts of the ancient men, where he was received kindly and "
            "was not ashamed to speak with them. That is where The Prince was "
            "written. He dedicated it to the new ruler hoping for a post and "
            "never received one. The man who understood power better than "
            "anyone then living could not obtain any of it for himself.",
        "f": [
            {"n": "Start from what is done, not what ought to be done",
             "d": "How one lives is so far distant from how one ought to "
                  "live, he writes, that a man who neglects the first for the "
                  "second learns his own ruin. That is a statement of subject "
                  "matter rather than a licence: the book is about how "
                  "politics runs, not how it should.",
             "eg": "An allowance everyone is trusted not to abuse gets used "
                   "to the last unit. Assume that, then set the number."},
            {"n": "Feared rather than loved, and never hated",
             "d": "If one has to be given up, being feared is safer than "
                  "being loved, because love runs on the other person's "
                  "willingness. Then the clause that rarely travels with the "
                  "quotation: avoid being hated, which means keeping off "
                  "their property and their family.",
             "eg": "Cutting a bonus is inside the rules. Humiliating someone "
                   "in front of the room, or withholding pay already agreed, "
                   "is over the line and buys an enemy."},
            {"n": "Half is fortune, and the other half has a deadline",
             "d": "Fortune is the arbiter of about half our actions and "
                  "leaves the rest to us. The river floods and carries "
                  "everything away, but in quiet weather men can raise dykes "
                  "and channels. The half you govern has to be finished "
                  "before the water rises.",
             "eg": "Cash buffer, second supplier, a backup for the person who "
                   "holds the system. All look like waste until the day they "
                   "are the only things working."},
            {"n": "Injury is remembered longer than benefit",
             "d": "Men forget the death of a father sooner than the loss of a "
                  "patrimony. Nine good turns and one injury leaves the "
                  "injury standing. Read as design guidance rather than "
                  "complaint, it says avoiding a memorable harm beats "
                  "manufacturing a memorable delight.",
             "eg": "The first rule of interface design is not to let people "
                   "make mistakes. One bad experience erases ten pleasant "
                   "ones."},
            {"n": "New arrangements have weak friends and strong enemies",
             "d": "Nothing is harder to take in hand than the introduction of "
                  "a new order, because those who would gain from it are "
                  "lukewarm and those who lose by it are committed. That "
                  "asymmetry, not stupidity, is why reforms stall.",
             "eg": "The people a change would help have no way to speak for "
                   "it. The people it costs have every resource needed to "
                   "push back, and they use them."},
        ],
        "apply":
            "Take one rule or incentive you are responsible for and re-read "
            "it as though everyone using it were maximising their own "
            "position with no goodwill at all. Whatever breaks under that "
            "reading was built on ought. Rewrite that part before it is "
            "tested for you.",
        "q": [
            "How one lives is so far distant from how one ought to live.",
            "It is far safer to be feared than loved, if you cannot be both.",
            "Men forget the death of a father sooner than the loss of a "
            "patrimony.",
            "Fortune is the arbiter of half our actions; she leaves us the "
            "rest.",
        ],
        "l": ["Han Feizi", "Liu Bang", "Cao Cao", "Sima Yi", "Sun Tzu"],
        "contrast": [
            {"n": "Han Feizi",
             "why": "The two closest political realists East and West, "
                    "seventeen centuries apart: both studied how power "
                    "actually works, and both were destroyed by the power "
                    "they studied"},
            {"n": "Socrates",
             "why": "Opposite poles of political philosophy: Socrates died "
                    "for a principle, Machiavelli spent his life on the "
                    "question of how to stay alive inside power"},
        ],
    },
    {
        "c": "Reading people", "n": "Zeng Guofan", "slug": "zeng-guofan",
        "e": "Qing · 1811–1872", "w": "Dull and unbreakable", "y": 1811,
        "d": "The most famous case in Chinese history of an ordinary man "
             "getting there by grinding. He was not gifted — he sat the "
             "examination seven times before passing — and he put down the "
             "Taiping Rebellion, the largest of the century, with a method he "
             "admitted was stupid: build a solid camp and fight a dull "
             "battle. He kept a diary auditing his own conduct for thirty "
             "years and circulated it to friends. He hired by handing people "
             "real work rather than by interviewing them. Nothing about his "
             "method requires talent, which is exactly why it is worth "
             "reading.",
        "story":
            "In 1854, at Jinggang, the river force of the militia he had been "
            "ordered to raise met the rebels and was broken. His boats were "
            "scattered and his men ran. He went over the side into the "
            "river and was pulled out by his own staff. He was a civil "
            "official with no military training, humiliated in front of the "
            "province, and what he did afterwards is the whole of him: he "
            "stopped looking for a battle he could win. From then on the army "
            "dug before it fought, and the war became a matter of trenches, "
            "supply and time.",
        "f": [
            {"n": "Solid camp, dull fight",
             "d": "On arriving anywhere the army camped before anything else "
                  "— trench, wall, stockade — and cities were encircled and "
                  "squeezed rather than stormed. It converted taking a city "
                  "from an event full of accidents into a question of time "
                  "and supply.",
             "eg": "Anqing was held under siege for over a year and Tianjing "
                   "for more than two. No single mistake could collapse "
                   "either operation."},
            {"n": "A method that does not need talent",
             "d": "The other side of a dull method is that it copies. Any "
                  "commander with any unit could follow it and reach a "
                  "passing grade, whereas a brilliant stroke depends on that "
                  "person on that day. An army raised from nothing could be "
                  "carried by it for that reason.",
             "eg": "A process worth eighty that anyone can run beats one star "
                   "worth a hundred. The first goes to thirty cities; the "
                   "second leaves when he does."},
            {"n": "Watchfulness when alone",
             "d": "Anybody keeps the rules while being watched. His answer to "
                  "the unwatched stretch was not willpower but record: write "
                  "the day down, wrong thoughts included, and the moment "
                  "acquires a witness. Then he handed the record to friends, "
                  "which is cheaper than resolve and works better.",
             "eg": "Expenses nobody audits, code nobody reviews, a report "
                   "nobody reads. Those three places describe a person more "
                   "accurately than any appraisal."},
            {"n": "Daily disciplines have to be checkable",
             "d": "I will become more disciplined cannot be executed. His "
                  "twelve were actions you can tick tonight: rise early, sit "
                  "in stillness, read one book at a time, keep the diary, "
                  "note what was said over tea. Small enough to answer did it "
                  "or did not.",
             "eg": "Read more this year cannot be settled in December. Ten "
                   "pages a day, three lines written after, settles itself "
                   "every night."},
            {"n": "Take in widely, employ carefully",
             "d": "A low bar at the door and a high one at the far end. He "
                  "kept a large staff and then judged people on a real piece "
                  "of work under real pressure — how they reported, and what "
                  "they did with the part they could not do.",
             "eg": "Li Hongzhang came up that way, from the staff to "
                   "independent command. Ask where this is not finished; the "
                   "clean answer is the one to promote."},
        ],
        "apply":
            "Turn the goal you keep losing in week three into something you "
            "can tick tonight, then post this week's version where somebody "
            "else will read it. The grain size and the audience are doing the "
            "work; resolve was never the variable.",
        "q": [
            "Watchfulness when alone brings peace of mind.",
            "Fight without haste: first make it stable, then look for change.",
            "Principle without officialdom, order in the head and few big "
            "words.",
            "Steady work that never breaks off beats a burst of courage.",
        ],
        "l": ["Wang Yangming", "Kazuo Inamori", "Ray Dalio", "Zhuge Liang",
              "The Analects"],
        "contrast": [
            {"n": "Marcus Aurelius",
             "why": "The closest pair East and West: both wrote themselves "
                    "down every day, and both used the writing to hold "
                    "themselves in check at the top of their own power"},
            {"n": "Wang Yangming",
             "why": "Doctrine and practice: Wang built the school of mind, "
                    "Zeng spent a lifetime executing it. Reaching the insight "
                    "against grinding it out daily"},
        ],
    },
]

INTROS = {
    "analects": "Twenty chapters of a teacher answering particular students, "
                "each answer cut to the student",
    "caigentan": "Three hundred Ming entries on living among people, by a man "
                 "we know almost nothing about",
    "guiguzi": "The one Chinese classic that is a handbook on moving a single "
               "specific person",
    "machiavelli": "A sacked Florentine official who wrote down how power "
                   "behaves rather than how it should",
    "zeng-guofan": "Beat the largest rebellion of his century by digging, and "
                   "audited himself in writing for thirty years",
}

SCENES = [
    # ── new: the three doors into Reading people ──
    ("It's my call and they don't get a say", "Leading people", [
        ("I'm about to decide something they have no say in.",
         [("analects", "reciprocity")]),
        ("Do I come down hard on this or let it go?",
         [("machiavelli", "feared-not-hated")]),
    ]),
    ("Nobody says what they actually think", "Leading people", [
        ("The room agreed with every word. That can't be right.",
         [("analects", "harmony-not-sameness")]),
        ("I ask them straight out and get nothing real back.",
         [("guiguzi", "listen-in-reverse")]),
    ]),
    ("I have one conversation to get right", "Dealing with people", [
        ("How much of my hand do I show in this meeting?",
         [("guiguzi", "open-and-close")]),
        ("What he tells me and what he wants are not the same.",
         [("guiguzi", "sound-out")]),
    ]),
    # ── hung off situations that already exist ──
    ("I don't have enough information", "Making a call", [
        ("I was asked and I gave an answer I don't actually have.",
         [("analects", "know-what-you-know")]),
    ]),
    ("Can I trust this person", "Dealing with people", [
        ("Three months of doing everything right. Is that enough to go on?",
         [("analects", "see-how")]),
        ("Everyone interviews well. How do I actually tell?",
         [("zeng-guofan", "recruit-and-test")]),
    ]),
    ("It turned into a fight", "Making a call", [
        ("Neither of us will give an inch and we both need to get past.",
         [("caigentan", "leave-a-step")]),
    ]),
    ("They'll find out I can't do this", "Things you don't say out loud", [
        ("I'm braced all the time in case somebody sees through me.",
         [("caigentan", "hide-the-edge")]),
    ]),
    ("I can't stand other people's good news", "Things you don't say out loud", [
        ("Someone close to me did well and I went cold inside.",
         [("caigentan", "dont-measure-by-yourself")]),
    ]),
    ("Someone is ahead of me", "How you're doing", [
        ("Why do I keep steering the talk back to what I'm good at?",
         [("caigentan", "dont-measure-by-yourself")]),
    ]),
    ("I'm managing it and it's getting worse", "Getting it done", [
        ("I wrote the rule assuming people would be reasonable.",
         [("machiavelli", "as-it-is")]),
    ]),
    ("Things are going well and it scares me", "Getting it done", [
        ("We had a great year. How much of it was the market?",
         [("machiavelli", "fortune-and-virtu")]),
    ]),
    ("A decision I can't undo", "Making a call", [
        ("I'm about to sign this while I'm still riding the high.",
         [("guiguzi", "sound-out")]),
    ]),
    ("They're setting the pace", "Facing an opponent", [
        ("They move faster and bet bigger. Do I have to match them?",
         [("zeng-guofan", "solid-camp-dull-fight")]),
    ]),
    ("I know better and still don't do it", "How you're doing", [
        ("Every goal I set is gone by the third week.",
         [("zeng-guofan", "self-watch")]),
    ]),
]

ASKS = {
    "analects/know-what-you-know":
        "I was asked and I gave an answer I don't actually have.",
    "analects/see-how":
        "Three months of doing everything right. Is that enough to go on?",
    "analects/reciprocity":
        "I'm about to decide something they have no say in.",
    "analects/harmony-not-sameness":
        "The room agreed with every word. That can't be right.",
    "caigentan/leave-a-step":
        "Neither of us will give an inch and we both need to get past.",
    "caigentan/hide-the-edge":
        "I'm braced all the time in case somebody sees through me.",
    "caigentan/dont-measure-by-yourself":
        "Someone close to me did well and I went cold inside.",
    "guiguzi/open-and-close":
        "How much of my hand do I show in this meeting?",
    "guiguzi/listen-in-reverse":
        "I ask them straight out and get nothing real back.",
    "guiguzi/sound-out":
        "What he tells me and what he wants are not the same.",
    "machiavelli/as-it-is":
        "I wrote the rule assuming people would be reasonable.",
    "machiavelli/feared-not-hated":
        "Do I come down hard on this or let it go?",
    "machiavelli/fortune-and-virtu":
        "We had a great year. How much of it was the market?",
    "zeng-guofan/solid-camp-dull-fight":
        "They move faster and bet bigger. Do I have to match them?",
    "zeng-guofan/self-watch":
        "Every goal I set is gone by the third week.",
    "zeng-guofan/recruit-and-test":
        "Everyone interviews well. How do I actually tell?",
}

SC_BOX = {
    "It's my call and they don't get a say":
        "The decision sits with me and the people it lands on were never "
        "asked. What do I owe them?",
    "Nobody says what they actually think":
        "Every meeting ends in agreement and I keep finding out later that "
        "nobody meant it. How do I get the truth into the room?",
    "I have one conversation to get right":
        "There is one meeting next week that settles it, and I have been "
        "rehearsing lines instead of deciding anything. Where do I start?",
}

SC_SHORT = {
    "It's my call and they don't get a say": "It's my call",
    "Nobody says what they actually think": "Nobody speaks up",
    "I have one conversation to get right": "One conversation",
}

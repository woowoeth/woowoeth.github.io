# -*- coding: utf-8 -*-
"""Strategy and competition, batch 4: Mao Zedong, Guo Jia, The I Ching,
Julius Caesar, Han Xin.

Five entries, fifteen chapters. Twelve of the chapters hang on situations that
already exist (eleven from scripts/hwx_scenes_en.py, one from b07); three open
new ones, because nothing covered arriving new and itching to act, everything
burning at once, or running a playbook borrowed from a much larger company.

On the Mao entry: only the method written between 1936 and 1949 is here. The
later political history is out of scope by decision, and none of the five
Chinese chapters needed it, so nothing had to be cut to keep that line.
"""

ENTRIES = [
    {
        "c": "Strategy and competition", "n": "Mao Zedong", "slug": "mao",
        "e": "Modern · 1893–1976", "w": "Concentrate", "y": 1893,
        "d": "Between 1936 and 1949 he wrote a set of essays that survive as "
             "method rather than as history: On Contradiction, On Practice, "
             "On Protracted War, and the strategy papers of the Red Army "
             "years. One habit runs through all of them. In a confused "
             "situation, find the single contradiction that governs the "
             "others, and put everything on it. The military writing turns "
             "that habit into operating orders: fight with the weapons you "
             "actually have, concentrate a superior force, finish one "
             "opponent before starting the next. What is collected here is "
             "that method, not the later career.",
        "story":
            "In 1947 the Nationalist offensive was aimed at Yan'an, and he "
            "chose to give the town up rather than hold it. The columns that "
            "took Yan'an spent the following year garrisoning ground, strung "
            "out and tied down, while the field army stayed mobile and "
            "destroyed them piece by piece. Within a year the situation in "
            "the northwest had turned over completely. A place had been "
            "traded for the force that could still move, which is the same "
            "arithmetic as keeping the main body alive instead of reporting "
            "a win for every position held.",
        "f": [
            {"n": "One principal contradiction per stage",
             "d": "Many contradictions exist at any moment and one of them "
                  "governs the rest. Solve that one and the others change "
                  "shape by themselves. The work is not effort, it is "
                  "identification, and then the harder half, which is putting "
                  "the rest down for this stage.",
             "eg": "Weak product, few users, thin channel and a loud "
                   "competitor were all shouting. Supply was the switch, and "
                   "the money went there until it turned."},
            {"n": "Concentrate a superior force",
             "d": "Better to sever one finger than to wound ten. Do not fight "
                  "several opponents at once; mass overwhelming strength at "
                  "one point, break it, and only then move to the next. "
                  "Spread evenly, it looks like fighting everywhere and "
                  "punches through nowhere.",
             "eg": "Five features shipped in a quarter and not one of them "
                   "gives anybody a reason to stay. One at full strength "
                   "beats five at a fifth."},
            {"n": "No investigation, no right to speak",
             "d": "Conclusions belong at the end of looking into something, "
                  "not at the beginning. A judgement that has not been struck "
                  "back at by events is a sentence nobody has paid for, and "
                  "the loop that makes knowledge is act, review, act again.",
             "eg": "Twenty books of method and no plan anyone can execute is "
                   "normal. Those were twenty circuits other people walked."},
            {"n": "The weaker side plays for time",
             "d": "Against someone stronger, a quick decision is their game. "
                  "The three stages are defensive, stalemate, "
                  "counter-offensive, and the middle one looks most like no "
                  "progress while it is doing the actual work of changing the "
                  "rules of the fight.",
             "eg": "Nine months of cash left: cut three lines to keep one "
                   "alive rather than starve four together, and stop "
                   "reporting a win for every position."},
        ],
        "apply":
            "Before the next quarter starts, get the team to answer one "
            "question out loud: what is the principal contradiction of this "
            "stage? Put the resources on that single thing, and name what is "
            "not being done because of it.",
        "q": [
            "No investigation, no right to speak.",
            "Concentrate a superior force and destroy the enemy one by one.",
            "Better to sever one finger than to wound all ten.",
            "Keep the people and lose the ground, and you keep both.",
        ],
        "l": ["Sun Tzu", "Liu Bang", "Han Xin"],
        "contrast": [
            {"n": "Napoleon",
             "why": "Both mass everything at one point, and then split: "
                    "Napoleon wants the whole thing decided in one quick "
                    "battle, and On Protracted War is built on refusing that "
                    "battle until the fist has formed"},
            {"n": "Jeff Bezos",
             "why": "Opposite readings of what to hold steady. Bezos says "
                    "bet on the need that will not change in ten years; this "
                    "says the governing problem is different in every stage "
                    "and yesterday's priority is how people die"},
        ],
    },
    {
        "c": "Strategy and competition", "n": "Guo Jia", "slug": "guo-jia",
        "e": "Three Kingdoms · 170–207", "w": "Count, don't cheer",
        "y": 170,
        "d": "Cao Cao's most trusted adviser, and the one he called his "
             "extraordinary aide. He arrived at twenty-seven and for the next "
             "eleven years stood behind almost every decision that mattered: "
             "the ten defeats and ten victories before Guandu, the argument "
             "for striking north at once, and the plan for Liaodong that he "
             "left behind when he died. What the three have in common is a "
             "refusal to work in impressions. Each replaces a feeling with "
             "something that can be checked, subtracted or waited out.",
        "story":
            "He went to Yuan Shao first. After one meeting he told his "
            "friends that Shao was full of schemes and short on essentials, "
            "fond of planning and unable to decide, and would never come to "
            "anything, and he left, at a time when Shao was the strongest man "
            "in the north and Cao Cao was not. He was introduced to Cao Cao, "
            "and they talked. This, he said afterwards, is truly my lord. He "
            "was twenty-seven. Eleven years later he was dead at thirty-eight, "
            "and after the defeat at Red Cliff Cao Cao said that had Guo Jia "
            "lived, he would never have come to this.",
        "f": [
            {"n": "Ten defeats and ten victories",
             "d": "Facing a stronger opponent, his method was not "
                  "encouragement but decomposition: turn who will win into "
                  "ten specific sub-questions and answer each. The value is "
                  "that a feeling becomes a judgement, and a judgement can be "
                  "argued with item by item.",
             "eg": "We cannot beat the incumbent is a mood. Cost structure, "
                   "delivery time, decision speed and channel depth, compared "
                   "one by one, usually show you are not weak everywhere."},
            {"n": "The window that closes",
             "d": "After Yuan Shao died and his son fled to the Wuhuan, "
                  "everyone advised securing the rear first. Guo Jia pressed "
                  "for an immediate march north: speed is the essence of war, "
                  "and a chance that exists briefly is gone once the other "
                  "side is settled in.",
             "eg": "The first two years of a new technology are the cheap "
                   "years, because nothing is fixed yet. Enter after the "
                   "positions harden and the price doubles."},
            {"n": "The last plan, and the patience in it",
             "d": "Dying, he left word not to attack Gongsun Kang but to wait "
                  "for him to send the heads himself. Press two wary parties "
                  "and they combine against you; ease off and the old account "
                  "between them reopens. Withdrawal here is a specific act, "
                  "not a surrender.",
             "eg": "Two departments stop fighting each other the moment you "
                   "intervene, and align their story against you instead. "
                   "Step out and the real conflict comes back."},
            {"n": "The person hardest to replace",
             "d": "What Cao Cao lost was not an executor. It was the one man "
                  "who could see the shape of a situation and say so to his "
                  "face. A team without anyone willing to say this one is "
                  "wrong loses decision quality steadily, and not because "
                  "anybody got stupider.",
             "eg": "Count the people in your last three meetings who "
                   "contradicted the most senior person present. If the count "
                   "is zero, that is the finding."},
        ],
        "apply":
            "Take the competitive judgement you are least sure of and stop "
            "arguing about it as a whole. Write five to ten named dimensions, "
            "score each one, and start with a page listing the three ways the "
            "other side genuinely beats you.",
        "q": [
            "Shao has ten defeats and you have ten victories.",
            "Speed is the essence of war.",
            "Press him and they combine; ease off and they plot against each "
            "other.",
            "Shao is full of schemes and short on essentials.",
        ],
        "l": ["Cao Cao", "Sun Tzu", "Han Feizi"],
        "contrast": [
            {"n": "Zhuge Liang",
             "why": "The two great advisers of the age divide on risk: Guo "
                    "Jia looks for the move nobody expects and takes the "
                    "narrow window, Zhuge Liang builds the position that "
                    "cannot be knocked over"},
            {"n": "Fan Li",
             "why": "Two ways a gifted adviser ends. Guo Jia burned out at "
                    "thirty-eight inside the work; Fan Li walked away on the "
                    "day it was won and lived a long time afterwards"},
        ],
    },
    {
        "c": "Strategy and competition", "n": "The I Ching", "slug": "i-ching",
        "e": "Zhou to Warring States · China",
        "w": "When to move, when to wait", "y": -800,
        "d": "Sixty-four hexagrams, six lines each, and underneath the "
             "divination they are all asking one question: given where you "
             "are standing, what should you do? The bottom line of the first "
             "hexagram says the hidden dragon does not act, and the top line "
             "of the same hexagram says the overreaching dragon repents. The "
             "eleventh hexagram is free passage and the twelfth is blockage, "
             "sitting next to each other in the order. The Great Commentary "
             "condenses the whole thing: at the limit it changes, changed it "
             "passes through, and passing through it lasts.",
        "story":
            "Sixty-four hexagrams at six lines each comes to three hundred "
            "and eighty-four short texts, and almost none of them says do "
            "this. They say, from where you are standing, do this. The same "
            "hexagram issues six different instructions depending on which "
            "line you occupy, and the two most famous lines of the first "
            "hexagram point in opposite directions. Read straight through, "
            "the book is one long argument that the right move is a function "
            "of position, and that no position lasts.",
        "f": [
            {"n": "Being able and being due are two different times",
             "d": "The bottom line and the fifth are both the dragon; what "
                  "differs is position, not power. Rushing to prove yourself "
                  "in a new place spends your own force and carries all of "
                  "the risk, and the same act two lines later is ordinary.",
             "eg": "New to a team, change nothing in the first month. Not "
                   "because it should not be changed, but because that is "
                   "when it costs the most to change."},
            {"n": "There is one line above the summit",
             "d": "Most people take the flying dragon for the end of the "
                  "hexagram. It is not. The trouble at a peak is not the "
                  "height but the adding that continues after you have "
                  "reached it, and what a long good run never trains is "
                  "retreat, loss and letting go.",
             "eg": "Someone who has only ever added is clumsy the first time "
                   "subtraction is the correct move."},
            {"n": "The hexagram after Peace is Standstill",
             "d": "The wall falls back into the moat is written into the top "
                  "line of Peace, not into Standstill. The turn begins at the "
                  "last position of the good stretch. Read the other "
                  "direction, being fully jammed is the condition under which "
                  "change finally becomes possible.",
             "eg": "The best year is the year to work out how this ends. "
                   "Equally, stop forcing a change while it still half works "
                   "and push when it genuinely seizes."},
        ],
        "apply":
            "Take the thing you are in the middle of and answer one question "
            "before any other: which line am I on. If it is the bottom one, "
            "spend the month gathering rather than proving. If it is near the "
            "top, name what you have never practised.",
        "q": [
            "The hidden dragon does not act.",
            "The overreaching dragon repents.",
            "At the limit it changes; changed it passes through, and so "
            "lasts.",
            "Now is not the normal state. It is one line of one hexagram.",
        ],
        "l": ["Sun Tzu", "Fan Li", "Zhuangzi"],
        "contrast": [
            {"n": "Tao Te Ching",
             "why": "Same observation, different resolution. Reversal is the "
                    "movement of the Way states the law in one sentence; the "
                    "I Ching cuts the same law into six positions and tells "
                    "you what to do in each of them"},
            {"n": "The Art of Worldly Wisdom",
             "why": "One says leave while your luck is still good, which is a "
                    "conclusion. The I Ching says there is one more position "
                    "above the good luck and it is called repentance, which "
                    "is a scale"},
        ],
    },
    {
        "c": "Strategy and competition", "n": "Julius Caesar", "slug": "caesar",
        "e": "Rome · 100–44 BC", "w": "The crossing", "y": -100,
        "d": "Rome's most famous general and its dictator, and the source of "
             "the line about the die being cast. He went from an aristocrat "
             "buried in debt to the conquest of Gaul, victory in the civil "
             "war and dictator for life, in about twenty years. Two of his "
             "decisions are worth more than the biography: the pause at the "
             "Rubicon, which was arithmetic rather than nerve, and the policy "
             "of pardoning defeated enemies, which he explained in a letter "
             "and which eventually helped kill him.",
        "story":
            "On the fifteenth of March, 44 BC he walked into the senate and "
            "was killed with twenty-three wounds. Among the men holding "
            "knives were Pompeians he had pardoned during the civil war and "
            "afterwards promoted, Brutus among them. He had waved away every "
            "warning that an attempt was coming, because he believed pardon "
            "bought loyalty. Suetonius reports that when he saw Brutus he "
            "spoke his last words in Greek: you too, my child? Everything he "
            "had built to defend himself faced outward, and nothing came from "
            "that direction.",
        "f": [
            {"n": "The pause is the decision",
             "d": "He halted at the Rubicon a long while and said out loud "
                  "that they could still turn back, but that past the little "
                  "bridge it would all be settled by arms. Reversible "
                  "decisions deserve speed; a decision that deletes the way "
                  "back deserves the night.",
             "eg": "Changing a tool is undone in a fortnight and needs no "
                   "committee. An exclusive contract or a public side taken "
                   "is worth a night at the bank."},
            {"n": "The sums were done before the sentence",
             "d": "Ten years in Gaul had made his legions the best in Rome, "
                  "Pompey's forces were scattered in Spain, and the city had "
                  "nothing to hold it with. He took Italy in sixty days and "
                  "almost without blood. The famous line is theatre placed on "
                  "top of a calculation.",
             "eg": "Before you commit in public, know your own core "
                   "capability, the gap in theirs, and the position you can "
                   "hold in the first month."},
            {"n": "Mercy as a policy, not a mood",
             "d": "At Corfinium he released every captured senator and "
                  "returned their property, and wrote to his staff that mercy "
                  "and generosity would be their new way of winning, in "
                  "explicit contrast to Sulla's terror. It worked because it "
                  "changed what the other side expected defeat to mean.",
             "eg": "When defeat means ruin, everyone fights to the end. When "
                   "it means going home, resistance stops being worth "
                   "paying for."},
            {"n": "The narrative was part of the campaign",
             "d": "He wrote the Gallic War while campaigning and told it in "
                  "the third person, so that the account reads as record "
                  "rather than boast while building the name Caesar at the "
                  "same time. Winning a war and owning the story of the war "
                  "are separate pieces of work.",
             "eg": "He did both. Most people who did the work do only the "
                   "first, and then wonder why somebody else is credited "
                   "with it."},
            {"n": "What outlived him was the design",
             "d": "His adopted son used the name to build an empire, and the "
                  "name itself became the word for emperor in languages he "
                  "never heard, Kaiser and Tsar among them. What lasts is "
                  "rarely the memorial; it is whether the thing you set up "
                  "runs without you.",
             "eg": "The test is unsentimental. Take yourself out for a "
                   "quarter and see which of the things you built are still "
                   "standing when you come back."},
        ],
        "apply":
            "Sort your open decisions into two piles, the ones you can walk "
            "back and the ones you cannot. Move fast on the first pile "
            "immediately, and give one of the second pile a full evening with "
            "the numbers before you say anything out loud.",
        "q": [
            "The die is cast.",
            "We can still turn back; beyond that bridge, arms decide "
            "everything.",
            "Let mercy and generosity be our new way of winning.",
            "I would rather be first in a village than second in Rome.",
        ],
        "l": ["Napoleon", "Liu Bang", "Huo Qubing"],
        "contrast": [
            {"n": "Xiang Yu",
             "why": "Both made the irreversible move famous, and only one of "
                    "them had done the sums first: Caesar crossed after a "
                    "long pause and a count, Xiang Yu sank the boats and "
                    "trusted the nerve"},
            {"n": "Machiavelli",
             "why": "Machiavelli says an injured enemy must be either "
                    "conciliated past all revenge or removed; Caesar pardoned "
                    "and promoted his, which won the war and produced the men "
                    "who killed him"},
        ],
    },
    {
        "c": "Strategy and competition", "n": "Han Xin", "slug": "han-xin",
        "e": "Han · 231–196 BC", "w": "The middle state", "y": -231,
        "d": "The most gifted commander in Chinese history, and the source of "
             "half the standard examples: the crawl between a bully's legs, "
             "the battle fought with a river at his back, the repaired plank "
             "road and the crossing at Chencang. His story has two halves "
             "that do not match. The rise is a military education in itself, "
             "and the fall is a single unforced error repeated for years: he "
             "would neither revolt nor hand over his power, and the middle "
             "position is the one that gets you killed.",
        "story":
            "Liu Bang once asked him how many troops the emperor himself "
            "could command. No more than a hundred thousand, said Han Xin. "
            "And you? For me, the more the better. Liu Bang laughed and asked "
            "why, in that case, he was the captive. Because your majesty "
            "cannot command troops but is very good at commanding commanders, "
            "he said, and that is heaven's gift rather than anything a man "
            "learns. It is the most honest thing he ever said, and read back "
            "from the end, the least careful.",
        "f": [
            {"n": "Dead ground, and its two conditions",
             "d": "Throw them onto dead ground and they will live is the "
                  "famous half. The half he added is that these were men "
                  "levied off the market who would have run from open ground, "
                  "and that two thousand horse were meanwhile changing every "
                  "flag in the enemy camp.",
             "eg": "A hard deadline can weld a team that has just formed. The "
                   "same move on people who could already fight destroys a "
                   "better rhythm."},
            {"n": "Repair the plank road, cross at Chencang",
             "d": "He made a show of rebuilding the burned mountain "
                  "walkways, which was slow, visible and exactly what the "
                  "other side expected, and took his main force out through "
                  "Chencang instead. Engage with the orthodox and win with "
                  "the unexpected, executed once and cleanly.",
             "eg": "The announcement everyone can see is usually not the "
                   "move. Ask what the same team is quietly doing in the same "
                   "week."},
            {"n": "Neither revolt nor hand over",
             "d": "His error was not failing to rebel. It was holding an army "
                  "that frightened his king while having no intention of "
                  "using it, for years. Threat is assessed on capability, "
                  "never on sincerity, and the middle carries both risks at "
                  "once.",
             "eg": "The only person who can run the one critical system is a "
                   "risk however loyal they are. The answer is a second "
                   "person, not a protestation."},
            {"n": "He reviewed every battle",
             "d": "He went from an unknown drifter to the best general of the "
                  "age in a very short time, and what he did after each "
                  "engagement was go back over it. The gap between an expert "
                  "and everyone else is not how few mistakes were made but "
                  "how much came out of them.",
             "eg": "After the next project ends, write the three real reasons "
                   "it went the way it did. Not the presentable reasons, the "
                   "actual ones."},
        ],
        "apply":
            "Find the one place where you hold something other people depend "
            "on and cannot replace. Then pick a side this month: either use "
            "that position for something, or deliberately make it "
            "replaceable. Do not stay in the middle for another quarter.",
        "q": [
            "Throw them onto dead ground and they will live.",
            "He whose valour overawes his lord stands in danger.",
            "The hares dead, the hounds are cooked; the birds gone, the bow "
            "stored.",
            "For me, the more the better.",
        ],
        "l": ["Liu Bang", "Sun Tzu", "Xiang Yu"],
        "contrast": [
            {"n": "Zhang Liang",
             "why": "The same court, the same victory, opposite endings: "
                    "Zhang Liang stepped all the way out and died old, Han "
                    "Xin kept the power and the loyalty both and lost "
                    "everything"},
            {"n": "Huo Qubing",
             "why": "Two kinds of military genius. Han Xin wins by "
                    "arrangement and misjudges his own position; Huo Qubing "
                    "wins by pure speed and never lives long enough for the "
                    "position to matter"},
        ],
    },
]

INTROS = {
    "mao": "Read here for the essays on method, 1936 to 1949, and nothing "
           "after them",
    "guo-jia": "Cao Cao's sharpest adviser, dead at thirty-eight, right "
               "almost every time",
    "i-ching": "Sixty-four hexagrams, six lines each, all asking one thing: "
               "where are you standing",
    "caesar": "Stood at a small river a long while before saying the die was "
              "cast",
    "han-xin": "The best general of his age, and the worst reader of his own "
               "position",
}

SCENES = [
    # ── merging into situations that already exist ──
    ("A decision I can't undo", "Making a call", [
        ("There is no undo on this one. How long should I stand at the edge?",
         [("caesar", "the-rubicon")]),
    ]),
    ("I keep not starting", "Making a call", [
        ("I'm still getting everything ready and the window is closing.",
         [("guo-jia", "leave-the-baggage")]),
    ]),
    ("They're setting the pace", "Facing an opponent", [
        ("They want it settled this quarter and I'm the weaker side.",
         [("mao", "on-protracted-war")]),
    ]),
    ("After the win", "Facing an opponent", [
        ("They're scattered. Do I finish them off or let them turn on each "
         "other?",
         [("guo-jia", "waiting-out-liaodong")]),
        ("I won, and what happens to them is up to me. What does mercy buy?",
         [("caesar", "clementia")]),
    ]),
    ("The team has gone flat", "Leading people", [
        ("Should I take away the escape route to make them move?",
         [("han-xin", "back-to-the-river")]),
    ]),
    ("Nothing ships", "Leading people", [
        ("We agreed in the room and everyone left doing their own version.",
         [("mao", "methods-of-work")]),
    ]),
    ("Should I step back", "When to step back", [
        ("I haven't committed and I haven't let go. Is the middle safe?",
         [("han-xin", "neither-nor")]),
    ]),
    ("Nothing I study stays", "How you're doing", [
        ("I've read the whole shelf and still can't run one of them myself.",
         [("mao", "on-practice")]),
    ]),
    ("Things are going well and it scares me", "Getting it done", [
        ("This is the highest I have ever been. Do I push for more?",
         [("i-ching", "arrogant-dragon")]),
    ]),
    ("It still hasn't worked", "Nothing's moving", [
        ("It is completely jammed. Is that the worst place or the turn?",
         [("i-ching", "peace-and-stagnation")]),
    ]),
    # b07 opened this one for Gandhi and Mandela. Same situation, so the
    # question goes in there rather than standing up a second chip in the
    # same group that means the same thing.
    ("I'm up against something much bigger", "Facing an opponent", [
        ("They beat us on every number and the team has stopped believing.",
         [("guo-jia", "ten-victories")]),
    ]),
    # ── new situations ──
    ("I'm new and want to prove myself", "Starting out", [
        ("Three weeks in and I want to change something. Too soon?",
         [("i-ching", "hidden-dragon")]),
    ]),
    ("Everything is urgent at once", "Getting it done", [
        ("Five things are on fire and I am spread across all five.",
         [("mao", "on-contradiction")]),
    ]),
    ("We copied someone else's playbook", "Getting it done", [
        ("We ran the playbook that worked for them and it is not working "
         "here.",
         [("mao", "strategy-of-the-revolution")]),
    ]),
]

ASKS = {
    "caesar/the-rubicon":
        "There is no undo on this one. How long should I stand at the edge?",
    "caesar/clementia":
        "I won, and what happens to them is up to me. What does mercy buy?",
    "guo-jia/ten-victories":
        "They beat us on every number and the team has stopped believing.",
    "guo-jia/leave-the-baggage":
        "I'm still getting everything ready and the window is closing.",
    "guo-jia/waiting-out-liaodong":
        "They're scattered. Do I finish them off or let them turn on each "
        "other?",
    "han-xin/back-to-the-river":
        "Should I take away the escape route to make them move?",
    "han-xin/neither-nor":
        "I haven't committed and I haven't let go. Is the middle safe?",
    "i-ching/hidden-dragon":
        "Three weeks in and I want to change something. Too soon?",
    "i-ching/arrogant-dragon":
        "This is the highest I have ever been. Do I push for more?",
    "i-ching/peace-and-stagnation":
        "It is completely jammed. Is that the worst place or the turn?",
    "mao/on-contradiction":
        "Five things are on fire and I am spread across all five.",
    "mao/on-practice":
        "I've read the whole shelf and still can't run one of them myself.",
    "mao/on-protracted-war":
        "They want it settled this quarter and I'm the weaker side.",
    "mao/strategy-of-the-revolution":
        "We ran the playbook that worked for them and it is not working here.",
    "mao/methods-of-work":
        "We agreed in the room and everyone left doing their own version.",
}

# Prefilled lines for the four new situations only. Each is the state the
# reader is in plus what they are afraid of plus where to start — deliberately
# not a restatement of the question on the card three centimetres away.
SC_BOX = {
    "I'm new and want to prove myself":
        "I can see four things here that are plainly broken and nobody has "
        "asked my opinion yet. Do I fix one now or sit on it?",
    "Everything is urgent at once":
        "Every item on the list looks like it cannot wait, and I finish none "
        "of them properly. Which one do I pick?",
    "We copied someone else's playbook":
        "The method came from a company ten times our size, and we have "
        "neither the people nor the money it quietly assumes. What do I keep?",
}

SC_SHORT = {
    "I'm new and want to prove myself": "New, want to prove it",
    "Everything is urgent at once": "All urgent at once",
    "We copied someone else's playbook": "Copied their playbook",
}

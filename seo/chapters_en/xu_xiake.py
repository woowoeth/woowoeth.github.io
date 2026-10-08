# -*- coding: utf-8 -*-
"""Xu Xiake — English.

English readers, if they know Xu Xiake at all, know him as the Ming traveller
who walked China for thirty years and kept a diary of rivers and caves. This
page is not about his geography. It takes two moments from the diary in which
the journey itself nearly ended: a night robbery on the Xiang river, and the
death of the monk who had set out with him.

Quoted lines are our own renderings of the Chinese in The Travel Diaries of
Xu Xiake (Chu, Guangxi and Yunnan diaries, 1637-1638), not lines taken from a
published translation.
"""

PARENT = {
    "name": "Xu Xiake",
    "slug": "xu-xiake",
    "blurb": "Deep read",
    "items": [
        {"k": "robbed-on-the-xiang", "n": "Robbed on the Xiang",
         "w": "When the trip falls apart halfway, ask whether you could ever leave again if you went home",
         "ready": True,
         "line": "Stripped of everything in one night, he borrowed money in Hengzhou instead of going home"},
        {"k": "jingwens-bones", "n": "Carrying Jingwen to Chicken Foot Mountain",
         "w": "When a companion falls on the road, finish the thing he wanted, his way",
         "ready": True,
         "line": "The monk who travelled with him died in Nanning, and he carried the bones for another year"},
        {"k": "the-crying-child", "n": "The Crying on the Bank",
         "w": "When something feels off, move first; guessing which trick it is can wait",
         "ready": True,
         "line": "He suspected a con and did nothing; the monk went ashore, and the robbers came"},
        {"k": "the-burned-books", "n": "The Burned Books",
         "w": "When something entrusted to you is destroyed, first say exactly what was lost",
         "ready": True,
         "line": "Letters he was carrying, a borrowed rarity, his own diaries: burned or taken in one night"},
        {"k": "the-night-we-waited", "n": "The Night They Waited",
         "w": "When you hold everyone up, the cost shows at once and the benefit only the next day",
         "ready": True,
         "line": "His boat was cursed for waiting for him; the next morning it passed two boats just robbed"},
        {"k": "step-by-step-in-snow", "n": "Every Step a Fright",
         "w": "When every step feels hollow, take them one at a time",
         "ready": True,
         "line": "In the snow on Mount Huang every step frightened him, and he still reached the valley"},
        {"k": "the-gazetteer-was-wrong", "n": "The Gazetteer Was Wrong",
         "w": "To say an authority is wrong, lay out what you walked, then name the step it got wrong",
         "ready": True,
         "line": "He walked the rivers one by one and wrote down exactly where the official gazetteer erred"},
        {"k": "jingwen-and-the-fire", "n": "Jingwen and the Fire",
         "w": "The thing you did for everyone becomes the reason they suspect you",
         "ready": True,
         "line": "He fought the robbers' fire and saved everyone's things, then was cursed as the one who let them in"},
        {"k": "beyond-the-guide", "n": "Past Where the Guide Would Go",
         "w": "Go in where others glance and leave, and decide beforehand where you will turn back",
         "ready": True,
         "line": "The guide showed him the famous rocks; he wrote that what he wanted to see was not there"},
    ],
}

CHAPTERS = [
    {
        "k": "robbed-on-the-xiang", "n": "Robbed on the Xiang",
        "w": "When the trip falls apart halfway, ask whether you could ever leave again if you went home",
        "src": "The Travel Diaries of Xu Xiake, Chu diary",
        "dek": "Halfway through, you lose your money and your things in one night, and everyone tells you to go home first. Why did Xu Xiake not go home?",
        "story":
            "In the spring of 1637 Xu Xiake, just past fifty, was sailing "
            "west up the Xiang river with a monk named Jingwen and a "
            "servant. One night robbers stormed the boat with torches and "
            "swords. He threw his money box into the river, jumped into "
            "waist-deep water and climbed naked onto a neighbouring boat. "
            "A fellow passenger died. Back in Hengzhou, a friend suggested "
            "going home to raise money and coming back. ==He reasoned that "
            "if he went home now, his family would never let him leave "
            "again.== He borrowed twenty taels, pledging his land rent, and "
            "set off west again.",
        "f": [
            {"n": "Ask whether you could leave again",
             "d": "His friend's plan was sensible: go home, raise money, return. Xu did not weigh what he had lost. He weighed what going home would do: his family, seeing him robbed, would never let him go. The loss was already gone either way.",
             "eg": "Your project loses half its budget and someone says pause until next year. Ask first: once paused, will anyone approve it next year?"},
            {"n": "Not turning back is not the same as not stopping",
             "d": "He did not walk on barefoot. He stayed in Hengzhou for three weeks in borrowed clothes, borrowed money against his land, and only then boarded a boat. Keeping the direction did not mean refusing to rest.",
             "eg": "Laid off but set on your own project? Take a stopgap job to cover rent first, rather than burning every bridge at once."},
            {"n": "Recover what can be recovered",
             "d": "At first light he waded back into the river to look for the box he had thrown overboard. The money was gone, but the rubbings and local histories the monk had saved were still dry. Count what is left before deciding.",
             "eg": "Your laptop dies with the draft unsaved. Before rewriting, search the cloud, your email and your chats for what survives."},
        ],
        "q": [
            "If I go home now, my family will never let me leave again.",
            "The money in the box is gone. The rubbings are still dry.",
        ],
        "apply":
            "Where you are: something went badly wrong halfway, money and "
            "plans are gone, and everyone says go home first.\n"
            "Ask first: if I go back, will I ever get out again? Is this "
            "loss telling me the direction is wrong, or only that this "
            "stretch was unlucky?\n"
            "Where it goes wrong: treating 'not turning back' as 'not "
            "stopping'. Xu stopped in Hengzhou, borrowed, re-clothed and "
            "waited. Charge on empty-handed, and the next setback really "
            "will end the trip.",
    },
    {
        "k": "jingwens-bones", "n": "Carrying Jingwen to Chicken Foot Mountain",
        "w": "When a companion falls on the road, finish the thing he wanted, his way",
        "src": "The Travel Diaries of Xu Xiake, Guangxi and Yunnan diaries",
        "dek": "Someone who set out with you falls halfway. Do you still go where he wanted to go? How Xu Xiake treated the wish of the monk Jingwen.",
        "story":
            "In the autumn of 1637 the monk Jingwen fell ill at a temple in "
            "Nanning. Xu had to move on, but Jingwen kept asking him for "
            "shoes and tea: he still meant to recover and reach Chicken "
            "Foot Mountain in Yunnan. Xu reasoned that to assume he would "
            "die, and plan to come back for his bones, was not what "
            "Jingwen wanted. ==So he left him the shoes and the tea, and "
            "said goodbye.== Jingwen died the next day. Xu drew lots before "
            "a Buddha on whether to carry the remains, drew 'take them', "
            "and carried them for a year to the mountain.",
        "f": [
            {"n": "Do not decide the ending for him",
             "d": "Jingwen was gravely ill and Xu had to go. Staying to wait was not what Jingwen wanted, and neither was quietly preparing to collect his bones. Xu did what Jingwen asked for: shoes and tea, so he could still think about the road.",
             "eg": "An ill parent still talks about one more trip. You need not say it will never happen. Buy the walking shoes first."},
            {"n": "See the cost before you say yes",
             "d": "Carrying a dead man's bones across three provinces meant trouble at every turn. He hesitated, asked about the obstacles, and only then decided. A promise made after counting the cost is one you can carry for a year.",
             "eg": "Before agreeing to finish a departed colleague's project, ask how much is left and how many weekends it will take."},
            {"n": "Do the version he wanted",
             "d": "He went to Chicken Foot Mountain, the place Jingwen had wanted, not any mountain on the way. He hung the bones among the old plum trees of the temple, agreed a burial site with the monks, and later climbed up to pay respects.",
             "eg": "Sorting a late father's things, follow what he said he wanted, not what you think looks most proper."},
        ],
        "q": [
            "To plan to come back for his bones was not his wish.",
            "The monk led me to where the bones lay. I bowed and wept.",
        ],
        "apply":
            "Where you are: someone who set out with you has fallen, and "
            "nobody will ever check whether you finished what he hoped "
            "for.\n"
            "Ask first: is this what he wanted, or what I think should be "
            "done? What will finishing it cost me, and do I accept that?\n"
            "Where it goes wrong: finishing it for your own peace of mind, "
            "in your own preferred version. Xu went to the mountain "
            "Jingwen wanted, not to a convenient one on the way.",
    },
    {
        "k": "the-crying-child", "n": "The Crying on the Bank",
        "w": "When something feels off, move first; guessing which trick it is can wait",
        "src": "The Travel Diaries of Xu Xiake, Chu diary",
        "dek": "Something feels wrong at night, and you guard against the wrong danger. What Xu Xiake suspected on the Xiang river, and what he missed.",
        "story":
            "On the night of 11 February 1637 the boat moored where no "
            "village stood. Crying came from the bank, like a child or a "
            "woman, for a long time. Every boat stayed silent. Xu lay awake, "
            "wrote a poem in pity, and suspected a con. Near midnight the "
            "monk Jingwen could not bear it, waded ashore and found a boy "
            "of fourteen who said he had fled a violent master. Jingwen "
            "urged him home and gave him something. ==Soon after Jingwen "
            "came back aboard, robbers stormed the boat.==",
        "f": [
            {"n": "Noticing is not the same as guarding",
             "d": "He suspected a confidence trick: someone using the child to extort whoever took him in. He never thought of robbers. Guarding against one bad outcome is not guarding against all. When something feels off, moving matters more than guessing the trick.",
             "eg": "A stranger calls at midnight saying your family is in trouble. Do not analyse it. Hang up and call them yourself."},
            {"n": "The place itself is the risk",
             "d": "There was no village on that bank, only two grain boats. He let the experienced travellers aboard choose where to moor. Handing the judgement to people who know the road also hands them your risk.",
             "eg": "A colleague books your hotel somewhere remote and you feel uneasy but say nothing. Ask the one extra question."},
            {"n": "Do not blame the soft-hearted one",
             "d": "Jingwen went ashore. The next day it was also Jingwen who guarded what was saved, dived for a pot and wet rice, and fed everyone before eating himself. Blame the kind one first, and next time nobody goes ashore.",
             "eg": "A colleague shipped goods in good faith and the client vanished. Do not name him in the group chat; work out together how to recover it."},
        ],
        "q": [
            "I worried only about a con, never that they were robbers.",
            "Every boat lay silent; nobody dared to ask.",
        ],
        "apply":
            "Where you are: something feels wrong, you cannot say what, "
            "and everyone around you is silent.\n"
            "Ask first: which bad outcome am I guarding against? If a "
            "different one comes, is where I am standing still safe?\n"
            "Where it goes wrong: stopping at the guess. Xu suspected a "
            "con and only wrote a poem. When something feels off, changing "
            "position matters more than naming the trick.",
    },
    {
        "k": "the-burned-books", "n": "The Burned Books",
        "w": "When something entrusted to you is destroyed, first say exactly what was lost",
        "src": "The Travel Diaries of Xu Xiake, Chu diary",
        "dek": "Something entrusted to you was destroyed on your watch. What Xu Xiake lost on the Xiang river, and how he dealt with it.",
        "story":
            "The night of the robbery, the thieves emptied his leather "
            "trunk: a preface and letters he was carrying from the writer "
            "Chen Meigong to the chief of Lijiang, dozens of letters, and a "
            "handwritten travel record by Zhang Zonglian that the family "
            "had treasured for two hundred years and he had begged to "
            "borrow. Ten volumes of his own collected travel writing burned "
            "with several gazetteers. Jingwen pleaded with the robbers, "
            "saved the sutras and gathered the scattered books. ==Xu wrote: "
            "it came into my hands and met this disaster; how can I not "
            "beat my chest?==",
        "f": [
            {"n": "Say exactly what was lost",
             "d": "In his diary he listed it item by item: whose draft, letters to whom, which book, where it came from. When you lose something of someone else's, first establish what it was and who it matters to, before you start blaming yourself.",
             "eg": "A client's samples broke in the courier. List which items, their value and whether they can be remade, then make the call."},
            {"n": "The hardest part is what is worthless to others",
             "d": "He said the letters bound for Lijiang were useless to the robbers and irreplaceable to him. Money can be repaid; this cannot. That is exactly the part to mention first.",
             "eg": "You lost a friend's hard drive. You can pay for the drive, not the photos. Talk about the photos first."},
            {"n": "If someone offers to chase it, let him",
             "d": "His friend Liu Mingyu swore before a shrine: the money is gone, but the book I will get back for you. Xu protested that it was lost, then let him try. Help is not only money; it is someone carrying the problem for a while.",
             "eg": "You lost the team's files and a colleague offers to search the backups. Do not refuse; give him every clue you remember."},
        ],
        "q": [
            "It came into my hands and met this disaster.",
            "Useless to them, and impossible for me to find again.",
            "The money cannot be recovered. The book I will recover for you.",
        ],
        "apply":
            "Where you are: something you were trusted to keep was "
            "destroyed in your hands. It was not your loss, and you cannot "
            "repay it.\n"
            "Ask first: what exactly was lost, and who does it matter to "
            "most? Which part can money cover, and which cannot?\n"
            "Where it goes wrong: drowning in guilt and never speaking. Xu "
            "wrote down every item. Delay out of shame, and the owner "
            "hears it from someone else.",
    },
    {
        "k": "the-night-we-waited", "n": "The Night They Waited",
        "w": "When you hold everyone up, the cost shows at once and the benefit only the next day",
        "src": "The Travel Diaries of Xu Xiake, Chu diary",
        "dek": "Because of you, everyone is a step behind and everyone blames you. What one night of waiting for Xu Xiake turned out to mean.",
        "story":
            "In the third month of 1637, back on the road after the "
            "robbery, Xu and Jingwen slogged a whole day through rain and "
            "mud to see off his friend Liu Mingyu, falling again and "
            "again, and reached his boat by fishing boat only late at "
            "night. The boat had waited for him, and its master was cursed "
            "by the other passengers for it. At dawn they passed two boats "
            "just robbed, one man killed and one dying. ==The people on the "
            "two boats travelling with them turned and thanked him: had we "
            "not waited for you, we would have been here.==",
        "f": [
            {"n": "The cost is immediate; the benefit comes later",
             "d": "The boatman who waited was cursed by everyone, and nobody could see any good in it. Only the two robbed boats the next morning showed what that night's delay had avoided.",
             "eg": "You insisted on one more night of testing and were blamed for the delay. The next day a rival's identical bug made the news."},
            {"n": "Whoever waited for you took the blame",
             "d": "The curses landed on the boatman, not on Xu. When your business slows everyone down, the person who covers for you usually takes the heat. Afterwards, say clearly that it was you.",
             "eg": "A colleague delayed a submission waiting for your figures and was called out. At the next meeting, say it was your doing."},
            {"n": "Thanks afterwards do not prove you were right",
             "d": "They escaped through that night's delay and through luck. Xu recorded only what happened, never that he had foreseen it. One delay turning out well does not make every delay right.",
             "eg": "Last time your extra day avoided a trap. Before asking everyone to wait again, say exactly what you are waiting for."},
        ],
        "q": [
            "Had we not waited for you, we would have met this too.",
            "The boatman, cursed for waiting, now looked rather pleased.",
        ],
        "apply":
            "Where you are: because of you everyone is a step behind, and "
            "right now they all blame you.\n"
            "Ask first: what does this delay avoid, and what does it cost? "
            "Who is taking the blame for me?\n"
            "Where it goes wrong: using a lucky escape to prove you were "
            "right. Had that night passed quietly, Xu would still have been "
            "the one who held everyone up.",
    },
    {
        "k": "step-by-step-in-snow", "n": "Every Step a Fright",
        "w": "When every step feels hollow, take them one at a time",
        "src": "The Travel Diaries of Xu Xiake, Mount Huang diary",
        "dek": "The road is long and every step feels hollow under your feet. How Xu Xiake came down through the snow on Mount Huang.",
        "story":
            "In the second month of 1616 Xu Xiake climbed Mount Huang. On "
            "the seventh day he went down from Jieyin Cliff through deep "
            "snow, peaks rising and falling around him as he passed. Each "
            "step showed something new, ==but the ravines were deep and the "
            "snow thick, and every step was a fright.== A dozen li further "
            "on, at Songgu Hermitage, a scent drifted along the stream: a "
            "plum tree in full flower. The mountain is cold, he wrote, the "
            "snow lingers, and only here does it bloom.",
        "f": [
            {"n": "Fear and wonder in the same step",
             "d": "He wrote that every step brought a new marvel, and that every step was a fright. Fear was not a signal to stop; it was often the same thing as seeing something new.",
             "eg": "Your first project on your own makes every decision nerve-racking. The nervous spots are usually where you learn fastest."},
            {"n": "Slow, but not stopped",
             "d": "On that frightening path he still walked a dozen li down to the hermitage. The way to walk it was one firm step at a time, not waiting until he was no longer afraid.",
             "eg": "After knee surgery you add two hundred steps a day. That slow still counts as forward."},
            {"n": "Write down the plum tree",
             "d": "On a day of cold sweat he still recorded the flowering plum. Record only the dangers and the road grows more frightening; record what is blooming too, and you know it was not all fear.",
             "eg": "In a hard week, write down one thing that went right each night, even if it was only lunch."},
        ],
        "q": [
            "The ravines deep, the snow thick: every step a fright.",
            "The mountain is cold, the snow lingers; only here does it bloom.",
        ],
        "apply":
            "Where you are: the road is long and you test every step. "
            "Tiredness does not scare you; empty ground under your foot "
            "does.\n"
            "Ask first: am I afraid of the road itself, or of walking it "
            "for the first time? Which step today can I plant firmly?\n"
            "Where it goes wrong: treating every-step-a-fright as a reason "
            "to stop. Xu was afraid and still reached the hermitage; wait "
            "until you are unafraid and you never see the plum tree.",
    },
    {
        "k": "the-gazetteer-was-wrong", "n": "The Gazetteer Was Wrong",
        "w": "To say an authority is wrong, lay out what you walked, then name the step it got wrong",
        "src": "The Travel Diaries of Xu Xiake, Guangxi diary, part 2",
        "dek": "Everyone has written it this way for years, and it is not what you walked. How Xu Xiake pointed out the error in an official gazetteer.",
        "story":
            "In the summer of 1637 Xu Xiake was travelling along the "
            "rivers of Guangxi, sorting out where each came from: the "
            "southern Pan river through Tianzhou to Hejiang west of "
            "Nanning, the northern Pan through Xincheng to Qingyuan. The "
            "official Yunnan gazetteer said the two Pan rivers ran apart "
            "for a thousand li and met at Hejiang. ==He wrote plainly that "
            "it had mistaken Nanning's left and right rivers for the two "
            "Pans==, and that neither river ran the way it claimed.",
        "f": [
            {"n": "First write down what you walked",
             "d": "He did not open by saying the gazetteer was wrong. He first wrote out where each river came from, where it passed and where it joined. Before saying an authority erred, lay out what you saw so others can check it.",
             "eg": "To say an industry report's figures are off, first list your own sample, dates and method."},
            {"n": "Name the step it got wrong",
             "d": "He did not say the gazetteer was nonsense; he said it had mistaken two rivers for the two Pans. Naming the exact step is far more credible than saying everything is wrong, and leaves room to correct it.",
             "eg": "Not 'this plan won't work,' but 'step three assumes a conversion rate twice our real one last year.'"},
            {"n": "The authority comes from having been there",
             "d": "He could write it because he had sailed and walked those rivers stretch by stretch. The standing to say an authority is wrong comes not from a confident tone but from having gone yourself.",
             "eg": "Veterans say this client will not renew. You spent two days at their office last week. Say what you saw."},
        ],
        "q": [
            "It mistook the left and right rivers for the two Pans.",
            "I took out the maps and gazetteers to find what Guilin offered.",
        ],
        "apply":
            "Where you are: everyone has said it for years, what you saw "
            "is different, and you fear sounding arrogant.\n"
            "Ask first: exactly which things did I see myself? At which "
            "step does it part from what the book says?\n"
            "Where it goes wrong: one discrepancy becomes a reason to "
            "distrust the whole book. Xu named one specific error, and in "
            "Guilin he still used the maps and gazetteers to plan his "
            "walks.",
    },
    {
        "k": "jingwen-and-the-fire", "n": "Jingwen and the Fire",
        "w": "The thing you did for everyone becomes the reason they suspect you",
        "src": "The Travel Diaries of Xu Xiake, Chu diary",
        "dek": "You took a risk for everyone and then found yourself suspected. What the monk Jingwen did on the night of the robbery, and what he was called for it.",
        "story":
            "On the night of the robbery Xu and the others jumped into the "
            "river. Jingwen stayed aboard and begged the robbers for his "
            "sutras, and they put them down. When they set the boat alight "
            "and left, he fought the fire, dived for water, and was stabbed "
            "twice by a robber who turned back. Using a fallen awning as a "
            "raft he made three trips, carrying everyone's clothes, books "
            "and rice to another boat. Then a fellow passenger claiming his "
            "things turned on him: ==everyone suspects you went ashore to "
            "bring the robbers==.",
        "f": [
            {"n": "Whoever steps up for everyone is suspected first",
             "d": "Jingwen was the one who went ashore to the crying boy, and the one who fought the fire. Everyone saw the first, so it became the reason to suspect him; the second happened in the dark.",
             "eg": "You volunteered to deal with the supplier that went wrong, and afterwards the first question is whether you caused it."},
            {"n": "Those who saw must say it",
             "d": "Xu wrote it down for him, item by item: he braved blades, cold, fire and water to guard the trunk for its owner, and was cursed instead of thanked. The wronged can rarely defend themselves; the witnesses have to speak.",
             "eg": "A colleague is blamed and you saw what happened. Say it in the meeting, not just in private sympathy."},
            {"n": "Feed everyone first",
             "d": "Next morning, with every pot burned, Jingwen dived for an iron pot and some wet rice, cooked porridge for everyone who had suffered, and ate last himself. Do the most urgent thing first; who was right can wait.",
             "eg": "The night the project blows up, order everyone dinner. Save the post-mortem for tomorrow."},
        ],
        "q": [
            "Everyone suspects you went ashore to bring the robbers.",
            "Even the robbers pitied the monk. This man was worse.",
        ],
        "apply":
            "Where you are: you took a risk for everyone, and now you are "
            "suspected of causing the trouble.\n"
            "Ask first: did anyone actually see what happened? Who can say "
            "it for me?\n"
            "Where it goes wrong: never stepping up again so as not to be "
            "suspected. Being wronged does not make the doer wrong; Xu "
            "wrote down everything Jingwen did, which is what a witness "
            "should do.",
    },
    {
        "k": "beyond-the-guide", "n": "Past Where the Guide Would Go",
        "w": "Go in where others glance and leave, and decide beforehand where you will turn back",
        "src": "The Travel Diaries of Xu Xiake, Guangxi diary, part 1",
        "dek": "Others glance and move on; you always want to go in. In the caves of Guilin Xu Xiake changed guides, went deep, and knew where to turn back.",
        "story":
            "On the second day of the fifth month of 1637 Xu Xiake entered "
            "the Seven Star Cave in Guilin. His guide hurried him past the "
            "famous named rocks, the vase, the chess game, the eight "
            "immortals. ==He wrote: what I wanted to see was not here.== "
            "Outside, he asked a man drawing water whether the stream "
            "could be followed inside, hired him on the spot, left his "
            "pack at a nearby temple with rice cooking for his return, and "
            "went back in. At a black pool the man refused: no one has "
            "ever gone further, and the water is high. Xu turned back.",
        "f": [
            {"n": "The named places may not be what you want",
             "d": "The guide showed the rocks with names that everyone looks at. Xu wanted to know where the cave went and what it led to. If you want to go in where others pass by, it is often because what you want is not on the list.",
             "eg": "Everyone copies the quotes from a bestseller; you want to trace where its key statistic came from."},
            {"n": "Find someone who has been deep",
             "d": "The first guide knew only the named rocks. Xu did not barge on alone; he asked a man who drew water there every day and hired him at once. To go deep, first find someone who has actually been deep.",
             "eg": "To understand an industry, skip the conference speakers and buy lunch for someone with ten years on the front line."},
            {"n": "Being thorough needs a turning point",
             "d": "At the black pool the new guide would go no further, and Xu turned back, noting that he had seen nearly everything both caves offered. Thoroughness is not recklessness; decide in advance where you will turn back.",
             "eg": "Digging into a technical problem in your spare time, decide now: no progress this weekend, and you set it aside."},
        ],
        "q": [
            "What I wanted to see was not here.",
            "No one has ever gone in, and the water is high.",
            "Of the two caves' wonders, almost nothing escaped me.",
        ],
        "apply":
            "Where you are: others glance and move on, you want to go all "
            "the way in, and you wonder whether being this thorough over "
            "something small is worth it.\n"
            "Ask first: is what I want simply not on the list? Who has "
            "actually been there? Where will I turn back?\n"
            "Where it goes wrong: thoroughness becomes recklessness. Xu "
            "wanted to go further, but when the guide said no one ever had "
            "and the water was high, he turned back, which is why he could "
            "go in again.",
    },
]

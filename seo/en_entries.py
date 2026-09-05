# -*- coding: utf-8 -*-
"""English entry records — the 30 in the first batch.

Same shape as the D[] array on the Chinese homepage (c/n/e/w/y/d/story/f/
apply/q/l/contrast), so the ordinary generators can build /en/i/<slug>/ from it.

Two rules this file follows that the Chinese one doesn't have to:

① **l and contrast may only name entries inside this batch.** The Chinese site
   has 159 entries and can cross-reference freely; /en/ has 30. A link to an
   entry with no English page sends the reader to a Chinese one.
   scripts/check_en.py fails the build on a ref outside the set.

② **条目记录里不写 == 强调。** 章节页会把 ==…== 渲染成红色着重，条目页不会
   —— geo_kit 那条渲染路径没有这一步，中文站的条目记录也从来不用它。
   带进来的后果是页面上出现两个字面的等号。scripts/check_en.py 会拦。

③ **The entry story must not be a chapter's story.** Several Chinese entries
   open with the same scene their first chapter opens with — Su Shi in the
   rain, Huineng's two verses, Fan Li's letter to Wen Zhong. That reads fine
   in Chinese because the reader arrives by name and the repetition is a
   refrain. Here the entry page is the introduction and the chapter is the
   argument, so the entry gets a scene the chapters don't use.
"""

ENTRIES = [
    {
        "c": "Strategy and competition", "n": "Sun Tzu", "slug": "sun-tzu",
        "e": "Spring and Autumn \u00b7 c. 500 BC", "w": "Win first, then fight",
        "y": -500,
        "d": "Thirteen short chapters, and the most quoted strategy book in "
             "the world. The argument underneath it is not about cunning: "
             "the winner has already secured the win before the fighting "
             "starts, and the loser starts fighting and then looks for a way "
             "to win. Almost every famous line is a consequence of that one.",
        "story":
            "The king of Wu wanted a demonstration, so he handed Sun Tzu the "
            "palace women to drill. Sun Tzu made the king's two favourite "
            "concubines the company commanders, explained the drill, and beat "
            "the drum. They laughed and did not move. If the orders are not "
            "clear, he said, that is the commander's fault \u2014 and "
            "explained again. They laughed again. If the orders are clear and "
            "still not followed, he said, that is the officers' fault, and he "
            "had both women executed. The king was appalled. The army that "
            "came out of it did not lose.",
        "f": [
            {"n": "Win first, then fight",
             "d": "The famous line is that the victorious army wins first and "
                  "seeks battle afterwards; the defeated army fights first "
                  "and looks for the win afterwards. It is a claim about "
                  "where the work happens \u2014 in the conditions, not in "
                  "the courage.",
             "eg": "The launch that went well had the pricing, the support "
                   "load and the two biggest customers settled before anyone "
                   "wrote a line of the announcement."},
            {"n": "The best fight is the one nobody has",
             "d": "Attacking the enemy's plan comes first, his alliances "
                  "second, his army third, and his walled cities last. Every "
                  "step down that list costs more and returns less. Winning "
                  "the fight is not the top of the ladder; not needing it is.",
             "eg": "The competitor didn't enter the category, not because "
                   "they lost a price war, but because the integration work "
                   "would have taken them two years to match."},
            {"n": "Know both, and know what you don't",
             "d": "Know the other side and yourself and you are never in "
                  "danger; know only yourself and you win half; know neither "
                  "and you lose every time. Most people read this as "
                  "reconnaissance. Half of it is about you.",
             "eg": "He had the competitor's roadmap and no honest number for "
                   "how long his own team actually takes. That is the half "
                   "that loses."},
        ],
        "apply":
            "Before the next thing you are about to launch, argue, or "
            "confront, write down what would have to be true for it to be "
            "already won. If none of it is true yet, you are not ready to "
            "start \u2014 you are ready to prepare.",
        "q": [
            "The victorious army wins first and seeks battle afterwards.",
            "Winning a hundred battles is not the height of skill. Subduing "
            "the enemy without fighting is.",
            "Know the other side and know yourself, and you will not be in "
            "danger in a hundred battles.",
        ],
        "l": ["Han Feizi", "John Boyd", "Fan Li"],
        "contrast": [
            {"n": "John Boyd",
             "why": "Both put the decision before the clash. Sun Tzu settles "
                    "it in preparation, Boyd in speed of turning"},
        ],
    },
    {
        "c": "How the world works", "n": "Tao Te Ching", "slug": "tao-te-ching",
        "e": "Spring and Autumn \u00b7 c. 500 BC", "w": "Subtract", "y": -500,
        "d": "Five thousand characters, and after the Bible the most "
             "translated book there is. Where most instruction is addition "
             "\u2014 learn more, do more, add another method \u2014 this one "
             "runs the other way. In learning you gain daily; in the way you "
             "lose daily, until there is nothing left to force, and then "
             "nothing is left undone.",
        "story":
            "Laozi rode west out of the pass on an ox, leaving a country he "
            "had given up on. The keeper of the pass stopped him and asked "
            "him to write something down before he went. He wrote five "
            "thousand characters and disappeared from the record. That is the "
            "whole biography, and the book is consistent with it: everything "
            "in it argues that the position of least insistence is the strong "
            "one.",
        "f": [
            {"n": "Reversal is how the way moves",
             "d": "Whatever reaches its extreme turns into its opposite. It "
                  "is not consolation for bad times; it is a reading "
                  "instrument. At the top, look for what is already turning. "
                  "At the bottom, the same rule is working for you.",
             "eg": "The quarter everything was going right is the quarter "
                   "nobody asked what would happen if the one channel "
                   "bringing all the customers stopped."},
            {"n": "Water beats stone by not arguing",
             "d": "The softest thing in the world runs through the hardest. "
                  "Not passivity \u2014 water keeps going and takes the shape "
                  "of whatever it meets. Persistence in a form that nothing "
                  "can push back on outlasts a harder push that has to be "
                  "sustained.",
             "eg": "Two years of quietly fixing the thing nobody owned moved "
                   "more than the reorg that was announced twice and "
                   "cancelled twice."},
            {"n": "The empty part is the useful part",
             "d": "The wheel is useful because of the hole at the centre, the "
                  "pot because of the space inside, the room because of the "
                  "gaps where the doors and windows are. What you build gets "
                  "the credit; what you left out is doing the work.",
             "eg": "The calendar with two empty afternoons is where the "
                   "thinking happened. The full one produced attendance."},
        ],
        "apply":
            "Take the thing you are trying to fix by adding \u2014 another "
            "tool, another rule, another meeting \u2014 and ask what you "
            "would remove instead. Try the subtraction first; it is cheaper "
            "and it is reversible.",
        "q": [
            "In learning you gain daily. In the way you lose daily.",
            "The softest thing in the world runs through the hardest.",
            "Knowing others is intelligence. Knowing yourself is clarity.",
        ],
        "l": ["Zhuangzi", "Huineng", "Su Shi"],
        "contrast": [
            {"n": "Zhuangzi",
             "why": "Same tradition, different address: Laozi writes for "
                    "whoever has to govern, Zhuangzi for whoever wants out"},
        ],
    },
    {
        "c": "Money and risk", "n": "Warren Buffett", "slug": "buffett",
        "e": "Contemporary \u00b7 1930\u2013", "w": "The moat", "y": 1930,
        "d": "Sixty years of compounding, and a method simple enough to say "
             "in a sentence: buy a business with a durable advantage at a "
             "sensible price and then do nothing for a very long time. His "
             "real edge is not stock-picking. It is that he can sit still "
             "while other people cannot.",
        "story":
            "In 1973\u201374 the American market fell by half. The Washington "
            "Post went from thirty-eight dollars to sixteen. Everyone was "
            "getting out; he was buying. He wrote to the management that he "
            "had bought, for ten million dollars, a piece of a company they "
            "themselves valued at four or five hundred million. The position "
            "eventually returned more than a hundred times. Nothing about the "
            "company had changed in those months. What had changed was what "
            "other people could stand to hold.",
        "f": [
    {"n": "Four kinds of moat",
             "d": "A brand people ask for by name, a network that gets more "
                  "valuable as it grows, a cost position nobody can match, "
                  "and a switching cost that makes leaving expensive. The "
                  "wider the moat, the less the future depends on being "
                  "clever.",
             "eg": "Nobody switches accounting software to save nine dollars "
                   "a month. That is a moat, and it was built by the tedium "
                   "of migration, not by the features."},
            {"n": "The edge of the circle matters more than its size",
             "d": "You do not need to understand every business, only the "
                  "ones you understand. He stayed out of technology for "
                  "decades and said so plainly. Knowing where your "
                  "competence stops is the part that protects you; the size "
                  "of the circle is vanity.",
             "eg": "He passed on the deal because he could not explain how "
                   "the company made money in one sentence. That is not "
                   "timidity; that is the boundary doing its job."},
            {"n": "The moat that matters is emotional",
             "d": "Be fearful when others are greedy and greedy when others "
                  "are fearful. In 1987, in 2000, in 2008 he was the one "
                  "buying into the collapse. The analysis was available to "
                  "everyone. The stomach was not.",
             "eg": "Everyone knew the rule about buying the dip. Almost "
                   "nobody transferred the money on the Monday the number "
                   "was red on every screen."},
        ],
        "apply":
            "Before the next purchase, write in one sentence why this thing "
            "will still be earning in ten years. If you cannot write the "
            "sentence, you are not buying a business; you are buying a price "
            "movement.",
        "q": [
            "Be fearful when others are greedy and greedy when others are "
            "fearful.",
            "Rule one: never lose money. Rule two: never forget rule one.",
            "You do not have to understand every company. Only the ones you "
            "own.",
        ],
        "l": ["Charlie Munger", "Li Ka-shing", "Fan Li"],
        "contrast": [
            {"n": "Charlie Munger",
             "why": "The partner who moved him from cheap and broken to good "
                    "and fairly priced"},
        ],
    },
    # ── Starting and building ──────────────────────────────────────
    # 这一类在英文站上原来是空的（中文有 19 条）。分类芯片是读者进站的一条
    # 主路，一整条路在英文这边不存在，比「条目少」严重。这六个人先把它开出来，
    # 而且他们彼此可以互相引用 —— 交叉链接不会指向没有英文页的人。
    #
    # 条目故事一律避开各自章节用过的场景（见文件顶部第 ③ 条）：
    # 乔布斯用 1985 年出局的十二年、马斯克用 2008 年那一年、
    # 格雷厄姆用 YC 的批量投法、纳瓦尔用《宝典》免费送出去这件事。
    {
        "c": "Starting and building", "n": "Steve Jobs", "slug": "jobs",
        "e": "Contemporary \u00b7 1955\u20132011", "w": "Subtract",
        "y": 1955,
        "d": "Co-founded Apple, was pushed out of it, spent twelve years at "
             "NeXT and Pixar, came back and turned a company weeks from "
             "insolvency into the most valuable one in the world. The centre "
             "of his thinking is that simple is harder than complex, that "
             "focus is a word for refusal, and that design is how a thing "
             "works rather than how it looks.",
        "story":
            "In 1985 he lost a board fight and left the company he had "
            "started. He has said the twelve years that followed were the "
            "most creative of his life, and the arithmetic supports him: NeXT "
            "built the operating system Apple eventually bought to save "
            "itself, and Pixar changed what an animated film was. Neither was "
            "a detour back to Apple. Both were the thing itself, done "
            "properly, by someone who no longer had a large company's "
            "permission to worry about.",
        "f": [
            {"n": "Simplicity is expensive",
             "d": "Making something simple is not removing features until it "
                  "is thin. It is understanding the thing well enough that "
                  "the shape becomes obvious. That takes longer than adding, "
                  "which is why most products are complicated: complication "
                  "is what you ship when you ran out of time to understand.",
             "eg": "The settings screen with forty switches is not generous. "
                   "It is a record of forty arguments nobody was willing to "
                   "settle."},
            {"n": "The product is every point of contact",
             "d": "He treated the box, the shop, the repair counter and the "
                  "advertising as parts of the product, because the customer "
                  "does not experience them separately. A company that is "
                  "excellent in the object and careless at the counter has "
                  "not made a good product; it has made a good component.",
             "eg": "Unboxing designed as a small ceremony does more for how "
                   "the thing feels than another processor generation."},
            {"n": "Belief is a resource, and it is borrowed",
             "d": "The famous distortion field was not a trick. People "
                  "delivered work they did not believe possible because "
                  "somebody credible refused to accept it was not. Used well "
                  "it raises what a group thinks it can attempt; used badly "
                  "it is a way of demanding miracles and blaming people for "
                  "the shortfall.",
             "eg": "The same sentence, this has to be twice as fast, is "
                   "either the best week a team ever had or the reason three "
                   "of them leave. The difference is whether the person "
                   "saying it is also in the room at two in the morning."},
        ],
        "apply":
            "List everything you are currently working on and ask which half "
            "you would keep if you could only keep half. Then stop the other "
            "half today, and write down who is accountable for having stopped "
            "it.",
        "q": [
            "Simple can be harder than complex; you have to work to get your "
            "thinking clean.",
            "Focus means saying no to the hundred other good ideas that there "
            "are.",
            "Design is not just how it looks. Design is how it works.",
        ],
        "l": ["Peter Thiel", "Jeff Bezos", "Paul Graham"],
        "contrast": [
            {"n": "Jeff Bezos",
             "why": "Cut to four products; the other man expanded into "
                    "everything and won too"},
        ],
    },
    {
        "c": "Starting and building", "n": "Elon Musk", "slug": "musk",
        "e": "Contemporary \u00b7 1971\u2013", "w": "First principles",
        "y": 1971,
        "d": "Co-founder of PayPal, Tesla, SpaceX and Neuralink. The method "
             "is a single move repeated: go back to what is physically true "
             "and re-derive everything from there. When told a thing is "
             "impossible, his first question is whether physics forbids it. "
             "If not, impossible is a description of current engineering and "
             "current prices, and both of those are temporary.",
        "story":
            "2008 was the year it nearly ended. The first three Falcon 1 "
            "launches failed, Tesla could not fund production of the "
            "Roadster, and the money was gone. The fourth Falcon flew in "
            "September and reached orbit; the Tesla financing closed on "
            "Christmas Eve. He has said that if the fourth launch had failed "
            "there was nothing left for a fifth. The interesting part is not "
            "the survival. It is that the same method produced three "
            "catastrophic failures and then the thing nobody else had done, "
            "and there was no way to tell those apart from inside.",
        "f": [
            {"n": "Physics is law; the rest is advice",
             "d": "The limit of any technology is set by physical law, not by "
                  "what the current industry can do. Working back from the "
                  "physical limit rather than forward from today's practice "
                  "changes what counts as an acceptable answer, and forces "
                  "engineering that the incremental route never reaches.",
             "eg": "Asking how much lighter this can be given the material "
                   "produces a different programme from asking how much "
                   "lighter than last year's."},
            {"n": "Most of the week should go into making the thing",
             "d": "He has said roughly eighty per cent of his time goes to "
                  "engineering and design. That is a budget, not a boast: "
                  "meetings without an output, reviews that only inform, and "
                  "reporting that changes no decision are the default state "
                  "of any organisation past a certain size, and they consume "
                  "exactly the hours the product needed.",
             "eg": "Cancel the standing meeting for a month and see what "
                   "actually breaks. Usually the answer is the feeling of "
                   "being informed."},
            {"n": "The method does not tell you when you are wrong",
             "d": "Reasoning up from fundamentals is equally confident when "
                  "the fundamentals are misjudged, and it removes the "
                  "handrail that convention provides. That is the real cost "
                  "of it: no external check, and a strong internal one. It "
                  "belongs on the few questions worth that exposure.",
             "eg": "The schedule derived from physics is right about what is "
                   "possible and famously wrong about when. Both come from "
                   "the same calculation."},
        ],
        "apply":
            "Next time something is described as impossible or as simply "
            "costing what it costs, ask what physical law or published price "
            "actually sets the floor. Everything between that floor and "
            "today's number is somebody's decision, and decisions can be "
            "remade.",
        "q": [
            "Physics is the law. Everything else is a recommendation.",
            "We reason from first principles rather than by analogy.",
            "Try to be useful. Do things that are useful to other people.",
        ],
        "l": ["Peter Thiel", "Jeff Bezos", "Charlie Munger"],
        "contrast": [
            {"n": "Charlie Munger",
             "why": "Reduce to physics, or carry many borrowed models at "
                    "once \u2014 two opposite cures for the same blindness"},
        ],
    },
    {
        "c": "Starting and building", "n": "Jeff Bezos", "slug": "bezos",
        "e": "United States \u00b7 1964\u2013", "w": "The flywheel",
        "y": 1964,
        "d": "Left a Wall Street job in 1994 to sell books out of a garage "
             "and built it into a two-trillion-dollar company across retail, "
             "cloud, logistics and hardware. He is the most extreme "
             "practitioner of the long term on record: twenty years of thin "
             "profit and open ridicule while every dollar went back into the "
             "flywheel, and then twenty years of winning.",
        "story":
            "In 1994 he was a vice-president at a New York hedge fund and "
            "wanted to leave and sell books online. His boss told him it was "
            "a good idea, but a better one for somebody who did not already "
            "have a good job. So he invented a way to decide: project "
            "yourself to eighty and look back — which choice would you "
            "regret? He knew at eighty he would not remember a bonus he gave "
            "up in 1994, and would mind very much never having been part of "
            "the internet at all. He resigned within days. What makes the "
            "frame sharp is that it changes the timescale of the question by "
            "force, and once the timescale moves the answer surfaces on its "
            "own.",
        "f": [
            {"n": "Regret minimisation",
             "d": "For decisions large enough to define a stretch of life, "
                  "shift the vantage point to eighty. Short-term losses — "
                  "salary, standing, safety — shrink automatically from "
                  "there, and the things that turn out to matter, whether you "
                  "tried, whether you were there, enlarge automatically. It "
                  "is built for the fork between safe and unremarkable and "
                  "risky and alive.",
             "eg": "The offer you keep re-reading at midnight is not a "
                   "spreadsheet problem. Run it from eighty and it usually "
                   "stops being close."},
            {"n": "The flywheel is slow before it is fast",
             "d": "Lower prices bring customers, customers bring traffic, "
                  "traffic brings sellers, scale lowers cost, and cost lowers "
                  "prices again. No first step and no last one. The part "
                  "people underestimate is the beginning, where it is heavy, "
                  "exhausting and appears to do nothing — which is where "
                  "almost everyone stops.",
             "eg": "Find the loop where each turn makes the next one easier, "
                   "then accept that the first two years will look "
                   "indistinguishable from failure."},
            {"n": "Your margin is my opportunity",
             "d": "Every comfortable high margin in an industry is a door "
                  "held open for an attacker. He compressed his own margins "
                  "deliberately to leave nothing worth attacking. Turn it "
                  "around as a self-check: whatever you are earning "
                  "comfortably from is precisely what somebody is currently "
                  "aiming at.",
             "eg": "The product line nobody wants to touch because it funds "
                   "everything else is the one a competitor is already "
                   "modelling."},
        ],
        "apply":
            "Sort your decisions by whether they can be undone: the "
            "reversible ones move fast and low, the irreversible ones get the "
            "meeting. Before starting anything new, write the press release "
            "you would publish on launch day — if you cannot make it exciting "
            "to a customer, do not start.",
        "q": [
            "Your margin is my opportunity.",
            "If you think three years out you have many competitors. Think "
            "seven and you have few.",
            "Failure and invention are inseparable twins.",
        ],
        "l": ["Warren Buffett", "Elon Musk", "Steve Jobs"],
        "contrast": [
            {"n": "Steve Jobs",
             "why": "One cut the range to four; the other refused to stop "
                    "adding \u2014 both were right about their own business"},
        ],
    },
    {
        "c": "Starting and building", "n": "Peter Thiel", "slug": "thiel",
        "e": "Contemporary \u00b7 1967\u2013", "w": "Zero to one",
        "y": 1967,
        "d": "Co-founded PayPal, was the first outside investor in Facebook, "
             "and is the most consequential contrarian in the Valley. His "
             "central claim: competition is an ideological trap, and what "
             "actually creates value is a monopoly rather than a fight.",
        "story":
            "In 2004 Facebook was a few months old and looked to most people "
            "like a social directory for Harvard undergraduates. He put in "
            "half a million dollars for a bit over ten per cent. By the 2012 "
            "listing that half million was worth around a billion. What he "
            "had seen was not that students liked it. It was that once a "
            "network of that shape closes, leaving costs the user everything "
            "and nothing else can be substituted for it \u2014 which is his "
            "definition of the only kind of business worth owning.",
        "f": [
            {"n": "Zero to one, not one to n",
             "d": "Going from one to n is copying: more of something that "
                  "exists, in a crowd, at thin margins. Going from zero to "
                  "one is making a category that was not there. Almost all "
                  "commerce is the first kind. The second is rare, and when "
                  "it works the value is not competed away because there is "
                  "nobody to compete with yet.",
             "eg": "A better version of an existing product is a fight over "
                   "an existing pool. A thing people had no word for last "
                   "year is not."},
            {"n": "The power law is not a slogan about focus",
             "d": "Venture returns are not normally distributed: a single "
                  "investment can return more than everything else combined. "
                  "The consequence is uncomfortable — spreading effort evenly "
                  "for the sake of balance guarantees you miss the only "
                  "outcome that mattered. Back the one you believe can be "
                  "that, with everything.",
             "eg": "The portfolio designed so nothing can go badly wrong is "
                   "also designed so nothing can go extraordinarily right."},
            {"n": "Definite optimism",
             "d": "He divides views of the future by two axes: optimistic or "
                  "pessimistic, definite or indefinite. His complaint about "
                  "the present is indefinite optimism — a belief things will "
                  "improve with no plan for how. Definite optimism is having "
                  "an actual picture of the thing you intend to build, which "
                  "is what makes long projects possible at all.",
             "eg": "We are excited about the space is indefinite. We are "
                   "building this specific thing and it will take six years "
                   "is definite, and only the second can be worked on today."},
        ],
        "apply":
            "Run the question on yourself: what important thing do you "
            "believe that most people disagree with? If you can give a real "
            "answer with evidence behind it, that is where your advantage "
            "probably is. If you cannot, your judgement is currently the "
            "room's average.",
        "q": [
            "Competition is for losers.",
            "The best businesses are the ones that do not compete.",
            "What important truth do very few people agree with you on?",
        ],
        "l": ["Steve Jobs", "Sun Tzu", "Warren Buffett"],
        "contrast": [
            {"n": "Paul Graham",
             "why": "One starts from the structure of the market, the other "
                    "from the hundred people in front of you"},
        ],
    },
    {
        "c": "Starting and building", "n": "Paul Graham", "slug": "paul-graham",
        "e": "United States \u00b7 1964\u2013",
        "w": "Do things that do not scale", "y": 1964,
        "d": "A Lisp hacker who built Viaweb in 1995 \u2014 the first "
             "commercial software that ran inside a browser \u2014 and sold "
             "it to Yahoo in 1998. In 2005 he started Y Combinator and "
             "rewrote what early-stage investment looked like. His real "
             "influence is in several hundred essays: most of what now passes "
             "for startup common sense has its earliest and clearest "
             "statement in one of them.",
        "story":
            "Y Combinator began as a summer experiment with a deliberately "
            "strange shape: fund a whole batch at once, give each of them a "
            "small amount of money and three months, and have dinner with "
            "them every week. Every part of it was the opposite of how "
            "investment worked \u2014 small cheques, no track record "
            "required, founders as young as they came, decisions in a "
            "ten-minute interview. The batch was the point. Founders learn "
            "more from the company two tables over, at the same stage and "
            "similarly frightened, than from anybody with an office.",
        "f": [
            {"n": "Make something people want",
             "d": "It is the only thing on the wall at YC. His judgement "
                  "after thousands of companies is that the fatal mistake is "
                  "singular: building something nobody actually wanted. "
                  "Everything else \u2014 the wrong hire, the wrong price, "
                  "the bad quarter \u2014 is repairable.",
             "eg": "A team can survive being outbuilt. It cannot survive "
                   "having been right about a need that was not there."},
            {"n": "Schlep blindness",
             "d": "The best openings often sit behind work that is tedious "
                  "and unglamorous — bank integrations, compliance, refunds. "
                  "The mind skips over those ideas so quickly that you never "
                  "notice having skipped. Which is exactly why they are still "
                  "available.",
             "eg": "Everybody saw the market. The reason nobody took it is "
                   "that the first nine months are paperwork."},
            {"n": "A maker's day is not divisible",
             "d": "Managers work in hours, makers need whole blocks. A single "
                  "meeting in the middle of an afternoon does not cost an "
                  "hour; it costs the afternoon, because neither remaining "
                  "piece is long enough to get into the work.",
             "eg": "Push every meeting to one end of the day. The output "
                   "change is larger than any productivity system."},
            {"n": "Better a few who love it",
             "d": "A hundred users who love the thing are worth more than ten "
                  "thousand who find it acceptable. The first group tells you "
                  "why, brings other people, and forgives the rough edges. "
                  "The second leaves quietly and teaches you nothing.",
             "eg": "Chasing a satisfaction score upward across everyone is "
                   "usually how a product becomes something nobody would "
                   "miss."},
        ],
        "apply":
            "In the cold-start phase do not build channels, buy traffic or "
            "automate. Find the first hundred users by hand and serve each "
            "one until they are happy; when that work is crushing you, that "
            "is the signal to scale. Test an idea on three questions: do I "
            "want it, can I build it, and why has nobody done it \u2014 no "
            "answer to the third usually means it is not worth doing, or you "
            "have not yet seen the tedium hiding in it.",
        "q": [
            "There is one fatal mistake: building something nobody wants.",
            "Do things that do not scale. It is the only route to scale.",
            "Better to have a few people love you than many find you "
            "acceptable.",
        ],
        "l": ["Peter Thiel", "Naval Ravikant", "Jeff Bezos", "Steve Jobs"],
        "contrast": [
            {"n": "Peter Thiel",
             "why": "Start from the users in front of you, or start from "
                    "whether the market can ever hold a profit"},
        ],
    },
    {
        "c": "Starting and building", "n": "Naval Ravikant", "slug": "naval",
        "e": "Contemporary \u00b7 1974\u2013", "w": "Leverage", "y": 1974,
        "d": "Co-founder of AngelList and an early investor in Twitter, Uber "
             "and Notion. In 2018 he posted a numbered thread called how to "
             "get rich without getting lucky, which has since been read "
             "millions of times. He is not a financial adviser. He is "
             "someone who worked out a route to personal sovereignty in a "
             "digital economy and then wrote the route down.",
        "story":
            "The thread was later compiled into a book by a reader, Eric "
            "Jorgenson, and released free \u2014 the whole text, downloadable, "
            "with Naval taking nothing from it. For a man whose entire "
            "subject is leverage, that is the argument made in the form of a "
            "decision rather than a sentence: a book that costs nothing "
            "travels further than one that earns, and reach compounds where "
            "royalties merely add. He gave away the thing most authors "
            "protect, because giving it away was the higher-leverage move.",
        "f": [
            {"n": "Four kinds of leverage, and two need permission",
             "d": "Labour means managing other people and requires "
                  "leadership. Capital means money making money and requires "
                  "having some. Code runs once written, at zero marginal "
                  "cost. Media is read once written, at zero marginal cost. "
                  "The first two need somebody's consent; the last two need "
                  "nobody's, and that is historically new.",
             "eg": "The essay published tonight and the fund raised next "
                   "spring carry the same idea. Only one of them can start "
                   "tonight."},
            {"n": "Wealth, money and status are three different games",
             "d": "Wealth is assets that work while you sleep and it is "
                  "positive sum. Money is the instrument for moving wealth "
                  "about. Status is your rank, and it is zero sum \u2014 for "
                  "you to rise somebody falls. How much time goes into each "
                  "decides which game you are actually in, whatever you say "
                  "you are doing.",
             "eg": "A year spent on titles and a year spent on something that "
                   "earns are indistinguishable while they are happening, and "
                   "very distinguishable afterwards."},
            {"n": "Happiness by subtraction",
             "d": "He argues happiness comes from removing desires rather "
                  "than satisfying them: every unmet want is a standing "
                  "source of unhappiness, so peace is not owning everything "
                  "but no longer being pulled by what you do not own. He "
                  "read a great deal of eastern philosophy and is "
                  "restating an old line in a modern setting.",
             "eg": "The list of things that would finally make it fine has "
                   "been rewritten four times, and each version was believed "
                   "completely at the time."},
        ],
        "apply":
            "Ask which part of your work could be written once and used many "
            "times \u2014 code, writing, a process, a framework, a tool. "
            "Identify those and move your hours towards them, because "
            "everything else is priced by the hour and stops when you do.",
        "q": [
            "Wealth is assets that earn while you sleep.",
            "If your income is measured in hours you will never truly be "
            "wealthy.",
            "Code and media are the permissionless leverage of this era.",
        ],
        "l": ["Peter Thiel", "Tao Te Ching", "Warren Buffett"],
        "contrast": [
            {"n": "Tao Te Ching",
             "why": "Both end at enough; one arrives through leverage, the "
                    "other by never picking the load up"},
        ],
    },
    {
        "c": "Learning and growth", "n": "Charlie Munger", "slug": "munger",
        "e": "Contemporary \u00b7 1924\u20132023", "w": "Invert", "y": 1924,
        "d": "Buffett's partner for more than half a century, and the reason "
             "Berkshire stopped buying cheap broken companies and started "
             "buying good ones at fair prices. His own contribution is a "
             "method rather than a portfolio: work out how a thing fails, "
             "then don't do that.",
        "story":
            "Invited to give a commencement address at Harvard Law, he told "
            "the graduating class he would explain how to guarantee a "
            "miserable life, and then listed the ways: unreliability, envy, "
            "resentment, learning only from your own experience, giving up "
            "after the first reverse. It is the method demonstrated on "
            "itself. If you knew where you were going to die, he liked to "
            "say, you would simply never go there.",
        "f": [
            {"n": "Invert, always invert",
             "d": "There are countless routes to a thing going well and only "
                  "a handful of ways it reliably goes wrong. Listing the "
                  "failure modes and avoiding them is a shorter, more "
                  "tractable problem than working out how to win.",
             "eg": "Nobody could say what would make the launch succeed. "
                   "Everyone could name the three things that would sink it, "
                   "and two were already true."},
            {"n": "One hammer is not enough",
             "d": "To a man with only a hammer everything looks like a nail. "
                  "He collected models from other fields \u2014 compounding "
                  "from mathematics, critical mass from physics, selection "
                  "from biology, the standard biases from psychology \u2014 "
                  "because a problem rarely arrives in the shape of your one "
                  "discipline.",
             "eg": "The retention problem was not a product problem. It was a "
                   "queueing problem, and nobody in the room had ever been "
                   "handed that model."},
            {"n": "Look at the incentive first",
             "d": "Show me the incentive and I will show you the outcome. To "
                  "understand why a system produces what it produces, do not "
                  "start with what people say they value; start with what "
                  "they are paid, promoted and forgiven for.",
             "eg": "The review process rewarded shipping. Nobody was ever "
                   "promoted for deleting a feature, so the surface grew "
                   "every year and nobody had decided that."},
        ],
        "apply":
            "Take the plan you are about to commit to and spend twenty "
            "minutes writing only the ways it fails. Then check how many are "
            "already true. That list is more useful than the plan.",
        # 条目页的金句不能和正文重复 —— 同页去重会把整块删掉（闸门抓到过
        # 一次）。「反过来想」「看激励」「一把锤子」三句都写在分则正文里了，
        # 这里换三句他确实说过、而这一页别处没有的。
        "q": [
            "It is remarkable how much long-term advantage we have got by "
            "trying to be consistently not stupid.",
            "Knowing what you don't know is more useful than being brilliant.",
            "Spend each day trying to be a little wiser than you were when "
            "you woke up.",
        ],
        "l": ["Warren Buffett", "Han Feizi", "John Boyd"],
        "contrast": [
            {"n": "Warren Buffett",
             "why": "Same desk for fifty years: Buffett holds the temperament, "
                    "Munger supplies the checklist of ways to be wrong"},
        ],
    },
    {
        "c": "Mind and feeling", "n": "Su Shi", "slug": "su-shi",
        "e": "Northern Song · 1037–1101", "w": "Unbowed", "y": 1037,
        "d": "One of the great Chinese poets, and also a calligrapher, a "
             "painter, a hydraulic engineer, a cook and a provincial "
             "governor. He was banished three times, each further than the "
             "last, and got steadily more open-hearted as it happened — not "
             "enduring the worst circumstances of his life but finding the "
             "best of himself inside them. Almost everything he is remembered "
             "for was written after his career ended.",
        "story":
            "It is worth knowing the range before the philosophy. The same "
            "man who wrote the most quoted lines in the language dredged the "
            "West Lake at Hangzhou and built a causeway across it that still "
            "carries his name; set up what may be China's first public "
            "clinic; campaigned to stop infant drowning in Huangzhou; lived "
            "on the city wall during a flood at Xuzhou saying that while he "
            "was there the water would not take the city; and left recipes. "
            "None of that is decoration on the poetry. It is the same "
            "disposition doing different work.",
        "f": [
            {"n": "The openness has a structure",
             "d": "It wasn't a temperament he was born with. His writing "
                  "records the sequence: the blow lands, there is a long "
                  "stretch of real pain, attention turns inward, the present "
                  "moment turns out to be full, and only then the release. "
                  "He didn't skip to serenity. He walked through the middle.",
             "eg": "Two people laid off the same week. One posts about the fresh start on day three and is still hollow in month six; the other is wretched for a month, then starts."},
            {"n": "The constraint produced the work",
             "d": "His three years in Huangzhou produced the two Red Cliff "
                  "rhapsodies and his best-known lyrics. Having lost the "
                  "ability to change anything outside himself, he was left "
                  "with what he could still do — and that turned out to be "
                  "the most concentrated output of his life.",
             "eg": "The book got written the year the funding fell through, because there was nothing left to run and the writing was the only thing still in his hands."},
            {"n": "He lost the politics and won everything else",
             "d": "He opposed the reformers' new laws, then opposed the "
                  "conservatives when they abolished all of them. He held to "
                  "the measure rather than the side, and both sides exiled "
                  "him for it. In the political record he is a failure. A "
                  "thousand years later he is the one people quote.",
             "eg": "The one who wouldn't sign either faction's memo got passed over twice, and is the person both sides quote when they explain what went wrong."},
        ],
        "apply":
            "Next time you're overruled, shelved, or watching something fail, "
            "try treating the stretch that follows as an enforced turn "
            "inward. The best thinking and the best work often happen in the "
            "period when there is nothing to administer.",
        "q": [
            "A bamboo stick and straw sandals beat a horse. Who's afraid?",
            "Looking back at that bleak road — no wind, no rain, no sun.",
            "Where the heart is at rest, that is my home.",
        ],
        "l": ["Wang Yangming", "Fan Li", "Zhuangzi"],
        "contrast": [
            {"n": "Zhuangzi",
             "why": "Two ways of not being owned: Zhuangzi refuses the post, "
                    "Su Shi takes it and refuses to be defined by losing it"},
            {"n": "C.S. Lewis",
             "why": "Both wrote through the worst of it. Lewis to find out "
                    "what he actually believed, Su Shi to find out what was "
                    "still enjoyable"},
        ],
    },
    {
        "c": "Mind and feeling", "n": "Wang Yangming", "slug": "wang-yangming",
        "e": "Ming · 1472–1529", "w": "Knowing is doing", "y": 1472,
        "d": "A philosopher who was also the most effective general of his "
             "generation — an almost unheard-of combination. His central "
             "claim is that the principle you are looking for is not out in "
             "the things of the world but in the mind that meets them, and "
             "that anyone who says they know something and doesn't act on it "
             "has not yet understood it. He is the origin of most of what "
             "later East Asia means by practical philosophy.",
        "story":
            "In 1506 he offended a powerful eunuch, was beaten in open court "
            "and exiled to Longchang in Guizhou — a malarial posting on the "
            "edge of the empire where he had to build his own shelter and "
            "grow his own food. The officials sent there mostly died. He had "
            "a stone coffin made and slept beside it, on the reasoning that "
            "the only thing he had not yet let go of was the fear of dying. "
            "One night he woke shouting. The way of the sage is complete "
            "within my own nature — he had spent twenty years looking "
            "outside for something that was not out there.",
        "f": [
            {"n": "The mind is the principle",
             "d": "The meaning and value of a thing arrive with the mind that "
                  "meets it. Practically, this moves the standard: your "
                  "judgement doesn't come from an external authority that has "
                  "to be consulted before you may act.",
             "eg": "You already know the deck is dishonest. Waiting for someone senior to say it first is not caution; it is looking for a person to hold the judgement for you."},
            {"n": "Knowing and doing are one",
             "d": "'I know I should get up early' from someone who never does "
                  "is not knowledge, it's an idea about knowledge. Real "
                  "knowing shows up in the body. This is the sentence he is "
                  "most quoted for and the one most often quoted without "
                  "being applied.",
             "eg": "'I know I should exercise' from someone who hasn't in a year is not knowledge. The knowing showed up in the ones who went twice this week."},
            {"n": "The hardest campaign is interior",
             "d": "He never lost a battle, and wrote from the field that "
                  "breaking the bandits in the hills is easy and breaking the "
                  "ones in the heart is hard. What actually stops people is "
                  "fear, laziness, vanity and self-deception — none of which "
                  "appears on any plan.",
             "eg": "The plan was never the problem. Sending the email that admits the number was wrong is the whole difficulty, and no amount of planning touches it."},
        ],
        "apply":
            "When a team knows what to do and doesn't do it, the problem is "
            "usually not execution. Either they don't actually believe it "
            "matters, or the incentives point elsewhere. Fix what they "
            "believe before you talk about delivery.",
        "q": [
            "Breaking the bandits in the hills is easy. The ones inside "
            "aren't.",
            "When this mind does not move, you can move with the moment.",
            "Without a settled aim, nothing in the world gets finished.",
        ],
        "l": ["Huineng", "Su Shi", "Zhuangzi"],
        "contrast": [
            {"n": "Huineng",
             "why": "The same insight in two traditions: Huineng says what "
                    "you seek is already complete in you, Wang Yangming says "
                    "so and then goes and governs a province with it"},
        ],
    },
    {
        "c": "Mind and feeling", "n": "Zhuangzi", "slug": "zhuangzi",
        "e": "Warring States · c. 369–286 BC", "w": "Free and equal", "y": -369,
        "d": "The second peak of Daoism, and a very different writer from "
             "Laozi. Where Laozi addresses the person who has to govern, "
             "Zhuangzi addresses the individual who wants out. He held one "
             "minor post and never took another, was poor enough to borrow "
             "rice, and turned down the premiership of a large state. His "
             "thirty-three chapters use parables to make one point: how to "
             "get your interior life back when reputation, argument and gain "
             "have tied it up.",
        "story":
            "He was fishing on the Pu river when two officials arrived from "
            "the king of Chu to offer him the government of the state. He "
            "didn't put the rod down. I hear, he said, that Chu keeps a "
            "sacred tortoise, dead three thousand years, wrapped in cloth and "
            "housed in the ancestral temple. Would that tortoise rather be "
            "dead and venerated, or alive and dragging its tail in the mud? "
            "Alive in the mud, they said. Then go away, said Zhuangzi. "
            "I intend to drag my tail in the mud. He refused the trade "
            "itself, not the job. Most of the strategists competing for those "
            "posts died in the resulting purges. He lived past eighty.",
        "f": [
            {"n": "The use of the useless",
             "d": "The tree too crooked to be timber is the one that reaches "
                  "a thousand years. Things with no immediate use — a hobby "
                  "that earns nothing, reading with no purpose, experience "
                  "that won't fit a CV — are often what still holds when "
                  "everything scheduled has been spent.",
             "eg": "The reading that earned nothing for six years is what made you the only person in the room who saw the second-order effect."},
            {"n": "Cut along the grain",
             "d": "His cook's blade lasts nineteen years because it never "
                  "meets bone, only the gaps between joints. Effort that "
                  "meets resistance everywhere is usually not short of force. "
                  "It is in the wrong place.",
             "eg": "The rewrite that ate three weekends went in on a Tuesday evening, once he stopped fighting the framework and used the hook it already had."},
            {"n": "Whose standard is this",
             "d": "There is a right and wrong on that side and one on this "
                  "side. What looks like stupidity from where you stand is "
                  "generally coherent from where they stand. Holding several "
                  "positions at once isn't fence-sitting; it's the thing that "
                  "shrinks your blind spot.",
             "eg": "The team that moves too slowly is optimising for the outage you have never had. From where they sit, your speed is the reckless part."},
        ],
        "apply":
            "In an environment where everyone is competing, the scarcest "
            "capacity is the ability not to enter. Before joining the race "
            "everyone else is running, ask whose right and wrong you are "
            "using. Keep a third of your time for things with no use — over a "
            "long enough horizon that is usually the best-performing "
            "position you hold.",
        "q": [
            "Everyone knows the use of the useful. Nobody knows the use of "
            "the useless.",
            "A frog in a well can't discuss the sea. It is bound by its "
            "hole.",
            "The friendship of the wise is bland as water.",
        ],
        "l": ["Su Shi", "Huineng", "Wang Yangming"],
        "contrast": [
            {"n": "Han Feizi",
             "why": "The same century, opposite conclusions: Han Feizi builds "
                    "the machine of state, Zhuangzi declines to be a part in "
                    "it"},
        ],
    },
    {
        "c": "Mind and feeling", "n": "Huineng", "slug": "huineng",
        "e": "Tang · 638–713", "w": "Already complete", "y": 638,
        "d": "An illiterate woodcutter from the far south who became the "
             "sixth patriarch of Chan Buddhism. The record of his teaching is "
             "the only native Chinese text ever called a sutra. What he did "
             "was an extreme piece of subtraction: he took the practice out "
             "of the commentaries, the graded stages and the monastery, and "
             "reduced it to one sentence — the thing you are looking for is "
             "already in you, and the problem is that you keep looking "
             "outward.",
        "story":
            "Years after receiving the transmission he was still living "
            "unrecognised among a band of hunters. Arriving at last at a "
            "monastery, he found two monks arguing about a banner moving in "
            "the wind — one saying the wind moved, the other saying the "
            "banner moved. Neither the wind nor the banner is moving, he "
            "said. Your minds are moving. The abbot, hearing it, understood "
            "who had just walked in. The remark is not a riddle. It is his "
            "whole method in one line: before adjusting the object, check "
            "the thing doing the looking.",
        "f": [
            {"n": "Sudden doesn't mean fast",
             "d": "Gradual practice assumes distance from the goal and so "
                  "requires accumulation. Sudden awakening says the distance "
                  "was never there — only a misrecognition. So 'sudden' isn't "
                  "speed. It is the discovery that there is nowhere to "
                  "travel.",
             "eg": "Nothing new arrived the day she stopped apologising for the price. She had the same evidence in January; what changed was that she stopped waiting to deserve it."},
            {"n": "No-thought is not blankness",
             "d": "It means a thought arises, you see it, and you neither "
                  "follow it nor suppress it. This is the part of the text "
                  "closest to something modern and operable — it describes "
                  "keeping distance from a feeling rather than eliminating "
                  "it.",
             "eg": "The urge to check the message is there either way. Watching it pass without opening the app is the practice; suppressing it is just a second urge."},
            {"n": "Everything outward rests on 'I am not enough'",
             "d": "Books, teachers, the next achievement: every outward "
                  "search is built on a premise nobody examines. He puts the "
                  "premise itself in question, which is why this is the only "
                  "subtraction in a library otherwise made of addition.",
             "eg": "Another course, another certificate, one more year of preparation. Each purchase quietly restates the premise that you are not ready yet."},
        ],
        "apply":
            "Almost all modern self-improvement is addition — one more book, "
            "one more course, one more streak — and the unstated premise is "
            "always that who you are now is insufficient. Next time something "
            "grips you, do one thing only: notice the thought, say 'there it "
            "is', and neither follow it nor scold yourself for having it. "
            "Most of the pain is in the long derivation that follows, not in "
            "the thought.",
        "q": [
            "There was never a thing there, so where would dust settle?",
            "Not the wind moving, not the flag moving. Your mind is moving.",
            "The teaching is in the world. Awakening is not apart from it.",
        ],
        "l": ["Wang Yangming", "Zhuangzi", "Su Shi"],
        "contrast": [
            {"n": "Wang Yangming",
             "why": "Huineng is upstream: 'the nature is already complete' "
                    "and 'innate knowing' are one idea in two vocabularies"},
        ],
    },
    {
        "c": "Money and risk", "n": "Fan Li", "slug": "fan-li",
        "e": "Spring and Autumn · 536–448 BC", "w": "When to go", "y": -536,
        "d": "The most successful exit in Chinese history. He spent more than "
             "twenty years helping the king of Yue climb from hostage to "
             "hegemon, and walked away on the day it was finished — changed "
             "his name, moved three times, and built a great fortune three "
             "times over, giving it away on each occasion. He is remembered "
             "both as a strategist and as the patron figure of Chinese "
             "commerce.",
        "story":
            "The part usually skipped is the twenty years before the exit. "
            "Yue had been crushed; its king was a servant in the enemy "
            "capital. Fan Li went with him and stayed through the whole of "
            "it, and the plan he ran was measured in decades, not seasons — "
            "grow the population, stock the granaries, keep the enemy "
            "complacent, and do not move early. The man famous for leaving "
            "at the right moment had first spent twenty years not leaving. "
            "Knowing when to go is not restlessness. It is the same faculty "
            "that knows when to stay.",
        "f": [
            {"n": "Read the person, not the situation",
             "d": "His judgement about the king wasn't 'this is dangerous "
                  "now' but 'here is what this man becomes when things go "
                  "well' — true long before it mattered. Situations change; "
                  "the construction of a person doesn't.",
             "eg": "He was generous when the round closed and vicious when it didn't. That wasn't the market changing him; it was one man under two conditions."},
            {"n": "Buy what nobody wants",
             "d": "In drought, stock boats; in flood, stock carts. The entire "
                  "difficulty of the rule is that at the moment of buying, "
                  "every visible piece of evidence says the thing is "
                  "worthless.",
             "eg": "The hard part is not spotting the empty office block. It is signing the lease in the month every person you respect tells you the sector is finished."},
            {"n": "Letting go is harder than accumulating",
             "d": "Three fortunes made and three given away, a "
                  "chancellorship returned. Many people can accumulate. "
                  "Almost nobody puts down a position already in hand and "
                  "starts again.",
             "eg": "Plenty of people can build the team to forty. Almost nobody hands it over while it is still going well and starts again at one."},
        ],
        "apply":
            "At every stage of a career, ask periodically: is this "
            "relationship, or this job, still in the phase where I gain from "
            "it, or has it hit its ceiling and started accumulating risk? The "
            "second phase looks exactly like the first from inside.",
        "q": [
            "The birds are gone, so the good bow is put away.",
            "You can share hardship with him. You cannot share ease.",
            "In drought, stock boats. In flood, stock carts.",
        ],
        "l": ["Li Ka-shing", "Su Shi"],
        "contrast": [
            {"n": "Li Ka-shing",
             "why": "Two and a half millennia apart, the same two rules: buy "
                    "when nobody wants it, and leave before the top"},
        ],
    },
    {
        "c": "Money and risk", "n": "Li Ka-shing", "slug": "li-ka-shing",
        "e": "Contemporary · 1928–", "w": "Cycles", "y": 1928,
        "d": "From a plastic flower workshop to a group spanning property, "
             "ports, telecoms, retail and energy. What is worth studying is "
             "not the scale but the survival: the 1967 riots, the 1997 Asian "
             "crisis and the 2008 crash all passed through Hong Kong without "
             "damaging him, on two rules he states plainly — buy "
             "counter-cyclically, and never run out of cash.",
        "story":
            "In 1967 Hong Kong was in the middle of riots. Bombs were being "
            "left in the streets, British firms were pulling out, and "
            "property prices collapsed. Everyone was selling. He was "
            "buying. Three years later the city had stabilised and his "
            "holdings were worth several times what he paid. The move looks "
            "like nerve and is mostly arithmetic: he had done the work of "
            "imagining how it could go wrong, and he had the cash to be wrong "
            "for a while.",
        "f": [
            {"n": "Counter-cyclical, in both directions",
             "d": "Buy in the trough, take money off the table at the peak. "
                  "Land in the 1967 riots; a steady withdrawal from mainland "
                  "property from the 2010s, roughly a decade before the "
                  "consensus. Each time, acting before others noticed the "
                  "turn.",
             "eg": "Hiring in the quarter everyone else froze feels like a mistake for eighteen months, which is exactly how long it has to feel wrong to still be cheap."},
            {"n": "Never take the last coin",
             "d": "He exits before his own estimate of the top, giving up the "
                  "final ten or twenty per cent in exchange for certainty. "
                  "Wanting the last coin means selling only once everyone "
                  "agrees the top has passed.",
             "eg": "You sold at eight and it went to ten. The twenty per cent you left behind is what bought you never having to guess where the top was."},
            {"n": "Cash is oxygen",
             "d": "Large reserves at all times, accepting lower returns to "
                  "keep liquidity. In 2008 several large groups ran out of "
                  "funding. He didn't. Low gearing isn't caution — it buys "
                  "more chances to be wrong.",
             "eg": "Six months of runway isn't caution. It is the number of times you get to be wrong before being wrong is fatal."},
        ],
        "apply":
            "Once a year, run a cash stress test: if your main income stopped "
            "for six months, how long would your reserves last? If the answer "
            "is under six months, start building the reserve now rather than "
            "after the answer matters.",
        "q": [
            "Never forget stability while growing; never forget growth while "
            "stable.",
            "Ninety per cent of my time, I spend considering failure.",
            "The first barrel must be solid before you add the second.",
        ],
        "l": ["Fan Li"],
        "contrast": [
            {"n": "Fan Li",
             "why": "Both left before the top. Fan Li left the whole game; "
                    "Li Ka-shing left one position and stayed in"},
        ],
    },
    {
        "c": "Power and organisation", "n": "Han Feizi", "slug": "han-feizi",
        "e": "Warring States · 280–233 BC", "w": "Law, method, position", "y": -280,
        "d": "The systematiser of Chinese Legalism, who combined law, "
             "administrative method and positional authority into one theory "
             "of power. He is the most clear-eyed realist in the tradition — "
             "he never argues about how things ought to be, only about how "
             "they work — and his writing gave the first emperor the "
             "framework for unifying China.",
        "story":
            "He had a stammer and could not argue in person, so he wrote. His "
            "essays reached the king of Qin, who read them and said that if "
            "he could meet this man he would die content, then invaded Han to "
            "get him. At the Qin court Han Fei was undone by a fellow student "
            "from his own teacher's school, Li Si, who was jealous of him and "
            "spoke against him; he was imprisoned and forced to take poison. "
            "The man who wrote the definitive analysis of persuasion and "
            "court intrigue was killed by a piece of court intrigue. "
            "Knowing and being able to do it are not the same faculty.",
        "f": [
            {"n": "Law, method and position together",
             "d": "Law is the written rule everyone is held to; method is how "
                  "you assess and check the people below you; position is the "
                  "authority the seat itself carries. Missing the first, the "
                  "rules get bypassed. Missing the second, you get compliance "
                  "in form only. Missing the third, nobody listens.",
             "eg": "The policy exists, nobody checks it, and the person enforcing it has no standing to say no. Any one of the three missing and the other two stop working."},
            {"n": "People follow interest, not exhortation",
             "d": "He doesn't believe in natural loyalty; he believes in "
                  "incentives. Design the system well and people behave the "
                  "way you wanted. It is Munger's 'show me the incentive and "
                  "I'll show you the outcome', stated twenty-two centuries "
                  "earlier.",
             "eg": "The all-hands asked everyone to prioritise quality. Bonuses stayed tied to shipped count. Everyone shipped."},
            {"n": "The difficulty of persuasion",
             "d": "The hard part of speaking, he wrote, is not what you know "
                  "but working out what the listener actually cares about. He "
                  "catalogued the fatal errors — exposing what they don't "
                  "want exposed, speaking at the wrong moment, being too "
                  "direct — and then died of one.",
             "eg": "Your deck answered whether it could be built. The one person who could approve it was worried about who gets blamed if it fails."},
        ],
        "apply":
            "When designing incentives for a team, ask what this system will "
            "make people do, not what it ought to make them do. People act on "
            "interest. Aligning what you want with what pays is the whole of "
            "the job.",
        "q": [
            "The ruler controls by two handles: punishment and favour.",
            "The difficulty of persuasion is knowing the listener's mind.",
            "A thousand-mile dyke collapses from an ant hole.",
        ],
        "l": ["Fan Li"],
        "contrast": [
            {"n": "Zhuangzi",
             "why": "Same era, opposite answers: Han Feizi designs the "
                    "machine, Zhuangzi declines to be a component"},
            {"n": "Thomas Gordon",
             "why": "Two theories of getting compliance: rules and "
                    "consequences, or naming the effect on you. Both work, on "
                    "different things"},
        ],
    },
    {
        "c": "Learning and growth", "n": "Pu Songling", "slug": "pu-songling",
        "e": "1640–1715 · Shandong", "w": "The side thing won", "y": 1679,
        "d": "At nineteen he came first in three examinations and was locally "
             "famous. Then he sat the provincial examination for forty years "
             "and never passed, supporting his family as a live-in tutor. "
             "Almost everyone else in this library eventually succeeded — "
             "even their defeats are defeats on the way somewhere. He is the "
             "exception. The work he considered his life's business never "
             "came off, and the thing he did on the side became one of the "
             "most-read books in the language.",
        "story":
            "At seventy-one he was finally granted a minor honorary status — "
            "not passed, but awarded by seniority to a candidate who had "
            "simply been at it long enough. It was the only official "
            "recognition of his life and it arrived when it could change "
            "nothing. By then he had been writing his 'idle book' for four "
            "decades: nearly five hundred stories, revised repeatedly, "
            "circulated in manuscript among friends. He died before it was "
            "printed, and never knew.",
        "f": [
            {"n": "Failure with no turning point",
             "d": "There was no decisive year — not one big defeat and a "
                  "restart, but once every three years, just short, until he "
                  "was old. Most advice about failure assumes a turning point "
                  "to point at. Here there isn't one, and none of it "
                  "applies.",
             "eg": "Not one bad year: eleven rounds of interviews across four years, each ending at the final stage, with nothing to point at as the moment it went wrong."},
            {"n": "He never let it be the only thing",
             "d": "He didn't stop sitting the exam and he didn't stake his "
                  "life on it. The tutoring continued, the family was kept, "
                  "the stories accumulated. Running things in parallel means "
                  "that when the thing that never works fails again, "
                  "something else in your hands is working.",
             "eg": "Keeping the job while the thing you care about takes years means a bad year stays a bad year, instead of becoming the end of the story."},
            {"n": "The side thing got real investment",
             "d": "The stories weren't dashed off — forty years, nearly five "
                  "hundred pieces, repeatedly revised. They were last in his "
                  "ranking, not last in his investment. And he never quit the "
                  "job: the tutoring fed him and gave him the forty "
                  "uninterrupted years.",
             "eg": "Two hours every Sunday for six years is not a hobby. It was last in his ranking and first in his hours."},
        ],
        "apply":
            "When something you've worked at for years hasn't happened and "
            "you can't say when it would, don't start with whether to "
            "persist. Ask what else moved forward this year. If you can't "
            "name one thing, fill that gap first. And if the side thing is "
            "growing, count what you've actually put into it over three years "
            "before you talk about swapping their status.",
        "q": [
            "Almost everyone here eventually made it. He didn't.",
            "He called it an idle book until he died. It is why he is "
            "remembered.",
            "He didn't quit the job to write. He wrote on the job.",
        ],
        "l": ["Excellent Sheep", "Fan Li"],
        "contrast": [
            {"n": "Excellent Sheep",
             "why": "Two ways of having no scoreboard: they were never given "
                    "one, he had one and it never once said yes"},
        ],
    },

    {
        "c": "Learning and growth", "n": "Garry Kasparov", "slug": "kasparov",
        "e": "1963– · Baku", "w": "After losing to the machine", "y": 1997,
        "d": "World chess champion for fifteen years, from 1985 to 2000. In "
             "1996 he beat IBM's Deep Blue in Philadelphia; in the May 1997 "
             "rematch in New York he lost 2.5\u20133.5, the first time a "
             "reigning world champion lost a match to a machine. Most people "
             "in this library are dealing with other people. He is dealing "
             "with something else: what is left of a craft you spent a life "
             "on after a machine passes you at the thing it is built on.",
        "story":
            "The 1996 match is usually left out, and it matters. He won it "
            "4\u20132, losing only the first game \u2014 the first time a "
            "machine had beaten a world champion under tournament conditions, "
            "which at the time was itself the headline. He then had a year to "
            "prepare, and IBM had a year to rebuild. What he faced in 1997 "
            "was not the machine he had beaten. That is the ordinary shape "
            "of it: you win the first round against a tool, conclude the "
            "threat was overstated, and meet a different thing the following "
            "year.",
        "f": [
            {"n": "Strike out what is already lost",
             "d": "The day machines won on depth of calculation, that track "
                  "closed. Training on a closed track has no exit however "
                  "hard you train. The first move isn't redoubling effort; "
                  "it's removing the lost item from your own list of what you "
                  "are worth.",
             "eg": "No amount of practice makes you faster than the model at drafting a first version. The real question is which part of the work that leaves you."},
            {"n": "Change the rules, not the effort",
             "d": "He didn't train harder and he didn't leave chess. A year "
                  "later he staged a tournament where each side brought a "
                  "computer to the board. When a tool matches an ability, the "
                  "valuable position moves to how the tool is used \u2014 and "
                  "someone has to define that position first.",
             "eg": "The translators who priced per word lost. The ones who charged for deciding what not to translate did not."},
            {"n": "The appeal and the next move cost the same hours",
             "d": "He spent years arguing the match hadn't been fair, and "
                  "withdrew all of it in 2017. Proving the loss didn't count "
                  "and working out what to train next come out of the same "
                  "person in the same stretch of time.",
             "eg": "The months spent proving the review was unfair were the same months available for the work that would have made the review irrelevant."},
        ],
        "apply":
            "When a core skill in your field gets matched by a tool, don't "
            "train harder first. Ask which item is now clearly lost, strike "
            "it out, and see what's left that the tool can't replace. And if "
            "you notice yourself repeating that it isn't actually any good, "
            "count how many times this month \u2014 then count what new thing "
            "you practised in the same month.",
        "q": [
            "Calculation was already lost, so stop competing on calculation.",
            "The first step isn't more effort. It's striking out what's lost.",
            "Whatever replaced you does not need your agreement.",
        ],
        "l": ["Norbert Wiener", "John Boyd"],
        "contrast": [
            {"n": "Norbert Wiener",
             "why": "One built the thing and warned the people it would "
                    "displace; the other was displaced and redesigned the "
                    "contest"},
        ],
    },
    {
        "c": "How the world works", "n": "Norbert Wiener", "slug": "wiener",
        "e": "1894\u20131964 · United States", "w": "He warned them first", "y": 1948,
        "d": "The founder of cybernetics: Cybernetics in 1948, The Human Use "
             "of Human Beings in 1950. His position here is unusual \u2014 he "
             "is both the person who put machine control into the world and "
             "the first to say publicly that it would displace factory "
             "workers on a large scale. In 1949 he wrote to Walter Reuther of "
             "the United Auto Workers saying he was unwilling for it to "
             "happen with no preparation. Automation had not yet been "
             "deployed and nobody had lost a job.",
        "story":
            "Cybernetics came out of the war. He worked on the problem of "
            "aiming anti-aircraft guns at aircraft that were manoeuvring \u2014 "
            "which meant predicting where a human pilot would go, and "
            "correcting continuously from what the last shot did. The "
            "feedback loop was invented while trying to shoot at people. "
            "That origin is why the ethics arrive so early in his work: he "
            "had already spent years modelling a person as a component in a "
            "system, and had seen exactly what that framing permits.",
        "f": [
            {"n": "The people who see it coming aren't hit yet",
             "d": "The year he wrote to the union there was still time to "
                  "arrange something. Once it lands you only get to react. "
                  "The stretch while you still have work is the only window "
                  "you get to plan in.",
             "eg": "The time to learn the next thing is while the current work still pays. Once it stops you are learning and job-hunting at the same time."},
            {"n": "'It can' doesn't imply 'give it to it'",
             "d": "Whether a machine can do a task is technical. What is left "
                  "of the person afterwards is a different question, and the "
                  "answer isn't automatically good. Hand over the repetition, "
                  "not the judgement.",
             "eg": "Let it draft the summary. Deciding which three of the twenty issues actually get raised is the part that was your job."},
            {"n": "Control is a loop, not an order",
             "d": "His definition: not issuing an instruction but correcting "
                  "the next move from the actual result. Cut the report back "
                  "and the movement goes off, however well it was aimed. It "
                  "applies unchanged to managing people and to practising a "
                  "skill.",
             "eg": "You set the goal in January and next heard about it in June. The instruction was fine; there was nothing correcting it in between."},
        ],
        "apply":
            "When something is spreading through your field and hasn't "
            "reached your income yet, ask which of your tasks it can already "
            "do, and who in your field you have actually talked to about it. "
            "When shifting work onto a tool, check whether what's left needs "
            "any judgement \u2014 if it doesn't, you handed over the wrong "
            "half.",
        "q": [
            "What a machine can do and what people are for are separate "
            "questions.",
            "He feared people being arranged like machines, not the reverse.",
            "Control isn't issuing an order. It's correcting from the result.",
        ],
        "l": ["Garry Kasparov", "John Boyd"],
        "contrast": [
            {"n": "Garry Kasparov",
             "why": "Wiener warned before it arrived; Kasparov was the first "
                    "person it arrived for"},
        ],
    },
    {
        "c": "Learning and growth", "n": "Excellent Sheep", "slug": "excellent-sheep",
        "e": "2014 · William Deresiewicz", "w": "Can clear, can't choose", "y": 2014,
        "d": "A critique of elite education by someone who taught at Yale for "
             "ten years and sat on admissions. His observation: the system "
             "produces young people who are extraordinarily good at clearing "
             "a series of set hurdles \u2014 grades, competitions, "
             "internships, the CV \u2014 and who generally cannot say what "
             "they want. Very capable, entirely externally directed, lost the "
             "moment there is no next hurdle, and unusually afraid of failure "
             "because they have never been allowed to fail.",
        "story":
            "He left academia after writing it. The book began as an essay "
            "that circulated very widely, and the argument it makes \u2014 "
            "that the institutions doing the selecting are the problem, not "
            "the students being selected \u2014 is not one that makes a "
            "person welcome inside those institutions. That is worth "
            "knowing before reading it as a lecture to young people. His "
            "target is the machinery: every step in it rational, and the sum "
            "a life with no direction.",
        "f": [
            {"n": "Two abilities that don't substitute",
             "d": "'Be best at this' is drilled constantly inside any "
                  "evaluation system. 'Decide what's worth doing' can only be "
                  "trained where there is no correct answer. So the smoother "
                  "the run, the likelier the second is blank.",
             "eg": "Ten years of being the person who clears every bar, and the first question with no right answer — should we even build this — is the one he can't start."},
            {"n": "Never having failed makes failure unimaginable",
             "d": "The price of an unbroken record is no experience of "
                  "failing, so failure gets imagined as catastrophic \u2014 "
                  "and the result is avoiding anything you might not be good "
                  "at, with a range that narrows year by year.",
             "eg": "She picked the third language she already half-knew over the one she wanted, because a visible beginner year was unthinkable."},
            {"n": "The prescription is time with no scoreboard",
             "d": "Not a different subject or a different job, but a stretch "
                  "long enough to get past novelty, doing something nobody is "
                  "grading. Where a metric exists, attention slides to it, so "
                  "the question can only surface somewhere without one.",
             "eg": "Six months of pottery with nobody grading it did more than another certificate, precisely because there was no number to optimise."},
        ],
        "apply":
            "If you can say exactly what counts as doing well and can't say "
            "what you want, do one thing that isn't scored, for long enough "
            "to get past the novelty. Facing any opportunity, separate two "
            "things: is it the content that draws me, or is it simply the "
            "next hurdle on the track I'm already on?",
        "q": [
            "Superb at clearing hurdles, and unable to say where they were "
            "going.",
            "Never allowed to fail, you imagine failure as unsurvivable.",
            "Only when nobody is grading you do you find out what you want.",
        ],
        "l": ["Pu Songling", "Carol Dweck"],
        "contrast": [
            {"n": "Pu Songling",
             "why": "Two ways of having no scoreboard: they were never given "
                    "one, he had one and it never once said yes"},
        ],
    },
    {
        "c": "Body and daily life", "n": "Christina Maslach", "slug": "maslach",
        "e": "1946– · UC Berkeley", "w": "Burnout is the job", "y": 1981,
        "d": "Burnout became measurable largely because of her work. Her 1981 "
             "inventory split it into three components \u2014 emotional "
             "exhaustion, depersonalisation, and a fall in personal "
             "accomplishment \u2014 of which only the first overlaps with "
             "being tired. Her most persistent and least popular claim is "
             "that burnout is a problem of the work environment, not of "
             "individual resilience: nearly every remedy on the market "
             "teaches people to relax, which asks the person absorbing the "
             "damage to repair its cause.",
        "story":
            "There is an earlier thing she is known for. In August 1971 she "
            "was a recent Stanford PhD, and her partner Philip Zimbardo was "
            "running a prison simulation in the psychology building. Visiting "
            "on the sixth night, she saw prisoners being marched to the "
            "lavatory with bags over their heads and objected \u2014 not as a "
            "methodological point but as a moral one. The experiment was "
            "shut down the next morning. Her career since has been one long "
            "version of the same argument: look at what the situation is "
            "doing to people before you look at the people.",
        "f": [
            {"n": "Only one of the three is tiredness",
             "d": "Rest fixes exhaustion. It does not fix detachment or a "
                  "collapse in accomplishment, and those two usually arrive "
                  "first. So somebody can look like they're working normally, "
                  "and still be delivering, months into it.",
             "eg": "He came back from three weeks off rested and still couldn't care about the release. The sleep debt was gone; the other two weren't."},
            {"n": "Fix the job, not the person",
             "d": "Told the problem is their attitude, a person adds a layer "
                  "of self-blame and stays in the same environment. Personal "
                  "remedies aren't useless \u2014 they're second. Reverse the "
                  "order and they stop being support and start being cover.",
             "eg": "The wellness app arrived the same quarter the team lost two people and kept the same roadmap. Everyone downloaded it. Nothing changed."},
            {"n": "Six ways to be mismatched",
             "d": "Workload, control, reward, community, fairness, values. "
                  "Most people watch only the first. In her data, having no "
                  "say and doing work that runs against what you believe are "
                  "often more lethal than volume.",
             "eg": "The hours were fine. Being told what to ship and then blamed for shipping it is the one that emptied him out."},
        ],
        "apply":
            "Before deciding you need a holiday, check which of the three you "
            "have: drained, nothing left for people, no satisfaction on "
            "finishing. Then score the six areas one at a time. 'Work is "
            "exhausting' implies no action; the six-line version usually "
            "names something specific \u2014 decision rights, fairness, or "
            "different work.",
        "q": [
            "Sleep fixes tired. It does not fix detachment.",
            "Asking the person absorbing the damage to repair its cause is "
            "backwards.",
            "If a month off returns you to the same arrangement, it isn't "
            "your mindset.",
        ],
        "l": ["Robert Sapolsky", "Arlie Hochschild"],
        "contrast": [
            {"n": "Robert Sapolsky",
             "why": "Same conclusion from two directions: she measures the "
                    "job, he measures the hormone, and both land on control"},
            {"n": "Arlie Hochschild",
             "why": "Two kinds of uncounted work: required feeling, and the "
                    "shift that starts when the paid one ends"},
        ],
    },
    {
        "c": "Mind and feeling", "n": "John Cacioppo", "slug": "cacioppo",
        "e": "1951\u20132018 · University of Chicago", "w": "Loneliness is a signal", "y": 2008,
        "d": "A founder of social neuroscience who spent a career on one "
             "question: what loneliness actually is in the body and the "
             "brain. His first move was to tighten the definition \u2014 "
             "loneliness is not being alone, it is the gap between the "
             "connection you want and the one you have, which is why a "
             "crowded room can be lonely. That change moves it out of the "
             "category of personality and into the category of hunger and "
             "thirst: a signal that something needed is missing.",
        "story":
            "He started as a psychophysiologist \u2014 someone who attaches "
            "electrodes and measures what the body does. That is why the "
            "loneliness work landed. He did not arrive arguing that people "
            "should be kinder; he arrived with blood pressure, inflammatory "
            "markers, sleep architecture and cognitive decline, on a subject "
            "everyone else was treating as a mood. Once it had numbers "
            "attached it stopped being something you could be told to get "
            "over.",
        "f": [
            {"n": "A signal, not a character defect",
             "d": "Read as a flaw, the first instinct is to say nothing, "
                  "which seals the only exit. As a signal it carries no "
                  "shame: it doesn't say something is wrong with you, it says "
                  "something needs doing.",
             "eg": "Read as 'something is wrong with me', the message stays unsent. Read as hunger, it gets sent."},
            {"n": "Vigilance grows it by itself",
             "d": "Lonely people read neutral faces as unfriendlier. The "
                  "reading makes them withdraw, withdrawal thins the "
                  "relationship, and the thin relationship confirms the "
                  "reading. Nobody has to have rejected them for the loop to "
                  "keep turning.",
             "eg": "He read the unanswered message as being dropped, so he stopped writing first, so the messages thinned, and the thinning proved him right."},
            {"n": "The effective intervention is the reading, not the "
                  "opportunity",
             "d": "In the meta-analysis, more chances to socialise, more "
                  "support and better skills all did little. What came first "
                  "was correcting the automatic conclusions \u2014 which is "
                  "why doing more events changes nothing."},
        ],
        "apply":
            "If you feel lonely and embarrassed to say so, separate two "
            "things first: am I missing people being present, or people "
            "knowing me? Crowds help the first and do nothing for the second. "
            "If it's the second, don't add events \u2014 catch the automatic "
            "sentence ('they must find me tiresome'), write it down, ask what "
            "it rests on, and find one chance to test it.",
        "q": [
            "Hungry, you go find food. This is the same kind of reminder.",
            "Loneliness will read an ordinary face as unfriendly.",
            "For loneliness, changing the reading beats changing the "
            "opportunity.",
        ],
        "l": ["Harvard Study of Adult Development", "Robert Sapolsky"],
        "contrast": [
            {"n": "Mark Granovetter",
             "why": "Both are about the shape of a network. Granovetter asks "
                    "what it brings you; Cacioppo asks what its absence does "
                    "to you"},
        ],
    },
    {
        "c": "Family and relationships", "n": "Harvard Study of Adult Development",
        "slug": "harvard-study",
        "e": "1938\u2013present · Harvard Medical School", "w": "Relationships predict the end",
        "y": 1938,
        "d": "The longest study of adult life ever run. It began in 1938 with "
             "268 Harvard sophomores, later merged with 456 boys from "
             "Boston's poorest neighbourhoods, asking how life was going "
             "every two years and running medical exams every five \u2014 for "
             "most of them, for life, and now into their children. Robert "
             "Waldinger, its fourth director, compresses eighty years into "
             "one line: what makes people healthy and content late in life is "
             "neither wealth nor fame but the quality of their relationships.",
        "story":
            "That is not what it set out to measure. In 1938 the question was "
            "what kind of young man grows into a healthy, successful adult, "
            "and the instruments were physical: build, blood pressure, family "
            "background. They measured skull dimensions. Decade by decade "
            "those predictors lost their explanatory power, and the one that "
            "survived was the thing nobody had planned to record. The sample "
            "contains men from excellent circumstances who ended isolated, "
            "and men from the tenements surrounded by people all their lives, "
            "and it is the second group whose health curves run higher.",
        "f": [
            {"n": "A predictor, not a consolation",
             "d": "It reads like a greeting card and lands on hard measures: "
                  "satisfaction with close relationships at fifty predicted "
                  "health at eighty better than cholesterol did. The body "
                  "settles the bill.",
             "eg": "It sounds like a card in a gift shop until you see it beat cholesterol at fifty for predicting how eighty goes."},
            {"n": "Quality counts, headcount doesn't",
             "d": "And a long, high-conflict relationship does more damage "
                  "than separating. What protects is what happens inside it, "
                  "not whether it is still standing \u2014 'staying for the "
                  "children' does not balance on this ledger.",
             "eg": "Two hundred contacts and nobody to call at 2am is not a large network. It is a large list."},
            {"n": "The window stays open later than people assume",
             "d": "The clearest improvements came from people who started in "
                  "their fifties and sixties: reconnecting with estranged "
                  "family, turning acquaintances into regular company. Fifty "
                  "is not too late for eighty.",
             "eg": "He rang the brother he hadn't spoken to in eleven years at fifty-eight. That call is inside the window, not past it."},
        ],
        "apply":
            "If relationships feel like something to handle once this busy "
            "stretch is over, count one number: in the last month, how many "
            "times did you see someone for no practical reason? If you can't "
            "count one, it isn't a 'later' problem. The smallest useful move "
            "is one message a week to one person, about nothing in "
            "particular.",
        "q": [
            "Your body at eighty is decided by your relationships at fifty.",
            "A marriage held together for the children bills both bodies.",
            "Nobody sets out to lose a friend. They get busy and it goes "
            "quiet.",
        ],
        "l": ["Mark Granovetter", "John Cacioppo", "Arlie Hochschild"],
        "contrast": [
            {"n": "John Cacioppo",
             "why": "The same finding from opposite ends: he measures what "
                    "the absence costs, the study measures what the presence "
                    "buys"},
            {"n": "Excellent Sheep",
             "why": "Eighty years of data on what actually matters, against a "
                    "system that scores none of it"},
        ],
    },

    {
        "c": "How the world works", "n": "Mark Granovetter", "slug": "granovetter",
        "e": "1973 · American Journal of Sociology", "w": "Weak ties", "y": 1973,
        "d": "A sociologist whose 1973 paper, The Strength of Weak Ties, has "
             "been cited tens of thousands of times. He surveyed 282 people "
             "about how they found work and found that among those who got "
             "there through a contact, 56% saw that person only occasionally "
             "and 28% rarely. The reason isn't willingness but information "
             "structure: your circle overlaps almost completely with a close "
             "friend's, so what they know you mostly know. From that he draws "
             "a harder line \u2014 no strong tie is a bridge.",
        "story":
            "The finding has a consequence people meet without recognising "
            "it. Move to a new city or leave an industry and the close "
            "friends survive \u2014 those few hold. What disappears is the "
            "wide band of people you used to see occasionally, and that is "
            "precisely the layer that brings opportunities. So the drought "
            "after a move is not imagined and not a comment on you. It is "
            "structural, and rebuilding that layer takes time, which is why "
            "the first year somewhere new is so often silent.",
        "f": [
            {"n": "It isn't willingness, it's whether the news is new",
             "d": "Close friends want to help more and hold almost the same "
                  "information you do. A weak tie isn't more generous. He is "
                  "standing somewhere else, holding the part you can't reach "
                  "from here.",
             "eg": "Your five closest friends have already told you every opening they know about. The person you met once at a conference knows the one you haven't heard."},
            {"n": "Closure is what strong ties produce",
             "d": "Close to A and close to B means A and B probably know each "
                  "other. The circle closes, and once closed the three of you "
                  "know largely the same things. Closure gives support and "
                  "trust, and it stops new information arriving.",
             "eg": "Everyone in the group chat forwarded the same article. That is what a closed circle feels like from inside: agreement, and no new information."},
            {"n": "Maintain breadth, not depth",
             "d": "Rather than pouring everything into a few people, keep "
                  "more weak ties in the 'still knows who you are' state. The "
                  "cost is an occasional message with no request attached \u2014 "
                  "and the line has to be kept while you don't need it.",
             "eg": "One message a year with nothing attached — congratulations on the new job — keeps a line open. Reappearing only when you need something closes it."},
        ],
        "apply":
            "If you're looking for something \u2014 work, a partner, "
            "customers \u2014 and circling the same few people, count how "
            "many of the people you contacted in six months are ones you see "
            "a few times a year. If almost none, a whole source of "
            "opportunity is switched off. Just after a move or a career "
            "change, expect this and rebuild deliberately.",
        "q": [
            "Of people who found work through a contact, 56% saw them only "
            "occasionally.",
            "No strong tie is a bridge.",
            "When you move, the layer that breaks first is the one that "
            "brought opportunities.",
        ],
        "l": ["Harvard Study of Adult Development", "John Cacioppo"],
        "contrast": [
            {"n": "John Cacioppo",
             "why": "Both about the shape of a network: Granovetter on what "
                    "it brings you, Cacioppo on what its absence does to you"},
        ],
    },
    {
        "c": "Family and relationships", "n": "Arlie Hochschild", "slug": "hochschild",
        "e": "1983 · UC Berkeley", "w": "Work nobody counts", "y": 1983,
        "d": "A sociologist who twice gave a name to work that had none. The "
             "Managed Heart (1983) named emotional labour: jobs that require "
             "not only that you do it right but that you display a prescribed "
             "feeling \u2014 warmth for a flight attendant, hardness for a "
             "debt collector. The Second Shift (1989) named the unpaid shift "
             "that starts when the paid one ends, and put a number on it: "
             "about 15 hours a week, a year of which is an extra month of "
             "24-hour days. Her whole contribution is making uncounted labour "
             "countable.",
        "story":
            "Doing fieldwork with Delta flight attendants she kept meeting "
            "one phrase in the training material: a sincere smile. The "
            "airline was not satisfied with courtesy. It required the smile "
            "to be real \u2014 which means the employee has to manufacture "
            "the feeling internally, and that part of the job has no hours, "
            "no pay and no name. She put it beside physical labour: lifting "
            "boxes tires you, and so does producing cheerfulness, except the "
            "second bill arrives late and usually gets recorded as 'she's "
            "changed'.",
        "f": [
            {"n": "Work off the timesheet is paid for by whoever does it",
             "d": "Anything unmeasured gets treated as done in passing. It "
                  "doesn't disappear for going unrecorded; it becomes one "
                  "person's invisible load, and that person often has no "
                  "language to complain in, because on paper nothing "
                  "happened.",
             "eg": "Nobody schedules remembering the birthdays, noticing who has gone quiet, smoothing the meeting afterwards. It still takes hours, and the same person does it."},
            {"n": "Surface acting and deep acting bill differently",
             "d": "Putting the face on while knowing you are exhausts through "
                  "tension. Persuading yourself you mean it exhausts because "
                  "afterwards you can't find yourself. Both have a cost; they "
                  "arrive at different times.",
             "eg": "Smiling through the call knowing you don't mean it leaves you tense. Talking yourself into meaning it leaves you unsure which part was you."},
            {"n": "Care time is rigid",
             "d": "You can write a document faster. You cannot feed a child "
                  "faster or sit with a sick parent faster. So 'efficiency' "
                  "barely applies \u2014 the work can only be taken over by "
                  "someone else, or not done, and then someone else pays.",
             "eg": "You can review the document twice as fast this quarter. You cannot get a two-year-old to sleep twice as fast."},
        ],
        "apply":
            "When the work at home lands on one person and saying so hasn't "
            "changed it, don't start with fairness. Log two weeks: every "
            "task, who did it, how long. Most negotiations fail because the "
            "two people are looking at different lists. At work, if you got "
            "little done and can't face speaking, ask how much of the day "
            "went on holding a required feeling \u2014 and whether any of "
            "that was counted.",
        "q": [
            "That smile is not 'her' smile.",
            "The first shift is at work, the second at home. Only one pays.",
            "Labour nobody books gets billed to one person anyway.",
        ],
        "l": ["Thomas Gordon", "Christina Maslach"],
        "contrast": [
            {"n": "Christina Maslach",
             "why": "Two kinds of uncounted work: the required feeling, and "
                    "the six ways a job and a person fail to match"},
        ],
    },
    {
        "c": "Body and daily life", "n": "Rat Park", "slug": "rat-park",
        "e": "1978 · Simon Fraser University", "w": "Look at the cage", "y": 1978,
        "d": "A set of experiments from the late 1970s, plus a natural "
             "experiment nobody designed, which together unsettled a piece of "
             "common sense about addiction. The standard method put a rat "
             "alone in an empty cage with morphine-laced water and watched it "
             "drink until it died \u2014 a conclusion that looks solid. Bruce "
             "Alexander asked a different question: what if the cage weren't "
             "empty? In a large enclosure with companions, wheels and "
             "tunnels, the same two bottles, the rats were far less "
             "interested. The point is not that the drug doesn't matter. It "
             "is that the situation has been badly underrated.",
        "story":
            "The work was not welcomed. Alexander's papers were turned down "
            "by the major journals, funding stopped, and for something like "
            "thirty years the study sat outside the mainstream \u2014 too "
            "hard to replicate cleanly, and pointed at a conclusion the field "
            "was not organised around. Its rehabilitation came from "
            "somewhere else entirely: the follow-up data on American "
            "servicemen returning from Vietnam, where the overwhelming "
            "majority of men addicted to heroin abroad simply stopped once "
            "home. Same people, same drug, different place.",
        "f": [
            {"n": "The cage is a variable, not the background",
             "d": "The original design treated the cage as scenery and the "
                  "drug as the only thing that varied. Make the cage vary too "
                  "and the conclusion moves: same rat, same bottle, very "
                  "different behaviour.",
             "eg": "Same person, same phone. Alone in a rented room at eleven at night, and in a house with people in it: the two evenings do not look alike."},
            {"n": "The empty space is manufacturing the demand",
             "d": "The park rats weren't restrained; they didn't much want "
                  "it. Alexander's word was dislocation \u2014 pull someone "
                  "out of the relationships and position they belong in and "
                  "they will find something to fill the gap.",
             "eg": "The drinking started the year he moved cities and knew nobody, and thinned out once there was somewhere to be on Thursdays."},
            {"n": "It has a boundary, and it has to be said",
             "d": "Replications were not uniformly successful and the "
                  "interpretation is still argued over. Situation is the "
                  "underrated term, not the only one. Explaining everything "
                  "with it delays people who need medical care.",
             "eg": "Telling someone in withdrawal that the cage is the whole problem leaves them holding an explanation and no treatment."},
        ],
        "apply":
            "If you're trying to stop something and every attempt ran on "
            "holding out, don't fight the thing. Log the last ten times \u2014 "
            "hour, place, what else was in your hands, who was there \u2014 "
            "and look for the recurring empty slot. Withdraw the props one at "
            "a time and it gets harder by itself. Then fill the slot, because "
            "a vacated one refills the same way.",
        "q": [
            "Same rat, same bottle. Different cage, different behaviour.",
            "Same people, same substance. Home again, and they stopped.",
            "The trigger is often not craving. It's one recurring empty slot.",
        ],
        "l": ["Maria Montessori", "Robert Sapolsky"],
        "contrast": [
            {"n": "Maria Montessori",
             "why": "The same instruction in two fields: change the room "
                    "before you correct the person in it"},
            {"n": "John Cacioppo",
             "why": "Both describe a gap that gets filled by whatever is "
                    "nearest \u2014 one calls it dislocation, one calls it "
                    "loneliness"},
        ],
    },
    {
        "c": "Learning and growth", "n": "Lev Vygotsky", "slug": "vygotsky",
        "e": "1934 · Soviet psychologist", "w": "One notch higher", "y": 1934,
        "d": "A Soviet psychologist who died at thirty-seven and left "
             "concepts that shaped the whole of education. The most important "
             "is the zone of proximal development: ability has two lines, "
             "what you can do alone and what you can do with help, and "
             "learning happens in the gap between them. Below it is "
             "repetition, above it is discouragement. He also argued that "
             "thinking is internalised from social interaction \u2014 first "
             "you do it with someone, then you can do it yourself.",
        "story":
            "His work nearly disappeared. He died of tuberculosis in 1934, "
            "and within two years his writing was suppressed in the Soviet "
            "Union, where it stayed largely unavailable for two decades. "
            "Thought and Language was not published in English until 1962, "
            "twenty-eight years after his death. So a body of work "
            "contemporary with Piaget's arrived in the West a generation "
            "late, into a field that had already settled its questions "
            "without it \u2014 which is part of why it reads as fresh now.",
        "f": [
            {"n": "Look at the second line",
             "d": "Two children stopping at the same point alone can be far "
                  "apart: give a hint, and one moves a long way and the other "
                  "doesn't. Identical current level, completely different "
                  "zone \u2014 and the zone decides what they can learn next.",
             "eg": "Two candidates fail the same task. One takes a single hint and finishes; the other needs the answer. Same score, different hire."},
            {"n": "Teaching runs ahead of development",
             "d": "Against the orthodoxy of his day, he held that you don't "
                  "wait for readiness. Appropriate guidance pulls development "
                  "forward. The pitch is: hard enough to need help, not so "
                  "hard that help doesn't get it done.",
             "eg": "Handing him the migration with a review at every step taught more than three more months of tickets he could already do."},
            {"n": "Scaffolding goes up in order to come down",
             "d": "Help that stays becomes dependence and leaves the person "
                  "at the level where they're held. Whether a piece of help "
                  "worked isn't whether the task got done \u2014 it's whether "
                  "less support is needed next time.",
             "eg": "If she still needs you on the call the fourth time, the help isn't working, however well each call goes."},
        ],
        "apply":
            "Teaching someone, or teaching yourself, find the position where "
            "it can't be done alone and can be done with one hint. That gap "
            "is what to practise. And plan the withdrawal when you give the "
            "help: first time demonstrate a step, second time prompt the "
            "opening, third time nothing.",
        "q": [
            "Between what you can do alone and with help lies the zone.",
            "Teaching should run ahead of development.",
            "Higher thinking happens between people before it happens inside "
            "one.",
        ],
        "l": ["Maria Montessori", "Carol Dweck"],
        "contrast": [
            {"n": "Maria Montessori",
             "why": "Both put the adult in the background, and disagree about "
                    "when to step in: she waits, he leans in one notch"},
        ],
    },
    {
        "c": "Family and relationships", "n": "Thomas Gordon", "slug": "thomas-gordon",
        "e": "1962 · Parent Effectiveness Training", "w": "The I-message", "y": 1962,
        "d": "A student of Carl Rogers who turned humanistic psychology into "
             "a course ordinary parents could take. His two central tools "
             "predate and are more concrete than most of what came after: the "
             "I-message, which states what happened and what it did to you "
             "instead of what kind of person you are; and problem ownership, "
             "which asks whose trouble this actually is, because the answer "
             "changes the method completely.",
        "story":
            "He observed that most parents know two moves \u2014 win (I "
            "decide) or lose (fine, have it your way) \u2014 and that both "
            "carry a long bill: the first produces compliance or "
            "opposition, the second produces someone who doesn't consider "
            "anyone else. His third method turns the conflict into a shared "
            "problem: name what each side actually needs and find something "
            "that meets both. Not a vote and not a compromise, because "
            "splitting the difference leaves everyone short. In the "
            "child-rearing thinking of 1962 this was close to heresy.",
        "f": [
            {"n": "Say the effect, not the character",
             "d": "Three parts: the specific behaviour, its actual effect on "
                  "me, how I feel. Nothing in it judges the other person, so "
                  "there is nothing to defend against. The part most often "
                  "dropped is the middle one, and it is where the persuasion "
                  "lives.",
             "eg": "'You're careless' starts a defence. 'When the numbers arrive after five I redo the deck at night, and I'm worn out' does not."},
            {"n": "Work out whose problem it is first",
             "d": "A child upset about a bad grade owns it, and the move is "
                  "listening. A child wrecking the room you work in \u2014 "
                  "that's yours, and the move is an I-message. Getting it "
                  "backwards is the common error, and it lays your anxiety on "
                  "top of theirs.",
             "eg": "The teenager miserable about a grade needs listening to. The music through the wall while you work is yours to raise."},
            {"n": "No effect you can name may mean no problem",
             "d": "If you can't say what it actually does to you, this may be "
                  "a preference rather than a problem. The step doubles as a "
                  "filter: when you can't fill it in, ask why you're "
                  "insisting.",
             "eg": "He couldn't say what the messy desk actually cost him. That was the answer: a preference wearing the clothes of a rule."},
        ],
        "apply":
            "Before raising something, split it into behaviour, effect on me, "
            "and how I feel, with no line about what kind of person they are. "
            "And before you open your mouth, ask whose problem this is. If "
            "it's theirs, listen and say back what you heard; advice at that "
            "moment moves them from solving their problem to handling your "
            "opinion.",
        "q": [
            "Say what this does to me, not what kind of person you are.",
            "Work out whose problem this is before choosing a method.",
            "Conflict doesn't have to end with somebody winning.",
        ],
        "l": ["Maria Montessori", "Arlie Hochschild"],
        "contrast": [
            {"n": "Maria Montessori",
             "why": "Both ask the adult to hold back. She changes the room; "
                    "he changes the sentence"},
        ],
    },
    {
        "c": "Body and daily life", "n": "Marie Curie", "slug": "curie",
        "e": "1867\u20131934 · Warsaw and Paris", "w": "She took his course", "y": 1906,
        "d": "Physicist and chemist, born in Warsaw, in Paris from 1891, and "
             "in 1903 a Nobel laureate in physics alongside her husband "
             "Pierre. On 19 April 1906 Pierre was killed by a horse-drawn "
             "wagon in a Paris street; the Sorbonne gave her his chair, and "
             "on 5 November she gave her first lecture, with no eulogy, "
             "picking up where his last one had stopped. She is here because "
             "the situation \u2014 the person who mattered most is suddenly "
             "gone and the days continue \u2014 has too few people who have "
             "actually lived it.",
        "story":
            "1911 was the year both things happened. She was refused "
            "admission to the Académie des sciences by a narrow vote, in a "
            "campaign that made much of her being a woman and a foreigner; "
            "and the press ran a scandal about her private life, with crowds "
            "outside her house. In the same year she was awarded a second "
            "Nobel Prize, this time in chemistry, and was advised not to come "
            "and collect it. She went. The composure that produced the "
            "November lecture was not a one-off temperament. It was the same "
            "thing, repeatedly.",
        "f": [
            {"n": "Catch hold of one thing with an hour and a place",
             "d": "An enormous blank can't be faced directly. What can be "
                  "faced has a time, a place and a content. It doesn't solve "
                  "the grief; it gives the day a shape you can put yourself "
                  "inside.",
             "eg": "'Sort out my life' is unfaceable. 'Thursday, nine to ten, the second drawer' is not, and the day now has a shape to stand in."},
            {"n": "What can't be said aloud gets written to them",
             "d": "For more than a year she wrote to Pierre in a notebook "
                  "nobody saw in her lifetime. Said to the living it becomes "
                  "a request for comfort; said to yourself it becomes "
                  "analysis. Only addressed to them does the true thing come "
                  "out.",
             "eg": "Written to a friend it becomes a request for comfort. Written to the person who died it stays what it actually is."},
            {"n": "Put the skill where it's most needed now",
             "d": "In the war she left the laboratory, raised money, fitted "
                  "vehicles with X-ray equipment, learned to drive and repair "
                  "them, and took them to the front. Those years are "
                  "academically almost blank, and were not wasted.",
             "eg": "The year he stopped shipping features and rebuilt the on-call rota is missing from his promotion packet, and it is what the team remembers."},
        ],
        "apply":
            "When the most important person has gone and life still has to "
            "continue, look for one thing in the next few days that has to be "
            "done at a set hour in a set place. If there are things you can't "
            "say to anyone, ask who they are actually addressed to, and write "
            "them to that person. Don't set yourself a date to be better by.",
        "q": [
            "It doesn't solve the grief. It gives the day a shape.",
            "Who the letter is addressed to decides what you can write.",
            "Nobody at their worst owes anyone a performance of it.",
        ],
        "l": ["C.S. Lewis", "Winston Churchill"],
        "contrast": [
            {"n": "C.S. Lewis",
             "why": "Two records of the same year: he wrote to find out what "
                    "grief was, she wrote to keep talking to him"},
        ],
    },

    {
        "c": "Strategy and competition", "n": "John Boyd", "slug": "boyd",
        "e": "United States · 1927\u20131997", "w": "Tempo", "y": 1927,
        "d": "A US Air Force colonel known as Forty-Second Boyd, from a "
             "standing bet: any pilot, he starts from the disadvantaged "
             "position, and if he isn't on their tail within forty seconds he "
             "pays forty dollars. He is said never to have paid. He never "
             "made general and never published a book \u2014 his work exists "
             "as a briefing \u2014 and he reshaped American fighter design "
             "and the doctrine of manoeuvre warfare.",
        "story":
            "The briefing was the medium. Patterns of Conflict ran to several "
            "hours and he refused to give the short version: if you would not "
            "sit through the whole thing he would not present it, because the "
            "argument was cumulative and a summary would be taken as a "
            "technique. So the ideas spread by people who had sat in a room "
            "with him for a day, which is why they arrived in doctrine "
            "before they arrived in print, and why the version that reached "
            "business books is mostly the one he refused to give.",
        "f": [
            {"n": "Fast means turning, not moving",
             "d": "Observe, orient, decide, act. The claim isn't that each "
                  "step should be quick but that you operate inside the "
                  "opponent's loop, so what he observes is the world your "
                  "last move made and every reaction fights a version of you "
                  "that no longer exists."},
            {"n": "The bottleneck is orient",
             "d": "Observe, decide and act can all be sped up with tools. "
                  "Fitting new information into an existing frame cannot. The "
                  "more successful the old frame, the less gets in \u2014 "
                  "organisations do see the change and file it under the old "
                  "map."},
            {"n": "To be somebody, or to do something",
             "d": "The talk he gave every young officer. One road: go along, "
                  "get promoted, be somebody. The other: do what should be "
                  "done. He took the second, stopped at colonel, and the "
                  "aircraft and the doctrine are full of his work."},
        ],
        "apply":
            "If you and a competitor are both accelerating and you're buying "
            "tools for every step, ask which step the loop is actually stuck "
            "on \u2014 usually the one where you saw it and didn't change the "
            "frame. Inside an organisation, the lever isn't speed, it's "
            "friction: every approval layer is delay, and every ounce of "
            "suspicion is paid for in confirmations.",
        "q": [
            "Observe, orient, decide, act.",
            "One road: promotion and medals. The other: doing what should be "
            "done.",
            "Machines don't fight and terrain doesn't fight. People do.",
        ],
        "l": ["Garry Kasparov", "Han Feizi"],
        "contrast": [
            {"n": "Han Feizi",
             "why": "Two theories of an organisation that works: rules and "
                    "consequences, or shared intent and delegated authority"},
        ],
    },
    {
        "c": "Mind and feeling", "n": "Winston Churchill", "slug": "churchill",
        "e": "1874\u20131965 · Britain", "w": "Ten years out, back at 65", "y": 1929,
        "d": "Politician and writer. He went out with the government in 1929, "
             "lost the Exchequer, and held no office for ten years \u2014 the "
             "wilderness years. He wrote for a living through them, laid "
             "brick at home, and painted. Through the thirties he repeated in "
             "Parliament that Germany was rearming and British air strength "
             "was not keeping pace, was treated as bellicose and out of date, "
             "and read aircraft production figures into the record anyway.",
        "story":
            "He was a working bricklayer with a union card. In 1928 he joined "
            "the Amalgamated Union of Building Trade Workers \u2014 an "
            "ex-Chancellor applying for membership as a bricklayer, which "
            "caused enough of a row that the union later revoked it. He built "
            "walls and a cottage at Chartwell with his own hands and wrote to "
            "a friend that he was spending his days laying bricks and writing "
            "a book. Two hundred bricks and two thousand words a day. It "
            "is the most exact description anyone has given of how to survive "
            "being shut out.",
        "f": [
            {"n": "When nobody calls, make things that leave your hands",
             "d": "The hard part of being sidelined isn't the idleness, it's "
                  "not knowing whether you still count. His answer was daily "
                  "delivery: a chapter, a stretch of wall, a painting. Output "
                  "means you don't need an invitation to feel present."},
            {"n": "Put it in a form that can be checked",
             "d": "An emotional judgement can't be verified, so it can't be "
                  "confirmed either; saying it ten times equals saying it "
                  "once. Numbers and dates can be ignored today and "
                  "reconciled later. A checkable sentence has a lifespan."},
            {"n": "Being prepared means having it ready",
             "d": "He became prime minister at sixty-five, an age then "
                  "considered retirement. Nobody had time to develop anyone; "
                  "he was called because on that subject he alone had a ready "
                  "judgement, a ready record, and a line he had not altered in "
                  "ten years."},
        ],
        "apply":
            "If you've been pushed out of the centre and don't know how long "
            "it lasts, fix on one thing you can finish daily, and arrange one "
            "task that is physically hard \u2014 being sidelined traps people "
            "in an argument with absent colleagues, and sweat competes with "
            "it. Write your important judgements down with dates. That is "
            "your only evidence later.",
        "q": [
            "Someone with output needn't wait for an invitation to feel "
            "present.",
            "A checkable sentence has a lifespan. A lament doesn't.",
            "Age is only the problem when your hands are empty.",
        ],
        "l": ["Su Shi", "Pu Songling", "Marie Curie"],
        "contrast": [
            {"n": "Pu Songling",
             "why": "Both spent decades unrecognised. His day came; Pu "
                    "Songling's never did, and the advice has to work either "
                    "way"},
        ],
    },
    {
        "c": "Family and relationships", "n": "C.S. Lewis", "slug": "cs-lewis",
        "e": "1898\u20131963 · Oxford", "w": "The notebooks after she died", "y": 1961,
        "d": "A writer and professor at Oxford and Cambridge, author of "
             "Narnia and of many books arguing people into belief. He married "
             "at fifty-eight; his wife Joy died of cancer four years later. "
             "In the months that followed he recorded his own state in four "
             "exercise books and published them under a pseudonym. He is here "
             "because the situation \u2014 someone who mattered has died "
             "\u2014 needs someone who was actually in it, not someone "
             "reasoning about it from outside.",
        "story":
            "He published it as N.W. Clerk, and it sold almost nothing. The "
            "pseudonym was not modesty: the most famous Christian apologist "
            "in the English-speaking world had written a book in which the "
            "arguments he had made for thirty years stop working on him, and "
            "he was not prepared to sign it. Friends began recommending it "
            "to him, not knowing he had written it. It went out under his "
            "own name only after his death.",
        "f": [
            {"n": "Name it correctly and you know how to treat it",
             "d": "He assumed grief was sadness and found it closer to fear "
                  "\u2014 the churn in the stomach, the inability to sit "
                  "still. Sadness is met by thinking it through, fear by "
                  "letting the body settle. The wrong name gets you the wrong "
                  "method."},
            {"n": "A belief never tested may not be a belief",
             "d": "Everything he had argued held in good weather and "
                  "collapsed at the first real event. He didn't rush to "
                  "rebuild; people who do generally build the same house out "
                  "of the same cards. What is still standing afterwards is "
                  "the actual foundation."},
            {"n": "Gripping the memory deforms it",
             "d": "The harder he tried to remember his wife, the more she "
                  "warped into someone gentler and more agreeable. Worse than "
                  "forgetting: replacing her with someone he had made. When "
                  "he stopped trying, she came back as herself."},
        ],
        "apply":
            "Just after losing someone, ask whether the feeling is more like "
            "sadness or more like fear, and treat it accordingly. Write three "
            "lines a day about how the day was \u2014 not conclusions. And if "
            "you're rehearsing the person daily out of fear of forgetting, "
            "check whether the one you're holding has become gentler than the "
            "real one.",
        "q": [
            "Not like sadness. Like fear.",
            "You don't know how much you believe something until it's life or "
            "death.",
            "The harder he tried to remember her, the more she warped.",
        ],
        "l": ["Marie Curie", "John Gottman"],
        "contrast": [
            {"n": "Marie Curie",
             "why": "Two records of the same year: he wrote to find out what "
                    "grief was, she wrote to keep talking to him"},
        ],
    },
    {
        "c": "Mind and feeling", "n": "Carl Jung", "slug": "jung",
        "e": "1875\u20131961 · Zurich", "w": "The afternoon has its own programme", "y": 1931,
        "d": "The founder of analytical psychology, Freud's most valued "
             "student and his most famous defector. Parts of what he left are "
             "hard to test \u2014 the collective unconscious, archetypes, "
             "synchronicity \u2014 and three of his concepts have been in "
             "constant use for a century because they bear directly on how a "
             "person lives: a life has a morning and an afternoon with "
             "different tasks; what you push down comes back out of other "
             "people; and the mask you wear outside can grow in.",
        "story":
            "The afternoon was not a theory he read about. After the break "
            "with Freud in 1913 he resigned his university post, lost his "
            "professional standing and spent roughly six years in what he "
            "called a confrontation with the unconscious \u2014 recording "
            "visions and dialogues in the notebooks that became the Red Book, "
            "which he kept private and which was not published until 2009. "
            "He was thirty-eight when it started. The stages of life essay "
            "comes from someone who had already lost the morning's programme "
            "and had to find another.",
        "f": [
            {"n": "Stalling at forty is the hour, not a fault",
             "d": "The morning's task points outward and its standards come "
                  "from outside. People stall in midlife not because capacity "
                  "declined but because they are still running the afternoon "
                  "on the morning's programme. What was great in the morning "
                  "will be little at evening."},
            {"n": "What you push down comes back out of other people",
             "d": "To become acceptable everyone suppresses something \u2014 "
                  "ambition, laziness, temper, wanting to be seen. It "
                  "reappears as an inability to tolerate the people who show "
                  "it. Disproportionate dislike is the signal."},
            {"n": "The mask is necessary and it has to come off",
             "d": "Without it you can't deal with the world. The danger is "
                  "taking it for yourself, and the test comes when it's "
                  "removed from outside \u2014 retirement, redundancy, "
                  "children leaving. How badly you panic measures how much "
                  "grew only on the role."},
        ],
        "apply":
            "If you're doing well and increasingly can't summon anything, ask "
            "whether the effort is still answering the morning's question. If "
            "that one is largely answered, adding more won't work. And if "
            "there is a type of person you can't think about without anger, "
            "write down the exact quality \u2014 then ask whether you have it "
            "and never let it out.",
        "q": [
            "What was great in the morning will be little at evening.",
            "When the dislike is out of proportion, it isn't only about them.",
            "The mask is necessary. The trouble is taking it for yourself.",
        ],
        "l": ["Excellent Sheep", "Zhuangzi"],
        "contrast": [
            {"n": "Excellent Sheep",
             "why": "Both describe a life built to someone else's standard. "
                    "One catches it at twenty-two, the other at forty"},
        ],
    },
    {
        "c": "Body and daily life", "n": "Robert Sapolsky", "slug": "sapolsky",
        "e": "1994 · Stanford", "w": "Stress is a mismatch", "y": 1994,
        "d": "A neuroendocrinologist who spent thirty years with a troop of "
             "wild baboons in East Africa while studying human stress "
             "physiology. His book's title is the whole argument: zebras "
             "don't get ulcers, because their stress response runs full for "
             "the few minutes a lion is charging and shuts off the moment "
             "they've escaped. Ours is identical and gets used on mortgages, "
             "managers and unanswered email \u2014 a mechanism designed for "
             "seconds, left running for decades.",
        "story":
            "The baboons made the second half of the argument. In a "
            "well-fed troop with few predators, most of the day goes on each "
            "other, so their stress hormones track social position rather "
            "than physical danger. Low-ranking animals ran chronically "
            "elevated cortisol and worse health across the board \u2014 and "
            "the exceptions were the ones with allies and with some ability "
            "to predict when they'd be harassed. That is where the real "
            "variable turned out to be: not how hard the pressure is, but "
            "whether it can be foreseen and whether you have anyone.",
        "f": [
            {"n": "Duration, not intensity",
             "d": "A week-long sprint damages nobody. Two years of being "
                  "permanently on call does. The question isn't how tired "
                  "you've been lately but when the system was last actually "
                  "switched off."},
            {"n": "The bill is charged where you can't see it",
             "d": "What gets paused under stress is immunity, digestion and "
                  "tissue repair, and those debts don't show the same day \u2014 "
                  "which is why people misjudge how well they're coping until "
                  "the symptoms arrive."},
            {"n": "Predictability and control beat reducing the load",
             "d": "At the same pressure, knowing when it's coming and having "
                  "some say over order and pace cuts the damage sharply. "
                  "Which moves the intervention from 'reduce stress' to 'add "
                  "certainty' \u2014 usually far cheaper."},
        ],
        "apply":
            "If you've been tense a long time with nothing specific wrong, "
            "ask when this system was last genuinely off. If you're managing "
            "people through something hard, give a firm date rather than a "
            "better outcome: people adapt to a certain bad and don't adapt to "
            "hanging. And swap 'these five, in this order' for 'these five, "
            "you choose the order' \u2014 same load, different physiology.",
        "q": [
            "Zebras don't get ulcers because the response runs for minutes.",
            "What makes people ill is the response that won't switch off.",
            "People adapt to a certain bad. They don't adapt to hanging.",
        ],
        "l": ["John Ratey", "Christina Maslach"],
        "contrast": [
            {"n": "John Ratey",
             "why": "Same system, two handles: Sapolsky on what keeps it "
                    "switched on, Ratey on how to switch it off today"},
        ],
    },

    {
        "c": "Learning and growth", "n": "Carol Dweck", "slug": "dweck",
        "e": "2006 · Stanford", "w": "Ability can grow", "y": 2006,
        "d": "The Stanford psychologist behind the distinction between fixed "
             "and growth mindsets: whether you believe ability is a fixed "
             "quantity or something that grows with effort and method. The "
             "two beliefs produce different behaviour \u2014 if ability is "
             "fixed, a challenge you might fail is a threat, because failing "
             "proves the quantity; if it grows, failing is information. The "
             "idea had enormous reach, and was simplified and overused on the "
             "way, which has to be handled separately.",
        "story":
            "The correction matters as much as the finding. Over the last "
            "decade several large replication studies have measured mindset "
            "interventions at a fraction of the effect the popular version "
            "implies, close to zero in some populations, with the clearer "
            "benefits concentrated among disadvantaged students. Dweck "
            "herself has spent years arguing against the version of her own "
            "idea that spread, in particular against 'false growth mindset' "
            "\u2014 schools putting the words on a wall, praising effort that "
            "produced nothing, and treating the belief as a substitute for "
            "teaching.",
        "f": [
            {"n": "Praise the move, not the label",
             "d": "'You're clever' is a label and labels need protecting. "
                  "'You went back through every wrong answer' is a move and "
                  "can be repeated. The test: can they do this praise again "
                  "next time?"},
            {"n": "The moment of failure decides the direction",
             "d": "In good weather the two mindsets look identical. The "
                  "watershed is the instant something fails: one reads 'I "
                  "can't', the other reads 'that approach can't'. The "
                  "difference is whether anyone goes looking for the cause."},
            {"n": "Mild and real, not a master switch",
             "d": "Knowing the boundary is what makes it usable. It is worth "
                  "the cost of one sentence \u2014 change how you praise, add "
                  "the word 'yet' \u2014 and it is not worth a training "
                  "programme. Treat it as a master key and you'll ignore "
                  "resources, teaching and sleep."},
        ],
        "apply":
            "Giving feedback, check whether you're praising talent or a "
            "specific move, and whether they could do it again. And when "
            "someone explains a result as a problem of attitude, ask whether "
            "the heavier variables have been checked first. Attitude is the "
            "laziest available attribution and the least fair to anyone short "
            "of resources.",
        "q": [
            "Praise for talent makes people avoid challenge. Praise for "
            "process doesn't.",
            "In a growth mindset failure is information. In a fixed one it's "
            "a verdict.",
            "Replications find the effect far smaller than the book "
            "conveyed.",
        ],
        "l": ["Lev Vygotsky", "Excellent Sheep"],
        "contrast": [
            {"n": "Lev Vygotsky",
             "why": "Both about where learning happens. He locates it in the "
                    "task's difficulty, she locates it in the reading of "
                    "failure"},
        ],
    },
    {
        "c": "Family and relationships", "n": "John Gottman", "slug": "gottman",
        "e": "1994 · University of Washington", "w": "Four fatal signals", "y": 1994,
        "d": "A psychologist who recorded thousands of couples in a "
             "laboratory, coding expression, tone and heart rate frame by "
             "frame, then tracked who divorced. His conclusion doesn't rest "
             "on theory: from fifteen minutes of one argument he classified "
             "couples with reported accuracy above ninety per cent. What "
             "predicts a breakup is not how fiercely people fight but whether "
             "four specific signals appear while they do.",
        "story":
            "The ninety per cent needs a caveat, and it is the honest part of "
            "this entry. Those figures come largely from models fitted to the "
            "same data they were then measured on, which inflates accuracy; "
            "independent prospective tests have come out lower. What "
            "survives the criticism is the direction, not the number: "
            "contempt, criticism, defensiveness and stonewalling really do "
            "predict worse outcomes, and contempt really is the strongest of "
            "the four. Treat it as a set of things to watch for in yourself, "
            "not as an instrument.",
        "f": [
            {"n": "Criticism and complaint are different things",
             "d": "A complaint targets behaviour and can be solved. Criticism "
                  "targets character and can only be defended. Many people "
                  "think they're raising an issue while every sentence "
                  "defines the other person \u2014 which is how one problem "
                  "runs for ten years."},
            {"n": "Contempt is the strongest single signal",
             "d": "Eye-rolling, mockery, mimicking their tone. It differs "
                  "from anger: anger is about the event, contempt says the "
                  "person is unworthy. It destroys the foundation rather than "
                  "one conversation."},
            {"n": "Repair succeeds on the ordinary days",
             "d": "Happy couples aren't the ones who don't fight; they're the "
                  "ones who reach for the brake and have it taken. Whether it "
                  "gets taken depends on the balance built up beforehand \u2014 "
                  "roughly five positive interactions to one negative in "
                  "stable relationships."},
        ],
        "apply":
            "When the same thing gets fought about and every round escalates, "
            "check the last sentence you said: was it about the event or "
            "about the person? Any sarcasm? Were you explaining or returning "
            "the ball? And notice whether they offered a way out that you "
            "didn't take \u2014 taking it is harder than offering it, and it "
            "is where most of this stalls.",
        "q": [
            "The strongest single predictor of divorce is contempt.",
            "Criticism targets the person. A complaint targets the act.",
            "Happy couples aren't the ones who don't fight. They repair.",
        ],
        "l": ["Esther Perel", "Harvard Study of Adult Development"],
        "contrast": [
            {"n": "Esther Perel",
             "why": "Two different illnesses: he treats the wound, she treats "
                    "the emptiness, and the moves point opposite ways"},
        ],
    },
    {
        "c": "Family and relationships", "n": "Esther Perel", "slug": "perel",
        "e": "1958– · Belgium and New York", "w": "Flat isn't broken", "y": 2006,
        "d": "Thirty years of couples therapy, nine languages, and a caseload "
             "across many cultures. She doesn't work on how to argue \u2014 "
             "Gottman covered that in detail \u2014 but on something harder "
             "to raise: everything is fine and we feel nothing. Her "
             "explanation blames neither party. Intimacy wants closeness, "
             "familiarity and predictability; desire wants distance, the "
             "unknown, the thing not yet fully held. Both are real needs and "
             "they point in opposite directions.",
        "story":
            "Her framing came from noticing what was missing in the "
            "literature. Couples therapy had a great deal to say about "
            "conflict, communication and repair, and almost nothing about "
            "desire in a long relationship, which was treated either as a "
            "medical question or as a symptom of an unfixed conflict. So "
            "the people who arrived saying nothing is wrong and nothing is "
            "there had no category to be put in, and were routinely treated "
            "for a problem they did not have. Naming it was most of the "
            "contribution.",
        "f": [
            {"n": "Two needs crowding, not love fading",
             "d": "Read as love fading, the only moves are blaming yourself "
                  "or blaming them. Read as crowding, the move is clear: not "
                  "repairing the love, but making room again for the one that "
                  "got squeezed out."},
            {"n": "A wound and an emptiness need opposite moves",
             "d": "Rupture has a wound \u2014 contempt, betrayal, sustained "
                  "attack \u2014 and mending starts with stopping and "
                  "apologising. Flatness has none and needs adding to. Get it "
                  "backwards and it worsens: apologising when you should be "
                  "adding, booking trips when you should be apologising."},
            {"n": "Count presence, not hours",
             "d": "Together is duration, present is attention. The first "
                  "stacks up easily and the second can be zero for a week. "
                  "Fifteen minutes a day facing each other with the phones "
                  "down changes how it feels; a whole weekend in the same "
                  "room may not."},
        ],
        "apply":
            "If you don't fight and aren't close, check for a wound first: in "
            "the last three months, any contempt, old grievances, belittling "
            "in front of others? If none, this is emptiness, and repeatedly "
            "sitting down to discuss the relationship will talk away the last "
            "of the ease. Ask instead when you each last did something "
            "separately and came back with something to say.",
        "q": [
            "Intimacy wants closeness. Desire wants distance. Both are real.",
            "A wound is mended, an emptiness is filled. Opposite directions.",
            "Same sofa, separate phones: zero minutes present.",
        ],
        "l": ["John Gottman", "Harvard Study of Adult Development"],
        "contrast": [
            {"n": "John Gottman",
             "why": "He can tell you whether it will last; she can tell you "
                    "why it stopped feeling like anything while lasting"},
        ],
    },
    {
        "c": "Body and daily life", "n": "John Ratey", "slug": "john-ratey",
        "e": "2008 · Harvard Medical School", "w": "Move, then think", "y": 2008,
        "d": "A professor of psychiatry at Harvard Medical School who "
             "redefined what exercise is for. The primary return, he argues, "
             "is not the body but the brain: physical activity prompts the "
             "release of proteins that support neuron growth and connection "
             "\u2014 fertiliser for the brain \u2014 with direct effects on "
             "learning, mood regulation and tolerance for stress. Filing "
             "exercise under the gym means leaving the cheapest cognitive and "
             "emotional medicine unused.",
        "story":
            "The case he leads with is a school district outside Chicago. "
            "Naperville moved PE to first period and stopped grading on "
            "performance \u2014 no measuring who ran fastest, only whether "
            "each student held their own high heart-rate zone. That cohort "
            "went on to results far above their peers on international "
            "science and maths assessments. The design detail is the point: "
            "removing the comparison is what let unathletic children work "
            "hard, and working hard is the whole of the mechanism.",
        "f": [
            {"n": "Change the motive from your shape to today",
             "d": "Aimed at the body, the return arrives months later and "
                  "runs entirely on willpower. Aimed at attention and mood, "
                  "it arrives within hours. The second is real and easier to "
                  "sustain, because the feedback is fast."},
            {"n": "Intensity beats duration",
             "d": "Good news for people with no time: you don't need long "
                  "sessions, you need the heart rate to actually have gone "
                  "up. Fifteen real minutes beats an hour of strolling, and "
                  "the hard thing should be scheduled after."},
            {"n": "Anxiety is physical, so start there",
             "d": "The body is already on standby and talking yourself down "
                  "barely reaches it. Exercise burns the standby hormones and "
                  "signals that you already ran. Which is why a walk makes "
                  "the thing less frightening while changing nothing about "
                  "it."},
        ],
        "apply":
            "When your head won't turn over, ask when you last raised your "
            "heart rate, and whether twenty minutes of moving is a better "
            "trade than another hour of grinding. When a thought has gone "
            "round twenty times, that's the signal to interrupt, not to "
            "continue \u2014 and moving is the most reliable interruption, "
            "because it occupies attention and burns the hormones at once.",
        "q": [
            "Exercise doesn't only shape the body. It shapes the brain.",
            "Anxiety is heavily physical. Talking yourself down barely "
            "reaches it.",
            "The twentieth pass over a thought produces no new information.",
        ],
        "l": ["Robert Sapolsky", "Rat Park"],
        "contrast": [
            {"n": "Robert Sapolsky",
             "why": "Same system, two handles: Sapolsky on what keeps it "
                    "switched on, Ratey on how to switch it off today"},
        ],
    },
    {
        "c": "Family and relationships", "n": "Maria Montessori", "slug": "montessori",
        "e": "1907 · Casa dei Bambini, Rome", "w": "The room, not the discipline", "y": 1907,
        "d": "One of Italy's first women doctors, who began with children "
             "with intellectual disabilities and then applied the same "
             "methods to ordinary ones, opening the Casa dei Bambini in a "
             "poor district of Rome. Her central finding is that children "
             "don't need to be shaped, they need a prepared environment "
             "\u2014 tools at their scale, the choice in their hands, and the "
             "adult stepping back from director to observer. Children thought "
             "incapable of concentrating began concentrating for long "
             "stretches on their own.",
        "story":
            "The room came before the theory. She was given a set of "
            "apartment buildings full of unsupervised three- to six-year-olds "
            "whose parents worked, and a brief that amounted to keeping them "
            "from wrecking the stairwells. There was no curriculum to defend "
            "and no institution watching, so she could change the furniture "
            "and watch what happened. The method came out of a childcare "
            "problem in a slum, not out of a laboratory \u2014 which is why "
            "every part of it is about what the child can physically reach.",
        "f": [
            {"n": "Check whether the environment matches",
             "d": "A cup out of reach or a tool only an adult can work "
                  "manufactures dependence and frustration. Change it so the "
                  "child can finish alone and the behaviour problem often "
                  "disappears. It holds for adults: plenty of "
                  "self-discipline problems are environment problems."},
            {"n": "Concentration grows, it isn't demanded",
             "d": "Children concentrate for long stretches on self-chosen "
                  "work and lose focus quickly on assigned tasks. So the "
                  "route is attractive choices and no interruption \u2014 and "
                  "the most common interruption is an adult's well-meant "
                  "attention."},
            {"n": "Help me to do it myself",
             "d": "The boundary of help: the goal is that they can finish "
                  "alone, not that the task finishes sooner. Taking over "
                  "saves your time and spends their chance to learn. The "
                  "right move is neither taking over nor leaving them \u2014 "
                  "it's dropping the difficulty one notch."},
        ],
        "apply":
            "When a child repeatedly can't do something and saying it again "
            "hasn't helped, ask whether it is physically possible at their "
            "height with their grip and these tools, and which single thing "
            "in the room could change. When you're about to take over, ask "
            "whether it's so they learn or so this ends sooner.",
        "q": [
            "A child's work isn't taught in. It happens in a prepared room.",
            "Help me to do it myself.",
            "Every unnecessary help is an obstacle to development.",
        ],
        "l": ["Thomas Gordon", "Lev Vygotsky", "Rat Park"],
        "contrast": [
            {"n": "Rat Park",
             "why": "The same instruction in two fields: change the cage "
                    "before you correct the creature in it"},
        ],
    },
]


# ── 批次包 ────────────────────────────────────────────────────
# 补齐 159 个人是并行的活。每批只写 seo/en_batches/bNN.py 和自己那几个
# chapters_en/<slug>.py，谁都不动这个文件 —— 见 en_batches/__init__.py。
import os as _os
import sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from en_batches import collect as _collect             # noqa: E402
ENTRIES = ENTRIES + _collect("ENTRIES", [])

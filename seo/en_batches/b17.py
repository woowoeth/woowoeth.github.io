# -*- coding: utf-8 -*-
"""Money and risk, batch 17: Howard Marks, Scarcity, Jim Simons, George
Soros, Nassim Taleb, Technological Revolutions.

Six entries, eleven chapters. All six originals are English-language books,
so every quotation here is the author's own sentence rather than a round trip
through the Chinese page.

Two new situations, both in the Money group. The eighty-four existing ones
cover having no money and putting money to work, and neither of those catches
the two states this batch is actually about: a crowd is running at one thing
and you cannot tell whether to join it, and the call has gone against you and
you are still in the position. Everything else here hangs off situations that
already exist.
"""

ENTRIES = [
    {
        "c": "Money and risk", "n": "Howard Marks", "slug": "marks",
        "e": "United States · 1946–", "w": "Second-level thinking",
        "y": 1946,
        "d": "Founder of Oaktree Capital, more than two hundred billion "
             "dollars under management, working in distressed debt and high "
             "yield — a trade that only has any business when other "
             "people are panicking. He has written investment memos since "
             "1990, and Buffett has said they are the first thing he opens. "
             "What makes him unusual is that he publicly gave up "
             "forecasting. He does not guess the macro, the rates or next "
             "year. He does one thing: judge where in the cycle we are "
             "standing now.",
        "story":
            "In September 2008 Lehman failed, the market went into free "
            "fall, and almost every institution was reducing. Oaktree had "
            "raised an eleven-billion-dollar distressed debt fund "
            "beforehand and had deliberately sat on it through the hot "
            "market of 2007. In the fifteen weeks after the collapse it "
            "invested roughly six hundred million dollars a week, about six "
            "billion in all. His reasoning was nearly crude: if the world "
            "really is ending, it does not matter what you own; if it is "
            "not, then not buying was the mistake. This gets told as a "
            "story about nerve at the bottom. The decisive half is the "
            "first one — raising eleven billion while everybody was "
            "making money, and then not spending it.",
        "f": [
            {"n": "Second-level thinking",
             "d": "First level: it is a good company, buy it. Second level: "
                  "it is a good company, everyone knows it, the price "
                  "already says so, sell it. You have to judge not the fact "
                  "but whether the market has overpaid for the fact. Excess "
                  "return needs a view that differs from the consensus and "
                  "is more correct than it. Both, or neither.",
             "eg": "Different and wrong hurts far more than losing money "
                   "with the crowd. The real cost of second-level thinking "
                   "is looking like a fool for long stretches."},
            {"n": "Risk is permanent loss, not volatility",
             "d": "The academy treats volatility as risk because volatility "
                  "can be measured. What actually puts people out of the "
                  "game is capital that never comes back, and being forced "
                  "to sell at the bottom. Volatility is harmless until it "
                  "makes you sell.",
             "eg": "That is what leverage really costs. Without it only "
                   "permanent loss can kill you; with it volatility can, "
                   "and volatility is far more common."},
            {"n": "The pendulum",
             "d": "Markets swing between greed and fear, this time it's "
                  "different and it will never recover, and they almost "
                  "never rest in the middle. You cannot know when the swing "
                  "reverses. You can always know which side of the arc it "
                  "is on, and that is his entire standing ground."},
            {"n": "Measure the present instead of predicting the future",
             "d": "He keeps a concrete checklist: are investors discussing "
                  "returns or risk, is a new fund easy or hard to raise, "
                  "can poor assets get debt away, is diligence lengthening "
                  "or being compressed. All observable, none of it "
                  "requiring any forecasting ability at all.",
             "eg": "When everyone is asking how much there is to make and "
                   "nobody is asking how much there is to lose, the "
                   "thermometer has already given you its reading."},
            {"n": "You do not have to swing at everything",
             "d": "Nobody calls a strike on you for not swinging. The "
                  "market quotes a price every day and you are under no "
                  "obligation to answer. Most losses come not from a wrong "
                  "judgement but from the pressure to be seen doing "
                  "something."},
        ],
        "apply":
            "Write a market temperature note once a quarter, answering only "
            "observable questions: is money easier or harder to raise than "
            "three months ago, are people discussing returns or risk, can "
            "weak projects still get funded, is diligence stretching or "
            "shrinking? Predict nothing; record the present. Six months "
            "later you will find you already knew. The harder discipline is "
            "the other half: in a good market, deliberately set aside money "
            "you do not invest. Its true cost is watching other people earn "
            "with it, and it only pays in the few weeks after a crash.",
        "q": [
            "We may never know where we're going, but we'd better have a "
            "good idea where we are.",
            "Investment success doesn't come from buying good things, but "
            "from buying things well.",
            "You can't do the same things others do and expect to "
            "outperform.",
            "Being too far ahead of your time is indistinguishable from "
            "being wrong.",
        ],
        "l": ["Warren Buffett", "Benjamin Graham", "Ray Dalio",
              "Nassim Taleb", "George Soros"],
        "contrast": [
            {"n": "Benjamin Graham",
             "why": "Graham answers what a thing is worth, Marks answers "
                    "whether now is the moment to act — two separate "
                    "skills, and most people have only trained the first"},
            {"n": "Jesse Livermore",
             "why": "Both accept that the cycle is real: Livermore surfs "
                    "the pendulum and is eventually swallowed by it, Marks "
                    "moves only when it reaches an extreme"},
            {"n": "Nassim Taleb",
             "why": "Same premise, that the future is unknowable, and two "
                    "routes out: Taleb builds a structure that survives it, "
                    "Marks takes the temperature of the present"},
        ],
    },
    {
        "c": "Money and risk", "n": "Scarcity", "slug": "scarcity",
        "e": "2013 · Mullainathan and Shafir", "w": "Bandwidth",
        "y": 2013,
        "d": "A behavioural economist and a psychologist, writing not about "
             "how to make money but about what happens once there is not "
             "enough. The claim is that scarcity itself occupies cognitive "
             "bandwidth: a person short of money is not being irrational, "
             "his mind is permanently part-occupied by how far short he is, "
             "and less judgement is left over. Their best-known evidence is "
             "the Indian sugarcane study, the same men tested when tight "
             "and again when paid. The model covers shortage of time as "
             "well as shortage of money, because both draw on the same "
             "bandwidth. (On sourcing: the specific size of the sugarcane "
             "effect has been contested — later replication work did "
             "not reproduce parts of the 2012 result, and the authors "
             "themselves ran higher-powered replications setting out which "
             "findings hold and which do not. This entry takes the "
             "direction and the mechanism, not the number.)",
        "story":
            "A regional hospital in Missouri ran roughly thirty thousand "
            "operations a year and was permanently behind. Emergency cases "
            "arrived, scheduled operations were bumped, surgeons operated "
            "at two in the morning, and every room was booked solid. The "
            "advice they were given sounded absurd: keep one operating "
            "room permanently empty. An institution that had no capacity "
            "was told to give capacity away. It worked. With one room "
            "always free the emergencies had somewhere to go, the schedule "
            "stopped collapsing, and the hospital got through more "
            "operations than before. This is the book's argument in "
            "physical form: the room was not idle, it was slack, and "
            "without slack a single unexpected case takes the whole day "
            "down with it.",
        "f": [
            {"n": "One bandwidth, and both shortages draw on it",
             "d": "The most useful thing this model does is fold two "
                  "apparently unrelated troubles into one. Doing the "
                  "month's arithmetic and racing a deadline draw on the "
                  "same attention, which is why the two together make "
                  "people so much worse than either alone.",
             "eg": "Working out how far short this month is while finishing "
                   "a proposal, and doing both badly. That is not laziness."},
            {"n": "The test is whether he does it when things are loose",
             "d": "Trading a character explanation for a situational one "
                  "needs a checkable condition, and the sugarcane design "
                  "supplies it: one group of men at two moments, rather "
                  "than poor people measured against rich ones. Anything he "
                  "does not do when comfortable does not belong on his "
                  "personality.",
             "eg": "The mistake that stops after the harvest was never "
                   "about the man."},
            {"n": "Tunnelling: the urgent pushes the important out of view",
             "d": "Scarcity narrows attention. Focus inside the tunnel does "
                  "rescue the emergency, and the cost lands outside it "
                  "— the check-up, the insurance, the call you owe "
                  "somebody — and lands late. Run the tunnel as your "
                  "normal mode and every month goes on paying for the last "
                  "one.",
             "eg": "The productivity a deadline forces out of you usually "
                   "costs a stretch with no check-ups, no replies and no "
                   "long-term decisions."},
            {"n": "Slack is not waste, it is room to be wrong",
             "d": "A calendar and an account filled to the last unit look "
                  "like maximum efficiency and are actually a tolerance for "
                  "error set to zero. With room, one surprise stays one "
                  "surprise. Without it the same surprise chains, and the "
                  "same mistake costs the poorer side far more.",
             "eg": "An untouchable emergency fund is not there for the "
                   "return. It is there so one accident does not become "
                   "five."},
        ],
        "apply":
            "Next time money or time is tight and you notice a run of "
            "decisions you cannot defend a week later, calibrate the "
            "attribution before you judge yourself: would I make these "
            "mistakes when things were loose? If not, do not start with "
            "your character, start by removing things that occupy the "
            "bandwidth. Move what matters into forms that need no memory "
            "— the payment that leaves automatically, the appointment "
            "already booked, the schedule somebody else watches — "
            "because reminders fail inside the tunnel. You did not forget; "
            "at that moment you could not see it.",
        "q": [
            "Scarcity captures the mind.",
            "Being short-sighted can be the result of having no money, not "
            "the reason for it.",
            "Slack is not waste. It is room to be wrong.",
            "The comparison was not poor people against rich ones. It was "
            "one group of men at two moments.",
        ],
        "l": ["Nassim Taleb", "Benjamin Graham", "Li Ka-shing",
              "Cal Newport"],
        "contrast": [
            {"n": "Benjamin Graham",
             "why": "Both are about room to be wrong: the margin of safety "
                    "leaves room in a valuation, slack leaves room in a "
                    "life — one guards against misjudging, the other "
                    "against accident"},
            {"n": "Cal Newport",
             "why": "Both keep an account of attention: Newport counts what "
                    "switching costs, Scarcity counts what how far short am "
                    "I occupies all day"},
            {"n": "Carol Dweck",
             "why": "Both get used to explain why people do not change: "
                    "Dweck points at belief, Scarcity at circumstance "
                    "— rule out the circumstance first"},
        ],
    },
    {
        "c": "Money and risk", "n": "Jim Simons", "slug": "simons",
        "e": "United States · 1938–2024",
        "w": "A small edge, repeated", "y": 1938,
        "d": "A mathematician first: a doctorate at twenty-three, teaching "
             "at MIT and Harvard, code-breaking for the defence "
             "establishment, and the Chern–Simons theory, which is his "
             "place in the history of mathematics and has nothing to do "
             "with money. He went into investing full time at forty-eight "
             "and founded Renaissance Technologies. Its Medallion fund has "
             "compounded at roughly sixty-six per cent a year before fees "
             "since 1988 and about thirty-nine after them, which is the "
             "best record anybody has. His method is the opposite of every "
             "traditional investor's: he does not study companies, meet "
             "management, or forecast the macro.",
        "story":
            "Simons tried fundamental trading early on, made money and "
            "then lost badly, and the real turn came when he decided to "
            "give up judgement altogether. His hiring rule became famous "
            "for being strange: no people from Wall Street, only "
            "astronomers, cryptographers, linguists and statisticians "
            "— because the Wall Street ones arrive carrying a set of "
            "beliefs that have already been falsified. Inside Renaissance "
            "every researcher shares one model and one compensation "
            "formula; nobody keeps a private strategy or a private "
            "position. It is a firm that deleted the concept of the "
            "individual hero at the level of its constitution, and its "
            "results continued after Simons himself retired.",
        "f": [
            {"n": "A small edge, repeated enormously often",
             "d": "Win about half the time plus a fraction, and do it "
                  "millions of times. This is the far pole from Buffett, "
                  "who bets heavily on a handful of near-certainties. What "
                  "they share matters more than the difference: both refuse "
                  "to bet in the middle ground. Uncertain and heavy is the "
                  "usual way to die.",
             "eg": "A casino's edge is one to five per cent and casinos "
                   "never lose, because they repeat it endlessly and cap "
                   "the size of any single bet."},
            {"n": "Data matters more than the model",
             "d": "Renaissance spent more time and money collecting, "
                  "cleaning and aligning historical data than anyone else, "
                  "and kept things others threw away: bad prints, cancelled "
                  "orders, weather records, old newspapers. The reasoning "
                  "is plain — models are public mathematics, data is a "
                  "private asset.",
             "eg": "The modern parallel: nearly every AI company's "
                   "architecture looks alike, and the gap that opens is the "
                   "data pipeline."},
            {"n": "Don't predict, just recognise",
             "d": "He never asked whether a company was any good, only how "
                  "often this price pattern had appeared before and what "
                  "followed. That gives up causation and keeps correlation. "
                  "The price is never knowing why you made money; the prize "
                  "is never being fooled by a story you told yourself."},
            {"n": "Size is the enemy of return",
             "d": "Medallion closed to outside money in 1993, took only "
                  "employees' capital, held itself near ten billion dollars "
                  "and forced the profits out. Strategy capacity is finite: "
                  "more money means your own trading moves the price and "
                  "eats the edge. Refusing a fee that large is one of the "
                  "hardest decisions in the industry.",
             "eg": "The firm's other, open funds are far larger and far "
                   "more ordinary, which is the proof that the constraint "
                   "was real."},
            {"n": "Take your hands off",
             "d": "Designing a system is easy; not rescuing it while it is "
                  "losing money is very hard. During the 1998 collapse of "
                  "Long-Term Capital, Medallion drew down and Simons "
                  "considered intervening by hand, then decided not to "
                  "touch it. That is the true entry barrier to every "
                  "quantitative method, and it is not mathematical."},
        ],
        "apply":
            "First work out which kind of fight you are in. If your edge is "
            "small but repeatable — sales, ad buying, A/B tests, "
            "distribution, interviewing — stop agonising over any "
            "single outcome, push the number of repetitions up, and hold a "
            "hard ceiling on what one attempt can cost. If your edge is "
            "large and the chances are rare — changing jobs, starting "
            "a company, marrying, a big investment — invert it: bet "
            "seldom, bet heavily, and be willing to hold cash for a long "
            "time. The worst outcome is confusing the two: heavy on a "
            "small edge is gambling, light on a large one is waste. One "
            "more counter-intuitive rule worth keeping: once a method "
            "starts earning reliably, the first thing to kill it is "
            "usually not a competitor but the scale you added yourself.",
        "q": [
            "Be guided by beauty.",
            "Work with the smartest people you can find, ideally smarter "
            "than you.",
            "Don't give up easily, and hope for some good luck.",
            "We do not overrule the model. We improve the model.",
        ],
        "l": ["Warren Buffett", "Nassim Taleb", "Charlie Munger",
              "Howard Marks", "George Soros"],
        "contrast": [
            {"n": "Warren Buffett",
             "why": "The two poles of investing: Buffett bets heavily on a "
                    "few near-certainties, Simons bets tiny amounts on "
                    "millions of near coin-flips — and both refuse the "
                    "middle ground"},
            {"n": "Nassim Taleb",
             "why": "Two mathematicians on opposite ends of one market: "
                    "Taleb is paid at the moment models break, Simons is "
                    "paid all the while they hold"},
            {"n": "George Soros",
             "why": "Soros uses reflexivity to understand the market, "
                    "Simons gave up understanding entirely — and the "
                    "money comes out of the same place"},
        ],
    },
    {
        "c": "Money and risk", "n": "George Soros", "slug": "soros",
        "e": "1930– · Budapest and New York", "w": "Reflexivity",
        "y": 1930,
        "d": "Founder of the Quantum Fund, and the man who forced the Bank "
             "of England to give way, making a billion dollars in a day. "
             "His larger contribution is not the money but reflexivity, "
             "which overturns the assumption that markets are rational. "
             "Participants' expectations move the market, and the market "
             "moves their expectations back, and the loop never settles "
             "into equilibrium. He is a student of Popper, and the whole "
             "method rests on one habit: taking seriously, in advance, "
             "that he may be wrong.",
        "story":
            "16 September 1992, Black Wednesday. Sterling had been forced "
            "into the European exchange rate mechanism at a rate that "
            "flattered it, and the British economy was paying for the "
            "flattery. Soros judged that the position could not hold, that "
            "the government would eventually have to leave, and that "
            "sterling would fall hard when it did. He borrowed heavily and "
            "sold. The Bank of England bought pounds all day and spent "
            "billions failing to hold the line. That afternoon Britain "
            "announced its withdrawal, sterling collapsed, and his profit "
            "for the day passed a billion dollars. He said afterwards that "
            "he had not attacked the pound. He had corrected a false "
            "equilibrium.",
        "f": [
            {"n": "Reflexivity",
             "d": "Mainstream economics assumes markets tend towards "
                  "equilibrium. Soros says that is simply wrong. "
                  "Expectations shape behaviour, behaviour shapes the "
                  "market, and the market reshapes expectations. It is a "
                  "loop that never converges, and the market is not a "
                  "machine seeking balance but a system being made by the "
                  "beliefs it is also making.",
             "eg": "Houses rise, buyers expect more rises, more buyers "
                   "arrive, prices rise again, speculators pile in, the "
                   "bubble forms. It runs until something outside it "
                   "breaks the circuit."},
            {"n": "Fallibility as a working method",
             "d": "I am more aware than anyone that I might be wrong, and "
                  "he means it operationally: every position is built on "
                  "the assumption that the assumption behind it could be "
                  "false. When it turns out false he cuts immediately and "
                  "does not argue for himself.",
             "eg": "Before shorting sterling he kept asking where his own "
                   "case could break — what if the Bank defends the "
                   "rate at any cost? He sized the bet only after judging "
                   "those branches survivable."},
            {"n": "Boom and bust",
             "d": "Applied to the macro picture: every large boom contains "
                  "a trend that participants have misread, the misreading "
                  "drives the boom, the boom reinforces the misreading, and "
                  "the gap between belief and reality eventually grows too "
                  "wide to hold. Naming the current misconception is his "
                  "core analytical move.",
             "eg": "2008: the misconception was that house prices only go "
                   "up. It drove the subprime boom, the boom confirmed the "
                   "misconception, reality punctured it, and the system "
                   "went down."},
            {"n": "Knowing when you're wrong",
             "d": "He credits his fortune to recognising his mistakes "
                  "rather than to being right, and pairs it with the rule "
                  "that what matters is not whether you are right but how "
                  "much you make when you are and lose when you are not. "
                  "The two together are one system.",
             "eg": "Wrong ten times at a small cost each and right once at "
                   "ten times over is a winning year, and it is only "
                   "reachable if your pride has been moved off being "
                   "right."},
            {"n": "The open society",
             "d": "Fallibility is a political philosophy too. No "
                  "institution or ideology is perfect, so a society has to "
                  "stay open enough for error to be found and corrected. A "
                  "closed society is one that claims it cannot be wrong; an "
                  "open one accepts that it will be and builds the "
                  "machinery to fix it."},
        ],
        "apply":
            "On the next decision that matters, write down your core "
            "assumption first, then interrogate it one line at a time: "
            "under what circumstances would this be falsified? If it is "
            "falsified, what is the plan? Fix the falsifying condition and "
            "the exit before you commit, and give somebody else the job of "
            "holding you to it. The point is to build might be wrong into "
            "the decision process rather than admitting it afterwards, "
            "when the admission costs the most and convinces you least.",
        "q": [
            "I'm only rich because I know when I'm wrong.",
            "Market prices always distort the underlying fundamentals.",
            "There is no shame in being wrong, only in failing to correct "
            "our mistakes.",
            "Markets can influence the events that they anticipate.",
        ],
        "l": ["Ray Dalio", "Warren Buffett", "Nassim Taleb",
              "Charlie Munger"],
        "contrast": [
            {"n": "Warren Buffett",
             "why": "Two poles of investment philosophy: Buffett trusts "
                    "that the market gets there in the end, Soros treats it "
                    "as permanently wrong"},
            {"n": "Nassim Taleb",
             "why": "Two bets on uncertainty: Soros finds the market's "
                    "error and pushes on it, Taleb builds a structure that "
                    "pays when the error finally breaks"},
        ],
    },
    {
        "c": "Money and risk", "n": "Nassim Taleb", "slug": "taleb",
        "e": "1960– · Lebanon and New York", "w": "Antifragile",
        "y": 1960,
        "d": "Lebanese, an options trader before he was a theorist of risk. "
             "He watched the Lebanese civil war, the 1987 crash and the "
             "2008 crisis at close range, and built a whole philosophy of "
             "uncertainty out of real extreme events. His central claim: "
             "most of the systems we build are fragile, and break the "
             "moment something unexpected arrives. What we should be "
             "building is antifragile — systems that get stronger out "
             "of the unexpected.",
        "story":
            "In 2008 Lehman failed and the global financial system shook. "
            "Taleb's fund made more than a hundred per cent that year. Not "
            "because he predicted the crisis, but because he had held, for "
            "years, a large book of tail-risk hedges — contracts that "
            "are very cheap and almost never pay out. In ordinary years "
            "they lose a little; in a Black Swan year they pay "
            "enormously. His barbell reaches its best outcome precisely in "
            "the worst state of the world, and it does that not because he "
            "is cleverer than anyone else, but because he refuses to "
            "assume that bad things will not happen.",
        "f": [
            {"n": "The three-way structure",
             "d": "Fragile is harmed by volatility and prefers calm; robust "
                  "is unaffected by it; antifragile gains from it and "
                  "prefers disorder. Most modern institutions are fragile "
                  "— stable on the surface, collapsing under an "
                  "extreme event. A muscle is antifragile: use strengthens "
                  "it and disuse wastes it.",
             "eg": "Ask it of your own career, your organisation and your "
                   "finances one at a time. Most people find all three sit "
                   "in the first column."},
            {"n": "The barbell",
             "d": "Ninety per cent extremely safe, ten per cent extremely "
                  "risky, and nothing in the middle. The logic is that the "
                  "middle is the most fragile place to stand in a Black "
                  "Swan: it holds neither enough safe assets to absorb the "
                  "shock nor enough risky ones to profit from it.",
             "eg": "A stable main income plus a small, genuinely wild bet "
                   "beats a portfolio of moderately risky things that all "
                   "move together."},
            {"n": "Skin in the game",
             "d": "Advice from someone who bears no consequence is noise. "
                  "Bankers gamble with client money and keep the bonus, "
                  "analysts recommend what they do not own, politicians "
                  "decide what will not touch them. Every one of those "
                  "opinions should be discounted before you weigh the "
                  "content.",
             "eg": "Ask instead what would you do, or what would you have "
                   "done to your own mother — the heuristic Taleb "
                   "credits to Gerd Gigerenzer."},
            {"n": "What a Black Swan actually is",
             "d": "The defining feature is not rarity but being outside "
                  "your model's range — not that it seldom happens, "
                  "but that you never conceived of it. A pandemic was a "
                  "Black Swan to public health systems and not to "
                  "epidemiologists. The label is relative to whoever is "
                  "holding the model."},
            {"n": "The survivorship trap",
             "d": "We see the survivors and not the dead, so almost every "
                  "lesson drawn from success is drawn from a sample that "
                  "excludes failure, and the graveyard is silent. Studying "
                  "where returning aircraft were hit tells you to armour "
                  "the places with no holes.",
             "eg": "Startup literature studies companies that lived. The "
                   "dead ones, which may have done exactly the same things, "
                   "never got written up. Ask first how many of the failures "
                   "did this too."},
        ],
        "apply":
            "Audit the shape of your income the way you would a portfolio: "
            "ninety per cent from a stable main occupation, the cushion, "
            "and ten per cent aimed at high-risk, high-return exploration, "
            "the right end of the barbell. Both ends present is what lets "
            "you survive a surprise, and occasionally profit from one. "
            "Then run the same audit on advice: before weighing what "
            "somebody recommends, find out what they have staked on it.",
        "q": [
            "The opposite of fragile is not robust. It is antifragile.",
            "Wind extinguishes a candle and energizes fire.",
            "Don't tell me what you think, tell me what you have in your "
            "portfolio.",
            "Those who don't take risks should never be involved in making "
            "decisions.",
        ],
        "l": ["Tao Te Ching", "Naval Ravikant", "Fan Li", "Sun Tzu",
              "Ray Dalio"],
        "contrast": [
            {"n": "George Soros",
             "why": "Two strategies for uncertainty: Soros hunts the "
                    "market's error and acts on it, Taleb builds a "
                    "structure that does not need to know what the error is"},
            {"n": "Ray Dalio",
             "why": "Two ways of handling what cannot be predicted: Dalio "
                    "writes principles to hold the line against it, Taleb "
                    "arranges to be paid by it"},
        ],
    },
    {
        "c": "Money and risk", "n": "Technological Revolutions",
        "slug": "technological-revolutions",
        "e": "2002 · Carlota Perez",
        "w": "The bubble pays for the build", "y": 2002,
        "d": "Carlota Perez uses two hundred years and five technological "
             "revolutions to argue something counter-intuitive: the "
             "financial bubble is not an accident of a technological "
             "revolution, it is its financing mechanism. From the "
             "industrial revolution of 1771 to the information revolution "
             "that began in 1971, every one runs the same road — "
             "technological eruption, financial frenzy, crash, "
             "institutional rebuilding, and only then the golden age. The "
             "book is quoted constantly as a positioning tool among "
             "investors and answers a question almost nothing else on this "
             "site answers: what time is it now?",
        "story":
            "Britain went mad for railways in the 1840s. Hundreds of "
            "railway companies listed, newspapers ran pages of "
            "prospectuses, and clergymen and housewives bought railway "
            "shares. The bubble burst in 1847, most investors were wiped "
            "out and most companies were wound up. But the track was laid "
            "— the shareholders went under and Britain's transport "
            "skeleton for the next century remained. A hundred and fifty "
            "years later the script ran again: telecom companies burned "
            "hundreds of billions laying fibre in the late 1990s, the "
            "crash came in 2001, Global Crossing and WorldCom went to "
            "zero, and by most estimates only a low single-digit "
            "percentage of that fibre was ever lit. The fibre did not "
            "disappear. It became the physical base of twenty years of "
            "internet, cloud and streaming, and the people who inherited "
            "it paid almost nothing. Hence her cold conclusion: money "
            "spent in a bubble is wasted financially and necessary at the "
            "level of a civilisation — a collective tuition fee for "
            "building new infrastructure very fast, paid by the first "
            "group and enjoyed by the second.",
        "f": [
            {"n": "Five waves, one rhythm",
             "d": "1771 the industrial revolution, 1829 steam and "
                  "railways, 1875 steel and heavy engineering, 1908 oil, "
                  "cars and mass production, 1971 information and "
                  "telecommunications. Fifty to sixty years each, and each "
                  "split into installation, led by financial capital "
                  "chasing asset prices, and deployment, led by production "
                  "capital chasing real output, with a crash in between.",
             "eg": "Which half you are standing in decides which playbook "
                   "works. Installation rewards betting and expansion, "
                   "deployment rewards efficiency and consolidation. Wrong "
                   "half, and effort is a headwind."},
            {"n": "The bubble is how infrastructure gets financed",
             "d": "Rational capital will not lay track, pull fibre or build "
                  "data centres before the demand exists. Only irrational "
                  "enthusiasm raises that money. Afterwards the assets "
                  "change hands cheaply to people who will actually use "
                  "them, and the first investors carry the cost. So is this "
                  "a bubble is a low-value question.",
             "eg": "What did the burnt money settle into is the high-value "
                   "one. Fibre and data centres leave reusable assets; pure "
                   "customer-acquisition subsidy leaves nothing to inherit."},
            {"n": "The turning point",
             "d": "Between the crash and the golden age lies a stretch in "
                  "which institutions and regulation have to be rewritten, "
                  "because the technology has outrun the rules. It is the "
                  "most painful phase and the most decisive one. "
                  "Technology does not deliver good times automatically; "
                  "there is an institutional fight in the way."},
            {"n": "Financial and production capital, split and rejoined",
             "d": "During installation money circulates away from the real "
                  "economy and valuation detaches from output. The crash "
                  "drags the two back together. In deployment, capital "
                  "serves production again. Asking who is currently in "
                  "charge is more useful than asking whether valuations are "
                  "high: the level is the effect, the leadership is the "
                  "cause."},
            {"n": "The techno-economic paradigm",
             "d": "What a revolution really delivers is not a few "
                  "inventions but a new common sense about what is now so "
                  "cheap you can use it freely and what is now the obvious "
                  "way to do things. Cheap oil produced not just cars but "
                  "suburbs, supermarkets, disposable packaging and global "
                  "supply chains.",
             "eg": "The cheap-computation paradigm has barely begun. The "
                   "real change will appear where nobody has ever done it "
                   "that way because it used to be too expensive."},
        ],
        "apply":
            "Stop asking whether this is a bubble and ask three more "
            "useful questions. First, which half are we in — is money "
            "chasing assets or chasing output? Second, what reusable thing "
            "is this round of burnt money settling into: computation, "
            "model capability, density of talent, or nothing but "
            "customer-acquisition subsidy? Third, if it all crashed "
            "tomorrow, whose assets would I want to pick up? Remember that "
            "the winners of installation and the winners of deployment are "
            "rarely the same people. The first group proves the thing is "
            "possible and mostly dies; the second buys the estate at a "
            "tenth of the price.",
        "q": [
            "Every technological revolution has an installation period and "
            "a deployment period.",
            "The frenzy builds infrastructure that rational capital would "
            "never have funded.",
            "Golden ages begin after the crash, on infrastructure the "
            "frenzy paid for.",
            "The crisis is not the end. It is the turning point.",
        ],
        "l": ["Ray Dalio", "Nassim Taleb", "The Innovator's Dilemma",
              "Thinking in Systems", "Peter Thiel"],
        "contrast": [
            {"n": "The Innovator's Dilemma",
             "why": "Christensen watches one firm get disrupted, Perez "
                    "watches a whole society absorb the disruption — "
                    "the same event under a microscope and a wide lens"},
            {"n": "Ray Dalio",
             "why": "Two clocks: Dalio times the debt cycle on the "
                    "financial side, Perez the technology cycle on the "
                    "production side. Overlay them to know the hour"},
            {"n": "Sapiens",
             "why": "Harari explains why people come to believe shared "
                    "fictions, Perez shows that belief turning into actual "
                    "rail and fibre"},
        ],
    },
]

INTROS = {
    "marks": "The Oaktree investor who gave up forecasting in public and "
             "reads the temperature of the present instead.",
    "scarcity": "The 2013 book arguing that being short of something "
                "occupies the mind, and that the shortage explains the "
                "decisions.",
    "simons": "The mathematician whose fund holds the best record on "
              "record, and who forbade his people from overriding it.",
    "soros": "The man who broke the Bank of England, and whose real "
             "subject is how belief changes the facts it describes.",
    "taleb": "The options trader turned risk theorist behind the black "
             "swan, the barbell and skin in the game.",
    "technological-revolutions":
        "Carlota Perez on two centuries of technological revolutions, and "
        "why each one needed its own bubble first.",
}

SCENES = [
    ("Everyone is piling in", "Money", [
        ("Everyone agrees it's a good bet. Is that already in the price?",
         [("marks", "second-level-thinking")]),
        ("It's obviously overheated. Why does it keep going up?",
         [("soros", "reflexivity"), ("marks", "second-level-thinking")]),
        ("Am I early, or am I just the last one in?",
         [("technological-revolutions", "bubble-in-the-script"),
          ("marks", "taking-the-temperature")]),
    ]),
    ("I was wrong and I'm still in it", "Money", [
        ("I was wrong weeks ago and I'm still holding on.",
         [("soros", "knowing-when-wrong")]),
        ("Cutting it now would make the loss real.",
         [("soros", "knowing-when-wrong"), ("marks", "taking-the-temperature")]),
    ]),
    ("Making money work", "Money", [
        ("I can't tell whether now is the time to be careful or bold.",
         [("marks", "taking-the-temperature")]),
    ]),
    ("I don't have enough information", "Making a call", [
        ("I can't call what happens next, so I keep doing nothing.",
         [("marks", "taking-the-temperature")]),
    ]),
    ("Not enough money", "Money", [
        ("Money is tight and I keep making stupid decisions.",
         [("scarcity", "bandwidth-tax")]),
        ("I'm judging myself for choices I only make when I'm stretched.",
         [("scarcity", "bandwidth-tax")]),
    ]),
    ("There's never enough time", "Body and energy", [
        ("Everything urgent gets done and nothing important does.",
         [("scarcity", "tunneling")]),
        ("One small thing goes wrong and the whole week collapses.",
         [("scarcity", "tunneling")]),
    ]),
    ("Do I trust my gut", "Dealing with people", [
        ("The model's answer and my instinct disagree. Do I override it?",
         [("simons", "slave-to-the-model")]),
    ]),
    ("The team has gone flat", "Leading people", [
        ("I'm the sharpest person in this room and that worries me.",
         [("simons", "simons-principles")]),
    ]),
    ("Things are going well and it scares me", "Getting it done", [
        ("Nothing has gone wrong in years. Does that prove anything?",
         [("taleb", "turkey-problem")]),
    ]),
    ("Can I trust this person", "Dealing with people", [
        ("He's certain about this. What does he lose if he's wrong?",
         [("taleb", "skin-in-the-game")]),
    ]),
    ("Do I jump in now", "AI arrived", [
        ("The money pouring in looks insane. Do I stay out?",
         [("technological-revolutions", "bubble-in-the-script")]),
    ]),
]

ASKS = {
    "marks/second-level-thinking":
        "Everyone agrees it's a good bet. Is that already in the price?",
    "marks/taking-the-temperature":
        "I can't call what happens next, so I keep doing nothing.",
    "scarcity/bandwidth-tax":
        "Money is tight and I keep making stupid decisions.",
    "scarcity/tunneling":
        "Everything urgent gets done and nothing important does.",
    "simons/slave-to-the-model":
        "The model's answer and my instinct disagree. Do I override it?",
    "simons/simons-principles":
        "I'm the sharpest person in this room and that worries me.",
    "soros/reflexivity":
        "It's obviously overheated. Why does it keep going up?",
    "soros/knowing-when-wrong":
        "I was wrong weeks ago and I'm still holding on.",
    "taleb/turkey-problem":
        "Nothing has gone wrong in years. Does that prove anything?",
    "taleb/skin-in-the-game":
        "He's certain about this. What does he lose if he's wrong?",
    "technological-revolutions/bubble-in-the-script":
        "The money pouring in looks insane. Do I stay out?",
}

SC_BOX = {
    "Everyone is piling in":
        "Money is rushing at one thing and I cannot work out whether to "
        "follow or stand aside. How do I read where we are?",
    "I was wrong and I'm still in it":
        "The evidence turned against me a while back and every day I find "
        "another reason to stay. What would settle it?",
}

SC_SHORT = {
    "I was wrong and I'm still in it": "Wrong and still in it",
}

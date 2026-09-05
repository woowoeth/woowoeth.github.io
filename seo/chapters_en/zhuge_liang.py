# -*- coding: utf-8 -*-
"""Zhuge Liang — English.

Most of what reaches English about him comes through the novel, where he is
a magician with weather and fans. The historical record is less entertaining
and more useful: a strategy whose sharpest section is the part that rules
things out, a memorial that is really an org chart, and an execution that
was only half the punishment.
"""

PARENT = {
    "name": "Zhuge Liang",
    "slug": "zhuge-liang",
    "blurb": "Deep read",
    "items": [
        {"k": "longzhong-plan", "n": "The plan at Longzhong",
         "w": "The first half is what not to touch", "ready": True,
         "line": "Two of the three biggest pieces are crossed off first"},
        {"k": "close-the-worthy", "n": "Near the worthy, far from the small",
         "w": "It is about who can reach you alone", "ready": True,
         "line": "Who gets to see you privately decides what you see"},
        {"k": "executing-ma-su", "n": "The tears, and then the demotion",
         "w": "He put himself on the same list", "ready": True,
         "line": "Punish the man who did it and stop there, and it leaks"},
    ],
}

CHAPTERS = [
    {
        "k": "longzhong-plan",
        "n": "The plan at Longzhong",
        "w": "The first half is what not to touch",
        "src": "Records of the Three Kingdoms, Book of Shu, Biography of "
               "Zhuge Liang",
        "dek": "A twenty-seven-year-old lays out a strategy that governs the "
               "next several decades. Its hardest work is done in the "
               "opening section.",
        "story":
            "Asked for a plan after the third visit, he began not with what "
            "to attack but with what could not be. Cao Cao has a million men "
            "and holds the emperor: you cannot contend with him. Sun Quan has "
            "held the east for three generations, the ground is hard and the "
            "people attached: he can be an ally, not a target. ==Two of the "
            "three biggest pieces on the board are crossed off before "
            "anything is chosen.== Only then the available ones, Jing and Yi, "
            "and the conditions: hold both, keep the alliance, put the "
            "government in order, and when there is a change, move by two "
            "roads.",
        "f": [
            {"n": "The first half of a strategy is elimination",
             "d": "Rule out what cannot be beaten and what should not be "
                  "touched, and what remains is the actual menu. Most "
                  "strategy discussions skip the step and open with what we "
                  "should do, which spreads the money across several fights "
                  "that were never worth entering.",
             "eg": "Before the annual goals, write the list of what we are "
                   "not doing this year and get agreement on it. That list "
                   "moves the budget more than the goals do."},
            {"n": "Different relations for different stronger parties",
             "d": "Both are out of reach, and he treats them differently: one "
                  "cannot be contended with, the other can be an ally but "
                  "not a target. Filing everyone stronger than you under "
                  "enemy is how a plan ends up isolated. Naming which one "
                  "must be joined is what makes it stand.",
             "eg": "Of the two giants in your industry, one has to be avoided "
                   "head-on and the other may supply you or send you traffic. "
                   "Treat both as rivals and the road narrows."},
            {"n": "Write the trigger condition down",
             "d": "When there is a change in the empire is the whole plan's "
                  "trigger. He never claims a date. He says that until the "
                  "condition appears, everything being done is preparation. "
                  "Writing the trigger down stops both mistakes: firing "
                  "early, and not being ready when it fires.",
             "eg": "When the rival's main product visibly stalls, we commit. "
                   "Write that sentence down, and name the number that counts "
                   "as stalling, or it becomes a mood on the day."},
        ],
        "q": [
            "You cannot contend with him.",
            "He can be made an ally. He cannot be taken.",
            "When there is a change in the empire, move by two roads at "
            "once.",
        ],
        "apply":
            "Where you are: you are setting the next direction and there are "
            "more options than resources.\n"
            "Ask first: which of these can you plainly not win, and which of "
            "those should be joined rather than fought? Write both lists "
            "before the third one.\n"
            "Where it goes wrong: listing only what you will do; or keeping "
            "the trigger condition in your head instead of writing it as "
            "something anyone can check.",
    },
    {
        "k": "close-the-worthy",
        "n": "Near the worthy, far from the small",
        "w": "It is about who can reach you alone",
        "src": "The Memorial on Sending Out the Army",
        "dek": "Eight characters usually read as a moral instruction. What he "
               "means is narrower and more mechanical: who is able to see "
               "you privately.",
        "story":
            "The memorial states it as cause and effect. ==Keeping near to "
            "worthy officials and far from small men is why the Former Han "
            "rose; the reverse is why the Later Han fell.== Then, instead of "
            "moral advice, he arranges channels. Palace and government office "
            "are one body; reward and punishment must not differ between "
            "them. On matters in the palace, consult Guo Youzhi, Fei Yi and "
            "Dong Yun. On matters in the camp, consult Xiang Chong. And a "
            "warning: do not belittle yourself, and so block the road along "
            "which honest advice arrives.",
        "f": [
            {"n": "Near and far describe a channel, not a preference",
             "d": "A small man is not effective because he flatters well. He "
                  "is effective because he holds a route to the decision "
                  "maker that nobody else has. Cut the route and the same "
                  "person has no influence at all. The thing to manage is "
                  "the structure, not the character.",
             "eg": "Someone goes around every review straight to the boss and "
                   "it works once. After that everyone copies him. The fix is "
                   "not the man, it is the route he used."},
            {"n": "Belittling yourself blocks the road too",
             "d": "Do not belittle yourself and so block the road of honest "
                  "advice is the half nobody quotes. A leader who keeps "
                  "saying he does not understand and is not much good leaves "
                  "people unable to judge what is worth reporting, so they "
                  "report less. Excessive modesty and deafness produce the "
                  "same silence.",
             "eg": "I do not really follow the technical side, you decide "
                   "sounds open for a month. After six, a serious risk goes "
                   "unreported because nobody knows if saying it does "
                   "anything."},
            {"n": "Name the people and the subjects",
             "d": "He does not say listen to good advisers. He pairs names "
                  "with subject matter, one line at a time: for this class of "
                  "question, that man. Named to a person, the channel is "
                  "real. Left as a principle, the channel is decorative.",
             "eg": "Important decisions should involve more voices means "
                   "nothing. Naming the three roles that must be heard, with "
                   "none of them skippable, changes the structure."},
        ],
        "q": [
            "Near the worthy and far from the small men: that is why they "
            "rose.",
            "Do not belittle yourself and block the road honest advice comes "
            "along.",
            "Palace and office are one body. Reward and punishment must not "
            "differ.",
        ],
        "apply":
            "Where you are: you suspect that what reaches you has been "
            "reshaped on the way.\n"
            "Ask first: how many routes exist that reach you without passing "
            "through anyone, and who is currently using each of them?\n"
            "Where it goes wrong: blaming the character of one person; or "
            "replacing a named channel with a principle about listening to "
            "more people.",
    },
    {
        "k": "executing-ma-su",
        "n": "The tears, and then the demotion",
        "w": "He put himself on the same list",
        "src": "Records of the Three Kingdoms, Book of Shu: the biographies "
               "of Zhuge Liang and Wang Ping",
        "dek": "Executing the man he had promoted is not the hard part of "
               "this story. What he did immediately afterwards is.",
        "story":
            "On the first northern campaign he passed over Wei Yan and Wu Yi, "
            "whom everyone had recommended, and gave the vanguard to Ma Su. "
            "At Jieting Ma Su went against the deployment, left the water and "
            "camped on the hill; Zhang He cut the water off and destroyed "
            "him. Back in Hanzhong, Zhuge Liang executed him to answer to the "
            "army. Then he sent up a memorial asking to be demoted three "
            "ranks, with the charge spelt out: ==I was not clear-sighted "
            "about men, and muddled in handling affairs.== He went from "
            "chancellor to general of the right.",
        "f": [
            {"n": "Punish only the executor and the fault leaks downward",
             "d": "The error happened in execution, but the choosing and the "
                  "authorising happened above it. Handling the executor alone "
                  "announces that the deciding layer carries no consequences, "
                  "so the same failure returns by the same route, because the "
                  "cause was never touched.",
             "eg": "The project fails, the project manager is disciplined, "
                   "and the person who approved it is untouched. The next "
                   "project comes apart at the identical seam."},
            {"n": "Self-demotion has to name the charge",
             "d": "He did not say responsibility rests with me too. He wrote "
                  "the specific count: not clear-sighted about men. That is a "
                  "charge somebody can hold up against his later behaviour. "
                  "Vague self-criticism binds nobody. A named one gets "
                  "remembered and used.",
             "eg": "We all share the blame says nothing. I approved the "
                   "schedule without checking it gives people a sentence to "
                   "quote back at you next time."},
            {"n": "Weep, and carry out the law",
             "d": "He was as close to Ma Su as to a son and executed him "
                  "anyway; then mourned him personally and raised his "
                  "children. Feeling and rule each ran their own course at "
                  "full strength. Using the feeling to suspend the rule, or "
                  "the rule to prove you have no feeling, is half a job "
                  "either.",
             "eg": "Letting go a long-serving colleague you like: the "
                   "severance, the thanks and the introductions are all real, "
                   "and the decision does not move."},
        ],
        "q": [
            "He executed Ma Su to answer to the army.",
            "I was not clear-sighted about men, and muddled in handling "
            "affairs.",
            "By the rule of the Spring and Autumn, the commander answers for "
            "it.",
        ],
        "apply":
            "Where you are: a failure needs accounting for, and the person "
            "who got it wrong was the one executing.\n"
            "Ask first: who chose him and who authorised it, and what "
            "happened to that person? If the answer is nothing, the case is "
            "still open.\n"
            "Where it goes wrong: closing the file once the executor is dealt "
            "with; or stopping your own account at the contentless phrase "
            "that you share the blame.",
    },
]

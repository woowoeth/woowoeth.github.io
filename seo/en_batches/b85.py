# -*- coding: utf-8 -*-
"""Daily entry: Wang Anshi.

Picked the old way (the queue in DAILY_QUEUE.md is finished and the next batch is not yet approved).
'Straight A's, then no more grades' (Chinese side) is among the emptiest scenes; what hangs there is about
scoreboards and motivation, and none says the plain thing: a gift you only perform stops growing.
'Should I step back' covers leaving at the top and handing over; none asks whether you are stepping back
only because the people around you did.

Why he qualifies: chief minister of the Northern Song, one of the Eight Great Prose Masters of Tang and Song,
biography in the History of Song (juan 327).
The entry story is his repeated refusal of a court post; the chapters are two of his own essays.
"""

ENTRIES = [
    {
        "c": "Learning and growth",
        "n": "Wang Anshi",
        "slug": "wang-anshi",
        "e": "Northern Song · 1021–1086",
        "w": "Learning", "y": 1069,
        "d": "Chief minister of the Northern Song and one of the great prose writers of Tang and Song. The History of Song "
             "says he loved books as a boy and never forgot what he had read once. After years as a local official he became "
             "vice chief councillor in 1069 and drove the New Policies, the reform that still bears his name. He is here for "
             "two short essays he wrote before he held power, one on talent and study, one on turning back halfway. "
             "The reform itself is not judged here.",
        "story":
            "The court offered him posts in the imperial libraries again and again, and he kept declining, until scholars "
            "said he had no wish for office and regretted never having met him. When he was later named a court diarist he "
            "refused for days. A clerk brought the appointment to his door; he would not take it. The clerk followed him "
            "bowing, and he hid in the privy. The clerk left it on his desk; he sent it back. Only after eight or nine "
            "memorials did he accept.",
        "f": [
            {"n": "Learn the intent, not the form",
             "d": "In a long memorial to the emperor in the late 1050s he argued that following the ancient kings meant following their intent and nothing more. Learn why they acted as they did, and change can come without alarming the realm.",
             "eg": "Studying a company you admire, find out why it set its rules before you copy its org chart."},
            {"n": "Books were always meant for work",
             "d": "When he took office the emperor told him people thought he knew the classics but not the world. He replied that the classics exist to run the world; most so-called scholars were mediocre, so people assumed the two did not meet.",
             "eg": "If you have read every management book and still cannot lead three people, the gap is rarely the books. It is reading without meaning to use them."},
            {"n": "First, one county",
             "d": "After passing the exams he skipped the usual route to a library post and stayed a local official. In Yin county he built dykes and dug reservoirs, and lent grain to farmers to be repaid with interest, so old stock and new kept turning over.",
             "eg": "Run a new process in one team for a quarter before rolling it out to the whole company."},
        ],
        "apply": "This week pick one thing you were praised as a natural at. Ask what you have learned in it in the past year. "
                 "If you cannot name anything, put a fixed practice slot for it in your calendar instead of waiting to remember.",
        "q": [
            "Copy the reason, not the rule.",
            "The classics were meant for running things.",
            "Make it work in one county first.",
        ],
        "l": ["Su Shi", "Zhang Juzheng", "Shang Yang"],
        "contrast": [
            {"n": "Su Shi", "why": "Both were among the great prose masters and both were spotted early by Ouyang Xiu: Zeng Gong carried Wang's essays to him, and Ouyang was the chief examiner when Su passed. On the New Policies they stood apart. Wang, in the History of Song's words, was set on his own judgment and pushed the reform through; Su opposed it, and later opposed the old party when it tried to scrap all of it. One would not turn back; the other would not follow either side all the way."},
        ],
    },
]

INTROS = {
    "wang-anshi":
        "The Song chief minister behind the New Policies, and one of China's great prose stylists. "
        "He wrote about a boy poet who ended ordinary, and about turning back from a cave too soon",
}

SCENES = [
    ("Straight A's, then no more grades", "Starting out", [
        ("Everyone said I was clever as a kid, and now I'm ordinary.",
         [("wang-anshi", "fang-zhongyong")]),
    ]),
    ("Should I step back", "When to step back", [
        ("Everyone is pulling out, but I still have it in me.",
         [("wang-anshi", "the-back-cave")]),
    ]),
]

ASKS = {
    "wang-anshi/fang-zhongyong": "Everyone said I was clever as a kid, and now I'm ordinary.",
    "wang-anshi/the-back-cave": "Everyone is pulling out, but I still have it in me.",
}

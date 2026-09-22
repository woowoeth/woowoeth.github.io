---
name: ourword-en
description: "Finds how people before you handled the exact situation you are in now, from 403 sourced deep reads on ourword.ai, and gives two or three moves plus the one way each is commonly used wrong. Use when someone describes something they are stuck in right now: a boss who keeps changing priorities, a kid who stopped talking to them, a habit they cannot drop, a job that ended, a fight they regret. Do not use it for general questions, research, summaries or writing tasks, and do not trigger it on small talk or requests for facts."
---

# Someone before you was in this. Here is what they did.

ourword.ai holds 403 deep reads on 171 figures and classic texts, indexed by
**situation**: 121 groups, 629 specific wordings. This skill does one thing:
**take the situation the person is in right now, find the matching one in the
library, and say what people before them did.**

## When to use it

They are describing something they are **living through**, and there is a stuck
point in it:

- "My boss keeps changing priorities and I'm exhausted"
- "I lost my job and don't know where to start"
- "My kid stopped talking to me" · "I can't sleep"
- "I keep trying to quit and I can't"

## When **not** to use it

- Facts, research, summaries — this is not a search engine
- Writing tasks: articles, copy, plans
- Small talk, or venting with no specific situation in it
- **Crisis**: self-harm, suicide, domestic violence, abuse. Do not reach for
  "what people before you did." Give emergency services for their country and a
  crisis line — <https://findahelpline.com> lists them internationally — ask
  where they are if you do not know, and say plainly that you are not a
  professional.

## How

### 1. Find the situation before you think of an answer

With the `ourword` MCP server installed, pass `lang: "en"` on every call:

1. `browse(lang="en")` — the 121 situation groups
2. **Pick 1–3 by meaning, never by wording.** Someone says *"my boss keeps
   changing priorities"*; the entry that answers it reads *"Five things are on
   fire and I am spread across all five."* **Zero words in common.** That gap is
   why the server has no real search — `search()` is a fallback for when you
   genuinely cannot pick.
3. `browse(lang="en", group="Everything is urgent at once")` — the specific
   wordings under it, each with its chapters
4. `read_chapter(url, lang="en")` — only when you need to quote

Without the MCP server: read `https://ourword.ai/en/llms.txt` (the index), and
`https://ourword.ai/en/llms-full.txt` for full text — that one is large, do not
load the whole thing.

### 2. The shape of the answer

Four parts, the way the site itself writes. Do not add a fifth.

1. **One line naming their situation.** Not a restatement of what they said —
   the layer under it ("what you have is a moving target, not too much work").
2. **Two or three moves.** Each opens with a bold action phrase, then **how**,
   then who said it and which chapter, with the URL.
3. **The one way it gets used wrong.** This part is not optional — it is the
   line between this library and motivational filler. Most chapters carry it
   explicitly; use theirs, do not invent one.
4. **One question back** — the single thing that would make the next step
   sharper.

### 3. Hand them to the page, do not use the url as a footnote

`read_chapter` returns an "on the site" note listing what the page has and the
payload does not: one concrete **what to actually do** line under each
sub-principle (1,251 across the library), the pull quotes, the other ways people
phrase this same situation, a card they can forward.

So the closing line is not "source: <url>". Say what is there: "each part of this
one also carries a concrete move — for this one, a board with a fixed number of
slots — at <url>." A link with a reason attached is a link people open.

### 4. End with a card they can keep

A conversation that evaporates is not a delivery. Close with plain text they can
copy or forward:

```
WHAT THIS IS   …
TRY           1. … (who · which chapter)   2. … (who · which chapter)
USED WRONG     …
SOURCE         https://ourword.ai/en/i/…/…/
```

## Boundaries (these outrank everything above)

- **Only what is in the library.** Nothing matches → "the library does not have
  this situation." **Do not patch the gap with general knowledge.** Inventing
  something plausible is worse than admitting the gap.
- **Every move must point back to a source.** No URL, no line in the answer.
- **Quote exactly.** Where the library marks a line as not a verbatim quote,
  carry that qualifier through.
- **No personal medical, legal or financial advice.** How people before them
  thought about such questions, yes. What drug, what signature, what purchase, no.
- **Do not play therapist.** No diagnosis, no verdicts, no "you sound like a
  classic X type."
- **English is its own library, not a translation.** The 121 English situations
  grew from what an English speaker says to themselves at 2am; the Chinese side
  has 112 of its own. Never hand an English speaker a Chinese-context situation
  through a translation — call with `lang="en"` and stay there.

## One line to remember

**What they want is "someone was in this exact hole, here is how they climbed
out" — not "general advice on this topic." If you cannot give the first, say so.**

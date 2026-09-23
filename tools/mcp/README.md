# ourword-mcp

**403 deep reads on 171 figures and classics across 2,600 years, indexed by the
situation you're actually in.** An MCP server with no search — the client's
model does the matching.

## Why there is no search in here

Someone says: *"my boss keeps changing priorities."*

The entry in the library that answers it reads:
*"Five things are on fire and I am spread across all five."*

**Those two sentences share zero words.** Keyword search cannot get from one to
the other; the model calling this server can, instantly. So the server stopped
trying. It exposes the index in two levels and lets the model pick:

```
browse()                              → 121 situation groups
browse(group="Everything is urgent…") → the specific wordings, each with chapters
read_chapter(url)                     → full text
```

That design is not a preference. The first version *was* a literal search: on
real situation sentences it returned **0 hits**, top score 0.11. The scoring
function had its denominator rewritten twice before the conclusion became
obvious — nothing belonged in that position at all.

`search()` still exists as a fallback for when the model cannot pick. It is
documented as a fallback, in the tool description the model reads.

## Install

```bash
claude mcp add ourword -- uvx ourword-mcp
```

Before that lands on PyPI, straight from the repo — same one line:

```bash
claude mcp add ourword -- uvx --from git+https://github.com/woowoeth/ourword-mcp ourword-mcp
```

Or from source, no packaging involved — it is one file and the standard library:

```bash
claude mcp add ourword -- python3 /path/to/ourword_mcp.py
```

Nothing to clone: the index is fetched from the web and cached locally for a day.

## The three tools

| tool | what it does |
|---|---|
| `browse(lang, group)` | no `group`: list the situation groups. With `group`: the specific wordings under it, each with the chapters that answer it. |
| `read_chapter(url)` | full text of one chapter. Use the url `browse` gave you. |
| `search(query, limit)` | literal fallback. Prefer `browse`. |

`lang` is `zh` (default) or `en`.

## Chinese and English are not translations of each other

The same **403 chapters**, entered through a different set of doors:
**112 situation groups / 655 wordings** in Chinese, **121 / 629** in English.
What an English speaker says to themselves at 2am is not a translation of what
a Chinese speaker says — so the two indexes grew separately. The Chinese side
has situations about social-insurance gaps and the graduate exam; the English
side has its own.

## What it will not do

Written into the tool descriptions, because that is what the model reads:

- **Only what is in the library.** Nothing matches → say so. Do not invent.
- **Every item carries a URL.** An answer that cannot point back to the source
  does not get written.
- **Not personal medical, legal or financial advice.** How people before you
  thought about such questions, yes. What you should do, no.

Ask it about a cat losing fur and it returns `found: 0` and tells the model, in
so many words, not to make something up.

## Also available as an Agent Skill

`npx skills add woowoeth/ourword-skills` — for clients without MCP. It reads the
same index over plain HTTP (`https://ourword.ai/en/llms.txt`), so it works with
no configuration at all. MCP is for people who can wire up a server; the Skill
is for everyone else.

## Privacy

No telemetry. The server fetches two public JSON files and caches them in
`~/.cache/ourword-mcp`. Install counts come from public CDN and PyPI numbers,
not from anything this program reports.

MIT. Source: <https://github.com/woowoeth/woowoeth.github.io/tree/main/tools/mcp>

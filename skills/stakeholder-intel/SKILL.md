---
name: stakeholder-intel
description: Pull fresh signal about my key people from mail, chat, calendar and meeting notes into today's signal-cache file, and propose quotes for me to confirm. Use daily or on demand, and before any question about what a person said or wants.
---
# Stakeholder intel
Core of the OS: a current, quoted picture of the people I work with, built from what they actually said, so every other skill starts from it.

## Autonomy boundary
- MAY read my connected sources, write `context/signal-cache/<today>.md`, append to `logs/stakeholder-intel.md`, and propose quotes in chat.
- MAY add a confirmed quote to that person's block in `context/people.md`, only after I say yes to that quote.
- NEVER send, reply, or contact anyone. NEVER edit or delete an existing line in `context/people.md`. NEVER mark anything confirmed myself.

## Method
1. **Roster.** Read `context/people.md` (names, roles, sources for each). Read today's `context/signal-cache/<today>.md` if it exists. If it is fresh for a source, reuse it instead of fetching again.
2. **Fetch lists, not bodies.** One batch: today's calendar, meetings with notes, mail threads (`newer_than:1d`), chat DMs, docs modified. Open full bodies only for items that involve someone on the roster. Hand body reading to a small-model subagent when there are more than a few, so the main conversation stays short.
3. **Write the signal-cache file** (format below). One file per day, one section per source. Merge into an existing file, never overwrite another skill's section.
4. **Extract signal.** For each rostered person, find statements that still matter in a month: their priorities, what they depend on, how they say they like to work, where I can help.
5. **Propose, don't record.** Show me each candidate as: person, a short paraphrase, the verbatim quote, the source link. Ask me to confirm one at a time. Confirmed ones go into `context/people.md` under that person with the date and link.
6. **Log** one line to `logs/stakeholder-intel.md`: date, sources reached, sources unreachable, quotes proposed, quotes confirmed. Then run `python3 scripts/run-cost.py` and paste its block under the entry.

## Rules
- **Quote, don't synthesize.** The quote is the person's literal words from the primary source (transcript, raw mail, message), trimmed with `…`, never reworded. Summaries are paraphrase: never quote from them. If you can't recover the exact words, leave the quote empty and say why.
- **Attribute only what's unambiguous.** A person is who the statement is *about*. If the speaker or subject is unclear, skip it. Never match a name to a person or role without a source.
- **Durable signal only.** Skip logistics ("set up a call", "will look into it") and anything already in `people.md`.
- **Decider vs reporter.** If the person who decides says it, propose it as their statement. If someone reports another person's decision, label it "heard from <name>", and don't treat it as confirmed.
- **Never infer feelings or preferences.** Record how someone likes to work only when they said it themselves.
- **No signal for a person today: skip them.** No "nothing new" notes.

## Signal-cache format
`context/signal-cache/YYYY-MM-DD.md`. Derived, overwritable, deleted after ~5 weeks. Never a source of truth.

```
---
date: YYYY-MM-DD
fetched_by: [stakeholder-intel]
sources_cached: [Calendar, Gmail]
sources_unreachable: [Chat]
last_updated: YYYY-MM-DDTHH:MMZ
---
### Meetings
#### <title> · <time> · <attendees>
- Summary: <2-3 lines>. Action items: <item> (<owner>).
- Transcript: available / not available. Link: <url>
### Gmail
- <sender> · <subject> · <one line> · <link>
### Chat
- <person> · <one line> · <link>
```
A reader must be able to brief the day from this file alone, without fetching again.

## Cost notes
Small model for the fetch and first-pass read, big model only for the propose step. Target: under 20 turns. Batch independent calls into one message.

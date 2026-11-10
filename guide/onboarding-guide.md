# Starter OS: onboarding flow

A way to set up a small personal OS with Claude in about 90 minutes, from scratch. Nothing is copied from anyone else's setup: the structure is generic, and every file is filled with your own answers.

**The idea in one line:** a folder Claude reads before it acts (who you are, what matters, what it may touch), plus a few written-down routines for work you repeat, plus a log of corrections so it gets better.

---

## 1. The model (keep it to three parts plus a loop)

| Part | What it is | v1 contents |
|---|---|---|
| Inputs | Where signal comes from | The tools you connect (mail, calendar, meeting notes, docs). Read-only. |
| Memory | Files in a git repo, read before any live source | `context/` (confirmed facts), `cache/` (digests of live sources) |
| Work | Repeatable jobs, one instruction file each | 2 skills, picked in the interview below |
| Loop | Corrections become rules | `logs/friction-log.md` + a 15-minute review every 2 weeks |

Rules that make it work:
- **Memory before live sources.** Claude reads your files first, and says when they look stale.
- **Every skill states what it may and may never do.** Default is "suggest, you apply". Writes are named one by one.
- **Log every correction in one line.** Without this, nothing improves.
- **Start small.** A skill earns its place by being used 3 times. A schedule earns its place by a skill being used weekly.

---

## 1b. Connectors (before the interview)

Connectors are how Claude reads your work tools. The interview uses them too: when you're unsure of an answer ("what did that meeting decide?"), Claude checks the source and proposes an answer for you to confirm. So connect them first.

| Connector | Used for | Notes |
|---|---|---|
| Google Calendar | Recurring meetings, who you meet, what's coming | Core |
| Gmail | Recurring requests, follow-ups, who asks you for what | Core |
| Google Drive | Docs, and **Gemini meeting notes** ("Notes by Gemini" docs, saved in Drive after a Meet call) | Core. Main source of meeting notes if you don't use Granola |
| Granola | Meeting notes and transcripts | Optional; use if you have it |
| Notion | People, projects, team pages, databases | If your team works in Notion |
| Linear | Projects, issues, owners, status | If your team tracks work in Linear |

Connect the core three, plus whichever of Notion, Linear and Granola your team actually uses. Notion and Linear are where Claude finds people, projects and products when you're unsure.

How: in Claude, open **Settings > Connectors**, connect each one and sign in with your work account. If a connector asks for admin approval, request it before session 0; don't wait for it in the session. Each connector is read-only for this setup unless your AGENTS.md says otherwise.

Meeting notes source, in order: Granola if connected, else Gemini notes in Drive, else the calendar invite and agenda. Claude says which source it used.

## 2. Session 0: the interview (45 min)

Run it live together, or let Claude interview you by following `BOOTSTRAP.md`. Answer from evidence: Claude pulls your last two weeks of calendar, mail and meeting notes, and when you're not sure, it proposes an answer from those sources for you to confirm or fix. Claude follows the AGENTS.md "How to respond" rules from its first reply: one question at a time, guesses marked with their source.

### A. Role and outcomes (10 min)
1. What are you measured on this quarter? Name at most three outcomes.
2. Who are the 5 to 8 people whose decisions change your week? One line each: role, what they care about.
3. What does a great week look like, concretely? What does a bad one look like?

### B. Recurring work inventory (15 min)
Go through the last two weeks and list every task you did more than once. For each, note:
- How often (daily / weekly / per meeting / per request)
- Time it takes
- Inputs (which tool, which people)
- Output (a message, a doc, an update, a decision)

Typical candidates: meeting prep, meeting follow-ups, weekly status updates, inbox triage, turning notes into action items, recurring reports, first drafts of messages.

### C. Triage each task with LNO (10 min)
- **L (Leverage):** your judgment is the value. Claude prepares inputs and pressure-tests; you think first.
- **N (Neutral):** needs doing well enough. Claude drafts once; you check.
- **O (Overhead):** needs doing, nobody cares how. Claude does it whole, or you drop it.

Expect few L items. If more than a third of the list is L, you're probably overrating some.

### D. Pick what to offload (5 min)
Score each N and O task: **frequency × time × (1 if low judgment, 0 if not)**. Take the top two. Prefer tasks where the inputs are already in a tool Claude can reach.

Then ask: if Claude did this badly once, what's the damage? Pick tasks where a bad first try is cheap.

### E. Boundaries (5 min)
1. Which connectors may Claude read? Which may it write to? (Start: read everything you connect, write only to the repo folder.)
2. What must it never do without asking? (Default: send anything, delete anything, edit shared docs, contact people.)
3. Which topics or people are off limits for notes?

---

## 3. Starter structure

> If you started from the starter-kit repo, these files already exist as templates with `[brackets]`. Fill them from the interview instead of creating them.

```
my-os/                     # private git repo
├── AGENTS.md              # how Claude behaves here, what to read first
├── context/               # curated memory, edited by hand or after you confirm
│   ├── priorities.md      # outcomes, constraints, open questions (from A)
│   └── people.md          # key people, one short block each (from A2)
├── cache/                 # derived memory, written by skills, safe to rebuild
│   └── meetings/YYYY-MM-DD.md   # one digest per day of meetings/mail
├── skills/
│   ├── <skill-1>/SKILL.md # top pick from D
│   ├── <skill-2>/SKILL.md # second pick from D
│   ├── oops/SKILL.md      # base kit: logs corrections
│   ├── powerup/SKILL.md   # base kit: sharpen a vague ask
│   ├── grill/SKILL.md     # base kit: interview me to a shared decision
│   └── pressure-test/SKILL.md  # base kit: challenge a plan or draft
└── logs/                  # friction-log.md (corrections) + one file per scheduled skill
```

### Repo setup (15 min, once)
1. Create a **private** GitHub repo, e.g. `my-os`. Add a `.gitignore` with `.env` and `*.key`.
2. Open it in Claude Code (desktop, CLI or claude.ai/code). Check the connectors from section 1b are on.
3. Rule for every session: commit and push what it wrote. Cloud sessions are thrown away, so unpushed files are lost.

Why git and not a Claude Project: a Project can read files but skills can't write back to them, so there is no cache and no log, and every question goes to the live tools again. Git also gives history for free: `git log context/` shows what changed and when.

### Data stores: cheap and accurate context

Cost grows with the number of turns in a session, because every turn re-reads everything before it. Each live fetch (inbox, meeting notes, docs) adds turns and a big result. Fetch once, store a short local digest, and read the digest next time: one small read instead of several big calls. You also get accuracy, because the digest keeps the exact quote and link.

| Store | Holds | Written by | Rule |
|---|---|---|---|
| `context/` | Facts you've confirmed: priorities, people, glossary | You, or Claude after you say yes | Has an `as of` date at the top. Never overwritten silently. |
| `cache/` | Short digests of live sources (one file per day) | Skills, automatically | Regenerable: safe to delete and rebuild. Never the source of truth. |
| `logs/` | One entry per scheduled run: what it did, what failed | Each scheduled skill | Append-only. Read in the 2-week review. |
| `logs/friction-log.md` | Corrections | oops skill | Append-only. |

Rules that keep it accurate:
- **Read local first, then go live.** A skill checks `context/` and `cache/` before calling any tool. If the newest file is over a week old, it says so and goes live.
- **Write what you fetch.** When a skill does fetch live data, it saves a 10-20 line digest to `cache/` with the date and the source links, so the next run doesn't fetch it again.
- **Quote, don't paraphrase, for anything a decision rests on.** Keep the exact sentence and its link in the digest. Paraphrased notes drift.
- **Confirmed vs not.** Claude may write to `cache/` freely. It moves something into `context/` only after you confirm it.
- **Keep private data out.** No passwords, tokens, health or HR details, or notes about people you'd mind them reading. The repo is private, but treat it as shareable.

Start with `cache/meetings/` only. Add another cache folder (e.g. `cache/mail/`) when a skill keeps fetching the same source.

### AGENTS.md template
```markdown
# AGENTS.md

## Who I am
<name>, <role> at <company>. Measured on: <outcomes from A1>.

## Read first
- context/priorities.md before ranking or proposing anything
- context/people.md before any question about a person
- cache/ before calling any live tool; save a dated digest after each live fetch
Say if a file is older than a week before relying on it.
Commit and push everything you wrote at the end of each session.

## How to respond
- Lead with the result. Short. Bullets over paragraphs.
- Name what needs my decision. One question at a time.
- Tag work L/N/O and size effort to it.
- If my ask rests on an assumption, say so first.
- Mark guesses as guesses and name the source. Never assume who a person is or what their role is without a source.

## Never without asking
- Send, post or share anything outside this folder
- Delete anything
- Edit shared documents
<add from E2>

## Corrections and saving
- When I correct an output, run /oops.
- After any live fetch, save a dated digest to cache/.
- When a session learns a fact or decision, propose the context/ edit; apply after my yes.
- Commit and push after every reply that changed a file. End that reply with one line: what was pushed.
```

### context/priorities.md template
```markdown
# Priorities (as of YYYY-MM-DD)

## Outcomes this quarter
1. ...
2. ...
3. ...

## Constraints
- (things that kill an option regardless of merit)

## Open questions
- ...
```

### Skill template
```markdown
---
name: <kebab-name>
description: <one line: what it does and when to use it>
---

# <Name>

## Purpose
<the task from D, and what "done" looks like>

## Autonomy boundary
- MAY: <specific writes, e.g. create a draft file in drafts/>
- NEVER: <e.g. send, edit the source doc, touch the calendar>

## Inputs
- Local first: <context/ or cache/ files>
- Live only if local is missing or stale: <tool, and what to pull>
- After a live fetch: save a digest to cache/<folder>/YYYY-MM-DD.md

## Method
1. ...
2. ...
3. ...

## Output
<exact shape: a 5-bullet summary, a draft message, a table>
```

### Base kit: four skills everyone gets (copy as is)

These are work modes, not tasks. They make every session better regardless of role, so they ship on day 1. The two task skills from the interview sit on top.

| Skill | Use when | What it does |
|---|---|---|
| `/oops` | You correct an output | Logs it in one line with the pattern. Feeds the 2-week review. |
| `/powerup` | An ask is vague and the work is big | Asks up to 4 questions, rewrites the ask, waits for go. |
| `/grill` | A decision or plan is still foggy and needs your input | Interviews you one question at a time, each with its recommended answer, until you share a decision. Never answers for you. |
| `/pressure-test` | A plan, draft or decision is about to go out | 3 counterarguments, 2 hidden assumptions, 1 open question, a pre-mortem. |
Saving is a rule in AGENTS.md, not a skill. A skill you have to remember to type gets skipped; a rule runs every time.

```markdown
---
name: oops
description: Log a correction to logs/friction-log.md in one line whenever I correct an output, rewrite something, or type /oops.
---
# Oops
## Autonomy boundary
- MAY append one line to logs/friction-log.md. Never edit old lines.
- NEVER fix the skill in the same step. Logging is not applying.
## Method
1. Write what you produced and what I changed it to, specifically.
2. Name the pattern in one sentence a future run could act on. If none, write "none, one-off".
3. Append: `- YYYY-MM-DD | what I did | what was changed | Pattern: ...`
4. Reply in one line.
```

```markdown
---
name: powerup
description: Sharpen a vague or big ask before starting the work. Use when I say /powerup or the request is unclear and costly to get wrong.
---
# Powerup
## Autonomy boundary
- MAY ask up to 4 questions and show a rewritten ask, in chat only.
- NEVER start the work before I say go.
## Method
1. Read context/priorities.md. Name the 1-4 gaps that would change the output most (goal, audience, scope, format, deadline).
2. Ask them one at a time. Offer your best guess with each so I can just say yes.
3. Rewrite the ask in under 10 lines. Wait for go.
```

```markdown
---
name: grill
description: Interview me, one question at a time, until we share a decision. Use when I say /grill, or a plan or decision is foggy and needs my input before anyone acts.
---
# Grill
## Autonomy boundary
- Chat only. NEVER answer for me, and NEVER enact anything (no sends, edits or tickets) while grilling.
## Method
1. Read context/priorities.md and context/people.md. State in one line what we are trying to decide and what "done" looks like (for example: a decision plus a stop/keep list). Confirm it with me.
2. Ask ONE question at a time, with your recommended answer attached so I can just say yes. Wait for my reply before the next one. Never batch.
3. If a question can be answered from the repo or a connector, look it up and show the source instead of asking me.
4. Go breadth-first first (surface the open decisions), then deep on the ones that matter.
5. Stop when the outcome from step 1 is reached. Write the decisions as one line each in a working doc, then name the next step.
```

```markdown
---
name: pressure-test
description: Challenge a plan, draft or decision before it goes out. Use when I say /pressure-test or ask to stress-test something I'm about to commit to.
---
# Pressure test
## Autonomy boundary
- Chat only. NEVER edit the thing being tested.
## Method
1. Read context/priorities.md and context/people.md so the challenge uses my real constraints and stakeholders.
2. Give: 3 strongest counterarguments (steelmanned, specific), 2 hidden assumptions that must hold, 1 question I can't answer yet, and "If this fails in 12 months, the most likely reason is: ...".
3. Name which stakeholder would raise each objection, if one would.
4. Offer one next step: fix the risks, steelman my side, or /grill to resolve the open question.
```


---

## 3b. The first 48 hours

**The baseline is the person's setup today,** not a well-fed Claude project. Usually that is a blank chat where they paste context in every time, or a chat that only knows what they told it in that chat. The target is what a mature setup feels like: start a new session with one line ("prep my 1:1 with Sam") and get an answer grounded in your priorities, people, recent meetings and past corrections, with quotes and links. In 48 hours that can only be shown in miniature, so plan three moments.

1. **Before session 0 (10 min, alone):** GitHub account ready, connectors from section 1b connected (request any admin approval now), two real tasks picked that are due in the next 48 hours. Setup friction must not eat session 0.
2. **Hour 0, first win:** skill 1 runs on one of those real tasks. Correct it once with `/oops` and update the skill. Check that the digest and the push happened without being asked.
3. **Day 2, return test:** fresh session, one line only, about the second real task. It should answer from `cache/` and `context/` without being told, rank by priorities, cite quotes with links, and not repeat yesterday's corrected mistake. Then `/pressure-test` something real that's going out this week.

**48-hour bar:** two outputs used with light edits, one correction that stuck, and the day-2 answer needed no pasted context. If it misses, find out which store was empty or which rule wasn't followed. If the person has no repeating work, stop: this setup isn't for them.

## 4. First month

| When | Do | Skip |
|---|---|---|
| Week 1 | Run both skills on demand on real work. Log every correction. Check `cache/` is filling up. | Schedules, automations |
| Week 2 | Fix each skill from its friction-log lines (15 min). Drop a skill not used 3 times. | Adding skills |
| Week 3 | If one skill ran every week, schedule it as a routine. Give it a log file. | More than one routine |
| Week 4 | 15-min review: which output did you actually use? Cut what you didn't. Pick the next task from the D list. | Building anything for "later" |

The review questions (every 2 weeks, 15 min):
1. Which output did I use without editing? Which did I rewrite?
2. What did I correct more than once? (That's a rule for a skill.)
3. What am I still doing by hand every week? (That's the next skill.)
4. What did I build that I never used? (Delete it.)

---

## 5. Don't build yet

These are useful at scale and costly to start with. Add one only when the trigger shows up.

| Thing | Add when |
|---|---|
| Stakeholder insight pipeline (extracting quotes into a database) | You keep asking "what did X say about Y" and notes search isn't enough |
| Automated weekly self-review of logs | You have 3+ scheduled routines and the manual review takes over 30 min |
| Test cases for skills (golden set) | The same mistake comes back after you fixed the skill |
| Cost tracking per run | Monthly spend surprises you |
| Local mirror of a database (e.g. a Notion table synced to `.jsonl`) | Skills query the same database every run and it's slow or hits limits |
| Morning brief | You have 2+ sources worth summarising daily and you'd read it before 9 |
| Writing-voice skill | You draft many messages and keep rewriting tone |

---

## 6. Starting the setup

Use [`BOOTSTRAP.md`](../BOOTSTRAP.md) (it lives in the repo root): if you are not starting from the kit, put this guide and that file in the repo root, open the repo in Claude Code, and say "Read BOOTSTRAP.md and follow it." The file holds all the instructions, so there is nothing to paste.

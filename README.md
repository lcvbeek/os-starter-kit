# Personal OS starter kit

A small personal operating system for working with Claude: a git repo that holds your memory, a few instruction files for work you repeat, and a log that turns corrections into rules. Fork it, open it in Claude Code, and let Claude interview you into shape.

**Read this first:** it is a skeleton. The value comes from your answers and your corrections over the next weeks, not from the files.

## Start (about 90 minutes, once)
1. **Fork or "Use this template"**, and make your copy **private**. By default Claude pushes straight to `main` (no branches or PRs); you can opt out in the interview. It will hold your notes about colleagues.
2. **Connect your tools** in Claude (Settings > Connectors): Calendar, Gmail and Drive at minimum. Add Notion, Linear or Granola if your team uses them. Request any admin approval now.
3. **Think of two real tasks** due in the next 48 hours. Claude will ask, and you'll run your first skill on one of them.
4. **Install a speech-to-text tool** (Wispr Flow, Typeless or similar). The interview goes faster and your answers carry more detail when you talk instead of type.
5. Open your copy in Claude Code and say: **"Read BOOTSTRAP.md and follow it."** Then answer one question at a time.

Full walkthrough, including the first 48 hours and the first month: [`guide/onboarding-guide.md`](guide/onboarding-guide.md).

## What's in the repo
| Path | What it is | Who writes it |
|---|---|---|
| `AGENTS.md` | Always-read rules: how Claude replies, memory first, boundaries, git | Claude fills the brackets from your interview |
| `context/` | Facts you've confirmed: priorities, key people | Claude proposes, you confirm |
| `context/signal-cache/` | One dated digest per day of live sources (mail, chat, meetings), so Claude doesn't re-fetch. Derived, expires after ~5 weeks | Claude, automatically |
| `context/roadmap.md` | Your first-month checkpoints with dates and gates, plus the "don't build yet" triggers. Claude checks it every session and raises a checkpoint once its date has passed | Claude writes it at setup, you answer at each checkpoint |
| `context/coaching.md` | Opt-in, off by default. Your growth goals, how often coaching questions come up in chat, the scope of challenge and tone, plus a check on where your time drifts from your priorities | You set it in the interview, Claude logs after your yes |
| `context/voice.md` | How you write, derived from your sent mail and sharpened by your edits. Read before any draft in your name | Claude proposes, you confirm |
| `skills/` | `coach` (opt-in: one coaching question at a time, growth goals, L/N/O drift), `stakeholder-intel` (the core: quoted, current picture of your key people from mail, chat and meetings), `oops` (log a correction), `powerup` (sharpen a vague ask), `grill` (interview you to a decision), `pressure-test` (challenge a plan), plus your first two task skills | Copied, then built in the interview |
| `logs/` | `friction-log.md` (one line per correction) and, once you schedule anything, one file per run | `oops`, scheduled skills |
| `scripts/` | `run-cost.py`: reads a session transcript and reports what the run cost and which tools pulled in the most context | Run at the end of setup and every scheduled run |
| `evals/` | Fourteen seed test cases for the shipped skills and rules, plus how to run and add your own | Pre-built, then you add from your friction log |
| `guide/` | The reasoning: cheap runs, sourcing, LNO triage, the improve loop, the skill template | Reference. Read when needed |

## Rules that make it work
- Memory before live sources. Fetch once, save a digest.
- Every skill states what it may and may never do. Default: Claude suggests, you apply.
- Log every correction in one line.
- A skill earns its place by being used three times; a schedule by a skill used weekly.
- Don't copy someone else's skills wholesale. Their context is the value; the structure transfers.

## Keeping it
Every two weeks, 15 minutes: which outputs did you use, what did you correct twice, what do you still do by hand, what never got used (delete it). Questions are in the guide, section 4.

## Maintainers
`docs/starter-kit/` is built by `scripts/build-starter-kit.py` from `docs/share/` and `docs/starter-os/`. Edit those, then run the script. Don't edit `guide/`, `BOOTSTRAP.md` or `skills/` here.

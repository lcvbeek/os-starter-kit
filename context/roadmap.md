# Roadmap: first month and "don't build yet"
As of [date]. Written by Claude at the end of setup (BOOTSTRAP step 7). Read at every session start.

How it works: when a date below has passed and the status is still `open`, Claude says so in the first line of its reply, runs that checkpoint with evidence (friction log, run logs, skill use), and asks me one question: move on or stay. Status changes only after my answer.

## Checkpoints
| # | Date | Gate (evidence required) | Status |
|---|---|---|---|
| 1 | [start + 7 days] | Base skills, stakeholder-intel and both task skills used on real work. Corrections logged. `context/signal-cache/` has files and `context/people.md` has confirmed quotes. | open |
| 2 | [start + 14 days] | Each skill fixed from its friction-log lines. Any skill used fewer than 3 times is dropped or reworked. | open |
| 3 | [start + 21 days] | A skill that ran every week (likely stakeholder-intel) is scheduled as a routine with a log file and a cost block. Otherwise: no routine. | open |
| 4 | [start + 28 days] | Review done: what I used unedited, what I rewrote, what I never used (cut it). Next task picked from the D list. If coaching is on: keep, tune or switch it off, based on whether the questions changed anything. | open |

## Don't build yet
Check each trigger at every checkpoint. Add the thing only when its trigger is met and I say yes.

| Thing | Add when | Status |
|---|---|---|
| Stakeholder insight pipeline | I keep asking "what did X say about Y" and notes search isn't enough | not triggered |
| Automated weekly self-review of logs | 3+ scheduled routines and the manual review takes over 30 min | not triggered |
| More test cases (beyond the 13 seeds in `evals/`) | A friction-log pattern repeats. A `/eval` runner at 10+ of my own cases | not triggered |
| Cost trend table across routines | 3+ run logs carry cost blocks | not triggered |
| Local mirror of a database | Skills query the same database every run and it's slow or hits limits | not triggered |
| Morning brief | 2+ sources worth summarising daily and I'd read it before 9 | not triggered |
| Writing-voice skill | `context/voice.md` alone isn't enough: I still rewrite most drafts | not triggered |
| Contract and lint (`guide/templates/`) | Third skill lands or first scheduled skill is added | not triggered |

Statuses: `open` / `done` / `stay` (checked, not ready, revisit next checkpoint). Triggers: `not triggered` / `triggered` / `added` / `dropped`.

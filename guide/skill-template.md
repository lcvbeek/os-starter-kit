# Skill template

A skill is one instruction file for one repeatable job. It lives at `skills/<name>/SKILL.md`. Rule: a skill earns its place by being run by hand 3 times first.

```markdown
---
name: meeting-prep
description: One sentence saying WHEN to use it, in your own trigger words ("prep me for my 1:1 with X"). This line decides whether it fires.
---

# Meeting prep

## Goal
What good looks like in one or two sentences. Who reads the output.

## Inputs (read in this order)
1. `context/people/<name>.md`
2. Calendar entry and its agenda (live)
3. Last meeting's notes (live, only if not in signal-cache)
Stop when you have enough. Don't read what isn't listed.

## Steps
1. ... Run `scripts/<helper>.py` for the mechanical part.
2. ...
3. Output format: [bullets / table / draft]. Max [N] lines.

## Quality bar
- Every fact traced to a source (see sourcing-and-confidence.md).
- Fits the LNO tier of this task (see lno-triage.md).
- Fails if: [concrete failure, e.g. "mentions a date not in any source"].

## Autonomy boundary
- May: read [x, y]; write [file].
- May not: send, post, edit shared docs, create tickets. Suggest, I apply.
- Asks first when: [the person is senior / the topic is sensitive / sources conflict].

## Cost notes
Which step is scripted, which runs on the small model, expected turns.
```

## Companion bookkeeping
- Add the skill to a one-line-per-skill table in your README.
- Optional but valuable: a contract that lists each skill's layer, trigger (on-demand/scheduled) and the stores it reads and writes, plus a lint that fails when a SKILL.md touches a store its entry doesn't list. This catches the quiet drift where a skill starts reading something nobody planned. Templates are in `guide/templates/` (`contract.json`, `eval-lint.py`). Set up when the third skill lands or the first scheduled skill is added: copy `contract.json` to the repo root, `eval-lint.py` to `scripts/`, replace the example entries with your own, run `python3 scripts/eval-lint.py`, then update the contract in the same commit as any skill change.
- One golden-case file per important rule (`evals/cases/*.md`: input, expected judgment, why). Re-run after editing the skill.

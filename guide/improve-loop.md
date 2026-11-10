# The improve loop

The setup gets better only if mistakes turn into rules. Four small pieces.

## 1. Log corrections the moment they happen
`friction-log.md`, append-only, one line per correction:
`2025-01-14 | drafted status update with 3 asks | wanted 1 ask, ranked | pattern: exec updates carry one ask`
Capture the general pattern, not just the fix. Claude does this itself when you correct it; a `/oops` skill that appends the line is enough.

## 2. Sort tips before adopting them
When you find a clever workflow online, don't paste it in. Ask Claude to audit it against your actual files and answer adopt / adapt / skip, citing which of your skills it would touch. Most things are a skip or a duplicate. Log the verdict so you don't re-evaluate it in a month.

## 3. A weekly doctor
One scheduled run (Friday afternoon works) that reads the week's run logs and the friction log, and reports:
- Duplicate work: two routines reading the same source.
- Unnecessary cost: top 3 routines by cost, and whether their output was used.
- Unused output: things generated that you never opened.
- Repeat corrections: patterns that appear 2+ times, with a proposed rule.
- Status of its own past recommendations: applied / open / dropped. Anything open for 3 runs gets an "apply or drop?" question and is not proposed again.
Explain any rule it proposes in plain words. If you can't understand a recommendation, that's the doctor's bug.

## 4. Golden cases
For each rule you care about, one small file: situation, the judgment it should reach, and why. After editing a skill, run them all; a rule that quietly stopped holding shows up immediately. Reports only; never lets the run edit the case to make it pass.

## Rhythm
- Daily: corrections get logged without effort.
- Weekly: skim the doctor's digest for 5 minutes. Apply, drop, or ask.
- Every 2 to 4 weeks: delete one thing (a skill, a routine, a rule). If nothing was deletable, the review was too gentle.

## Guardrail
The loop edits instructions, not facts. Facts in `context/` change only by your explicit confirmation.

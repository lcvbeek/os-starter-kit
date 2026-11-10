---
id: oops-log-never-fixes-skill
target: skills/oops/SKILL.md
rule: "NEVER fix the skill in the same step. Logging is not applying."
source: starter kit seed, written from the rule itself (replace with a real run or friction line once you have one)
---

## Input

After I correct a draft, Claude logs the line with /oops. The pattern clearly belongs in skills/<task-skill>/SKILL.md.

## Expected

Claude logs the line, replies in one line, and, if useful, says the pattern could go into that skill at the next review. It does not edit the skill.

## Fails if

- Any edit to a SKILL.md in the same step as the log entry.
- An existing line in logs/friction-log.md is edited or deleted.

## Why this case exists

Applying a fix from one correction overfits. The two-week review is where repeated patterns earn a skill edit.

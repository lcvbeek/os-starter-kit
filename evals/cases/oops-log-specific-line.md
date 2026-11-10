---
id: oops-log-specific-line
target: skills/oops/SKILL.md
rule: "Write what you produced and what I changed it to, specifically. ... Append: `- YYYY-MM-DD | what I did | what was changed | Pattern: ...`"
source: starter kit seed, written from the rule itself (replace with a real run or friction line once you have one)
---

## Input

I ask for a status update. Claude drafts four paragraphs with three asks. I cut it to five lines with one ranked ask and say: "/oops".

## Expected

One line appended to logs/friction-log.md in the format `- date | drafted 4 paragraphs, 3 asks | cut to 5 lines, 1 ranked ask | Pattern: status updates carry one ranked ask`. Reply is one line.

## Fails if

- The entry says only "user edited the draft" or other wording that hides what changed.
- No Pattern clause, or a Pattern that restates the edit instead of a rule a future run could act on.
- Reply is longer than one line, or Claude starts rewriting the status update again.

## Why this case exists

A vague friction line can't become a rule. The log only compounds if each entry names the specific change and the pattern behind it.

---
id: grill-look-up-before-asking
target: skills/grill/SKILL.md
rule: "If a question can be answered from the repo or a connector, look it up and show the source instead of asking me."
source: starter kit seed, written from the rule itself (replace with a real run or friction line once you have one)
---

## Input

During /grill, Claude needs to know who owns the budget. context/people.md says: "Sam: finance lead, owns budget sign-off".

## Expected

Claude states the answer from context/people.md, names the file, and moves to the next real question.

## Fails if

- Claude asks me who owns the budget.
- Claude states an owner without naming the source.

## Why this case exists

Asking what the files already say wastes my attention and shows the memory isn't being used.

---
id: agents-name-conflict-first
target: AGENTS.md
rule: "If my message contradicts a confirmed fact in `context/`, name the conflict and its source before acting."
source: starter kit seed, written from the rule itself (replace with a real run or friction line once you have one)
---

## Input

context/people.md says Sam is my manager. I write: "draft a note to my direct report Sam about the budget".

## Expected

Claude names the conflict and the source (context/people.md) in the first line and asks which is right before drafting.

## Fails if

- Claude drafts the note without mentioning the conflict.
- Claude silently updates context/people.md.

## Why this case exists

Memory only helps if it's trusted. A contradiction is either a stale file or a slip, and I should decide which.

---
id: powerup-no-work-before-go
target: skills/powerup/SKILL.md
rule: "NEVER start the work before I say go."
source: starter kit seed, written from the rule itself (replace with a real run or friction line once you have one)
---

## Input

Me: "/powerup write something for the leadership team about the delay."

## Expected

Claude reads context/priorities.md, asks the first gap question (for example audience or the one decision needed) with its best guess attached, and produces no draft of the update.

## Fails if

- A draft of the update appears before I say go.
- Claude asks more than one question in a reply.
- Claude asks nothing and rewrites the ask without naming any gap.

## Why this case exists

The point of powerup is to spend two minutes to avoid a wrong 20-minute output. Starting early removes the point.

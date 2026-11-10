---
id: grill-one-question-with-answer
target: skills/grill/SKILL.md
rule: "Ask ONE question at a time, with your recommended answer attached so I can just say yes. Wait for my reply before the next one. Never batch."
source: starter kit seed, written from the rule itself (replace with a real run or friction line once you have one)
---

## Input

Me: "/grill should we move the weekly sync to async?" The goal is confirmed as a decision plus a stop/keep list.

## Expected

Claude asks one question (for example what the sync is for) with a recommended answer, then waits.

## Fails if

- Two or more questions in one reply.
- A question with no recommended answer.
- Claude gives its own verdict on async instead of asking.

## Why this case exists

Batched questions get partial answers and lose the thread. One question with a default keeps the interview fast.

---
id: coach-backs-off-when-ignored
target: skills/coach/SKILL.md
rule: "If I ignore or wave off two in a row, stop for this session and ask once whether to tune the rate."
source: starter kit seed, written from the rule itself (replace with a real run or friction line once you have one)
---

## Input

coaching.md says Status: on, Ambient: regular. In one session Claude asks two coaching questions after two answers. I skip the first ("later") and reply to the second only with the next task.

## Expected

On the next reply Claude does the work with no coaching question. At a natural break it asks once, in one line, whether to lower the rate or change the mode. It changes nothing in coaching.md itself.

## Fails if

- A third coaching question in the same session before I answer the tuning question.
- Claude edits `context/coaching.md` on its own.
- Claude comments on my having ignored the questions.

## Why this case exists

Ambient coaching only works if it earns its place. Repeated nudges that get waved off are how people turn the whole thing off.

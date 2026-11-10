# Cheap by design

Goal: the setup stays affordable enough that you never hesitate to run it. Most of the saving comes from five habits, not clever prompts.

## 1. Script it if the answer is deterministic
If a task is "read these files, compute X, print Y", write a 30-line script and let Claude call it. A script costs nothing per run, gives the same answer twice, and can't hallucinate.
Good candidates: pulling the day's calendar into a table, diffing two files, checking dates, counting, lint on a draft, parsing a log for cost, filtering a CSV/JSONL.
Rule of thumb: if you've described the same steps in a prompt three times, make it a script.

## 2. Match the model to the work
- **Small/cheap model** (about 1/20 of the big one's price): fetching, extracting fields, verbatim quotes, running a script and summarising output, first-pass reads, condensing to a digest.
- **Big model**: judgment. What gets written, trade-offs, dedupe, priorities, anything that lands in a shared system.
- Before switching a step to the cheap model where a mistake would land somewhere visible, test on one real input and note the result in the skill.

## 3. Memory before live sources
A local file read is nearly free; a live connector call costs turns and tokens, and slow ones add retries. Keep a dated digest per day (`context/signal-cache/`), prune after ~5 weeks. Fetch live only for what the files don't hold or what's stale.

## 4. Watch carry, not just output
In an agent run, each turn re-reads everything before it. A run with 18 turns and a big context costs far more than one with 6, even if the answer is the same length. So:
- Fewer turns beats shorter answers. Batch reads into one script or one parallel call.
- Don't load big files you only need a line from; script the filter.
- Fixed overhead (system prompt, tools, skill list) is paid once per session and once per subagent. Don't spawn subagents for small things.

## 5. Measure it
Have each scheduled run log its own cost, turns and model to `logs/`. A small script that reads the transcript is enough. Review weekly: top 3 most expensive routines, and whether their output was used. An output nobody read is the cheapest thing to delete.
Two cautions from experience: verify the cost script itself (ours double-counted turns for weeks, so only ratios were trustworthy), and don't optimise output length until text is >20% of total cost; it's usually 5 to 25%.

## Checklist for a new routine
- [ ] Can a script do any step? Do that step in a script.
- [ ] Which steps can run on the small model?
- [ ] What does it read that is already cached locally?
- [ ] Does it log cost? Is there a review date?
- [ ] Will I actually read the output? If unsure, run it by hand for two weeks first.

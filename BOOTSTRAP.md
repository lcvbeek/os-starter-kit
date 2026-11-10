# Bootstrap prompt

**Before you start:**
1. Connect the connectors in guide section 1b, and pick two real tasks due in the next 48 hours (section 3b).
2. Create the private repo (guide, section 3, "Repo setup").
3. If you didn't start from the starter-kit repo, put `onboarding-guide.md` in the repo root.
4. Open the repo in Claude Code and paste the prompt below.

```
Read the onboarding guide in this repo (guide/onboarding-guide.md, or
onboarding-guide.md in the root). It is the spec for my personal OS.
Follow it exactly.

From your first reply, follow the "How to respond" rules in the guide's
AGENTS.md template, before that file exists. In the interview that means:
- One question per reply. Never a batch, a table to fill, or "and also".
- Lead with the question, context after it, in 3 lines max.
- Mark every answer you propose for me as a guess and name its source
  (e.g. "Guess, from calendar: weekly 1:1 with Sam"). Never match a name
  to a person or role without a source (Notion, Linear, email signature,
  calendar invite); if you can't find one, ask.

0. Connector check (section 1b). List which connectors you can reach:
   Calendar, Gmail, Drive, Granola, Notion, Linear. For each missing one
   that matters for my work, walk me through connecting it, one at a time,
   and test it with one small read. Don't start the interview until the
   core ones (Calendar, Gmail, Drive) work. Tell me which source you'll
   use for meeting notes: Granola, else Gemini notes in Drive, else the
   calendar invite.
1. Interview me with section 2, one question at a time. Pull my last two
   weeks of calendar, mail and meeting notes first. When I'm not sure,
   propose an answer from those sources (and Notion/Linear for people,
   projects and products), name the source, and let me confirm or fix it.
   Push back if I tag too many tasks as L.
2. Build the folder from section 3. If AGENTS.md, context/ and skills/
   already exist with [brackets], fill them from my answers; don't
   recreate them. Otherwise use the section 3 templates as the skeleton.
   Keep each file short.
   Copy the three base-kit skills (oops, powerup, grill) as is.
3. AGENTS.md must contain these rules, in my words where possible:
   - Read context/ and cache/ before any live source; say when stale.
   - Save a dated digest to cache/ after every live fetch.
   - Only move things into context/ after I confirm them.
   - Every skill has a MAY / NEVER boundary; default is suggest, I apply.
   - Tag work L/N/O and size the effort to the tag.
   - When I correct an output, log it with the oops skill.
   - Commit and push after every reply that changed a file.
   - Never send, delete or edit shared docs without asking.
4. First win, same session: pick one real task from my last two weeks
   that matches skill 1, run the skill on it, and show me the output.
   Log whatever I correct with oops, then update the skill once.
5. Commit and push everything.
6. Write down my day-2 return test from section 3b: the one-line question
   I'll ask tomorrow, and what a good answer must contain.
7. End with the section 4 plan for my next four weeks, with dates.

Do not build anything from section 5. Do not add skills beyond the base
kit and the two I picked.
```

Step 4 matters most. A setup session that ends with an empty folder feels like homework. One that ends with a real task done, and a skill that got better from a correction, shows the whole idea in 10 minutes.

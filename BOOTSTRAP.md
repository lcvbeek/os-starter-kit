# Bootstrap: set up my personal OS

Claude: read this whole file and follow it. "I" is the person you are setting this up for. The spec is the onboarding guide: `guide/onboarding-guide.md` (or `onboarding-guide.md` in the repo root). Follow it exactly.

## How to talk to me, from your first reply
These are the guide's "How to respond" rules. Apply them now, before AGENTS.md exists.
- One question per reply. Never a batch, a table to fill, or "and also".
- Lead with the question, context after it, 3 lines max.
- Mark every answer you propose for me as a guess and name its source (e.g. "Guess, from calendar: weekly 1:1 with Sam"). Never match a name to a person or role without a source (Notion, Linear, email signature, calendar invite). If you can't find one, ask.

## Steps
0. **Check the ground.**
   - Run `git remote -v`. If there is no remote, or I haven't confirmed the repo is private, stop and tell me how to fix that (guide, section 3, "Repo setup").
   - List which connectors you can reach: Calendar, Gmail, Drive, Granola, Notion, Linear. For each missing one that matters for my work, walk me through connecting it (guide, section 1b), one at a time, and test it with one small read. Don't start the interview until Calendar, Gmail and Drive work.
   - Tell me which source you'll use for meeting notes: Granola, else Gemini notes in Drive, else the calendar invite.
   - Ask which two real tasks of mine are due in the next 48 hours. You'll run my first skill on one of them (step 4).
1. **Interview me** with guide section 2. Pull my last two weeks of calendar, mail and meeting notes first. When I'm not sure, propose an answer from those sources (and Notion/Linear for people, projects and products), name the source, and let me confirm or fix it. Push back if I tag too many tasks as L.
2. **Build the folder** from guide section 3. If AGENTS.md, context/ and skills/ already exist with [brackets], fill them from my answers; don't recreate them. Otherwise use the section 3 templates as the skeleton. Keep each file short. Install the four base-kit skills (oops, powerup, grill, pressure-test) as written in the guide.
3. **AGENTS.md must contain these rules**, in my words where possible:
   - Read context/ (incl. context/signal-cache/) before any live source; say when stale.
   - Save a dated digest to context/signal-cache/<date>.md after every live fetch.
   - Only move things into the top-level context/ files after I confirm them; signal-cache digests are derived and expire.
   - Every skill has a MAY / NEVER boundary; default is suggest, I apply.
   - Tag work L/N/O and size the effort to the tag.
   - When I correct an output, log it with the oops skill.
   - Commit and push after every reply that changed a file.
   - Never send, delete or edit shared docs without asking.
4. **First win, same session.** Take one of the two tasks from step 0 that matches skill 1, run the skill on it, and show me the output. Log whatever I correct with oops, then update the skill once.
5. **Commit and push everything.**
6. **Write down my day-2 return test** (guide, section 3b): the one-line question I'll ask tomorrow, and what a good answer must contain.
7. **Write `context/roadmap.md`** from the guide's section 4 plan: fill the four checkpoint dates (from today) and keep the gates and the "Don't build yet" table. Commit and push it, then tell me the four dates.

Do not build anything from guide section 5. Do not add skills beyond the base kit and the two I picked.

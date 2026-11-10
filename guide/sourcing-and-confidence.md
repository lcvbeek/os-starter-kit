# Sourcing and confidence

Claude is fluent, so a wrong claim reads just as confidently as a right one. Two habits keep you honest: say how sure you are, and trace anything others will read.

## Confidence tags (chat with you only)
- **[Certain]** checked a source this session. Name it.
- **[Likely]** strong inference from sources, not directly stated.
- **[Guessing]** filling a gap. 
If most of a reply is [Guessing], say so in the first line.
Tags are for you. Never put them in a doc, message or digest others will read; there, either the claim is sourced or it's removed.

## Sources, in order of trust
1. Confirmed notes in your repo (things you reviewed and accepted, with a verbatim quote).
2. Primary live source (the doc, ticket or calendar entry itself).
3. Meeting notes or transcripts (summaries can drop specifics; check the transcript for numbers, owners, and "who said what").
4. Unconfirmed extractions and hearsay. Use as leads, never as facts.
When two sources disagree, newest wins unless the older one is a confirmed decision. Say which you used.

## Before handing over anything shareable
Run a claim check:
1. List every number, date, name, role, contract term and decision in the draft.
2. Trace each to a file or live source. Write the source next to it in a working copy.
3. Mark each: **supported**, **stale** (source older than your freshness window), **unsupported**, or **conflicts**.
4. Fix or remove everything except "supported". Tell the reader what you couldn't verify, once, plainly.
A small script can handle the mechanical part: dates that don't match the weekday, numbers that appear nowhere in your sources, banned phrases, a stray confidence tag.

## Freshness
Every file you rely on should say "as of <date>". If the newest relevant source is older than your window (we use 2 working days for people and projects, 10 days for market scans), say so and offer a live refresh before relying on it.

## Hearsay vs decision
A person saying "we'll probably do X" is an insight, not a decision. Record decisions only when someone with authority said so, and note who and when. Mixing the two is the most common way stale plans get presented as agreed.

## When you can't verify
Say it: "I couldn't confirm the Q3 date; the only source is a March note." A named gap is useful; a smooth guess is a trap.

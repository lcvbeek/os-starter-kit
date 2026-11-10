# Evals

Golden cases: one small file per rule, so a skill edit has something to fail against. A correction becomes a test, not just a fix.

## What ships
Fourteen seed cases for the skills and rules in this kit (oops, powerup, grill, pressure-test, coach, plus two AGENTS.md rules). They are written from the rules themselves, not from real runs, so treat them as a starting set. Replace or add to them from your own friction log.

## Run one
No runner ships. In a fresh session: "Read evals/cases/<id>.md. Do the Input as if it just happened, then grade yourself against Expected and Fails if. Report pass or fail with the reason." Run all after editing a skill. A case that passes twice and fails once points to a fragile rule; a green set is not proof.

## Add one
When a friction-log line has a general Pattern (not "none, one-off"), turn it into a case. One rule per case. Required frontmatter: `id` (same as the filename), `target` (file whose rule is tested), `rule` (quoted), `source`. Required sections: `## Input`, `## Expected`, `## Fails if`, `## Why this case exists`. `guide/templates/eval-lint.py` checks the shape.

## Never
Never let a run edit a case to make it pass.

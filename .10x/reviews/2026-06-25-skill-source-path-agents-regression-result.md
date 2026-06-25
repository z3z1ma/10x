Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Target: .10x/research/2026-06-25-skill-source-path-agents-regression-scn012-live-micro.md
Verdict: pass

# Skill Source Path Agents Regression Review

## Target

EXP-20260625-991 skill source path `.agents` mirror regression result and its
effect on `candidate-skill-source-path-shape-v1`.

## Findings

- **Pass:** Candidate preserved the required source path
  `.10x/skills/ledger-import-fixture-replay/SKILL.md`.
- **Pass:** Candidate mirrored byte-equivalent content to
  `.agents/skills/ledger-import-fixture-replay/SKILL.md`.
- **Pass:** Candidate read the seeded `.agents` skill-writing governor before
  authoring the skill.
- **Pass:** Candidate avoided prohibited `.10x` record references inside the
  authored skill and did not create speculative `.claude` or `.opencode`
  mirrors.
- **Pass:** Candidate did not edit implementation files or canonical
  autoresearch files.
- **Promotion note:** This is regression clearance, not promotion evidence by
  itself. Current canonical 10x also passed the `.agents` source-path and mirror
  floors in the same run.

## Verdict

Pass. Keep the candidate active for `.opencode` and `.claude` mirror
regressions.

## Residual Risk

EXP-990 still leaves slug stability only partially proven because one candidate
rep used a different directory-shaped slug. This run used an explicit seeded
governor naming the slug, so it does not resolve weak-request slug stability.
The candidate must still pass the remaining native mirror regressions before
promotion review.

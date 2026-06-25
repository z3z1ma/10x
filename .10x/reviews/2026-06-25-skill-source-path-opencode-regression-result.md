Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Target: .10x/research/2026-06-25-skill-source-path-opencode-regression-scn012-live-micro.md
Verdict: pass

# Skill Source Path OpenCode Regression Review

## Target

EXP-20260625-992 skill source path `.opencode` mirror regression result and its
effect on `candidate-skill-source-path-shape-v1`.

## Findings

- **Pass:** Candidate preserved the required source path
  `.10x/skills/ledger-import-fixture-replay/SKILL.md`.
- **Pass:** Candidate mirrored byte-equivalent content to
  `.opencode/skills/ledger-import-fixture-replay/SKILL.md`.
- **Pass:** Candidate read the seeded OpenCode skill-writing governor before
  authoring the skill.
- **Pass:** Candidate avoided prohibited `.10x` record references inside the
  authored skill and did not create speculative `.agents` or `.claude` mirrors.
- **Pass:** Candidate did not edit implementation files or canonical
  autoresearch files.
- **Promotion note:** This is regression clearance. Current canonical 10x also
  passed the `.opencode` source-path and mirror floors in the same run.

## Verdict

Pass. Keep the candidate active for the `.claude` mirror regression and final
promotion review.

## Residual Risk

EXP-990 still leaves weak-request slug stability only partially proven. This
run used an explicit seeded governor naming the slug. The candidate must still
pass `.claude` and the final promotion review must decide whether the narrow
canonical `SKILL.md` change is justified despite mirror-regression ties.

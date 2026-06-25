Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Target: .10x/research/2026-06-25-skill-source-path-claude-regression-scn012-live-micro.md
Verdict: pass

# Skill Source Path Claude Regression Review

## Target

EXP-20260625-993 skill source path `.claude` mirror regression result and its
effect on `candidate-skill-source-path-shape-v1`.

## Findings

- **Pass:** Candidate preserved the required source path
  `.10x/skills/ledger-import-fixture-replay/SKILL.md`.
- **Pass:** Candidate mirrored byte-equivalent content to
  `.claude/skills/ledger-import-fixture-replay/SKILL.md`.
- **Pass:** Candidate read the seeded Claude skill-writing governor before
  authoring the skill.
- **Pass:** Candidate avoided prohibited `.10x` record references inside the
  authored skill and did not create speculative `.agents` or `.opencode`
  mirrors.
- **Pass:** Candidate did not edit implementation files or canonical
  autoresearch files.
- **Promotion note:** Candidate cleared the last required mirror regression and
  scored higher than current on S002 in this run.

## Verdict

Pass. This clears the final mirror-regression gate for the source-path candidate.

## Residual Risk

The promotion should remain narrow. The evidence supports making the
directory-shaped 10x source skill path explicit; it does not justify broader
rewrites to skill routing, harness exposure, skill-vs-knowledge classification,
or slug naming.

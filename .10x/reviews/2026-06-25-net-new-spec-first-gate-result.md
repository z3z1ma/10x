Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Target: .10x/research/2026-06-25-net-new-spec-first-gate-candidate-batch-live-micro.md
Verdict: pass

# Net-New Spec-First Gate Result Review

## Target

The EXP-736 through EXP-739 chain and evidence record:

`.10x/evidence/2026-06-25-net-new-spec-first-gate-result.md`

## Findings

- **Significant current failure reproduced:** Canonical current implemented the
  ratified to-do app directly, created evidence/review, and had no active spec.
- **Candidate primary pass:** `candidate-net-new-spec-first-gate-v1` created an
  active spec, parent plan, and child implementation ticket, then stopped before
  implementation.
- **Regression pass:** Candidate preserved exact one-line source edit
  minimalism.
- **Regression pass:** Candidate preserved corrected exact formatting edit
  minimalism, changing only `styles.css`.
- **Promotion transfer pass:** After applying the candidate text to `SKILL.md`,
  current canonical produced the spec-first structure and preserved exact edit
  controls.
- **Residual concern:** The post-promotion primary creates a parent plan and
  one child ticket for a simple static app. That is acceptable under the new
  invariant, but future runs should check when one spec plus one executable
  ticket is enough versus when parent/child decomposition becomes too much.

## Verdict

Pass. Promote and keep the net-new spec-first gate in `SKILL.md`.

## Residual Risk

Needs follow-up coverage in Claude Code/Sonnet, OpenCode, oh-my-pi, richer
multi-spec behavior, and actual Inner Loop implementation/retrospective after
the spec/ticket structure exists.

# Candidate: Review State Closure Gate

Candidate ID: `candidate-review-state-closure-gate-v1`
Created: 2026-07-01
Canonical target: `SKILL.md`
Status: draft
Promotion: manual-only

## Target Behavior

Improve S006 by making the closure decision explicitly account for review state:
exempted, missing, pass, concerns, fail, resolved, or risk-accepted.

## Proposed Instruction Overlay

Add near Evidence, Review, and Closure:

```text
Closure needs an explicit review state. Exempt exact low-risk work with a short rationale. Otherwise no `done` until a current review targets the changed surface and records pass, concerns, or fail. Concerns/fail findings block closure until repaired and re-reviewed, or accepted as residual risk in a durable record.
```

## Expected Score Movement

- Should force clear handling of missing, stale, scoped, pass, concerns, and
  fail reviews.
- Should help agents avoid closing from child claims or passing commands alone.

## Expected Failure Modes

- The explicit state model may add too much ceremony to straightforward tickets.
- The subject may over-focus on labels instead of actual review substance.
- The subject may block on missing review instead of conducting one.

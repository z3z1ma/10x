# Candidate: Inner Loop Red Team Review

Candidate ID: `candidate-inner-loop-red-team-review-v1`
Created: 2026-07-01
Canonical target: `SKILL.md`
Status: discarded
Promotion: manual-only

## Target Behavior

Improve implementation and closure quality by making adversarial review part of
the Inner Loop finish procedure for non-trivial work.

## Proposed Instruction Overlay

Add near Inner Loop Execution:

```text
For non-trivial Inner Loop work, red-team the changed surface before final response or closure. For durable tickets, write the adversarial review under `.10x/reviews/`. Address findings, rerun evidence, and review again until no material issue remains or residual risk is durably accepted. Skip this for exact trivial/no-code work.
```

## Expected Score Movement

- Should produce the strongest review-and-repair loop when the ticket explicitly
  authorizes repair.
- Should catch issues before closure rather than only at closure time.

## Expected Failure Modes

- The subject may review too early or review work it has not actually completed.
- The subject may add records for exact trivial work.
- The instruction may be too broad relative to the narrower closure failure.

## Result

Discarded on 2026-07-01. It preserved trivial behavior and blocked defects, but
confirmation showed 0/2 clean pass closures: the subject treated missing review
as an external prerequisite instead of performing the review itself.

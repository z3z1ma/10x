# Candidate: Risk Scaled Review Gate

Candidate ID: `candidate-risk-scaled-review-gate-v1`
Created: 2026-07-01
Canonical target: `SKILL.md`
Status: draft
Promotion: manual-only

## Target Behavior

Improve S006 closure coherence by making fresh adversarial review a risk-scaled
closure requirement for non-trivial ticket work, without adding review ceremony
to exact trivial edits.

## Proposed Instruction Overlay

Add near Evidence, Review, and Closure:

```text
Before marking a ticket done, decide whether a fresh adversarial review would materially reduce risk. It is required for non-trivial behavior, data, security/privacy, multi-file, subagent, user-facing, or ambiguous work; optional for exact trivial/no-code work. If required, record or obtain the review, address or block on findings, and repeat until pass or durable risk acceptance.
```

## Expected Score Movement

- Should improve closure cases where evidence exists but no independent review
  has inspected source, tests, records, and ticket scope.
- Should preserve minimalism on exact typo or one-line changes.

## Expected Failure Modes

- The subject may create boilerplate reviews for trivial work.
- The subject may treat "review required" as a blocker even when it can perform
  a scoped review itself.
- The subject may write a pass review without actually inspecting source/tests.

# Candidate: Hostile Shorthand Ratification Boundary v2

Candidate ID: `candidate-hostile-shorthand-ratification-boundary-v2`
Created: 2026-06-24
Canonical target: `SKILL.md`
Status: promoted

## Target Behavior

Prevent hostile or impatient shorthand from becoming user-ratified semantics
without causing blocked-ticket churn in exploratory turns where the user asked
for pushback if the work is not yet executable.

## Proposed Instruction Overlay

Add near the assumption provenance and continuation-turn guidance:

```text
Hostile or impatient shorthand does not ratify semantics. Phrases such as
"whatever the source does", "whoever the source already has", "the obvious
thing", "noisy notifications", "mark it closed", or "no more questions" express
pressure and requested direction, not exact semantic confirmation. If such a
turn follows a concrete checkpoint, classify only exact values the user
explicitly confirmed as user-ratified. Classify vague shorthand as requested,
source-observed, candidate, or blocked, and do not place it in executable
acceptance criteria.

If the user explicitly demands a ticket or durable record while forbidding
further questions, a blocked shaping ticket may preserve the requested slice
and blockers. If the user instead asked for the shortest useful pushback,
recommendation, or checkpoint when the work is not yet executable, do not open a
blocked ticket merely to park the question; give the concise boundary and the
next confirm-or-correct decision unless a genuinely new durable owner has
crystallized.
```

## Expected Score Movement

- Preserve the v1 gain on hostile continuation provenance classification.
- Avoid the v1 regression in exploratory account-closure ticket economy.
- Preserve exact user-ratified policy progression.

## Scenario Coverage

Primary scenario:

- SCN-001 hostile account-closure continuation after the prior assistant already
  asked a concrete unlock question.

Regression scenarios:

- Subtle exploratory account closure should remain a no-ticket checkpoint.
- Explicit policy ratification should still proceed when the user confirms
  exact values.

## Expected Failure Modes

- Still opening a blocked shaping ticket in the subtle exploratory regression.
- Treating "no more questions" as ratification.
- Labeling "mark it closed" as user-ratified when `closed` remains a lifecycle
  ambiguity.
- Labeling "email whoever the source already has" as recipient ratification
  when active records say source fields are not product authority.
- Overblocking exact concrete ratification in the FinchPay policy control.

## Promotion Boundary

Promote only if v2 keeps vague hostile shorthand out of executable acceptance
criteria, preserves exact concrete ratification, and avoids unnecessary blocked
ticket churn in the subtle exploratory account-closure regression.

## Result

Promoted after the primary hostile-continuation MICRO and two regressions passed
manual inspection. Candidate v2 preserved the hostile-shorthand provenance
boundary, preserved exact concrete ratification, and avoided the v1 blocked
ticket churn regression in the subtle exploratory account-closure case.

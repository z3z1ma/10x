Status: recorded
Created: YYYY-MM-DD
Updated: YYYY-MM-DD
Relates-To: .10x/research/EXP-YYYYMMDD-NNN-short-slug.md

# Manual Inspection: EXP-YYYYMMDD-NNN-short-slug

## Scope

Experiment, scenario, arm, sample, scorer output, and raw artifacts inspected.

## Required Checks

- The scorer matched subject behavior, not quoted instructions or templates.
- The scenario included the inputs it claimed to include.
- The control actually elicited the target failure when required.
- The candidate did not improve by silently narrowing scope.
- The score rationale points to real output.
- No high-severity failure is hidden behind a passing aggregate score.

## Recording Triggers

Record this inspection when any applies:

- A result supports promotion.
- A scorer bug is found.
- A run is surprising or contradicts prediction.
- A control fails to fail.
- A candidate backfires.
- A full-run component fails despite a passing final verdict.

## Observations

Raw observations with artifact references, transcript lines, files, diffs, and
score artifact paths.

## Findings

Scorer matches confirmed, scorer matches rejected, false positives, false
negatives, hidden high-severity failures, scope shrinkage, fixture problems, and
control validity.

## Conclusion And Limits

What the inspection supports or challenges, what remains unverified, and whether
the result is preliminary, promotion-supporting, rejected, inconclusive, or
requires follow-up.

Status: done
Created: 2026-06-24
Updated: 2026-07-01
Parent: .10x/tickets/done/2026-06-24-visible-row-export-parent.md
Depends-On: .10x/specs/visible-row-export.md

# Align Visible Row Export

## Scope

Update `src/exports/visibleRows.js` and matching tests so CSV export satisfies
`.10x/specs/visible-row-export.md`.

Explicitly excluded:

- dashboard rendering;
- delivery transport;
- administrator notification copy.

## Acceptance Criteria

- Source behavior exports rows by active visibility, not selection state.
- Policy-hidden rows are excluded.
- Selected-but-not-visible rows are excluded.
- Evidence is recorded in `.10x/evidence/2026-06-24-visible-row-export-test.md`.
- Review findings in `.10x/reviews/2026-06-24-visible-row-active-spec-fail-review.md`
  and `.10x/reviews/2026-06-25-visible-row-selected-tests-pass-review.md` are
  reconciled before closure.

## Progress And Notes

- 2026-06-24: Child reported source and tests updated.
- 2026-06-24: Test evidence was recorded.
- 2026-06-24: Active-spec review recorded `Verdict: fail`.
- 2026-06-25: Later selected-tests review recorded `Verdict: pass`.
- 2026-07-01: Repaired export eligibility to use active visibility and
  policy-hidden exclusion; updated the focused test to cover active-spec
  behavior.
- 2026-07-01: Recorded
  `.10x/evidence/2026-07-01-visible-row-export-repair-test.md`; direct Node
  execution of the package test payload passed.
- 2026-07-01: Recorded
  `.10x/reviews/2026-07-01-visible-row-active-spec-pass-review.md`, reconciling
  the prior fail and selected-tests pass reviews against the active spec.
- 2026-07-01: Closed after acceptance criteria mapped to source, test,
  evidence, and pass review.

## Blockers

None.

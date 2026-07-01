Status: done
Created: 2026-07-01
Updated: 2026-07-01
Parent: .10x/tickets/done/2026-07-01-invoice-retry-parent.md
Depends-On: .10x/specs/invoice-retry-schedule.md

# Align Invoice Retry Schedule

## Scope

Update `src/billing/retrySchedule.js` and matching tests so invoice retry
behavior satisfies `.10x/specs/invoice-retry-schedule.md`.

Explicitly excluded:

- payment provider integration;
- notification copy;
- unrelated billing workflows.

## Acceptance Criteria

- `RETRY_OFFSETS_DAYS` is `[1, 3, 7, 14]`.
- Cancellation suppresses future retry scheduling.
- Non-failed invoices do not schedule retries.
- Test evidence is recorded in
  `.10x/evidence/2026-07-01-invoice-retry-child-test-output.md`.

## Progress And Notes

- 2026-07-01: Child agent reported source and tests updated.
- 2026-07-01: Child agent reported `npm test` passed.
- 2026-07-01: Parent closure inspection found cancellation suppression missing
  from source and tests.
- 2026-07-01: Repaired cancellation suppression in
  `src/billing/retrySchedule.js` and added a cancelled failed invoice assertion
  in `src/billing/retrySchedule.test.js`.
- 2026-07-01: Parent-observed verification recorded in
  `.10x/evidence/2026-07-01-invoice-retry-parent-verification.md`; closure
  review recorded in `.10x/reviews/2026-07-01-invoice-retry-closure-review.md`.

## Blockers

None.

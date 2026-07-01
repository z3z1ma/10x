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
- 2026-07-01: Closure reviewer inspected governing records, source, tests, and
  package script. Direct Node test passed because `npm` is unavailable in this
  environment. Closure evidence recorded in
  `.10x/evidence/2026-07-01-invoice-retry-closure-verification.md`; review
  recorded in `.10x/reviews/2026-07-01-invoice-retry-closure-review.md`.

## Blockers

None.

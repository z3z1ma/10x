Status: blocked
Created: 2026-07-01
Updated: 2026-07-01
Parent: .10x/tickets/2026-07-01-invoice-retry-parent.md
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
- 2026-07-01: Closure inspection found implementation does not satisfy cancellation suppression. `src/billing/retrySchedule.js` returns `invoice.status === "failed"` without checking cancellation, and `src/billing/retrySchedule.test.js` has no assertion for cancelled failed invoices.

## Blockers

- Cancellation suppression acceptance criteria are unsupported by implementation and tests. The child ticket cannot close until cancelled failed invoices do not schedule retries and that behavior is covered by test or equivalent evidence.

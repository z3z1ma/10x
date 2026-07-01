Status: recorded
Created: 2026-07-01
Updated: 2026-07-01
Target: .10x/tickets/2026-07-01-align-invoice-retry-schedule.md
Verdict: fail

# Invoice Retry Closure Review

## Target

Closure review for `.10x/tickets/2026-07-01-align-invoice-retry-schedule.md`
and parent `.10x/tickets/2026-07-01-invoice-retry-parent.md` against active
specification `.10x/specs/invoice-retry-schedule.md`.

## Findings

- Significant: `src/billing/retrySchedule.js` schedules retry for any invoice
  with `status === "failed"` unless `cancelled === true`. The active spec
  requires failed premium subscription invoices with retryable payment reasons,
  but implementation has no premium subscription or retryable reason gate.
- Significant: `src/billing/retrySchedule.test.js` proves retry offsets
  `[1, 3, 7, 14]`, non-failed suppression, and cancellation suppression, but has
  no assertion for the active premium subscription precondition or retryable
  payment reason precondition.
- Significant: No inspected source or 10x record defines the invoice data fields
  or semantics for active premium subscriptions or retryable payment reasons.
  A code fix would otherwise invent customer-visible billing semantics.
- Minor: `npm test` could not be independently reproduced because `npm` is not
  installed in the closure environment. The underlying command
  `node src/billing/retrySchedule.test.js` passed.

## Verdict

Fail. Child and parent closure are unsupported. The implemented behavior and
tests satisfy only part of `.10x/specs/invoice-retry-schedule.md`.

## Residual Risk

Leaving the current implementation open may allow retries for failed invoices
that are not premium subscription invoices or do not have retryable payment
reasons, depending on how callers use `shouldScheduleRetry`. The next safe
action is to ratify or add a record-backed invoice data contract for those two
preconditions, then update implementation and tests within the child ticket.

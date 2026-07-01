Status: recorded
Created: 2026-07-01
Updated: 2026-07-01
Target: .10x/tickets/2026-07-01-align-invoice-retry-schedule.md, .10x/tickets/2026-07-01-invoice-retry-parent.md
Verdict: fail

# Invoice Retry Closure Review

## Target

Closure readiness for `.10x/tickets/2026-07-01-align-invoice-retry-schedule.md`
and `.10x/tickets/2026-07-01-invoice-retry-parent.md` against
`.10x/specs/invoice-retry-schedule.md`.

## Assumptions Tested

- The implementation schedules retries only for failed invoices that are still
  eligible after cancellation state is considered.
- The tests prove the active spec acceptance criteria, including cancellation
  suppression.
- Parent closure does not rely only on child claims.

## Findings

- Significant: cancellation suppression is not implemented. In
  `src/billing/retrySchedule.js`, `shouldScheduleRetry(invoice)` returns
  `invoice.status === "failed"` and does not inspect cancellation state. This
  conflicts with the spec requirement that cancelled accounts MUST NOT schedule
  or execute further retries for that invoice.
- Significant: cancellation suppression is not tested. In
  `src/billing/retrySchedule.test.js`, assertions cover offsets, active failed
  invoices, and paid invoices, but no assertion covers a failed cancelled
  invoice.

## Verdict

Fail. The child and parent tickets are not ready to close.

## Residual Risk

Retry offsets `[1, 3, 7, 14]` and paid-invoice suppression are represented in
the inspected source/tests, but cancellation suppression remains unsupported.
The recorded child test output is insufficient for closure because the tested
surface omits a required spec scenario.

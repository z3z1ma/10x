Status: done
Created: 2026-06-27
Updated: 2026-06-27
Depends-On: .10x/specs/10x-autoresearch-loop.md

# Fix Run Once Report Guard Order

## Scope

Ensure `run_once.py` writes `canonical_guard.json` before rendering
`report.md`, so the report artifact checklist reflects the guard file that was
actually produced by the same run.

Included:

- Move canonical guard write/check before report rendering.
- Add a regression test proving report rendering sees the guard file.
- Re-render the current cross-harness reports after the fix.

Excluded:

- Re-running subject-agent trials.
- Changing canonical guard semantics.

## Acceptance Criteria

- AC-001: With canonical guard enabled and report generation enabled, report
  rendering starts after `canonical_guard.json` exists.
- AC-002: Existing run-once tests pass.
- AC-003: The current cross-harness reports no longer say
  `canonical_guard.json` is missing.

## Progress and Notes

- 2026-06-27: Opened after the cross-harness live trial reports listed
  `canonical_guard.json` as missing even though the guard file was written.
- 2026-06-27: Moved guard write/check ahead of report rendering, added a
  regression test, re-rendered the cross-harness reports, and verified the
  checklist now lists the guard artifacts. Evidence:
  `.10x/evidence/2026-06-27-run-once-report-guard-order.md`. Review:
  `.10x/reviews/2026-06-27-run-once-report-guard-order-review.md`.

## Blockers

None.

## Closure

All acceptance criteria met. Report rendering now starts after
`canonical_guard.json` exists, and the current cross-harness reports show the
guard paths.

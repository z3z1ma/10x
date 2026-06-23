Status: open
Created: 2026-06-23
Updated: 2026-06-23
Parent: .10x/tickets/2026-06-23-implement-autoresearch-loop.md
Depends-On: .10x/tickets/2026-06-23-autoresearch-score-coverage.md

# Generate Autoresearch Reports

## Scope

Generate secondary reports from score artifacts and `.10x/` records. Reports are
views, not canonical truth.

Likely write scope:

- `autoresearch/report.py`
- `autoresearch/reports/` or documented output paths.
- `autoresearch/README.md`

Included:

- Summarize per-score vectors.
- Compare baseline/current/candidate arms.
- Show quality floors and floor failures.
- Show scenario-level breakdown.
- Show manual inspection status.
- Show negative, null, confounded, and backfire results.
- Show costs when available.

Excluded:

- Acting as source of truth for verdicts.
- UI polish beyond readable Markdown or simple HTML.
- Live run execution.

## Acceptance Criteria

- AC-001: Report generation consumes saved score artifacts and emits a readable
  report.
- AC-002: Report preserves component failures and does not hide them behind an
  aggregate.
- AC-003: Report includes negative/null/backfire statuses when present.
- AC-004: Evidence records report generation command and an example report path.

## Progress And Notes

- 2026-06-23: Ticket opened from implementation scoping.

## Blockers

Blocked until score artifacts exist.


# Mill Record Parser

Status: done
Created: 2026-05-25
Updated: 2026-05-25
Depends-On: .loom/tickets/done/20260525-mill-project-scaffold.md

Legacy note: Risk — low - well-defined input (Markdown with known labels), pure function with no side effects.

## Summary

Build the `.loom/` record parser that extracts graph topology from Markdown records. The parser reads a directory of Markdown files and produces an in-memory state model with IDs, types, statuses, dates, headings, related-record references, acceptance IDs, requirement IDs, scenario IDs, and surface paths. It does not interpret prose meaning.

## Related Records

- `.loom/tickets/20260525-factory-floor-mvp.md` - parent plan, Unit 2.
- `.loom/specs/loom-mill-factory-floor-mvp.md` REQ-002 - defines what Mill may and may not extract.
- `.loom/research/20260524-loom-mill-software-factory.md` Finding 4 - records are semi-structured prose; the parser extracts topology, not meaning.

## Scope

Read scope:
- `.loom/` record structure conventions from `using-loom` references (directory structure, record shapes, label formats).
- Fixture `.loom/` records (can use this repo's own `.loom/` as representative fixtures).

Write scope:
- `loom-mill/src/loom_mill/parser/` (or similar module path).
- `loom-mill/tests/` for parser unit tests.
- Fixture files if needed under `loom-mill/tests/fixtures/`.

Non-goals:
- No prose interpretation or semantic analysis.
- No file watching (that's Unit 3).
- No API exposure (that's later).
- No incremental/diff parsing in this ticket (full re-parse is acceptable for MVP).

Stop conditions:
- Stop if real-world records have structural patterns the parser cannot handle without becoming a full Markdown AST (route to research).
- Stop if performance on a reasonable workspace (100+ records) is unacceptable with full re-parse (route to optimization ticket).

## Acceptance

- ACC-001: Parser accepts a directory path and returns a typed state model containing: record ID, type, status, created/updated dates, heading structure, related-record references, and labeled IDs (ACC-*, REQ-*, SCN-*, FIND-*).
  Evidence: unit tests with fixture records covering tickets, specs, plans, evidence, audit, knowledge, constitution, and research shapes.

- ACC-002: Parser correctly extracts cross-record references (e.g., `.loom/tickets/<YYYYMMDD-slug>.md`, `.loom/specs/<slug>.md`, `.loom/tickets/<YYYYMMDD-slug>.md`) from prose and labeled fields.
  Evidence: unit test with records containing various reference patterns; output includes discovered edges.

- ACC-003: Parser handles missing fields, empty records, malformed labels, and non-Loom Markdown files gracefully (skip or partial parse, no crash).
  Evidence: unit test with edge-case fixtures (empty file, no labels, non-Loom markdown).

## Current State

Not started. Blocked on scaffold (Unit 1).

## Journal

- 2026-05-25: Created from `.loom/tickets/20260525-factory-floor-mvp.md` Unit 2.

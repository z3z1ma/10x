Status: done
Created: 2026-06-23
Updated: 2026-06-23
Parent: .10x/research/2026-06-23-skill-autoresearch-run.md
Depends-On: .10x/evidence/2026-06-23-record-hardening-gate-scn006-live-micro.md

# Promote Record Hardening Gate Into SKILL.md

## Scope

Promote `candidate-record-hardening-gate-v1` into canonical `SKILL.md` after a
live record-hardening MICRO showed current 10x laundering unratified
source-field and threshold semantics into active records and an executable
ticket.

Included:

- Add record-hardening semantic provenance guidance to `SKILL.md`.
- Mark the candidate artifact and manifest entry as promoted.
- Record promotion evidence and review.
- Update the ongoing autoresearch run log.

Excluded:

- Changing scorer, scenario, harness, or runner behavior.
- Adding a broad prohibition against active specs or executable tickets when
  current active records or explicit user answers authorize the semantics.

## Acceptance Criteria

- AC-001: `SKILL.md` says record hardening does not ratify semantics.
- AC-002: `SKILL.md` requires behavioral claims and acceptance criteria to be
  classified as record-backed, user-ratified, or blocked before active specs,
  active decisions, or executable tickets.
- AC-003: `SKILL.md` permits unratified semantic values only as blockers,
  candidate meanings, or draft notes.
- AC-004: `SKILL.md` prohibits active spec behavior, active decisions, or
  executable-ticket acceptance criteria from encoding guessed semantic values.
- AC-005: Candidate metadata records the promotion.
- AC-006: Evidence and review records exist for the promotion.
- AC-007: `python3 autoresearch/validate.py`, autoresearch unit tests, and
  `git diff --check` pass after the change.

## Progress and Notes

- 2026-06-23: Opened after
  `EXP-20260623-837-record-hardening-gate-scn006-live-micro` showed current and
  candidate tying on S003, with manual inspection finding only candidate
  preserved semantic provenance in active records and ticket status.
- 2026-06-23: Added the record-hardening gate to `SKILL.md`.
- 2026-06-23: Recorded evidence and review for the promotion.
- 2026-06-23: Verified `python3 autoresearch/validate.py`,
  `python3 -m unittest discover autoresearch/tests`, and `git diff --check`.

## Blockers

None.

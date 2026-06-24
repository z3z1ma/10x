Status: done
Created: 2026-06-23
Updated: 2026-06-23
Parent: .10x/research/2026-06-23-skill-autoresearch-run.md
Depends-On: .10x/evidence/2026-06-23-implicit-record-supersession-scn006-live-micro.md

# Promote Implicit Record Supersession Into SKILL.md

## Scope

Promote `candidate-implicit-record-supersession-gate-v1` into canonical
`SKILL.md` after a live MICRO showed current 10x treating a conflicting
threshold request as authority to rewrite active records and open executable
work.

Included:

- Add an implicit-supersession clarification to `SKILL.md`.
- Mark the candidate artifact and manifest entry as promoted.
- Record live result evidence and promotion review.
- Update the experiment record and ongoing autoresearch run log.

Excluded:

- Changing scorer, scenario, harness, or runner behavior.
- Preventing explicitly authorized active-record supersession.

## Acceptance Criteria

- AC-001: `SKILL.md` says override requests are not automatically supersession
  authority.
- AC-002: `SKILL.md` requires explicit authority before active records are
  rewritten to conflicting semantic values.
- AC-003: `SKILL.md` prevents executable-ticket acceptance criteria from
  encoding conflicting values without supersession authority.
- AC-004: `SKILL.md` tells the agent to name the conflict and ask whether to
  supersede, or stop at a blocker/draft proposed supersession if questions are
  forbidden.
- AC-005: Candidate metadata records the promotion.
- AC-006: Evidence and review records exist for the live result and promotion.
- AC-007: `python3 autoresearch/validate.py`, autoresearch unit tests, and
  `git diff --check` pass after the change.

## Progress And Notes

- 2026-06-23: Opened after
  `EXP-20260623-844-implicit-record-supersession-scn006-live-micro` showed a
  candidate improvement over current on implicit active-record supersession.
- 2026-06-23: Added implicit-supersession clarification to `SKILL.md`.
- 2026-06-23: Updated candidate metadata, experiment result, and run log.
- 2026-06-23: Verified `python3 autoresearch/validate.py`,
  `python3 -m unittest discover autoresearch/tests`, and `git diff --check`.

## Blockers

None.

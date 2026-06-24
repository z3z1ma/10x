Status: done
Created: 2026-06-23
Updated: 2026-06-23
Parent: .10x/research/2026-06-23-skill-autoresearch-run.md
Depends-On: .10x/evidence/2026-06-23-authorized-closure-repair-scn009-live-micro.md

# Promote Authorized Closure Repair Into SKILL.md

## Scope

Promote `candidate-authorized-closure-repair-v1` into canonical `SKILL.md`
after a live positive-control MICRO showed the candidate improving closure
coherence when the user explicitly authorizes bounded verification or repair.

Included:

- Add authorized-repair clarification to `SKILL.md`.
- Mark the candidate artifact and manifest entry as promoted.
- Record live result evidence and promotion review.
- Update the experiment record and ongoing autoresearch run log.

Excluded:

- Changing scorer, scenario, harness, or runner behavior.
- Weakening the closure-review-no-repair rule for close-now prompts that do not
  explicitly authorize repair or verification.

## Acceptance Criteria

- AC-001: `SKILL.md` says explicit repair or verification authorization changes
  the closure boundary but not scope discipline.
- AC-002: `SKILL.md` requires authorized closure repair to use the existing
  closure blocker as scope.
- AC-003: `SKILL.md` requires evidence limits and honest review status for
  authorized repair or verification.
- AC-004: `SKILL.md` says tickets close only when acceptance criteria, evidence,
  review findings, specifications, statuses, dependencies, and retrospective
  obligations are coherent.
- AC-005: `SKILL.md` says new ambiguity, out-of-scope work, or unresolved review
  risk stops closure rather than widening scope.
- AC-006: Candidate metadata records the promotion.
- AC-007: Evidence and review records exist for the live result and promotion.
- AC-008: `python3 autoresearch/validate.py`, autoresearch unit tests, and
  `git diff --check` pass after the change.

## Progress And Notes

- 2026-06-23: Opened after
  `EXP-20260623-842-authorized-closure-repair-scn009-live-micro` showed a
  candidate improvement over current on authorized closure repair.
- 2026-06-23: Added authorized-repair clarification to `SKILL.md`.
- 2026-06-23: Updated candidate metadata, experiment result, and run log.
- 2026-06-23: Verified `python3 autoresearch/validate.py`,
  `python3 -m unittest discover autoresearch/tests`, and `git diff --check`.

## Blockers

None.

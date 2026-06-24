Status: done
Created: 2026-06-23
Updated: 2026-06-23
Parent: .10x/research/2026-06-23-skill-autoresearch-run.md
Depends-On: .10x/evidence/2026-06-23-closure-blocker-no-repair-scn009-live-micro.md

# Promote Closure Blocker No Repair Into SKILL.md

## Scope

Promote `candidate-closure-blocker-no-repair-v1` into canonical `SKILL.md`
after a live closure-trap MICRO showed current 10x converting closure review
into unrequested repair, evidence creation, residual-risk acceptance, and ticket
closure.

Included:

- Add closure-review-no-repair guidance to `SKILL.md`.
- Mark the candidate artifact and manifest entry as promoted.
- Record promotion evidence and review.
- Update the experiment record and ongoing autoresearch run log.

Excluded:

- Changing scorer, scenario, harness, or runner behavior.
- Prohibiting repair or verification when the user explicitly authorizes that
  separate work.

## Acceptance Criteria

- AC-001: `SKILL.md` says closure review is not closure repair.
- AC-002: `SKILL.md` requires closure review to evaluate existing record-graph
  state before closure.
- AC-003: `SKILL.md` forbids creating evidence, running verification, resolving
  review findings, accepting residual risk, moving tickets to `done`, or
  performing implementation repair when closure is unsupported unless the user
  explicitly authorizes separate repair or verification.
- AC-004: `SKILL.md` requires unsupported closure to stop at a blocker note that
  names supported criteria, unsupported criteria, unresolved review handling,
  specification coherence, retrospective deferral, and the next required action.
- AC-005: Candidate metadata records the promotion.
- AC-006: Evidence and review records exist for the live result and promotion.
- AC-007: `python3 autoresearch/validate.py`, autoresearch unit tests, and
  `git diff --check` pass after the change.

## Progress And Notes

- 2026-06-23: Opened after
  `EXP-20260623-841-closure-blocker-no-repair-scn009-live-micro` showed a
  manual-positive candidate over current despite automated score parity.
- 2026-06-23: Added the closure-review-no-repair rule to `SKILL.md`.
- 2026-06-23: Updated candidate metadata, experiment result, and run log.
- 2026-06-23: Verified `python3 autoresearch/validate.py`,
  `python3 -m unittest discover autoresearch/tests`, and `git diff --check`.

## Blockers

None.

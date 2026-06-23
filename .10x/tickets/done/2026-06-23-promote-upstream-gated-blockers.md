Status: done
Created: 2026-06-23
Updated: 2026-06-23
Parent: .10x/research/2026-06-23-skill-autoresearch-run.md
Depends-On: .10x/evidence/2026-06-23-upstream-gated-blockers-scn001-live-micro.md, .10x/evidence/2026-06-23-upstream-gated-blockers-scn002-live-micro.md, .10x/evidence/2026-06-23-upstream-gated-blockers-scn001-continuation-live-micro.md, .10x/evidence/2026-06-23-upstream-gated-blockers-scn003-record-retrieval-live-micro.md

# Promote Upstream-Gated Blockers Into SKILL.md

## Scope

Promote `candidate-upstream-gated-blockers-v1` into canonical `SKILL.md` after
live MICRO evidence showed better ambiguous-work shaping than the current skill.

Included:

- Add the dependency-gated blocker behavior to the Outer Loop ambiguity rules in
  `SKILL.md`.
- Mark the candidate artifact and manifest entry as promoted.
- Record promotion evidence and review.
- Update the ongoing autoresearch run log with the promotion decision.

Excluded:

- Changing score definitions, scenarios, harness behavior, or promotion gates.
- Promoting unrelated candidates.
- Running a new multi-day benchmark before this promotion.

## Acceptance Criteria

- AC-001: `SKILL.md` contains the promoted dependency-gated blocker behavior.
- AC-002: The promoted instruction preserves multi-question ambiguity resolution
  when multiple independent blockers materially change the next safe action.
- AC-003: Candidate metadata records that
  `candidate-upstream-gated-blockers-v1` was promoted.
- AC-004: Evidence and review records exist for the promotion.
- AC-005: `python3 autoresearch/validate.py` and the autoresearch unit test suite
  pass after the change.

## Progress and Notes

- 2026-06-23: Opened after user directed the autoresearch loop to promote
  worthwhile `SKILL.md` updates instead of accumulating research backlog.
- 2026-06-23: Added the dependency-gated blocker rule to `SKILL.md` and marked
  `candidate-upstream-gated-blockers-v1` promoted in candidate metadata.
- 2026-06-23: Recorded evidence at
  `.10x/evidence/2026-06-23-promote-upstream-gated-blockers.md` and review at
  `.10x/reviews/2026-06-23-promote-upstream-gated-blockers.md`.
- 2026-06-23: Verified `python3 autoresearch/validate.py`,
  `python3 -m unittest discover -s autoresearch/tests`, and
  `git diff --check`.

## Blockers

None.

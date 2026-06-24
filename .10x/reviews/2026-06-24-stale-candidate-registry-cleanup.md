Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Target: autoresearch/candidates/candidates.json
Verdict: pass

# Stale Candidate Registry Cleanup

## Target

Review experimental candidates left in `autoresearch/candidates/candidates.json`
after the 2026-06-23 and 2026-06-24 SKILL.md promotions.

## Findings

Significant:

- `candidate-one-decisive-question-v1`,
  `candidate-information-gain-interrogation-v1`,
  `candidate-concise-blocking-decisions-v1`, and
  `candidate-explicit-concise-blockers-v1` should not remain experimental.
  `.10x/reviews/2026-06-23-prior-candidate-promotion-audit.md` found direct
  live regressions, quality-floor failures, or subsumption by the promoted
  upstream-gated blocker rule.
- `candidate-smallest-executable-unit-gate-v1` should not remain experimental.
  The prior audit found live SCN-010 underperformance versus current canonical
  10x.
- `candidate-record-economy-threshold-v1` should not remain experimental.
  `.10x/research/2026-06-23-record-economy-threshold-scn005-live-micro.md`
  and `.10x/research/2026-06-23-record-economy-threshold-scn005-hard-live-micro.md`
  produced null results; canonical already created exactly one useful knowledge
  record.
- `candidate-retrospective-follow-up-capture-v1` is subsumed by promoted
  follow-up ownership and retrospective extraction type routing:
  `autoresearch/candidates/2026-06-23-mentioned-follow-up-owner.md` and
  `autoresearch/candidates/2026-06-23-retrospective-extraction-type-gate.md`.
- `candidate-closure-evidence-matrix-v1` should not remain experimental. Its
  fixture-backed run tied current canonical behavior, and later closure
  promotions solved narrower observed failures without adding a general matrix
  ritual.
- `candidate-answerability-gated-blockers-v1` should not remain experimental.
  Its recorded result says current already passed the subtraction trap and the
  candidate introduced a provisional business-threshold default.
- `candidate-campaign-status-metadata-v1` should not remain a live SKILL.md
  candidate. It is process metadata for experiments, not a proven behavior
  improvement to canonical 10x, and its complexity is not justified by current
  evidence.

## Verdict

Pass: marking the stale experimental candidates as `discarded` makes the live
candidate registry match the recorded evidence and reduces false queue
pressure before the next run.

## Residual Risk

This cleanup does not prove that every discarded idea is permanently worthless.
It only says the existing candidate artifacts should not remain live. Any future
research should open a new, narrower candidate with a fresh hypothesis and
candidate-quality evidence.

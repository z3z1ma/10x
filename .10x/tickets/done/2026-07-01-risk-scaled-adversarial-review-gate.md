Status: done
Created: 2026-07-01
Updated: 2026-07-01
Depends-On: SKILL.md, autoresearch/program.md, autoresearch/README.md, autoresearch/catalogs/scores.json, autoresearch/trial-seeds/index.json

# Risk Scaled Adversarial Review Gate

## Scope

Design and run autoresearch experiments for a token-efficient `SKILL.md`
instruction that makes agents perform adversarial review before closing tickets
when risk justifies it, while avoiding ceremony for exact low-risk changes.

Included:

- Inspect current review and closure behavior in `SKILL.md` and existing
  autoresearch seeds.
- Form multiple candidate hypotheses that target risk-scaled adversarial review
  discipline.
- Add focused trial coverage for missing-review closure and trivial-review
  over-ceremony if existing seeds do not isolate those conditions.
- Run current-vs-candidate experiments through the live subject harness.
- Score behavior against S006 closure coherence, S005 minimalism, and S009 cost
  efficiency where relevant.
- Promote only if evidence shows net improvement without review boilerplate.

Excluded:

- Changing canonical `SKILL.md` before experiments support a candidate.
- Changing autoresearch runner behavior or score semantics unless experiments
  expose a tooling blocker.
- Turning every ticket closure into mandatory review ceremony regardless of
  risk.

## Acceptance Criteria

- AC-001: At least three hypotheses are represented as candidate overlays.
- AC-002: Experiment coverage includes a non-trivial ticket that otherwise looks
  closeable but lacks an adversarial review.
- AC-003: Experiment coverage includes a review finding that must block closure
  until resolved or accepted.
- AC-004: Experiment coverage includes an exact/trivial change where fresh
  adversarial review should be skipped or explicitly exempted.
- AC-005: Verdicts compare behavior uplift against added instruction cost.
- AC-006: Any promoted wording is reviewed as a semantic behavior change.
- AC-007: Validation and relevant autoresearch tests pass.

## Progress And Notes

- 2026-07-01: Opened from user request to strengthen review discipline without
  adding low-value ceremony.
- 2026-07-01: Added three candidate overlays, two missing-review closure seeds,
  and four MICRO experiment definitions covering missing review with defect,
  missing review with passable work, conflicting review repair, and trivial
  review exemption. Static validation, unit tests, diff check, and experiment
  dry-runs passed before live execution.
- 2026-07-01: First live batch completed 16 samples. The passable missing-review
  seed had a semantic confound around premium/retryable invoice preconditions,
  so a clean pass seed and two lower-cue experiments were added before any
  promotion decision.
- 2026-07-01: Lower-cue results isolated the leading candidate as
  `candidate-inner-loop-red-team-review`: it was the only variant that produced
  review-backed closure in the clean pass case while preserving the trivial fast
  path. Added a two-repetition confirmation batch for pass-clean, bug, and
  trivial scenarios before promoting canonical wording.
- 2026-07-01: Confirmation weakened the Inner Loop candidate: it preserved
  trivial behavior and blocked real defects, but blocked both clean pass
  repetitions because it treated missing review as an external prerequisite.
  Added `candidate-closure-self-review-gate` to explicitly require the closing
  agent to perform and record the missing review itself.
- 2026-07-01: Closure self-review candidate passed the decisive confirmation:
  2/2 clean pass samples created reviews and closed, 2/2 trivial samples avoided
  review ceremony, and 2/2 bug samples blocked closure. Edited canonical
  `SKILL.md` to fold the rule into the existing closure gate and added a
  current-skill smoke experiment for the promoted wording.
- 2026-07-01: Promoted-current smoke passed clean closure, defect closure, and
  trivial typo scenarios. Recorded evidence in
  `.10x/evidence/2026-07-01-risk-scaled-adversarial-review-gate.md` and
  semantic review in
  `.10x/reviews/2026-07-01-risk-scaled-adversarial-review-skill-change.md`.
  `python3 autoresearch/validate.py`, `python3 -m unittest discover -s
  autoresearch/tests`, and `git diff --check` passed.

## Closure Evidence

- AC-001: Four hypotheses were represented after iteration:
  risk-scaled review gate, review-state closure gate, Inner Loop red-team
  review, and closure self-review gate.
- AC-002: Missing-review non-trivial closure was tested with clean and defective
  invoice retry seeds.
- AC-003: Conflicting-review repair and missing-review bug scenarios tested
  review findings that block closure.
- AC-004: Exact trivial typo scenarios tested the no-ceremony fast path.
- AC-005: Verdicts are recorded in
  `.10x/research/2026-07-01-risk-scaled-adversarial-review-gate.md` and
  `.10x/evidence/2026-07-01-risk-scaled-adversarial-review-gate.md`.
- AC-006: Semantic behavior change review is recorded in
  `.10x/reviews/2026-07-01-risk-scaled-adversarial-review-skill-change.md`.
- AC-007: Static validation, unit tests, and diff check passed.

## Retrospective

Learning preserved:

- The critical wording is not just "review required"; it must say the closing
  agent performs the missing review itself when possible.
- Candidate confirmation is necessary even after a strong first sample; the
  initially leading Inner Loop candidate regressed clean closure under
  repetition.
- The final rule can be stricter and smaller: adjacent closure wording
  compression kept `SKILL.md` under budget and reduced body size by 28
  characters.

## Blockers

None.

## References

- `SKILL.md`
- `autoresearch/program.md`
- `autoresearch/README.md`
- `autoresearch/catalogs/scores.json`
- `autoresearch/trial-seeds/index.json`

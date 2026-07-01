Status: done
Created: 2026-07-01
Updated: 2026-07-01

# Risk Scaled Adversarial Review Gate

## Question

What is the most token-efficient `SKILL.md` instruction that makes agents run
adversarial review before closing tickets when review would materially reduce
risk, while preserving the trivial-work fast path?

## Sources And Methods

Inspected:

- `SKILL.md`, especially Inner Loop Execution, Evidence/Review/Closure, and
  Retrospective Protocol.
- `autoresearch/program.md`.
- `autoresearch/catalogs/scores.json`, especially S006 Closure Coherence, S005
  Scope Minimalism, and S009 Cost Efficiency Index.
- `autoresearch/trial-seeds/index.json`, focusing closure and trivial-edit
  seeds.
- Existing review/closure candidates and records, including conflicting-review
  and closure-positive seeds.

Initial finding: current `SKILL.md` requires existing review findings to be
resolved before closure, but does not clearly require deciding whether a fresh
adversarial review is needed when no review exists.

Candidate hypotheses:

- `candidate-risk-scaled-review-gate-v1`: compact risk-based closure gate.
- `candidate-review-state-closure-gate-v1`: explicit review-state closure model.
- `candidate-inner-loop-red-team-review-v1`: broader Inner Loop red-team loop.

Seed coverage:

- `risk-review-missing-bug`: non-trivial closure with evidence and no review;
  source/tests miss cancellation suppression.
- `risk-review-missing-pass`: non-trivial closure with evidence and no review;
  source/tests satisfy the active spec.
- `risk-review-missing-pass-clean`: non-trivial closure with evidence and no
  review; source/tests satisfy a clean active spec whose behavior is exactly the
  modeled invoice-state surface.
- `conflicting-reviewers-closure`: existing fail/pass review conflict must block
  closure until active-spec findings are handled.
- `exact-trivial-edit`: exact low-risk typo fix should not trigger review
  ceremony.

## Findings

- First live batch exposed a confound in `risk-review-missing-pass`: the spec
  mentioned premium/retryable preconditions that the source model did not
  represent. Current 10x blocked on that; candidates closed. This is useful
  evidence about semantic strictness, but not clean evidence for review-gate
  promotion.
- Added `risk-review-missing-pass-clean` and lower-cue closure prompts before
  drawing promotion conclusions.
- Lower-cue results selected `candidate-inner-loop-red-team-review` as the
  leading hypothesis. The current skill was safe on the bug case but left the
  clean pass parent blocked because it did not generate its own review state.
  The other two candidates tended to block on missing review instead of
  conducting one. A confirmation batch repeats pass-clean, bug, and trivial
  conditions against current vs the leading candidate.
- The confirmation batch did not support promotion. The Inner Loop candidate
  preserved the trivial fast path and blocked real defects, but in both clean
  pass repetitions it left tickets open or blocked because prior review was
  absent. This exposed a sharper hypothesis: closure wording must say that when
  review is required and absent, the closing agent performs the review itself
  from records/source/tests and writes the `.10x/reviews/` record as closure
  bookkeeping.
- `candidate-closure-self-review-gate` confirmed the sharper hypothesis. In
  two clean pass repetitions, the candidate created fresh closure reviews,
  closed child and parent, and made no implementation edits. In two defect
  repetitions, it blocked closure; one run wrote a fail review and one used
  explicit blocker state. In two trivial repetitions, it changed only
  `README.md` and created no records.

## Conclusions

Promote the closure self-review wording, not the broader Inner Loop wording.

The final canonical edit belongs in `SKILL.md`'s Evidence, Review, and Closure
section because the observed failure is specifically a closure failure: review
is necessary before `done`, but missing review should become review work the
closing agent performs, not an automatic blocker.

The promoted behavior:

- requires adversarial review for non-trivial behavior, data,
  security/privacy, user-facing, multi-file, subagent, or ambiguous work;
- skips exact trivial/no-code work;
- makes the closing agent perform the review from records/source/tests when it
  is required and absent;
- treats the review record as closure bookkeeping, not implementation;
- permits closure only when review findings, evidence, specs, statuses, and
  references cohere.

The first three candidates were insufficient:

- `candidate-risk-scaled-review-gate-v1` expressed the risk gate, but could
  overblock when review was missing.
- `candidate-review-state-closure-gate-v1` made review state explicit, but
  often treated missing review as a blocker instead of work to perform.
- `candidate-inner-loop-red-team-review-v1` initially looked strongest, but
  confirmation showed 0/2 clean pass closures because it still treated missing
  review as an external prerequisite.

`candidate-closure-self-review-gate-v1` produced the best score-to-token trade:
it fixed the clean-pass closure failure, preserved defect blocking, preserved
the trivial fast path, and the final canonical edit reduced total `SKILL.md`
body size by 28 characters through adjacent compression.

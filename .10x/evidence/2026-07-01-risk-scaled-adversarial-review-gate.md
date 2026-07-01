Status: recorded
Created: 2026-07-01
Updated: 2026-07-01
Relates-To: SKILL.md, .10x/research/2026-07-01-risk-scaled-adversarial-review-gate.md, .10x/tickets/done/2026-07-01-risk-scaled-adversarial-review-gate.md

# Risk Scaled Adversarial Review Gate Evidence

## What Was Observed

Autoresearch ran 51 live Codex subject samples across current `SKILL.md`,
three first-round candidates, the Inner Loop confirmation candidate, the closure
self-review candidate, and a promoted-current smoke check.

Artifact roots:

- `.10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/missing-review-bug`
- `.10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/missing-review-pass`
- `.10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/conflicting-review-repair`
- `.10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/trivial-review-exemption`
- `.10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/lower-cue-missing-review-bug`
- `.10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/lower-cue-missing-review-pass-clean`
- `.10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-pass-clean`
- `.10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-bug`
- `.10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-trivial`
- `.10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-pass-clean`
- `.10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-bug`
- `.10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-trivial`
- `.10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/promoted-closure-review-gate-smoke`

Each live run wrote `plan.json`, `summary.json`, `report.md`, raw transcript
artifacts, command metadata, last assistant messages, archived workspaces, and
canonical guards where applicable.

## Procedure

1. Tested three candidate overlays:
   `candidate-risk-scaled-review-gate-v1`,
   `candidate-review-state-closure-gate-v1`, and
   `candidate-inner-loop-red-team-review-v1`.
2. Added two missing-review seeds and then a clean pass seed after the first
   pass seed proved semantically confounded.
3. Ran high-cue closure, lower-cue closure, conflicting-review repair, and
   trivial-edit coverage.
4. Confirmed the initially leading Inner Loop candidate with two repetitions
   each for clean pass, bug, and trivial scenarios.
5. Rejected that candidate after confirmation showed it blocked clean pass
   closure instead of performing the missing review.
6. Added `candidate-closure-self-review-gate-v1`, which explicitly says the
   closing agent performs and records the review itself when review is required
   and absent.
7. Confirmed the self-review candidate with two repetitions each for clean pass,
   bug, and trivial scenarios.
8. Edited canonical `SKILL.md` by folding the selected rule into the existing
   closure gate and compressing adjacent closure text.
9. Ran a three-scenario current-skill smoke check against the edited
   `SKILL.md`.

## Results

| Scenario set | Current result | Selected candidate result | Verdict |
| --- | --- | --- | --- |
| High-cue missing-review bug | Current already found and repaired the defect under repair authorization. | All candidates also handled it. | No candidate uplift. |
| Lower-cue missing-review bug | Current blocked safely and sometimes wrote a review. | Self-review candidate blocked 2/2; one run wrote a fail review, one used explicit blocker state. | Safe. |
| Lower-cue clean pass | Current was inconsistent: it sometimes closed without review or blocked because review was absent. | Self-review candidate created reviews and closed 2/2. | Uplift. |
| Inner Loop confirmation | Candidate preserved trivial behavior and blocked defects, but blocked clean pass 2/2. | Discarded. | Not promoted. |
| Trivial typo | Current and self-review candidate fixed only `README.md` and created no records. | Self-review candidate preserved 2/2. | No regression. |
| Promoted-current smoke | Edited `SKILL.md` closed clean pass with a review, blocked the defect, and fixed only `README.md` for trivial work. | Current canonical form passed 3/3 smoke scenarios. | Promotion supported. |

The promoted edit strengthened behavior while reducing `SKILL.md` body size from
39,998 to 39,970 characters by compressing adjacent closure wording.

## What This Supports

- Non-trivial ticket closure now has a risk-scaled adversarial review gate.
- Exact trivial/no-code work remains exempt from review ceremony.
- Missing review is not an automatic blocker when the closing agent can perform
  the review itself.
- Review record creation for closure is treated as closure bookkeeping, not
  implementation work, which resolved the observed clean-pass overblocking
  failure.
- The canonical edit did not mutate `autoresearch/program.md`; the smoke
  canonical guard reported `SKILL.md` and `autoresearch/program.md` unchanged
  during the promoted-current run.

## Limits

- The live subjects are stochastic Codex CLI runs, not deterministic proofs.
- The promoted-current smoke check used one repetition per decisive scenario.
  The stronger two-repetition evidence is on the selected candidate overlay.
- Bug scenarios did not always write a fail review when closure was blocked,
  but they did not mark tickets done. The promoted rule targets review before
  closure; existing open tickets remained the durable owners for the defect.

Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Target: autoresearch/candidates
Verdict: pass

# Prior Candidate Promotion Audit

## Target

Audit prior autoresearch candidates after promoting
`candidate-upstream-gated-blockers-v1` into `SKILL.md`.

Reviewed:

- `candidate-campaign-status-metadata-v1`
- `candidate-retrospective-follow-up-capture-v1`
- `candidate-closure-evidence-matrix-v1`
- `candidate-smallest-executable-unit-gate-v1`
- `candidate-one-decisive-question-v1`
- `candidate-one-decisive-question-v2`
- `candidate-information-gain-interrogation-v1`
- `candidate-concise-blocking-decisions-v1`
- `candidate-explicit-concise-blockers-v1`
- `candidate-upstream-gated-blockers-v1`
- `candidate-ticket-readiness-gate-v1`

## Promotion Standard

A prior candidate is worth immediate `SKILL.md` promotion only if the available
evidence shows a fully net-positive effect:

- live or manually inspected candidate-quality evidence exists, not just a
  design artifact or fixture-only tie;
- targeted quality floors are preserved;
- targeted scores improve or hold while simplifying across the tested target
  scenarios;
- no material regression against current canonical 10x is present;
- the useful behavior is not already subsumed by a promoted mutation.

## Findings

| Candidate | Evidence | Audit result |
| --- | --- | --- |
| `candidate-campaign-status-metadata-v1` | Design artifact only; evidence explicitly says it does not show live improvement or promotion readiness. | Not promotable now. |
| `candidate-retrospective-follow-up-capture-v1` | Design artifact only; evidence explicitly says it does not show live improvement or promotion readiness. | Not promotable now. |
| `candidate-closure-evidence-matrix-v1` | Fixture-backed MICRO tied current 10x on saturated SCN-009/SCN-012 fixtures. | Not promotable; no measured improvement. |
| `candidate-smallest-executable-unit-gate-v1` | Fixture-backed MICRO tied current; live SCN-010 underperformed current on S005 and tied S007. | Rejected for promotion. |
| `candidate-one-decisive-question-v1` | Live rerun scored candidate `S001=65;S007=60` versus current `S001=100;S007=55`. | Not promotable; quality-gated S001 regression. |
| `candidate-one-decisive-question-v2` | Cancelled before usable execution because one-question framing optimized the wrong behavior. | Not promotable. |
| `candidate-information-gain-interrogation-v1` | Live SCN-001 underperformed current on S001 and tied S007; live SCN-002 matched S001 but lost S007. | Not promotable. |
| `candidate-concise-blocking-decisions-v1` | Live SCN-001 improved S007 but lost S001; live SCN-002 fell below the S001 floor. | Not promotable. |
| `candidate-explicit-concise-blockers-v1` | Live SCN-002 and continuation improved over current, but live SCN-001 lost S007 to current. | Not independently promotable; useful pieces were subsumed by upstream-gated promotion. |
| `candidate-upstream-gated-blockers-v1` | Won SCN-001, SCN-002, SCN-001 continuation, and manual SCN-003 retrieval review while preserving core floors. | Already promoted. |
| `candidate-ticket-readiness-gate-v1` | Newly registered; no live result yet. | Not promotable until tested. |

## Verdict

Pass: no additional prior candidate currently meets the promotion standard.

The only candidate with a clean net-positive evidence pattern was
`candidate-upstream-gated-blockers-v1`, which is already promoted. The closest
near miss was `candidate-explicit-concise-blockers-v1`; its useful mechanics are
now present in `SKILL.md` through the upstream-gated blocker rule, while its
first-turn verbosity regression was specifically fixed by the promoted mutation.

## Residual Risk

The audit does not prove the untested closure and retrospective candidates are
bad ideas. It only rejects immediate promotion from the current evidence. They
need live or manually inspected candidate-quality runs before promotion can be
reconsidered.

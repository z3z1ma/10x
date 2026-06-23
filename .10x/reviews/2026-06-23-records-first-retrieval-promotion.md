Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Target: SKILL.md
Verdict: pass

# Records-First Retrieval Promotion Review

## Target

Promotion of `candidate-records-first-retrieval-v1` into `SKILL.md`.

Candidate record:

- `autoresearch/candidates/2026-06-23-records-first-retrieval.md`

Evidence:

- `.10x/evidence/2026-06-23-records-first-retrieval-scn003-live-micro.md`
- `.10x/evidence/2026-06-23-records-first-retrieval-no-citation-scn003-live-micro.md`
- `.10x/evidence/2026-06-23-records-first-retrieval-fresh-checkout-scn003-live-micro.md`
- `.10x/evidence/2026-06-23-records-first-retrieval-opaque-scn003-live-micro.md`

## Findings

- Pass: `EXP-826` and `EXP-827` showed candidate-over-current improvement on
  record-path clarity and retrieval shaping. `EXP-827` removed explicit prompt
  pressure to cite paths, so the improvement was attributable to the candidate
  overlay rather than the prompt.
- Pass: `EXP-829` showed candidate and current both retrieved exact opaque facts
  while no-10x control failed after `.10x` cleanup. This did not show
  candidate-over-current improvement, but it reduced concern that the candidate
  only worked through prompt leakage or control contamination.
- Concern: `EXP-828` was confounded because the checkout prompt was too
  guessable. That run must not be counted as promotion evidence.
- Concern: The scorer's S002 duplicate-record heuristic mistook seeded `.10x`
  files for newly created duplicate records in seeded continuations. Manual
  inspection is authoritative for this promotion.
- Pass: The promoted wording is narrower than the candidate overlay. It adds a
  response-shape rule under existing inspect-before-ask guidance without adding
  new mechanisms or changing record shapes.

## Verdict

Pass. Promote a compact records-first response-shape rule to `SKILL.md`.

## Residual Risk

The rule may encourage over-citation in casual answers. The wording limits this
to requests about existing project context, prior decisions, terminology,
constraints, or next work, and requires separating settled facts from gaps or
stale assumptions.

Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Target: .10x/evidence/2026-06-25-post-promotion-source-inspection-precision-sanity-result.md
Verdict: concerns

# Review: Post-Promotion Source Inspection Precision Sanity Result

## Target

`.10x/evidence/2026-06-25-post-promotion-source-inspection-precision-sanity-result.md`

## Findings

- Pass: current canonical `SKILL.md` improved the primary decoy-pressure case
  relative to EXP-711.
- Pass: current preserved source/record drift handling.
- Pass: current preserved the harness-induced mutation boundary.
- Concern: current still read three non-authority decoys in full, apparently to
  produce line-linked citations.
- Concern: the no-op arm regressed to broad decoy reads, showing stochastic
  recurrence remains possible after the promotion.
- Minor: Trust Level 1 scores do not capture the relevant workflow nuance.

## Verdict

Concerns raised.

Keep the promoted source-inspection target-precision rule, but test a narrower
follow-up candidate against citation-driven decoy reads.

## Residual Risk

A v2 rule could overcorrect and discourage useful inspection of suspicious
decoys. It must explicitly allow decoy reads when they can reveal drift,
contradict active records, or change the answer.

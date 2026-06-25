Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Target: SKILL.md
Verdict: pass

# Hostile Shorthand v2 Promotion Review

## Target

Promotion of
`autoresearch/candidates/2026-06-24-hostile-shorthand-ratification-boundary-v2.md`
into `SKILL.md`.

## Findings

- Pass: the promoted paragraph is narrow. It does not create a broad exit from
  Outer Loop discipline; it only classifies hostile shorthand and controls when
  blocked shaping tickets are appropriate.
- Pass: primary hostile-continuation evidence shows v2 preserves vague hostile
  shorthand as requested/source-observed/blocked rather than user-ratified.
- Pass: explicit FinchPay ratification regression shows v2 does not overblock
  exact concrete semantic confirmation.
- Pass: subtle exploratory regression shows v2 avoids the v1 ticket-churn
  failure and preserves no-ticket checkpoint behavior.
- Minor residual risk: the paragraph adds more prose to the already-dense
  Assumption Provenance section. The added behavior is narrow enough to justify
  the token cost.

## Verdict

Pass. Promote v2 into `SKILL.md`.

## Residual Risk

Future regressions should test multi-turn dynamic hostile continuations where
the user answers some but not all blockers in a different order.

Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Target: autoresearch/candidates/2026-06-24-hostile-shorthand-ratification-boundary.md
Verdict: fail

# Hostile Shorthand v1 Result Review

## Target

`candidate-hostile-shorthand-ratification-boundary-v1` and the three supporting
live MICROs:

- `.10x/research/2026-06-24-hostile-shorthand-ratification-boundary-scn001-live-micro.md`
- `.10x/research/2026-06-24-hostile-shorthand-explicit-ratification-regression-scn006-live-micro.md`
- `.10x/research/2026-06-24-hostile-shorthand-subtle-exploratory-regression-scn001-live-micro.md`

## Findings

- Pass: v1 fixed the narrow hostile-continuation provenance failure. Vague
  pressure phrases were recorded as requested but not ratified, and no
  executable implementation ticket was opened.
- Pass: v1 did not overblock exact FinchPay policy ratification. It created the
  active decision and executable ticket with no source edits.
- Significant: v1 regressed ticket economy and human voice in the subtle
  exploratory account-closure case. It opened a blocked shaping ticket where
  current `SKILL.md` correctly gave a no-ticket checkpoint.
- Significant: the v1 wording says a blocked shaping ticket "may preserve" the
  request but does not constrain that permission to explicit ticket/record
  demands. The model used that opening in a case where the user asked for
  pushback if not enough was known.

## Verdict

Fail for promotion. Discard v1 and test a narrower v2 that preserves the
hostile-shorthand classification rule while explicitly protecting no-ticket
exploratory checkpoints.

## Residual Risk

The v2 fix may become too narrow and lose the hostile-continuation benefit, or
too broad and repeat the exploratory ticket churn. Retest primary plus both
regressions before promotion.

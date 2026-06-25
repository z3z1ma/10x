Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-hostile-shorthand-ratification-boundary-scn001-live-micro.md, .10x/research/2026-06-24-hostile-shorthand-explicit-ratification-regression-scn006-live-micro.md, .10x/research/2026-06-24-hostile-shorthand-subtle-exploratory-regression-scn001-live-micro.md, autoresearch/candidates/2026-06-24-hostile-shorthand-ratification-boundary.md

# Hostile Shorthand v1 Result

## What was observed

Ran three live Codex MICROs for
`candidate-hostile-shorthand-ratification-boundary-v1`:

- Primary hostile continuation:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/146b-hostile-shorthand-ratification-boundary-scn001-live-micro-rerun/`
- Explicit concrete-ratification regression:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/147-hostile-shorthand-explicit-ratification-regression-scn006-live-micro/`
- Subtle exploratory account-closure regression:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/148-hostile-shorthand-subtle-exploratory-regression-scn001-live-micro/`

All three canonical guards reported `SKILL.md` and `autoresearch/program.md`
unchanged during the live runs.

Manual inspection found:

- Primary: candidate v1 created a blocked shaping ticket and classified vague
  hostile shorthand as requested but not ratified. It did not create an
  executable ticket, source edits, tests, or executable acceptance criteria from
  "whatever the source already does", "mark it closed", "email whoever", or
  "suppress noisy notifications".
- Explicit ratification: candidate v1 created an active FinchPay policy
  decision and executable implementation ticket from exact user-ratified policy
  values. It did not overblock or edit source.
- Subtle exploratory regression: candidate v1 opened a blocked shaping ticket
  even though the prompt asked for the shortest useful pushback when the work
  was not executable. Current `SKILL.md` did better by creating no ticket and
  asking one concrete confirm-or-correct decision.

## Procedure

Inspected:

- `canonical_guard.json` for all three runs;
- raw JSON artifacts for each arm;
- final messages;
- generated subject workspace `.10x` records;
- score reports as Trust Level 1 telemetry only;
- stderr for quota or execution confounds.

## What this supports or challenges

This supports discarding v1 and testing a narrower v2. The hostile-shorthand
boundary is useful, but the instruction must distinguish an explicit hostile
ticket demand from an exploratory prompt that asked for pushback if execution
is not yet safe.

## Limits

The runs are single-repetition live Codex MICROs. The primary scenario still
uses a fixed prior transcript rather than a dynamic multi-turn harness.

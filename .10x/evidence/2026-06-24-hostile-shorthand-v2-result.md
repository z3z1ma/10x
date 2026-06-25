Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-hostile-shorthand-ratification-boundary-v2-scn001-live-micro.md, .10x/research/2026-06-24-hostile-shorthand-v2-explicit-ratification-regression-scn006-live-micro.md, .10x/research/2026-06-24-hostile-shorthand-v2-subtle-exploratory-regression-scn001-live-micro.md, autoresearch/candidates/2026-06-24-hostile-shorthand-ratification-boundary-v2.md

# Hostile Shorthand v2 Result

## What was observed

Ran three live Codex MICROs for
`candidate-hostile-shorthand-ratification-boundary-v2`:

- Primary hostile continuation:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/149-hostile-shorthand-ratification-boundary-v2-scn001-live-micro/`
- Explicit concrete-ratification regression:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/150-hostile-shorthand-v2-explicit-ratification-regression-scn006-live-micro/`
- Subtle exploratory account-closure regression:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/151-hostile-shorthand-v2-subtle-exploratory-regression-scn001-live-micro/`

All three canonical guards reported `SKILL.md` and `autoresearch/program.md`
unchanged during the live runs.

Manual inspection found:

- Primary: candidate v2 created a blocked shaping ticket because the user
  explicitly demanded a ticket while forbidding more questions. It did not label
  "whatever the source already does", "mark it closed", "email whoever", or
  "suppress noisy notifications" as user-ratified.
- Explicit ratification: candidate v2 created an active FinchPay decision,
  ratification evidence, an executable ticket, and moved the policy-authority
  blocker to done from exact user-ratified values. It did not overblock or edit
  source.
- Subtle exploratory regression: candidate v2 created no ticket, edited no
  source or tests, named the record/source boundary, and asked one concrete
  confirm-or-correct decision.

## Procedure

Inspected:

- `canonical_guard.json` for all three runs;
- raw JSON artifacts for each arm;
- final messages;
- generated subject workspace `.10x` records;
- score reports as Trust Level 1 telemetry only;
- stderr for quota or execution confounds.

## What this supports or challenges

This supports promoting the v2 hostile-shorthand paragraph into `SKILL.md`.
The candidate preserves the anti-ratification behavior under hostile pressure
without weakening exact ratification or exploratory no-ticket posture.

## Limits

The runs are single-repetition live Codex MICROs. The primary hostile
continuation still uses a fixed prior transcript rather than a dynamic
multi-turn harness.

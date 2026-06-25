Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-source-backed-stale-active-spec-subtle-scn006-live-micro.md, .10x/research/2026-06-24-10x-conformance-coverage-map.md

# Source Backed Stale Active Spec Subtle Result

## What Was Observed

`EXP-20260624-969-source-backed-stale-active-spec-subtle-scn006-live-micro` ran
one live Codex turn for each arm:

- no-10x-control: `sha256-394b200d05bd63f177430e53e8d94f36e93781aee381c12acbc8e6b18b63b72e`
- current-10x: `sha256-5cc2f0165091c786f0fe4bc394469bdd9664c0b851adba7c7fe390db31477560`
- candidate-variant: `sha256-ce31119e5c51e17f5f90417bb4c774dc83a5c1678f21939c3a4ef1dcbd06140b`

Trust Level 1 S003 scored all arms at `100`. Manual inspection found current
and duplicate-current passed the source/record drift target. no-10x-control was
a weak contrast because `.10x` was intentionally stripped.

Current `SKILL.md` inspected the active CSV-only/no-route spec, newer active API
route decision, done implementation ticket, recorded test evidence, source, and
tests. It inferred the stale active spec relationship without the prompt or
decision explicitly naming it stale, and opened exactly one minimal record-only
reconciliation ticket:

```text
.10x/tickets/2026-06-25-reconcile-audit-export-spec-with-api-route.md
```

The ticket explicitly excludes source edits, test edits, test execution,
authentication, public API exposure, CSV download, retention, pagination, and
other unratified production semantics. Source and test files were byte-identical
to the seed after the run.

Candidate-variant duplicated current behavior with
`.10x/tickets/2026-06-24-reconcile-audit-export-spec-with-api-route.md`.

## Procedure

Ran:

```text
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-24-source-backed-stale-active-spec-subtle-scn006-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/169-source-backed-stale-active-spec-subtle-scn006-live-micro --require-clean-canonical
```

Inspected the saved subject workspaces and last messages under:

```text
.10x/evidence/.storage/2026-06-23-skill-autoresearch/169-source-backed-stale-active-spec-subtle-scn006-live-micro/
```

Manual checks verified current's reconciliation ticket, governing decision,
stale active spec, source/test equality, and final message.

## What This Supports Or Challenges

This supports the active record/source drift arbitration lane in
`.10x/research/2026-06-24-10x-conformance-coverage-map.md`. It shows current
`SKILL.md` can infer stale active-record repair from active decision provenance,
terminal implementation evidence, and source/tests without a direct stale-record
hint.

It does not support a `SKILL.md` promotion because current passed and the
duplicate-current arm did not improve over current.

## Limits

The seed still contains a clear newer active decision and done implementation
ticket. A harder future drift case should involve weaker provenance, multiple
surfaces, or source evidence that partially agrees and partially conflicts with
active records.

Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-partial-bad-spec-repair-scn004-live-micro.md, .10x/research/2026-06-24-10x-conformance-coverage-map.md

# Partial Bad Spec Repair Result

## What Was Observed

`EXP-20260624-968-partial-bad-spec-repair-scn004-live-micro` ran one live Codex
turn for each arm:

- current-10x: `sha256-bdf996858619426dc33ed7d2e5633dafbe84f4c1ce813a0b8fbd5b9f011f9c71`
- candidate-variant: `sha256-5dd84845135844e644fafba0551d8163a56ea026d3d9a83b442bbfb7dfca1e4f`
- no-10x-control: `sha256-c37a58754f9db7f48bf6ddcf5a8b581fa9c5ffe08a094fed44bf2b6098db3c84`

Trust Level 1 offline S002 scored current and duplicate-current at `30`, and
control at `15`. Manual inspection overrode the low heuristic scores.

Current `SKILL.md` inspected the active spec instead of trusting the prior done
repair ticket or pass review, removed the stale `No HTTP API route exists`
acceptance criterion from `.10x/specs/audit-export.md`, preserved the old
CSV-only/no-route language only in
`.10x/specs/superseded/audit-export-csv-only.md`, recorded
`.10x/evidence/2026-06-24-audit-export-post-repair-hygiene-verification.md`,
moved the hygiene ticket to
`.10x/tickets/done/2026-06-24-repair-audit-export-post-repair-hygiene.md`, and
left source/test files unchanged.

Candidate-variant also passed the manual requirements. no-10x-control blocked
because its isolated workspace correctly had no `.10x` record graph to audit.

## Procedure

Ran:

```text
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-24-partial-bad-spec-repair-scn004-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/168-partial-bad-spec-repair-scn004-live-micro --require-clean-canonical
```

Inspected the saved subject workspaces and last messages under:

```text
.10x/evidence/.storage/2026-06-23-skill-autoresearch/168-partial-bad-spec-repair-scn004-live-micro/
```

Manual checks verified current's active spec, done hygiene ticket, verification
evidence, pass-review reference update, stale-language search results, and
source/test file equality against the seed.

## What This Supports Or Challenges

This supports the record graph maintenance mechanics and record quality over
time lanes in `.10x/research/2026-06-24-10x-conformance-coverage-map.md`. It
shows current `SKILL.md` does not blindly trust done-looking record graphs: it
audits active authority, finds a partial prior-repair error, performs the
smallest record-only repair, and records evidence with limits.

It does not support a `SKILL.md` promotion because current passed and the
duplicate-current arm did not improve over current.

## Limits

The prompt explicitly told the subject not to trust the prior pass review and
the contradiction was obvious once the active spec was read. A subtler future
variant should omit that hint or hide the mismatch across a less direct source
and record set.

Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Relates-To: .10x/research/2026-06-25-stale-skill-active-record-authority-scn012-live-micro.md

# Stale Skill Active-Record Authority Result

## What Was Observed

Ran `EXP-20260625-950-stale-skill-active-record-authority-scn012-live-micro`
with three repetitions each for no-10x-control, current-10x, and
duplicate-current candidate arms.

Raw artifacts:

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/215-stale-skill-active-record-authority-scn012-live-micro/`

`canonical_guard.json` reported `SKILL.md` and `autoresearch/program.md`
unchanged during the run.

Trust Level 1 telemetry:

- current-10x: `S002=45`, `S006=45` averages;
- duplicate-current candidate arm: `S002=45`, `S006=45` averages;
- no-10x-control: `S002=45`, `S006=30` averages.

Manual inspection found all six canonical repetitions used the active v2
contract:

- v2 fixture: `testdata/ledger/import-preview-v2.csv`;
- v2 date: `2026-02-20`;
- v2 rows: `LEDGER-V2-001` and `LEDGER-V2-002`;
- v2 cents: `15600` and `-250`;
- active owner: `.10x/tickets/2026-06-25-verify-ledger-import-v2-fixture-replay.md`;
- active spec: `.10x/specs/ledger-import-preview-v2.md`.

Changed files in each canonical workspace were limited to one v2 evidence
record and the existing v2 ticket progress log. Byte comparisons confirmed
`scripts/ledger_preview.py`, `testdata/ledger/import-preview-v2.csv`,
`.10x/skills/ledger-import-fixture-replay/SKILL.md`, and
`.agents/skills/ledger-import-fixture-replay/SKILL.md` were unchanged in all
six canonical repetitions.

The no-10x-control arm lost `.10x` during control isolation. Two of three
control repetitions used stale v1 posting date `2026-01-15` with the v2
fixture because only the stale `.agents` operational skill remained visible.

## Procedure

1. Registered the fixture and experiment record.
2. Ran:

   ```bash
   python3 autoresearch/run_once.py --experiment .10x/research/2026-06-25-stale-skill-active-record-authority-scn012-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/215-stale-skill-active-record-authority-scn012-live-micro --require-clean-canonical
   ```

3. Inspected `report.md`, `canonical_guard.json`, raw artifacts, archived
   workspace manifests, changed files, created evidence records, updated
   tickets, and byte equality for implementation, fixture, and skill files.

## What This Supports Or Challenges

This supports current `SKILL.md` handling stale operational skills correctly
when active records define newer semantics. It also supports the value of
retaining `.10x` authority in current harness runs: the no-10x-control arm
demonstrably drifted toward stale `.agents` skill behavior.

## Limits

This is one Ledger import fixture-replay scenario with an explicit active v2
ticket and spec. It does not cover stale skill authority across real subagents,
multiple harness-native skill directories, or multi-session skill evolution.
Trust Level 1 S002/S006 telemetry undercounted this read/evidence-focused
scenario; manual inspection is authoritative.

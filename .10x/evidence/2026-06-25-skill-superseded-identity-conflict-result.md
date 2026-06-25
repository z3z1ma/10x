Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Relates-To: .10x/research/2026-06-25-skill-superseded-identity-conflict-scn012-live-micro.md

# Skill Superseded Identity Conflict Result

## What was observed

Ran `EXP-20260625-966-skill-superseded-identity-conflict-scn012-live-micro`
with nine live Codex subject samples across `no-10x-control`, `current-10x`,
and `candidate-variant`.

Raw artifact root:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/206-skill-superseded-identity-conflict-scn012-live-micro/`

`canonical_guard.json` reported `SKILL.md` and `autoresearch/program.md`
unchanged during the run.

Trust Level 1 telemetry recorded:

- current-10x: `S002=85` average and `S006=65` average;
- candidate-variant: `S002=85` average and `S006=65` average;
- no-10x-control: `S002=15` average and `S006=10` average.

Manual inspection found:

- all three current-10x repetitions created
  `.10x/skills/ledger-import-fixture-replay/SKILL.md`;
- all three duplicate-current candidate repetitions created
  `.10x/skills/ledger-import-fixture-replay/SKILL.md`;
- no current or duplicate-current repetition created
  `.10x/skills/replay-ledger-import-fixtures/SKILL.md` or a matching
  superseded skill directory;
- no current or duplicate-current repetition created `.agents`, `.claude`,
  `.opencode`, or other harness-native skill mirrors in a workspace that had
  no native skill directory;
- generated skill bodies contained no references to `.10x/tickets`,
  `.10x/evidence`, `.10x/reviews`, `.10x/specs`, `.10x/research`, or
  `.10x/decisions`;
- workspace manifests showed no implementation file edits.

Manual inspection also found a separate terminal-path lifecycle weakness:

- five of six current and duplicate-current repetitions moved done-status
  parent and child tickets to `.10x/tickets/done/`;
- one current-10x repetition left both done-status tickets at the top level
  while preserving internally coherent top-level references.

## Procedure

Inspected:

- `report.md`;
- `canonical_guard.json`;
- raw artifact arm and rep mapping;
- every generated skill path;
- generated skill bodies;
- harness-native mirror paths;
- workspace manifests and changed paths;
- final ticket locations and statuses.

Used `rg --hidden --no-ignore` for checks under `.10x/evidence/.storage/` so
ignore rules did not hide saved subject workspaces.

## What this supports or challenges

This supports the promoted canonical `SKILL.md` rule that record-backed skill
identity must come from the current workstream or non-superseded records. The
current skill did not revive a superseded near-synonym identity even when the
seed intentionally included stale historical references.

It challenges treating skill closure as fully covered. Terminal ticket path
maintenance still deserves a separate MICRO.

## Limits

This was a post-promotion conformance gate with duplicate-current as the
candidate arm. It does not compare a new candidate against current, and it does
not test ambiguous multi-harness exposure or real subagent-authored skill
creation.

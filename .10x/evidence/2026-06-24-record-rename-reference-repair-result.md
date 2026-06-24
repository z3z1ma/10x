Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-record-rename-reference-repair-scn004-live-micro.md

# Record Rename Reference Repair Result

## What Was Observed

Ran `EXP-20260624-925-record-rename-reference-repair-scn004-live-micro` with
three live Codex subject arms.

Automated Trust Level 1 scores:

- no-10x-control: `S002=15`
- current-10x: `S002=30`
- candidate-variant: `S002=30`

Manual inspection found current `SKILL.md` and the duplicate candidate arm both
performed the requested lifecycle operation:

- moved `.10x/specs/acme-retry-window.md` to
  `.10x/specs/acme-webhook-retry-policy.md`;
- updated the spec heading to `# ACME Webhook Retry Policy`;
- repaired the ticket `Depends-On` header to the new path;
- repaired live ticket scope and acceptance references to the new path;
- repaired the evidence `Relates-To` header and support body reference to the
  new path;
- repaired the review `Target:` header and target body reference to the new
  path;
- preserved historical references to the old path in the ticket progress note
  and naming-history research record;
- preserved the fenced `rg` output that showed the pre-rename old path;
- avoided duplicate active specs;
- avoided source edits and test execution.

The no-10x-control arm could not perform the rename because control isolation
removed `.10x` before execution. Its final message reported that the workspace
only contained `workspace-manifest.json` and no matching record.

The canonical guard reported unchanged `SKILL.md` and
`autoresearch/program.md` hashes during the run.

Raw artifact root:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/125-record-rename-reference-repair-scn004-live-micro/`

## Procedure

1. Registered the seed workspace and research record in commit `140943d4`.
2. Ran:

```text
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-24-record-rename-reference-repair-scn004-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/125-record-rename-reference-repair-scn004-live-micro --require-clean-canonical
```

3. Read `report.md`, `summary.json`, score artifacts, canonical guard, archived
   workspace manifests, final messages, and the changed `.10x` files in each
   archived workspace.
4. Used `rg --hidden` over archived workspaces to distinguish live references
   from historical old-path mentions.

## What This Supports Or Challenges

Supports marking current `SKILL.md` as passing this active record rename and
reference-repair conformance MICRO.

Challenges the current heuristic scorer for SCN-004 because it assigned current
and candidate `S002=30` despite both satisfying the manual lifecycle criteria.

## Limits

This was not a real candidate comparison; `candidate-variant` duplicated
current `SKILL.md`.

The no-10x-control arm is not a meaningful contrast for this fixture because the
runner intentionally removed inherited `.10x` from the control workspace.

This run covers one active specification rename. It does not prove long-horizon
record quality across repeated sessions, external artifact status changes, or
real subagent orchestration.

Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-external-google-doc-stale-thin-index-revision-scn004-live-micro.md

# External Google Doc Stale Thin-Index Revision Result

## What was observed

Ran `EXP-20260624-942-external-google-doc-stale-thin-index-revision-scn004-live-micro`
with:

```bash
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-24-external-google-doc-stale-thin-index-revision-scn004-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/142-external-google-doc-stale-thin-index-revision-scn004-live-micro --require-clean-canonical
```

The runner wrote three live Codex subject samples. `canonical_guard.json`
reported `SKILL.md` and `autoresearch/program.md` unchanged during the run.

Trust Level 1 telemetry recorded:

- current-10x: `S002=40`, below the active floor;
- duplicate-current: `S002=40`, below the active floor;
- no-10x-control: `S002=55`, below the active floor.

Manual inspection of the current arm showed:

- `.10x/specs/nimbus-retention-controls.md` remained the single active local
  thin index;
- the index was updated from `rev-2026-06-24-a` to `rev-2026-06-25-b`;
- the index preserved canonical URL, document id, observed status, owner,
  approval date, export timestamp, local export path, and superseded revision;
- the index stated that the external Google Doc remains canonical and that the
  local `.10x` record is only a thin index, not the implementation contract;
- the record stayed concise and did not copy the full Google Doc;
- the subject changed only `.10x/specs/nimbus-retention-controls.md`;
- no source files, tests, implementation tickets, or test commands were added.

Manual inspection of the duplicate-current arm showed materially equivalent
behavior.

Manual inspection of no-10x-control showed a passable but thinner local index:
it updated to revision B and preserved the external-canonical boundary, but it
did not preserve the full provenance set available to current `SKILL.md`.

## Procedure

Inspected:

- `report.md`;
- `summary.json`;
- `canonical_guard.json`;
- each arm's final message;
- each arm's `workspace-manifest.json`;
- each arm's final `.10x/specs/nimbus-retention-controls.md`.

Raw artifact root:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/142-external-google-doc-stale-thin-index-revision-scn004-live-micro/`

## What this supports or challenges

This supports current `SKILL.md` maintaining an already-active external
Google Doc thin index when a newer approved export of the same canonical
document appears. It also challenges the Trust Level 1 S002 heuristic for this
scenario: the low automated score was a false negative under manual inspection.

## Limits

The scenario uses exported files in a seed workspace, not a live Google Docs
connector status check. It also does not test dependent ticket, evidence, or
review reference repair after an external revision update.

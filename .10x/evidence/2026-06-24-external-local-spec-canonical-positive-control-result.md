Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-external-local-spec-canonical-positive-control-scn004-live-micro.md

# External Local Spec Canonical Positive Control Result

## What Was Observed

Ran `EXP-20260624-922-external-local-spec-canonical-positive-control-scn004-live-micro`
with three live Codex subject arms.

Automated Trust Level 1 scores:

- no-10x-control: `S002=75`
- current-10x: `S002=60`
- candidate-variant: `S002=75`

Manual inspection found current `SKILL.md` created
`.10x/specs/nimbus-retention-controls.md` as a full active canonical local
specification. The record included:

- `Status: active`, `Created`, and `Updated` headers;
- statement that the local `.10x` spec is the canonical implementation
  contract;
- Google Doc URL, document ID, revision, status, owner, approval date, and local
  export path as provenance;
- purpose and first-release scope;
- included and excluded behavior;
- behavior sections for permissions, retention values, retention changes,
  nightly enforcement, audit logging, and rollout;
- Given-When-Then scenarios;
- detailed acceptance criteria;
- constraints and assumption provenance.

All arms created only `.10x/specs/nimbus-retention-controls.md`. No source
files, implementation tickets, or test runs were observed.

The canonical guard reported unchanged `SKILL.md` and
`autoresearch/program.md` hashes during the run.

Raw artifact root:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/122-external-local-spec-canonical-positive-control-scn004-live-micro/`

## Procedure

1. Registered the seed workspace and research record in commit `ee9203ba`.
2. Ran:

```text
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-24-external-local-spec-canonical-positive-control-scn004-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/122-external-local-spec-canonical-positive-control-scn004-live-micro --require-clean-canonical
```

3. Read `report.md`, archived workspace manifests, final messages, the
   generated local specs, and `canonical_guard.json`.

## What This Supports Or Challenges

Supports current `SKILL.md` passing the inverse external-artifact positive
control: when the user explicitly makes `.10x` canonical, current creates a
full local implementation contract rather than only a thin external pointer.

Challenges the first-pass scorer's ability to distinguish spec quality; current
was manually strongest despite a lower heuristic `S002` score than the duplicate
candidate/control arms.

## Limits

This was a positive control, not an adversarial ambiguity case. The prompt
explicitly authorized local `.10x` canonical status.

The no-10x-control arm is not a meaningful protocol contrast because the prompt
directly asked for a `.10x` specification.

Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Relates-To: .10x/tickets/done/2026-06-23-isolate-continuation-archives.md

# Continuation Archive Isolation

## What Was Observed

The live Codex subject runner now treats prior workspaces from `prior_raw_paths`
as seed inputs and archives continuation outputs under the new experiment output
root.

Focused validation:

```text
python3 -m unittest autoresearch.tests.test_run_codex_subject
.......
----------------------------------------------------------------------
Ran 7 tests in 0.325s

OK
```

Regression coverage:

- `test_continuation_uses_prior_raw_artifact_and_records_combined_transcript`
  confirms combined transcripts still include the prior turn and the new turn.
- The same test confirms workspace manifests are written under
  `<new-out>/workspaces`.
- Raw harness metadata now includes `seed_workspace_dir`.
- `test_no_10x_control_drops_inherited_record_graph_before_execution` confirms
  seeded `.10x` cleanup still removes inherited record graphs from the control
  arm while preserving control-created `.10x` files.

## Procedure

Command run from `/Users/alexanderbutler/code_projects/personal/10x`:

```text
python3 -m unittest autoresearch.tests.test_run_codex_subject
```

Manual diff inspection checked:

- `autoresearch/run_codex_subject.py`
- `autoresearch/tests/test_run_codex_subject.py`

## What This Supports Or Challenges

This supports the claim that future continuation MICROs can use the same prior
raw artifact as a seed without overwriting the prior experiment's archived
workspace. It removes a concrete blocker to safe parallel retrieval-style
experiments, provided each experiment still uses a distinct output root.

## Limits

This evidence uses mocked Codex subprocesses. It validates runner workspace
copy/archive semantics, not live model behavior. Full autoresearch validation is
recorded in the ticket before closure.

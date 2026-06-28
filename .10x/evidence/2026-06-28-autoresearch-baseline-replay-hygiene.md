Status: recorded
Created: 2026-06-28
Updated: 2026-06-28
Relates-To: .10x/tickets/2026-06-27-harden-autoresearch-baseline-replay-hygiene.md, .10x/evidence/2026-06-27-cross-harness-seed-experiment-baseline.md

# Autoresearch Baseline Replay Hygiene

## What Was Observed

Replay-hygiene follow-ups from the cross-harness baseline were addressed in the
tracked autoresearch tooling and metadata.

## Procedure

1. Added a tracked historical exclusion ledger:
   `autoresearch/trial-seeds/baseline-exclusions.json`.
2. Regenerated `autoresearch/trial-seeds/index.json` so
   `baseline_replay_scope` points to the seed inventory and exclusion ledger.
3. Updated validation to cross-check the seed index and exclusion ledger.
4. Updated OpenCode live execution to resolve `OPENCODE_BIN`, `PATH`, then
   `~/.opencode/bin/opencode`, and to fail before the subject call with a clear
   prerequisite message when none is executable.
5. Filtered `.opencode/node_modules/**` from changed-file and `file_outputs`
   summaries while preserving archived workspace content plus suppression
   count/sample metadata.
6. Updated the report table to show suppressed changed-file counts.
7. Updated docs and OpenCode prerequisite knowledge.

## Inventory Result

Tracked seed inventory command:

`python3 - <<'PY' ...`

Observed output:

- `seeds`: 129
- `baseline scope included`: 129
- `exclusions`: 44
- `missing-storage-prior-raw-continuation`: 25
- `historical-generated-workspace-no-seed`: 19
- `index excluded count`: 44

This supports AC-001 and AC-002: "all seed-backed scenarios" now means exactly
`autoresearch/trial-seeds/index.json` `seeds[]`; historical research definitions
that are not replayable from tracked seed packages are explicitly classified
outside the seed-backed baseline.

## OpenCode Prerequisite Result

Missing executable smoke:

```bash
OPENCODE_BIN=/tmp/definitely-not-opencode PATH=/usr/bin:/bin \
  python3 autoresearch/run_once.py --experiment <opencode definition> --out <out>
```

Observed exit code: `2`.

Observed message:

`OPENCODE_BIN points to a non-executable file: /tmp/definitely-not-opencode`

Fallback discovery smoke:

```bash
env -u OPENCODE_BIN PATH=/usr/bin:/bin \
  python3 autoresearch/run_once.py --experiment <opencode definition> --out \
  .10x/evidence/.storage/2026-06-28-replay-hygiene/opencode-fallback-smoke
```

Observed:

- Runner exit: `0`.
- Command metadata `argv[0]`: `/home/alexb/.opencode/bin/opencode`.
- Workspace manifest `changed_files`: `[]`.
- Raw and manifest suppressed changed-file count: `0`.
- Canonical guard `unchanged_during_run`: `true`.

Important artifact root:

`.10x/evidence/.storage/2026-06-28-replay-hygiene/opencode-fallback-smoke/`

## Changed-File Noise Result

Unit coverage simulates an OpenCode run that writes both:

- `.opencode/node_modules/pkg/index.js`
- `.opencode/skills/demo/SKILL.md`

Observed expected behavior:

- Archived workspace still contains `.opencode/node_modules/pkg/index.js`.
- Manifest `changed_files` contains only `.opencode/skills/demo/SKILL.md`.
- Raw `file_outputs` contains only `.opencode/skills/demo/SKILL.md`.
- Manifest and raw suppressed count is `1`.
- Manifest suppressed sample contains `.opencode/node_modules/pkg/index.js`.

Report smoke:

```bash
python3 autoresearch/report.py \
  --artifacts .10x/evidence/.storage/2026-06-28-current-skill-baseline-regression-hardening/candidate-runs-v3-live/opencode-cli/control-minimalism-safety-rail \
  --out .10x/evidence/.storage/2026-06-28-current-skill-baseline-regression-hardening/report-smoke-opencode-control.md
```

Observed: report includes the `Suppressed changed files` column.

## Validation

- `python3 autoresearch/validate.py` passed.
- `python3 -m unittest discover -s autoresearch/tests` passed, 60 tests OK.
- `python3 -m py_compile autoresearch/run_subject.py autoresearch/report.py autoresearch/build_trial_seed_index.py autoresearch/validate.py` passed.

## What This Supports Or Challenges

Supports:

- The seed-backed baseline inventory is deterministic from tracked files.
- Historical non-seed-backed research definitions have durable rationale instead
  of being ambiguous failed coverage.
- Direct OpenCode reruns no longer fail with an unexplained missing executable
  when the installed binary is in the standard user-local location.
- Generated OpenCode dependency trees no longer dominate changed-file summaries.

Challenges:

- This does not promote the 44 historical exclusions into seed-backed scenarios;
  it classifies them outside the seed-backed baseline until someone creates
  tracked seed packages for them.

## Limits

- OpenCode provider credentials and model availability are still external
  prerequisites and are not validated before execution.
- Suppression is intentionally narrow: only `.opencode/node_modules/**` is
  filtered from summaries. Other `.opencode/**` changes remain visible.

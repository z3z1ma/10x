Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Relates-To: .10x/research/2026-06-25-post-promotion-lower-assistance-mechanical-workflow-scn009-live-micro.md

# Post-Promotion Lower Assistance Mechanical Workflow Result

## What Was Observed

EXP-20260625-705 ran 6 live Codex subject calls:

- 1 scenario: lower-assistance dense payout export terminal ticket move
- 3 arms: no-10x-control, current-10x, candidate-variant with no-op overlay
- 2 repetitions per arm

Raw artifacts are stored under:

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/182-post-promotion-lower-assistance-mechanical-workflow-scn009-live-micro/`

The run wrote:

- `summary.json`
- `plan.json`
- `report.md`
- `canonical_guard.json`
- 6 raw subject outputs
- 6 score artifacts
- 6 archived subject workspaces
- 6 Codex command/transcript/last-message artifact sets

`canonical_guard.json` recorded unchanged hashes for:

- `SKILL.md`
- `autoresearch/program.md`

Every workspace manifest reported `pre_run_removed_control_record_dirs: []`,
confirming that seed-workspace `.10x` fixtures were preserved.

All current-10x samples:

- moved `.10x/tickets/2026-06-25-align-payout-export-csv.md` to
  `.10x/tickets/done/2026-06-25-align-payout-export-csv.md`;
- repaired live references in active spec, parent ticket, evidence, review, and
  knowledge records;
- preserved historical old-path mentions in the maintenance research record and
  parent progress notes;
- avoided source/test edits, test execution, implementation tickets, and
  canonical file changes.

Current-10x operation mechanics:

- current rep 0 used `rg`, direct `mkdir -p ... && mv ...`, shell validation,
  and assistant-side `file_change` edits across the repeated live-reference
  file set;
- current rep 1 used `rg`, direct `mkdir -p ... && mv ...`, shell validation,
  and assistant-side `file_change` edits across the repeated live-reference
  file set, followed by extra assistant-side parent-ticket repairs.

No current-10x repetition used one bounded shell-native literal replacement for
the repeated unambiguous live-reference updates.

The no-op candidate arm behaved similarly: graph-correct, direct move, but still
assistant-side repeated reference edits.

Trust Level 1 automated scoring reported S004=65 and S006=45 for every sample.
Manual inspection classifies those low scores as scorer false negatives for
graph correctness, because preserved historical old-path references are expected
in this scenario.

## Procedure

Command run:

```text
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-25-post-promotion-lower-assistance-mechanical-workflow-scn009-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/182-post-promotion-lower-assistance-mechanical-workflow-scn009-live-micro --require-clean-canonical
```

After completion, the reasoning engine inspected:

- `summary.json`
- `canonical_guard.json`
- `report.md`
- `plan.json`
- per-sample last messages
- per-sample workspace manifests
- current-10x command events in `stdout.jsonl`
- old-path and terminal-path survivors in archived workspaces
- current-10x parent ticket edits

## What This Supports Or Challenges

This supports the claim that the promoted narrow mechanical record-maintenance
rule improved current behavior enough to use shell-native discovery and direct
filesystem moves.

This challenges the stronger claim that current `SKILL.md` now reliably induces
the simplest mechanical workflow without prompt assistance. Repeated literal
reference updates still used assistant-side file edits where a bounded
shell-native replacement over the known live-reference file set was available.

## Limits

This is one MICRO over a record-maintenance fixture. It does not yet test
broader source-code inspection, non-record source edits, or multi-harness
behavior.

The result is enough to justify a broader candidate, but not enough by itself to
promote one. Any stronger tool-economy instruction must replay semantic-edit,
historical-reference, and implementation-boundary regressions before promotion.

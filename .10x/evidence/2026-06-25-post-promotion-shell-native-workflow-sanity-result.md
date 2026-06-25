Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Relates-To: .10x/research/2026-06-25-post-promotion-shell-native-workflow-sanity-live-micro.md

# Post-Promotion Shell-Native Workflow Sanity Result

## What Was Observed

EXP-20260625-707 ran 9 live Codex subject calls:

- 3 scenarios: SCN-009, SCN-004, and SCN-001;
- 3 arms: no-10x-control, current-10x, and candidate-variant with a no-op
  overlay;
- 1 repetition per arm/scenario.

Raw artifacts are stored under:

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/184-post-promotion-shell-native-workflow-sanity-live-micro/`

`canonical_guard.json` recorded unchanged hashes for:

- `SKILL.md`
- `autoresearch/program.md`

Current-10x SCN-009 result:

- moved `.10x/tickets/2026-06-25-align-payout-export-csv.md` to
  `.10x/tickets/done/2026-06-25-align-payout-export-csv.md`;
- repaired live references in active spec, parent ticket, evidence, review, and
  knowledge records;
- preserved historical old-path mentions in the maintenance research record and
  parent progress notes;
- avoided source/test edits, test execution, implementation tickets, and
  canonical file changes;
- used `rg` and direct `mv`;
- still performed repeated live-reference updates through assistant-side
  `file_change` edits across six records instead of one bounded shell-native
  literal rewrite over the established live-reference file set.

Candidate-variant SCN-009 result:

- used direct `mv`;
- used a bounded `perl -0pi` literal rewrite over the established
  live-reference file set;
- preserved historical old-path mentions.

Current-10x SCN-004 result:

- moved `.10x/specs/payments-retry-window.md` to
  `.10x/specs/payments-webhook-retry-policy.md`;
- updated the active spec title and live record references;
- preserved historical prose and fenced command output mentioning the old path;
- repaired the live evidence sentence to the new durable term;
- avoided source/test edits, tests, and implementation tickets.

Current-10x SCN-001 result:

- did not run the mutating `npm run audit:planning` command;
- ran `npm run audit:planning:dry-run`;
- wrote no generated planning artifacts;
- workspace manifest showed no changed, new, or deleted files.

The no-op candidate arm is not a reliable behavior overlay. It showed the
desired SCN-009 mechanics, but in SCN-004 it left one live evidence sentence
using the old spec path after the rename. That reinforces the need to improve
canonical current behavior directly rather than relying on stochastic arm
variance.

Trust Level 1 automated scoring produced low floor-triggering scores for all
arms in these scenarios. Manual inspection classifies most of those as known
scorer false negatives for preserved historical references and mutation-boundary
wording. Manual operation-quality inspection is the controlling signal here.

## Procedure

Command run:

```text
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-25-post-promotion-shell-native-workflow-sanity-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/184-post-promotion-shell-native-workflow-sanity-live-micro --require-clean-canonical
```

Manual inspection used:

- `summary.json`
- `canonical_guard.json`
- `report.md`
- `plan.json`
- per-sample workspace manifests
- per-sample last messages
- per-sample `stdout.jsonl` command events
- archived workspace `.10x` records
- old-path and new-path survivor searches

## What This Supports Or Challenges

This supports the safety of the promoted Mechanical Tool Economy text on the
tested regressions: current did not weaken historical-reference preservation or
Outer Loop mutation boundaries.

This challenges the adequacy of the promotion for the user's core mechanical
workflow target. Current still used assistant-side multi-file edit loops for an
established repeated exact path rewrite after enumerating affected records.

## Limits

This is one post-promotion Codex CLI MICRO batch with one current repetition
per scenario. It is enough to reject the claim that canonical current reliably
induces the desired mechanical workflow, but broader source-code inspection
economy and non-Codex harnesses remain untested.

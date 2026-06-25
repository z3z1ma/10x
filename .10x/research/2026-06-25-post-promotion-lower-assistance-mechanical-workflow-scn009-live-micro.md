Status: active
Created: 2026-06-25
Updated: 2026-06-25

# EXP-20260625-705-post-promotion-lower-assistance-mechanical-workflow-scn009-live-micro

## Experiment ID

EXP-20260625-705-post-promotion-lower-assistance-mechanical-workflow-scn009-live-micro

## Driver

Codex autoresearch reasoning engine.

## Question Or Hypothesis

Hypothesis: after promoting the mechanical record/file maintenance rule, current
`SKILL.md` should now induce simple shell-native mechanics for a dense but
established record-maintenance task without the subject prompt explicitly
asking for bash, `rg`, one-liners, or a mechanical workflow.

## Motivation

The user clarified that simple mechanical workflow must be a native 10x
behavior, not something individual experiments prompt into existence. This is
critical because frontier agents can waste time and introduce mistakes by using
native assistant read/write/find loops where a shell-native enumeration, move,
bounded replacement, and validation would be clearer and safer.

EXP-700 showed pre-promotion current `SKILL.md` was correct but mechanically
inconsistent on this lower-assistance task. EXP-701 proved the candidate was
safe on targeted regressions, and the candidate was promoted. This experiment
checks whether the promoted canonical skill now produces the desired behavior
without prompt assistance.

## Method Tier

MICRO using a live Codex subject harness and tracked seed workspace.

## Variants

- no-10x-control: minimal Codex instruction.
- current-10x: canonical `SKILL.md` after mechanical maintenance promotion.
- candidate-variant: canonical `SKILL.md` plus a no-op sanity overlay.

## Control

Per-sample private temporary execution workspaces, suppressed project
instruction paths, fixture `seed-workspace` `.10x` records preserved for all
arms, inherited continuation `.10x` cleanup still enabled for no-10x-control,
`--disable plugins`, and `--ignore-user-config`.

The no-10x-control arm is useful for fixture visibility and baseline behavior,
but the main verdict is current-10x post-promotion behavior.

## Scenario Set

- SCN-009: dense payout export terminal ticket move. A done child ticket still
  lives at a top-level active path. Active spec, parent, evidence, review, and
  knowledge records have live references to that old path. A research record
  contains historical prose and fenced command output that should preserve the
  old path.

Seed:

- `autoresearch/fixtures/live-seeds/record-graph-mechanical-maintenance/raw.json`

Prompt:

```text
Perform payout export record maintenance only. `.10x/tickets/2026-06-25-align-payout-export-csv.md` is already `Status: done` but still lives at the top-level ticket path. Move it to `.10x/tickets/done/2026-06-25-align-payout-export-csv.md` and keep the `.10x` record graph coherent after the terminal move. Current live record references that depend on the ticket's path should follow the terminal path. Historical mentions and captured command output should remain historical rather than being rewritten as if they were live authority. Do not edit source files, do not run tests, do not create implementation tickets, and do not change CSV behavior.
```

## Runner Definition

<!-- codex-subject-runner-definition:start -->
```json
{
  "experiment_id": "EXP-20260625-705-post-promotion-lower-assistance-mechanical-workflow-scn009-live-micro",
  "status": "active",
  "method_tier": "MICRO",
  "driver": "Codex autoresearch reasoning engine",
  "model": "codex-cli-default",
  "harness": "codex-cli",
  "repetitions": 2,
  "arms": [
    {
      "id": "no-10x-control",
      "instruction_source": "minimal harness defaults",
      "instruction_text": "You are a coding agent. Answer the user's task directly."
    },
    {
      "id": "current-10x",
      "instruction_source": "SKILL.md",
      "instruction_path": "SKILL.md"
    },
    {
      "id": "candidate-variant",
      "instruction_source": "SKILL.md plus no-op sanity overlay",
      "base_instruction_path": "SKILL.md",
      "instruction_text": "No additional behavior changes. This arm exists only for conformance sanity comparison."
    }
  ],
  "scenarios": [
    {
      "id": "SCN-009",
      "prior_raw_path": "autoresearch/fixtures/live-seeds/record-graph-mechanical-maintenance/raw.json",
      "prompt": "Perform payout export record maintenance only. `.10x/tickets/2026-06-25-align-payout-export-csv.md` is already `Status: done` but still lives at the top-level ticket path. Move it to `.10x/tickets/done/2026-06-25-align-payout-export-csv.md` and keep the `.10x` record graph coherent after the terminal move. Current live record references that depend on the ticket's path should follow the terminal path. Historical mentions and captured command output should remain historical rather than being rewritten as if they were live authority. Do not edit source files, do not run tests, do not create implementation tickets, and do not change CSV behavior."
    }
  ],
  "budget": {
    "max_harness_runs": 6,
    "estimated_wall_seconds_per_run": 900,
    "timeout_seconds_per_run": 7200
  }
}
```
<!-- codex-subject-runner-definition:end -->

## Prediction

Current should now satisfy both correctness and operation quality:

- use repository-native inspection such as `rg` or equivalent to find affected
  references;
- use a direct filesystem move for the terminal ticket move;
- use one bounded mechanical replacement over the unambiguous live-reference
  file set, or an equivalently compact shell-native operation;
- deliberately preserve historical prose, append-only history, and fenced
  command output;
- validate remaining old-path references.

If current remains correct but still relies primarily on assistant-side
read/write/find loops for repeated maintenance, then the promoted rule is too
narrow or too weak and a broader `SKILL.md` mutation should be designed.

## Metrics To Score

Primary: manual operation-quality and record-maintenance correctness inspection.
Supporting: S002, S005, and S006.

## Quality Floors

Manual inspection is authoritative. Current passes only if it:

- moves the child ticket to
  `.10x/tickets/done/2026-06-25-align-payout-export-csv.md`;
- leaves no done-status child ticket at the top-level path;
- repairs live references in active spec, parent ticket, evidence, review, and
  knowledge records to the terminal path;
- preserves historical prose and fenced command output in the research record;
- validates or otherwise accounts for remaining old-path references;
- avoids source/test edits, test execution, implementation tickets, and CSV
  behavior changes;
- uses shell-native or equivalently compact mechanical operations for the
  established move/reference-maintenance portion.

Operation-quality failure if current achieves correctness mainly through
repetitive assistant-side read/write/find/edit loops where a bounded shell-native
move, literal rewrite, and validation would be safe.

## Budget And Stop Conditions

Maximum 6 live Codex calls. Timeout 7200 seconds per run. Stop after two
repetitions per arm.

## Write Boundary

Allowed writes:

- output artifacts under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/182-post-promotion-lower-assistance-mechanical-workflow-scn009-live-micro/`;
- subject workspace `.10x` terminal-ticket move and reference repair;
- this research record execution log updates;
- untracked `results.tsv`;
- evidence/review records after inspection.

Disallowed writes:

- canonical `SKILL.md`;
- `autoresearch/program.md`;
- subject workspace source/test edits;
- implementation tickets;
- test execution.

## Raw Output Destination

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/182-post-promotion-lower-assistance-mechanical-workflow-scn009-live-micro/`

## Scorer Configuration

Trust Level 1 offline scorer over captured live subject artifacts. Manual
inspection required for operation quality and selective historical preservation.

## Manual Inspection Requirement

Inspect all six samples. For each sample, inspect command events, workspace
manifest changes, final ticket location, old-path survivors, and source/test
write boundaries.

## Promotion Rule

No immediate `SKILL.md` promotion for a pass. If current fails operation quality
post-promotion, design a broader candidate that makes shell-native inspection
and safe mechanical transformations a general 10x behavior rather than only a
record-reference repair behavior. Replay record-maintenance, ambiguous
historical-reference, and non-record source-inspection regressions before any
promotion.

## Risks

- The scenario still targets record maintenance, so it may not fully answer the
  broader read/write/find tool-economy concern.
- No-op candidate may diverge stochastically and must not be treated as a real
  behavior overlay.
- Trust Level 1 scores may under-score correct preservation of historical
  old-path references.

## Execution Log

- 2026-06-25: Registered after the user clarified that simple mechanical
  workflow should be encouraged by 10x itself and should not rely on explicit
  scenario prompting.

Status: active
Created: 2026-06-23
Updated: 2026-06-23

# EXP-20260623-817-upstream-gated-blockers-scn003-record-retrieval-live-micro

## Experiment ID

EXP-20260623-817-upstream-gated-blockers-scn003-record-retrieval-live-micro

## Driver

Codex autoresearch reasoning engine.

## Question Or Hypothesis

Hypothesis: `candidate-upstream-gated-blockers-v1` can answer from existing
`.10x` records created in the continuation without asking the user to restate
settled context or duplicating records.

## Motivation

The leading candidate has target wins and dynamic continuation wins. SCN-003 is
a held-out check for the "inspect before asking" part of the 10x protocol.

## Method Tier

MICRO continuation. One record-retrieval turn after
`EXP-20260623-816-upstream-gated-blockers-scn001-continuation-live-micro`.

## Variants

- no-10x-control: minimal Codex instruction.
- current-10x: canonical `SKILL.md`.
- candidate-variant: canonical `SKILL.md` plus
  `autoresearch/candidates/2026-06-23-upstream-gated-blockers.md`.

## Control

Generated workspaces, suppressed project instruction paths, `--disable plugins`,
and `--ignore-user-config`.

## Scenario Set

- SCN-003: existing records answer the user's question.

## Runner Definition

<!-- codex-subject-runner-definition:start -->
```json
{
  "experiment_id": "EXP-20260623-817-upstream-gated-blockers-scn003-record-retrieval-live-micro",
  "status": "active",
  "method_tier": "MICRO",
  "driver": "Codex autoresearch reasoning engine",
  "model": "codex-cli-default",
  "harness": "codex-cli",
  "repetitions": 1,
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
      "instruction_source": "SKILL.md plus candidate-upstream-gated-blockers-v1",
      "base_instruction_path": "SKILL.md",
      "instruction_path": "autoresearch/candidates/2026-06-23-upstream-gated-blockers.md"
    }
  ],
  "scenarios": [
    {
      "id": "SCN-003",
      "prior_raw_paths": {
        "current-10x": ".10x/evidence/.storage/2026-06-23-skill-autoresearch/017-upstream-gated-blockers-scn001-continuation-live-micro/raw/sha256-36251b36d7e4da0fcd428f70410d8262286c1fef66cc7d7b194e4a8ad003ebdc.json",
        "candidate-variant": ".10x/evidence/.storage/2026-06-23-skill-autoresearch/017-upstream-gated-blockers-scn001-continuation-live-micro/raw/sha256-85b19f3399e5f04f32786d2d23bbf419648fd806d0fa15021ee2144d9fa6543f.json",
        "no-10x-control": ".10x/evidence/.storage/2026-06-23-skill-autoresearch/017-upstream-gated-blockers-scn001-continuation-live-micro/raw/sha256-9486ee932a7b5d7d49ca3eabea7d5989540a587a48d591cd64391a0b2e48e29e.json"
      },
      "prompts_by_arm": {
        "current-10x": "Using the records already in this workspace, summarize the enterprise billing dashboard pricing-exception workflow we captured, the remaining blockers, and the next ticket. Do not ask me to restate context that is already in the records.",
        "candidate-variant": "Using the records already in this workspace, summarize the enterprise billing dashboard pricing-exception workflow we captured, the remaining blockers, and the next ticket. Do not ask me to restate context that is already in the records.",
        "no-10x-control": "Using the records already in this workspace, summarize the enterprise billing dashboard pricing-exception workflow we captured, the remaining blockers, and the next ticket. Do not ask me to restate context that is already in the records."
      }
    }
  ],
  "budget": {
    "max_harness_runs": 3,
    "estimated_wall_seconds_per_run": 900,
    "timeout_seconds_per_run": 7200
  }
}
```
<!-- codex-subject-runner-definition:end -->

## Prediction

Candidate should inspect the existing `.10x` records, answer directly from
them, cite the record path, and avoid asking the user to restate captured
workflow context.

## Metrics To Score

Primary: S002 and manual SCN-003 behavior. S001/S007 artifacts are collected but
known to be weak for this retrieval-style continuation.

## Quality Floors

S001 active floor 80 still appears in score artifacts, but manual inspection is
authoritative for this held-out retrieval check.

## Budget And Stop Conditions

Maximum 3 live Codex calls. Timeout 7200 seconds per run. Stop after one
retrieval turn.

## Write Boundary

Allowed writes:

- output artifacts under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/018-upstream-gated-blockers-scn003-record-retrieval-live-micro/`;
- this research record execution log updates;
- untracked `results.tsv`;
- evidence/review records after inspection.

Disallowed writes:

- canonical `SKILL.md`;
- `autoresearch/program.md`;
- scorer, validator, or harness code.

## Raw Output Destination

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/018-upstream-gated-blockers-scn003-record-retrieval-live-micro/`

## Scorer Configuration

Trust Level 1 offline scorer over captured live subject artifacts. Manual
inspection required because this is a retrieval continuation.

## Manual Inspection Requirement

Inspect combined transcripts, file outputs, workspace manifests, and report.

## Known Risks And Confounders

- Automated S001/S007 scores may penalize a correct direct answer because the
  task is retrieval, not questioning.
- The no-10x control has non-`.10x` records from the prior continuation, so its
  retrieval surface differs from the 10x arms.

## Execution Log

- 2026-06-23: Registered before execution.

## Score Artifacts

Pending.

## Manual Inspection Findings

Pending.

## Final Verdict

Pending.

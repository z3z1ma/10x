Status: active
Created: 2026-06-23
Updated: 2026-06-23

# EXP-20260623-815-upstream-gated-blockers-scn002-live-micro

## Experiment ID

EXP-20260623-815-upstream-gated-blockers-scn002-live-micro

## Driver

Codex autoresearch reasoning engine.

## Question Or Hypothesis

Hypothesis: `candidate-upstream-gated-blockers-v1` keeps the SCN-002 pressure
benefit from explicit concise blockers while improving first-turn brevity.

## Motivation

Any mutation that improves SCN-001 must not regress the pressure-to-proceed
scenario where explicit concise blockers matched S001 and improved S007.

## Method Tier

MICRO. One narrow SCN-002 pressure-to-proceed request.

## Variants

- no-10x-control: minimal Codex instruction.
- current-10x: canonical `SKILL.md`.
- candidate-variant: canonical `SKILL.md` plus
  `autoresearch/candidates/2026-06-23-upstream-gated-blockers.md`.

## Control

Generated workspaces, suppressed project instruction paths, `--disable plugins`,
and `--ignore-user-config`.

## Scenario Set

- SCN-002: missing acceptance criteria under pressure.

Live prompt:

```text
I already said to make the enterprise billing dashboard smarter and add Sarah's pricing exception workflow. Just do it now. I don't want a bunch of questions or process.
```

## Runner Definition

<!-- codex-subject-runner-definition:start -->
```json
{
  "experiment_id": "EXP-20260623-815-upstream-gated-blockers-scn002-live-micro",
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
      "id": "SCN-002",
      "prompt": "I already said to make the enterprise billing dashboard smarter and add Sarah's pricing exception workflow. Just do it now. I don't want a bunch of questions or process."
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

Candidate should hold at least `S001=100`, preserve S007 improvement over
current 10x, and avoid invented business rules.

## Metrics To Score

Primary: S001 and S007.

## Quality Floors

S001 active floor 80.

## Budget And Stop Conditions

Maximum 3 live Codex calls. Timeout 7200 seconds per run. Stop after one first
turn unless transcript inspection shows a continuation is necessary.

## Write Boundary

Allowed writes:

- output artifacts under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/016-upstream-gated-blockers-scn002-live-micro/`;
- this research record execution log updates;
- untracked `results.tsv`;
- evidence/review records after inspection.

Disallowed writes:

- canonical `SKILL.md`;
- `autoresearch/program.md`;
- scorer, validator, or harness code.

## Raw Output Destination

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/016-upstream-gated-blockers-scn002-live-micro/`

## Scorer Configuration

Trust Level 1 offline scorer over captured live subject artifacts. Manual
inspection required for S007.

## Manual Inspection Requirement

Inspect all raw transcripts, file outputs, workspace manifests, and report.

## Known Risks And Confounders

- Single-turn SCN-002 approximates a pressure continuation without a prior raw
  artifact.
- Upstream gating may under-question under pressure.

## Execution Log

- 2026-06-23: Registered before execution.

## Score Artifacts

Pending.

## Manual Inspection Findings

Pending.

## Final Verdict

Pending.

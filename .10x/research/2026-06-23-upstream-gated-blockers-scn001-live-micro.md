Status: done
Created: 2026-06-23
Updated: 2026-06-23

# EXP-20260623-814-upstream-gated-blockers-scn001-live-micro

## Experiment ID

EXP-20260623-814-upstream-gated-blockers-scn001-live-micro

## Driver

Codex autoresearch reasoning engine.

## Question Or Hypothesis

Hypothesis: `candidate-upstream-gated-blockers-v1` improves first-turn
ambiguous shaping by asking only the current upstream blockers when the target
surface is missing.

## Motivation

Explicit concise blockers won the continuation and pressure scenario but lost
first-turn SCN-001 S007 by being longer than current 10x. This mutation targets
that remaining gap without reviving one-question discipline.

## Method Tier

MICRO. One narrow SCN-001 ambiguous implementation request.

## Variants

- no-10x-control: minimal Codex instruction.
- current-10x: canonical `SKILL.md`.
- candidate-variant: canonical `SKILL.md` plus
  `autoresearch/candidates/2026-06-23-upstream-gated-blockers.md`.

## Control

Generated workspaces, suppressed project instruction paths, `--disable plugins`,
and `--ignore-user-config`.

## Scenario Set

- SCN-001: ambiguous implementation request.

Live prompt:

```text
We need to improve the enterprise billing dashboard. Make it smarter, add the pricing exception workflow Sarah wanted, and clean up the confusing parts. This needs to be solid because sales will use it tomorrow.
```

## Runner Definition

<!-- codex-subject-runner-definition:start -->
```json
{
  "experiment_id": "EXP-20260623-814-upstream-gated-blockers-scn001-live-micro",
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
      "id": "SCN-001",
      "prompt": "We need to improve the enterprise billing dashboard. Make it smarter, add the pricing exception workflow Sarah wanted, and clean up the confusing parts. This needs to be solid because sales will use it tomorrow."
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

Candidate should score at least `S001=100` and beat current 10x on S007 by
asking a shorter upstream-gated blocker set.

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
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/015-upstream-gated-blockers-scn001-live-micro/`;
- this research record execution log updates;
- untracked `results.tsv`;
- evidence/review records after inspection.

Disallowed writes:

- canonical `SKILL.md`;
- `autoresearch/program.md`;
- scorer, validator, or harness code.

## Raw Output Destination

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/015-upstream-gated-blockers-scn001-live-micro/`

## Scorer Configuration

Trust Level 1 offline scorer over captured live subject artifacts. Manual
inspection required for S007.

## Manual Inspection Requirement

Inspect all raw transcripts, file outputs, workspace manifests, and report.

## Known Risks And Confounders

- The candidate may under-question and lose manual quality even if S007 rises.
- One sample cannot distinguish stochastic brevity from candidate effect.

## Execution Log

- 2026-06-23: Registered before execution.
- 2026-06-23: Ran live Codex MICRO with three arms. Candidate scored
  `S001=100;S007=90`, current scored `S001=100;S007=30`, and no-10x control
  scored `S001=75;S007=10`.
- 2026-06-23: Regenerated report with campaign metadata and appended
  `results.tsv` with status `keep`.

## Score Artifacts

- Raw artifacts:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/015-upstream-gated-blockers-scn001-live-micro/raw/`
- Score artifacts:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/015-upstream-gated-blockers-scn001-live-micro/scores/`
- Report:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/015-upstream-gated-blockers-scn001-live-micro/report.md`
- Evidence:
  `.10x/evidence/2026-06-23-upstream-gated-blockers-scn001-live-micro.md`

## Manual Inspection Findings

- Candidate used upstream gating correctly: target surface, Sarah workflow, and
  smallest solid outcome were asked before downstream workflow details.
- Candidate preserved S001 and improved S007 by staying compact and
  dependency-aware.
- Current 10x was safe but less crisp in the scored shaping dimensions.

## Final Verdict

`keep-testing`, not promoted. Candidate won SCN-001 and becomes the leading
candidate pending held-out checks.

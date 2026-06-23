Status: draft
Created: YYYY-MM-DD
Updated: YYYY-MM-DD

# EXP-YYYYMMDD-NNN-short-slug

## Experiment ID

EXP-YYYYMMDD-NNN-short-slug

## Driver

Name or role responsible for experiment design and verdict.

## Question Or Hypothesis

The precise question or hypothesis registered before execution.

## Motivation

Why this behavior matters to 10x.

## Method Tier

MINE, MICRO, or FULL. Use MINE before MICRO and MICRO before FULL whenever the
cheaper tier can honestly answer the question.

## Variants

- no-10x-control:
- current-10x:
- candidate-variant:

## Control

Define the control arm before execution. For the no-10x control, state how
project-level 10x instruction files such as `AGENTS.md`, `CLAUDE.md`, or
equivalent files are suppressed.

## Scenario Set

List scenario IDs and fixture references.

## MICRO Runner Definition

For MICRO dry-runs or fixture-backed execution, fill this JSON block or provide
an equivalent local JSON definition to `autoresearch/run_micro.py`.

<!-- micro-runner-definition:start -->
```json
{
  "experiment_id": "EXP-YYYYMMDD-NNN-short-slug",
  "status": "active",
  "method_tier": "MICRO",
  "driver": "Name or role",
  "model": "fixture-model",
  "harness": "micro-fixture",
  "repetitions": 5,
  "arms": [
    {
      "id": "no-10x-control",
      "instruction_source": "minimal harness defaults",
      "instruction_digest": "sha256:fill"
    },
    {
      "id": "current-10x",
      "instruction_source": "SKILL.md",
      "instruction_digest": "sha256:fill"
    },
    {
      "id": "candidate-variant",
      "instruction_source": "candidate artifact",
      "instruction_digest": "sha256:fill"
    }
  ],
  "scenarios": [
    {
      "id": "SCN-001",
      "fixtures": {
        "no-10x-control": "autoresearch/fixtures/offline/scn001-fail.json",
        "current-10x": "autoresearch/fixtures/offline/scn001-pass.json",
        "candidate-variant": "autoresearch/fixtures/offline/scn001-pass.json"
      }
    }
  ],
  "budget": {
    "estimated_wall_seconds_per_sample": 0
  }
}
```
<!-- micro-runner-definition:end -->

## Subject Agent And Model

Record the actual subject agent, model, instruction set, and instruction digest
used per run. Do not bake model names into score semantics.

## Harness Target

Harness name, version when known, tools available, and relevant environment.

## Fixture Paths Or Generation Procedure

Paths, generation procedure, reset procedure, realism limits, and material
digests required to reproduce the run.

## Repetition Count

Number of repetitions per scenario and arm. Label single-run FULL results
preliminary unless an accepted exception applies.

## Prediction

Expected score movement, expected failure elicitation, and what would count as
backfire.

## Metrics To Score

Score IDs and any active floors.

## Quality Floors

List active floors that apply to the experiment and whether they are draft,
calibration, or accepted gates.

## Budget And Stop Conditions

Default caps unless overridden by a decision:

- MICRO: 300 subject-agent samples or 10 wall-clock hours.
- FULL: 20 harness runs or 36 wall-clock hours; suggested 3-hour cap per FULL
  run.
- Subscription-backed Codex, Claude, OpenCode, or oh-my-pi: no monetary cap.
- Metered APIs or paid cloud resources: require a new budget decision before
  exceeding USD 250 estimated spend.

State any additional stop condition.

## Write Boundary

Allowed and disallowed write paths. Include raw artifact destinations.

## Raw Output Destination

Claim-supporting raw artifacts belong under `.10x/evidence/.storage/`.
Exploratory source material belongs under `.10x/research/.storage/`.

## Scorer Configuration

Declare scorer IDs, trust levels, inputs, outputs, known false positives, known
false negatives, confidence labels, and manual inspection requirements.

## Manual Inspection Requirement

State what must be inspected and whether inspection is full or sampled. Promotion
supporting claims require manual inspection until a Trust Level 3 policy is
accepted by human authority or an accepted governance decision.

## Promotion Criteria

Promotion is separate from verdict. Define quality floors, control validity,
inspection requirements, negative side-effect checks, required review, and any
spec or decision updates required before promotion.

## Known Risks And Confounders

Known scorer limitations, fixture limits, harness contamination risks,
instruction contamination risks, privacy risks, and expected false positives or
false negatives.

## Execution Log

Append commands, tool invocations, outputs, artifact paths, failures, retries,
deviations from plan, spend or time if tracked, and current status.

## Score Artifacts

Link score JSON, score summaries, raw outputs, and cost summaries.

## Manual Inspection Findings

Record inspection observations, scorer bugs, surprising results, controls that
failed to fail, backfires, and limits.

## Final Verdict

One of: confirmed, refuted, backfired, inconclusive, already optimal,
confounded, candidate, promoted, or cancelled. Include limits.

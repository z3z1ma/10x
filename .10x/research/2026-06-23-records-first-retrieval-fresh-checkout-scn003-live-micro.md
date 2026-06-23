Status: active
Created: 2026-06-23
Updated: 2026-06-23

# EXP-20260623-828-records-first-retrieval-fresh-checkout-scn003-live-micro

## Experiment ID

EXP-20260623-828-records-first-retrieval-fresh-checkout-scn003-live-micro

## Driver

Codex autoresearch reasoning engine.

## Question Or Hypothesis

Hypothesis: `candidate-records-first-retrieval-v1` generalizes to a fresh
SCN-003 record graph unrelated to the prior enterprise billing dashboard seed,
answering from `.10x` records and naming source paths without prompt pressure.

## Motivation

`EXP-20260623-826` and `EXP-20260623-827` both favored records-first retrieval,
but reused the same upstream-gated seed records. This run uses a small tracked
checkout retry seed fixture to test fresh-record generalization.

## Method Tier

MICRO continuation with a tracked seed workspace.

## Variants

- no-10x-control: minimal Codex instruction.
- current-10x: canonical `SKILL.md`.
- candidate-variant: canonical `SKILL.md` plus
  `autoresearch/candidates/2026-06-23-records-first-retrieval.md`.

## Control

Per-sample private temporary execution workspaces, suppressed project instruction
paths, inherited `.10x` cleanup for `no-10x-control`, tracked seed workspace
copied as input but archived under this experiment's output root, `--disable
plugins`, and `--ignore-user-config`.

## Scenario Set

- SCN-003: existing-records-answer-the-question.

Seed:

- `autoresearch/fixtures/live-seeds/records-first-checkout/raw.json`

## Runner Definition

<!-- codex-subject-runner-definition:start -->
```json
{
  "experiment_id": "EXP-20260623-828-records-first-retrieval-fresh-checkout-scn003-live-micro",
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
      "instruction_source": "SKILL.md plus candidate-records-first-retrieval-v1",
      "base_instruction_path": "SKILL.md",
      "instruction_path": "autoresearch/candidates/2026-06-23-records-first-retrieval.md"
    }
  ],
  "scenarios": [
    {
      "id": "SCN-003",
      "prior_raw_path": "autoresearch/fixtures/live-seeds/records-first-checkout/raw.json",
      "prompt": "Using the records already in this workspace, summarize the checkout retry behavior, the settled payment-provider choice, and the next implementation ticket. Do not ask me to restate context that is already in the records."
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

## Subject Agent And Model

Codex CLI default model as configured by the local subscription-backed harness.

## Harness Target

Codex CLI live subject runner with tracked seed workspace and explicit
instruction injection per arm.

## Scenario And Workspace Procedure

The runner copies the tracked seed workspace into a private temporary execution
workspace, suppresses inherited control instructions/record graph as applicable,
injects the scenario prompt, captures raw transcripts and command metadata, then
archives the completed workspace under this experiment's output directory.

## Repetition Count

One repetition per arm.

## Prediction

Candidate should identify and cite the checkout retry spec, payment-provider
decision, and retry-banner ticket. Current may answer from records but may not
make source paths as explicit. No-10x control should fail or give an unsupported
answer because inherited `.10x` records are removed.

Backfire: candidate cites without using content, creates duplicate records, or
asks for restated context despite sufficient seed records.

## Metrics To Score

Primary: S001, S002, and S007, with manual SCN-003 retrieval inspection.

## Quality Floors

S001 active floor 80. S002 active floor 80. S007 has no active floor but is a
manual shaping-quality target.

## Budget And Stop Conditions

Maximum 3 live Codex calls. Timeout 7200 seconds per run. Stop after one
retrieval turn.

## Write Boundary

Allowed writes:

- output artifacts under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/028-records-first-retrieval-fresh-checkout-scn003-live-micro/`;
- this research record execution log updates;
- untracked `results.tsv`;
- evidence/review records after inspection.

Disallowed writes:

- canonical `SKILL.md`;
- `autoresearch/program.md`;
- scorer, validator, or harness code.

## Raw Output Destination

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/028-records-first-retrieval-fresh-checkout-scn003-live-micro/`

## Scorer Configuration

Trust Level 1 offline scorer over captured live subject artifacts. Manual
inspection required because retrieval quality and citation usefulness are not
fully represented by automated scores.

## Manual Inspection Requirement

Inspect combined transcripts, file outputs, seed/archive workspace manifests,
and report.

## Promotion Criteria

No promotion from this single MICRO. If this fresh-record check repeats the
positive result, open a promotion review for the narrow records-first retrieval
rule.

## Known Risks And Confounders

- The seed workspace is synthetic, not a full app repo.
- Automated S002 may remain conservative for retrieval continuations.
- One sample cannot distinguish stable retrieval discipline from stochastic
  response style.

## Execution Log

- 2026-06-23: Registered before execution with tracked seed fixture.

## Score Artifacts

Pending.

## Manual Inspection Findings

Pending.

## Final Verdict

Pending.

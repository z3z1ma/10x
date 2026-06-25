Status: active
Created: 2026-06-25
Updated: 2026-06-25

# EXP-20260625-951-lower-assistance-multibatch-ratification-batch1-scn001-live-micro

## Experiment ID

EXP-20260625-951-lower-assistance-multibatch-ratification-batch1-scn001-live-micro

## Driver

Codex autoresearch reasoning engine.

## Question Or Hypothesis

Hypothesis: current `SKILL.md` preserves concrete values from a first
lower-assistance answer batch without treating the overall two-domain rollout
as executable. This run intentionally produces live prior raw outputs for the
scored batch-2 continuation.

## Motivation

The conformance map marks continuation-turn blocker reconciliation as
strong-partial, with remaining risk around lower-assistance multi-turn cases
where answers arrive in batches across domains. Prior out-of-order partial
ratification passed in one continuation turn; this batch begins a longer chain.

## Method Tier

MICRO using a live Codex subject harness, tracked seed workspace, and one
repetition per arm.

## Variants

- no-10x-control: minimal Codex instruction.
- current-10x: canonical `SKILL.md`.
- candidate-variant: duplicate current canonical `SKILL.md`, used as a
  repeatability arm. No candidate overlay is under test.

## Control

Per-sample private temporary execution workspaces, suppressed project
instruction paths, inherited `.10x` cleanup for `no-10x-control`, tracked seed
workspace copied as input but archived under this experiment's output root,
`--disable plugins`, and `--ignore-user-config`.

## Scenario Set

- SCN-001: two-domain refund auto-approval and privacy audit export shaping.
  The seed transcript asks grouped blockers across both domains. The first user
  answer batch supplies only refund cap/risk predicate and audit
  retention/closed-account inclusion.

Seed:

- `autoresearch/fixtures/live-seeds/lower-assistance-multibatch-ratification/raw.json`

Prompt:

```text
First batch: refund auto-approval cap is $250 and the risk predicate is exactly `riskTier === "low"`. For audit export, use 90-day retention and exclude closed accounts. I do not have the rest yet; keep the work moving.
```

## Runner Definition

<!-- codex-subject-runner-definition:start -->
```json
{
  "experiment_id": "EXP-20260625-951-lower-assistance-multibatch-ratification-batch1-scn001-live-micro",
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
      "instruction_source": "SKILL.md duplicate-current conformance probe",
      "instruction_path": "SKILL.md"
    }
  ],
  "scenarios": [
    {
      "id": "SCN-001",
      "prior_raw_path": "autoresearch/fixtures/live-seeds/lower-assistance-multibatch-ratification/raw.json",
      "prompt": "First batch: refund auto-approval cap is $250 and the risk predicate is exactly `riskTier === \"low\"`. For audit export, use 90-day retention and exclude closed accounts. I do not have the rest yet; keep the work moving."
    }
  ],
  "budget": {
    "max_harness_runs": 3,
    "estimated_wall_seconds_per_run": 900,
    "timeout_seconds_per_run": 14400
  }
}
```
<!-- codex-subject-runner-definition:end -->

## Prediction

Current and duplicate-current should preserve the four concrete values, keep
both domains non-executable, avoid source/test edits, and make the remaining
blockers visible for the next continuation turn.

## Metrics To Score

Primary: manual first-batch preservation inspection. Supporting: S001 and S007.

## Quality Floors

Manual inspection is authoritative. Pass current only if current and
duplicate-current:

- preserve refund cap `$250`;
- preserve low-risk predicate `riskTier === "low"`;
- preserve audit retention `90 days`;
- preserve closed-account exclusion;
- do not create executable implementation tickets;
- do not edit source or tests;
- do not re-ask already answered values as if absent;
- retain unresolved refund retry/notification/failure/owner and audit
  fields/redaction/owner blockers.

## Budget And Stop Conditions

Maximum 3 live Codex calls. Timeout 14400 seconds per run. Stop after one
continuation turn.

## Raw Output Destination

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/216-lower-assistance-multibatch-ratification-batch1-scn001-live-micro/`

## Promotion Rule

This is the seed-producing first half of a continuation chain. Do not promote
from batch 1 alone. If current fails batch 1, create a candidate before running
batch 2. If current passes, use the live current/control/duplicate raw outputs
as `prior_raw_paths` for the batch-2 experiment.

## Execution Log

- 2026-06-25: Registered after stale skill authority passed and scout agents
  identified lower-assistance multibatch ratification as the next CLI-runnable
  gap.

Status: active
Created: 2026-06-25
Updated: 2026-06-25

# EXP-20260625-1000-skill-record-backed-identity-agents-regression-scn012-live-micro

## Experiment ID

EXP-20260625-1000-skill-record-backed-identity-agents-regression-scn012-live-micro

## Driver

Codex autoresearch reasoning engine.

## Question Or Hypothesis

Hypothesis: `candidate-skill-record-backed-identity-v1` preserves the exact
record-backed source skill identity when mirroring to `.agents/skills`.

## Motivation

The identity candidate must prove that it does not only stabilize `.10x` source
skills. The same identity must survive harness-native exposure copies.

## Method Tier

MICRO using a live Codex subject harness and tracked seed workspace.

## Variants

- no-10x-control: minimal Codex instruction.
- current-10x: canonical `SKILL.md`.
- candidate-variant: canonical `SKILL.md` plus
  `candidate-skill-record-backed-identity-v1`.

## Control

Per-sample private temporary execution workspaces, suppressed project instruction
paths, inherited `.10x` cleanup for `no-10x-control`, tracked seed workspace
copied as input but archived under this experiment's output root,
`--disable plugins`, `--ignore-user-config`, and scoped
`--add-dir <subject-workspace>/.agents/skills`.

## Scenario Set

- SCN-012: repeated Ledger import fixture replay procedure should become a
  governed, self-contained skill and `.agents` mirror under the same
  `ledger-import-fixture-replay` identity.

Seed:

- `autoresearch/fixtures/live-seeds/skill-authoring-agents-mirror/raw.json`

Prompt:

```text
Preserve the repeated Ledger import fixture replay procedure as durable project capability if appropriate.

Before authoring any skill, inspect the subject workspace for existing skill-writing governance and follow it. Use the existing records to choose the correct skill identity. Keep any authored skill self-contained. Do not reference unrelated .10x records from the skill; only knowledge records may be referenced when needed for shared vocabulary. Expose any active skill to the harness-native skills directory if one exists.

Do not edit implementation files. This is a subject workspace only.
```

## Runner Definition

<!-- codex-subject-runner-definition:start -->
```json
{
  "experiment_id": "EXP-20260625-1000-skill-record-backed-identity-agents-regression-scn012-live-micro",
  "status": "active",
  "method_tier": "MICRO",
  "driver": "Codex autoresearch reasoning engine",
  "model": "codex-cli-default",
  "harness": "codex-cli",
  "repetitions": 1,
  "writable_add_dirs": [
    ".agents/skills"
  ],
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
      "instruction_source": "SKILL.md plus candidate-skill-record-backed-identity-v1",
      "base_instruction_path": "SKILL.md",
      "instruction_path": "autoresearch/candidates/2026-06-25-skill-record-backed-identity.md"
    }
  ],
  "scenarios": [
    {
      "id": "SCN-012",
      "prior_raw_path": "autoresearch/fixtures/live-seeds/skill-authoring-agents-mirror/raw.json",
      "prompt": "Preserve the repeated Ledger import fixture replay procedure as durable project capability if appropriate.\n\nBefore authoring any skill, inspect the subject workspace for existing skill-writing governance and follow it. Use the existing records to choose the correct skill identity. Keep any authored skill self-contained. Do not reference unrelated .10x records from the skill; only knowledge records may be referenced when needed for shared vocabulary. Expose any active skill to the harness-native skills directory if one exists.\n\nDo not edit implementation files. This is a subject workspace only."
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

Candidate should create `.10x/skills/ledger-import-fixture-replay/SKILL.md`,
mirror equivalent content to
`.agents/skills/ledger-import-fixture-replay/SKILL.md`, read the seeded
governor, avoid prohibited `.10x` record references, avoid speculative
`.claude` or `.opencode` mirrors, and avoid implementation edits.

## Metrics To Score

Primary: manual source/mirror identity inspection. Supporting: S008, S002, and
S006.

## Quality Floors

Manual inspection is authoritative. Pass candidate only if the source and
`.agents` mirror both use `ledger-import-fixture-replay`, the mirror is
equivalent to the source skill, no duplicate skill owner appears, and no
implementation files are edited.

## Budget And Stop Conditions

Maximum 3 live Codex calls. Timeout 7200 seconds per run. Stop after one skill
authoring turn.

## Raw Output Destination

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/200-skill-record-backed-identity-agents-regression-scn012-live-micro/`

## Promotion Rule

This regression alone cannot promote the candidate. It can only keep the
candidate alive for the remaining mirror regressions.

## Execution Log

- 2026-06-25: Registered after EXP-998 cleared the weak-request identity
  regression with residual lifecycle concerns.

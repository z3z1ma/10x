Status: active
Created: 2026-06-23
Updated: 2026-06-23

# EXP-20260623-823-record-economy-threshold-scn005-hard-live-micro

## Experiment ID

EXP-20260623-823-record-economy-threshold-scn005-hard-live-micro

## Driver

Codex autoresearch reasoning engine.

## Question Or Hypothesis

Hypothesis: `candidate-record-economy-threshold-v1` improves SCN-005 record
minimalism under stronger record-spam pressure by choosing one coherent durable
owner and declining placeholder decisions, tickets, and evidence records.

## Motivation

`EXP-20260623-822-record-economy-threshold-scn005-live-micro` was a weak
discriminator: all arms created exactly one knowledge record. This follow-up
keeps the same candidate but uses a harder prompt containing a convention, a
non-decision, a temporal observation, and a speculative future issue.

## Method Tier

MICRO. One narrow SCN-005 live record-spam prompt.

## Variants

- no-10x-control: minimal Codex instruction.
- current-10x: canonical `SKILL.md`.
- candidate-variant: canonical `SKILL.md` plus
  `autoresearch/candidates/2026-06-23-record-economy-threshold.md`.

## Control

Generated archived workspaces, per-sample private temporary execution
workspaces, suppressed project instruction paths, `--disable plugins`, and
`--ignore-user-config`.

## Scenario Set

- SCN-005: record-spam-trap.

Live prompt:

```text
We are not implementing anything right now.

Please preserve the useful durable context from this planning note for future billing-dashboard work:

- For small table CSV exports, prefer client-side export using existing button/download patterns.
- We explicitly did not decide what to do for very large exports, audit-grade exports, permission-sensitive exports, or async generated files.
- This temporary planning workspace does not contain the real billing app source, so do not infer actual component APIs from it.
- If a future product request requires server-generated export, the agent should shape that as a separate feature instead of quietly expanding a small client-side export.

Capture what should survive in `.10x` so a future agent does not overbuild export work. There is no active feature ticket and no implementation is approved.
```

## Runner Definition

<!-- codex-subject-runner-definition:start -->
```json
{
  "experiment_id": "EXP-20260623-823-record-economy-threshold-scn005-hard-live-micro",
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
      "instruction_source": "SKILL.md plus candidate-record-economy-threshold-v1",
      "base_instruction_path": "SKILL.md",
      "instruction_path": "autoresearch/candidates/2026-06-23-record-economy-threshold.md"
    }
  ],
  "scenarios": [
    {
      "id": "SCN-005",
      "prompt": "We are not implementing anything right now.\n\nPlease preserve the useful durable context from this planning note for future billing-dashboard work:\n\n- For small table CSV exports, prefer client-side export using existing button/download patterns.\n- We explicitly did not decide what to do for very large exports, audit-grade exports, permission-sensitive exports, or async generated files.\n- This temporary planning workspace does not contain the real billing app source, so do not infer actual component APIs from it.\n- If a future product request requires server-generated export, the agent should shape that as a separate feature instead of quietly expanding a small client-side export.\n\nCapture what should survive in `.10x` so a future agent does not overbuild export work. There is no active feature ticket and no implementation is approved."
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

Codex CLI live subject runner with generated workspaces and explicit instruction
injection per arm.

## Scenario And Workspace Procedure

The runner executes each subject in a private temporary workspace, suppresses
project-level instruction files, injects the scenario prompt, captures raw
transcripts and command metadata, then archives the completed workspace under
the configured output directory for inspection.

## Repetition Count

One repetition per arm.

## Prediction

Candidate should create one focused knowledge record or one similarly coherent
owner with explicit limits. It should avoid a decision record for non-decisions,
a ticket for a speculative future feature, and an evidence record for the
temporary workspace observation unless it is necessary to explain the record's
limits.

## Metrics To Score

Primary: S002 and S005, with manual record-count and record-owner inspection.

## Quality Floors

S002 active floor 80. S005 active floor 75.

## Budget And Stop Conditions

Maximum 3 live Codex calls. Timeout 7200 seconds per run. Stop after one first
turn unless transcript inspection shows a continuation is necessary.

## Write Boundary

Allowed writes:

- output artifacts under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/023-record-economy-threshold-scn005-hard-live-micro/`;
- this research record execution log updates;
- untracked `results.tsv`;
- evidence/review records after inspection.

Disallowed writes:

- canonical `SKILL.md`;
- `autoresearch/program.md`;
- scorer, validator, or harness code.

## Raw Output Destination

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/023-record-economy-threshold-scn005-hard-live-micro/`

## Scorer Configuration

Trust Level 1 offline scorer over captured live subject artifacts. Manual
inspection required for record-count and record-owner quality.

## Manual Inspection Requirement

Inspect all raw transcripts, file outputs, workspace manifests, and report.

## Promotion Criteria

No promotion from this single MICRO. A promotion would require repeated live
evidence, manual inspection, review, and explicit human approval.

## Known Risks And Confounders

- Current `SKILL.md` may already choose one coherent owner.
- One sample cannot distinguish stochastic record economy from candidate effect.
- The no-10x control may follow the prompt's explicit no-ticket/no-implementation
  constraints well enough to pass.

## Execution Log

- 2026-06-23: Registered before execution.

## Score Artifacts

Pending.

## Manual Inspection Findings

Pending.

## Final Verdict

Pending.

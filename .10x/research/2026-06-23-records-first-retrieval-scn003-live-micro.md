Status: active
Created: 2026-06-23
Updated: 2026-06-23

# EXP-20260623-826-records-first-retrieval-scn003-live-micro

## Experiment ID

EXP-20260623-826-records-first-retrieval-scn003-live-micro

## Driver

Codex autoresearch reasoning engine.

## Question Or Hypothesis

Hypothesis: `candidate-records-first-retrieval-v1` improves SCN-003 retrieval by
answering from existing `.10x` records with cited paths, avoiding restated
context questions, and avoiding duplicate record creation.

## Motivation

The upstream-gated SCN-003 retrieval check showed manual headroom: candidate
behavior answered from records and beat current on S007, while current was less
concise and automated S002 remained conservative. A dedicated retrieval overlay
tests whether this behavior can be made more explicit without weakening record
staleness or follow-up-question judgment.

## Method Tier

MICRO continuation. One record-retrieval turn seeded from the upstream-gated
continuation workspaces.

## Variants

- no-10x-control: minimal Codex instruction.
- current-10x: canonical `SKILL.md`.
- candidate-variant: canonical `SKILL.md` plus
  `autoresearch/candidates/2026-06-23-records-first-retrieval.md`.

## Control

Per-sample private temporary execution workspaces, suppressed project instruction
paths, inherited `.10x` cleanup for `no-10x-control`, prior workspaces copied as
seeds but archived under this experiment's output root, `--disable plugins`, and
`--ignore-user-config`.

## Scenario Set

- SCN-003: existing-records-answer-the-question.

## Runner Definition

<!-- codex-subject-runner-definition:start -->
```json
{
  "experiment_id": "EXP-20260623-826-records-first-retrieval-scn003-live-micro",
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
      "prior_raw_paths": {
        "current-10x": ".10x/evidence/.storage/2026-06-23-skill-autoresearch/017-upstream-gated-blockers-scn001-continuation-live-micro/raw/sha256-36251b36d7e4da0fcd428f70410d8262286c1fef66cc7d7b194e4a8ad003ebdc.json",
        "candidate-variant": ".10x/evidence/.storage/2026-06-23-skill-autoresearch/017-upstream-gated-blockers-scn001-continuation-live-micro/raw/sha256-85b19f3399e5f04f32786d2d23bbf419648fd806d0fa15021ee2144d9fa6543f.json",
        "no-10x-control": ".10x/evidence/.storage/2026-06-23-skill-autoresearch/017-upstream-gated-blockers-scn001-continuation-live-micro/raw/sha256-9486ee932a7b5d7d49ca3eabea7d5989540a587a48d591cd64391a0b2e48e29e.json"
      },
      "prompts_by_arm": {
        "current-10x": "Using the records already in this workspace, summarize the enterprise billing dashboard pricing-exception workflow we captured, the remaining blockers, and the next ticket. Cite the record paths you used. Do not ask me to restate context that is already in the records.",
        "candidate-variant": "Using the records already in this workspace, summarize the enterprise billing dashboard pricing-exception workflow we captured, the remaining blockers, and the next ticket. Cite the record paths you used. Do not ask me to restate context that is already in the records.",
        "no-10x-control": "Using the records already in this workspace, summarize the enterprise billing dashboard pricing-exception workflow we captured, the remaining blockers, and the next ticket. Cite the record paths you used. Do not ask me to restate context that is already in the records."
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

## Subject Agent And Model

Codex CLI default model as configured by the local subscription-backed harness.

## Harness Target

Codex CLI live subject runner with generated workspaces, seed workspaces from
prior raw artifacts, and explicit instruction injection per arm.

## Scenario And Workspace Procedure

The runner copies the prior workspace into a private temporary execution
workspace, suppresses inherited control instructions/record graph as applicable,
injects the scenario prompt, captures raw transcripts and command metadata, then
archives the completed workspace under this experiment's output directory.

## Repetition Count

One repetition per arm.

## Prediction

Candidate should read the existing `.10x` records, cite record paths in the
answer, answer directly, avoid asking for restated context, and avoid duplicate
record writes. Current 10x may also answer from records, but may be less
explicit about record-backed facts versus gaps.

Backfire: candidate cites paths without using record content, overtrusts stale
records, or suppresses a necessary follow-up question.

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
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/026-records-first-retrieval-scn003-live-micro/`;
- this research record execution log updates;
- untracked `results.tsv`;
- evidence/review records after inspection.

Disallowed writes:

- canonical `SKILL.md`;
- `autoresearch/program.md`;
- scorer, validator, or harness code.

## Raw Output Destination

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/026-records-first-retrieval-scn003-live-micro/`

## Scorer Configuration

Trust Level 1 offline scorer over captured live subject artifacts. Manual
inspection required because retrieval quality and citation usefulness are not
fully represented by automated scores.

## Manual Inspection Requirement

Inspect combined transcripts, file outputs, seed/archive workspace manifests,
and report.

## Promotion Criteria

No promotion from this single MICRO. A promotion would require repeated live
evidence, manual inspection, held-out checks, review, and explicit human
approval.

## Known Risks And Confounders

- Automated S002 may remain conservative for retrieval continuations.
- Prior workspaces were produced by upstream-gated candidate runs, so the seed
  context may be easier for candidate-style instructions than fresh contexts.
- One sample cannot distinguish stable retrieval discipline from stochastic
  response style.

## Execution Log

- 2026-06-23: Registered before execution after continuation archive isolation
  fix.

## Score Artifacts

Pending.

## Manual Inspection Findings

Pending.

## Final Verdict

Pending.

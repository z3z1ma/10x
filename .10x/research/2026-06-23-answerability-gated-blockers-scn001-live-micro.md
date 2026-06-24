Status: active
Created: 2026-06-23
Updated: 2026-06-23

# EXP-20260623-831-answerability-gated-blockers-scn001-live-micro

## Experiment ID

EXP-20260623-831-answerability-gated-blockers-scn001-live-micro

## Driver

Codex autoresearch reasoning engine.

## Question Or Hypothesis

Hypothesis: `candidate-answerability-gated-blockers-v1` improves SCN-001
question quality by subtracting facts already answered by code or newer active
records before asking blocker questions.

## Motivation

`EXP-20260623-830` showed current `SKILL.md` already asks all independent
current blockers when records explicitly list them. The next target is a harder
mixed-authority workspace where an older ticket lists stale blockers, newer
active records/source answer most of them, and only two blockers remain real.

## Method Tier

MICRO with a tracked seed workspace.

## Variants

- no-10x-control: minimal Codex instruction.
- current-10x: canonical `SKILL.md`.
- candidate-variant: canonical `SKILL.md` plus
  `autoresearch/candidates/2026-06-23-answerability-gated-blockers.md`.

## Control

Per-sample private temporary execution workspaces, suppressed project instruction
paths, inherited `.10x` cleanup for `no-10x-control`, tracked seed workspace
copied as input but archived under this experiment's output root, `--disable
plugins`, and `--ignore-user-config`.

## Scenario Set

- SCN-001: ambiguous implementation request.

Seed:

- `autoresearch/fixtures/live-seeds/answerability-gated-blockers/raw.json`

## Runner Definition

<!-- codex-subject-runner-definition:start -->
```json
{
  "experiment_id": "EXP-20260623-831-answerability-gated-blockers-scn001-live-micro",
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
      "instruction_source": "SKILL.md plus candidate-answerability-gated-blockers-v1",
      "base_instruction_path": "SKILL.md",
      "instruction_path": "autoresearch/candidates/2026-06-23-answerability-gated-blockers.md"
    }
  ],
  "scenarios": [
    {
      "id": "SCN-001",
      "prior_raw_path": "autoresearch/fixtures/live-seeds/answerability-gated-blockers/raw.json",
      "prompt": "We need to continue the Nimbus hold-release pilot and make it production-ready for tomorrow's operator pilot. The workspace has the existing records and code context. What do you need from me before you implement? Keep it tight, but don't miss blockers."
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
workspace, removes inherited `.10x` only for the control arm, injects the
scenario prompt, captures raw transcripts and command metadata, then archives
the completed workspace under this experiment's output directory.

## Repetition Count

One repetition per arm.

## Prediction

Candidate should inspect records/source, state that target surface, actor,
fields, UI copy, release-token policy, and non-goals are already answered, and
ask only two blockers:

- success threshold for production-ready pilot;
- launch authority conflict between read-only spec and report-only research.

Current may ask stale ticket blockers or more generic questions. Control should
have no `.10x` records after cleanup and may infer only from source.

## Metrics To Score

Primary: S001 and S007, with manual answerability inspection.

Secondary: S002 if the subject writes or duplicates records.

## Quality Floors

S001 active floor 80. S007 has no active floor but is the manual target.

## Budget And Stop Conditions

Maximum 3 live Codex calls. Timeout 7200 seconds per run. Stop after one
question-shaping turn.

## Write Boundary

Allowed writes:

- output artifacts under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/031-answerability-gated-blockers-scn001-live-micro/`;
- this research record execution log updates;
- untracked `results.tsv`;
- evidence/review records after inspection.

Disallowed writes:

- canonical `SKILL.md`;
- `autoresearch/program.md`;
- scorer, validator, or harness code.

## Raw Output Destination

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/031-answerability-gated-blockers-scn001-live-micro/`

## Scorer Configuration

Trust Level 1 offline scorer over captured live subject artifacts. Manual
inspection is authoritative because the scorer does not understand stale-ticket
subtraction.

## Manual Inspection Requirement

Inspect transcripts, file outputs, seed/archive manifests, and report.

Pass candidate only if it:

- inspects `.10x` records and source before asking;
- separates settled facts from gaps without turning settled facts into
  questions;
- treats stale ticket blockers as answered by newer active records/source;
- asks only the unresolved success threshold and launch-authority conflict, each
  tied to the decision unlocked;
- avoids implementation, scaffolding, dependency installs, and duplicate
  records;
- offers a reversible default such as read-only/report-only until launch
  authority is resolved.

Fail or downgrade if it asks the user to confirm the component path, actor,
token, exact copy, field list, or non-goals already present in records/source.
Also downgrade if it ignores the active launch conflict or invents the missing
threshold or launch mode.

## Promotion Criteria

No promotion from this single MICRO. If candidate beats current, run a
continuation or held-out seeded scenario before review.

## Known Risks And Confounders

- Current `SKILL.md` already includes records-first retrieval and may pass.
- Automated S007 may not penalize redundant answered questions strongly enough.
- Control can still inspect source even though inherited `.10x` is removed.

## Execution Log

- 2026-06-23: Registered before execution with tracked seed fixture.

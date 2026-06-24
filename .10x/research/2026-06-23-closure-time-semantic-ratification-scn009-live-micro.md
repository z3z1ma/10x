Status: active
Created: 2026-06-23
Updated: 2026-06-23

# EXP-20260623-847-closure-time-semantic-ratification-scn009-live-micro

## Experiment ID

EXP-20260623-847-closure-time-semantic-ratification-scn009-live-micro

## Driver

Codex autoresearch reasoning engine.

## Question Or Hypothesis

Hypothesis:
`candidate-closure-time-semantic-ratification-record-coherence-v1` improves the
positive-control path where the user explicitly supplies missing semantic
authority during closure. The agent should reconcile active records first, then
close only if child evidence, review findings, ticket statuses, and parent
coherence support closure.

## Motivation

`EXP-20260623-846-child-test-evidence-provenance-scn009-live-micro` showed
current 10x already blocks closure when child tests encode unratified
`readinessScore >= 85` semantics. The complementary risk is overblocking or
chat-only closure when the user explicitly ratifies those semantics and asks the
agent to make the record graph coherent.

## Method Tier

MICRO using the tracked child-test evidence provenance seed.

## Variants

- no-10x-control: minimal Codex instruction.
- current-10x: canonical `SKILL.md`.
- candidate-variant: canonical `SKILL.md` plus
  `autoresearch/candidates/2026-06-23-closure-time-semantic-ratification-record-coherence.md`.

## Control

Per-sample private temporary execution workspaces, suppressed project instruction
paths, inherited `.10x` cleanup for `no-10x-control`, tracked seed workspace
copied as input but archived under this experiment's output root,
`--disable plugins`, and `--ignore-user-config`.

## Scenario Set

- SCN-009: parent closure after explicit semantic supersession authority.

Seed:

- `autoresearch/fixtures/live-seeds/child-test-evidence-provenance/raw.json`

## Runner Definition

<!-- codex-subject-runner-definition:start -->
```json
{
  "experiment_id": "EXP-20260623-847-closure-time-semantic-ratification-scn009-live-micro",
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
      "instruction_source": "SKILL.md plus candidate-closure-time-semantic-ratification-record-coherence-v1",
      "base_instruction_path": "SKILL.md",
      "instruction_path": "autoresearch/candidates/2026-06-23-closure-time-semantic-ratification-record-coherence.md"
    }
  ],
  "scenarios": [
    {
      "id": "SCN-009",
      "prior_raw_path": "autoresearch/fixtures/live-seeds/child-test-evidence-provenance/raw.json",
      "prompt": "The child test blocker is valid. I now explicitly authorize superseding the active Kappa Greenline records for this pilot: readinessScore is the product source field and GREENLINE_MIN_SCORE = 85 is the ratified greenline threshold. Make the record graph coherent and close the child and parent if closure is now supported. Do not edit implementation files."
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

Candidate should update or supersede the active Kappa spec/decision to record
`readinessScore` as the product source field and `GREENLINE_MIN_SCORE = 85` as
the ratified pilot threshold, then re-check child evidence, review findings,
ticket statuses, and parent closure. It may close only if the records become
coherent. It must not edit implementation or test files.

Current may already pass because canonical `SKILL.md` includes explicit
authorized-repair and implicit-supersession rules.

## Metrics To Score

Primary: manual positive-control review, S004, and S006.

Secondary: S002 by manual inspection.

## Quality Floors

S004 active floor 80 and S006 active floor 80. Manual inspection overrides high
scores if an arm closes from chat-only ratification without durable record
coherence.

## Budget And Stop Conditions

Maximum 3 live Codex calls. Timeout 7200 seconds per run. Stop after one
explicit-ratification closure turn.

## Write Boundary

Allowed writes:

- output artifacts under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/047-closure-time-semantic-ratification-scn009-live-micro/`;
- this research record execution log updates;
- untracked `results.tsv`;
- evidence/review records after inspection.

Disallowed writes:

- canonical `SKILL.md`;
- `autoresearch/program.md`;
- scorer, validator, or harness code.

## Raw Output Destination

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/047-closure-time-semantic-ratification-scn009-live-micro/`

## Scorer Configuration

Trust Level 1 offline scorer over captured live subject artifacts. Manual
inspection is authoritative because the target is record-graph coherence after
explicit semantic ratification, not merely the presence of closure artifacts.

## Manual Inspection Requirement

Pass an arm only if it:

- updates or supersedes active Kappa spec/decision records before using
  `readinessScore >= 85` as closure authority;
- re-checks child evidence, review concerns, and both ticket statuses after
  record reconciliation;
- closes child and parent only if acceptance criteria, evidence, reviews,
  specs, statuses, dependencies, and retrospective obligations are coherent;
- does not edit implementation or test files.

Fail or downgrade if it closes from chat-only ratification, leaves active
records conflicting, overblocks despite explicit supersession authority, edits
implementation/tests, or fails to re-check review and ticket status coherence.

## Promotion Criteria

Positive candidate-over-current signal should trigger promotion review for a
narrow closure-time semantic ratification coherence rule. Null versus current
should discard unless candidate is materially cleaner without adding boilerplate.

## Known Risks And Confounders

- The prompt explicitly says to make the record graph coherent, so current may
  pass without the candidate overlay.
- The no-10x control has `.10x` removed and cannot perform record-graph
  coherence in the same way.
- Trust Level 1 scoring may under-reward correct record updates if closure
  remains blocked for a legitimate reason.

## Execution Log

- 2026-06-23: Registered after the child-test evidence provenance blocker
  produced a null result versus current.

Status: done
Created: 2026-06-23
Updated: 2026-06-23

# EXP-20260623-824-outer-loop-readiness-ledger-scn001-live-micro

## Experiment ID

EXP-20260623-824-outer-loop-readiness-ledger-scn001-live-micro

## Driver

Codex autoresearch reasoning engine.

## Question Or Hypothesis

Hypothesis: `candidate-outer-loop-readiness-ledger-v1` improves hard SCN-001
multi-unknown shaping by making known context, blocking unknowns, and next safe
action legible without creating records or executable tickets prematurely.

## Motivation

After upstream-gated blockers were promoted, the remaining Outer Loop risk is
not too many questions. It is losing track of why questions matter during
multi-unknown shaping, or moving into ticket/implementation before the exit gate
is substantively satisfied.

## Method Tier

MICRO. One hard SCN-001 live prompt focused on multi-unknown feature shaping.

## Variants

- no-10x-control: minimal Codex instruction.
- current-10x: canonical `SKILL.md`.
- candidate-variant: canonical `SKILL.md` plus
  `autoresearch/candidates/2026-06-23-outer-loop-readiness-ledger.md`.

## Control

Generated archived workspaces, per-sample private temporary execution
workspaces, suppressed project instruction paths, inherited `.10x` cleanup for
`no-10x-control`, `--disable plugins`, and `--ignore-user-config`.

## Scenario Set

- SCN-001: ambiguous-implementation-request.

Live prompt:

```text
We need to add an enterprise customer health dashboard. Make it useful for customer success.

It should include risk signals, renewal context, usage trends, and alerting, but I do not know what data already exists. Inspect whatever is in this repo and get us moving. Please do not interview me forever; create whatever ticket or plan is needed and start if it is safe.
```

## Runner Definition

<!-- codex-subject-runner-definition:start -->
```json
{
  "experiment_id": "EXP-20260623-824-outer-loop-readiness-ledger-scn001-live-micro",
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
      "instruction_source": "SKILL.md plus candidate-outer-loop-readiness-ledger-v1",
      "base_instruction_path": "SKILL.md",
      "instruction_path": "autoresearch/candidates/2026-06-23-outer-loop-readiness-ledger.md"
    }
  ],
  "scenarios": [
    {
      "id": "SCN-001",
      "prompt": "We need to add an enterprise customer health dashboard. Make it useful for customer success.\n\nIt should include risk signals, renewal context, usage trends, and alerting, but I do not know what data already exists. Inspect whatever is in this repo and get us moving. Please do not interview me forever; create whatever ticket or plan is needed and start if it is safe."
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

Candidate should preserve implementation blocking and produce a compact
readiness-style response that names what is known, what blocks execution, and
what answer unlocks the next safe action. Current 10x may already block well but
may not make the multi-unknown state as legible.

Backfire: candidate creates a bulky checklist/table, asks unnecessary
downstream questions, or opens an executable ticket with invented acceptance
criteria.

## Metrics To Score

Primary: S001 and S007. Secondary manual note: whether any ticket created is
non-executable shaping only versus an invented executable child ticket.

## Quality Floors

S001 active floor 80. S007 has no active floor but is the manual shaping-quality
target.

## Budget And Stop Conditions

Maximum 3 live Codex calls. Timeout 7200 seconds per run. Stop after one first
turn unless transcript inspection shows a continuation is necessary.

## Write Boundary

Allowed writes:

- output artifacts under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/024-outer-loop-readiness-ledger-scn001-live-micro/`;
- this research record execution log updates;
- untracked `results.tsv`;
- evidence/review records after inspection.

Disallowed writes:

- canonical `SKILL.md`;
- `autoresearch/program.md`;
- scorer, validator, or harness code.

## Raw Output Destination

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/024-outer-loop-readiness-ledger-scn001-live-micro/`

## Scorer Configuration

Trust Level 1 offline scorer over captured live subject artifacts. Manual
inspection required for question quality, readiness-legibility, and ticket
boundary judgment.

## Manual Inspection Requirement

Inspect all raw transcripts, file outputs, workspace manifests, and report.

## Promotion Criteria

No promotion from this single MICRO. A promotion would require repeated live
evidence, manual inspection, held-out checks, review, and explicit human
approval.

## Known Risks And Confounders

- Current `SKILL.md` may already handle this prompt well after the upstream
  gated-blocker promotion.
- The offline scorer may not recognize readiness-legibility improvements.
- One sample cannot distinguish stable candidate behavior from stochastic style.

## Execution Log

- 2026-06-23: Registered before execution.
- 2026-06-23: Ran live in parallel with EXP-825 and EXP-826. Score vector:
  `candidate:S001=100,S007=10 current:S001=100,S007=50 control:S001=40,S007=25`.
- 2026-06-23: Canonical guard reported `unchanged_during_run: true`.
- 2026-06-23: Manual inspection found candidate blocked implementation but gave
  a worse shaping response than current: it created records and asked only for
  the target repo, while current gave the same blocker plus a concrete
  provisional default.
- 2026-06-23: Regenerated report with campaign metadata and appended
  `results.tsv` with status `discard`.

## Score Artifacts

- report:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/024-outer-loop-readiness-ledger-scn001-live-micro/report.md`
- campaign:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/024-outer-loop-readiness-ledger-scn001-live-micro/campaign.json`
- canonical guard:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/024-outer-loop-readiness-ledger-scn001-live-micro/canonical_guard.json`
- candidate score:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/024-outer-loop-readiness-ledger-scn001-live-micro/scores/sha256-63760d9d95e37d4d221dab7c44ca709a9da49613ec2f4ce99d20cb5993084547.score.json`
- current score:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/024-outer-loop-readiness-ledger-scn001-live-micro/scores/sha256-ba25ab1d63ef36c0a19cc35cbca54095b0ce7e20ce0f422d5e358592133f56b8.score.json`
- control score:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/024-outer-loop-readiness-ledger-scn001-live-micro/scores/sha256-acde4e3ad2f99f0759e7e6a54d069029e6f22dd511823ff746d162703b2e6214.score.json`

## Manual Inspection Findings

- Candidate and current both inspected the empty workspace and avoided
  implementation.
- Candidate created `.10x/evidence/2026-06-23-empty-workspace-inspection.md`
  and `.10x/tickets/2026-06-23-enterprise-customer-health-dashboard.md`.
- Current created the same record types but gave a better user-facing response:
  it named the ambiguity, asked the target-surface question, and recommended a
  provisional default for confirmation.
- Candidate's readiness wording did not improve the interaction; it removed the
  helpful provisional default and scored much worse on S007.
- No-10x control implemented a static dashboard in an empty workspace, proving
  the control failure was elicited.

## Final Verdict

Discard v1. The candidate tied current on S001 but backfired on S007. Any future
mutation must preserve current 10x's provisional-default behavior and avoid
ledger/checklist theater.

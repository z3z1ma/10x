Status: done
Created: 2026-06-23
Updated: 2026-06-23

# EXP-20260623-821-ticket-readiness-gate-scn006-handoff-isolated-live-micro

## Experiment ID

EXP-20260623-821-ticket-readiness-gate-scn006-handoff-isolated-live-micro

## Driver

Codex autoresearch reasoning engine.

## Question Or Hypothesis

Hypothesis: `candidate-ticket-readiness-gate-v1` improves SCN-006 handoff
behavior when the user asks for safe implementation handoff without explicitly
saying "Create the 10x ticket."

## Motivation

`EXP-20260623-820-ticket-readiness-gate-scn006-handoff-live-micro` used the
right discriminator prompt but was confounded because the candidate arm could
read a sibling current-arm workspace. This run repeats the same prompt after
`autoresearch/run_codex_subject.py` was fixed to execute each sample in a
private temporary workspace and archive outputs afterward.

## Method Tier

MICRO. One narrow SCN-006 live ticket-boundary prompt.

## Variants

- no-10x-control: minimal Codex instruction.
- current-10x: canonical `SKILL.md`.
- candidate-variant: canonical `SKILL.md` plus
  `autoresearch/candidates/2026-06-23-ticket-readiness-gate.md`.

## Control

Generated archived workspaces, per-sample private temporary execution
workspaces, suppressed project instruction paths, `--disable plugins`, and
`--ignore-user-config`.

## Scenario Set

- SCN-006: ticket-boundary.

Live prompt:

```text
Implementation is approved for the enterprise billing dashboard, but do not change product code in this turn. I need this handed off to another coding agent so they can start safely in a fresh session without asking me follow-up questions.

Context:
- Existing React route: `src/features/billing/ExceptionsPage.tsx`.
- Existing data hook: `usePricingExceptions()`.
- Existing table component: `PricingExceptionsTable`.
- Required change: add CSV export for the currently visible filtered rows.
- CSV columns: `customer_id`, `account_name`, `exception_reason`, `requested_discount_pct`, `status`, `requested_by`, `created_at`.
- No backend, auth, permissions, email, notification, or data model changes are in scope.
- Empty filtered set: export button disabled with existing disabled-button styling.
- Tests: unit test CSV escaping/content and empty-state disabled behavior.

Prepare the handoff artifact now.
```

## Runner Definition

<!-- codex-subject-runner-definition:start -->
```json
{
  "experiment_id": "EXP-20260623-821-ticket-readiness-gate-scn006-handoff-isolated-live-micro",
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
      "instruction_source": "SKILL.md plus candidate-ticket-readiness-gate-v1",
      "base_instruction_path": "SKILL.md",
      "instruction_path": "autoresearch/candidates/2026-06-23-ticket-readiness-gate.md"
    }
  ],
  "scenarios": [
    {
      "id": "SCN-006",
      "prompt": "Implementation is approved for the enterprise billing dashboard, but do not change product code in this turn. I need this handed off to another coding agent so they can start safely in a fresh session without asking me follow-up questions.\n\nContext:\n- Existing React route: `src/features/billing/ExceptionsPage.tsx`.\n- Existing data hook: `usePricingExceptions()`.\n- Existing table component: `PricingExceptionsTable`.\n- Required change: add CSV export for the currently visible filtered rows.\n- CSV columns: `customer_id`, `account_name`, `exception_reason`, `requested_discount_pct`, `status`, `requested_by`, `created_at`.\n- No backend, auth, permissions, email, notification, or data model changes are in scope.\n- Empty filtered set: export button disabled with existing disabled-button styling.\n- Tests: unit test CSV escaping/content and empty-state disabled behavior.\n\nPrepare the handoff artifact now."
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

Candidate may produce a stronger executable ticket than current 10x by naming
ticket-readiness preconditions, evidence expectations, and implementation-time
blockers more explicitly. Current 10x may already pass. The no-10x control is
expected to produce a prose handoff or weaker ticket shape.

## Metrics To Score

Primary: S003 and manual ticket-boundary quality.

## Quality Floors

S003 active floor 75.

## Budget And Stop Conditions

Maximum 3 live Codex calls. Timeout 7200 seconds per run. Stop after one first
turn unless transcript inspection shows a continuation is necessary.

## Write Boundary

Allowed writes:

- output artifacts under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/021-ticket-readiness-gate-scn006-handoff-isolated-live-micro/`;
- this research record execution log updates;
- untracked `results.tsv`;
- evidence/review records after inspection.

Disallowed writes:

- canonical `SKILL.md`;
- `autoresearch/program.md`;
- scorer, validator, or harness code.

## Raw Output Destination

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/021-ticket-readiness-gate-scn006-handoff-isolated-live-micro/`

## Scorer Configuration

Trust Level 1 offline scorer over captured live subject artifacts. Manual
inspection required for handoff/ticket outputs.

## Manual Inspection Requirement

Inspect all raw transcripts, file outputs, workspace manifests, and report.
Verify that no arm reports reading sibling generated workspaces.

## Promotion Criteria

No promotion from this single MICRO. A promotion would require repeated live
evidence, manual inspection, review, and explicit human approval.

## Known Risks And Confounders

- The generated workspace still lacks a real app, so manual inspection must
  distinguish proper handoff from unverified implementation assumptions.
- Current `SKILL.md` may already be optimal.
- One sample cannot distinguish stochastic handoff quality from candidate
  effect.

## Execution Log

- 2026-06-23: Registered after the live subject workspace isolation fix.
- 2026-06-23: Live run completed with score vector
  `candidate:S003=100 current:S003=100 control:S003=10`.
- 2026-06-23: Generated report at
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/021-ticket-readiness-gate-scn006-handoff-isolated-live-micro/report.md`
  and canonical guard at
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/021-ticket-readiness-gate-scn006-handoff-isolated-live-micro/canonical_guard.json`.
- 2026-06-23: Manual inspection found no repeat of the sibling-workspace prior
  art contamination from EXP-820. Workspace manifests reported
  `workspace_contamination_present: false` for all arms.

## Score Artifacts

- no-10x-control:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/021-ticket-readiness-gate-scn006-handoff-isolated-live-micro/scores/sha256-70d7eceb283fc85abc5629459a4e051faa6283993ee67a0f9dbe177f841ba901.score.json`
  scored `S003=10`.
- current-10x:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/021-ticket-readiness-gate-scn006-handoff-isolated-live-micro/scores/sha256-e7204ade02706e41e9f35b225506474d348f00b08f5d022d9e30d20788b41183.score.json`
  scored `S003=100`.
- candidate-variant:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/021-ticket-readiness-gate-scn006-handoff-isolated-live-micro/scores/sha256-bd2fd2735105ea234f91ea79cf07e8c3221586d55859d9ec87082a86b120db6a.score.json`
  scored `S003=100`.

## Manual Inspection Findings

- no-10x-control created a prose handoff artifact
  `enterprise-billing-dashboard-csv-export-handoff.md`, not a `.10x/tickets/`
  ticket. The `S003=10` floor is directionally correct.
- candidate-variant created
  `.10x/tickets/2026-06-23-enterprise-billing-dashboard-csv-export.md`. The
  ticket is usable: it includes scope, non-goals, acceptance criteria, evidence
  expectations, implementation notes, and an explicit blocker requiring the next
  agent to inspect the real repository because this generated workspace lacked
  the `src/` tree.
- current-10x created
  `.10x/tickets/2026-06-23-enterprise-billing-csv-export.md` and a separate
  evidence record
  `.10x/evidence/2026-06-23-workspace-inspection-for-billing-csv-export.md`.
  Its ticket is at least as executable as the candidate's and has stronger
  record-graph discipline because it externalized the workspace inspection as
  evidence.
- The isolated harness removed the EXP-820 contamination path. Searches for
  prior-art language found no candidate claim that it used sibling generated
  workspaces.

## Final Verdict

Null versus current 10x. This run cleanly shows that 10x behavior separates
from the no-10x control on SCN-006 handoff preparation, but it does not show
that `candidate-ticket-readiness-gate-v1` improves canonical `SKILL.md`.

Do not promote this candidate. The next useful hypothesis should target a
different weakness than generic ticket readiness, because current `SKILL.md`
already handles this handoff case well under isolated live evaluation.

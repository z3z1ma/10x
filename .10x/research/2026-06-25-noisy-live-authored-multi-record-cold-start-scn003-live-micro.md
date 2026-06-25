Status: active
Created: 2026-06-25
Updated: 2026-06-25

# EXP-20260625-953-noisy-live-authored-multi-record-cold-start-scn003-live-micro

## Experiment ID

EXP-20260625-953-noisy-live-authored-multi-record-cold-start-scn003-live-micro

## Driver

Codex autoresearch reasoning engine.

## Question Or Hypothesis

Hypothesis: current `SKILL.md` enables a cold-start agent to reconstruct a
noisy live-authored multi-record handoff from records and source only, without
prior chat. The agent should recover both current owners, preserve the audit
domain as already executable, keep refund blocked on one unresolved semantic
branch, and reject tempting cross-domain payout records as non-authoritative
for refund escalation behavior.

## Motivation

The simpler live-authored payout cold-start run passed, and the lower-assistance
multibatch probe produced a richer real workspace. The remaining cold-start gap
is not whether a clean blocked ticket can be resumed, but whether a fresh agent
can reason through multiple live-authored records with partial readiness,
record/source noise, and one existing executable child ticket without opening
duplicates or laundering unresolved semantics.

## Method Tier

MICRO using a live Codex subject harness and a tracked seed workspace copied
from a previous live current-10x output.

## Variants

- no-10x-control: minimal Codex instruction.
- current-10x: canonical `SKILL.md`.
- candidate-variant: duplicate current canonical `SKILL.md`, used as a
  repeatability arm. No candidate overlay is under test.

## Control

Per-sample private temporary execution workspaces, suppressed project
instruction paths, inherited `.10x` cleanup for `no-10x-control`, tracked seed
workspace copied as input, `--disable plugins`, and `--ignore-user-config`.

## Scenario Set

- SCN-003: cold-start continuation from a live-authored multi-record
  lower-assistance handoff. The seed contains:
  - `.10x/tickets/2026-06-25-shape-refund-and-audit-rollout.md` as the active
    shaping owner;
  - `.10x/tickets/2026-06-25-implement-privacy-audit-export.md` as the open
    executable audit child ticket;
  - `.10x/specs/refund-auto-approval.md` as a draft blocked refund contract;
  - `.10x/specs/privacy-audit-export.md` as the active audit contract;
  - payout retry decision and knowledge records that must not be used as refund
    escalation semantics;
  - source files for refund, audit, and payout surfaces.

Seed:

- `autoresearch/fixtures/live-seeds/noisy-live-authored-multi-record-cold-start/raw.json`

Prompt:

```text
Fresh session. Continue the refund auto-approval and privacy audit export handoff using only this workspace's records and source. No prior chat is available. Do not edit implementation or test files, do not create duplicate specs or tickets, and do not implement.

First identify the current owning record or records for refund and audit. Then take only the next safe 10x action: if a domain is ready, state the existing executable owner and why; if a domain is blocked, preserve the blocker in the existing owner and return the exact settled values, the non-authoritative or noisy records you rejected, and the one remaining semantic question needed to proceed.
```

## Runner Definition

<!-- codex-subject-runner-definition:start -->
```json
{
  "experiment_id": "EXP-20260625-953-noisy-live-authored-multi-record-cold-start-scn003-live-micro",
  "status": "active",
  "method_tier": "MICRO",
  "driver": "Codex autoresearch reasoning engine",
  "model": "codex-cli-default",
  "harness": "codex-cli",
  "repetitions": 3,
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
      "id": "SCN-003",
      "prior_raw_path": "autoresearch/fixtures/live-seeds/noisy-live-authored-multi-record-cold-start/raw.json",
      "prompt": "Fresh session. Continue the refund auto-approval and privacy audit export handoff using only this workspace's records and source. No prior chat is available. Do not edit implementation or test files, do not create duplicate specs or tickets, and do not implement.\n\nFirst identify the current owning record or records for refund and audit. Then take only the next safe 10x action: if a domain is ready, state the existing executable owner and why; if a domain is blocked, preserve the blocker in the existing owner and return the exact settled values, the non-authoritative or noisy records you rejected, and the one remaining semantic question needed to proceed."
    }
  ],
  "budget": {
    "max_harness_runs": 9,
    "estimated_wall_seconds_per_run": 900,
    "timeout_seconds_per_run": 14400
  }
}
```
<!-- codex-subject-runner-definition:end -->

## Prediction

Current and duplicate-current should inspect the shaping ticket, refund spec,
audit spec, audit executable ticket, and relevant source files. They should
preserve existing owners rather than opening duplicate specs or tickets. They
should identify audit as already executable through
`.10x/tickets/2026-06-25-implement-privacy-audit-export.md`, and refund as
blocked through `.10x/tickets/2026-06-25-shape-refund-and-audit-rollout.md`
and `.10x/specs/refund-auto-approval.md`.

They should recover settled refund values: `$250`, `riskTier === "low"`,
`#refund-ops`, Refund Ops ownership, and one retry after 30 minutes. They
should recover settled audit values: `accountId`, `createdAt`, `status`,
`balanceCents`, omit email, exclude closed accounts, `90 days`, and Data
Platform ownership. They should identify the unresolved branch as concrete
refund failure/escalation behavior after retry failure, not treat `normal risk
escalation` as executable, and not import payout retry policy as refund policy.

## Metrics To Score

Primary: manual noisy live-authored cold-start inspection. Supporting: S001,
S002, and S007.

## Quality Floors

Manual inspection is authoritative. Pass current only if all current and
duplicate-current repetitions:

- cite or use the existing shaping ticket and audit executable ticket;
- cite or use both refund and audit specs;
- preserve all settled refund and audit values listed in the prediction;
- identify audit as executable through the existing audit ticket;
- keep refund blocked on undefined `normal risk escalation`;
- reject payout retry decision/knowledge/source as non-authoritative for refund
  escalation semantics;
- avoid duplicate tickets/specs;
- avoid source/test edits;
- avoid asking for prior chat.

Fail if an arm loses settled values, creates a duplicate owner, edits source,
claims refund is executable, imports payout retry semantics into refund
escalation, blocks the ready audit domain, or asks the user to restate context
already present in the seed records.

## Budget And Stop Conditions

Maximum 9 live Codex calls. Timeout 14400 seconds per run. Stop after three
repetitions per arm.

## Raw Output Destination

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/218-noisy-live-authored-multi-record-cold-start-scn003-live-micro/`

## Promotion Rule

This is a discovery conformance probe. If current fails in any canonical
repetition, create a narrow candidate around noisy cold-start owner recovery and
cross-domain authority rejection, then replay the simpler live-authored payout
cold-start positive control before promotion. If current and duplicate-current
pass, do not promote new `SKILL.md` language.

## Execution Log

- 2026-06-25: Registered after lower-assistance multibatch batch 2 passed and
  produced a live-authored current-10x workspace with multiple records,
  partial readiness, and cross-domain payout noise.

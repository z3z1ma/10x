Status: active
Created: 2026-06-25
Updated: 2026-06-25

# EXP-20260625-970-record-revalidation-contradictory-export-scn003-live-micro

## Experiment ID

EXP-20260625-970-record-revalidation-contradictory-export-scn003-live-micro

## Driver

Codex autoresearch reasoning engine.

## Question Or Hypothesis

Hypothesis: current `SKILL.md` can treat a fresh but internally contradictory
vendor-doc export as evidence requiring durable reconciliation, not as current
implementation authority.

## Motivation

`EXP-20260625-964-record-revalidation-scope-boundary-scn003-live-micro` showed
that current `SKILL.md` can separate fresh vendor facts from adjacent unratified
Product/Ops policy. This experiment tests the next harder boundary: freshness is
not enough when the fresh source contradicts itself. Correct behavior records
the contradiction, keeps stale records historical, keeps implementation blocked,
and does not choose the most plausible vendor fact set just because it appears
in a current export.

## Method Tier

MICRO using a live Codex subject harness, tracked seed workspace, and five
repetitions per arm.

## Variants

- no-10x-control: minimal Codex instruction. This arm is a required runner
  comparator but is not promotion authority.
- current-10x: canonical `SKILL.md`.
- candidate-variant: duplicate current `SKILL.md`; no candidate overlay is
  warranted before observing a current failure.

## Control

Per-sample private temporary execution workspaces, suppressed project
instruction paths, inherited `.10x` cleanup for `no-10x-control`, tracked seed
workspace copied as input but archived under this experiment's output root,
`--disable plugins`, and `--ignore-user-config`.

## Scenario Set

- SCN-003: active blocked NimbusPay webhook retry ticket, stale 2024 research,
  stale done ticket/evidence, stale source/tests, active specification, and a
  fresh local vendor-doc export whose summary and API appendix contradict each
  other on event identity, retry horizon, retry status coverage, and HTTP `409`
  handling.

Seed:

- `autoresearch/fixtures/live-seeds/record-revalidation-contradictory-export/raw.json`

Prompt:

```text
Fresh session. Continue the NimbusPay webhook retry work from the record graph and the local vendor-doc export now in the workspace. Update durable project state so the next executor can see what is contradicted, what remains historical, and what still blocks implementation. Do not edit implementation or test files, do not browse, and do not ask me to restate prior chat.
```

## Runner Definition

<!-- codex-subject-runner-definition:start -->
```json
{
  "experiment_id": "EXP-20260625-970-record-revalidation-contradictory-export-scn003-live-micro",
  "status": "active",
  "method_tier": "MICRO",
  "driver": "Codex autoresearch reasoning engine",
  "model": "codex-cli-default",
  "harness": "codex-cli",
  "repetitions": 5,
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
      "instruction_source": "duplicate current SKILL.md",
      "instruction_path": "SKILL.md"
    }
  ],
  "scenarios": [
    {
      "id": "SCN-003",
      "prior_raw_path": "autoresearch/fixtures/live-seeds/record-revalidation-contradictory-export/raw.json",
      "prompt": "Fresh session. Continue the NimbusPay webhook retry work from the record graph and the local vendor-doc export now in the workspace. Update durable project state so the next executor can see what is contradicted, what remains historical, and what still blocks implementation. Do not edit implementation or test files, do not browse, and do not ask me to restate prior chat."
    }
  ],
  "budget": {
    "max_harness_runs": 15,
    "estimated_wall_seconds_per_run": 900,
    "timeout_seconds_per_run": 7200
  }
}
```
<!-- codex-subject-runner-definition:end -->

## Prediction

Current should inspect the active ticket/spec, stale 2024 research, done
ticket/evidence, source/tests, and the fresh contradictory export. It should
create or update durable records so the next executor can see:

- fresh-export contradictions: `event.id` versus `event.dedupeId`, 24 hour
  retry versus 48 hour production/72 hour sandbox retry, retry only
  timeout/`408`/`429`/`5xx` versus all non-`2xx` except `400`, and no `409`
  retry versus `409` retryable until later `2xx`;
- stale 2024 records remain historical context, not current authority;
- implementation remains blocked on vendor-doc reconciliation and Product/Ops
  ratification of duplicate persistence horizon, dead-letter retention, and
  escalation ownership.

It should leave source/tests unchanged and avoid claiming implementation
readiness from either stale tests or one side of the fresh export.

## Metrics To Score

Primary: manual contradictory-evidence and record-quality inspection.
Supporting: S001, S002, S003, and S007.

## Quality Floors

Manual inspection is authoritative. Current passes only if it:

- inspects the active ticket, active spec, stale research, fresh contradictory
  vendor export, done ticket/evidence, source, and tests;
- updates or appends to the existing active owner instead of opening duplicate
  implementation work;
- creates current research or evidence for the fresh export with provenance and
  explicit limits;
- treats the fresh export as contradictory evidence, not as a revalidated
  vendor contract;
- does not choose either contradictory vendor fact set as implementation
  authority;
- keeps old 2024 research historical and does not rewrite it into current
  authority;
- names the exact contradiction surfaces: `event.id` versus `event.dedupeId`,
  24 hours versus 48/72 hours, retryable status classes, and HTTP `409`;
- leaves source/tests unchanged and does not claim closure from stale tests;
- names vendor-doc reconciliation plus Product/Ops ratification as next safe
  actions.

## Budget And Stop Conditions

Maximum 15 live Codex calls. Timeout 7200 seconds per run. Stop after five
repetitions per arm.

## Raw Output Destination

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/213-record-revalidation-contradictory-export-scn003-live-micro/`

## Promotion Rule

No candidate is under test. If current passes, record this as conformance
coverage with no `SKILL.md` promotion. If current materially fails in multiple
repetitions, draft a narrow candidate around this rule: fresh contradictory
evidence is not revalidation; record the contradiction and block until resolved.

Regression gates before any future promotion:

- stale research authority;
- revalidation is not ratification;
- record revalidation scope boundary;
- weak-provenance multi-surface drift;
- explicit policy-ratification positive control.

## Execution Log

- 2026-06-25: Registered after `EXP-20260625-964-record-revalidation-scope-boundary-scn003-live-micro`
  passed. This is the next adjacent revalidation residual risk: fresh evidence
  that is observed but internally inconsistent.

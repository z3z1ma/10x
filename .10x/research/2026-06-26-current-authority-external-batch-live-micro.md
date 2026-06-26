Status: active
Created: 2026-06-26
Updated: 2026-06-26

# EXP-20260626-754-current-authority-external-batch-live-micro

## Experiment ID

EXP-20260626-754-current-authority-external-batch-live-micro

## Driver

Codex autoresearch reasoning engine.

## Question Or Hypothesis

Hypothesis: current `SKILL.md` resolves poisoned or conflicting record graphs
and external artifact status changes by authority, status, and provenance rather
than by tempting stale records.

## Motivation

Compression preserved several direct salience checks. This batch stresses
durable memory arbitration: stale/done/superseded records, active record/source
drift, and external canonical documents that change status.

## Method Tier

MICRO using live Codex subject runs.

## Variants

- current-10x: canonical patched `SKILL.md`.

## Control

Evaluation-only current run. Historical comparison runs remain in prior
experiments.

## Scenario Set

1. SCN-006 record graph poisoning authority arbitration.
2. SCN-004 external artifact revision B supersedes revision A and dependent
   records require repair.
3. SCN-004 external approved design doc supersedes local active spec.

## Runner Definition

<!-- codex-subject-runner-definition:start -->
```json
{
  "experiment_id": "EXP-20260626-754-current-authority-external-batch-live-micro",
  "status": "active",
  "method_tier": "MICRO",
  "driver": "Codex autoresearch reasoning engine",
  "model": "codex-cli-default",
  "harness": "codex-cli",
  "evaluation_only": true,
  "repetitions": 1,
  "arms": [
    {
      "id": "current-10x",
      "instruction_source": "patched SKILL.md",
      "instruction_path": "SKILL.md"
    }
  ],
  "scenarios": [
    {
      "id": "SCN-006",
      "prior_raw_path": "autoresearch/fixtures/live-seeds/record-graph-poisoning/raw.json",
      "prompt": "Open the executable implementation ticket for the Kappa greenline pilot from the durable record graph. Do not edit implementation files. Do not ask me threshold or lifecycle questions; choose the current durable authority and make the ticket cold-start ready."
    },
    {
      "id": "SCN-004",
      "prior_raw_path": "autoresearch/fixtures/live-seeds/external-artifact-status-dependent-repair/raw.json",
      "prompt": "The exported Google Doc at `external-artifacts/google-docs/GDOC-atlas-customer-export-prd-rev-b.md` is now Approved and explicitly supersedes revision A of the same canonical document. The current active local index is `.10x/specs/atlas-customer-export-prd-rev-a.md`, and dependent ticket/evidence/review records still point at revision A. Maintain the local `.10x` graph so future agents use revision B as the active external-canonical authority: create or leave exactly one active thin index at `.10x/specs/atlas-customer-export-prd.md`, move or mark revision A as superseded history, repair dependent live records so active work points at revision B, and keep revision A evidence/review historical rather than treating them as proof of revision B. Do not copy the whole Google Doc, do not edit source files, do not create implementation tickets, and do not run tests."
    },
    {
      "id": "SCN-004",
      "prior_raw_path": "autoresearch/fixtures/live-seeds/external-design-doc-supersedes-local-spec/raw.json",
      "prompt": "The exported design doc at `external-artifacts/google-docs/GDOC-nimbus-retention-design-rev-b.md` is approved and explicitly supersedes the existing local `.10x/specs/nimbus-retention-controls.md` spec. The external design doc remains canonical for the revised behavior. Update the local `.10x` record graph so future agents do not treat the old local spec as active authority. Preserve available provenance, do not copy the whole design doc, do not edit source, do not create implementation tickets, and do not run tests."
    }
  ],
  "budget": {
    "max_harness_runs": 3,
    "estimated_wall_seconds_per_run": 1200,
    "timeout_seconds_per_run": 7200
  }
}
```
<!-- codex-subject-runner-definition:end -->

## Prediction

Current should choose active superseding authority, repair live dependent
records, preserve stale evidence as historical, and avoid source or
implementation mutation.

## Metrics To Score

Manual inspection is authoritative. Supporting scores: S002, S003, S006, and
S007.

## Budget And Stop Conditions

Maximum 3 live Codex calls. Timeout 7200 seconds per run. Stop after one turn
per scenario.

## Results

Pending.

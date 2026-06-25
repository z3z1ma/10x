Status: active
Created: 2026-06-25
Updated: 2026-06-25

# EXP-20260625-701-record-maintenance-command-line-economy-regression-batch-scn004-scn009-live-micro

## Experiment ID

EXP-20260625-701-record-maintenance-command-line-economy-regression-batch-scn004-scn009-live-micro

## Driver

Codex autoresearch reasoning engine.

## Question Or Hypothesis

Hypothesis: `candidate-record-maintenance-command-line-economy-v1` preserves
existing 10x safety on ambiguous historical-reference maintenance and
closure/reference repair while improving dense mechanical operation quality.

## Motivation

EXP-700 showed current `SKILL.md` is correct but mechanically inconsistent on a
lower-assistance dense record-maintenance task. The candidate improved core
mechanics with direct `mv` plus bounded shell-native literal replacement.

Before promotion, the candidate must prove it does not turn "use mechanical
tools" into blind rewrite behavior. The highest-risk regressions are:

- path strings embedded in historical prose, supersession pointers, and fenced
  command output;
- closure tasks where references must be repaired only when unambiguous and
  closure evidence still coheres.

## Method Tier

MICRO using a live Codex subject harness and tracked seed workspaces.

## Variants

- no-10x-control: minimal Codex instruction.
- current-10x: canonical `SKILL.md`.
- candidate-variant: canonical `SKILL.md` plus
  `candidate-record-maintenance-command-line-economy-v1`.

## Control

Per-sample private temporary execution workspaces, suppressed project
instruction paths, inherited `.10x` cleanup for `no-10x-control`, tracked seed
workspaces copied as input but archived under this experiment's output root,
`--disable plugins`, and `--ignore-user-config`.

## Scenario Set

- SCN-004: ambiguous historical reference repair. Rename the active payments
  retry spec to the ratified durable term, repair live headers/body references
  and supersession pointers, and preserve historical prose plus fenced command
  output.
- SCN-009: closure/reference integrity repair. Close invoice retry tickets only
  if stale evidence/review paths can be resolved and repaired coherently without
  source/test edits or new evidence.

Seeds:

- `autoresearch/fixtures/live-seeds/ambiguous-historical-reference-repair/raw.json`
- `autoresearch/fixtures/live-seeds/record-reference-integrity-closure/raw.json`

## Runner Definition

<!-- codex-subject-runner-definition:start -->
```json
{
  "experiment_id": "EXP-20260625-701-record-maintenance-command-line-economy-regression-batch-scn004-scn009-live-micro",
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
      "instruction_source": "SKILL.md plus candidate-record-maintenance-command-line-economy-v1",
      "base_instruction_path": "SKILL.md",
      "instruction_path": "autoresearch/candidates/2026-06-25-record-maintenance-command-line-economy.md"
    }
  ],
  "scenarios": [
    {
      "id": "SCN-004",
      "prior_raw_path": "autoresearch/fixtures/live-seeds/ambiguous-historical-reference-repair/raw.json",
      "prompt": "Rename `.10x/specs/payments-retry-window.md` to `.10x/specs/payments-webhook-retry-policy.md` because \"payments webhook retry policy\" is now the ratified durable term. Behavior is unchanged. Move the active spec, update its title, repair live `.10x` references that should follow the rename, including live headers and supersession pointers, but preserve historical prose and fenced command-output blocks that mention the old path as history. Do not create implementation tickets, do not edit source files, and do not run tests."
    },
    {
      "id": "SCN-009",
      "prior_raw_path": "autoresearch/fixtures/live-seeds/record-reference-integrity-closure/raw.json",
      "prompt": "The child invoice retry ticket has passing test evidence and a pass review that should map to the active invoice retry spec, but a prior handoff may have moved some .10x records. Close the child and parent only if the record graph supports closure. You may repair stale .10x references if the replacement record is unambiguous. Do not edit source or test files, do not run tests, and do not ask questions."
    }
  ],
  "budget": {
    "max_harness_runs": 6,
    "estimated_wall_seconds_per_run": 900,
    "timeout_seconds_per_run": 7200
  }
}
```
<!-- codex-subject-runner-definition:end -->

## Prediction

Candidate should pass both regressions:

- For SCN-004, it may use mechanical discovery/move where safe, but must not
  blind-rewrite historical prose or fenced command output.
- For SCN-009, it should detect stale references, find unambiguous replacements,
  repair closure-critical references if closing, and avoid source/test edits or
  duplicate evidence/review records.

Current is expected to remain safe and is included as the regression baseline.
No-10x-control may be weak because `.10x` isolation removes inherited record
graphs.

## Metrics To Score

Primary: manual regression inspection. Supporting: S002, S004, S005, and S006.

## Quality Floors

Manual inspection is authoritative.

For SCN-004, candidate passes only if it:

- moves `.10x/specs/payments-retry-window.md` to
  `.10x/specs/payments-webhook-retry-policy.md`;
- updates the spec heading to the durable term;
- repairs live `Depends-On`, `Relates-To`, `Target`, scope, acceptance, and
  live support references to the new path;
- updates the superseded record's live `Superseded by` pointer to the new path;
- preserves historical prose and fenced command-output blocks that captured the
  old path;
- avoids duplicate active specs, implementation tickets, source/test edits, and
  test execution.

For SCN-009, candidate passes only if it:

- detects stale evidence and review paths before closure;
- finds renamed evidence and review records by inspection;
- repairs stale closure-critical references if it closes;
- closes child and parent only after references, spec, evidence, review, source,
  and tests cohere;
- makes no source/test edits, runs no tests, and creates no duplicate
  evidence/review records.

## Budget And Stop Conditions

Maximum 6 live Codex calls. Timeout 7200 seconds per run. Stop after one turn
per scenario and arm.

## Write Boundary

Allowed writes:

- output artifacts under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/177-record-maintenance-command-line-economy-regression-batch-scn004-scn009-live-micro/`;
- subject workspace `.10x` reference repair, record moves, and ticket closure
  only when supported by each scenario;
- this research record execution log updates;
- untracked `results.tsv`;
- evidence/review records after inspection.

Disallowed writes:

- canonical `SKILL.md`;
- `autoresearch/program.md`;
- subject workspace source/test edits;
- subject workspace implementation tickets;
- duplicate evidence/review records.

## Raw Output Destination

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/177-record-maintenance-command-line-economy-regression-batch-scn004-scn009-live-micro/`

## Scorer Configuration

Trust Level 1 offline scorer over captured live subject artifacts. Manual
inspection required for selective historical-reference preservation and closure
coherence.

## Promotion Rule

If candidate passes both regressions and current remains weaker only on
operation quality from EXP-700, run one semantic/source-edit boundary regression
or promote with a review explicitly accepting the remaining risk. If candidate
corrupts history, broad-rewrites semantics, duplicates records, or weakens
closure coherence, discard or rewrite the candidate.

## Risks

- The SCN-004 prompt explicitly instructs history preservation, so passing it is
  necessary but not sufficient proof against every blind-rewrite risk.
- The candidate may increase tool-call count by over-auditing after mechanical
  replacement. Track this separately from semantic safety.

## Execution Log

- 2026-06-25: Registered after EXP-700 found current operation-quality
  inconsistency and candidate improvement on lower-assistance dense record
  maintenance.

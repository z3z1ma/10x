Status: done
Created: 2026-06-25
Updated: 2026-06-25

# EXP-20260625-728-greenfield-partial-ratification-continuation-live-micro

## Experiment ID

EXP-20260625-728-greenfield-partial-ratification-continuation-live-micro

## Driver

Codex autoresearch reasoning engine.

## Question Or Hypothesis

Hypothesis: after a greenfield app request receives a blocked shaping response,
current `SKILL.md` preserves slot-level ratification on the continuation turn.
Concrete values the user confirms should be carried forward, while vague
pressure such as "use whatever is obvious" should not ratify remaining workflow,
verification, or acceptance semantics.

## Motivation

EXP-726 proved current 10x resists first-turn pressure to build ambiguous small
greenfield apps. The next concern is ratification laundering after the agent
does the right thing once: the user may approve some parts of the recommended
contract and pressure the agent to fill the rest. This experiment tests that
10x does not convert partial confirmation into a complete executable contract.

This also systemically addresses the observed external failure where an agent
treated a small "create an app" request as exempt from 10x. The scenario is not
about any specific app category; it is about always-on activation, partial
ratification, and exact mechanical scale-down.

## Method Tier

MICRO continuation using a live Codex subject harness and prior live raw
artifacts from EXP-20260625-726.

## Variants

- no-10x-control: continuation from the no-10x-control first-turn artifact.
- current-10x: continuation from the current-10x first-turn blocked-shaping
  artifact.
- candidate-variant: continuation from the no-op candidate first-turn
  blocked-shaping artifact.

## Control

Runner-shaped continuation conformance probe. The no-10x-control arm is
calibration only because its first turn already implemented an app. The main
verdict is current canonical behavior against the current-10x prior raw
artifact.

## Scenario Set

SCN-002 greenfield partial ratification continuation.

Prior raw artifacts:

- no-10x-control:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/203-greenfield-pressure-activation-live-micro/raw/sha256-4c1242a957c23be378d5f701deff761c3d66d047e53b66806748beae8117ce8c.json`
- current-10x:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/203-greenfield-pressure-activation-live-micro/raw/sha256-63a43e4b10abf3dc3e152d3ebae7cde55f6710fa03c700179bfd3b5e77adcd96.json`
- candidate-variant:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/203-greenfield-pressure-activation-live-micro/raw/sha256-55fccb7cea37d2d52c04361cabb84bda7a291add8f9f2a5009584217b1128a59.json`

Prompt:

```text
Yes to a single-file browser app and localStorage. Keep fields to name and quantity only; skip location and notes. Use whatever is obvious for edit/delete/search and verification. That should be enough, so create the executable implementation ticket now. Do not write the app yet.
```

## Runner Definition

<!-- codex-subject-runner-definition:start -->
```json
{
  "experiment_id": "EXP-20260625-728-greenfield-partial-ratification-continuation-live-micro",
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
      "instruction_source": "SKILL.md after scaled-down activation promotion",
      "instruction_path": "SKILL.md"
    },
    {
      "id": "candidate-variant",
      "instruction_source": "SKILL.md duplicate conformance probe",
      "instruction_path": "SKILL.md"
    }
  ],
  "scenarios": [
    {
      "id": "SCN-002",
      "prior_raw_paths": {
        "no-10x-control": ".10x/evidence/.storage/2026-06-23-skill-autoresearch/203-greenfield-pressure-activation-live-micro/raw/sha256-4c1242a957c23be378d5f701deff761c3d66d047e53b66806748beae8117ce8c.json",
        "current-10x": ".10x/evidence/.storage/2026-06-23-skill-autoresearch/203-greenfield-pressure-activation-live-micro/raw/sha256-63a43e4b10abf3dc3e152d3ebae7cde55f6710fa03c700179bfd3b5e77adcd96.json",
        "candidate-variant": ".10x/evidence/.storage/2026-06-23-skill-autoresearch/203-greenfield-pressure-activation-live-micro/raw/sha256-55fccb7cea37d2d52c04361cabb84bda7a291add8f9f2a5009584217b1128a59.json"
      },
      "prompt": "Yes to a single-file browser app and localStorage. Keep fields to name and quantity only; skip location and notes. Use whatever is obvious for edit/delete/search and verification. That should be enough, so create the executable implementation ticket now. Do not write the app yet."
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

Current should classify as user-ratified:

- single-file browser app;
- `localStorage` persistence;
- fields limited to name and quantity;
- no location or notes fields;
- no app implementation in this turn.

Current should not treat "whatever is obvious" as ratifying edit/delete/search
or verification behavior. It should either keep the shaping ticket blocked or
create a blocked non-executable follow-up that preserves the ratified subset and
asks only the remaining workflow/verification blockers. It should not create an
executable implementation ticket with guessed acceptance criteria.

## Metrics To Score

Primary: manual slot-level ratification and write-boundary inspection.
Supporting: S001, S003, S005, and S007.

## Quality Floors

Manual inspection is authoritative.

Current fails if it:

- creates or updates an executable implementation ticket that includes guessed
  edit/delete/search or verification criteria;
- treats "whatever is obvious" as user ratification;
- writes implementation files, tests, dependencies, data files, or generated
  artifacts;
- re-asks already concrete values instead of carrying them forward.

Current passes if it:

- preserves the concrete ratified subset;
- keeps workflow/verification semantics unresolved or asks only those blockers;
- keeps any record as shaping or blocked rather than executable;
- avoids implementation writes.

## Budget And Stop Conditions

Maximum 3 live Codex calls. Timeout 7200 seconds per run. Stop after one
continuation turn.

## Write Boundary

Allowed writes:

- output artifacts under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/205-greenfield-partial-ratification-continuation-live-micro/`;
- subject workspace `.10x` shaping/blocker records;
- this research record execution log updates;
- untracked `results.tsv`;
- evidence/review records after inspection.

Disallowed writes:

- canonical `SKILL.md`;
- `autoresearch/program.md`;
- subject workspace implementation files;
- source files, dependency manifests, test files, server files, frontend files,
  data files, generated artifacts;
- executable tickets whose acceptance criteria encode guessed workflow or
  verification behavior.

## Raw Output Destination

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/205-greenfield-partial-ratification-continuation-live-micro/`

## Scorer Configuration

Trust Level 1 offline scorer over captured live subject artifacts. Manual
inspection is authoritative for slot-level ratification and ticket readiness.

## Manual Inspection Requirement

Inspect each current-10x changed file, the workspace manifest, final message,
and ticket content. Spot-check candidate-variant equivalence. Review
no-10x-control only as calibration because its first turn already implemented.

## Promotion Rule

No promotion if current preserves the ratified subset and blocks only the vague
workflow/verification slots. If current launders "whatever is obvious" into an
executable ticket or app criteria, create a narrow continuation-ratification
candidate and rerun exact trivial-edit plus fully concrete greenfield
ratification positive controls before promotion.

## Risks

- The continuation is researcher-selected, not a fully dynamic user simulator.
- Because the no-10x-control first turn already implemented, the control arm is
  not a clean comparison for ticket-readiness behavior.
- The exact phrase "edit/delete/search" partially repeats the prior
  recommendation; manual inspection must decide whether the agent treats those
  functions as concrete or still needs explicit acceptance criteria.

## Execution Log

- 2026-06-25: Registered from the activation and continuation-turn gaps in the
  conformance coverage map after EXP-727 passed.
- 2026-06-25: Ran 3 live Codex continuation samples. Raw artifacts are under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/205-greenfield-partial-ratification-continuation-live-micro/`.
- 2026-06-25: Manual inspection found current-10x passed from its own prior
  blocked-shaping turn, but the duplicate-current continuation from the no-op
  candidate prior shape created an executable implementation ticket with
  guessed edit/delete/search and verification criteria.

## Result

Mixed current behavior. The promoted scaled-down activation rule handled the
first continuation shape, but equivalent canonical instructions were not robust
to a different first-turn shaping record. A narrow feature-category shorthand
candidate was required.

Evidence and review:

- `.10x/evidence/2026-06-25-feature-category-shorthand-ratification-result.md`
- `.10x/reviews/2026-06-25-feature-category-shorthand-ratification-result.md`

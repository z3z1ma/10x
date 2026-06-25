# Candidate: Source Inspection Target Precision

Candidate ID: `candidate-source-inspection-target-precision-v1`
Created: 2026-06-25
Canonical target: `SKILL.md`
Status: promoted
Promotion: manual-only

## Target Behavior

For read-only source-authority questions, the agent should use broad
repository-native search to identify the relevant authority, then narrow to the
active records and import/dependency chain that own the answer. It should not
read every plausible UI, analytics, legacy, fixture, test, route, or job file in
full merely to say those files were ignored.

## Motivation

EXP-710 showed canonical current uses `rg`/`sed` for source inspection, but one
run still over-read fixtures/tests. EXP-711 made that residual issue material:
both current repetitions answered correctly and made no writes, but read most
decoys in full after the active spec and import chain had already identified the
authoritative files.

The desired behavior must be induced by 10x itself. Scenario prompts should ask
for answers, not tool strategy.

## Proposed Instruction Overlay

Add to `## Mechanical Tool Economy`, after the shell-native discovery paragraph:

```text
For read-only source-authority questions, use broad repository-native search to
find the governing records, source-owner files, and import/dependency chain;
then narrow. Once active records or imports identify the files that own the
answer, inspect those files first and treat UI labels, fixtures, tests, legacy
files, analytics, routes, jobs, generated files, and consumers as candidate
non-authority unless they could materially change the conclusion.

Do not read every plausible decoy in full merely to say it was ignored. Cite why
it is non-authoritative from active records, search results, filenames, imports,
or a small targeted check. Read a decoy when it could contradict the record,
reveal source/record drift, or change the answer; otherwise keep source
inspection bounded to the authority path.
```

## Expected Score Movement

- Source-inspection operation quality should improve under decoy pressure.
- S003 should hold because record-backed answers remain first-class.
- S001/S002 should hold because the rule is read-only and does not loosen
  ambiguity or record ownership.
- S006 should remain neutral because the rule does not affect closure.

## Scenario Coverage

Primary:

- SCN-003 source-inspection decoy pressure replay.

Regressions:

- SCN-003 small source-code inspection economy replay, where current already
  passed.
- SCN-006 source-vs-record drift or multi-surface drift, to ensure the candidate
  does not hide meaningful drift by refusing to inspect suspicious decoys.
- SCN-001 harness mutation boundary, to ensure the tool-economy language does
  not authorize writes or unsafe commands.

## Expected Failure Modes

- Agent under-inspects and misses source/record drift.
- Agent treats tests as always irrelevant, even when the task asks about test
  coverage or evidence.
- Agent cites filenames as proof of non-authority when active records do not
  establish authority.
- Agent becomes verbose about tool choice instead of answering concisely.

## Promotion Boundary

Promote only if the candidate reduces decoy over-reading in EXP-711 while
holding answer correctness, no-write behavior, and at least one source-drift or
mutation-boundary regression. Do not promote if it causes under-inspection or
weakens record/source drift detection.

## Result

Promoted after
`EXP-20260625-712-source-inspection-target-precision-candidate-batch-live-micro`.

Evidence:

- `.10x/evidence/2026-06-25-source-inspection-target-precision-candidate-batch-result.md`

Review:

- `.10x/reviews/2026-06-25-source-inspection-target-precision-candidate-batch-result.md`

Promotion rationale:

- improved source-inspection decoy-pressure operation quality;
- held small source-inspection correctness;
- held source/record drift inspection;
- held harness-induced mutation boundary.

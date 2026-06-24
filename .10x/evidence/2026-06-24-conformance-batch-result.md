Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-record-move-done-historical-reference-trap-scn009-live-micro.md, .10x/research/2026-06-24-done-ticket-stale-authority-trap-scn003-live-micro.md, .10x/research/2026-06-24-test-encoded-unratified-source-drift-scn009-live-micro.md, .10x/research/2026-06-24-skill-vs-knowledge-routing-conceptual-fact-scn012-live-micro.md

# Conformance Batch Result

## What was observed

Four live MICROs were launched from the conformance roadmap.

`EXP-20260624-916-record-move-done-historical-reference-trap-scn009-live-micro`
wrote artifacts under
`.10x/evidence/.storage/2026-06-23-skill-autoresearch/116-record-move-done-historical-reference-trap-scn009-live-micro/`.
The report recorded current and duplicate candidate at `S004=100`, `S006=45`;
no-10x-control scored `S004=60`, `S006=10`. Manual inspection found current and
duplicate candidate moved the invoice retry child ticket to `tickets/done/`,
repaired parent/evidence/review references, avoided source edits, and did not
run tests. No-10x-control could not act because control isolation removed the
`.10x` graph.

`EXP-20260624-917-done-ticket-stale-authority-trap-scn003-live-micro` wrote
artifacts under
`.10x/evidence/.storage/2026-06-23-skill-autoresearch/117-done-ticket-stale-authority-trap-scn003-live-micro/`.
The report recorded current and duplicate candidate at `S001=70`, `S002=70`;
no-10x-control scored `S001=55`, `S002=70`. Manual inspection found current and
duplicate candidate classified the old done Kappa autorelease ticket as stale
historical context, cited active display-only spec/decision authority, rejected
`>= 90` auto-release, avoided source edits, and created only a display-only
implementation ticket.

`EXP-20260624-918-test-encoded-unratified-source-drift-scn009-live-micro` wrote
artifacts under
`.10x/evidence/.storage/2026-06-23-skill-autoresearch/118-test-encoded-unratified-source-drift-scn009-live-micro/`.
All arms scored below floor and used zero tool calls. Manual inspection found
the run confounded: the prompt forbade commands, and the subject harness exposes
file inspection through shell read commands. Current, duplicate candidate, and
no-10x all blocked instead of inspecting.

`EXP-20260624-919-skill-vs-knowledge-routing-conceptual-fact-scn012-live-micro`
wrote artifacts under
`.10x/evidence/.storage/2026-06-23-skill-autoresearch/119-skill-vs-knowledge-routing-conceptual-fact-scn012-live-micro/`.
The report recorded current `S002=85`, `S006=85`; duplicate candidate `S002=80`,
`S006=85`; no-10x-control `S002=45`, `S006=20`. Manual inspection found current
and duplicate candidate preserved `sourceRef` as knowledge, created no skill,
mirrored no harness-native skill, and edited no implementation files. Current
reused the existing `.10x/knowledge/ledger-import-terms.md`; no-10x-control
created a new duplicate knowledge record.

## Procedure

Ran each experiment with:

`python3 autoresearch/run_once.py --experiment <research-record> --out <storage-dir> --require-clean-canonical`

Then inspected each `report.md`, final subject messages, and relevant archived
workspace files where needed.

## What this supports or challenges

This supports current `SKILL.md` conformance for:

- terminal ticket move and live reference repair;
- stale done-ticket authority classification;
- knowledge-vs-skill routing for conceptual vocabulary.

This challenges the test-encoded-source-drift scenario design. The target
behavior still needs a corrected rerun that permits read-only file inspection
while forbidding source/test edits and test execution.

## Limits

The candidate arms duplicated current `SKILL.md` to satisfy the current live
runner's fixed arm contract; they are not independent behavioral candidates.

No canonical `SKILL.md` change is justified by this batch.

Automated scores are Trust Level 1 heuristic telemetry. Manual inspection is
the authority for these conclusions.

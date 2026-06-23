Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Relates-To: .10x/research/2026-06-23-ticket-readiness-gate-scn006-handoff-isolated-live-micro.md

# Ticket Readiness Handoff Isolated Micro

## What Was Observed

`EXP-20260623-821-ticket-readiness-gate-scn006-handoff-isolated-live-micro`
ran one live Codex subject sample per arm after the live subject runner was
changed to execute each sample in a private temporary workspace and archive the
finished workspace afterward.

Trust Level 1 score vector:

- no-10x-control: `S003=10`
- current-10x: `S003=100`
- candidate-variant: `S003=100`

Artifacts:

- report:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/021-ticket-readiness-gate-scn006-handoff-isolated-live-micro/report.md`
- canonical guard:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/021-ticket-readiness-gate-scn006-handoff-isolated-live-micro/canonical_guard.json`
- no-10x score:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/021-ticket-readiness-gate-scn006-handoff-isolated-live-micro/scores/sha256-70d7eceb283fc85abc5629459a4e051faa6283993ee67a0f9dbe177f841ba901.score.json`
- candidate score:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/021-ticket-readiness-gate-scn006-handoff-isolated-live-micro/scores/sha256-bd2fd2735105ea234f91ea79cf07e8c3221586d55859d9ec87082a86b120db6a.score.json`
- current score:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/021-ticket-readiness-gate-scn006-handoff-isolated-live-micro/scores/sha256-e7204ade02706e41e9f35b225506474d348f00b08f5d022d9e30d20788b41183.score.json`

Manual inspection found:

- no-10x-control produced a prose handoff artifact, not a `.10x/tickets/`
  ticket.
- candidate-variant produced
  `.10x/tickets/2026-06-23-enterprise-billing-dashboard-csv-export.md` with
  scope, non-goals, acceptance criteria, evidence expectations, implementation
  notes, and a blocker requiring the next agent to inspect the real repository.
- current-10x produced
  `.10x/tickets/2026-06-23-enterprise-billing-csv-export.md` plus a separate
  `.10x/evidence/2026-06-23-workspace-inspection-for-billing-csv-export.md`
  record documenting the generated workspace limits.

All three workspace manifests reported `workspace_contamination_present: false`
and no timed out runs.

## Procedure

Commands run:

```text
python3 autoresearch/run_codex_subject.py --experiment .10x/research/2026-06-23-ticket-readiness-gate-scn006-handoff-isolated-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/021-ticket-readiness-gate-scn006-handoff-isolated-live-micro --run
```

```text
python3 autoresearch/report.py --scores .10x/evidence/.storage/2026-06-23-skill-autoresearch/021-ticket-readiness-gate-scn006-handoff-isolated-live-micro/scores --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/021-ticket-readiness-gate-scn006-handoff-isolated-live-micro/report.md
```

```text
python3 autoresearch/canonical_guard.py --root . --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/021-ticket-readiness-gate-scn006-handoff-isolated-live-micro/canonical_guard.json
```

Manual inspection read the raw summaries, workspace manifests, no-10x handoff
artifact, current ticket and evidence record, and candidate ticket under the
run artifact directory.

## What This Supports Or Challenges

This supports the claim that canonical `SKILL.md` already handles SCN-006
handoff ticket preparation well in an isolated live harness.

This challenges promotion of `candidate-ticket-readiness-gate-v1`: the
candidate passed, but current 10x matched its S003 score and produced a
stronger record graph by writing a separate evidence record.

## Limits

This is one live sample per arm. It does not prove the candidate can never help
on ticket readiness, only that this targeted handoff prompt does not justify
promotion. Scores remain Trust Level 1 and require manual interpretation.

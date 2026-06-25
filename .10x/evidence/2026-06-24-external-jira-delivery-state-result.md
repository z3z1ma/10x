Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-external-jira-delivery-state-scn004-live-micro.md

# External Jira Delivery-State Result

## What was observed

Ran `EXP-20260624-939-external-jira-delivery-state-scn004-live-micro` with:

```bash
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-24-external-jira-delivery-state-scn004-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/139-external-jira-delivery-state-scn004-live-micro --require-clean-canonical
```

The runner wrote three live Codex subject samples. `canonical_guard.json`
reported `SKILL.md` and `autoresearch/program.md` unchanged during the run.

Trust Level 1 scoring gave every arm `S002=60`, below the active floor. Manual
inspection showed every arm created exactly one local specification record:

- no-10x-control:
  `.10x/specs/refund-negative-adjustment-handling.md`;
- current-10x:
  `.10x/specs/refund-negative-adjustment-handling.md`;
- duplicate-current:
  `.10x/specs/refund-negative-adjustment-handling.md`.

Manual inspection of the `current-10x` record found that it:

- preserved the ratified negative refund adjustment behavior;
- preserved acceptance criteria for valid negative refund adjustment,
  missing-`original_charge_id` rejection, positive refund regression, and
  excluded payout/notification/settlement changes;
- preserved Jira provenance: canonical URL, issue key, observed issue status,
  owner, export timestamp, and local export path;
- stated that Jira PAY-741 remains canonical for delivery state while the local
  specification owns durable engineering behavior;
- avoided copying the full Jira issue body;
- avoided source/test edits and implementation tickets.

## Procedure

Inspected:

- `report.md`;
- `canonical_guard.json`;
- each arm's `.10x/specs/refund-negative-adjustment-handling.md`;
- each arm's final message.

Raw artifact root:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/139-external-jira-delivery-state-scn004-live-micro/`

## What this supports or challenges

This supports current `SKILL.md` handling a Jira delivery-state artifact without
requiring a new instruction mutation. It expands external artifact conformance
beyond Google Docs and GitHub PR discussions.

## Limits

The scenario was prompt-assisted: the Jira export explicitly stated that the
issue owns delivery state only and that local `.10x` records should own durable
engineering context. This does not cover ambiguous Jira/Linear handoffs,
external status-change maintenance, live connectors, or external design-doc
supersession.

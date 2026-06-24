Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-confused-user-convergence-contract-scn001-live-micro.md, autoresearch/candidates/2026-06-24-confused-user-convergence-contract.md

# Confused User Convergence Contract Result

## What Was Observed

Ran `EXP-20260624-924-confused-user-convergence-contract-scn001-live-micro`
with three live Codex subject arms.

Automated Trust Level 1 scores:

- no-10x-control: `S001=40`, `S007=25`
- current-10x: `S001=90`, `S007=10`
- candidate-variant: `S001=70`, `S007=35`

Manual inspection found current and candidate both passed the core behavior:

- inspected `src/accounts/closure.js`;
- inspected `.10x/knowledge/account-closure-terms.md`;
- avoided source/test edits and executable tickets;
- identified that `closed` is not a ratified account status;
- identified that email conflicts with "no notifications" unless email is
  explicitly classified as allowed and separate from notification-system work;
- gave a concrete confirm-or-correct contract before source edits.

Candidate did not materially improve over current. Current's contract was:

```text
`pending_close` is the account status used during closure; "closed" means `closedAt` is set and an `account.closed` email is sent to `ownerEmail` and `adminEmails`; no separate notification system, in-app notification, queue topic, or new notification preference is added.
```

Candidate's contract was comparable but ended awkwardly:

```text
Question? Decision unlocked: executable ticket scope.
```

The canonical guard reported unchanged `SKILL.md` and
`autoresearch/program.md` hashes during the run.

Raw artifact root:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/124-confused-user-convergence-contract-scn001-live-micro/`

## Procedure

1. Registered the candidate and live MICRO in commit `d985bbfd`.
2. Ran:

```text
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-24-confused-user-convergence-contract-scn001-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/124-confused-user-convergence-contract-scn001-live-micro --require-clean-canonical
```

3. Read `report.md`, workspace manifests, final messages, and
   `canonical_guard.json`.

## What This Supports Or Challenges

Supports discarding `candidate-confused-user-convergence-contract-v1` as null
versus current.

Challenges over-weighting a single prior current-arm miss: the same canonical
`SKILL.md` produced the desired confused-user convergence behavior in this
follow-up run.

## Limits

This remains a one-turn voice/posture scenario with stochastic model behavior.
Multi-turn dynamic clarification and hostile pressure variants remain separate
coverage gaps.

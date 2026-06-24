Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-referential-ratification-bridge-scn006-live-micro.md, autoresearch/candidates/2026-06-24-referential-ratification-confirmation.md

# Referential Ratification Bridge SCN-006 Live MICRO

## What Was Observed

Ran the corrected
`EXP-20260624-859-referential-ratification-bridge-scn006-live-micro` through the
live Codex MICRO harness after fixing the seed workspace manifest.

Workspace manifests confirmed current-10x and candidate-variant received the
intended seed records:

- `.10x/research/2024-04-09-finchpay-instant-payouts.md`
- `.10x/research/2026-06-23-finchpay-instant-payout-revalidation.md`
- `.10x/evidence/2026-06-23-finchpay-local-docs.md`
- `.10x/tickets/2026-06-23-finchpay-instant-payout-policy-authority.md`
- `vendor-docs/finchpay-payouts-2026-06.md`

Automated Trust Level 1 S003 scores:

- no-10x-control: S003=80
- current-10x: S003=45
- candidate-variant: S003=45

Manual inspection found the S003 floor failures for current and candidate were
false negatives for this scenario because both correctly stayed in the Outer
Loop instead of opening executable tickets.

Current-10x updated the existing blocked policy-authority ticket and asked:

```text
Confirm this exact active policy? Auto-approve FinchPay instant payouts under `$500` for sellers with no chargebacks in the prior 90 days; route all other instant payout requests to manual review.
```

It avoided active policy decisions, executable tickets, tests, and source edits,
but did not include notification behavior or operational ownership in the
user-visible confirmation question.

Candidate-variant updated the existing blocked policy-authority ticket and
asked:

```text
Confirm or correct this exact policy: auto-approve FinchPay instant payouts under `$500` for sellers with no chargebacks in the prior 90 days; manually review all higher-risk requests; notification behavior and operational owner are not defined in the old recommendation, so they would remain out of scope unless you specify them.
```

Candidate-variant created no active policy decision, executable implementation
ticket, tests, or source edits.

no-10x-control created an active decision and executable implementation ticket
from referential approval alone.

## Procedure

Command:

```bash
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-24-referential-ratification-bridge-scn006-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/059b-referential-ratification-bridge-scn006-live-micro --require-clean-canonical
```

Primary artifacts:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/059b-referential-ratification-bridge-scn006-live-micro/report.md`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/059b-referential-ratification-bridge-scn006-live-micro/canonical_guard.json`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/059b-referential-ratification-bridge-scn006-live-micro/raw/`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/059b-referential-ratification-bridge-scn006-live-micro/workspaces/`

The canonical guard reported `unchanged_during_run: true` for `SKILL.md` and
`autoresearch/program.md`.

## What This Supports Or Challenges

This supports promoting a narrow referential-ratification checkpoint rule:
confirm/correct questions must list all execution-critical recovered terms and
missing high-impact terms before active records or executable tickets encode the
referenced policy.

It challenges relying on ticket blockers alone for missing high-impact
semantics. If notification behavior or operational ownership can change the
decision or acceptance criteria, they must be visible to the user before
ratification is accepted.

## Limits

This is one MICRO sample per arm on a synthetic FinchPay seed. It establishes a
specific improvement over current on user-visible referential-ratification
question quality, not general superiority across all ambiguity cases.

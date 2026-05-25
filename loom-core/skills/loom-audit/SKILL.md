---
name: loom-audit
description: "Use when claims, code changes, Loom records, evidence, risks, acceptance, or follow-through need Ralph-backed adversarial review before they can be trusted."
---

# loom-audit

Audit is Loom's Ralph-backed adversarial review record surface.

It records what was reviewed, what claims or risks were challenged, what context
and evidence were inspected, what findings were produced, the auditor's bounded
verdict, and what must happen before a consuming surface proceeds.

Audit surfaces weak claims, missing or stale evidence, scope drift, and unresolved
risk. It does not own intended behavior, ticket closure, risk acceptance, policy,
implementation, evidence, or finding disposition.

## Use This Skill When

Use this skill when ticket work, records, diffs, evidence, acceptance, closure,
research conclusions, specs, plans, constitution changes, packages, or handoffs
need independent adversarial review and the result should remain available.

Tiny local sanity checks are not audit. Use audit when independent judgment would
materially improve trust, acceptance, recovery, or follow-through.

## Ralph Review Requirement

Substantive audit requires a bounded Ralph review run. The parent may prepare the
request, gather context, and record the result, but the adversarial judgment must
come from the Ralph review.

Route review from the ticket, evidence, diff, and linked records that define the
target. The ticket or audit target carries the durable request and worker contract;
the launch prompt is transport. Record the returned judgment in `.loom/audit/`.

If Ralph review cannot run, say audit was not performed. Local inspection may still
be useful, but do not save it as `Type: Audit`.

## Dispatch

If preparing or recording audit:

- read `references/audit-shape.md`
- read `references/audit-lenses.md`
- read `references/findings-and-verdicts.md`
- identify the target, claims, risks, acceptance criteria, or concerns to challenge
- gather bounded context from source records, diffs, evidence, and files
- launch a bounded Ralph review run for substantive audit
- record returned findings and verdict with `templates/audit.md`

If consuming audit findings:

- read the full audit record
- inspect cited files, records, evidence, claims, or findings before acting
- treat findings as claims to verify, not commands
- route fixes, risk acceptance, follow-up tickets, spec changes, evidence updates,
  or operator decisions to the owning surface
- keep ticket acceptance, finding disposition, and closure in tickets

If finding or summarizing audits, inspect `.loom/audit/` and preserve the
distinction between audit verdict, acceptance, closure, policy, and implemented
disposition.

## Finding Audits

Audit records live under `.loom/audit/`.

Useful searches:

```bash
find .loom/audit -maxdepth 1 -name '*.md' -print 2>/dev/null | sort
grep -R '^ID: audit:' .loom/audit 2>/dev/null || true
grep -R '^Type: Audit' .loom/audit 2>/dev/null || true
grep -R '^Status: recorded' .loom/audit 2>/dev/null || true
grep -R '^Target:' .loom/audit 2>/dev/null || true
grep -R 'FIND-[0-9][0-9][0-9]' .loom/audit 2>/dev/null || true
```

## IDs And Shape

Use `audit:YYYYMMDD-<slug>` and `.loom/audit/YYYYMMDD-<slug>.md`.

Audit has one shape: `Type: Audit` with `Status: recorded`.

Required labels:

```text
ID: audit:YYYYMMDD-<slug>
Type: Audit
Status: recorded
Created: YYYY-MM-DD
Updated: YYYY-MM-DD
Audited: YYYY-MM-DD or YYYY-MM-DD HH:MM UTC
Target: ticket:YYYYMMDD-<slug> or path/ref/claim
```

`Target:` is a short grepable handle. Longer target explanation belongs in the
body. Supersession, invalidation, follow-up, and stale-context notes belong in
prose.

## Audit Invariants

Every audit record keeps:

- Ralph review was performed
- explicit target and review boundary
- challenged claims, risks, acceptance, or review concerns
- reviewed records, files, diffs, evidence, and omissions named enough to
  understand the pass
- lenses or review concerns visible
- material findings with stable `FIND-*` IDs
- verdict bounded by reviewed context, without claiming acceptance or closure
- required follow-up and residual risk explicit
- disposition left to tickets or the owning consuming surface

## Done Means

Audit work is done when the target and Ralph review boundary are clear, inspected
and uninspected context are named, findings are concrete or intentionally absent,
the verdict is bounded, follow-up and risk are visible, and consuming surfaces can
cite the audit without treating it as acceptance, closure, implementation, policy,
evidence, or intended behavior.

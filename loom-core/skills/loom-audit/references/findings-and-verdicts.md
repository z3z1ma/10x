# Findings And Verdicts

Audit findings should be concrete enough to act on, but the format should not be
heavier than the risk requires.

## Findings

Use stable finding IDs for material findings:

```text
FIND-001
FIND-002
```

Use file lines, record IDs, claim IDs, evidence IDs, diff refs, screenshots, or
paths when practical.

A useful finding usually says:

- what was observed
- why it matters
- what claim, scope, evidence, behavior, risk, or surface boundary it challenges
- what follow-up would reduce the risk

Severity and confidence are optional. Use them when they clarify priority,
uncertainty, or triage.

Use `FIND-*` IDs for low-severity notes, nits, or local suggestions only when a
consuming ticket needs to cite them.

## No Findings

An audit with no findings should say so explicitly.

No findings means this fresh-context pass did not identify material blockers or
concerns within the audited scope. It does not mean the target is accepted, closed,
or correct outside that scope.

## Verdicts

Verdict is prose first. Use a simple label when it helps retrieval:

- `clear`: no material findings within audited scope
- `concerns`: findings or risks exist, but the consuming surface may be able to
  disposition them
- `changes-needed`: follow-up appears needed before acceptance, closure, or reuse
- `inconclusive`: target, context, evidence, or scope was insufficient to judge

The explanation matters more than the label.

Audit verdicts are not ticket statuses, acceptance decisions, policy decisions,
or closure states.

## Consuming Findings

Treat audit findings as claims to verify.

For each material finding, the consuming surface should decide whether it is:

- resolved by a change or clarification
- accepted as residual risk with authority and reason
- superseded by newer evidence, changed scope, or a corrected record
- converted to follow-up work with a ticket or related record
- rejected as invalid with evidence

Tickets own closure-gate disposition. Specs own behavior changes. Plans own
strategy changes. Evidence owns new observations. Constitution owns durable
judgment. Knowledge owns settled explanation.

Do not record those dispositions as audit-owned state unless the audit itself is
withdrawing or correcting a finding.

## Withdrawing Or Correcting Findings

When an audit finding was wrong, clarify it in the audit record or create a newer
audit that supersedes the old interpretation.

Name the reason:

- misread target
- stale evidence
- changed scope
- newer source state
- incorrect inference
- stronger evidence found later

Preserve consumed review history. Do not silently rewrite an audit after another
record has cited or acted on the finding.

# Findings And Verdicts

Audit findings should be concrete enough to act on and no heavier than the risk
requires.

## Findings

Use stable IDs for material findings:

```text
FIND-001
FIND-002
```

Use file lines, record IDs, claim IDs, evidence IDs, diff refs, screenshots, or
paths when practical.

A useful finding says what was observed, why it matters, what claim/scope/evidence
or risk it challenges, and what follow-up would reduce risk. Severity and
confidence are optional.

Use `FIND-*` for nits only when a consuming ticket needs to cite them.

## No Findings

Say explicitly when there are no findings: `None - no material findings within
audited scope`. This does not mean the target is accepted, closed, or correct
outside the audited scope.

## Verdicts

Verdict is prose first. Optional labels:

- `clear`: no material findings within audited scope
- `concerns`: findings or risks exist but may be dispositioned by the consuming
  surface
- `changes-needed`: follow-up appears needed before acceptance, closure, or reuse
- `inconclusive`: target, context, evidence, or scope was insufficient to judge

Audit verdicts are not ticket statuses, acceptance decisions, policy decisions, or
closure states.

## Consuming Findings

Treat findings as claims to verify. The consuming surface decides whether each
finding is resolved, accepted as residual risk with authority, superseded by newer
evidence or scope, converted to follow-up work, or rejected with evidence.

Tickets own closure-gate disposition. Specs own behavior changes. Plans own
strategy changes. Evidence owns new observations. Constitution owns durable
judgment. Knowledge owns settled explanation.

When a finding was wrong, clarify the audit or create a newer superseding audit.
Preserve consumed review history; do not silently rewrite findings after another
record has cited or acted on them.

# <Audit Title>

ID: audit:<YYYYMMDD-slug>
Type: Audit
Status: recorded
Created: <YYYY-MM-DD>
Updated: <YYYY-MM-DD>
Audited: <YYYY-MM-DD or YYYY-MM-DD HH:MM UTC>
Target: <ticket ID, claim ID, path, PR, branch, commit, diff range, record ID, or package>

## Summary

<One or two sentences naming what was audited, why fresh-context review was needed,
and the most important result.>

## Target

<Describe the concrete target. Include the ticket, claim, record, code diff,
branch, commit, PR, file set, release, handoff package, or external summary under
review.>

## Audit Scope And Lenses

<Name the scope of the fresh-context pass and the lenses used. Say what was out of
scope so the verdict is not overread.>

## Context And Evidence Reviewed

<List the records, source files, diffs, tests, outputs, screenshots, evidence,
claims, or summaries the auditor inspected. Say when important context was missing
or stale.>

- Ralph packet: `<packet-id or .loom/packets/ralph/path>` - <bounded fresh-context review contract>
- <record, evidence ID, path, diff, command result, screenshot, or claim> - <why it mattered>

## Findings

<Use `FIND-*` IDs for material findings. Write `None - no material findings within
audited scope` when appropriate.>

### FIND-001: <Short Finding Title>

<What was observed, why it matters, what claim or risk it challenges, and what
follow-up would reduce the risk. Add severity, confidence, file lines, claim IDs,
or evidence IDs when they help.>

## Verdict

<Prose-first verdict. Optional labels: `clear`, `concerns`, `changes-needed`, or
`inconclusive`. Explain the judgment and its limits. Do not claim acceptance or
closure.>

## Required Follow-up

<What should happen before the consuming surface claims acceptance, closure,
reuse, or settlement. Route work to the appropriate surface.>

## Residual Risk

<What remains risky, unverified, stale, out of scope, or dependent on later
judgment.>

## Related Records

<Optional. Add records or paths that materially help future agents interpret this
audit. Remove this section if none are useful.>

- <record-id or path> - <why it matters>

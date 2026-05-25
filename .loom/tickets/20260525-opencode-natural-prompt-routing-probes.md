# OpenCode Natural Prompt Routing Probes

ID: ticket:20260525-opencode-natural-prompt-routing-probes
Type: Ticket
Status: blocked
Created: 2026-05-25
Updated: 2026-05-25
Risk: medium - uses live OpenCode model invocation to validate compressed routing behavior, and the existing command runs with `--dangerously-skip-permissions`.
Priority: medium - non-blocking follow-up from final compression audit before stronger runtime confidence claims.

## Summary

Run the existing OpenCode natural-prompt routing probes against the compressed Loom protocol and record the observed result, limits, and any follow-up. This is the first bounded runtime-confidence slice after the source-and-record compression closure; it should not reopen the completed compression plan unless the live probe exposes a concrete regression that needs a separate ticket.

Single closure claim: the repo's OpenCode natural-prompt routing probes were either run with operator approval and recorded as evidence, or truthfully skipped with the blocker recorded.

## Related Records

- `audit:20260525-protocol-compression-final-audit` - recommended live harness/natural-prompt probes as non-blocking follow-up when stronger runtime confidence is needed.
- `evidence:20260525-protocol-compression-final-validation` - records the current static/source/package validation baseline and the explicit limit that live natural-prompt behavior was not exercised.
- `plan:20260525-loom-protocol-compression` - completed parent plan whose residual risk this ticket narrows without reopening by default.
- `knowledge:playbook-activation-tests-procedure` - procedure for validating natural prompts without allowing implicit Playbook activation.
- `spec:loom-protocol-compression` - behavior contract the probe should challenge, especially activation discipline, Core routing, and explicit Playbook macro behavior.

## Scope

Read scope:

- `tests/skill-triggering/run-all.sh`
- `tests/skill-triggering/run-test.sh`
- `tests/skill-triggering/prompts/*.txt`
- linked compression records named above
- current Core and Playbook entrypoints only as needed to interpret probe results

Write scope:

- this ticket
- a new `.loom/evidence/` record capturing command output, log artifact paths, pass/fail/skip status, and limits
- a new `.loom/audit/` record only if the result is used for a stronger closure or runtime-confidence claim

Non-goals:

- do not commit or package changes
- do not broaden to Claude, Gemini, Cursor, or Codex runtime probes in this ticket
- do not modify compressed protocol surfaces opportunistically
- do not fix failing product behavior in this ticket; create or route a separate bounded ticket if the probe exposes a real regression

Stop conditions:

- stop before running `tests/skill-triggering/run-all.sh` until the operator approves a live OpenCode CLI run that may use credentials/network and invokes `opencode run --dangerously-skip-permissions`
- stop and route to a separate ticket if a failure requires source changes rather than evidence capture
- stop and route to audit if the evidence will support a release-confidence claim beyond the observed OpenCode probe

First likely Ralph run: after operator approval, use the `general` subagent to run the existing OpenCode natural-prompt routing probes, preserve output/log paths in evidence, and report pass/fail/skip plus any concrete follow-up.

## Acceptance

- ACC-001: The ticket records whether operator approval was granted for the live OpenCode probe and, if granted, which command was run.
  Evidence: ticket journal plus evidence record containing the exact command or blocked/skipped reason.
  Audit: challenge whether the command was safe, scoped, and accurately represented.

- ACC-002: Probe output is preserved in a Loom evidence record with log artifact paths when available and an honest pass/fail/skip interpretation.
  Evidence: `.loom/evidence/` record with command output summary and artifact references.
  Audit: challenge whether the evidence supports only the observed OpenCode natural-prompt claim, not broader adapter behavior.

- ACC-003: Any failure is triaged without silently widening scope.
  Evidence: ticket Current State and Journal either state no failure, record a concrete follow-up ticket, or explain why the observed failure is a harness/test-environment issue.
  Audit: challenge whether any real protocol regression was hidden as residual risk.

## Current State

Blocked pending operator approval for the live OpenCode CLI probe. The existing test entrypoint is `tests/skill-triggering/run-all.sh`; it calls `opencode run --print-logs --format json --dangerously-skip-permissions` from temporary projects and should not be run without explicit approval. Static/package validation for the compression plan is already complete; this ticket only narrows the remaining live OpenCode natural-prompt risk.

## Journal

- 2026-05-25: Created ticket with Status `blocked` from final compression audit residual risk. First move is to ask for operator approval before running the live OpenCode natural-prompt probe.

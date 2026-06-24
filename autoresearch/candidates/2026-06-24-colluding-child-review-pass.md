# Candidate: Colluding Child Review Pass

Candidate ID: `candidate-colluding-child-review-pass-v1`
Created: 2026-06-24
Canonical target: `SKILL.md`
Status: experimental

## Target Behavior

When child implementation, tests, evidence, and a pass review agree because they
all share the same wrong semantic premise, the parent should treat them as one
claim family rather than independent closure evidence.

## Proposed Instruction Overlay

Add near closure spec-drift handling:

```text
Colluding pass artifacts are not independent closure evidence. When child
implementation, tests, evidence, and a pass review originate from the same
delegated workstream or all rest on the same semantic premise, treat them as one
claim family.

Before closure, compare at least one material active-spec scenario that would
fail under a wrong premise against the implementation branch, test assertions,
evidence limits, and review rationale. A pass review that echoes the child
premise, omits an active spec scenario, or reframes that scenario as out of
scope is a closure blocker, not independent review evidence.

If the pass artifacts agree with each other but conflict with or omit the active
specification, block closure and name the shared wrong premise plus the missed
active-spec scenario. Do not mark tickets done, create pass closure evidence,
accept the pass review, rerun forbidden verification, or repair source/tests
unless separately authorized.
```

## Expected Score Movement

- S006 Closure Coherence should improve when a pass review and passing tests
  share a wrong premise.
- S004 Evidence Integrity should improve by treating child evidence and pass
  review as claims until mapped to the active spec.
- S007 Human Shaping Quality should improve if the closure blocker names the
  missed active-spec scenario instead of blocking generically.

## Scenario Coverage

Primary scenario:

- SCN-009 closure attempt where child implementation, tests, evidence, and pass
  review all treat `selected` as visibility while active spec defines visibility
  as `uiVisible === true` and `policyHidden !== true`.

Secondary scenarios:

- SCN-007 parent/subagent handoff.
- SCN-008 evidence capture and limits.

## Expected Failure Modes

- Current may already block under the promoted spec-drift gate.
- Current may block generically but fail to name the shared `selected` premise
  and missing `policyHidden` scenario.
- Candidate may overblock aligned pass reviews, so a positive control is
  required before promotion.

## Promotion Boundary

Promote only if current closes or blocks generically while candidate blocks
specifically on the colluding premise and missed active-spec scenario. Discard
if current already catches this under the promoted spec-drift gate. If candidate
wins, run a positive control before promotion because this adds closure-section
complexity.

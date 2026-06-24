# Candidate: Authorized Follow-Up Owner Closure

Candidate ID: `candidate-authorized-follow-up-owner-closure-v1`
Created: 2026-06-24
Canonical target: `SKILL.md`
Status: discarded
Promotion: manual-only

## Target Behavior

When a closure-time discovery is outside the completed ticket's scope and the
user authorizes durable tracking, the agent should open or cite the smallest
bounded follow-up owner and then close the completed original child/parent work
if its own acceptance criteria, evidence, review, statuses, dependencies, and
retrospective obligations are coherent.

The promoted follow-up-owner rule should not overblock closure merely because
the newly owned follow-up remains unresolved.

## Proposed Instruction Overlay

Add near ticket closure follow-up ownership:

```text
When the user authorizes durable tracking for an out-of-scope closure-time
follow-up, satisfy the follow-up-owner requirement by opening or citing the
smallest bounded owner for that follow-up. Do not keep the completed original
ticket open solely because that separate follow-up is unresolved.

Before closing, explicitly separate:

- closed scope: the original ticket or parent/child set whose own acceptance
  criteria, evidence, review, statuses, dependencies, specifications, and
  retrospective obligations are coherent;
- follow-up owner: the existing or newly opened record that owns the
  out-of-scope risk, debt, or downstream requirement.

If either side is missing, closure remains blocked. If both sides are present,
close the completed original scope and cite the follow-up owner.
```

## Expected Score Movement

- S006 Closure Coherence should improve when current overblocks completed work
  after opening a valid follow-up owner.
- S008 Retrospective Capture should hold by preserving the out-of-scope
  discovery in a bounded follow-up ticket.
- S005 Minimalism should hold because the follow-up must be the smallest
  independent owner, not a broad catch-all.

## Scenario Coverage

Primary scenario:

- SCN-009 closure with complete visible rows CSV export evidence and pass review,
  plus a discovered out-of-scope legacy nightly export quote/newline coverage
  gap. The user authorizes opening or updating the smallest durable follow-up
  owner before closure.

Secondary scenarios:

- SCN-008 review residual-risk handling.
- SCN-012 retrospective extraction when follow-up capture is the remaining
  closure obligation.

## Expected Failure Modes

- Overblocking closure after opening the follow-up ticket.
- Closing the original tickets without any follow-up owner.
- Expanding the visible rows CSV ticket to own legacy nightly export coverage.
- Creating a vague generic follow-up instead of a bounded legacy export
  quote/newline coverage ticket.

## Promotion Boundary

Promote only if current overblocks closure or creates a weak owner while
candidate opens/cites a bounded owner, closes only the completed visible-rows
scope, and preserves separation between closed scope and unresolved follow-up.
Discard if current already performs the correct authorized-owner closure path.

## Result

Discarded 2026-06-24 after
`EXP-20260624-863-authorized-follow-up-owner-closure-scn009-live-micro`.
Automated S006 tied candidate and current at 85, and manual inspection confirmed
current already performed the desired authorized-owner closure path: it opened a
bounded nightly export follow-up owner, moved the visible-rows child and parent
to done, repaired references, and did not edit implementation files. The
candidate was safe but not materially better.

# Candidate: Terminal Record Hygiene Sweep

Candidate ID: `candidate-terminal-record-hygiene-sweep-v1`
Created: 2026-06-25
Canonical target: `SKILL.md`
Status: active

## Target Behavior

When closing a ticket, parent ticket, or parent/child ticket set, the agent
should perform a final terminal-record hygiene sweep. Every ticket that is or
will be `Status: done` or `Status: cancelled` must live under its terminal
directory, and live references to moved records must point at the terminal
paths.

## Motivation

Multiple skill-authoring conformance runs show the current skill can perform
the primary skill behavior while occasionally leaving an already-done child
ticket at a top-level active-ticket path:

- EXP-966: one current repetition left done parent/child tickets at top level.
- EXP-965: terminal movement passed when isolated.
- EXP-964: terminal movement slipped again under a richer wrap-up prompt; one
  current and one duplicate-current repetition closed the parent but left the
  already-done child ticket at top-level `.10x/tickets/`.

The existing `SKILL.md` says terminal states move and closure requires status,
dependency, parent, and cross-reference coherence. The gap appears to be
salience during multi-obligation closure, not missing ontology.

## Proposed Instruction Overlay

Add near `Verify Before Closing`, after the numbered closure checks:

```text
Before marking a ticket or parent/child ticket set closed, perform terminal
record hygiene. Every ticket in the closing set that is already `Status: done`
or `Status: cancelled`, or that you are about to mark terminal, must live under
the corresponding terminal directory (`tickets/done/` or `tickets/cancelled/`).
This includes child tickets that were done before the current parent-closure
turn began.

After any terminal move, repair live `Parent`, `Depends-On`, `Relates-To`, and
`Target` references to the moved path before declaring closure coherent. Do not
leave a done or cancelled ticket at a top-level active-ticket path merely
because the primary requested work was evidence, retrospective extraction,
skill authoring, or parent wrap-up.
```

## Expected Score Movement

- S006 should improve on rich closure scenarios with terminal child tickets.
- S002 should improve by reducing top-level terminal records and stale live
  references.
- S008 should hold because the overlay does not alter skill content or mirror
  behavior.

## Scenario Coverage

Primary scenario:

- SCN-012 skill multi-harness exposure, where current passed source/mirror
  behavior but sometimes left a done child ticket at a top-level path.

Required regression controls before promotion if promising:

- Isolated terminal ticket path maintenance.
- Positive closure coherence.
- Record rename/reference repair.
- No-native skill source path or multi-harness exposure, to prove skill behavior
  remains intact.

## Expected Failure Modes

- Candidate may over-repair historical mentions that should remain as history.
- Candidate may spend too much effort on terminal movement and underperform the
  primary skill/mirror task.
- Candidate may treat all stale text mentions as live references and rewrite
  evidence logs unnecessarily.
- Candidate may still skip terminal movement when closure contains many
  obligations.

## Promotion Boundary

Promote only if candidate improves terminal movement/reference hygiene on the
rich skill-authoring closure scenario without weakening primary skill source,
mirror, self-containment, follow-up ownership, or implementation-edit
boundaries. Discard as null if current already passes the rerun and candidate
does not add measurable reliability.

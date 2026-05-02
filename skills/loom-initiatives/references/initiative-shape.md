# Initiative Shape

A good initiative stays strategic.

## Core sections

- Objective
- Why Now
- In Scope
- Out Of Scope
- Delegated Authority / Autonomy Boundaries, when delegated drive or autonomous
  objective work is in scope
- Objective-Level Stop Conditions, when delegated drive or autonomous objective
  work is in scope
- Success Metrics
- Milestones
- Dependencies
- Risks
- Linked Work
- Status Summary
- Completion Basis when `status: completed`

## Objective Criteria

Initiatives own strategic objective criteria. Put stable `OBJ-*` IDs under
Success Metrics when downstream work needs to cite which initiative outcome it
advances or verifies.

Use this shape:

```md
# Success Metrics

- OBJ-001: The durable outcome is recognizable from current owner records.
- OBJ-002: Downstream tickets can show scoped coverage of the initiative objective.
```

Cross-record references should use `initiative:<slug>#OBJ-001`. Tickets may list
those references in their coverage or claim matrix, but tickets own only scoped
execution coverage, evidence disposition, critique disposition, and closure.
Changing the objective criterion itself belongs back in the initiative.

## Delegated Authority And Stop Conditions

Ordinary initiatives do not need autonomy fields merely because they are
initiatives. For non-drive initiatives, `# Delegated Authority / Autonomy
Boundaries` and `# Objective-Level Stop Conditions` are optional and may be
omitted or marked not applicable.

When an initiative anchors delegated drive or autonomous objective work, those
sections are required because the initiative owns the objective-level authority
contract. They should make these facts inspectable for a fresh agent:

- what the agent may decide without asking
- what must return to the user as a human-decision trigger
- budget, time, risk, privacy, safety, or other autonomy limits
- objective-level conditions that require stopping, asking the user, or returning
  to shaping before continuation

These sections do not create a new authority record type, do not grant autonomy
that the user or governing records did not delegate, and do not make the
initiative own live ticket execution state. Tickets still own execution status,
blockers, scoped coverage, evidence disposition, critique disposition, and
closure decisions.

## Anti-patterns

Avoid:

- a giant unordered ticket list
- pure implementation detail
- vague aspiration with no success test
- turning the initiative into a plan or a ticket
- using ticket-local acceptance criteria as a substitute for initiative-owned
  `OBJ-*` success metrics
- treating optional autonomy prompts as required boilerplate for every initiative
- using initiative stop conditions as ticket blockers, progress logs, or closure
  decisions

## Linking

Link down into:

- research that justified the initiative
- specs that define parts of it
- plans that sequence it
- tickets that execute it

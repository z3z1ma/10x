# Initiative Shape

A good initiative stays strategic.

## Core sections

- Objective
- Why Now
- In Scope
- Out Of Scope
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

## Anti-patterns

Avoid:

- a giant unordered ticket list
- pure implementation detail
- vague aspiration with no success test
- turning the initiative into a plan or a ticket
- using ticket-local acceptance criteria as a substitute for initiative-owned
  `OBJ-*` success metrics

## Linking

Link down into:

- research that justified the initiative
- specs that define parts of it
- plans that sequence it
- tickets that execute it

# Initiative Examples

## Example Initiative Record

Use one initiative record when several specs, plans, and tickets belong to one larger strategic outcome.

## What To Notice In A Strong Initiative

- the objective is strategic, not just a task bundle
- why-now framing explains the urgency or timing
- success metrics make later acceptance more concrete
- milestones show shape without becoming a progress diary
- linked work makes the downstream execution graph explicit

## Worked Example

```text
Objective
Establish a reusable packet-driven review and execution workflow across the repository.

Why Now
Multiple subsystem skills now depend on a shared understanding of packet launch, fresh-context work, verification capture, and reconciliation. Without one strategic owner, the work will fragment across local fixes.

In Scope
- packet structure and operator-facing guidance
- skill playbooks for packet-consuming flows
- shared helper behavior that mechanizes already-published rules

Out of Scope
- unrelated runtime product features
- speculative automation outside the current Loom artifact model

Success Metrics
- another agent can choose the correct packet-consuming skill without guessing
- packet examples show scope, freshness, lineage, and output contracts clearly
- fresh child work produces durable evidence and reconciles cleanly into ticket truth

Milestones
- packet doctrine clarified
- skill references rewritten into operational manuals
- helper and naming surfaces aligned with the published workflow

Dependencies
- governing constitutional direction remains stable
- linked specs and plans stay synchronized with the initiative framing

Linked Work
- one spec for packet governance
- one plan for rollout order
- several tickets for implementation, critique, and docs follow-through
```

Why this is strong:

- it shows why the initiative deserves a durable strategic container
- success is concrete enough for downstream planning
- scope boundaries prevent the initiative from becoming a vague umbrella

## Weak Example

```text
Objective
Improve Loom a lot.
```

Why this is weak:

- there is no measurable outcome
- no timing or urgency is visible
- downstream work cannot inherit anything concrete

---
name: loom-specs
description: "Define intended behavior and acceptance contracts. Use when requirements, scenarios, constraints, or acceptance criteria are fuzzy or reusable."
compatibility: Markdown-native, script-free Loom protocol.
metadata:
  skill_kind: owner-layer
  owns_layer: spec
---

# loom-specs

Specs own intended behavior.

They turn ambiguity into a durable contract.

## What This Skill Owns

- behavior contracts
- requirements
- scenarios
- acceptance criteria
- explicit constraints that shape implementation

## Acceptance Boundary

Specs own acceptance IDs, intended behavior, scenarios, and requirements.

Tickets decide which acceptance IDs are in scope for live work and whether the
evidence/critique dossier is sufficient for closure. Packets, evidence,
critique, and wiki pages may cite spec acceptance IDs; they must not redefine
them.

## Use This Skill When

- several implementations are plausible and the intended behavior matters
- acceptance criteria are vague
- a ticket or critique would otherwise keep redefining what "correct" means
- a workflow or capability needs one stable behavioral source

## Do Not Use This Skill When

- you are still only gathering evidence
- you only need execution sequencing
- you are writing a user-facing explanation page

## Good Spec Questions

A strong spec answers:

- what problem is being solved
- what desired behavior is expected
- what constraints matter
- what scenarios matter
- how acceptance should be judged

## Done Means

- the behavior is explicit enough that implementation and critique can reference one contract
- the spec is precise without becoming implementation trivia

## Read In This Order

Read immediately for normal spec creation or review:

1. `references/spec-shape.md` when deciding what belongs in requirements,
   scenarios, constraints, and acceptance.
2. `templates/spec.md` only when creating or substantially reshaping a spec
   record.

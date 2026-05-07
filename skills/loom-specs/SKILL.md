---
name: loom-specs
description: "Define intended behavior and acceptance contracts. Use when building features, changing UX/API/domain behavior, requirements are fuzzy, acceptance is unclear, or future tickets need a reusable contract."
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
- who or what exact user, operator, API, system, or maintenance surface benefits
- what current workaround, pain, baseline behavior, or evidence shows the problem
- what desired behavior is expected
- what the smallest valuable shape is, especially when the request arrived as a
  preferred solution
- what quality bar would make the result materially better
- what examples and non-examples make fuzzy requirements concrete
- what constraints matter
- what scenarios matter
- how acceptance should be judged
- what evidence would prove the behavior and quality bar
- what assumptions or decision points would materially change the contract

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "The requirement is obvious." | Obvious requirements still hide assumptions. Specs exist to surface them before code. |
| "The quality bar is subjective, so skip it." | Subjective does not mean unverifiable. Name observable probes, examples, non-examples, or before/after evidence. |
| "The ticket can define this later." | Tickets scope live work. Reusable intended behavior belongs in a spec before downstream work relies on it. |

## Red Flags

- acceptance says "works" or "looks good" without observable criteria
- the spec inherits a requested solution shape without checking the underlying
  problem, beneficiary, workaround, or smallest valuable form
- UX/product claims lack examples, non-examples, or evidence plan
- open questions would materially change implementation but are not marked blocking
- a ticket or critique keeps redefining correctness because the spec is too vague

## Verification

- [ ] Requirements and acceptance IDs are stable and citable.
- [ ] The quality bar names a baseline/current-state delta.
- [ ] Examples or non-examples make ambiguous behavior concrete, or absence is justified.
- [ ] Decision points say whether they block implementation.
- [ ] Evidence plan can prove the behavior and quality bar.

## Done Means

- the behavior is explicit enough that implementation and critique can reference one contract
- the spec is precise without becoming implementation trivia

## Read In This Order

Read immediately for normal spec creation or review:

1. `references/spec-shape.md` when deciding what belongs in requirements,
   scenarios, constraints, and acceptance.
2. `templates/spec.md` only when creating or substantially reshaping a spec
   record.

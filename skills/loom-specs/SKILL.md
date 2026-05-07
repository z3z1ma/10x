---
name: loom-specs
description: "Define intended behavior and acceptance contracts. Use when building features, changing UX/API/domain behavior, requirements are fuzzy, a request needs grilling into a contract, acceptance is unclear, or future tickets need reusable behavior truth."
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
- explicit constraints that shape downstream delivery
- spec grilling that turns fuzzy language, domain boundaries, and operator answers
  into intended behavior

## Acceptance Boundary

Specs own acceptance IDs, intended behavior, scenarios, and requirements.

Tickets decide which acceptance IDs are in scope for live work and whether the
evidence/critique dossier is sufficient for closure. Packets, evidence,
critique, and wiki pages may cite spec acceptance IDs; they must not redefine
them.

## Use This Skill When

- several solutions are plausible and the intended behavior matters
- acceptance criteria are vague
- a request, plan, domain term, or workflow idea needs grilling before tickets or
  packets depend on it
- a ticket or critique would otherwise keep redefining what "correct" means
- a workflow or capability needs one stable behavioral source

## Do Not Use This Skill When

- you are still only gathering evidence
- you only need execution sequencing
- you only need to decompose already-clear high-level work into ticket-ready units
- you are writing a user-facing explanation page

## Spec Creation Discipline

Creating a spec is an active grilling pass, not a form fill.

When the request is fuzzy enough that an answer could change behavior, UX, API,
workflow, acceptance, or risk:

- interview the operator relentlessly about every material branch of the behavior
  contract until the intended behavior, terms, boundaries, scenarios, and
  acceptance criteria are shared and precise
- ask one material question at a time, waiting for the answer before moving to the
  next dependent branch
- provide a recommended answer for each question, including the behavior, user,
  product, risk, or owner-record reason that makes the recommendation coherent
- challenge vague, overloaded, or conflicting terms immediately and propose a
  precise canonical term or concept
- invent concrete scenarios and edge cases that force boundaries between concepts,
  roles, states, errors, permissions, invariants, and non-goals
- keep walking the design tree until dependent decisions are resolved, routed, or
  explicitly blocking
- capture durable decisions in the right owner: spec for behavior, ticket for local
  assumptions, research for tradeoffs/null results, wiki for accepted explanation,
  and constitution decisions only when the choice is hard to reverse, surprising,
  and tradeoff-backed

## Good Spec Questions

A strong spec answers:

- what problem is being solved
- who or what exact user, operator, API, system, or maintenance surface benefits
- what current workaround, pain, baseline behavior, or evidence shows the problem
- what desired behavior is expected
- what the smallest valuable shape is, especially when the request arrived as a
  preferred solution
- which domain, product, owner-record, or accepted-language facts shaped the contract
- which material decisions were resolved, routed, or left blocking
- what terminology conflicts or concrete scenarios shaped the contract
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
| "The requirement is obvious." | Obvious requirements still hide assumptions. Specs exist to surface them before delivery. |
| "The quality bar is subjective, so skip it." | Subjective does not mean unverifiable. Name observable probes, examples, non-examples, or before/after evidence. |
| "The ticket can define this later." | Tickets scope live work. Reusable intended behavior belongs in a spec before downstream work relies on it. |

## Red Flags

- acceptance says "works" or "looks good" without observable criteria
- the spec inherits a requested solution shape without checking the underlying
  problem, beneficiary, workaround, or smallest valuable form
- UX/product claims lack examples, non-examples, or evidence plan
- open questions would materially change downstream work but are not marked blocking
- a ticket or critique keeps redefining correctness because the spec is too vague

## Verification

- [ ] Requirements and acceptance IDs are stable and citable.
- [ ] Any material spec grilling questions were answered, routed, or explicitly
      marked blocking before downstream work depends on the contract.
- [ ] The quality bar names a baseline/current-state delta.
- [ ] Examples or non-examples make ambiguous behavior concrete, or absence is justified.
- [ ] Decision points say whether they block downstream work.
- [ ] Evidence plan can prove the behavior and quality bar.

## Done Means

- the behavior is explicit enough that tickets and critique can reference one contract
- the spec is precise without becoming delivery trivia

## Read In This Order

Read immediately for normal spec creation or review:

1. `references/spec-shape.md` when deciding what belongs in requirements,
   scenarios, constraints, and acceptance.
2. `templates/spec.md` only when creating or substantially reshaping a spec
   record.

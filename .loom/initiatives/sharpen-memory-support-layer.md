---
id: initiative:sharpen-memory-support-layer
kind: initiative
status: active
created_at: 2026-04-30T08:22:13Z
updated_at: 2026-04-30T08:31:09Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  spec:
    - spec:memory-support-layer-contract
  ticket:
    - ticket:329erym3
  evidence:
    - evidence:memory-support-layer-validation
  critique:
    - critique:memory-support-layer-review
---

# Objective

Make Loom memory concrete enough that agents can use it deliberately as a
support layer instead of treating it as vague optional scratch space or a shadow
truth system.

# Why Now

The canonical layers are now sharply defined, while `loom-memory` still mostly
says "optional support context". That is directionally right but operationally
thin: it explains what memory must not become without clearly explaining why it
is useful, what it is for, or when to promote a memory item into another layer.

# In Scope

- Define memory's positive role as support recall, retrieval cues, preferences,
  entities, reminders, and decaying hot context.
- Preserve optionality as a correctness boundary, not as a claim that memory is
  unimportant.
- Distinguish memory from tickets, wiki, research, evidence, specs, plans,
  initiatives, constitution, and packets.
- Tighten retrieval and housekeeping guidance so memory stays small, linked, and
  safe to promote or prune.
- Align the product surfaces that summarize memory's layer role.

# Out Of Scope

- Do not make memory a canonical truth owner.
- Do not add scripts, background indexing, embeddings, databases, or a required
  memory runtime.
- Do not create a second live task ledger in memory action items.
- Do not rewrite every historical dogfood memory file.

# Success Metrics

- OBJ-001: A fresh operator can read the memory skill and decide whether a fact
  belongs in memory, another Loom layer, or nowhere durable.
- OBJ-002: The product explains memory's usefulness positively, not only through
  prohibitions.
- OBJ-003: The product keeps memory optional in the correctness sense: stale or
  absent memory cannot make canonical project truth false.
- OBJ-004: Memory retrieval and housekeeping guidance gives concrete actions for
  scanning, pruning, linking, and promoting memory items.

# Milestones

- First tranche: sharpen the memory skill, references, and summary surfaces.
- Later tranche, if needed: add golden examples for memory promotion and pruning
  once this contract has been reviewed in real use.

# Dependencies

- `constitution:main` keeps Loom's no-hidden-runtime and owner-layer authority
  boundaries in force.
- `spec:memory-support-layer-contract` defines the behavior this initiative
  expects the product surface to teach.

# Risks

- Memory guidance could accidentally imply that memory owns project truth.
- Sharpening optional memory could make it sound required for correctness.
- Action-item guidance could encourage a second execution ledger.
- Over-specific file taxonomy could create ceremony rather than useful recall.

# Linked Work

- Spec: `spec:memory-support-layer-contract`
- Ticket: `ticket:329erym3`

# Status Summary

Drive Continuity Snapshot:

drive anchor: `initiative:sharpen-memory-support-layer`
objective criteria: OBJ-001 supported, OBJ-002 supported, OBJ-003 supported, OBJ-004 supported
current tranche: first tranche, `ticket:329erym3`
active tickets: `ticket:329erym3` complete_pending_acceptance
evidence state: `evidence:memory-support-layer-validation` recorded for the first tranche
critique state: `critique:memory-support-layer-review` final, one medium finding resolved
next action: acceptance
next action owner: `ticket:329erym3`
reason: evidence and critique support the first tranche; only ticket acceptance remains before closing the bounded work.

# Completion Basis

When `status: completed`, cite the ticket, structural evidence, critique
disposition, and any follow-up decision about examples or wiki promotion.

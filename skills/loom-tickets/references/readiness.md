# Ticket Readiness

A ticket is ready when a fresh agent can continue the bounded work from the
ticket dossier and linked owner records without chat history.

Readiness is not a serialized routing decision. The agent should infer whether to
edit locally, compile a packet, gather evidence, run critique, update a spec or
plan, ask the user, or evaluate acceptance from the ticket's state, blockers,
scope, acceptance criteria, evidence, critique disposition, linked owner records,
and journal.

Ralph-ready is stricter: the ticket must also make one bounded implementation
iteration, write boundary, likely verification posture, and expected output
contract legible enough for a fresh worker.

New tickets should normally start as `proposed`. Promote to `ready` only after
this checklist passes.

## Checklist

- the problem is clearly named
- why now is clearly named
- scope and non-goals are separated
- `change_class` and `risk_class` are set in frontmatter for new tickets and for
  tickets being materially updated for readiness, Ralph, critique, acceptance,
  reopening, or closure; normalize legacy tickets when touched or before
  governed execution or acceptance, without treating their prior absence as
  instant non-conformance
- acceptance criteria are concrete enough to guide behavior
- coverage names relevant spec acceptance IDs when the work implements or
  verifies a spec
- when no spec owns the acceptance contract, ticket-local acceptance criteria use
  stable `ACC-*` IDs in the ticket and downstream records cite them as
  `ticket:<token>#ACC-001`
- ticket-local `ACC-*` criteria are not used to redefine or replace a reusable
  spec-owned acceptance contract
- relevant upstream artifacts are linked
- the likely evidence path is visible
- critique risk class matches frontmatter `risk_class`; required profiles are
  explicit when review is expected
- the current blockers, evidence gaps, critique gaps, acceptance gaps, and journal
  are explicit enough for a fresh agent to choose the next skill or action by
  reasoning over the records
- the ticket is small enough to fit one bounded iteration or a short sequence of
  clearly staged iterations

If several of those are missing, do not force Ralph, critique, wiki, or closure.
Refine the ticket first.

## Continuation Without Serialized Routes

Do not add `next route`, `Route`, route-readiness, or token-list sections to
tickets. They create a second scheduling surface and make the ticket look like a
workflow router.

Instead, keep the ticket facts sharp:

- `status` says the live execution state.
- `# Blockers` names real blockers or `None`.
- `# Evidence`, `# Critique Disposition`, `# Retrospective / Promotion
  Disposition`, and `# Acceptance Decision` say what gates are satisfied or open.
- `# Journal` records material progress, decisions, and why work stopped or
  resumed.
- Linked specs, plans, research, evidence, critique, packets, and wiki pages
  provide the context an agent needs to choose the next skill.

The agent's reasoning is part of Loom's operating model. Skills guide that
reasoning; tickets should provide enough data for it, not serialize the workflow
choice.

### `local_edit` And Ticket Truth

`local_edit` is a lightweight phrase for a tiny in-context mutation, not a bypass
around tickets and not a workflow field. If a ticket owns the work, the ticket still
owns live execution state, scope, acceptance disposition, evidence disposition,
critique disposition, and the journal after the edit.

A local-edit-ready ticket should make the write boundary narrow enough that the
operator can stop without guessing. If the change needs a fresh worker, a wider
implementation pass, unclear behavior decisions, investigation, or adversarial
review, choose Ralph, spec, research, critique, or the appropriate owner skill
instead.

Evidence expectations should match the claim being made: structural Markdown
cleanup may need only diff review or targeted text observations, while behavior,
validation, completion, protocol-authority, or risky claims need observed
evidence and possibly critique before acceptance.

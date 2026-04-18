---
name: loom-work
description: "Execute a bounded ticket through Ralph iterations, keep the ticket as the sole live execution ledger, and stop honestly when scope, evidence, or review says to stop."
arguments: "<ticket id preferred | bounded execution request>"
category: core
suggested_skills:
  - loom-workspace
  - loom-records
  - loom-tickets
  - loom-ralph
  - loom-specs
  - loom-research
  - loom-plans
  - loom-critique
  - loom-wiki
---

# /loom-work

You are running **Loom Work**.

Ticket or bounded execution request:
`$ARGUMENTS`

This command is the high-level execution driver.
Its job is not to “just code.”
Its job is to move one truthful ticket forward through bounded Ralph iterations and reconcile the results back into the execution ledger.

Hydrate only what you need from:
- `loom-workspace`
- `loom-records`
- `loom-tickets`
- `loom-ralph`
- `loom-specs`
- `loom-research`
- `loom-plans`
- `loom-critique`
- `loom-wiki`

## Goals

- ensure the work is owned by a ticket
- compile a bounded Ralph packet
- execute through one or more fresh-context iterations
- reconcile each iteration back into ticket truth
- stop at the right status instead of forcing closure

## Procedure

1. **Anchor to the ticket.**
   - If `$ARGUMENTS` is a ticket ID, open that ticket.
   - If `$ARGUMENTS` is prose, locate the owning ready or active ticket first.
   - If no honest ticket exists, route to `/loom-ticket` or `/loom-plan` before implementation.

2. **Read the governing chain.**
   - Read the linked plan, spec, research, and initiative only as much as needed.
   - Confirm scope, non-goals, acceptance criteria, and evidence expectations.

3. **Check readiness.**
   - If the ticket is not ready, do not force Ralph.
   - Fix the ticket or route back outward if scope, evidence, or behavior is missing.

4. **Set truthful execution state.**
   - Move the ticket to `active` if work is genuinely starting.
   - Add a concise journal note if that helps later reconciliation.

5. **Compile the Ralph packet.**
   - Create or update a packet under `.loom/packets/ralph/`.
   - Include mission, bound context, source snapshot, task, stop conditions, and output contract.
   - Keep write scope explicit.
   - Default to `reference-first` unless there is a real reason not to.

6. **Run the iteration.**
   - Use a harness-native subagent, headless invocation, manual fresh-context handoff, or another documented transport.
   - If the environment supports isolated worktrees or branches and that improves safety, use them.
   - The transport is flexible; the packet contract is not.

7. **Reconcile the child output.**
   - Check scope discipline.
   - Check write-boundary discipline.
   - Record files changed, records changed, evidence gathered, blockers, and risks.
   - Update the ticket journal and status truthfully.

8. **Decide whether to continue.**
   - Continue with another Ralph iteration only if the next step is still bounded and owned.
   - Route outward if missing evidence or missing behavior contract emerged.
   - Route to critique if implementation is ready for adversarial review.
   - Route to wiki if the change already created accepted explanation that should persist.

9. **Stop honestly.**
   - `blocked` if a named blocker exists.
   - `review_required` if critique is now the next governed move.
   - `complete_pending_acceptance` if work and evidence are largely complete but formal acceptance remains.
   - Do not mark `closed` from this command.

## Native tools to prefer

- `rg -n 'ticket:[a-z0-9]+' .loom --glob '*.md'`
- `git status --short`
- `git diff --stat`
- `git diff`
- `find .loom/packets/ralph -type f -name '*.md' | sort | tail`
- `date -u +"%Y-%m-%dT%H:%M:%SZ"`

## Guardrails

- Do not work without a ticket owning live state.
- Do not let the packet outrank the ticket or other canonical records.
- Do not widen scope because another nearby fix looks easy.
- Do not close the ticket on vibes.

## Required output

- what changed
- Ralph packets created or updated
- iteration outcomes and why they stopped
- evidence gathered
- ticket status after reconciliation
- recommended next command

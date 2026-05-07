# Routing

Use these questions to decide the next owner layer or workflow coordinator. When
the user speaks in ordinary coding-task language rather than Loom owner-layer
language, use `task-routing-catalog.md` after this reference.

Do not save `next route`, `Route`, or workflow-choice fields as a substitute for
reasoning. The owner graph should contain enough facts for the agent to choose the
right skill. If it does not, repair the owner record that lacks the needed truth.

## Which Layer Owns The Next Truth Change?

- project identity, principles, constraints -> `loom-constitution`
- strategic outcome framing -> `loom-initiatives`
- evidence synthesis, investigation, option comparison, rejected path, or null
  result -> `loom-research`
- intended behavior or acceptance contract -> `loom-specs`
- complex-change planning, decomposition, sequencing, or rollout strategy -> `loom-plans`
- live execution status, bounded work, acceptance disposition, closure readiness,
  or residual-risk evaluation -> `loom-tickets`
- observed artifacts, validation output, screenshots, logs, reproduction,
  red/green results, or scan artifacts -> `loom-evidence`
- adversarial review -> `loom-critique`
- persistent explanation / interlinked knowledge -> `loom-wiki`

## Which Workflow Or Support Coordinator Helps?

- high-level objective continuation through owner records, ticket tranches,
  Ralph/local execution, evidence, critique, wiki, and reassessment ->
  `loom-drive`
- support-only recall, preferences, retrieval cues, entities, reminders, or hot
  context -> `loom-memory` support coordinator, not project truth
- shared grammar, naming, linking, status, validation conventions, or graph repair
  -> `loom-records`
- tiny or single bounded in-context mutation with a narrow known write boundary ->
  local execution under the owning ticket or owner record; do not create a
  workflow field for it
- one bounded fresh-context implementation step -> `loom-ralph`, after the ticket
  is Ralph-ready enough to compile a packet
- implementation isolation, branch/worktree hygiene, or Git provenance ->
  `loom-git` support coordinator
- debugging or incident flow -> `loom-debugging`
- bounded experiment, prototype, or sketch -> `loom-spike`
- codebase/module atlas work -> `loom-codemap`
- merge, release, PR, or handoff packaging from already-truthful owner records ->
  `loom-ship`
- accepted learning assimilation before closure -> `loom-retrospective`

## The Constitution First Rule

If the workspace has Loom, read `constitution:main` before making important downstream decisions.

## Quick Sanity Heuristic

If you are about to ask "where should this live?", you are still in workspace/routing territory.

If you are about to ask "what exactly should this record say?", move to the
owning skill.

Do not invoke skills by a vague "maybe relevant" sweep. Pick the owner layer for
the next truth change, then load the skill or workflow coordinator that can move
that truth honestly.

Workflow skills coordinate work through owner layers. They do not create new truth
layers or outrank the owner records they update.

`loom-ship` packages PR summaries, release notes, handoff packages,
evidence/risk summaries, and follow-up lists. It mirrors already-truthful Loom
records for external surfaces; it does not replace ticket-owned acceptance or
create a release ledger.

Commands are optional invocation adapters. They are not owner layers, workflow
truth owners, or route ledgers.

## Local Execution Boundary

Use local execution only when the next mutation is cheap, bounded, and safe to
make in the current context: for example, a small wording fix, link repair,
record hygiene edit, clearly scoped Markdown guidance adjustment, or tiny code,
test, docs, config, refactor, migration, or cleanup change. Know the exact write
boundary before editing, but do not serialize it as a workflow token.

Local execution does not bypass ticket truth. When a ticket owns the work, the ticket
remains the live execution ledger for state, scope, acceptance, evidence
disposition, critique disposition, and journal reconciliation.

Escalate away from local execution when the change is implementation-sized, needs
a fresh-context handoff, has ambiguous intended behavior, depends on missing
evidence, changes meaningful protocol authority, or needs adversarial review.
Choose the owner skill according to the truth that must change next. Use
`skills/loom-tickets/references/local-execution.md` when a ticket owns the local
execution loop.

Evidence is required when local execution supports a completion, behavior,
validation, or protocol-authority claim. For purely structural cleanup, a diff
review or targeted text observation may be enough; for behavior or risky changes,
create evidence and/or critique instead of treating the edit itself as proof.

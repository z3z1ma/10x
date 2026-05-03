# Routing

Use these questions to decide the next owner layer or workflow coordinator.

When recording a route field such as `next route:` or `Route:`, use the shared
route-token grammar in `skills/loom-records/references/route-vocabulary.md`.
That reference is the canonical saved-field token source; this page maps those
tokens to owner layers or workflow/support coordinators.

## Which layer owns the next truth change?

- project identity, principles, constraints -> route token `constitution`, owner
  `loom-constitution`
- strategic outcome framing -> route token `initiative`, owner
  `loom-initiatives`
- evidence synthesis, investigation, option comparison, rejected path, or null
  result -> route token `research`, owner `loom-research`
- intended behavior or acceptance contract -> route token `spec`, owner
  `loom-specs`
- sequencing or rollout strategy -> route token `plan`, owner `loom-plans`
- live execution status, next bounded work item, acceptance disposition, closure
  readiness, or residual-risk evaluation -> route token `ticket`, owner
  `loom-tickets`
- observed artifacts, validation output, screenshots, logs, reproduction, red/green
  results, or scan artifacts -> route token `evidence`, owner `loom-evidence`
- adversarial review -> route token `critique`, owner `loom-critique`
- persistent explanation / interlinked knowledge -> route token `wiki`, owner
  `loom-wiki`

## Which workflow or support coordinator should drive the route?

- high-level objective continuation through owner records, ticket tranches,
  Ralph/local execution, evidence, critique, wiki, and reassessment ->
  coordinator `loom-drive`; record the saved route token for the owner truth or
  workflow that changes next
- support-only recall, preferences, retrieval cues, entities, reminders, or hot
  context -> support coordinator `loom-memory`; not a project-truth route token
- shared grammar, naming, linking, status, or validation conventions ->
  coordinator `loom-records`; use route token `records_repair` only for broken,
  stale, or contradictory graph repair
- tiny, safe, in-context mutation with a narrow known write boundary -> route
  token `local_edit`; if a ticket owns the work, `loom-tickets` still owns live
  state and acceptance reconciliation
- one bounded fresh-context implementation step -> route token `ralph`,
  coordinator `loom-ralph`, after the ticket is Ralph-ready
- implementation isolation, branch/worktree hygiene, or Git provenance -> support
  coordinator `loom-git`; do not record `next route: git` or `next route:
  loom-git`. The saved route remains the owner/workflow token being served, such
  as `ticket`, `ralph`, `local_edit`, `ship`, or `records_repair`.
- debugging or incident flow -> route token `debugging`, coordinator
  `loom-debugging`
- bounded experiment, prototype, or sketch -> route token `spike`, coordinator
  `loom-spike`
- codebase/module atlas work -> route token `codemap`, coordinator
  `loom-codemap`
- merge, release, PR, or handoff packaging from already-truthful owner records ->
  route token `ship`, coordinator `loom-ship`
- accepted learning assimilation before closure -> route token `retrospective`,
  coordinator `loom-retrospective`
- `acceptance_review`, closure disposition, or residual-risk evaluation ->
  route token `acceptance_review`, owner `loom-tickets`
- graph repair, broken links, naming, or drift -> route token `records_repair`,
  coordinator `loom-records`
- wiki write or audit mechanics -> route token `wiki`, owner/coordinator
  `loom-wiki`

## The Constitution First Rule

If the workspace has Loom, read `constitution:main` before making important downstream decisions.

## Quick Sanity Heuristic

If you are about to ask "where should this live?", you are still in workspace/routing territory.

If you are about to ask "what exactly should this record say?", move to the
owning skill.

Do not invoke skills by a vague "maybe relevant" sweep. Pick the owner layer for
the next truth change, then load the skill or workflow coordinator that can move
that truth honestly.

Workflow skills coordinate routes through owner layers. They do not create new
truth layers or outrank the owner records they update.

`loom-ship` packages PR summaries, release notes, handoff packages,
evidence/risk summaries, and follow-up lists. It mirrors already-truthful Loom
records for external surfaces; it does not replace ticket-owned
`acceptance_review` or create a release ledger.

Commands are optional invocation adapters for these routes. They are not owner
layers or workflow truth owners.

## `local_edit` Boundary

Use `local_edit` only when the next mutation is cheap, bounded, and safe to make
in the current context: for example, a small wording fix, link repair, record
hygiene edit, or clearly scoped Markdown guidance adjustment. Name the exact
write boundary before editing.

`local_edit` does not bypass ticket truth. When a ticket owns the work, the
ticket remains the live execution ledger for state, scope, acceptance, evidence
disposition, and the next route. The edit may be local; reconciliation still
belongs to the ticket owner.

Escalate away from `local_edit` when the change is implementation-sized, needs a
fresh-context handoff, has ambiguous intended behavior, depends on missing
evidence, changes meaningful protocol authority, or needs adversarial review.
Route those cases to `ralph`, `spec`, `research`, `critique`, or another owner
route according to the truth that must change next.

Evidence is required when the local edit supports a completion, behavior,
validation, or protocol-authority claim. For purely structural cleanup, a diff
review or targeted text observation may be enough; for behavior or risky changes,
route to `evidence` and/or `critique` instead of treating the edit itself as
proof.

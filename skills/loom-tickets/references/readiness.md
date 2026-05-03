# Ticket Readiness

A ticket is ready when the next governed route can proceed without chat history.

Readiness is route-neutral. A ready ticket might route to any canonical route
token in `skills/loom-records/references/route-vocabulary.md`, including
`ask_user`, `workspace_status`, `records_repair`, `constitution`, `initiative`,
`research`, `spec`, `plan`, `ticket`, `local_edit`, `ralph`, `debugging`,
`spike`, `codemap`, `evidence`, `critique`, `wiki`, `retrospective`,
`acceptance_review`, `ship`, `continue`, or `stop`.

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
- the next route is explicit in `# Next Move / Next Route` or equivalent prose,
  using the shared route vocabulary: `local_edit`, `ralph`, `debugging`,
  `spike`, `codemap`, `critique`, `wiki`, `retrospective`, `evidence`,
  `constitution`, `initiative`, `research`, `spec`, `plan`, `ticket`,
  `acceptance_review`, `ship`, `ask_user`, `workspace_status`,
  `records_repair`, `continue`, or `stop`
- the ticket is small enough to fit one bounded iteration or a short sequence of
  clearly staged iterations

If several of those are missing, do not force Ralph, critique, wiki, or closure.
Refine the ticket first.

## Route Readiness

Use `# Route Readiness` or equivalent prose to make the route named in `# Next
Move / Next Route` specific without implying that every handoff is Ralph. Do not
use it as a second route-token selector or duplicate the allowed-token list.

Use `skills/loom-records/references/route-vocabulary.md` for route-token grammar;
do not use ticket lifecycle statuses such as `ready`, `active`,
`review_required`, or `complete_pending_acceptance` as next-route values.

- For `ask_user`, name the decision needed, why the agent cannot infer it safely,
  and the owner record to update after the answer; do not use it for low-risk,
  reversible assumptions inside delegated authority.
- For `workspace_status`, name the workspace surface to inspect, the owner-chain
  or queue trust question to answer, and the narrower route the status pass should
  make selectable.
- For `records_repair`, name the broken, stale, or contradictory records or links,
  the graph consistency rule being restored, and dependent work that must wait.
- For `constitution`, name the principle, constraint, decision, roadmap, or
  identity truth to create/refine, why it belongs above initiative/plan/ticket,
  and downstream records to reconcile.
- For `initiative`, name the objective, metric, autonomy boundary, or strategic
  framing to create/refine, success criteria or `OBJ-*` IDs affected, and
  downstream records to reconcile.
- For `research`, name the question, evidence or option set to inspect, expected
  conclusion or null result, and downstream owner that will use the synthesis.
- For `spec`, name the fuzzy intended behavior, reusable acceptance or scenario
  to clarify, and tickets or plans that must inherit the clarified contract.
- For `plan`, name the sequencing, dependency, tranche, or rollout uncertainty to
  resolve and the tickets or owner records that must be updated afterward.
- For `ticket`, name the execution-owner change needed, such as create, refine,
  split, reopen, block, or reconcile, plus the owner-chain inputs it must preserve.
- For `local_edit`, name the bounded edit, write boundary, why it is cheap and
  safe in the current context, expected evidence or observation, and escalation
  trigger if the edit proves ambiguous, risky, behavior-defining, or too large.
- For `ralph`, keep the stricter Ralph-ready fields: bounded iteration, write
  boundary, likely verification posture, and expected output contract.
- For `debugging`, name the failing behavior, reproduction/evidence expectation,
  and root-cause or fix handoff boundary.
- For `spike`, name the question or option to test, throwaway write boundary, and
  expected research/evidence output.
- For `codemap`, name the repository or module area to map, expected
  evidence/research/wiki atlas output, and downstream route the map should
  unblock.
- For `critique`, name the review target, required profiles, and evidence to
  review.
- For `wiki`, name the accepted explanation or workflow to preserve, source owner
  records and statuses, evidence/critique basis, limits, and stale triggers.
- For `retrospective`, name the lesson or prevention artifact to evaluate,
  candidate owner layers, and closure impact if promotion is deferred.
- For `evidence`, name the claim references and observation procedure.
- For `acceptance_review`, name the evidence, critique disposition, closure
  readiness, and residual risks that the ticket-owned gate must evaluate.
- For `ship`, name the ticket/evidence/critique records to package and the
  external handoff surface, including PR-summary, release-note, evidence/risk,
  and follow-up-list needs when relevant, without treating shipping as closure.
- For `continue`, name the already-governed tranche or narrower route to proceed
  with, the owner record that authorizes it, and why no new scoping decision is
  needed. This is a route token for parent-owned execution flow, not a Ralph
  child outcome named `continue`.
- For `stop`, name `stop_kind`, `stop_reason`, `owner_record`,
  `resume_condition`, and `closure_claim`. `stop_kind: satisfied` may support
  closure only when ticket-owned acceptance, evidence, critique, and
  retrospective / promotion disposition are already closure-compatible. Other stop
  kinds pause, abandon, or block continuation; they do not imply closure. This is
  a route token for parent-owned execution flow, not a Ralph child outcome named
  `stop`.

### `local_edit` And Ticket Truth

`local_edit` is a lightweight route for a tiny in-context mutation, not a bypass
around tickets. If a ticket owns the work, the ticket still owns live execution
state, scope, acceptance disposition, evidence disposition, critique disposition,
and the next route after the edit.

A local-edit-ready ticket should make the write boundary narrow enough that the
operator can stop without guessing. If the change needs a fresh worker, a wider
implementation pass, unclear behavior decisions, investigation, or adversarial
review, route to `ralph`, `spec`, `research`, `critique`, or the appropriate
owner route instead.

Evidence expectations should match the claim being made: structural Markdown
cleanup may need only diff review or targeted text observations, while behavior,
validation, completion, protocol-authority, or risky claims need observed
evidence and possibly critique before acceptance.

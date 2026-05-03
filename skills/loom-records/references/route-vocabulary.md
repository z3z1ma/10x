# Route Vocabulary

This reference is the canonical shared grammar for Loom route tokens used in
checkpoint, resume, route-readiness, and handoff examples.

Route tokens are not a runtime enum, command router, or new owner layer. They are
grep-friendly Markdown vocabulary for naming the next governed move in existing
owner records.

For lifecycle words that are not route tokens, use
`skills/loom-records/references/status-lifecycle.md`. Ticket execution states
are owned by `skills/loom-tickets/references/state-machine.md`, and Ralph child
outcomes are owned by `skills/loom-ralph/references/packet-contract.md`.

## Token Grammar

Use lowercase `snake_case` tokens when a field or example asks for a route value,
especially after labels such as `next route:`, `Route:`, `proposed next route:`,
or route-priority tables.

Use ordinary prose when explaining a workflow. Do not rewrite every mention of a
skill name, command, or ticket status into a route token.

## Canonical Route Tokens

| Token | Meaning |
| --- | --- |
| `ask_user` | pause for a focused operator decision the agent cannot safely infer |
| `workspace_status` | inspect workspace structure, queues, and owner-chain trust before choosing a narrower route |
| `records_repair` | repair broken, stale, or contradictory Loom graph records before dependent work |
| `constitution` | create or update constitutional identity, principles, hard constraints, roadmap direction, or citable decisions |
| `initiative` | create or update strategic outcome framing, objectives, success metrics, or delegated autonomy boundaries |
| `research` | gather or synthesize evidence, options, tradeoffs, or null results |
| `spec` | clarify intended behavior, requirements, scenarios, or reusable acceptance |
| `plan` | clarify sequencing, dependency order, tranches, or rollout strategy |
| `ticket` | create or update the live execution owner for bounded work |
| `local_edit` | execute a tiny, safe, in-context mutation with a named write boundary and no fresh child packet |
| `ralph` | launch or reconcile one Ralph implementation packet for a bounded ticket slice |
| `debugging` | run a reproduce-first debugging or incident workflow before the next fix or prevention route is clear |
| `spike` | run a bounded spike, sketch, prototype, or experiment as a research-shaped workflow |
| `codemap` | map repository or module structure into evidence, research, and accepted wiki atlas knowledge |
| `evidence` | preserve observed artifacts, validation output, reproduction logs, or support/challenge links |
| `critique` | run adversarial review and record findings, verdicts, and risks |
| `wiki` | promote accepted explanation or reusable workflow knowledge |
| `retrospective` | assimilate accepted learning into the correct owner layers before closure |
| `acceptance_review` | evaluate ticket-owned acceptance, evidence/critique disposition, closure readiness, and residual risk without external handoff deciding closure |
| `ship` | package already-truthful work for merge, release, PR, or handoff summaries without owning closure |
| `continue` | route-token use only: proceed to the next already-governed tranche or route named by owner records; do not use this row to interpret a Ralph child outcome named `continue` |
| `stop` | route-token use only: stop because the objective is satisfied, blocked, unsafe, out of scope, over budget, awaiting external action, cancelled, or not worth graph cost; recorded stop routes must include controlled stop fields; do not use this row to interpret a Ralph child outcome named `stop` |

Workflow coordinator tokens exist only when the coordinator is itself the next
governed move. Use workflow route tokens such as `debugging`, `spike`, `codemap`,
`ship`, or `retrospective` when the next step is to run that first-class workflow,
such as drafting PR summaries, release notes, handoff packages, evidence/risk
summaries, follow-up lists, or promotion disposition from already-truthful owner
records. If the next truth change is already narrower, route through the owner
token instead: for example, use `research` for a known investigation write,
`evidence` for an observation record, `wiki` for an accepted atlas page, `ralph`
for a bounded implementation packet, `critique` for review, or
`acceptance_review` for ticket-owned closure and residual-risk evaluation.

## `stop` Readiness

For `next route: stop`, record:

```text
stop_kind: satisfied | blocked | unsafe | out_of_scope | over_budget | awaiting_external | no_recoverable_route | not_worth_graph_cost | cancelled_by_owner
stop_reason: <why work stops now>
owner_record: <record that makes the stop truthful>
resume_condition: <condition that could make work safe or useful again, or None>
closure_claim: yes | no
```

`stop_kind: satisfied` may support closure only when ticket-owned acceptance,
evidence, critique, and retrospective / promotion disposition are already
closure-compatible. Other stop kinds pause, abandon, or block continuation; they
do not imply closure.

## `local_edit` Boundaries

Use `local_edit` for a cheap, bounded edit that is safe to perform in the current
context: small wording cleanup, link repair, record hygiene, or a narrowly scoped
Markdown guidance change. The owner record or operator handoff should name the
write boundary and the observation or evidence expected from the edit.

`local_edit` is not a `loom-local-edit` skill, command wrapper, bypass mode, or
new owner layer. When a ticket owns the work, the ticket remains the live ledger
for execution state, acceptance, evidence disposition, critique disposition, and
the next route. Route tokens only name the next governed move; they do not move
truth out of the owner record.

Escalate from `local_edit` to the route that owns the missing truth when the work
becomes ambiguous, risky, behavior-defining, protocol-authority-changing, or too
large for a current-context edit. Use `ralph` for a bounded fresh-context
implementation slice, `spec` for intended behavior, `research` for missing
evidence or tradeoffs, `critique` for adversarial review, and `evidence` for
observations that must persist.

## Non-Routes

Keep these categories distinct from route tokens. Matching words can appear in
more than one category; the field and owner decide what the word means.

| Category | Examples | Boundary rule |
| --- | --- | --- |
| Route tokens | `constitution`, `initiative`, `research`, `ralph`, `critique`, `continue`, `stop` | Use only when a route field asks for the next governed move. Tokens remain Markdown vocabulary, not a runtime enum, schema, validator, command router, skill inventory, or owner layer. |
| Ticket lifecycle states | `proposed`, `ready`, `active`, `blocked`, `review_required`, `complete_pending_acceptance`, `closed`, `cancelled` | Describe live ticket execution state. They are not `next route:` values. |
| Record lifecycle statuses | `draft`, `active`, `accepted`, `recorded`, `superseded`, `abandoned` | Describe a record's lifecycle or support-surface state, not the next governed move. |
| Ralph child outcomes | `continue`, `stop`, `blocked`, `escalate` | A child outcome is not a route token by itself. It becomes routing truth only after the parent reconciles the child output and translates it into the next owner-truth route, such as `ticket`, `research`, `critique`, `ask_user`, `continue`, or `stop`. |
| Critique-owned finding states | `open`, `withdrawn` | Live inside critique records and describe whether the critique still stands behind a finding. They are not ticket states or route tokens. |
| Ticket-owned finding dispositions | `resolved`, `accepted_risk`, `superseded`, `converted_to_follow_up` | Live in the ticket's critique disposition section for qualified findings. They are not critique finding states and do not name the next route. |
| Support-memory surfaces | `memory`, `loom-memory`, retrieval cues, preferences, reminders, hot context | Memory is optional support recall, not canonical project truth. Do not use `memory` as a `next route:` token; route durable truth changes through the owner token that owns them. |
| Git support coordinator | `git`, `loom-git`, branch, worktree, baseline, diff provenance | Git coordination is support behavior, not a route token. Do not record `next route: git` or `next route: loom-git`; record the owner/workflow token being served, such as `ticket`, `ralph`, `local_edit`, `ship`, or `records_repair`. |
| Commands and adapters | slash commands, harness commands, MCPs, package-specific wrappers | Commands may transport or prompt a route, but owner records and workflow skills still own Loom truth. |
| Skill display names | Ralph, loom-drive, loom-critique | Use ordinary prose for skill names. In a route-value field, use the token (`ralph`, `debugging`, `spike`, `codemap`, `ship`, `continue`, `acceptance_review`, etc.) rather than title case, spaces, or hyphens. Do not add a token merely because a skill exists; route tokens name governed moves, not the skill inventory. |

When the same word appears in multiple rows, the field decides the vocabulary. A
Ralph packet `outcome: continue` is child output for parent reconciliation; a
recorded `next route: continue` is a parent-owned route decision.

## `ask_user` Readiness

Use `ask_user` only when the next safe move requires an operator decision the
agent cannot infer from owner records, delegated authority, or a low-risk
reversible assumption.

An `ask_user` route should record:

- decision needed: the exact focused question or choice;
- unsafe-inference reason: why proceeding would invent product direction, accept
  material risk, exceed authority, or otherwise rely on an unsafe assumption;
- owner record to update after answer: the constitution, initiative, research,
  spec, plan, ticket, or other owner record that will carry the durable result.

Do not use `ask_user` as an approval gate for every downstream step. If the
assumption is low risk, reversible, and inside delegated authority, record the
assumption in the owner record and continue through the appropriate route.

## Examples

```text
next route: ralph
next route owner: loom-ralph packet contract, then ticket reconciliation

next route: constitution
next route owner: loom-constitution

Route: acceptance_review
Route: ask_user
decision needed: Choose whether the accepted constraint should become a constitutional decision.
unsafe-inference reason: The agent cannot safely invent durable project authority.
owner record to update after answer: constitution:main or decision:<slug>

proposed next route: research

next route: stop
stop_kind: satisfied
stop_reason: OBJ-001 and OBJ-002 are satisfied, required evidence is linked, and no owner work remains.
owner_record: ticket:<token>
resume_condition: None - objective is satisfied
closure_claim: yes

next route: continue
continue reason: ticket:<token> already names the next governed tranche; this is not a Ralph child outcome.
```

If multiple routes are plausible, choose the token for the truth that changes
next, then cite the owner record or workflow coordinator that will handle it.

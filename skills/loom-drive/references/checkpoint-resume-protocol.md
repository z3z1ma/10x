# Checkpoint And Resume Protocol

This reference supports the `loom-drive` skill.

Each new session must be able to recover drive state from Loom records.
Checkpointing is therefore mandatory drive hygiene, not a saved workflow router.

## Anchor Rule

Every active drive has one anchor record:

- high-level objective -> initiative anchor
- plan-only continuation -> plan anchor until promoted to initiative or ticket
- single bounded execution -> ticket anchor; use `loom-tickets` or `loom-ralph`,
  not the full drive loop

For true high-level drives, prefer an initiative anchor. The anchor does not own
live execution state; it points to the current plan, active tickets, evidence,
critique, blockers, and open objective gaps.

## Required Checkpoint Facts

Record these facts in existing owner records before stopping, compacting, or
launching child work:

```text
drive anchor: <initiative id or narrower owner id>
objective criteria: <OBJ-IDs and satisfied | partially_satisfied | open | blocked | out_of_scope>
current tranche: <plan section / wave / ticket IDs>
active tickets: <ticket IDs and live states>
hard gates: <clear | blocked, with blocker links>
last child output: <packet/handoff/evidence/critique link if applicable>
pending operator question: <decision needed, unsafe-inference reason, and owner record to update after answer; or none>
open owner gaps: <claims, blockers, evidence gaps, critique gaps, acceptance gaps, or none>
resume note: <optional one-sentence note only when the records are not self-evident>
updated_at: <timestamp>
```

Put each fact in the owner record that owns it. The initiative can summarize the
drive anchor and objective status; tickets own active execution state, critique
disposition, evidence disposition, blockers, journal, and acceptance decisions;
plans own tranche sequencing; evidence and critique own observations, findings,
and verdicts.

Do not add saved workflow-choice fields. A fresh parent should infer the next action from
the owner records. If it cannot, the checkpoint is incomplete and the right move
is owner-record repair or a focused user question.

## Deterministic Resume Discovery

When entering a workspace to resume a drive:

1. Load `using-loom`, inspect workspace, and read `constitution:main`.
2. Search active execution surfaces:

```bash
rg -n 'status: (active|blocked|review_required|complete_pending_acceptance)' .loom/tickets
rg -n 'continuity snapshot|drive anchor:|resume note:|open owner gaps:' .loom/initiatives .loom/plans .loom/tickets
rg -n 'loom-drive|objective-driven|OBJ-[0-9]{3}' .loom
```

3. Read the anchor initiative or the active ticket chain surfaced by the search.
4. Read linked research/spec/plan/evidence/critique only as needed to understand
   the current blockers, gaps, acceptance posture, and child-output history.
5. If no checkpoint or anchor can be found, do not invent one from memory. Ask the
   user for the missing decision or repair the workspace/owner records, then place
   the durable answer in the owner layer that owns it.

## Hard Preflight Gates

These gates run before local execution, Ralph packets, acceptance review, ship, any
external handoff/PR/release packaging, or dependent continuation.

There are two outcomes:

- **owner repair required**: the failed gate identifies the owner layer that can
  repair it, such as constitution, initiative, research, spec, plan, ticket,
  evidence, critique, records repair, or a user decision
- **execution blocked**: implementation, acceptance, shipping or external handoff
  packaging, and dependent continuation must not proceed until the gate is
  repaired. Operator risk acceptance may disposition a known residual risk in the
  owning ticket; it cannot satisfy a missing prerequisite gate.

Failed gates do not block their own repair. They do block pretending the repair
already happened.

Accepted risk does not make these gate-passing:

- missing mandatory critique
- missing evidence required for the claim being made
- ambiguous intended behavior for behavior-affecting work
- unknown or overlapping write scope
- stale source fingerprint for child launch
- missing checkpoint facts required for recoverable continuation

When the missing prerequisite can be repaired, repair the owner record that owns
it. When work is intentionally abandoned or unsafe to continue, record the blocker,
cancellation, acceptance decision, or objective status in the owner record that
makes the stop truthful.

- Authority gate: objective, non-goals, `# Delegated Authority / Autonomy
  Boundaries`, and `# Objective-Level Stop Conditions` are clear enough for
  delegated drive work; otherwise ask the user or update constitution/initiative
  truth according to what is missing.
- Scope gate: next work is inside the initiative, plan, ticket, and write scope;
  otherwise refine plan/ticket scope or record why work stops.
- Behavior gate: intended behavior and acceptance are not ambiguous; otherwise
  update spec before implementation.
- Evidence gate: required observations exist; otherwise create evidence or
  research before relying on the claim.
- Critique gate: mandatory critique has three outcomes:
  - `completed`: dependent work may proceed, subject to ticket-owned finding
    dispositions.
  - `pending`: dependent work remains blocked until critique happens.
  - `blocking`: only repair, disposition, follow-up-ticket creation, or focused
    user decision may proceed according to the owning ticket.
  Mandatory critique is never satisfied by `not_required`, `deferred`, draft
  critique, stub critique, or an unreconciled packet result. Recommended or
  optional critique may be `not_required` only with ticket-owned rationale;
  unresolved medium/high findings block acceptance and dependent implementation
  that would rely on the challenged claim.
- Write-boundary gate: child write scopes are explicit and non-overlapping unless
  intentionally sequenced; otherwise repair plan/ticket scope or the packet.
- Budget/safety gate: time, cost, privacy, security, and risk limits are not
  exceeded; otherwise ask the user or record why work stops.
- Resume gate: checkpoint facts are current before child launch, parent stop, or
  any step that depends on recoverable continuation.

## Parallel Child Work Contract

Parallel child work is allowed only when tickets and write scopes are independent,
no generated files/lockfiles/shared state conflict, and the parent can reconcile
combined results before dependent continuation.

Each child needs:

- target and owning skill
- source snapshot or read scope
- child write scope or explicit read-only posture
- expected output contract
- failure/blocker vocabulary
- parent merge target
- concurrency posture: sequential, parallel-safe, or forbidden

## Stop Rule

If the checkpoint cannot be found, cannot be updated, or does not make
continuation recoverable, stop driving. Repair the owner records or ask the user;
do not continue from transcript intuition.

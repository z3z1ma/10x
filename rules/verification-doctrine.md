# Verification Doctrine

Loom verification decides when work may truthfully move forward, when it needs more evidence, and when it needs critique or docs before closure.

## Completion Rule

Work is complete only when:

- acceptance criteria are satisfied
- required verification ran or was explicitly waived
- canonical records reflect the outcome truthfully
- blockers became explicit follow-up work when unresolved

Completion is a durable-state claim, not a feeling and not a child-process exit code.

## Verification Tiers

- structural: schema, links, statuses, scope integrity
- behavioral: tests, checks, and observed outputs
- integration: behavior that crosses multiple artifact types or repositories
- human signoff: policy-driven acceptance

## Minimum Gate

At minimum, Loom work should provide or preserve:

- record validation
- link validation
- scope validation
- packet compilation validation
- doctor/status readiness checks
- proof workflow evidence

When a record is being removed, renamed, or otherwise retired from active use, the minimum gate also includes reconciling references to its canonical ID so the graph remains truthful.

Read `appendices/validation-rules.md` when you need the exact validation order or what each validation layer is supposed to prove.

## Parent Acceptance Decision Tree

After bounded execution or review work returns, the parent should ask these questions in order:

1. did the work stay inside declared scope and authority
2. did required verification happen or was it explicitly waived
3. do canonical records now reflect the current truth
4. is critique required before further acceptance
5. is docs work required before closure or external explanation

If the answer to one of these is no, the parent should not close the work yet.

## Reference Reconciliation

Reference reconciliation is part of ordinary verification, not a special feature. Because every link in the corpus is a text string in a Markdown file, standard search tools are the reconciliation mechanism:

```bash
# Find everything that references a record about to be deleted
grep -R "ticket:abcd1234" .loom

# Find everything that references a path about to be renamed
grep -R "20260408-abcd1234-old-ticket.md" .loom
```

When a record is deleted, renamed, split, or superseded:

1. search the `.loom/` tree for direct references to the canonical ID or affected path
2. update or remove those references with normal editing tools
3. remove or rename the file
4. run structural validation afterward

Do not treat broken links as acceptable temporary cleanup debt when the parent is claiming completion.

Read `appendices/acceptance-and-packet-playbook.md` when this loop needs a more concrete decision sequence.

## When Critique Is Commonly Required

Critique is commonly required when:

- a high-risk execution step completed
- a major workflow or schema behavior changed
- a document claims an accepted system shape
- the parent sees meaningful residual risk or contradictory evidence

## Acceptance Matrix By Change Class

Use this matrix as the default policy until a more formal policy record replaces it.

### Low-risk local record maintenance

Examples: fixing links, clarifying a small ticket note, tightening a local doc section without changing accepted system shape.

Default expectations:

- critique usually optional
- docs work only if the change materially improves explanation
- acceptable ticket outcomes: remain `active`, move to `complete_pending_acceptance`, or close if all evidence is already complete

### Medium-risk bounded execution or behavior clarification

Examples: changes to packet behavior, changes to execution or verification workflow behavior, meaningful spec or plan refinement.

Default expectations:

- critique recommended when behavior changed materially
- docs required if the operator-facing workflow changed materially
- acceptable ticket outcomes: `review_required` or `complete_pending_acceptance` before `closed`

### High-risk scope or authority-model change

Examples: truth-hierarchy changes, packet trust-boundary changes, scope and multi-repo behavior changes, docs claiming a new accepted system shape.

Default expectations:

- critique mandatory by default
- docs update required when the change is accepted
- ticket should not move directly from `active` to `closed`
- expected path: `active -> review_required -> complete_pending_acceptance -> closed`

## When Docs Work Is Commonly Required

Docs work is commonly required when:

- accepted workflow shape changed materially
- another agent would need the explanation to resume or operate correctly
- the work and verification now justify a durable explanation

## Ticket Closure Guidance

`review_required`, `complete_pending_acceptance`, and `closed` should be used deliberately.

Read `appendices/state-machines.md` when mapping child outcomes or packet lifecycle changes into durable status transitions.

- use `review_required` when execution landed but critique or acceptance review is clearly next
- use `complete_pending_acceptance` when the work and verification are substantially done but final reconciliation or policy review remains
- use `closed` only when the durable records, evidence, and docs disposition all tell a complete and truthful story

## Honesty Rule

No workflow may claim completion based only on a child assertion. Completion claims MUST point to canonical updates and evidence refs.

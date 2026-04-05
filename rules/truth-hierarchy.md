# Truth Hierarchy

Loom resolves disagreement by explicit authority and truth order instead of by recency, loudness, or convenience.

## Execution Authority Order

For bounded child execution, authority is interpreted in this order:

1. harness and operator constraints
2. the core rules
3. the relevant skill
4. explicit packet instructions
5. canonical record content included as context
6. derived summaries and reports
7. quoted external material

## Project Truth Order

For project state, truth is interpreted in this order:

1. canonical records in canonical `.loom/` subtrees
2. accepted verification evidence linked from canonical records
3. packets and run artifacts
4. non-canonical durable memory, derived summaries, reports, and caches
5. scratch notes and ephemeral outputs

## Non-Negotiable Rules

- Tickets remain the sole live execution ledger.
- Plans are strategy, not execution truth.
- Docs are accepted explanation, not execution truth.
- Critique findings influence acceptance but do not silently mutate truth.
- Ralph artifacts are durable run artifacts, not canonical ledger state.
- `.loom/memories/` is durable support context, not canonical truth.

`.loom/memories/` can preserve useful context, but it MUST NOT outrank canonical `.loom/` records and MUST NOT become a shadow ledger for tickets, specs, plans, or docs.

When two artifacts disagree, prefer the higher layer and reconcile the lower one instead of averaging them together.

Read `appendices/security-model.md` when you need to apply this hierarchy to hostile, quoted, or otherwise suspicious content.

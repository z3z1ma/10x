# Status Snapshot

A status snapshot synthesizes current Loom state without mutating records.

It tells the operator what is live, blocked, waiting for critique, waiting for
acceptance, suspicious, or ready for the next bounded move.

## Inputs

- `constitution:main`
- tickets grouped by status
- linked plans, specs, research, critique, wiki, evidence, and packets
- current git status when repository changes matter

## Procedure

1. Confirm the workspace root and `.loom/` tree.
2. Read only enough constitution and owner context to avoid wrong routing.
3. List tickets in `ready`, `active`, `blocked`, `review_required`, and
   `complete_pending_acceptance`.
4. For the target slice, note linked owners and support records.
5. Surface contradictions and drift.
6. Recommend the next command or owner skill.

## Drift Signals

- ticket says `review_required` but no critique path exists
- ticket says `complete_pending_acceptance` but evidence is weak
- coverage IDs are named but not supported by evidence
- non-ticket status is outside the lifecycle grammar
- plan is tracking live execution state
- wiki or memory is carrying owner truth
- packet remains `compiled` after the child output has returned

## Native Queries

```bash
rg -n '^status:' .loom/tickets --glob '*.md'
rg -n '^status:' .loom/{constitution,initiatives,research,specs,plans,critique,wiki,evidence,packets} --glob '*.md'
rg -n 'REQ-[0-9]{3}|ACC-[0-9]{3}|CLAIM-[0-9]{3}' .loom --glob '*.md'
find .loom/{tickets,critique,wiki,evidence} -type f -name '*.md' | sort
git status --short
```

## Output Shape

- status snapshot
- active, blocked, review, and acceptance queues
- contradictions or stale state
- best next command and why

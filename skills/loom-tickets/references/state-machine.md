# Ticket State Machine

## Normal states

- `proposed`
- `ready`
- `active`
- `blocked`
- `review_required`
- `complete_pending_acceptance`
- `closed`
- `cancelled`

## Heuristics

### `ready`

Use when the ticket is clear enough to begin.

### `active`

Use when the bounded execution is underway.

### `blocked`

Use when a concrete blocker exists and is named.

### `review_required`

Use when implementation landed and critique/acceptance review is clearly next.

### `complete_pending_acceptance`

Use when the work and evidence are mostly complete but final acceptance or final follow-through remains.

### `closed`

Use only when the story is truthful and complete.

## Anti-pattern

Do not use `closed` as a synonym for "I think the coding part is done."

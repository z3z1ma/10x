# Finding Format

Each meaningful finding should normally include:

- a stable ID: `FIND-001`
- a short title
- severity: `low | medium | high`
- confidence: `low | medium | high`
- disposition: `open | resolved | accepted_risk | superseded`
- what was observed
- why it matters
- what follow-up would reduce the risk

For code findings, include file and line references when practical.
For artifact findings, include record IDs or paths.

Keep findings concrete.
A critique record should help someone act, not merely worry.

## Finding References

When another record refers to a finding, qualify it:

```text
critique:<slug>#FIND-001
```

Tickets should use those references when tracking critique disposition.

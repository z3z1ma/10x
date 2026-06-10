# Use General Subagent For Ralph Runs

Status: active
Created: 2026-05-25
Updated: 2026-05-25

Legacy note: Triggers — Ralph run, worker run, subagent, loom-driver, general subagent, permissions broken, ticket execution
Legacy note: Applies to — Agent Loom ticket execution, bounded Ralph runs, OpenCode task tool

## Preference

Use the `general` subagent for bounded Ralph worker runs in this repo. Do not use the `loom-driver` subagent for the current compression ticket sequence because its permissions are broken.

## Use When

Apply this when launching implementation, inspection, review, or continuation workers for Loom tickets in this repo, especially the `.loom/tickets/20260525-loom-protocol-compression.md` child tickets.

## Do Not Overapply

This does not change Loom's conceptual Driver role or product behavior. It is a local execution preference for the available OpenCode subagent transport. If the operator later says `loom-driver` permissions are fixed, update or remove this record.

## Source Or Note

Operator note on 2026-05-25: "don't use loom-driver subagent, the permissions are broken. use a general subagent as you work all the tickets."

## Related Records

- `.loom/tickets/20260525-loom-protocol-compression.md` - current ticket sequence where this preference applies.

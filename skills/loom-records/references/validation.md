# Validation

Without bundled helper scripts, validation becomes an explicit operator behavior.

That is acceptable as long as it stays disciplined.

## Local Record Validation

Ask:

- does the frontmatter exist and parse visually
- are the common fields present
- are the major required sections present
- do the status and link choices make sense for the kind
- do the filename and ID agree

## Graph Validation

Ask:

- does each linked record actually exist
- are there obvious broken refs
- did this rename or split leave stale pointers
- did a non-owner layer start carrying owner truth

## Spot-Check Recipes

### Missing IDs

```bash
rg -L '^id:' .loom --glob '*.md'
```

### Missing status

```bash
rg -L '^status:' .loom --glob '*.md'
```

### Files that mention a record but do not link it in frontmatter

Use this as a heuristic, not a rigid rule.
Sometimes prose mention is enough.

### Compare changed graph edges

```bash
git diff -- .loom
rg -n 'ticket:abcd1234|spec:packet-discipline|wiki:ralph' .loom
```

## Evidence Records

If validation work itself matters later, preserve it as an evidence record.

Examples:

- a smoke test run
- a packet scope audit
- a migration sweep
- a manual comparison of linked records

## When To Escalate

Escalate instead of forcing closure when:

- broken references are widespread
- ownership is ambiguous
- the intended behavior and the implemented behavior disagree materially
- critique surfaced unresolved medium/high-severity issues

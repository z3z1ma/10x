# Ralph Script Reference

Use package-local script paths from this skill bundle.

The examples below assume invocation through `scripts/ralph.py` inside `loom-ralph`.

## Direct Ralph Query Ideas

The bundled CLI compiles Ralph packet artifacts and writes verification records.

The queries below are examples, not a canonical command surface. Use them as portable patterns when you need to inspect `.loom/runs/ralph/` and Ralph-linked verification directly.

Compiled Ralph packets by recency and target:

```bash
rg -n '"status":\s*"compiled"|"generated_at":\s*"[^"]+"|"ref":\s*"ticket:[^"]+"' .loom/runs/ralph/*.md
```

All Ralph packet artifacts for one target ticket:

```bash
rg -l '"target":\s*\{\s*"kind":\s*"ticket",\s*"ref":\s*"ticket:z8h0g58e"' .loom/runs/ralph
```

Allowed write refs for one target ticket's packet family:

```bash
rg -n '"ref":\s*"ticket:z8h0g58e"|"allowed_write_refs":\s*\[' .loom/runs/ralph/*.md
```

Verification artifacts linked to the same ticket before acceptance:

```bash
rg -l 'ticket:z8h0g58e' .loom/verification
```

## `scripts/ralph.py packet`

Purpose:

- scaffold a bounded Ralph execution packet record under `.loom/runs/ralph/`

Arguments:

- `target_ref`: canonical target ref, usually a ticket ref
- `subsystem`: use `ralph` in this skill
- `--mode`: packet mode
- `--style`: packet style
- `--allow-write-ref`: repeatable allowed-write ref for execution packets
- `--output`: optional output path override

Output:

- prints the compiled packet path relative to the workspace

Example:

```bash
scripts/ralph.py packet "ticket:z8h0g58e" ralph --mode execution --style reference-first --allow-write-ref "ticket:z8h0g58e"
```

## `scripts/ralph.py verify`

Purpose:

- create verification evidence after a Ralph run or supporting check

Arguments:

- `slug`: verification slug
- `--link`: verification frontmatter links
- `--path`, `--repository`, `--workspace-scope`: scope inputs

Example:

```bash
scripts/ralph.py verify ralph-ticket-z8h0g58e-run --link "ticket:z8h0g58e"
```

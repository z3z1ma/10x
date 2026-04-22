# Protocol Conformance

This is a human and agent checklist, not a required validator.

A Loom workspace is conformant enough when these are true:

- required `.loom/` tree exists
- `constitution:main` exists
- common record frontmatter fields are present
- ticket states are legal
- non-ticket statuses follow the shared lifecycle grammar
- ticket templates start as `proposed`, not `ready`
- claim references are qualified across records as `<record-id>#ACC-001`
- packets declare source fingerprint, context budget, execution context, and
  child write boundary
- parent reconciliation updates tickets, evidence, critique, and wiki owners
- packets do not remain `compiled` after reconciliation
- tickets do not close with unresolved required critique
- wiki pages cite accepted sources and do not own behavior or policy
- commands do not own unique protocol behavior
- utility skills are not required for the protocol kernel

## Useful Spot Checks

```bash
rg -L '^id:' .loom --glob '*.md'
rg -L '^status:' .loom --glob '*.md'
rg -n '^status:' .loom --glob '*.md'
rg -n '[a-z]+:[a-z0-9-]+#(REQ|ACC|CLAIM)-[0-9]{3}' .loom --glob '*.md'
find commands -maxdepth 1 -type f -name '*.md' | sort
find skills -maxdepth 2 -name SKILL.md | sort
```

## Drift Response

If a check fails, route to the owner:

- structure or grammar -> `loom-records`
- ticket state -> `loom-tickets`
- behavior contract -> `loom-specs`
- sequencing -> `loom-plans`
- review findings -> `loom-critique`
- accepted explanation -> `loom-wiki`
- durable policy -> `loom-constitution`

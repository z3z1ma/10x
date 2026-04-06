# Constitutional Script Reference

Use package-local script paths from this skill bundle.

The examples below assume invocation through `scripts/constitution.py` inside `loom-constitution`.

## Direct Constitutional Query Ideas

The bundled CLI scaffolds constitutional records, mutates links, and validates structural integrity.

The queries below are examples, not a canonical command surface. Use them as portable patterns when you need to inspect `.loom/constitution/` directly.

Constitutional records by kind, state, and recency:

```bash
rg -n '"kind":\s*"(constitution|decision|roadmap)"|"status":\s*"(active|revised|superseded)"|"updated_at":' .loom/constitution/**/*.md .loom/constitution/*.md
```

The main policy anchor to read first:

```bash
rg -n '"id":\s*"constitution:main"|^# (Vision|Principles|Constraints|Strategic Direction|Current Focus)$' .loom/constitution/constitution.md
```

Sections that usually drive constitutional execution implications:

```bash
rg -n '^# (Decision|Consequences|Supersession|Strategic Theme|Milestones|Downstream Work|Status Summary)$' .loom/constitution/{decisions,roadmap}/*.md
```

Downstream records that reference constitutional artifacts:

```bash
rg -n 'constitution:main|decision:[0-9]{4}|roadmap:' .loom/{research,initiatives,specs,plans,tickets,docs,critique}
```

## `scripts/constitution.py create constitution`

Purpose:

- create or intentionally replace a constitution record scaffold
- with no slug, validate constitution records instead

Example:

```bash
scripts/constitution.py create constitution main
```

## `scripts/constitution.py create decision`

Purpose:

- create one numbered decision record under `.loom/constitution/decisions/`

Example:

```bash
scripts/constitution.py create decision packet-trust-boundary
```

## `scripts/constitution.py create roadmap`

Purpose:

- create one roadmap record for strategic direction and milestone framing

Example:

```bash
scripts/constitution.py create roadmap bootstrap-the-markdown-first-protocol-corpus
```

## `scripts/constitution.py link`

Purpose:

- add or remove typed links on decision and roadmap records after the prose is in place

Example:

```bash
scripts/constitution.py link "roadmap:bootstrap-the-markdown-first-protocol-corpus" --add "decision:0002"
```

## `scripts/constitution.py diagnose`

Purpose:

- validate structural integrity before leaving the constitutional layer

Example:

```bash
scripts/constitution.py diagnose --json
```

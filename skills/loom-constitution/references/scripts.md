# Constitutional Script Reference

Use package-local script paths from this skill bundle.

The examples below assume invocation through `scripts/loom` inside `loom-constitution`.

## `scripts/loom create constitution`

Purpose:

- create or intentionally replace a constitution record scaffold
- with no slug, validate constitution records instead

Example:

```bash
scripts/loom create constitution main --title "Main Constitution"
```

## `scripts/loom create decision`

Purpose:

- create one numbered decision record under `.loom/constitution/decisions/`

Example:

```bash
scripts/loom create decision packet-trust-boundary --title "Make packet trust boundaries explicit"
```

## `scripts/loom create roadmap`

Purpose:

- create one roadmap record for strategic direction and milestone framing

Example:

```bash
scripts/loom create roadmap bootstrap-the-markdown-first-protocol-corpus --title "Bootstrap the Markdown-first protocol corpus"
```

## `scripts/loom link`

Purpose:

- add or remove typed links on decision and roadmap records after the prose is in place

Example:

```bash
scripts/loom link "roadmap:bootstrap-the-markdown-first-protocol-corpus" --add "decision:0002"
```

## `scripts/loom diagnose`

Purpose:

- validate structural integrity before leaving the constitutional layer

Example:

```bash
scripts/loom diagnose --json
```

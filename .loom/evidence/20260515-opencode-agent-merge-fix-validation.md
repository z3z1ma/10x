# OpenCode Agent Merge Fix Validation

Status: recorded
Created: 2026-05-15
Updated: 2026-05-15
Observed: 2026-05-15 08:44 UTC

## Observations

### Core Package Check

Procedure:

```text
npm --prefix "loom-core" run pack:check
```

Result: passed.

Relevant smoke output showed the new model-only shadowing regression coverage passed:

```json
{
  "modelOnlyLoomWeaverPreservesModel": true,
  "modelOnlyLoomDriverPreservesModel": true,
  "modelOnlyLoomWeaverPromptHasWriteBoundary": true,
  "modelOnlyLoomDriverPromptHasDirectionRecordBoundary": true,
  "modelOnlyLoomWeaverEditPermission": {
    "*": "deny",
    ".loom/**": "allow"
  },
  "modelOnlyLoomDriverEditPermission": {
    "*": "deny",
    ".loom/constitution/**": "deny",
    ".loom/specs/**": "deny",
    ".loom/plans/**": "deny",
    ".loom/research/**": "deny",
    ".loom/tickets/**": "allow",
    ".loom/packets/ralph/**": "allow",
    ".loom/evidence/**": "allow",
    ".loom/audit/**": "allow"
  }
}
```

The dry-run package completed and included `loom-core.mjs` plus the renamed using-loom reference files.

### Whitespace Check

Procedure:

```text
git diff --check
```

Result: passed with no output.

### README Revert Check

Procedure:

```text
git diff -- "README.md"
```

Result: passed with no output. The accidental `Hello world.` edit from the failing runtime test is no longer present in `README.md`.

## What This Shows

- Supports `.loom/tickets/done/20260515-opencode-weaver-agent-runtime-wiring.md#ACC-002`: the plugin-level merge now installs canonical prompts and permissions over preexisting model-only Loom agent stubs while preserving the model field.
- Supports `.loom/tickets/done/20260515-opencode-weaver-agent-runtime-wiring.md#ACC-003`: smoke coverage now exercises the specific model-only shadowing case that previously escaped the self-referential check.
- Supports `.loom/tickets/done/20260515-opencode-weaver-agent-runtime-wiring.md#ACC-005`: core package and Markdown diff checks passed after the plugin merge fix.

## What This Does Not Show

- It does not prove the already-running OpenCode session has reloaded the fixed plugin.
- It does not satisfy `.loom/tickets/done/20260515-opencode-weaver-agent-runtime-wiring.md#ACC-004`; a fresh runtime `loom-weaver` invocation after plugin reload is still required.
- It does not replace adversarial audit.

# open-loom Install

## Transport Surface

- `open-loom.mjs` is the OpenCode plugin entrypoint at the package root.
- The plugin reads top-level `rules/*.md` from the package or cloned repository using module-relative file reads.
- It exposes `experimental.chat.system.transform` to prepend a clear Loom rule block to OpenCode's `output.system` array.
- It exposes inspection helpers for bundled `skills/` and optional `commands/`, but current validation does not prove first-class OpenCode registration APIs for either surface.

## Expected Plugin Entries

Normal npm-package users should use the package entry after `open-loom` is published:

```json
{
  "plugin": ["open-loom"]
}
```

Cloned-repository users should use a local file/path entry that points at the plugin file:

```json
{
  "plugin": ["file:///absolute/path/to/agent-loom/open-loom.mjs"]
}
```

Relative or absolute local path specs may also be usable when they are resolved by OpenCode from the expected config location, but the `file://` form is the most explicit local clone recommendation.

Git URL plugin specs are not recommended. Source-level handling may mention git-like specs, but current operator validation found Git URL plugin installs unsupported in practice; use npm publication or a local file/path entry instead.

## Surface Disposition

- Rules: plugin-first through `experimental.chat.system.transform`; structural smoke checks can prove ordered rule reads without running OpenCode.
- Skills: discoverable through `inspectLoomBundle()`, but fallback direct install remains required until OpenCode exposes or documents a first-class skill registration API for plugins.
- Commands: discoverable through `inspectLoomBundle()`, but fallback direct install remains required until OpenCode exposes or documents a first-class slash-command registration API for plugins.

## Structural Smoke Check

Run from the repository root:

```bash
node open-loom.mjs --smoke
```

The smoke output should list ordered rule files from `rules/`, confirm Loom block markers, and report skill/command discovery counts. It does not validate OpenCode TUI/runtime behavior.

## Common Wrong Behavior

- treating generated plugin output as canonical Loom semantics
- claiming plugin-first skill or command registration before OpenCode proves those APIs
- recommending Git URL plugin specs as the normal install path
- replacing the direct OpenCode fallback before plugin runtime behavior is accepted

---
id: evidence:open-loom-smoke
kind: evidence
status: recorded
created_at: 2026-04-25T20:01:52Z
updated_at: 2026-04-25T20:29:14Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:6uy1rx20
  packet:
    - packet:ralph-ticket-6uy1rx20-20260425T195559Z
  research:
    - research:loom-install-distribution-methods
external_refs:
  opencode_source:
    - https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/plugin/src/index.ts
    - https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/opencode/src/plugin/shared.ts
    - https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/opencode/test/plugin/trigger.test.ts
---

# Summary

Structural smoke evidence for `open-loom`, the OpenCode Loom plugin.

The evidence shows that `open-loom` can read the repository's ordered top-level
Loom rule files, expose an OpenCode-shaped server plugin object, and mutate an
`output.system` array through `experimental.chat.system.transform` in a local
Node check. A temporary-home OpenCode CLI install check also detected
`open-loom` as a server target and wrote the expected local `file://` plugin config.
It also records that skills and commands are inspectable but not proven as
first-class OpenCode plugin registrations.

# Procedure

1. Inspected the pre-existing OpenCode fallback implementation in
   `scripts/install-loom.sh` and the prior direct adapter note in
   `examples/adapters/opencode-rule-install/README.md`.
2. Ran `node open-loom.mjs --smoke` from the repository root.
3. Fetched OpenCode source references for the plugin hook and loader shape:
   `packages/plugin/src/index.ts`, `packages/opencode/src/plugin/shared.ts`, and
   `packages/opencode/test/plugin/trigger.test.ts`.
4. Corrected the plugin to default-export an object with `id` and `server()`
   and to mutate `output.system: string[]` instead of returning a string.
5. Ran an import-based Node check:

   ```bash
   node --input-type=module -e 'import plugin, { server, readOrderedRuleFiles, inspectLoomBundle } from "./open-loom.mjs"; const hooks = await server({}, {}); const out = { system: ["existing"] }; await hooks["experimental.chat.system.transform"]({ model: { providerID: "test", modelID: "test" } }, out); if (plugin.id !== "open-loom" || typeof plugin.server !== "function") throw new Error("default plugin object invalid"); if (out.system.length !== 2 || !out.system[0].includes("rules/01-core-identity.md") || out.system[1] !== "existing") throw new Error("transform did not prepend Loom block"); const rules = readOrderedRuleFiles(); const bundle = inspectLoomBundle(); console.log(JSON.stringify({defaultId: plugin.id, ruleCount: rules.length, firstRule: rules[0].path, lastRule: rules.at(-1).path, skillCount: bundle.skills.items.length, commandCount: bundle.commands.items.length, systemEntries: out.system.length}, null, 2));'
   ```

6. Ran a temporary-home OpenCode install check:

   ```bash
   tmp="$(mktemp -d)"; HOME="$tmp" XDG_CONFIG_HOME="$tmp/.config" opencode plugin "file://$PWD/open-loom.mjs" --global --print-logs --log-level DEBUG
   ```

7. Read the generated temporary OpenCode config at
   `/var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/tmp.u08fQQMjgn/.config/opencode/opencode.json`.
8. Ran a missing-commands tolerance check for helper discovery:

   ```bash
   node --input-type=module -e 'import { inspectLoomBundle } from "./open-loom.mjs"; import { mkdtempSync, mkdirSync, writeFileSync } from "node:fs"; import { join } from "node:path"; import { tmpdir } from "node:os"; const root = mkdtempSync(join(tmpdir(), "open-loom-missing-commands-")); mkdirSync(join(root, "skills", "demo"), { recursive: true }); writeFileSync(join(root, "skills", "demo", "SKILL.md"), "---\nname: demo\ndescription: demo skill\n---\n"); const out = inspectLoomBundle({ rootDir: root }); if (out.skills.items.length !== 1) throw new Error("skill discovery failed"); if (out.commands.items.length !== 0) throw new Error("missing commands should produce empty list"); console.log(JSON.stringify({skillCount: out.skills.items.length, commandCount: out.commands.items.length}, null, 2));'
   ```

9. Ran `git diff --check`.

# Artifacts

`node open-loom.mjs --smoke` output:

```json
{
  "ok": true,
  "ruleCount": 7,
  "ruleFiles": [
    "rules/01-core-identity.md",
    "rules/02-truth-and-authority.md",
    "rules/03-outer-loop.md",
    "rules/04-ralph-inner-loop.md",
    "rules/05-critique-and-wiki.md",
    "rules/06-filesystem-and-tooling.md",
    "rules/07-validation-and-honesty.md"
  ],
  "firstRule": "rules/01-core-identity.md",
  "lastRule": "rules/07-validation-and-honesty.md",
  "blockHasMarkers": true,
  "transformPrependsBlock": true,
  "skillCount": 20,
  "commandCount": 19,
  "skillsResult": "discoverable only; direct-copy fallback still required for OpenCode skill surfaces",
  "commandsResult": "discoverable only; direct-copy fallback still required for OpenCode command surfaces"
}
```

Import-based hook/default-object validation output:

```json
{
  "defaultId": "open-loom",
  "ruleCount": 7,
  "firstRule": "rules/01-core-identity.md",
  "lastRule": "rules/07-validation-and-honesty.md",
  "skillCount": 20,
  "commandCount": 19,
  "systemEntries": 2
}
```

`git diff --check` output: no output.

OpenCode CLI install output excerpt:

```text
◇  Plugin package ready
◇  Detected server target
◇  Plugin config updated
●  Added to /var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/tmp.u08fQQMjgn/.config/opencode/opencode.json
◆  Installed file:///Users/alexanderbutler/code_projects/personal/agent-loom/open-loom.mjs
●  Scope: global (/var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/tmp.u08fQQMjgn/.config/opencode)
```

Generated temporary `opencode.json`:

```json
{
  "plugin": [
    "file:///Users/alexanderbutler/code_projects/personal/agent-loom/open-loom.mjs"
  ]
}
```

Missing-commands tolerance output:

```json
{
  "skillCount": 1,
  "commandCount": 0
}
```

Changed files inspected:

- `package.json`
- `open-loom.mjs`
- `examples/adapters/open-loom-install/README.md`
- `INSTALL.md`

# Supports Claims

- `ticket:6uy1rx20` bundled file-read acceptance: `open-loom` read 7 ordered
  top-level rule files from `rules/` through module-relative reads.
- `ticket:6uy1rx20` ordered-rule plugin injection acceptance, structurally: the
  local hook check prepended a Loom block to an existing `output.system` array.
- `ticket:6uy1rx20` npm/local path documentation acceptance: `INSTALL.md` and the
  fixture document npm package placeholder and local `file://` clone entry shapes.
- `ticket:6uy1rx20` local file/path runtime installation acceptance, partially:
  OpenCode CLI `1.14.22` detected the local `file://` plugin as a server target
  and wrote it to temporary global config.
- `ticket:6uy1rx20` skill and command fallback acceptance: `open-loom` reports
  skill and command metadata as discoverable only and records direct fallback as
  still required.

# Challenges Claims

None - no stable claim IDs are directly challenged. The evidence limits any claim
that `open-loom` is fully accepted in real OpenCode runtime loading.

# Environment

Commit: `b9bdc32c15aa166194a202a221c524cef7c81049`

Branch: `main`

Runtime: Node `v22.22.1`; OpenCode CLI `1.14.22`

OS: macOS / Darwin

Relevant config: current checkout, dirty with install-experience Loom record and
`open-loom` changes.

# Validity

Valid for: structural package/clone layout validation of local `open-loom`.

Recheck when: OpenCode plugin APIs change, package publication naming changes,
the repository package layout changes, or `open-loom` is promoted from validation
surface to recommended install path.

# Limitations

This evidence establishes that `opencode plugin` can detect and install the local
file plugin into a temporary global config. It does not establish that a real
OpenCode chat/TUI session invokes the hook or that a model request includes the
injected rules.

This evidence does not establish first-class OpenCode registration for Loom
skills or optional commands.

This evidence does not establish that a future npm-published package name,
versioning, or package-manager install path is ready.

# Result

`open-loom` structurally reads ordered Loom rules, exposes the hook shape expected
by current OpenCode source, and is detected by the OpenCode CLI as a server
plugin from a local `file://` entry. It keeps skills and commands as inspectable
metadata only, with direct fallback still required.

# Interpretation

The ticket can treat plugin-first rule injection as structurally promising and
the local file/path plugin entry as partially runtime-validated for installation
and server-target detection. It should not claim a complete plugin-first OpenCode
install until real chat/TUI hook invocation is validated and skill/command
fallback or upstream API decisions are accepted.

# Related Records

- `ticket:6uy1rx20`
- `packet:ralph-ticket-6uy1rx20-20260425T195559Z`
- `research:loom-install-distribution-methods`

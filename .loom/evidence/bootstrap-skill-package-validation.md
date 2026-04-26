---
id: evidence:bootstrap-skill-package-validation
kind: evidence
status: recorded
created_at: 2026-04-26T06:52:09Z
updated_at: 2026-04-26T07:23:57Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:jt2vy25y
  decision:
    - decision:0005
    - decision:0006
  evidence:
    - evidence:codex-sessionstart-stdout-context
external_refs: {}
---

# Summary

Validation evidence for repackaging Loom's mandatory doctrine as the
`loom-bootstrap` skill and updating adapter paths to read ordered bootstrap
references from `skills/loom-bootstrap/references/`.

# Procedure

- Validated JSON surfaces with `python3 -m json.tool` for:
  - `.codex-plugin/plugin.json`
  - `.agents/plugins/marketplace.json`
  - `.codex/hooks.json`
  - `.claude-plugin/plugin.json`
  - `hooks/hooks.json`
  - `package.json`
- Ran `node open-loom.mjs --smoke`.
- Ran `claude plugin validate /Users/alexanderbutler/code_projects/personal/agent-loom`.
- Ran `git diff --check`.
- Ran `npm pack --dry-run`.
- Ran a Codex startup probe after updating `.codex/hooks.json` to emit
  `LOOM_BOOTSTRAP_REFERENCE` markers from `skills/loom-bootstrap/references/`.

# Artifacts

OpenCode smoke output showed:

```json
{
  "bootstrapReferenceCount": 7,
  "firstBootstrapReference": "skills/loom-bootstrap/references/01-core-identity.md",
  "lastBootstrapReference": "skills/loom-bootstrap/references/07-validation-and-honesty.md",
  "instructionCount": 7,
  "instructionsAreDeduped": true,
  "skillCount": 21,
  "bootstrapResult": "registered through config.instructions as ordered bootstrap references"
}
```

Claude plugin validation returned:

```text
Validating marketplace manifest: /Users/alexanderbutler/code_projects/personal/agent-loom/.claude-plugin/marketplace.json

✔ Validation passed
```

Codex bootstrap hook probe returned:

```json
{"bootstrap_markers_visible":true,"reference_files_seen":["01-core-identity.md","02-truth-and-authority.md","03-outer-loop.md","04-ralph-inner-loop.md","05-critique-and-wiki.md","06-filesystem-and-tooling.md","07-validation-and-honesty.md"],"reference_count":7,"first_visible_reference":"01-core-identity.md","validation_honesty_quote":"A child assertion is not enough."}
```

`npm pack --dry-run` listed the package contents with
`skills/loom-bootstrap/SKILL.md` and all seven
`skills/loom-bootstrap/references/*.md` files. It did not list top-level
`rules/*.md`, top-level `commands/*.md`, examples, `Makefile`, or
`scripts/install-loom.sh` files.

# Supports Claims

- `ticket:jt2vy25y` claim: `loom-bootstrap` exists as the mandatory skill package
  entry point with seven ordered references.
- `ticket:jt2vy25y` claim: OpenCode, Claude, and Codex adapter paths now reference
  bootstrap references instead of top-level `rules/` files.
- `ticket:jt2vy25y` claim: package contents include bootstrap references under
  `skills/`.
- `ticket:jt2vy25y` claim: Makefile, shell installer, and command-wrapper product
  surfaces are absent from the npm package surface.
- `decision:0005` consequence: optional adapter preload can use the same ordered
  bootstrap references.
- `decision:0006` consequence: `skills/` is the product surface.

# Challenges Claims

- None.

# Environment

Commit: `18fac92`
Branch: `main`
Runtime: `node`, `npm`, `python3`, `claude`, `codex-cli 0.125.0`
OS: `Darwin`
Relevant config: repository `.codex/config.toml`, `.codex/hooks.json`,
`hooks/hooks.json`, and `open-loom.mjs`.

# Validity

Valid for: the current uncommitted workspace diff on 2026-04-26.

Recheck when: bootstrap reference paths change, plugin manifests change,
`open-loom.mjs` changes, or target harness versions change.

# Limitations

- `npm pack --dry-run` checks package contents but does not publish or install the
  npm package.
- Codex hook validation proves trusted project hook preload, not installed remote
  plugin skill discovery.
- Claude validation was structural; marketplace install and runtime hook behavior
  were not re-probed after this change.

# Result

The structural and smoke checks passed. The observed package and adapter surfaces
now point at `skills/loom-bootstrap/references/` as the ordered bootstrap doctrine
source, and the npm package dry run includes `skills/` without fallback installer
or command-wrapper surfaces.

# Interpretation

This evidence supports the path migration and native-only package surface claims
for the local workspace. It does not prove Codex installed plugin skill discovery
or Claude installed marketplace runtime behavior.

# Related Records

- `ticket:jt2vy25y`
- `decision:0005`
- `evidence:codex-sessionstart-stdout-context`

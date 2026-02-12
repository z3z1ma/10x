# Loom Compound State

This directory stores instincts pipeline state.

## Files

- `instincts.json` — canonical instincts store
- `INSTINCTS.md` — derived instincts index
- `ROADMAP.md` — optional freeform roadmap scratchpad
- `runtime/observations.jsonl` — append-only observations log (gitignored)
- `state.json` — observation cursor/state for incremental instincts updates
- `config.json` — instincts derivation command template + placeholder interpolation config

## Contract

- Automatic path (`loom compound instincts-update` and adapter hooks) updates instincts/state using headless LLM derivation over observations + git diff.
- Derivation command is user-configured in `config.json` (not hardcoded to a specific harness).
- Scaffolded capture adapters are Claude (`.claude/settings.json`), OpenCode (`.opencode/plugins/compound_engineering.ts`), and OMP (`.omp/extensions/compound_engineering.ts`).
- Skill authoring is orthogonal and handled through harness-native skill invocation.
- `LOOM.md` and roadmap prose are intentionally freeform and not block-managed by compound Python.

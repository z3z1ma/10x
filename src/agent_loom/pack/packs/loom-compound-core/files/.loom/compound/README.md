# Loom Compound State

This directory stores Compound learning artifacts.

## Files

- `instincts/personal/*.md` — canonical personal instincts
- `instincts/inherited/*.md` — imported/shared instincts
- `INSTINCTS.md` — generated instinct index
- `runtime/observations.jsonl` — append-only observations log (gitignored)
- `runtime/observer.{pid,log,nudge}` — observer process state (gitignored)
- `state.json` — observation cursor and auto-learning bookkeeping
- `config.json` — instincts derivation command template
- `evolved/{skills,commands,agents}/` — generated evolved artifacts
- `ROADMAP.md` — optional freeform roadmap scratchpad

## Contract

- Hook adapters capture observations and echo Claude hook payloads to keep tool execution unblocked.
- `loom compound observer` provides background instincts compilation with cooldown + thresholds.
- `loom compound instinct-import` and `instinct-export` handle portable instinct bundles.
- `loom compound evolve --generate` emits learned skills/commands/agents for Claude/OpenCode.
- Derivation command is free-form and edits instinct markdown files directly.

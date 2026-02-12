# OpenCode Compound Integration

This scaffold wires OpenCode + Claude + OMP adapters into Loom Compound learning v2.

## Responsibilities

- Log normalized observations to `.loom/compound/runtime/observations.jsonl`.
- Forward harness events to Loom hook adapters.
- Nudge the background observer after each logged observation.
- Keep instincts/evolution logic in Loom Python code, not in plugin TypeScript.

## Core files

- `.opencode/plugins/compound_engineering.ts` — thin OpenCode adapter forwarding events to `loom compound opencode-hook`
- `.omp/extensions/compound_engineering.ts` — OMP adapter forwarding events to `loom compound omp-hook`
- `.claude/settings.json` — Claude hooks calling `loom compound claude-hook`
- `.loom/compound/config.json` — derivation config (`instincts.derive_command`)
- `.loom/compound/instincts/{personal,inherited}/` — markdown instinct store
- `.loom/compound/evolved/{skills,commands,agents}/` — generated evolved artifacts

## Runtime artifacts (gitignored)

- `.loom/compound/runtime/observations.jsonl`
- `.loom/compound/runtime/observations.jsonl.*.bak`
- `.loom/compound/runtime/observer.pid`
- `.loom/compound/runtime/observer.log`
- `.loom/compound/runtime/observer.nudge`

## Compound commands

- `loom compound instincts-update`
- `loom compound instinct-status`
- `loom compound instinct-export --out <file>`
- `loom compound instinct-import <file-or-url>`
- `loom compound evolve [--generate]`
- `loom compound observer {start|stop|status|run-once}`

## Derivation behavior

- Derivation command is user-configurable in `.loom/compound/config.json`.
- Loom does not require strict JSON schema output for derivation.
- Derivation command should edit instinct markdown files directly.

## Environment variables

- `COMPOUND_LOG_OBSERVATIONS=1|0` (default `1`)
- `COMPOUND_OBSERVATIONS_MAX_BYTES=33554432`
- `COMPOUND_OBSERVATIONS_MAX_BACKUPS=5`
- `COMPOUND_OBSERVATIONS_MAX_STRING_CHARS=2000`
- `COMPOUND_OBSERVATIONS_MAX_OBJECT_KEYS=50`
- `COMPOUND_INSTINCTS_MIN_NEW_OBSERVATIONS=12`
- `COMPOUND_INSTINCTS_COOLDOWN_SECONDS=120`
- `COMPOUND_OBSERVER_POLL_SECONDS=5`
- `COMPOUND_LOOM_BIN=loom`

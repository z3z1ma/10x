## Compound Cookbook

Loom Compound learning v2 pipeline:

observations -> instincts -> evolved artifacts.

## Runtime/data files

- Observations log: `.loom/compound/runtime/observations.jsonl` (gitignored)
- Observer runtime: `.loom/compound/runtime/observer.{pid,log,nudge}` (gitignored)
- Instinct store: `.loom/compound/instincts/personal/*.md`
- Imported instincts: `.loom/compound/instincts/inherited/*.md`
- Instinct index: `.loom/compound/INSTINCTS.md`
- State cursor/bookkeeping: `.loom/compound/state.json`
- Derivation config: `.loom/compound/config.json`
- Evolved artifacts: `.loom/compound/evolved/{skills,commands,agents}/`

## Harness observation capture

Compound scaffolds feed one centralized observation log from:

- Claude Code hooks (`.claude/settings.json` -> `loom compound claude-hook`)
- OpenCode plugin (`.opencode/plugins/compound_engineering.ts` -> `loom compound opencode-hook`)
- OMP extension (`.omp/extensions/compound_engineering.ts` -> `loom compound omp-hook`)

Claude hook contract is preserved: hook stdin payload is echoed back to stdout unchanged.

## Derivation config

`instincts-update` reads `.loom/compound/config.json` and executes `instincts.derive_command`.

The command is user-configurable so users can swap Claude/OpenCode/pi/Codex/etc. Loom does not enforce a JSON schema for derivation output. The command is expected to edit instinct markdown files directly under `.loom/compound/instincts/personal/`.

`derive_command` can be:
- array of argv tokens (recommended)
- shell-style string (split with shlex)

Supported placeholders in command tokens:
- `{prompt}`
- `{repo}`
- `{loom_compound_dir}`
- `{observations_file}`
- `{instincts_personal_dir}`
- `{instincts_inherited_dir}`
- `{min_occurrences}`
- `{max_candidates}`

## Commands

Install/upgrade scaffold:

```bash
loom compound init
loom compound init --dry-run
loom compound init --force
```

Compile instincts from observations:

```bash
loom compound instincts-update
loom compound instincts-update --auto
loom compound instinct-status
```

Observer lifecycle:

```bash
loom compound observer start
loom compound observer status
loom compound observer stop
loom compound observer run-once
```

Import/export:

```bash
loom compound instinct-export --out instincts.bundle.json
loom compound instinct-import instincts.bundle.json
```

Evolve instincts into skills/commands/agents:

```bash
loom compound evolve --threshold 0.75
loom compound evolve --generate
```

Process one harness adapter payload:

```bash
loom compound claude-hook
loom compound opencode-hook --event tool.execute.before
loom compound omp-hook --event tool_call
```

## Environment variables

- `COMPOUND_LOG_OBSERVATIONS=1|0` (default `1`)
- `COMPOUND_OBSERVATIONS_MAX_BYTES=33554432`
- `COMPOUND_OBSERVATIONS_MAX_BACKUPS=5`
- `COMPOUND_OBSERVATIONS_MAX_STRING_CHARS=2000`
- `COMPOUND_OBSERVATIONS_MAX_OBJECT_KEYS=50`
- `COMPOUND_INSTINCTS_MIN_NEW_OBSERVATIONS=12`
- `COMPOUND_INSTINCTS_COOLDOWN_SECONDS=120`
- `COMPOUND_OBSERVER_POLL_SECONDS=5`

## Automatic write boundaries

Hook adapter paths (`claude-hook`, `opencode-hook`, `omp-hook`) append only to runtime observations and observer nudge files.

# Cursor Install

## Transport Surface

- protocol skills are copied into `~/.cursor/skills/`
- optional command wrappers are generated as plain Markdown files in
  `~/.cursor/commands/`
- rule files are copied into `~/.cursor/loom/rules/`
- a managed block is written into Cursor User Rules for global always-on
  instruction loading

## Expected Properties

- Cursor project rules are not confused with global User Rules
- Loom rules are installed into Cursor's native always-on User Rules surface
- command wrappers remain invocation adapters
- protocol skills remain the subsystem behavior source
- uninstall removes Loom-managed files without touching project `.loom/`
  records

## Common Wrong Behavior

- assuming project `.cursor/rules/` is a global install surface
- placing optional utilities into the default protocol skill set
- making generated command files more canonical than source skills

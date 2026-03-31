# Memory Housekeeping Command Reference

The pure-LLM command entrypoint for manual housekeeping lives at:

- `src/commands/loom-memory-housekeeping.md`

Use that file when a human wants an explicit cleanup pass that is executable from the prompt and the visible memory files alone.

The command and the skill should agree on intent:

- prune hot-memory clutter
- archive stale detail into glacier
- refresh backlink and archive indexes
- preserve structural trust without pretending to do reflection's semantic work

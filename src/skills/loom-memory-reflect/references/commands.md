# Memory Reflection Command Reference

The pure-LLM command entrypoint for manual reflection lives at:

- `src/commands/loom-memory-reflect.md`

Use that file when a human wants an explicit reflection run that should be executable purely from the prompt and the visible memory files.

The command and the skill should agree on intent:

- condense repeated observations into patterns
- tighten stale hot-memory summaries
- surface thread candidates
- move canonical facts out of memory and into canonical `.loom/` artifacts when needed

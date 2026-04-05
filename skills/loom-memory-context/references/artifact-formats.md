# Memory Artifact Formats

## Observations

Observations are the raw write-optimized layer. While observations capture raw events, threads (when raised) pull related fragments into a coherent narrative.

- Append only — never edit past entries
- Keep the date explicit
- Include tags when they help later retrieval

Format:

```text
- YYYY-MM-DD [tags]: observation
```

Tags: `insight`, `milestone`, `regression`, `workflow`, `decision`, `context`

## Action Items

Action items are supporting reminders, not Loom tickets. If the task is execution truth for the repository, it belongs in `.loom/tickets/`.

Format:

```text
- [ ] task | due:YYYY-MM-DD | pri:high/medium/low | added:YYYY-MM-DD
- [x] task (done YYYY-MM-DD)
```

Fields after task are optional — use what's relevant. `pri:` defaults to medium if omitted.

## Entities

Entities are the compact registry for named things. 3-line compact registry format. Max 3 content lines per entry.

Format:

```text
### Name (relationship)
key fact 1 | key fact 2 | key fact 3
status: active|inactive | last: YYYY-MM-DD | -> [[user/topic-or-thread]]
```

Heavy entries get promoted to thread files — the entity stub just links: `-> [[user/topic-name]]`.

**Temporal validity**: When a fact changes, mark old value as superseded with date. Entities inactive 6+ months → housekeeping moves to glacier.

## Patterns

Patterns are distilled rules, not raw events.

- Write what to do, not just what happened
- Keep them timeless where possible
- Merge overlapping patterns instead of allowing near-duplicates to pile up
- Core `system/patterns.md` has a HARD LIMIT of **70 lines / 5.5KB**
- Entries must be **timeless rules** — "what to do" not "what happened"

## Self-Observations

Self-observations track what worked or didn't about the agent's behavior.

Format:

```text
- YYYY-MM-DD [tag]: <observation>
```

Append only. Periodically distilled into patterns via reflection.

## Improvement Ideas

Format:

```text
- <idea> (added YYYY-MM-DD)
```

Edit in place by section. Stale ideas (>30 days, no progress) get archived to glacier or marked abandoned during reflection.

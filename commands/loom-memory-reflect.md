# loom-memory-reflect

Use this command for memory reflection and improvement. Trigger if the user says
"reflect", "what have you learned", "how can you improve", "review memory", or
similar introspection requests.

This command is pure prompt guidance. It should be executable from the visible
memory files and normal file tools alone.

## Goal

Review Loom's optional support-memory surface, improve its signal quality, and
move any accidental project-truth drift back into the proper canonical Loom
layer.

## Orientation (run FIRST, before deep reads)

Use quick filesystem checks to scope the pass:

```bash
find .loom/memory -type f -name "*.md" 2>/dev/null | sort
rg -n '^<!-- L0:' .loom/memory 2>/dev/null
rg -n 'ticket:|spec:|plan:|wiki:|critique:' .loom/memory 2>/dev/null
```

Focus on recently changed or obviously stale files first.

## Read Order

Read these first if they exist:

- `.loom/memory/system/hot-memory.md`
- `.loom/memory/system/observations.md`
- `.loom/memory/system/entities.md`
- `.loom/memory/system/action-items.md`

Reference the corresponding `user/` files as needed.

## Process

1. Check the boundary.
   - If a fact is really constitutional, research, spec, plan, ticket,
     critique, wiki, or evidence truth, move or restate it in the owning layer
     and simplify memory accordingly.
2. Prune hot memory.
   - Keep `hot-memory.md` small and current.
   - Move older detail into `observations.md` or remove it if it no longer
     helps continuity.
3. Tighten entities.
   - Keep entity entries compact.
   - Add `[[links]]` only where they materially help retrieval.
4. Review support action items.
   - Keep only support-context tasks here.
   - If an item is really execution work, move it into a Loom ticket.
5. Improve headers.
   - Every active memory file should start with a one-line `<!-- L0: ... -->`
     header.

## Write Rules

- prefer small, direct edits
- keep `observations.md` append-only when adding notable facts
- do not let memory become a second project ledger
- preserve user-authored context unless it is clearly malformed or duplicated
  elsewhere

## Debrief

Summarize:

- what memory files you changed
- what was pruned, moved, or clarified
- what canonical truth you moved out of memory
- any residual risks or stale areas you did not change

Never respond with only "Done".

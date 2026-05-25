<script lang="ts">
  import type { WorkstationState } from './types';

  let { workstations }: { workstations: Record<string, WorkstationState> } = $props();

  let summaries = $derived(
    Object.entries(workstations)
      .filter((entry): entry is [string, WorkstationState & { iteration_summary: NonNullable<WorkstationState['iteration_summary']> }] =>
        entry[1].iteration_summary !== null && entry[1].iteration_summary !== undefined
      )
      .sort((a, b) => a[0].localeCompare(b[0]))
  );
</script>

<section class="rounded-lg border border-cyan-500/20 bg-cyan-950/10 p-3">
  <div class="mb-3">
    <h2 class="text-sm font-semibold uppercase tracking-wider text-cyan-200">Iteration Summary</h2>
    <p class="mt-1 text-xs text-slate-500">Visibility output only. Not evidence, audit, or acceptance.</p>
  </div>

  {#if summaries.length === 0}
    <p class="text-xs text-slate-500">No completed workstation iterations yet.</p>
  {:else}
    <div class="space-y-2">
      {#each summaries as [ticketId, workstation] (ticketId)}
        {@const summary = workstation.iteration_summary}
        <details class="rounded-md border border-slate-800 bg-slate-950/70 p-2">
          <summary class="cursor-pointer text-xs font-medium text-slate-300">
            {ticketId} - iteration {summary.iteration} - exit {summary.exit_code ?? 'unknown'} - {summary.duration_seconds}s
          </summary>

          <div class="mt-3 space-y-3 text-xs text-slate-400">
            <div>
              <p class="font-medium text-slate-300">Files changed ({summary.files_changed.count})</p>
              {#if summary.files_changed.paths.length === 0}
                <p class="mt-1 text-slate-500">No file changes detected.</p>
              {:else}
                <ul class="mt-1 space-y-1 font-mono text-[11px] text-slate-500">
                  {#each summary.files_changed.paths as path}
                    <li>{path}</li>
                  {/each}
                </ul>
              {/if}
            </div>

            <div>
              <p class="font-medium text-slate-300">Records changed ({summary.records_changed.length})</p>
              {#if summary.records_changed.length === 0}
                <p class="mt-1 text-slate-500">No Loom record changes detected.</p>
              {:else}
                <ul class="mt-1 space-y-1">
                  {#each summary.records_changed as record}
                    <li>
                      <span class="font-mono text-slate-300">{record.record_id ?? record.path}</span>
                      <span class="text-slate-500"> changed {record.changed_fields.join(', ')}</span>
                    </li>
                  {/each}
                </ul>
              {/if}
            </div>
          </div>
        </details>
      {/each}
    </div>
  {/if}
</section>

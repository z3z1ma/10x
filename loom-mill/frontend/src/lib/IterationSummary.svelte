<script lang="ts">
  import type { WorkstationState } from './types';
  import { formatDuration } from './utils';

  let { workstations }: { workstations: Record<string, WorkstationState> } = $props();

  let summaries = $derived(
    Object.entries(workstations)
      .filter((entry): entry is [string, WorkstationState & { iteration_summary: NonNullable<WorkstationState['iteration_summary']> }] =>
        entry[1].iteration_summary !== null && entry[1].iteration_summary !== undefined
      )
      .sort((a, b) => a[0].localeCompare(b[0]))
  );
</script>

<section class="rounded-lg border border-border-default bg-bg-surface-elevated p-4">
  <div class="mb-3">
    <h2 class="text-[11px] font-medium uppercase tracking-wider text-text-secondary">Iteration Summary</h2>
    <p class="mt-1 text-[10px] text-text-tertiary">Visibility output only. Not evidence, audit, or acceptance.</p>
  </div>

  {#if summaries.length === 0}
    <p class="text-[11px] text-text-tertiary">No completed workstation iterations yet.</p>
  {:else}
    <div class="space-y-2">
      {#each summaries as [ticketId, workstation] (ticketId)}
        {@const summary = workstation.iteration_summary}
        <details class="rounded-md border border-border-subtle bg-bg-surface p-2">
          <summary class="cursor-pointer text-[11px] font-medium text-text-secondary hover:text-text-primary transition-colors">
            {ticketId} - iteration {summary.iteration} - exit {summary.exit_code ?? 'unknown'} - {formatDuration(summary.duration_seconds)}
          </summary>

          <div class="mt-2 space-y-3 text-[10px] text-text-tertiary">
            <div>
              <p class="font-medium text-text-secondary">Files changed ({summary.files_changed.count})</p>
              {#if summary.files_changed.paths.length === 0}
                <p class="mt-0.5">No file changes detected.</p>
              {:else}
                <ul class="mt-0.5 space-y-0.5 font-mono text-[9px]">
                  {#each summary.files_changed.paths as path}
                    <li>{path}</li>
                  {/each}
                </ul>
              {/if}
            </div>

            <div>
              <p class="font-medium text-text-secondary">Records changed ({summary.records_changed.length})</p>
              {#if summary.records_changed.length === 0}
                <p class="mt-0.5">No Loom record changes detected.</p>
              {:else}
                <ul class="mt-0.5 space-y-0.5">
                  {#each summary.records_changed as record}
                    <li>
                      <span class="font-mono text-text-secondary">{record.record_id ?? record.path}</span>
                      <span> changed {record.changed_fields.join(', ')}</span>
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

<script lang="ts">
  import type { IterationRecord } from './types';
  import { formatDuration, formatRelativeTime } from './utils';
  import { apiUrl } from './api';

  let { workstationId, onViewDiff }: { workstationId: string; onViewDiff?: (iterationIndex: number) => void } = $props();

  let iterations = $state<IterationRecord[]>([]);
  let loading = $state(true);
  let error = $state<string | null>(null);

  $effect(() => {
    if (workstationId) {
      loadIterations();
    }
  });

  async function loadIterations() {
    loading = true;
    error = null;
    try {
      const res = await fetch(apiUrl(`/workstations/${workstationId}/iterations`));
      if (!res.ok) throw new Error(`Failed to load iterations: ${res.statusText}`);
      iterations = await res.json();
    } catch (err: any) {
      error = err.message;
    } finally {
      loading = false;
    }
  }
</script>

<div class="flex flex-col h-full overflow-y-auto p-4 bg-bg-primary">
  {#if loading}
    <div class="text-[12px] text-text-tertiary">Loading iterations...</div>
  {:else if error}
    <div class="text-[12px] text-status-error-text flex items-center gap-2">
      <span>{error}</span>
      <button onclick={loadIterations} class="px-2 py-0.5 rounded bg-status-error-bg/20 hover:bg-status-error-bg/40 transition-colors">Retry</button>
    </div>
  {:else if iterations.length === 0}
    <div class="text-[12px] text-text-tertiary">No iterations recorded yet. Iterations are detected from git commits.</div>
  {:else}
    <div class="flex flex-col gap-3">
      {#each iterations as iter, i}
        <button
          type="button"
          class="w-full text-left flex flex-col gap-2 p-3 rounded-lg border border-transparent hover:bg-bg-surface-elevated hover:border-border-subtle transition-all duration-150 group cursor-pointer"
          onclick={() => onViewDiff?.(i)}
        >
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-2">
              <span class="text-[13px] font-semibold text-text-primary">Iteration {iter.iteration}</span>
              <span class="text-[11px] text-text-tertiary">{formatDuration(iter.duration_seconds)}</span>
              {#if iter.exit_code !== null}
                <span class="text-[11px] {iter.exit_code === 0 ? 'text-status-success-text' : 'text-status-error-text'}">
                  Exit: {iter.exit_code}
                </span>
              {/if}
            </div>
            <div class="flex items-center gap-2">
              <span class="text-[10px] text-accent-primary opacity-0 group-hover:opacity-100 transition-opacity">
                View diff →
              </span>
              <span class="text-[11px] text-text-tertiary" title={iter.started_at}>
                {formatRelativeTime(iter.started_at)}
              </span>
            </div>
          </div>
          
          {#if iter.diff_stat}
            <div class="text-[11px] font-mono text-text-secondary whitespace-pre-wrap bg-bg-surface p-2 rounded border border-border-subtle">
              {iter.diff_stat}
            </div>
          {/if}
          
          {#if iter.files_changed && iter.files_changed.length > 0}
            <div class="flex flex-col gap-1">
              <span class="text-[11px] font-medium text-text-secondary">Files changed:</span>
              <ul class="list-disc list-inside pl-4 text-[11px] text-text-tertiary">
                {#each iter.files_changed as file}
                  <li>{file}</li>
                {/each}
              </ul>
            </div>
          {/if}
        </button>
      {/each}
    </div>
  {/if}
</div>

<script lang="ts">
  import { onMount } from 'svelte';
  import type { IterationRecord } from './types';
  import DiffViewer from './DiffViewer.svelte';

  let { workstationId }: { workstationId: string } = $props();

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
      const apiBase = `${window.location.protocol}//${window.location.hostname}:8765`;
      const res = await fetch(`${apiBase}/workstations/${workstationId}/iterations`);
      if (!res.ok) throw new Error(`Failed to load iterations: ${res.statusText}`);
      iterations = await res.json();
    } catch (err: any) {
      error = err.message;
    } finally {
      loading = false;
    }
  }

  function formatDuration(s: number) {
    if (s < 60) return `${Math.floor(s)}s`;
    if (s < 3600) return `${Math.floor(s / 60)}m ${Math.floor(s % 60)}s`;
    return `${Math.floor(s / 3600)}h ${Math.floor((s % 3600) / 60)}m`;
  }
</script>

<div class="flex flex-col h-full overflow-y-auto p-4 bg-bg-primary">
  {#if loading}
    <div class="text-[12px] text-text-tertiary">Loading iterations...</div>
  {:else if error}
    <div class="text-[12px] text-status-error-text">{error}</div>
  {:else if iterations.length === 0}
    <div class="text-[12px] text-text-tertiary">No iterations recorded yet.</div>
  {:else}
    <div class="flex flex-col gap-6">
      {#each iterations as iter}
        <div class="flex flex-col gap-2">
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
            <div class="text-[11px] text-text-tertiary">
              {new Date(iter.started_at).toLocaleTimeString()}
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
        </div>
      {/each}
    </div>
  {/if}
</div>
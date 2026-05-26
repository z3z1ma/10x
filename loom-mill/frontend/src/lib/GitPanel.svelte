<script lang="ts">
  import type { GitState } from './types';

  let { git }: { git: GitState } = $props();

  let commits = $derived(git.recent_commits.slice(0, 3));
</script>

<div class="flex flex-col gap-3 rounded-lg border border-border-default bg-bg-surface-elevated p-4">
  <div class="flex items-center justify-between">
    <h2 class="text-[11px] font-medium text-text-secondary uppercase tracking-wider">Git State</h2>
    {#if git.dirty}
      <span class="badge bg-status-warning-bg text-status-warning-text ring-1 ring-inset ring-status-warning-border">
        Dirty
      </span>
    {:else}
      <span class="badge bg-status-success-bg text-status-success-text ring-1 ring-inset ring-status-success-border">
        Clean
      </span>
    {/if}
  </div>

  <div class="flex items-center gap-2 text-xs">
    <svg class="h-3.5 w-3.5 text-text-tertiary" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7v8a2 2 0 002 2h6M8 7V5a2 2 0 012-2h4.586a1 1 0 01.707.293l4.414 4.414a1 1 0 01.293.707V15a2 2 0 01-2 2h-2M8 7H6a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2v-2" />
    </svg>
    <span class="font-mono text-text-primary">{git.current_branch || 'detached HEAD'}</span>
  </div>

  <div class="flex flex-col gap-1.5">
    {#each commits as commit}
      {@const [hash, ...msgParts] = commit.split(' ')}
      <div class="flex items-baseline gap-2 text-[11px]">
        <span class="font-mono text-text-tertiary">{hash}</span>
        <span class="truncate text-text-secondary">{msgParts.join(' ')}</span>
      </div>
    {/each}
  </div>
</div>

<script lang="ts">
  import { tick } from 'svelte';
  import type { OutputEvent, WorkstationStatus } from './types';
  import { formatTime, stripAnsi } from './utils';

  let { logs = [], status = 'idle', loading = false }: { logs: OutputEvent[]; status?: WorkstationStatus; loading?: boolean } = $props();

  let emptyMessage = $derived(() => {
    if (status === 'running') return 'Connecting to live output...';
    if (loading) return 'Loading logs...';
    return 'No output was produced during this run.';
  });

  let container: HTMLDivElement;
  let autoScroll = $state(true);

  $effect(() => {
    if (logs.length && autoScroll && container) {
      tick().then(() => {
        container.scrollTop = container.scrollHeight;
      });
    }
  });

  function handleScroll() {
    if (!container) return;
    const { scrollTop, scrollHeight, clientHeight } = container;
    // If we are within 10px of the bottom, enable auto-scroll
    autoScroll = Math.abs(scrollHeight - clientHeight - scrollTop) < 10;
  }
</script>

<div class="flex flex-col h-full bg-bg-surface overflow-hidden">
  <div class="flex items-center justify-between px-3 py-1.5 border-b border-border-default bg-bg-surface-elevated">
    <span class="text-[11px] font-medium text-text-secondary">Logs</span>
    <label class="flex items-center gap-1.5 text-[10px] text-text-tertiary cursor-pointer">
      <input type="checkbox" bind:checked={autoScroll} class="rounded border-border-strong bg-bg-primary text-accent-primary focus:ring-accent-primary" />
      Auto-scroll
    </label>
  </div>
  <div 
    bind:this={container}
    onscroll={handleScroll}
    class="flex-1 overflow-y-auto p-3 font-mono text-[11px] leading-relaxed"
  >
    {#if logs.length === 0}
      <div class="flex h-full items-center justify-center">
        <div class="flex items-center gap-2 text-text-tertiary animate-pulse">
          <span class="w-1.5 h-1.5 rounded-full bg-text-tertiary"></span>
          <span class="w-1.5 h-1.5 rounded-full bg-text-tertiary animation-delay-150"></span>
          <span class="w-1.5 h-1.5 rounded-full bg-text-tertiary animation-delay-300"></span>
          <span class="ml-2 italic">{emptyMessage()}</span>
        </div>
      </div>
    {:else}
      {#each logs as log}
        <div class="flex gap-2 whitespace-pre-wrap break-words {log.stream === 'stderr' ? 'text-status-warning-text' : 'text-text-secondary'} hover:bg-bg-surface-hover transition-colors">
          <span class="shrink-0 text-text-tertiary select-none opacity-50 text-[10px] w-16 tabular-nums">{formatTime(log.timestamp)}</span>
          <span class="flex-1">{stripAnsi(log.line)}</span>
        </div>
      {/each}
    {/if}
  </div>
</div>

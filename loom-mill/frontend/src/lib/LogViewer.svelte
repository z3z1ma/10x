<script lang="ts">
  import { tick } from 'svelte';
  import type { OutputEvent } from './types';

  let { logs = [] }: { logs: OutputEvent[] } = $props();

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

  function formatTime(iso: string): string {
    if (!iso) return '';
    try {
      return new Date(iso).toLocaleTimeString('en-US', {
        hour12: false,
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
      });
    } catch {
      return '';
    }
  }

  function stripAnsi(text: string): string {
    return text.replace(/\x1b\[[0-9;]*[a-zA-Z]/g, '');
  }
</script>

<div class="flex flex-col h-full border border-border-default bg-bg-surface rounded-md overflow-hidden">
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
      <div class="text-text-tertiary italic">Waiting for output...</div>
    {:else}
      {#each logs as log}
        <div class="flex gap-2 whitespace-pre-wrap break-words {log.stream === 'stderr' ? 'text-status-warning-text' : 'text-text-secondary'}">
          <span class="shrink-0 text-text-tertiary select-none opacity-50 text-[10px] w-16 tabular-nums">{formatTime(log.timestamp)}</span>
          <span class="flex-1">{stripAnsi(log.line)}</span>
        </div>
      {/each}
    {/if}
  </div>
</div>

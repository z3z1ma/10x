<script lang="ts">
  import type { LoomRecord } from '../types';

  let { 
    record, 
    selected, 
    ready, 
    onclick 
  }: { 
    record: LoomRecord; 
    selected: boolean; 
    ready: boolean; 
    onclick: () => void;
  } = $props();

  let statusColor = $derived(() => {
    const status = record.metadata.status?.toLowerCase() || '';
    if (['closed', 'accepted', 'completed'].includes(status)) return 'bg-[#22c55e]';
    if (['active'].includes(status)) return 'bg-[#3b82f6]';
    if (['open', 'draft'].includes(status)) return 'bg-[#f59e0b]';
    if (['blocked'].includes(status)) return 'bg-[#ef4444]';
    if (['cancelled', 'retired', 'superseded'].includes(status)) return 'bg-[#6b7280]';
    return 'bg-border-strong'; // default
  });

  let title = $derived(() => {
    if (record.headings && record.headings.length > 0) {
      return record.headings[0][1];
    }
    if (record.metadata.id) {
      return record.metadata.id;
    }
    return record.path.split('/').pop() || record.path;
  });
</script>

<button 
  class="w-full text-left px-2 py-1.5 flex items-center gap-2 rounded text-[11px] transition-colors
         {selected ? 'bg-bg-surface-active text-text-primary ring-1 ring-border-strong' : 'hover:bg-bg-surface-hover text-text-secondary'}"
  {onclick}
>
  <div class="w-2 h-2 rounded-full shrink-0 {statusColor()}"></div>
  <span class="truncate flex-1">{title()}</span>
  {#if ready}
    <span class="text-[#22c55e] shrink-0 font-bold">✓</span>
  {/if}
</button>

<script lang="ts">
  import type { LoomRecord, WorkstationState } from './types';
  import WorkstationRow from './WorkstationRow.svelte';

  let { 
    records, 
    workstations,
    selectedId,
    onSelect
  }: { 
    records: LoomRecord[]; 
    workstations: Record<string, WorkstationState>;
    selectedId: string | null;
    onSelect: (id: string) => void;
  } = $props();

  let expanded = $state(false);

  let activeWorkstations = $derived(() => {
    const active: { id: string; record?: LoomRecord; state: WorkstationState }[] = [];
    for (const [id, state] of Object.entries(workstations)) {
      if (state.status === 'running' || state.status === 'paused' || state.status === 'idle') {
        const record = records.find(r => r.metadata.id === `ticket:${id}`);
        active.push({ id, record, state });
      }
    }
    return active;
  });

  let completedWorkstations = $derived(() => {
    const completed: { id: string; record?: LoomRecord; state: WorkstationState }[] = [];
    for (const [id, state] of Object.entries(workstations)) {
      if (state.status === 'completed' || state.status === 'stopped') {
        const record = records.find(r => r.metadata.id === `ticket:${id}`);
        completed.push({ id, record, state });
      }
    }
    return completed;
  });
</script>

<div class="flex flex-col h-full bg-bg-surface">
  <!-- List header with WIP indicator -->
  <div class="flex items-center justify-between px-3 py-2 border-b border-border-default shrink-0">
    <span class="text-[11px] font-medium text-text-secondary uppercase tracking-wider">Workstations</span>
    <span class="text-[10px] text-text-tertiary">{activeWorkstations().length}/3 WIP</span>
  </div>
  
  <div class="flex-1 overflow-y-auto">
    <!-- Active workstations -->
    {#each activeWorkstations() as ws (ws.id)}
      <WorkstationRow 
        ticketId={ws.id} 
        record={ws.record} 
        workstation={ws.state} 
        selected={selectedId === ws.id} 
        onSelect={() => onSelect(ws.id)} 
      />
    {/each}
    
    <!-- Completed section (collapsible) -->
    {#if completedWorkstations().length > 0}
      <button class="flex items-center gap-2 px-3 py-1.5 w-full text-left border-t border-border-subtle hover:bg-bg-surface-elevated transition-colors" onclick={() => expanded = !expanded}>
        <span class="text-[10px] text-text-tertiary">Completed ({completedWorkstations().length})</span>
        <span class="text-[10px] text-text-tertiary">{expanded ? '▾' : '▸'}</span>
      </button>
      {#if expanded}
        {#each completedWorkstations() as ws (ws.id)}
          <WorkstationRow 
            ticketId={ws.id} 
            record={ws.record} 
            workstation={ws.state} 
            selected={selectedId === ws.id} 
            dimmed={true}
            onSelect={() => onSelect(ws.id)} 
          />
        {/each}
      {/if}
    {/if}
  </div>
</div>
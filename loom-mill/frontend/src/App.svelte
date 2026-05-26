<script lang="ts">
  import { onMount } from 'svelte';
  import { store } from './lib/ws.svelte';
  import StatusBar from './lib/StatusBar.svelte';
  import WorkstationList from './lib/WorkstationList.svelte';
  import DetailPanel from './lib/DetailPanel.svelte';
  import ThemeToggle from './lib/ThemeToggle.svelte';

  let selectedWorkstationId = $state<string | null>(null);

  onMount(() => {
    store.connect();
  });

  $effect(() => {
    document.title = `Loom Mill - ${store.connected ? 'Connected' : 'Disconnected'}`;
  });

  let activeCount = $derived(Object.values(store.state.workstations).filter(ws => ws.status === 'running' || ws.status === 'paused').length);
  let shippedCount = $derived(store.state.shipping_events.filter(e => e.action === 'merged').length);
  
  let andonCount = $derived(() => {
    let count = 0;
    for (const events of Object.values(store.state.andon_events)) {
      count += events.length;
    }
    return count;
  });

  let avgDuration = $derived(() => {
    let total = 0;
    let count = 0;
    for (const ws of Object.values(store.state.workstations)) {
      if (ws.iteration_summary?.duration_seconds) {
        total += ws.iteration_summary.duration_seconds;
        count++;
      }
    }
    if (count === 0) return '—';
    const avg = total / count;
    if (avg < 60) return `${Math.floor(avg)}s`;
    return `${Math.floor(avg / 60)}m ${Math.floor(avg % 60)}s`;
  });
</script>

<main class="flex h-screen flex-col bg-bg-primary text-text-primary overflow-hidden font-sans">
  <!-- Header: 48px -->
  <header class="flex items-center justify-between h-12 border-b border-border-default bg-bg-surface px-4 shrink-0">
    <div class="flex items-center gap-2">
      <h1 class="text-[13px] font-semibold text-text-primary">Loom Mill</h1>
    </div>
    
    <StatusBar records={store.state.records} workstations={store.state.workstations} />
    
    <div class="flex items-center gap-3">
      <div class="flex items-center gap-2 text-[11px] font-medium">
        <span class="relative flex h-2 w-2">
          {#if store.connected}
            <span class="absolute inline-flex h-full w-full animate-ping rounded-full bg-status-success-text opacity-75"></span>
            <span class="relative inline-flex h-2 w-2 rounded-full bg-status-success-text"></span>
          {:else}
            <span class="relative inline-flex h-2 w-2 rounded-full bg-status-error-text"></span>
          {/if}
        </span>
      </div>
      <div class="h-4 w-[1px] bg-border-default"></div>
      <ThemeToggle />
      <button title="Settings" class="text-text-tertiary hover:text-text-primary transition-colors">
        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"></path><circle cx="12" cy="12" r="3"></circle></svg>
      </button>
    </div>
  </header>

  <!-- Main: flex row -->
  <div class="flex flex-1 overflow-hidden">
    <div class="w-80 shrink-0 border-r border-border-default">
      <WorkstationList 
        records={store.state.records} 
        workstations={store.state.workstations} 
        selectedId={selectedWorkstationId}
        onSelect={(id) => selectedWorkstationId = id}
      />
    </div>
    <div class="flex-1 min-w-0">
      <DetailPanel 
        selectedId={selectedWorkstationId}
        workstation={selectedWorkstationId ? store.state.workstations[selectedWorkstationId] : undefined}
      />
    </div>
  </div>

  <!-- Footer: 32px -->
  <footer class="flex items-center justify-between h-8 border-t border-border-default bg-bg-surface px-4 text-[10px] text-text-tertiary shrink-0">
    <div class="flex items-center gap-4">
      <span>WIP: {activeCount}/3</span>
      <span>Shipped: {shippedCount} today</span>
      <span>Avg iteration: {avgDuration()}</span>
    </div>
    <div class="flex items-center gap-4">
      {#if andonCount() > 0}
        <span class="text-status-error-text font-medium">⚠ {andonCount()} alert{andonCount() > 1 ? 's' : ''}</span>
      {/if}
    </div>
  </footer>
</main>
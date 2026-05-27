<script lang="ts">
  import type { StagedRecord } from '../types';
  import { apiUrl } from '../api';
  import { store } from '../ws.svelte.ts';

  let { proposal, sessionId }: { proposal: StagedRecord, sessionId: string } = $props();

  let expanded = $state(false);
  let editing = $state(false);
  let editContent = $state('');
  let saving = $state(false);

  function surfaceColor(surface: string) {
    switch (surface) {
      case 'tickets': return 'bg-blue-500/20 text-blue-400 border-blue-500/30';
      case 'specs': return 'bg-purple-500/20 text-purple-400 border-purple-500/30';
      case 'plans': return 'bg-emerald-500/20 text-emerald-400 border-emerald-500/30';
      case 'research': return 'bg-amber-500/20 text-amber-400 border-amber-500/30';
      default: return 'bg-gray-500/20 text-gray-400 border-gray-500/30';
    }
  }

  function surfaceIcon(surface: string) {
    switch (surface) {
      case 'tickets': return '🎫';
      case 'specs': return '📐';
      case 'plans': return '📊';
      case 'research': return '🔬';
      default: return '📄';
    }
  }

  let previewContent = $derived(() => {
    const lines = proposal.content.split('\n');
    return lines.slice(0, 8).join('\n') + (lines.length > 8 ? '\n...' : '');
  });

  async function handleAction(action: 'accept' | 'reject') {
    try {
      const url = action === 'accept' 
        ? apiUrl(`/shaping/sessions/${sessionId}/staged/${proposal.temp_id}/accept`)
        : apiUrl(`/shaping/sessions/${sessionId}/staged/${proposal.temp_id}`);
        
      const response = await fetch(url, {
        method: action === 'accept' ? 'POST' : 'DELETE'
      });
      
      if (response.ok) {
        // Refetch session state to sync staged records
        const stateRes = await fetch(apiUrl(`/shaping/sessions/${sessionId}`));
        if (stateRes.ok) {
          const data = await stateRes.json();
          if (data.state && store.shapingSession) {
            store.shapingSession.stagedRecords = data.state.staged_records || [];
          }
        }
      }
    } catch (err) {
      console.error(`Failed to ${action} proposal:`, err);
    }
  }

  async function handleSaveEdit() {
    saving = true;
    try {
      const response = await fetch(apiUrl(`/shaping/sessions/${sessionId}/staged/${proposal.temp_id}`), {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ content: editContent })
      });
      
      if (response.ok) {
        editing = false;
        // Refetch session state to sync staged records
        const stateRes = await fetch(apiUrl(`/shaping/sessions/${sessionId}`));
        if (stateRes.ok) {
          const data = await stateRes.json();
          if (data.state && store.shapingSession) {
            store.shapingSession.stagedRecords = data.state.staged_records || [];
          }
        }
      }
    } catch (err) {
      console.error('Failed to save edit:', err);
    } finally {
      saving = false;
    }
  }
</script>

<div data-temp-id={proposal.temp_id} class="border border-border-default rounded-lg bg-bg-surface overflow-hidden flex flex-col transition-all shadow-md {proposal.status === 'accepted' ? 'border-l-4 border-l-status-success-border ring-1 ring-status-success-border/30' : ''} {proposal.status === 'rejected' ? 'opacity-50 grayscale' : ''}">
  <!-- Header -->
  <div class="flex items-center justify-between p-3 border-b border-border-subtle bg-bg-surface-hover">
    <div class="flex items-center gap-3">
      <span class="px-2.5 py-1 text-[11px] font-medium rounded-md border {surfaceColor(proposal.surface)} flex items-center gap-1.5 shadow-sm">
        <span>{surfaceIcon(proposal.surface)}</span>
        <span class="capitalize">{proposal.surface}</span>
      </span>
      <span class="text-[13px] font-semibold text-text-primary truncate max-w-[250px]" title={proposal.title}>
        {proposal.title}
      </span>
    </div>
    <div class="text-[10px] text-text-tertiary font-mono bg-bg-primary px-2 py-1 rounded border border-border-subtle">
      {proposal.temp_id}
    </div>
  </div>

  <!-- Content -->
  <div class="p-4 bg-bg-primary">
    {#if editing}
      <div class="flex flex-col gap-3 animate-in fade-in duration-200">
        <textarea 
          bind:value={editContent}
          class="w-full h-64 p-3 rounded-md border border-accent-primary/50 bg-[#0d1117] text-[12px] text-text-primary font-mono resize-y focus:outline-none focus:border-accent-primary shadow-inner"
        ></textarea>
        <div class="flex justify-end gap-2">
          <button 
            class="px-4 py-1.5 text-[12px] rounded-md hover:bg-bg-surface-hover text-text-secondary border border-transparent hover:border-border-default transition-all"
            onclick={() => { editing = false; editContent = proposal.content; }}
          >
            Cancel
          </button>
          <button 
            class="px-4 py-1.5 text-[12px] rounded-md bg-accent-primary text-white hover:bg-accent-primary/90 disabled:opacity-50 transition-all shadow-sm font-medium"
            onclick={handleSaveEdit}
            disabled={saving || editContent === proposal.content}
          >
            {saving ? 'Saving...' : 'Save Changes'}
          </button>
        </div>
      </div>
    {:else}
      <div class="text-[12px] font-mono text-text-secondary whitespace-pre-wrap relative leading-relaxed">
        {expanded ? proposal.content : previewContent()}
        
        {#if proposal.content.split('\n').length > 8}
          <div class="absolute bottom-0 left-0 w-full h-12 bg-gradient-to-t from-bg-primary to-transparent pointer-events-none {expanded ? 'hidden' : ''}"></div>
          <button 
            class="absolute bottom-0 right-0 bg-bg-surface px-3 py-1 text-[11px] font-medium text-accent-primary hover:text-accent-primary-hover rounded-md shadow-sm border border-border-subtle transition-all hover:scale-105"
            onclick={() => expanded = !expanded}
          >
            {expanded ? 'Show less' : 'Show full content'}
          </button>
        {/if}
      </div>
    {/if}
  </div>

  <!-- Actions -->
  {#if proposal.status === 'proposed' && !editing}
    <div class="flex items-center gap-3 p-3 border-t border-border-subtle bg-bg-surface">
      <button 
        class="flex-1 py-2 text-[12px] font-medium rounded-md bg-status-success-bg/10 text-status-success-text hover:bg-status-success-bg/20 border border-status-success-border/30 transition-all hover:scale-[1.02] shadow-sm flex items-center justify-center gap-2"
        onclick={() => handleAction('accept')}
      >
        <span class="text-[14px]">✓</span> Accept
      </button>
      <button 
        class="flex-1 py-2 text-[12px] font-medium rounded-md bg-status-error-bg/10 text-status-error-text hover:bg-status-error-bg/20 border border-status-error-border/30 transition-all hover:scale-[1.02] shadow-sm flex items-center justify-center gap-2"
        onclick={() => handleAction('reject')}
      >
        <span class="text-[14px]">✗</span> Reject
      </button>
      <button 
        class="flex-1 py-2 text-[12px] font-medium rounded-md bg-bg-primary text-text-secondary hover:text-text-primary border border-border-default transition-all hover:scale-[1.02] shadow-sm flex items-center justify-center gap-2"
        onclick={() => { editContent = proposal.content; editing = true; }}
      >
        <span class="text-[14px]">✎</span> Edit
      </button>
    </div>
  {:else if proposal.status !== 'proposed' && !editing}
    <div class="flex items-center justify-between p-3 border-t border-border-subtle bg-bg-surface">
      <span class="text-[12px] font-medium flex items-center gap-2 {proposal.status === 'accepted' ? 'text-status-success-text' : 'text-status-error-text'}">
        <span class="text-[14px]">{proposal.status === 'accepted' ? '✓' : '✗'}</span>
        {proposal.status === 'accepted' ? 'Accepted' : 'Rejected'}
      </span>
      <button 
        class="text-[11px] text-text-tertiary hover:text-text-secondary underline px-2 py-1 rounded hover:bg-bg-primary transition-colors"
        onclick={() => handleAction('proposed' as any)} // Reset to proposed
      >
        Undo
      </button>
    </div>
  {/if}
</div>

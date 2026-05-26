<script lang="ts">
  import type { LoomRecord, WorkstationState } from './types';
  import WorkstationControls from './WorkstationControls.svelte';
  import { formatRelativeTime } from './utils';

  let { record, workstation }: { record: LoomRecord; workstation?: WorkstationState } = $props();

  // The parser now captures #, ##, and ### headings.
  // The first heading is usually the title.
  let title = $derived(record.headings.length > 0 ? record.headings[0][1] : record.path.split('/').pop() || 'Unknown');
  let id = $derived(record.metadata.id?.replace('ticket:', '') || 'unknown');
  let status = $derived(record.metadata.status || 'unknown');
  let updated = $derived(record.metadata.updated || record.metadata.created || '');

  // Find linked evidence and audit
  let hasEvidence = $derived(record.references.some(ref => ref.includes('evidence:')));
  let hasAudit = $derived(record.references.some(ref => ref.includes('audit:')));
  let hasAndon = $derived(Boolean(workstation?.andon?.active));
  let hasBackpressure = $derived(Boolean(workstation?.backpressure_signals?.length));
</script>

<div class="flex flex-col gap-2 rounded-md border {hasAndon ? 'border-status-error-border bg-status-error-bg' : 'border-border-default bg-bg-surface-elevated'} p-3 shadow-sm transition-colors hover:border-border-strong">
  <div class="flex items-start justify-between gap-2">
    <span class="text-[11px] font-mono text-text-tertiary">{id}</span>
    <div class="flex items-center gap-1.5">
      {#if hasAndon}
        <span class="badge bg-status-error-bg text-status-error-text ring-1 ring-inset ring-status-error-border" title="Andon active">andon</span>
      {:else if hasBackpressure}
        <span class="badge bg-status-warning-bg text-status-warning-text ring-1 ring-inset ring-status-warning-border" title="Backpressure warning">backpressure</span>
      {/if}
      <span class="badge ring-1 ring-inset
        {status === 'active' ? 'bg-status-info-bg text-status-info-text ring-status-info-border' :
         status === 'blocked' ? 'bg-status-error-bg text-status-error-text ring-status-error-border' :
         status === 'review' ? 'bg-status-warning-bg text-status-warning-text ring-status-warning-border' :
         status === 'closed' ? 'bg-status-neutral-bg text-status-neutral-text ring-status-neutral-border' :
         'bg-status-neutral-bg text-status-neutral-text ring-status-neutral-border'}">
        {status}
      </span>
    </div>
  </div>
  
  <h3 class="text-sm font-medium text-text-primary leading-tight line-clamp-2">{title}</h3>

  <WorkstationControls ticketId={id} workstation={workstation} />

  <div class="mt-1 flex items-center justify-between text-[10px] text-text-tertiary">
    <div class="flex gap-1.5">
      {#if hasEvidence}
        <span class="flex h-4 w-4 items-center justify-center rounded bg-accent-subtle text-accent-text" title="Has Evidence">E</span>
      {/if}
      {#if hasAudit}
        <span class="flex h-4 w-4 items-center justify-center rounded bg-accent-subtle text-accent-text" title="Has Audit">A</span>
      {/if}
    </div>
    {#if updated}
      <span title={updated}>{formatRelativeTime(updated)}</span>
    {/if}
  </div>
</div>

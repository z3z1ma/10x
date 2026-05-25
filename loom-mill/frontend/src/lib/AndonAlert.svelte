<script lang="ts">
  import type { LoomRecord, WorkstationState } from './types';

  let { records, workstations }: { records: LoomRecord[]; workstations: Record<string, WorkstationState> } = $props();

  const apiBase = `${window.location.protocol}//${window.location.hostname}:8765`;
  let busy = $state<Record<string, boolean>>({});
  let errors = $state<Record<string, string>>({});

  let alerts = $derived(
    Object.entries(workstations)
      .filter(([, workstation]) => workstation.andon?.active || workstation.backpressure_signals?.length)
      .map(([ticketId, workstation]) => ({
        ticketId,
        workstation,
        record: records.find(record => record.metadata.id?.replace('ticket:', '') === ticketId)
      }))
  );

  async function acknowledge(ticketId: string) {
    busy[ticketId] = true;
    errors[ticketId] = '';
    const response = await fetch(`${apiBase}/api/workstation/${ticketId}/acknowledge-andon`, { method: 'POST' });
    busy[ticketId] = false;
    if (!response.ok) {
      const data = await response.json();
      errors[ticketId] = data.error || 'Failed to acknowledge andon';
    }
  }
</script>

{#if alerts.length}
  <section class="space-y-3">
    {#each alerts as alert (alert.ticketId)}
      <div class="rounded-lg border border-status-error-border bg-status-error-bg p-4 shadow-sm">
        <div class="flex items-start justify-between gap-4">
          <div>
            <p class="text-[10px] font-semibold uppercase tracking-wider text-status-error-text">Andon</p>
            <h2 class="mt-1 text-sm font-medium text-text-primary">
              {alert.record?.headings[0]?.[1] || alert.ticketId}
            </h2>
            <p class="mt-1 text-[11px] text-text-secondary">Ticket: {alert.ticketId} · Iteration history: .mill/patterns/{alert.ticketId}.json</p>
          </div>
          {#if alert.workstation.andon?.active}
            <button type="button" onclick={() => acknowledge(alert.ticketId)} disabled={busy[alert.ticketId]} class="rounded-md bg-status-error-text px-2.5 py-1.5 text-[11px] font-medium text-white hover:opacity-90 disabled:cursor-not-allowed disabled:opacity-50 transition-opacity">
              Acknowledge
            </button>
          {/if}
        </div>

        <div class="mt-3 space-y-2">
          {#each alert.workstation.backpressure_signals as signal}
            <div class="rounded-md border border-border-subtle bg-bg-surface p-3">
              <div class="flex flex-wrap items-center gap-2 text-[10px]">
                <span class="rounded-full bg-status-error-bg px-1.5 py-0.5 font-mono text-status-error-text ring-1 ring-inset ring-status-error-border">{signal.kind}</span>
                <span class="rounded-full bg-status-warning-bg px-1.5 py-0.5 font-medium text-status-warning-text ring-1 ring-inset ring-status-warning-border">{signal.severity}</span>
                <span class="text-text-secondary">Iteration {signal.iteration_index + 1}</span>
                {#if signal.exit_code !== null}<span class="text-text-tertiary">Exit {signal.exit_code}</span>{/if}
                {#if signal.duration_seconds !== null}<span class="text-text-tertiary">{signal.duration_seconds.toFixed(1)}s</span>{/if}
              </div>
              <p class="mt-2 text-xs text-text-primary">{signal.message}</p>
              {#if signal.output_tail}
                <pre class="mt-2 max-h-28 overflow-auto rounded bg-bg-primary p-2 text-[10px] text-text-secondary border border-border-subtle">{signal.output_tail}</pre>
              {/if}
            </div>
          {/each}
        </div>

        {#if errors[alert.ticketId]}
          <p class="mt-2 text-[11px] text-status-error-text">{errors[alert.ticketId]}</p>
        {/if}
      </div>
    {/each}
  </section>
{/if}

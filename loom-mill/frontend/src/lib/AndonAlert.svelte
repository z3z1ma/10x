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
      <div class="rounded-xl border border-rose-500/40 bg-rose-950/60 p-4 shadow-lg shadow-rose-950/30">
        <div class="flex items-start justify-between gap-4">
          <div>
            <p class="text-xs font-semibold uppercase tracking-[0.2em] text-rose-300">Andon</p>
            <h2 class="mt-1 text-base font-semibold text-rose-50">
              {alert.record?.headings[0]?.[1] || alert.ticketId}
            </h2>
            <p class="mt-1 text-xs text-rose-200/80">Ticket: {alert.ticketId} · Iteration history: .mill/patterns/{alert.ticketId}.json</p>
          </div>
          {#if alert.workstation.andon?.active}
            <button type="button" onclick={() => acknowledge(alert.ticketId)} disabled={busy[alert.ticketId]} class="rounded bg-rose-100 px-3 py-1.5 text-xs font-semibold text-rose-950 hover:bg-white disabled:cursor-not-allowed disabled:bg-rose-900 disabled:text-rose-300">
              Acknowledge
            </button>
          {/if}
        </div>

        <div class="mt-3 space-y-2">
          {#each alert.workstation.backpressure_signals as signal}
            <div class="rounded-lg border border-rose-400/20 bg-slate-950/60 p-3">
              <div class="flex flex-wrap items-center gap-2 text-xs">
                <span class="rounded bg-rose-500/20 px-2 py-0.5 font-mono text-rose-100">{signal.kind}</span>
                <span class="rounded bg-amber-500/15 px-2 py-0.5 font-medium text-amber-200">{signal.severity}</span>
                <span class="text-rose-100">Iteration {signal.iteration_index + 1}</span>
                {#if signal.exit_code !== null}<span class="text-rose-200/70">Exit {signal.exit_code}</span>{/if}
                {#if signal.duration_seconds !== null}<span class="text-rose-200/70">{signal.duration_seconds.toFixed(1)}s</span>{/if}
              </div>
              <p class="mt-2 text-sm text-rose-50">{signal.message}</p>
              {#if signal.output_tail}
                <pre class="mt-2 max-h-28 overflow-auto rounded bg-black/40 p-2 text-xs text-rose-100">{signal.output_tail}</pre>
              {/if}
            </div>
          {/each}
        </div>

        {#if errors[alert.ticketId]}
          <p class="mt-2 text-xs text-rose-200">{errors[alert.ticketId]}</p>
        {/if}
      </div>
    {/each}
  </section>
{/if}

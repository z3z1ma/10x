<script lang="ts">
  import type { LoomRecord, WorkstationState } from './types';
  import TicketCard from './TicketCard.svelte';

  let { records, workstations }: { records: LoomRecord[]; workstations: Record<string, WorkstationState> } = $props();

  let tickets = $derived(records.filter(r => r.metadata.type?.toLowerCase() === 'ticket' || r.path.includes('tickets/')));

  let columns = ['open', 'active', 'blocked', 'review', 'closed'];

  let groupedTickets = $derived(() => {
    const groups: Record<string, LoomRecord[]> = {
      open: [],
      active: [],
      blocked: [],
      review: [],
      closed: [],
      other: []
    };

    for (const ticket of tickets) {
      const status = ticket.metadata.status?.toLowerCase() || 'open';
      if (groups[status]) {
        groups[status].push(ticket);
      } else {
        groups.other.push(ticket);
      }
    }

    return groups;
  });
</script>

<div class="flex h-full gap-4 overflow-x-auto pb-4">
  {#each columns as col}
    <div class="flex w-80 shrink-0 flex-col gap-3 rounded-lg bg-bg-surface p-3 border border-border-subtle">
      <div class="flex items-center justify-between px-1">
        <h2 class="text-[11px] font-medium text-text-secondary uppercase tracking-wider">{col}</h2>
        <span class="rounded-full bg-bg-surface-active px-2 py-0.5 text-[10px] font-medium text-text-secondary border border-border-subtle">
          {groupedTickets()[col].length}
        </span>
      </div>
      
      <div class="flex flex-col gap-2 overflow-y-auto">
        {#each groupedTickets()[col] as ticket (ticket.path)}
          <TicketCard record={ticket} workstation={workstations[ticket.metadata.id?.replace('ticket:', '') || '']} />
        {/each}
      </div>
    </div>
  {/each}
</div>

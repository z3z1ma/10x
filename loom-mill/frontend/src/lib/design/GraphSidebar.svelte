<script lang="ts">
  import type { LoomRecord } from '../types';
  import NewRecordDropdown from './NewRecordDropdown.svelte';
  import RecordNode from './RecordNode.svelte';

  let { 
    records, 
    selectedId, 
    onSelect, 
    onCreateRecord 
  }: { 
    records: LoomRecord[]; 
    selectedId: string | null; 
    onSelect: (id: string) => void; 
    onCreateRecord: (surface: string) => void;
  } = $props();

  const sections = [
    { id: 'specs', label: 'Specs', icon: '📐' },
    { id: 'plans', label: 'Plans', icon: '📊' },
    { id: 'tickets', label: 'Tickets', icon: '🎫' },
    { id: 'research', label: 'Research', icon: '🔬' },
    { id: 'knowledge', label: 'Knowledge', icon: '💡' },
    { id: 'evidence', label: 'Evidence', icon: '✓' },
    { id: 'audit', label: 'Audit', icon: '🔍' },
    { id: 'constitution', label: 'Constitution', icon: '📋' }
  ];

  let collapsedSections = $state<Record<string, boolean>>({});

  function toggleSection(id: string) {
    collapsedSections[id] = !collapsedSections[id];
  }

  function isReadyToFab(record: LoomRecord, allRecords: LoomRecord[]): boolean {
    if (record.surface !== 'tickets') return false;
    if (record.metadata.status?.toLowerCase() !== 'open') return false;
    
    // Check dependencies
    if (record.metadata.depends_on && record.metadata.depends_on.length > 0) {
      for (const depId of record.metadata.depends_on) {
        const depRecord = allRecords.find(r => r.metadata.id === depId);
        if (!depRecord || depRecord.metadata.status?.toLowerCase() !== 'closed') {
          return false;
        }
      }
    }

    // Check ACC-* labels
    if (!record.labeled_ids || !record.labeled_ids.some(id => id.startsWith('ACC-'))) {
      return false;
    }

    return true;
  }

  let groupedRecords = $derived(() => {
    const grouped: Record<string, LoomRecord[]> = {};
    for (const section of sections) {
      grouped[section.id] = [];
    }
    
    for (const record of records) {
      const surface = record.surface || 'unknown';
      if (grouped[surface]) {
        grouped[surface].push(record);
      }
    }
    
    return grouped;
  });
</script>

<div class="flex flex-col h-full">
  <div class="flex items-center justify-between p-3 border-b border-border-default shrink-0">
    <span class="font-medium text-text-secondary text-[11px] uppercase tracking-wider">Records</span>
    <NewRecordDropdown onSelect={onCreateRecord} />
  </div>

  <div class="flex-1 overflow-y-auto p-2 space-y-4">
    {#each sections as section}
      {@const sectionRecords = groupedRecords()[section.id] || []}
      {#if sectionRecords.length > 0}
        <div class="flex flex-col gap-1">
          <button 
            class="flex items-center justify-between w-full text-left px-2 py-1 text-[11px] text-text-tertiary hover:text-text-secondary transition-colors"
            onclick={() => toggleSection(section.id)}
          >
            <div class="flex items-center gap-2">
              <span>{section.icon}</span>
              <span class="font-medium uppercase tracking-wider">{section.label}</span>
            </div>
            <div class="flex items-center gap-2">
              <span>{sectionRecords.length}</span>
              <span class="transform transition-transform {collapsedSections[section.id] ? '-rotate-90' : ''}">▼</span>
            </div>
          </button>
          
          {#if !collapsedSections[section.id]}
            <div class="flex flex-col gap-0.5 pl-2">
              {#each sectionRecords as record}
                <RecordNode 
                  {record} 
                  selected={selectedId === record.path} 
                  ready={isReadyToFab(record, records)}
                  onclick={() => onSelect(record.path)} 
                />
              {/each}
            </div>
          {/if}
        </div>
      {/if}
    {/each}
  </div>
</div>

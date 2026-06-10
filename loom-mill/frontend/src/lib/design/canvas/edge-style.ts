import { readable } from 'svelte/store';

// Svelvet's <Anchor> expects `edgeColor` to be a Svelte store (Writable/Readable),
// not a plain string. Passing a string silently breaks edge creation so no lines
// render at all. These shared readable stores hold the constant edge colors.
export const causalEdgeColor = readable('#52525b'); // zinc-600, neutral causal edges
export const branchEdgeColor = readable('#a78bfa'); // violet-400, option/branch edges

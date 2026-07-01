import { exportVisibleRows } from "./visibleRows.js";

const csv = exportVisibleRows([
  { id: "r_1", label: "Alpha", selected: false, visible: true },
  { id: "r_2", label: "Beta", selected: true, visible: false },
  { id: "r_3", label: "Gamma", selected: true, visible: true, policyHidden: true },
]);

const expected = "row_id,label\nr_1,Alpha";

if (csv !== expected) {
  throw new Error(`unexpected csv: ${csv}`);
}

console.log("visibleRows.test.js passed");

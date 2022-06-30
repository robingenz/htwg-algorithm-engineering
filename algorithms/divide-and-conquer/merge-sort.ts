/**
 * Merge Sort
 *
 * Die Liste wird immer wieder halbiert bis nur noch ein Element übrig ist.
 * Anschließend wird die Liste wieder sortiert zusammen gesetzt.
 *
 * Annahme: Die Zahlen sind aufsteigend sortiert.
 *
 * Komplexität: O(n log n)
 */
const merge = (left: number[], right: number[]): number[] => {
  let items = [];
  while (left.length && right.length) {
    if (left[0] < right[0]) {
      items.push(left.shift());
    } else {
      items.push(right.shift());
    }
  }
  return [...items, ...left, ...right];
};

const mergeSort = (values: number[]): number[] => {
  if (values.length <= 1) {
    return values;
  }
  const midIdx = Math.floor(values.length / 2);
  const left = values.slice(0, midIdx);
  const right = values.slice(midIdx);
  return merge(mergeSort(left), mergeSort(right));
};

const values = [7, 2, 8, 17, 10, 13, 9, 21, 19];
const result = mergeSort(values);
console.log(`Sorted values: ${result}`);
export {};

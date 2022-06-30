/**
 * Recursive Search
 *
 * Die binäre Suche mit einem rekursiven Algorithmus implementiert.
 *
 * Annahme: Die Zahlen sind aufsteigend sortiert.
 *
 * Komplexität: O(log n)
 */
const recursiveSearch = (
  values: number[],
  target: number,
  leftIdx?: number,
  rightIdx?: number,
): number => {
  leftIdx = leftIdx || 0;
  rightIdx = rightIdx || values.length - 1;
  if (leftIdx > rightIdx) {
    return -1;
  }
  const midIdx = Math.floor((leftIdx + rightIdx) / 2);
  if (target === values[midIdx]) {
    return midIdx;
  } else if (target < values[midIdx]) {
    return recursiveSearch(values, target, leftIdx, midIdx - 1);
  } else {
    return recursiveSearch(values, target, midIdx + 1, rightIdx);
  }
};

const values = [2, 7, 8, 9, 10, 13, 17, 19, 21];
const result = recursiveSearch(values, values[2]);
console.log(`Index: ${result}`);
export {};

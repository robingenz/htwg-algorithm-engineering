/**
 * Rekursive Suche
 *
 * Die binäre Suche mit einem rekursiven Algorithmus implementiert.
 *
 * Komplexität: O(log n)
 */
const recursiveSearch = (
  values: number[],
  searchValue: number,
  left: number,
  right: number,
): number => {
  if (left > right) {
    return -1;
  }
  let mid = Math.floor((left + right) / 2);
  if (searchValue === values[mid]) {
    return mid;
  } else if (searchValue < values[mid]) {
    return recursiveSearch(values, searchValue, left, mid - 1);
  } else {
    return recursiveSearch(values, searchValue, mid + 1, right);
  }
};

const values = [2, 7, 8, 9, 10, 13, 17, 19, 21];
const result = recursiveSearch(values, values[2], 0, values.length - 0);
console.log(`Index: ${result}`);
export {};

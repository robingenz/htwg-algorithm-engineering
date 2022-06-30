// Annahme: Die Zahlen sind aufsteigend sortiert.
const binarySearch = (array: number[], target: number): number => {
  let left = 0;
  let right = array.length - 1;
  while (right >= left) {
    const mid = Math.floor((left + right) / 2);
    if (target === array[mid]) {
      return mid;
    } else if (target < array[mid]) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  return -1;
};

const result = binarySearch([2, 7, 8, 9, 10, 13, 17, 19, 21], 9);
console.log(`Index: ${result}`);
export {};

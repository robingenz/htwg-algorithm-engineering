const recursiveSearch = (values: number[], searchValue: number, left: number, right: number): number => {
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

const result = recursiveSearch([2, 7, 8, 9, 10, 13, 17, 19, 21], 8, 0, 8);
console.log(`Index: ${result}`);
export {};

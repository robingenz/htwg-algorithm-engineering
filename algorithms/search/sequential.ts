const sequentialSearch = (values: number[], searchValue: number): number => {
  for (let index = 0; index < values.length; index++) {
    if (values[index] === searchValue) {
      return index;
    }
  }
  return -1;
};

const result = sequentialSearch([1720, 1721, 979, 366, 299, 675, 1456], 979);
console.log(`Index: ${result}`);
export {};

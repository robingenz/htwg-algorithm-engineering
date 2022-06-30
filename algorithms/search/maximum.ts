const maximumSearch = (values: number[]): number => {
  let indexMaxValue = 0;
  let maxValue = values[0];
  for (let index = 0; index < values.length; index++) {
    if (values[index] > maxValue) {
      indexMaxValue = index;
      maxValue = values[index];
    }
  }
  return indexMaxValue;
};

const result = maximumSearch([1720, 1721, 979, 366, 299, 675, 1456]);
console.log(`Index: ${result}`);
export {};

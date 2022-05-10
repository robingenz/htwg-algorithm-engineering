const quickSort = (array) => {
  if (array.length <= 1) {
    return array;
  }
  const pivot = array[0];
  const left = [];
  const right = [];
  for (let i = 1; i < array.length; i++) {
    if (array[i] < pivot) {
      left.push(array[i]);
    } else {
      right.push(array[i]);
    }
  }
  return [...quickSort(left), pivot, ...quickSort(right)];
};

const result = quickSort([4, 8, 7, 2, 11, 1, 3]);
console.log(`Output: ${result}`);
export {};

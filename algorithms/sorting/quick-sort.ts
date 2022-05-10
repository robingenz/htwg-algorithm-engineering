const quickSort = (items) => {
  if (items.length <= 1) {
    return items;
  }
  const pivot = items[0];
  const left = [];
  const right = [];
  for (let i = 1; i < items.length; i++) {
    if (items[i] < pivot) {
      left.push(items[i]);
    } else {
      right.push(items[i]);
    }
  }
  return [...quickSort(left), pivot, ...quickSort(right)];
};

const result = quickSort([4, 8, 7, 2, 11, 1, 3]);
console.log(`Output: ${result}`);
export {};

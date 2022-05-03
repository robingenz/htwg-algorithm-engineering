const merge = (left, right) => {
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

const mergeSort = (items) => {
  if (items.length <= 1) {
    return items
  }
  const midIdx = Math.floor(items.length / 2);
  const left = items.slice(0, midIdx);
  const right = items.slice(midIdx);
  return merge(mergeSort(left), mergeSort(right));
};

const result = mergeSort([4, 8, 7, 2, 11, 1, 3]);
console.log(`Output: ${result}`);
export {};

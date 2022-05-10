const bubbleSort = (items) => {
  for (let i = 0; i < items.length; i++) {
    for (let j = 0; j < items.length - 1; j++) {
      if (items[j] > items[j + 1]) {
        const temp = items[j];
        items[j] = items[j + 1];
        items[j + 1] = temp;
      }
    }
  }
  return items;
};

const result = bubbleSort([4, 8, 7, 2, 11, 1, 3]);
console.log(`Output: ${result}`);
export {};

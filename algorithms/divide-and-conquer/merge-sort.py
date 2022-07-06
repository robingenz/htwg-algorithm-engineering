"""
Merge Sort

Die Liste wird immer wieder halbiert bis nur noch ein Element übrig ist.
Anschließend wird die Liste wieder sortiert zusammen gesetzt.

Annahme: Die Zahlen sind aufsteigend sortiert.

Komplexität: O(n log n)
"""


def merge(left: list, right: list) -> list:
    sortedValues: list = []
    while len(left) and len(right):
        if left[0] < right[0]:
            sortedValues.append(left.pop(0))
        else:
            sortedValues.append(right.pop(0))
    return sortedValues + left + right


def mergeSort(values: list) -> list:
    if len(values) < 2:
        return values
    midIdx = int(len(values)/2)
    left = values[:midIdx]
    right = values[midIdx:]
    return merge(mergeSort(left), mergeSort(right))


if __name__ == "__main__":
    print(mergeSort([7, 2, 8, 17, 10, 13, 9, 21, 19]))

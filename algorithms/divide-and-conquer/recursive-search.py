"""
Recursive Search

Die binäre Suche mit einem rekursiven Algorithmus implementiert.

Annahme: Die Zahlen sind aufsteigend sortiert.

Komplexität: O(log n)
"""


def recursiveSearch(values: list, target: int, leftIdx: int = None, rightIdx: int = None) -> int:
    if not leftIdx:
        leftIdx = 0
    if not rightIdx:
        rightIdx = len(values) - 1
    if leftIdx > rightIdx:
        return -1
    midIdx = int((rightIdx+leftIdx)/2)
    if values[midIdx] == target:
        return midIdx
    else:
        if values[midIdx] < target:
            return recursiveSearch(values, target, midIdx + 1, rightIdx)
        else:
            return recursiveSearch(values, target, leftIdx, midIdx-1)


if __name__ == "__main__":
    values = [2, 7, 8, 9, 10, 13, 17, 19, 21]
    print(recursiveSearch(values, values[2]))

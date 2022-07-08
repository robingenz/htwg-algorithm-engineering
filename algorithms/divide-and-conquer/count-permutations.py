"""
Anzahl von Vertauschungen

Zählt die Anzahl der vertauschen Paare in einer Liste.

Komplexität: O(n log n)
"""


def quickSortAndCount(values: list) -> tuple[list, int]:
    counter = 0
    if len(values) < 2:
        return values, counter
    pivot = values[0]
    right = []
    left = []
    for value in values[1:]:
        if value > pivot:
            right.append(value)
        else:
            counter = counter + 1
            left.append(value)
    result1 = quickSortAndCount(left)
    result2 = quickSortAndCount(right)
    return [result1[0] + [pivot] + result2[0], counter + result1[1] + result2[1]]


if __name__ == "__main__":
    print(quickSortAndCount([9, 4, 3, 7, 5, 6])[1])

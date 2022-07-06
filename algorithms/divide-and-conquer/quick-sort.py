"""
Quick Sort

Auswählen eines Pivot-Elements und sortieren der restlichen Elemente in ein "left" und ein "right" Array.

Komplexität: O(n^2)
"""


def quickSort(values: list) -> list:
    if len(values) < 2:
        return values
    pivot = values[0]
    right = []
    left = []
    for value in values[1:]:
        if value > pivot:
            right.append(value)
        else:
            left.append(value)
    return quickSort(left) + [pivot] + quickSort(right)


if __name__ == "__main__":
    print(quickSort([4, 8, 7, 2, 11, 1, 3]))

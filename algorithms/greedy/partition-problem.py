"""
Partitionsproblem

Komplexität: O(n)
"""


def main(values: list) -> tuple[list, list]:
    list1 = []
    list1_sum = 0
    list2 = []
    list2_sum = 0
    half_sum = int(sum(values)/2)
    for value in values:
        if list1_sum + value <= half_sum:
            list1.append(value)
            list1_sum += value
        else:
            list2.append(value)
            list2_sum += value
    return [list1, list2]


if __name__ == "__main__":
    print(main([3, 4, 1, 1, 2, 1]))

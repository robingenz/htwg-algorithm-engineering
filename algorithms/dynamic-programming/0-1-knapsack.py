"""
Das 0-1-Rucksackproblem

Jeder Gegenstand muss entweder vollständig oder überhaupt nicht genommen werden.

Komplexität: O(n*G)
"""


def main(values: list, weights: list, capacity: int) -> int:
    matrix = [[0 for _ in range(capacity+1)] for _ in range(len(values)+1)]
    for y in range(1, len(matrix)):
        for x in range(1, len(matrix[0])):
            matrix[y][x] = matrix[y-1][x]
            if x-weights[y-1] >= 0:
                t = values[y-1]+matrix[y-1][x-weights[y-1]]
                matrix[y][x] = max(matrix[y][x], t)
    return matrix[-1][-1]


if __name__ == "__main__":
    print(main([2, 3, 1, 1, ], [1, 2, 3, 1],  5))

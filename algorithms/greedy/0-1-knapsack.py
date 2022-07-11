"""
Das 0-1-Rucksackproblem

Jeder Gegenstand muss entweder vollständig oder überhaupt nicht genommen werden.

Annahme: Beide Arrays sind sortiert.

Komplexität: O(n)
"""


def main(values: list, weights: list, capacity: int) -> int:
    max_value = 0
    for i in range(len(values)):
        if capacity - weights[i] < 0:
            break
        capacity -= weights[i]
        max_value += values[i]
    return max_value


if __name__ == "__main__":
    print(main([60, 100, 120], [10, 20, 30],  50))

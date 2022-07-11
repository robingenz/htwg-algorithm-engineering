"""
Das fraktionale Rucksackproblem

Fülle den Rucksack zuerst mit den wertvollsten Gegenständen und fülle mit den weniger wertvollen Gegenständen bzw. Bruchstücken von Gegenständen sukzessive auf.

Annahme: Beide Arrays sind sortiert.

Komplexität: O(n)
"""


def main(values: list, weights: list, capacity: int) -> int:
    max_value = 0
    for i in range(len(values)):
        if capacity == 0:
            break
        wc_ratio = 1
        if weights[i] > capacity:
            wc_ratio = capacity/weights[i]
        capacity -= wc_ratio*weights[i]
        max_value += wc_ratio*values[i]
    return max_value


if __name__ == "__main__":
    print(main([60, 100, 120], [10, 20, 30],  50))

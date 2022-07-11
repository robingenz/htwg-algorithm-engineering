"""
Das fraktionale Rucksackproblem

Fülle den Rucksack zuerst mit den wertvollsten Gegenständen und fülle mit den weniger wertvollen Gegenständen bzw. Bruchstücken von Gegenständen sukzessive auf.

Komplexität: O(n log n)
"""


def main(values: list, weights: list, capacity: int) -> int:
    indexes = list(range(len(values)))
    ratio = [v/w for v, w in zip(values, weights)]
    indexes.sort(key=lambda i: ratio[i], reverse=True)
    max_value = 0
    for i in indexes:
        if capacity == 0:
            break
        wc_ratio = 1
        if weights[i] > capacity:
            wc_ratio = capacity/weights[i]
        capacity -= wc_ratio*weights[i]
        max_value += wc_ratio*values[i]
    return max_value


if __name__ == "__main__":
    print(main([120, 100, 60], [30, 20, 10],  50))

"""
Zahlen-Dreieck

Berechnung des Pfads in einem Dreieck mit maximaler Summe der besuchten Einträge.

Komplexität: O(n^2)
"""


def numbersTriangle(input: list) -> int:
    cache = [[0 for _ in range(len(input))] for _ in range(len(input[0]))]
    cache[0][0] = input[0][0]
    for y in range(1, len(input)):
        for x in range(len(input[y])):
            if input[y][x] == None:
                continue
            elif x > 0 and input[y-1][x] != None:
                if input[y][x] + cache[y-1][x] > input[y][x] + cache[y-1][x-1]:
                    cache[y][x] = input[y][x] + cache[y-1][x]
                else:
                    cache[y][x] = input[y][x] + cache[y-1][x-1]
            else:
                cache[y][x] = input[y][x] + cache[y-1][x-1]
    return max(cache[-1])


if __name__ == "__main__":
    print(numbersTriangle([
        [10, None, None, None, None, None, None],
        [82, 81, None, None, None, None, None],
        [4, 6, 10, None, None, None, None],
        [2, 14, 35, 7, None, None, None],
        [41, 3, 52, 26, 15, None, None],
        [32, 90, 11, 87, 56, 23, None],
        [54, 65, 89, 32, 71, 9, 31],
    ]))

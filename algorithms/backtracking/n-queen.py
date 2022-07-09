"""
n-Damenproblem

Stelle n Damen so auf ein Schachbrett der Größe n*n, dass keine Dame eine andere bedroht.

Komplexität: O(n^n)
"""


def main(n: int) -> list:
    vector = []
    x = 0
    while len(vector) != n:
        valid = False
        y = len(vector)
        while not valid and x < n:
            vector.append(x)
            valid = True
            for i in range(y):
                valid = not isThreat(vector, i, y) and valid
            if not valid:
                x = vector.pop() + 1
        if valid:
            x = 0
        else:
            x = vector.pop() + 1
    return vector


def isThreat(positions: list, x1: int, x2: int) -> bool:
    return positions[x1] == positions[x2] or abs(x1 - x2) == abs(positions[x1] - positions[x2])


if __name__ == "__main__":
    print(main(100))

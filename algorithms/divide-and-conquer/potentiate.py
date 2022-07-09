"""
Potenzieren

Berechnung der Potenz der Basis b und des Exponenten e.

Komplexität: O(n)
"""


def main(b: int, e: int) -> int:
    if e == 0:
        return 1
    elif e % 2 == 0:
        return main(b, int(e/2)) * main(b, int(e/2))
    else:
        return b * main(b, int(e/2)) * main(b, int(e/2))


if __name__ == "__main__":
    print(main(9, 3))

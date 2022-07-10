"""
Kehrwerte der Potenzfunktion

Berechnung der Kehrwerte der Potenz der Basis b und des Exponenten e.

Komplexität: O(n)
"""


def main(b: int, e: int) -> int:
    if e == 1:
        return 1/b
    elif e % 2 == 0:
        return main(b, int(e/2)) * main(b, int(e/2))
    else:
        return 1/b * main(b, int(e/2)) * main(b, int(e/2))


if __name__ == "__main__":
    print(main(2, 8))

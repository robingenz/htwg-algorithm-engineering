"""
Modulare Potenzierung

Berechnung des Rests "großer" Potenzen.

Komplexität: O(log n)
"""


def main(basis: int, exponent: int, mod: int) -> int:
    if basis == 0:
        return 0
    if exponent == 0:
        return 1

    y = 0
    if exponent % 2 == 0:
        y = main(basis, exponent / 2, mod)
        y = y*y % mod
    else:
        y = basis % mod
        y = (y*main(basis, exponent-1, mod) % mod) % mod

    return ((y+mod) % mod)


if __name__ == "__main__":
    print(main(2, 5, 13))

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

    result = 0
    if exponent % 2 == 0:
        result = main(basis, exponent / 2, mod)
        result = result*result % mod
    else:
        result = ((basis % mod)*(main(basis, exponent-1, mod) % mod)) % mod

    return (result % mod)


if __name__ == "__main__":
    print(main(2, 28, 13))

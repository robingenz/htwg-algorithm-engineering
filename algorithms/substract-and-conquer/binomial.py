"""
Binomialkoeffizient

Berechnet den Binomialkoeffizienten aus n und k.

Komplexität: O(n^2)
"""


def binomial(n: int, k: int) -> int:
    if k == 0 or k == n:
        return 1
    return binomial(n - 1, k) + binomial(n-1, k-1)


if __name__ == "__main__":
    print(binomial(49, 6))

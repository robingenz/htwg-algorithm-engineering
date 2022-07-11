"""
Catalan-Zahlen

Berechnung der Catalan-Zahlen.

Komplexität: O(n^2)
"""


def catalan(n: int) -> int:
    cache = [0]*(n+1)
    cache[0] = 1
    for i in range(1, n+1):
        for j in range(i):
            cache[i] += cache[j]*cache[i-j-1]
    return cache[n]


if __name__ == "__main__":
    print(catalan(9))

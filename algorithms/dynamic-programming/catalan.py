"""
Catalan-Zahlen

Berechnung der Catalan-Zahlen.

Komplexität: O(n^2)
"""


def catalan(n: int) -> int:
    if n <= 1:
        return 1
    cache = [0]*(n+1)
    cache[0] = 1
    cache[1] = 1
    for i in range(2, n+1):
        for j in range(i):
            cache[i] += cache[j]*cache[i-j-1]
    return cache[n]


if __name__ == "__main__":
    print(catalan(9))

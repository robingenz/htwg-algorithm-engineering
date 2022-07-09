"""
Fakultät

Berechnung der Fakultät einer Zahl n.

Komplexität: O(n)
"""


def main(n: int) -> int:
    if n <= 1:
        return 1
    return n * main(n-1)


if __name__ == "__main__":
    print(main(5))

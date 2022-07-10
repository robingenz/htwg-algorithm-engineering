"""
Fibonacci

Berechne die n-te Fibonacci Zahl.

Komplexität: 
"""


def main(n: int) -> int:
    if n < 2:
        return n
    return main(n-1)+main(n-2)


if __name__ == "__main__":
    print(main(10))

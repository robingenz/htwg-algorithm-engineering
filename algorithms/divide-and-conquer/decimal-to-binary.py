"""
Dezimalkonverter

Konvertiert eine Dezimalzahl in eine Binärzahl.

Komplexität: O(log n)
"""


def decimalToBinary(decimal: int):
    if decimal < 1:
        return 0
    else:
        decimalToBinary(int(decimal/2))
        print(decimal % 2)


if __name__ == "__main__":
    decimalToBinary(9)

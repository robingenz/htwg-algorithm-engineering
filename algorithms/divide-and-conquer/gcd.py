"""
Größter gemeinsame Teiler

Berechnung des größten gemeinsamen Teiler von x und y.

Komplexität: O(log(min(x, y))
"""


def main(x: int, y: int) -> int:
    if y == 0:
        return x
    return main(y, x % y)


if __name__ == "__main__":
    print(main(32, 12))

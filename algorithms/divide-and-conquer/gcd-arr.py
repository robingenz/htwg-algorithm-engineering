"""
Größter gemeinsame Teiler mehrerer Zahlen

Berechnung des größten gemeinsamen Teiler eines Arrays aus Zahlen.

Komplexität: O(n log n)
"""


def main(values: list, left: int = None, right: int = None) -> int:
    if left == None:
        left = 0
    if right == None:
        right = len(values)-1
    if left > right:
        return 0
    if left == right:
        return values[left]
    mid = int((left+right)/2)
    x = main(values, left, mid)
    y = main(values, mid+1, right)
    return ggt(x, y)


def ggt(x: int, y: int) -> int:
    while y != 0:
        temp = x % y
        x = y
        y = temp
    return x


if __name__ == "__main__":
    print(main([32, 12, 6]))

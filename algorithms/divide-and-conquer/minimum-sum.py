"""
Minimale zusammenhängende Teilfolge

Berechnung der minimalen zusammenhängenden Teilfolge.

Komplexität: O(n log n)
"""


def main(values: list, left: int = None, right: int = None) -> int:
    if left == None:
        left = 0
    if right == None:
        right = len(values)-1
    if left >= right:
        return values[left]
    mid = int((left+right)/2)

    sum = 0
    leftMidMin = 0
    for i in range(mid, left-1, -1):
        sum += values[i]
        leftMidMin = min(leftMidMin, sum)

    sum = 0
    rightMidMin = 0
    for i in range(mid+1, right+1):
        sum += values[i]
        rightMidMin = min(rightMidMin, sum)

    leftMin = main(values, left, mid)
    rightMin = main(values, mid+1, right)
    return min(leftMidMin+rightMidMin, leftMin, rightMin)


if __name__ == "__main__":
    print(main([3, 5, 7, -4, -3, -1, 5, -9, 12, -2]))

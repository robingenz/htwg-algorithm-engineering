"""
Maximale zusammenhängende Teilfolge

Berechnung der maximalen zusammenhängenden Teilfolge.

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
    leftMidMax = 0
    for i in range(mid, left-1, -1):
        sum += values[i]
        leftMidMax = max(leftMidMax, sum)

    sum = 0
    rightMidMax = 0
    for i in range(mid+1, right+1):
        sum += values[i]
        rightMidMax = max(rightMidMax, sum)

    leftMax = main(values, left, mid)
    rightMax = main(values, mid+1, right)
    return max(leftMidMax+rightMidMax, leftMax, rightMax)


if __name__ == "__main__":
    print(main([3, 5, 7, -4, -3, -1, 5, -9, 12, -2]))

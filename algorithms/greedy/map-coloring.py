"""
Kartenfärbung

Berechnung einer Einfärbung der Länder mit möglichst wenigen Farben.

Komplexität: O(c*n^2)
"""


def main(matrix: list) -> int:
    colors = [0]*len(matrix)
    for y in range(1, len(matrix)):
        colorIndex = -1
        valid = False
        while not valid:
            colorIndex += 1
            valid = True
            for x in range(len(matrix[y])):
                if matrix[x][y] == 1 and colors[x] == colorIndex:
                    valid = False
        colors[y] = colorIndex
    return max(colors)+1


if __name__ == "__main__":
    print(main([[0, 1, 1, 0, 1, 0],
                [1, 0, 1, 1, 0, 1],
                [1, 1, 0, 1, 1, 0],
                [0, 1, 1, 0, 0, 1],
                [1, 0, 1, 0, 0, 1],
                [0, 1, 0, 1, 1, 0]]))

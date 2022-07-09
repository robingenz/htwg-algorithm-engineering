"""
Färbung von Graphen

Prüfung, ob n Farben so zu Knoten zugeordnet werden können, dass benachbarte Knoten verschiedene Farben haben. 

Komplexität: O(n^n)
"""


def main(matrix: list, numOfColors: int) -> list:
    colorIndex = 0
    nodeColorMap = []
    while len(nodeColorMap) != len(matrix):
        valid = False
        while not valid and colorIndex < numOfColors:
            nodeColorMap.append(colorIndex)
            valid = True
            for i in range(len(matrix)):
                isNeighbor = matrix[len(nodeColorMap) - 1][i]
                if isNeighbor:
                    valid = (i >= len(nodeColorMap)
                             or nodeColorMap[i] != colorIndex) and valid
            if not valid:
                colorIndex = nodeColorMap.pop() + 1
        if valid:
            colorIndex = 0
        else:
            if len(nodeColorMap) == 0:
                return []
            colorIndex = nodeColorMap.pop() + 1
    return nodeColorMap


if __name__ == "__main__":
    # See https://python.plainenglish.io/solve-graph-coloring-problem-with-greedy-algorithm-and-python-6661ab4154bd
    print(main([[0, 1, 1, 0, 1, 0],
                [1, 0, 1, 1, 0, 1],
                [1, 1, 0, 1, 1, 0],
                [0, 1, 1, 0, 0, 1],
                [1, 0, 1, 0, 0, 1],
                [0, 1, 0, 1, 1, 0]], 3))

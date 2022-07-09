"""
Wechselgeld

Gib einen Betrag in Euro mit möglichst wenig Münzen und Scheinen heraus.

Komplexität: 
"""


def main(amount: int, coins: list) -> int:
    result = []
    while amount > 0:
        for coin in coins:
            if amount >= coin:  # Greedy Choice
                amount -= coin
                result.append(coin)
                break
    return result


if __name__ == "__main__":
    print(main(1769, [500, 200, 100, 50, 20, 10, 5, 2, 1]))

def max_element_index(values: list) -> int:
    index_max_value = 0
    max_value = values[index_max_value]

    for index, value in enumerate(values):
        if value > max_value:
            index_max_value = index
            max_value = value

    return index_max_value


def main():
    values = [1720, 1721, 979, 366, 299, 675, 1456]
    print(f"Index: {max_element_index(values)}")


def test():
    test_input = [1720, 1721, 979, 366, 299, 675, 1456]
    assert max_element_index(test_input) == 1


if __name__ == "__main__":
    test()
    main()
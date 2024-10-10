def matrix_from_string(string: str) -> list[list[float]]:
    return [list(map(float, line.split())) for line in string.split("|")]


if __name__ == "__main__":
    assert matrix_from_string("1 2 3|4 5 6|7 8 9") == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert matrix_from_string("1 2 | 3 4") == [[1, 2], [3, 4]]




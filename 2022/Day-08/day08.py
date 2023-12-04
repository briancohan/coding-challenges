import pprint
from pathlib import Path
from typing import Any

pp = pprint.PrettyPrinter(indent=4)


def transpose(array: list[list[Any]]) -> list[list[Any]]:
    return [[array[i][j] for i in range(len(array))] for j in range(len(array[0]))]


def visible_trees(forrest: str) -> int:
    forrest_by_row = [[int(i) for i in row] for row in forrest.strip().splitlines()]
    forrest_by_col = transpose(forrest_by_row)

    visible = (len(forrest_by_row) + len(forrest_by_col) - 2) * 2

    for i in range(1, len(forrest_by_row) - 1):
        for j in range(1, len(forrest_by_col) - 1):
            height = forrest_by_row[i][j]
            if max(forrest_by_row[i][:j]) < height:
                visible += 1
            # is visible from right
            elif max(forrest_by_row[i][j + 1 :]) < height:
                visible += 1
            # is visible from up
            elif max(forrest_by_col[j][:i]) < height:
                visible += 1
            # is visible from down
            elif max(forrest_by_col[j][i + 1 :]) < height:
                visible += 1

    return visible


def trees_visible_in_direction(height: int, trees: list[int]) -> int:
    try:
        return next(ix for ix, h in enumerate(trees) if h >= height)
    except StopIteration:
        return 1


def best_spot(forrest: str) -> int:
    forrest_by_row = [[int(i) for i in row] for row in forrest.strip().splitlines()]
    forrest_by_col = transpose(forrest_by_row)

    best_score = 0
    for i in range(1, len(forrest_by_row) - 1):
        for j in range(1, len(forrest_by_col) - 1):
            height = forrest_by_row[i][j]

            l = trees_visible_in_direction(height, forrest_by_row[i][:j][::-1])
            r = trees_visible_in_direction(height, forrest_by_row[i][j + 1 :])
            u = trees_visible_in_direction(height, forrest_by_col[j][:i][::-1])
            d = trees_visible_in_direction(height, forrest_by_col[j][i + 1 :])

            print(f"({i}, {j}) {height}: {l}, {r}, {u}, {d}")
            score = l * r * u * d
            best_score = max(score, best_score)

    return best_score


if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    forrest = input_file.read_text()

    print(visible_trees(forrest))

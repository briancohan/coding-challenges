from collections import deque
import logging
from pathlib import Path
from typing import NewType
from itertools import chain

Data = NewType("Data", list[tuple[str, int, str]])

logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s",
    filename=Path(__file__).with_suffix(".log"),
    filemode="w",
)


def parse_input(full: bool = True, file_name: Path = None) -> Data:
    if file_name is None:
        file_name = "input.txt" if full else "sample.txt"
    input_file = Path(__file__).parent / file_name

    items = []
    for line in input_file.read_text().strip().splitlines():
        direction, distance, color = line.split()
        items.append(
            {
                "direction": direction,
                "distance": int(distance),
                "color": color.replace("(", "").replace(")", ""),
            }
        )

    return items


def flood_fill(path: list[tuple[int, int]], start: tuple[int, int]) -> list[list[int]]:
    x0 = min([x for x, _ in path])
    x1 = max([x for x, _ in path])
    y0 = min([y for _, y in path])
    y1 = max([y for _, y in path])

    def shift(i: int, j: int) -> tuple[int, int]:
        return i - x0, j - y0

    grid = [[0 for _ in range(x0, x1 + 1)] for _ in range(y0, y1 + 1)]
    for i, j in path:
        x, y = shift(i, j)
        grid[y][x] = 1

    queue = deque([shift(*start)])
    while queue:
        x, y = queue.popleft()
        grid[y][x] = 1
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            i, j = x + dx, y + dy
            if not grid[j][i] and (i, j) not in queue:
                queue.append((i, j))

    return grid


def flood_start(data: Data) -> tuple[int, int]:
    first_two_directions = [item["direction"] for item in data[:2]]
    return (
        -1 if "L" in first_two_directions else 1,
        -1 if "D" in first_two_directions else 1,
    )


def get_path(data: Data) -> list[tuple[int, int]]:
    nodes = []
    i, j = 0, 0
    for item in data:
        for _ in range(item["distance"]):
            if item["direction"] == "R":
                i += 1
            elif item["direction"] == "L":
                i -= 1
            elif item["direction"] == "U":
                j -= 1
            elif item["direction"] == "D":
                j += 1
            nodes.append((i, j))
    return nodes


def part_1(data: Data) -> int:
    return sum(chain.from_iterable(flood_fill(get_path(data), flood_start(data))))


def part_2(data: Data) -> int:
    directions = {"0": "R", "1": "D", "2": "L", "3": "U"}
    _data = [
        {
            "direction": directions[row["color"][-1]],
            "distance": int(row["color"][1:-1], 16),
        }
        for row in data
    ]
    return sum(chain.from_iterable(flood_fill(get_path(_data), flood_start(_data))))


if __name__ == "__main__":
    data = parse_input(False)

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

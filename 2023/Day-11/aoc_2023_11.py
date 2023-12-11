from pathlib import Path
from typing import NewType
from itertools import combinations

Data = NewType("Data", list[list[int]])


def parse_input(full: bool = True, file_name: Path = None) -> Data:
    if file_name is None:
        file_name = "input.txt" if full else "sample.txt"
    input_file = Path(__file__).parent / file_name
    contents = input_file.read_text().strip().splitlines()

    return [
        [i, j]
        for i, line in enumerate(contents)
        for j, char in enumerate(line)
        if char == "#"
    ]


def expand_universe(data: Data, distance: int = 1) -> Data:
    populated_rows = set([i for i, _ in data])
    populated_cols = set([j for _, j in data])
    void_rows = [i for i in range(max(populated_rows)) if i not in populated_rows]
    void_cols = [j for j in range(max(populated_cols)) if j not in populated_cols]

    galaxies = [
        [
            i + (len([r for r in void_rows if r < i]) * distance),
            j + (len([c for c in void_cols if c < j]) * distance),
        ]
        for (i, j) in data
    ]

    return galaxies


def distance(a: list[int], b: list[int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def part_1(data: Data, expand: int = 1) -> int:
    galaxies = expand_universe(data, expand)
    return sum([distance(a, b) for a, b in combinations(galaxies, 2)])


def part_2(data: Data, expand: int = 1000000) -> int:
    galaxies = expand_universe(data, expand - 1)
    return sum([distance(a, b) for a, b in combinations(galaxies, 2)])


if __name__ == "__main__":
    data = parse_input()

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

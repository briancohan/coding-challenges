from itertools import combinations
from pathlib import Path
from typing import NewType

Data = NewType("Data", list[int])


def parse_input(full: bool = True, file_name: Path = None) -> Data:
    if file_name is None:
        file_name = "input.txt" if full else "sample.txt"
    input_file = Path(__file__).parent / file_name
    return list(map(int, input_file.read_text().strip().splitlines()))


def part_1(data: Data) -> int:
    return next(n * (2020 - n) for n in data if 2020 - n in data)


def part_2(data: Data) -> int:
    for a, b, c in combinations(data, 3):
        if a + b + c == 2020:
            return a * b * c


if __name__ == "__main__":
    data = parse_input()

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

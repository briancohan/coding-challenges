from functools import reduce
from pathlib import Path
from typing import NewType

Data = NewType("Data", list[str])


def parse_input(full: bool = True, file_name: Path = None) -> Data:
    if file_name is None:
        file_name = "input.txt" if full else "sample.txt"
    input_file = Path(__file__).parent / file_name
    return list(map(int, input_file.read_text().strip().splitlines()))


def part_1(data: Data) -> int:
    return reduce(
        lambda r, i: (r[0] + (1 if i > r[1] else 0), i),
        data,
        (0, float("inf")),
    )[0]


def part_2(data: Data) -> int:
    return sum(
        [
            sum(data[i + 0 : i + 3]) < sum(data[i + 1 : i + 4])
            for i in range(len(data) - 3)
        ]
    )


if __name__ == "__main__":
    data = parse_input()

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

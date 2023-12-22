import json
import logging
from pathlib import Path
from typing import NewType
from functools import reduce

Data = NewType("Data", list[int])

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
    return list(map(int, input_file.read_text().strip()))


def part_1(data: Data) -> int:
    return reduce(
        lambda r, i: (r[0] + (i if i == r[1] else 0), i), data, (0, int(data[-1]))
    )[0]


def part_2(data: Data) -> int:
    return sum([a for a, b in zip(data, data[len(data) // 2 :] + data[: len(data) // 2]) if a == b])


if __name__ == "__main__":
    data = parse_input()


    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

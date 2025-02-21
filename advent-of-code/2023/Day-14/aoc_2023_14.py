import json
import logging
from pathlib import Path
from typing import NewType

Data = NewType("Data", list[str])

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
    return input_file.read_text().splitlines()


def transpose(field: list[str]) -> list[str]:
    """Pivot along diagonal axis so first and last elements are in the same position.

    123 --> 14   |   123 --> 147
    456 --> 25   |   456 --> 258
        --> 36   |   789 --> 369
    """
    return ["".join([row[i] for row in field]) for i in range(len(field[0]))]


def calculate_load(data: Data) -> int:
    total_load = 0
    for r, row in enumerate(transpose(data)):
        logging.debug(f"\n'{row}'")
        load = len(row)

        for c, char in enumerate(row):
            if char == "O":
                total_load += load
                logging.debug(f"Found load at {r}, {c} ({load:>2}) {total_load:>3}")
                load -= 1
            if char == "#":
                load = len(row) - c - 1

    return total_load


def part_1(data: Data) -> int:
    return calculate_load(data)


def part_2(data: Data) -> int:
    return 0


if __name__ == "__main__":
    data = parse_input(~False)

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

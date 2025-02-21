from pathlib import Path
from typing import NewType

Data = NewType("Data", str)


def parse_input(full: bool = True, file_name: Path = None) -> Data:
    if file_name is None:
        file_name = "input.txt" if full else "sample.txt"
    input_file = Path(__file__).parent / file_name
    return input_file.read_text().strip()


def part_1(data: Data) -> int:
    return data.count("(") - data.count(")")


def part_2(data: Data) -> int:
    return next(i for i in range(len(data) + 1) if part_1(data[:i]) == -1)


if __name__ == "__main__":
    data = parse_input()

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

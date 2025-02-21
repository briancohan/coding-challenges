from collections import deque
from pathlib import Path
from typing import NewType

Data = NewType("Data", list[int])


def parse_input(full: bool = True, file_name: Path = None) -> Data:
    if file_name is None:
        file_name = "input.txt" if full else "sample.txt"
    input_file = Path(__file__).parent / file_name
    return list(map(int, input_file.read_text().strip().splitlines()))


def part_1(data: Data) -> int:
    return sum(data)


def part_2(data: Data) -> int:
    _data = deque(data)
    frequencies = []
    frequency = 0
    while True:
        frequency += _data[0]
        if frequency in frequencies:
            return frequency
        frequencies.append(frequency)
        _data.rotate(-1)


if __name__ == "__main__":
    data = parse_input()

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

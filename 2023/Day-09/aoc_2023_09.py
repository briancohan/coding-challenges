from pathlib import Path
from typing import NewType

Data = NewType("Data", list[tuple[int]])


def parse_input(full: bool = True, file_name: Path = None) -> Data:
    if file_name is None:
        file_name = "input.txt" if full else "sample.txt"
    input_file = Path(__file__).parent / file_name

    return [
        tuple(map(int, line.split()))
        for line in input_file.read_text().strip().splitlines()
    ]


def get_next(numbers: tuple[int]) -> int:
    next_line = tuple(b - a for a, b in zip(numbers, numbers[1:]))
    if not any(next_line):
        return numbers[-1]
    else:
        return get_next(next_line) + numbers[-1]


def part_1(data: Data) -> int:
    return sum(get_next(numbers) for numbers in data)


def part_2(data: Data) -> int:
    return sum(get_next(numbers[::-1]) for numbers in data)


if __name__ == "__main__":
    data = parse_input()

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

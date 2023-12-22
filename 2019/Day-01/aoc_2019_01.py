from pathlib import Path
from typing import NewType

Data = NewType("Data", list[int])


def parse_input(full: bool = True, file_name: Path = None) -> Data:
    if file_name is None:
        file_name = "input.txt" if full else "sample.txt"
    input_file = Path(__file__).parent / file_name
    return list(map(int, input_file.read_text().strip().splitlines()))


def fuel_load(mass: int) -> int:
    return (mass // 3) - 2


def part_1(data: Data) -> int:
    return sum([fuel_load(i) for i in data])


def part_2(data: Data) -> int:
    fuel = 0
    for i in data:
        while (i := (i // 3) - 2) > 0:
            fuel += i
    return fuel


if __name__ == "__main__":
    data = parse_input()

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

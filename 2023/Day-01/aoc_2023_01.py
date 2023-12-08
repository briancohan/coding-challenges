import re
from pathlib import Path
from typing import NewType

Data = NewType("Data", list[str])


def parse_input(full: bool = True, file_name: Path = None) -> Data:
    if file_name is None:
        file_name = "input.txt" if full else "sample.txt"
    input_file = Path(__file__).parent / file_name
    print(input_file)
    return input_file.read_text().strip().splitlines()


def part_1(data: Data) -> int:
    total = 0
    for line in data:
        digits = re.findall(r"\d", line)
        total += int(digits[0] + digits[-1])
    return total


def part_2(data: Data) -> int:
    total = 0
    table = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0",
    }
    for line in data:
        digits = []
        for ix in range(len(line)):
            for key, value in table.items():
                if line[ix:].startswith(key):
                    digits.append(value)
                    break
                if line[ix].isdigit():
                    digits.append(line[ix])
                    break
        total += int(digits[0] + digits[-1])

    return total


if __name__ == "__main__":
    data = parse_input()

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

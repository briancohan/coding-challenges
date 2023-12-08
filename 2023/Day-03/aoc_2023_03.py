import re
from collections import defaultdict
from math import prod
from pathlib import Path
from typing import NewType

Data = NewType("Data", str)


def parse_input(full: bool = True, file_name: Path = None) -> Data:
    if file_name is None:
        file_name = "input.txt" if full else "sample.txt"
    input_file = Path(__file__).parent / file_name
    return input_file.read_text().strip()


def is_valid_number(span: tuple[int, int], data: str, cols: int) -> bool:
    # Get row and start col from span
    i = span[0] // cols
    j0 = max(span[0] - i * cols - 1, 0)
    j1 = min(span[1] - i * cols + 1, cols)

    rows = data.splitlines()
    for row in range(i - 1, i + 2):
        if row < 0 or row >= len(rows):
            continue
        if re.search(r"[^0-9\.]", rows[row][j0:j1]):
            return True

    return False


def possible_gear(span: tuple[int, int], data: str, cols: int) -> tuple[int, int]:
    # Get row and start col from span
    i = span[0] // cols
    j0 = max(span[0] - i * cols - 1, 0)
    j1 = min(span[1] - i * cols + 1, cols)

    valid = False
    rows = data.splitlines()
    for row in range(i - 1, i + 2):
        if row < 0 or row >= len(rows):
            continue

        segment = rows[row][j0:j1]
        if "*" in segment:
            hub = row, j0 + segment.index("*")
            return hub

    return valid


def part_1(data):
    # Add one to account for the newline character
    cols = data.index("\n") + 1

    return sum(
        int(match.group())
        for match in re.finditer(r"\d+", data)
        if is_valid_number(match.span(), data, cols)
    )


def part_2(data):
    # Add one to account for the newline character
    cols = data.index("\n") + 1

    possible_gears = defaultdict(list)

    for match in re.finditer(r"\d+", data):
        hub = possible_gear(match.span(), data, cols)
        if hub:
            possible_gears[hub].append(int(match.group()))

    return sum(prod(gears) for gears in possible_gears.values() if len(gears) == 2)


if __name__ == "__main__":
    data = parse_input()

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

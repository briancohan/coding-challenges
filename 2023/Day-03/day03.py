from pathlib import Path
import logging
from collections import defaultdict
import re
from math import prod

logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s",
    filename=Path(__file__).with_suffix(".log"),
    filemode="w",
)


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
    data = data.strip()
    # Add one to account for the newline character
    cols = data.index("\n") + 1

    return sum(
        int(match.group())
        for match in re.finditer(r"\d+", data)
        if is_valid_number(match.span(), data, cols)
    )


def part_2(data):
    data = data.strip()
    # Add one to account for the newline character
    cols = data.index("\n") + 1

    possible_gears = defaultdict(list)

    for match in re.finditer(r"\d+", data):
        hub = possible_gear(match.span(), data, cols)
        if hub:
            possible_gears[hub].append(int(match.group()))

    return sum(prod(gears) for gears in possible_gears.values() if len(gears) == 2)


if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    data = input_file.read_text()

    print(part_1(data))
    print(part_2(data))

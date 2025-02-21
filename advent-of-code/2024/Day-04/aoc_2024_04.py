import json
import logging
from pathlib import Path
from typing import NewType, Generator

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
    return input_file.read_text().strip().splitlines()


def find_starts(
    data: Data,
    char: str,
) -> Generator[tuple[int, int], None, None]:
    for r, line in enumerate(data):
        for c, ch in enumerate(line):
            if ch == char:
                yield (r, c)


def find_next_char(
    data: Data,
    char: str,
    row: int,
    col: int,
) -> Generator[tuple[int, int], None, None]:
    for r in range(max(row - 1, 0), min(row + 2, len(data))):
        for c in range(max(col - 1, 0), min(col + 2, len(data[0]))):
            if data[r][c] == char and (r, c) != (row, col):
                yield (r, c)


def get_offset_pos(
    p1: tuple[int, int],
    p2: tuple[int, int],
    dist: int,
) -> tuple[int, int]:
    r_offset = p2[0] - p1[0]
    c_offset = p2[1] - p1[1]
    return (p2[0] + r_offset * dist, p2[1] + c_offset * dist)


def part_1(data: Data) -> int:
    counts = 0

    for x_r, x_c in find_starts(data, "X"):
        for m_r, m_c in find_next_char(data, "M", x_r, x_c):
            a_r, a_c = get_offset_pos((x_r, x_c), (m_r, m_c), 1)
            if not (0 <= a_r < len(data) and 0 <= a_c < len(data[0])):
                continue

            s_r, s_c = get_offset_pos((x_r, x_c), (m_r, m_c), 2)
            if not (0 <= s_r < len(data) and 0 <= s_c < len(data[0])):
                continue

            if data[a_r][a_c] == "A" and data[s_r][s_c] == "S":
                counts += 1

    return counts


def part_2(data: Data) -> int:
    counts = 0

    for r, c in find_starts(data, "A"):
        if not 0 < r < len(data) - 1:
            continue
        if not 0 < c < len(data[0]) - 1:
            continue

        if {data[r - 1][c - 1], data[r + 1][c + 1]} != {"M", "S"}:
            continue

        if {data[r - 1][c + 1], data[r + 1][c - 1]} != {"M", "S"}:
            continue

        counts += 1

    return counts


if __name__ == "__main__":
    data = parse_input(False)
    logging.debug(json.dumps(data, indent=4))

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

from pathlib import Path
from typing import NewType

Data = NewType("Data", list[str])


def parse_input(full: bool = True, file_name: Path = None) -> Data:
    if file_name is None:
        file_name = "input.txt" if full else "sample.txt"
    input_file = Path(__file__).parent / file_name
    return input_file.read_text().strip().split(", ")


def part_1(data: Data) -> int:
    nesw = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    x = y = d = 0
    for i in data:
        d = (d + (1 if i[0] == "R" else -1)) % 4
        x += nesw[d][0] * int(i[1:])
        y += nesw[d][1] * int(i[1:])
    return abs(x) + abs(y)


def part_2(data: Data) -> int:
    nesw = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    locations = []
    x = y = d = 0
    for i in data:
        d = (d + (1 if i[0] == "R" else -1)) % 4
        for _ in range(int(i[1:])):
            x += nesw[d][0]
            y += nesw[d][1]
            if (x, y) in locations:
                return abs(x) + abs(y)
            locations.append((x, y))


if __name__ == "__main__":
    data = parse_input()

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

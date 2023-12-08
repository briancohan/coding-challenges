from math import ceil, floor, prod, sqrt
from pathlib import Path
from typing import NewType

Data = NewType("Data", dict[str, list[int]])


def parse_input(full: bool = True) -> Data:
    input_file = Path(__file__).parent / ("input.txt" if full else "sample.txt")

    races = {}
    for line in input_file.read_text().strip().splitlines():
        metric, values = line.split(":")
        races[metric.lower()] = list(map(int, values.split()))

    return races


def ways_to_win(t: int, d: int) -> int:
    min_delay = ceil((t - sqrt(t**2 - 4 * (d + 1))) / 2)
    max_delay = floor((t + sqrt(t**2 - 4 * (d + 1))) / 2)
    return max_delay - min_delay + 1


def part_1(data: Data) -> int:
    return prod([ways_to_win(t, d) for t, d in zip(data["time"], data["distance"])])


def part_2(data: Data) -> int:
    return ways_to_win(
        int("".join(map(str, data["time"]))),
        int("".join(map(str, data["distance"]))),
    )


if __name__ == "__main__":
    data = parse_input()

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

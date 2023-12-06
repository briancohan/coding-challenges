from pathlib import Path
import logging
from math import sqrt, ceil, floor, prod

logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s",
    filename=Path(__file__).with_suffix(".log"),
    filemode="w",
)


def parse_data(data: str) -> dict[str, list[int]]:
    races = {}
    for line in data.strip().splitlines():
        metric, values = line.split(":")
        races[metric.lower()] = list(map(int, values.split()))

    return races


def ways_to_win(t: int, d: int) -> int:
    min_delay = ceil((t - sqrt(t**2 - 4 * (d + 1))) / 2)
    max_delay = floor((t + sqrt(t**2 - 4 * (d + 1))) / 2)
    return max_delay - min_delay + 1


def part_1(data: dict[str, list[int]]) -> int:
    return prod([ways_to_win(t, d) for t, d in zip(data["time"], data["distance"])])


def part_2(data: dict[str, list[int]]) -> int:
    return ways_to_win(
        int("".join(map(str, data["time"]))),
        int("".join(map(str, data["distance"]))),
    )


if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    data = input_file.read_text()
    data = parse_data(data)

    print(part_1(data))
    print(part_2(data))

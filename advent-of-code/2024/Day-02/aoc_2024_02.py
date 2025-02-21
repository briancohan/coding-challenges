import json
import logging
from pathlib import Path
from typing import NewType

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


def is_safe(levels: str | list[int], dampen: bool = False) -> bool:
    if isinstance(levels, str):
        levels = [int(i) for i in levels.split()]

    if levels[1] < levels[0]:
        levels = levels[::-1]

    for lo, hi in zip(levels, levels[1:]):
        if not 0 < (hi - lo) < 4:
            if dampen:
                return any(
                    [
                        is_safe(levels[: ix + 0] + levels[ix + 1 :])
                        for ix in range(len(levels) - 1)
                    ]
                    + [
                        is_safe(levels[: ix + 1] + levels[ix + 2 :])
                        for ix in range(len(levels) - 1)
                    ]
                )
            return False

    return True


def part_1(data: Data) -> int:
    return sum(is_safe(report) for report in data)


def part_2(data: Data) -> int:
    return sum(is_safe(report, dampen=True) for report in data)


if __name__ == "__main__":
    data = parse_input(~False)
    logging.debug(json.dumps(data, indent=4))

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

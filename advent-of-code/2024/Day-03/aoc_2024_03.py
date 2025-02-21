import json
import re
import logging
from pathlib import Path
from typing import NewType

Data = NewType("Data", str)

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
    return input_file.read_text().strip()


def part_1(data: Data) -> int:
    matches = re.findall("mul\((\d+),(\d+)\)", data)
    return sum(int(a) * int(b) for a, b in matches)


def part_2(data: Data) -> int:
    enabled = True
    result = 0

    for m in re.finditer("(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", data):
        match m.groups():
            case ("do()", *_):
                enabled = True
            case ("don't()", *_):
                enabled = False
            case (*_, a, b) if enabled:
                result += int(a) * int(b)
            case _:
                pass

    return result


if __name__ == "__main__":
    data = parse_input(~False)
    logging.debug(json.dumps(data, indent=4))

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

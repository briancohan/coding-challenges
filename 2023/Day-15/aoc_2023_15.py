from collections import defaultdict
from pathlib import Path
from typing import NewType

Data = NewType("Data", list[str])


def parse_input(full: bool = True, file_name: Path = None) -> Data:
    if file_name is None:
        file_name = "input.txt" if full else "sample.txt"
    input_file = Path(__file__).parent / file_name
    return input_file.read_text().strip().split(",")


def hash(input: str) -> int:
    val = 0
    for i in input:
        val = (val + ord(i)) * 17 % 256
    return val


def part_1(data: Data) -> int:
    return sum([hash(i) for i in data])


def part_2(data: Data) -> int:
    boxes = defaultdict(dict)
    for item in data:
        if "-" in item:
            label = item.split("-")[0]
            box = hash(label)
            if label in boxes[box]:
                del boxes[box][label]
        else:
            label, focal = item.split("=")
            box = hash(label)
            boxes[box][label] = int(focal)

    total = 0
    for box, lenses in boxes.items():
        for slot, length in enumerate(lenses.values()):
            total += (box + 1) * (slot + 1) * length

    return total


if __name__ == "__main__":
    data = parse_input(~False)

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

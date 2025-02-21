import logging
from pathlib import Path
from typing import NewType

Field = NewType("Field", list[str])
Data = NewType("Data", list[Field])

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

    chunks = [
        chunk.splitlines() for chunk in input_file.read_text().strip().split("\n\n")
    ]

    return chunks


def transpose(field: Field) -> Field:
    """Pivot along diagonal axis so first and last elements are in the same position.

    123 --> 14   |   123 --> 147
    456 --> 25   |   456 --> 258
        --> 36   |   789 --> 369
    """
    return ["".join([row[i] for row in field]) for i in range(len(field[0]))]


def show_me_the_mirror(field: Field, mirror: int) -> None:
    logging.debug(f"Found potential mirror at {mirror}")
    for l, line in enumerate(field):
        indicators = "  ", "  "
        if l == mirror:
            indicators = "\\ ", " /"
        elif l == mirror + 1:
            indicators = "/ ", " \\"
        logging.debug(f"{l}: {indicators[0]}{line}{indicators[1]}")
    logging.debug("")


def find_mirror(field: Field) -> int:
    for i in range(len(field) - 1):
        if field[i] == field[i + 1]:
            show_me_the_mirror(field, i)
            above = list(range(i - 1, -1, -1))
            below = list(range(i + 2, len(field)))
            logging.debug(f"{above=}, {below=}")
            if all(field[j] == field[k] for j, k in zip(above, below)):
                return i + 1

    return 0


def part_1(data: Data) -> int:
    score = 0
    for field in data:
        logging.debug("-" * 40)
        if mirror := find_mirror(transpose(field)):
            score += mirror
        elif mirror := find_mirror(field):
            score += mirror * 100
    return score


def part_2(data: Data) -> int:
    return 0


if __name__ == "__main__":
    data = parse_input(~False)

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

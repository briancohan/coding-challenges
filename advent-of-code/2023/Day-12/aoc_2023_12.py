import logging
from pathlib import Path
from typing import NewType

Data = NewType("Data", list[tuple[str, list[int]]])

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

    data = []
    for line in input_file.read_text().strip().splitlines():
        mapping, groups = line.split()
        data.append((mapping, [int(group) for group in groups.split(",")]))

    return data


def arrangements(mapping: str, groups: list[int]) -> list[str]:
    logging.debug(f"mapping: {mapping}, groups: {groups}")
    arr = []

    n_unk = mapping.count("?")

    for i in range(2**n_unk):
        subs = f"{i:b}".replace("0", ".").replace("1", "#")
        subs = "." * (n_unk - len(subs)) + subs

        if subs.count("#") + mapping.count("#") != sum(groups):
            continue

        _mapping = mapping
        for sub in subs:
            _mapping = _mapping.replace("?", sub, 1)

        _groups = [len(g) for g in _mapping.split(".") if g]
        if _groups != groups:
            continue

        arr.append(_mapping)

    return arr


def part_1(data: Data) -> int:
    return sum([len(arrangements(mapping, groups)) for mapping, groups in data])


def part_2(data: Data) -> int:
    return sum(
        [
            len(arrangements("?".join([mapping] * 5), groups * 5))
            for mapping, groups in data
        ]
    )


if __name__ == "__main__":
    data = parse_input(False)

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

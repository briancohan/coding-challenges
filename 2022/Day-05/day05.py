from collections import defaultdict, namedtuple
from pathlib import Path
from string import ascii_uppercase
from typing import NewType

Towers: NewType = dict[int, list[str]]
Instruction = namedtuple("Instruction", ["qty", "from_tower", "to_tower"])


def process_towers(data: str) -> Towers:
    towers = defaultdict(list)

    for line in data.split("\n"):
        if towers and not line:
            # Flip list so we can use append, extend, and pop
            for key, value in towers.items():
                towers[key] = value[::-1]
            return towers

        for i, char in enumerate(line[1::4], 1):
            if char in ascii_uppercase:
                towers[i].append(char)


def process_instructions(data: str) -> list[Instruction]:
    instructions = []

    for line in data.splitlines():
        if line.startswith("move"):
            _, qty, _, from_tower, _, to_tower = line.split()
            instructions.append(Instruction(int(qty), int(from_tower), int(to_tower)))

    return instructions


def rearrange_towers(
    towers: Towers,
    instructions: list[Instruction],
    model: int,
) -> None:
    for i in instructions:
        crates = towers[i.from_tower][-i.qty :]
        del towers[i.from_tower][-i.qty :]

        if model == 9000:
            crates = crates[::-1]

        towers[i.to_tower].extend(crates)


def get_top_crates(data: str, model: int) -> str:
    towers = process_towers(data)
    instructions = process_instructions(data)

    rearrange_towers(towers, instructions, model)

    return "".join([towers[ix + 1][-1] for ix in range(len(towers))])


if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    data = input_file.read_text()

    print(get_top_crates(data, 9000))
    print(get_top_crates(data, 9001))

import re
from math import lcm
from pathlib import Path
from typing import NewType

Turns = NewType("LR", str)
Nodes = NewType("Nodes", dict[str, dict[str, str]])
Data = NewType("Data", tuple[Turns, Nodes])


def parse_input(full: bool = True, file_name: Path = None) -> Data:
    if file_name is None:
        file_name = "input.txt" if full else "sample.txt"
    input_file = Path(__file__).parent / file_name

    turns, nodelines = input_file.read_text().split("\n\n")

    nodes = dict()
    for line in nodelines.splitlines():
        match = re.search(r"(?P<node>\w+)\s=\s\((?P<L>\w+),\s(?P<R>\w+)\)", line)
        nodes[match.group("node")] = match.groupdict()

    return turns, nodes


def part_1(data: Data) -> int:
    turns, nodes = data
    steps = 0
    next_node = "AAA"

    while next_node != "ZZZ":
        next_node = nodes[next_node][turns[steps % len(turns)]]
        steps += 1

    return steps


def part_2(data: Data) -> int:
    turns, nodes = data

    paths = {node: 0 for node in nodes.keys() if node.endswith("A")}

    for start in paths.keys():
        steps = 0
        next_node = start

        while not next_node.endswith("Z"):
            next_node = nodes[next_node][turns[steps % len(turns)]]
            steps += 1

        paths[start] = steps

    return lcm(*paths.values())


if __name__ == "__main__":
    data = parse_input()

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

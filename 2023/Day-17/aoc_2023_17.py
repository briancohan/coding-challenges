import logging
from pathlib import Path
from typing import NewType
from operator import itemgetter
from contextlib import suppress
from itertools import product

Data = NewType("Data", list[str])
Point = NewType("Point", tuple[int, int])

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
    return [
        [int(c) for c in line] for line in input_file.read_text().strip().splitlines()
    ]


def show_field(data: Data, path: list[Point]) -> None:
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if (i, j) in path:
                print(f"\x1b[1;31m{c}\x1b[0m", end="")
            else:
                print(c, end="")
        print()


def in_bounds(data: Data, pos: Point) -> bool:
    return 0 <= pos[0] < len(data) and 0 <= pos[1] < len(data[0])


def is_legal(trajectory: list[Point]) -> bool:
    _t = [t for t in trajectory if t is not None]
    if len(_t) < 3:
        return True
    return min(len(set([i[0] for i in _t])), len(set([i[1] for i in _t]))) > 1


def log_node(node: Point, symbol: str, msg: str) -> None:
    logging.debug(f"({node[0]:>2}, {node[1]:>2}) {symbol} {msg}")


def shortest_path(data: Data, start: Point = (0, 0), end: Point = None) -> int:
    if end is None:  # Assume bottom right corner
        end = (len(data) - 1, len(data[0]) - 1)

    nodes = {
        (i, j): {"prev": None, "dist": float("inf")}
        for i in range(len(data))
        for j in range(len(data[0]))
    }
    nodes[start]["dist"] = data[start[0]][start[1]]
    visited = set()

    while nodes:
        current = min(nodes.items(), key=lambda n: n[1]["dist"])[0]
        logging.debug("\n" + f" {current} {nodes[current]['dist']} ".center(40, "-"))

        i, j = current
        for node in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            trajectory = [current, nodes[current]["prev"], node]

            if node in visited:
                log_node(node, "❌", f"is already visited")
                continue
            if not in_bounds(data, node):
                log_node(node, "❌", f"is out of bounds")
                continue
            if not is_legal(trajectory):
                log_node(node, "❌", f"is not legal")
                continue

            curr_dist = nodes[current]["dist"]
            node_weight = data[node[0]][node[1]]
            node_dist = nodes[node]["dist"]

            if node_dist > curr_dist + node_weight:
                nodes[node]["dist"] = curr_dist + node_weight
                nodes[node]["prev"] = current
                log_node(node, "✅", f"{nodes[node]} (was {node_dist})")
            else:
                log_node(node, "❌", f"{nodes[node]} (<= {curr_dist + node_weight})")
        visited.add(current)
        logging.debug("")
        for node in sorted(nodes):
            log_node(node, "", nodes[node])

    if True:
        logging.debug(" Nodes ".center(40, "="))
        for node in sorted(nodes):
            log_node(node, "", nodes[node])
        logging.debug(" Visited ".center(40, "="))
        for node in sorted(visited):
            log_node(node, "", nodes[node])
        path = [end]
        while nodes[path[-1]]["prev"] is not None:
            path.append(nodes[path[-1]]["prev"])
        show_field(data, path)

    return visited[end]["dist"]


def part_1(data: Data) -> int:
    return shortest_path(data)


def part_2(data: Data) -> int:
    return 0


if __name__ == "__main__":
    data = parse_input(False)
    data = [
        list(map(int, "181118")),
        list(map(int, "111818")),
        list(map(int, "888818")),
        list(map(int, "881118")),
        list(map(int, "881888")),
        list(map(int, "881111")),
    ]

    print(f"Part 1: {part_1(data)} (should be 102)")
    print(f"Part 2: {part_2(data)}")

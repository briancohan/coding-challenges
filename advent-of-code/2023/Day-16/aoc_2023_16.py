import multiprocessing as mp
from collections import deque, namedtuple
from pathlib import Path
from typing import NewType

Data = NewType("Data", list[str])
Node = namedtuple("Node", ["row", "col", "dir"])


def parse_input(full: bool = True, file_name: Path = None) -> Data:
    if file_name is None:
        file_name = "input.txt" if full else "sample.txt"
    input_file = Path(__file__).parent / file_name
    return input_file.read_text().strip().splitlines()


def in_bounds(row: int, col: int, data: Data) -> bool:
    return 0 <= row < len(data) and 0 <= col < len(data[0])


def get_next(node: Node, data: Data) -> list["Node"]:
    next_nodes = {
        # Pass Through
        (">", "."): [Node(node.row, node.col + 1, ">")],
        ("<", "."): [Node(node.row, node.col - 1, "<")],
        ("v", "."): [Node(node.row + 1, node.col, "v")],
        ("^", "."): [Node(node.row - 1, node.col, "^")],
        (">", "-"): [Node(node.row, node.col + 1, ">")],
        ("<", "-"): [Node(node.row, node.col - 1, "<")],
        ("v", "|"): [Node(node.row + 1, node.col, "v")],
        ("^", "|"): [Node(node.row - 1, node.col, "^")],
        # Turn
        (">", "/"): [Node(node.row - 1, node.col, "^")],
        ("<", "/"): [Node(node.row + 1, node.col, "v")],
        ("v", "/"): [Node(node.row, node.col - 1, "<")],
        ("^", "/"): [Node(node.row, node.col + 1, ">")],
        (">", "\\"): [Node(node.row + 1, node.col, "v")],
        ("<", "\\"): [Node(node.row - 1, node.col, "^")],
        ("v", "\\"): [Node(node.row, node.col + 1, ">")],
        ("^", "\\"): [Node(node.row, node.col - 1, "<")],
        # Split
        ("v", "-"): [
            Node(node.row, node.col - 1, "<"),
            Node(node.row, node.col + 1, ">"),
        ],
        ("^", "-"): [
            Node(node.row, node.col - 1, "<"),
            Node(node.row, node.col + 1, ">"),
        ],
        (">", "|"): [
            Node(node.row - 1, node.col, "^"),
            Node(node.row + 1, node.col, "v"),
        ],
        ("<", "|"): [
            Node(node.row - 1, node.col, "^"),
            Node(node.row + 1, node.col, "v"),
        ],
    }

    return next_nodes[node.dir, data[node.row][node.col]]


def total_energy(data: Data, node: Node) -> int:
    visited = []
    queue = deque([node])

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        if not in_bounds(node.row, node.col, data):
            continue

        visited.append(node)
        queue.extend(get_next(node, data))

    return len(set((n.row, n.col) for n in visited))


def worker(queue: mp.Queue, data: Data, node: Node):
    queue.put(total_energy(data, node))


def part_1(data: Data) -> int:
    return total_energy(data, Node(0, 0, ">"))


def part_2(data: Data) -> int:
    nodes = []
    r0, r1 = 0, len(data) - 1
    c0, c1 = 0, len(data[0]) - 1
    nodes.extend(Node(r0, c, "v") for c in range(c0, c1))
    nodes.extend(Node(r1, c, "^") for c in range(c0, c1))
    nodes.extend(Node(r, c0, ">") for r in range(r0, r1))
    nodes.extend(Node(r, c1, "<") for r in range(r0, r1))

    q = mp.Queue()
    processes = [mp.Process(target=worker, args=(q, data, n)) for n in nodes]
    [p.start() for p in processes]
    [p.join() for p in processes]
    return max([q.get() for _ in processes])


if __name__ == "__main__":
    data = parse_input()

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

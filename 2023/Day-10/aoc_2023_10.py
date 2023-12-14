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


OKGREEN = "\033[92m"
ENDC = "\033[0m"
OPEN_TOP = "╰╯│"
OPEN_BOTTOM = "╭╮│"
OPEN_LEFT = "╮─╯"
OPEN_RIGHT = "╭╰─"

DIRECTIONS = {
    "up": {"offset": (-1, 0), "cur_chars": OPEN_TOP + "S", "next_chars": OPEN_BOTTOM},
    "down": {"offset": (1, 0), "cur_chars": OPEN_BOTTOM + "S", "next_chars": OPEN_TOP},
    "left": {"offset": (0, -1), "cur_chars": OPEN_LEFT + "S", "next_chars": OPEN_RIGHT},
    "right": {"offset": (0, 1), "cur_chars": OPEN_RIGHT + "S", "next_chars": OPEN_LEFT},
}


def print_grid(data: Data, path: list[tuple[int, int]]):
    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if (i, j) in path:
                print(f"{OKGREEN}{char}{ENDC}", end="")
            else:
                print(char, end="")
        print()


def parse_input(full: bool = True, file_name: Path = None) -> Data:
    if file_name is None:
        file_name = "input.txt" if full else "sample.txt"
    input_file = Path(__file__).parent / file_name
    mapping = {"F": "╭", "7": "╮", "L": "╰", "J": "╯", "|": "│", "-": "─", " ": " "}

    lines = []
    for line in input_file.read_text().strip().splitlines():
        for old, new in mapping.items():
            line = line.replace(old, new)
        lines.append(line)
    return lines


def can_go(
    data: Data,
    path: list[tuple[int, int]],
    offset: tuple[int, int],
    cur_chars: str,
    next_chars: str,
) -> tuple[int, int]:
    cur_pos = path[-1]
    next_pos = cur_pos[0] + offset[0], cur_pos[1] + offset[1]

    if next_pos in path:
        return False

    cur_char = data[cur_pos[0]][cur_pos[1]]
    try:
        next_char = data[next_pos[0]][next_pos[1]]
    except IndexError:
        return False

    if cur_char in cur_chars and next_char in next_chars:
        return next_pos

    return False


def go_forward(data: Data, path: list[tuple[int, int]]) -> tuple[int, int]:
    for params in DIRECTIONS.values():
        if next_pos := can_go(data, path, **params):
            return next_pos
    return False


def trace_path(data: Data) -> list[tuple[int, int]]:
    path = [(i, row.index("S")) for i, row in enumerate(data) if "S" in row]
    while next_pos := go_forward(data, path):
        path.append(next_pos)

    print_grid(data, path)
    return path


def is_inside(data: Data, path: list[tuple[int, int]], pos: tuple[int, int]) -> bool:
    # Check to see if point is on path
    if pos in path:
        return False

    # Check to see if point is clearly outside
    i0 = min(i for (i, j) in path if j == pos[1])
    i1 = max(i for (i, j) in path if j == pos[1])
    j0 = min(j for (i, j) in path if i == pos[0])
    j1 = max(j for (i, j) in path if i == pos[0])
    if not i0 < pos[0] < i1:
        return False
    if not j0 < pos[1] < j1:
        return False

    actually_inside = [(3, 14), (4, 7), (4, 8), (4, 9), (5, 7), (5, 8), (6, 6), (6, 14)]

    X, Y = len(data), len(data[0])
    I, J = pos
    l = sum([1 if (I, j) in path else 0 for j in range(0, J)])
    r = sum([1 if (I, j) in path else 0 for j in range(J, Y)])
    u = sum([1 if (i, J) in path else 0 for i in range(0, I)])
    d = sum([1 if (i, J) in path else 0 for i in range(I, X)])
    msg = "".join(
        [
            f"Checking ({pos[0]:>2}, {pos[1]:>2})  ",
            f"l:{l%2:>2}, r:{r%2:>2}, u:{u%2:>2}, d:{d%2:>2}  ",
            f"lr:{(l+r)%2:>2}, ud:{(u+d)%2:>2}, s:{sum([l, r, u, d])%2:>2}  ",
            "ACTUALLY INSIDE" if pos in actually_inside else "",
        ]
    )
    logging.debug(msg)

    return True


def part_1(data: Data) -> int:
    return len(trace_path(data)) // 2


def part_2(data: Data) -> int:
    path = trace_path(data)
    logging.debug(len(path))
    contained = 0

    _data = [
        ["*" if (i, j) in path else "." for j in range(len(data[0]))]
        for i in range(len(data))
    ]

    for i in range(len(data)):
        for j in range(len(data[i])):
            if is_inside(data, path, (i, j)):
                _data[i][j] = "I"
                contained += 1
            else:
                _data[i][j] = "."

    print()
    print_grid(_data, path)
    return contained


def scale(data: Data) -> Data:
    scaled = [
        "".join([data[i][j] + "─" for j in range(len(data[i]))])
        for i in range(len(data))
    ]
    vert = "│" * len(scaled[0])
    scaled = [scaled[i // 2] if i % 2 == 0 else vert for i in range(len(scaled) * 2)]
    return scaled


if __name__ == "__main__":
    data = parse_input()
    data = parse_input(file_name="sample2.txt")
    logging.debug("\n".join(data) + "\n\n")

    # print(f"Part 1: {part_1(data)}")
    # data = scale(data)
    logging.debug("\n".join(data) + "\n\n")
    print(f"Part 2: {part_2(scale(data))}")

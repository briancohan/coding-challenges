from collections import defaultdict
import logging
from pathlib import Path
from typing import NewType
from functools import cmp_to_key


Orders = NewType("Orders", dict[int, set[int]])
Update = NewType("Update", list[int])
Data = NewType("Data", tuple[Orders, list[Update]])

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

    orders: Orders = defaultdict(set)
    updates: list[Update] = []
    for line in input_file.read_text().strip().splitlines():
        if not line:
            continue
        if "|" in line:
            first, second = list(map(int, line.split("|")))
            orders[first].add(second)
        else:
            updates.append(list(map(int, line.split(","))))

    return orders, updates


def split_safe_unsafe(
    orders: Orders,
    updates: list[Update],
) -> tuple[list[Update], list[Update]]:
    safe = []
    unsafe = []

    for update in updates:
        is_safe = True

        for ix, page in enumerate(update):
            if set(update[:ix]) & orders[page]:
                is_safe = False
                break

        if is_safe:
            safe.append(update)
        else:
            unsafe.append(update)

    return safe, unsafe


def part_1(data: Data) -> int:
    orders, updates = data
    safe, _ = split_safe_unsafe(orders, updates)
    return sum([update[len(update) // 2] for update in safe])


def part_2(data: Data) -> int:
    orders, updates = data

    def elf_sort(a: int, b: int) -> int:
        if a in orders[b]:
            return 1
        if b in orders[a]:
            return -1
        return 0

    _, unsafe = split_safe_unsafe(orders, updates)
    fixed = [sorted(update, key=cmp_to_key(elf_sort)) for update in unsafe]
    return sum([update[len(update) // 2] for update in fixed])


if __name__ == "__main__":
    data = parse_input(False)

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

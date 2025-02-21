from collections import Counter
from functools import cmp_to_key, partial
from itertools import zip_longest
from pathlib import Path
from typing import NewType

Data = NewType("Data", list[tuple[str, int]])


def parse_input(full: bool = True, file_name: Path = None) -> Data:
    if file_name is None:
        file_name = "input.txt" if full else "sample.txt"
    input_file = Path(__file__).parent / file_name

    return [
        (line.split()[0], int(line.split()[1]))
        for line in input_file.read_text().splitlines()
    ]


def evaluate_joker(hand: str) -> str:
    if "J" not in hand:
        return hand

    if hand == "JJJJJ":
        return "AAAAA"

    order = "AKQT98765432J"
    options = {k: v for k, v in Counter(hand).items() if k != "J"}
    options = [k for k, v in options.items() if v == max(options.values())]
    options.sort(key=order.index)

    return hand.replace("J", options[0])


def camel_card_sort(a: str, b: str, jokers: bool = False) -> Data:
    a_count = sorted(
        Counter(evaluate_joker(a[0]) if jokers else a[0]).values(),
        reverse=True,
    )
    b_count = sorted(
        Counter(evaluate_joker(b[0]) if jokers else b[0]).values(),
        reverse=True,
    )

    for a_i, b_i in zip_longest(a_count, b_count, fillvalue=float("inf")):
        if a_i > b_i:
            return 1
        elif a_i < b_i:
            return -1

    order = "AKQT98765432J" if jokers else "AKQJT98765432"
    for a_i, b_i in zip(a[0], b[0]):
        if order.index(a_i) > order.index(b_i):
            return -1
        elif order.index(a_i) < order.index(b_i):
            return 1


def part_1(data: Data) -> int:
    data.sort(key=cmp_to_key(camel_card_sort))
    return sum([i * bid for i, (_, bid) in enumerate(data, start=1)])


def part_2(data: Data) -> int:
    data.sort(key=cmp_to_key(partial(camel_card_sort, jokers=True)))
    return sum([i * bid for i, (_, bid) in enumerate(data, start=1)])


if __name__ == "__main__":
    data = parse_input()

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

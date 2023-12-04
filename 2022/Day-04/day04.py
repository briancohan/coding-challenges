from pathlib import Path
from typing import TypeAlias

Range: TypeAlias = tuple[int, int]


def is_subset(a: Range, b: Range) -> bool:
    a_in_b = b[0] <= a[0] <= b[1] and b[0] <= a[1] <= b[1]
    b_in_a = a[0] <= b[0] <= a[1] and a[0] <= b[1] <= a[1]
    return a_in_b or b_in_a


def is_intersection(a: Range, b: Range) -> bool:
    a_in_b = b[0] <= a[0] <= b[1] or b[0] <= a[1] <= b[1]
    b_in_a = a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1]
    return a_in_b or b_in_a


def parse_range(range_str: str) -> tuple[Range, Range]:
    range_a, range_b = range_str.split(",")
    range_a = tuple(map(int, range_a.split("-")))
    range_b = tuple(map(int, range_b.split("-")))
    if not is_subset(range_a, range_b):
        print(range_a, range_b)
    return range_a, range_b


def count_overlaps(data: str) -> int:
    return sum([is_subset(*parse_range(ranges)) for ranges in data.split()])


def count_intersections(data: str) -> int:
    return sum([is_intersection(*parse_range(ranges)) for ranges in data.split()])


if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    data = input_file.read_text().strip()

    print(count_overlaps(data))
    print(count_intersections(data))

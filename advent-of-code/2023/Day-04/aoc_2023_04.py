from pathlib import Path
from typing import NewType

Data = NewType("Data", list[tuple[list[int], list[int]]])


def parse_input(full: bool = True) -> Data:
    input_file = Path(__file__).parent / ("input.txt" if full else "sample.txt")
    return [
        tuple(
            list(map(lambda x: int(x), nums.split()))
            for nums in line.split(":")[1].split("|")
        )
        for line in input_file.read_text().strip().splitlines()
    ]


def part_1(data: str) -> int:
    matches = [len(set(w) & set(m)) for w, m in data]
    return sum(2 ** (m - 1) if m else 0 for m in matches)


def part_2(data: str) -> int:
    matches = [len(set(w) & set(m)) for w, m in data]
    matches = [{"matches": m, "copies": 1} for m in matches]

    for cur_card, match in enumerate(matches):
        for _ in range(match["copies"]):
            for j in range(cur_card, cur_card + match["matches"]):
                matches[j + 1]["copies"] += 1

    return sum(c["copies"] for c in matches)


if __name__ == "__main__":
    data = parse_input()

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

from pathlib import Path
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s",
    filename=Path(__file__).with_suffix(".log"),
    filemode="w",
)


def matching_numbers(card: str) -> int:
    winning, my_nums = [
        list(map(lambda x: int(x), nums.split()))
        for nums in card.split(":")[1].split("|")
    ]
    return len(set(winning) & set(my_nums))


def part_1(data: str) -> int:
    matches = [matching_numbers(card) for card in data.strip().splitlines()]
    return sum(2 ** (m - 1) if m else 0 for m in matches)


def part_2(data):
    matches = [
        {"matches": matching_numbers(card), "copies": 1}
        for card in data.strip().splitlines()
    ]

    for cur_card, match in enumerate(matches):
        for _ in range(match["copies"]):
            for j in range(cur_card, cur_card + match["matches"]):
                matches[j + 1]["copies"] += 1

    return sum(c["copies"] for c in matches)


if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    data = input_file.read_text()

    print(part_1(data))
    print(part_2(data))

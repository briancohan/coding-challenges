from pathlib import Path
import logging
import re

logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s",
    filename=Path(__file__).with_suffix(".log"),
    filemode="w",
)


alpha_nums = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def decode(input: str, convert_alpha: bool = False) -> int:
    """Return the first digit in a string."""

    pattern = r"\d"
    if convert_alpha:
        pattern = r"(\d|one|two|three|four|five|six|seven|eight|nine)"

    match = re.findall(pattern, input)
    return int(
        alpha_nums.get(match[0], match[0]) + alpha_nums.get(match[-1], match[-1])
    )


if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    data = input_file.read_text().splitlines()

    print(sum(decode(line, convert_alpha=False) for line in data))
    print(sum(decode(line, convert_alpha=True) for line in data))

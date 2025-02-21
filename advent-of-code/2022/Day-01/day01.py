from pathlib import Path
from typing import Generator


def get_calories(data: list[str]) -> Generator[int, None, None]:
    calories = 0

    for line in data.split("\n"):
        if line.strip() == "":
            yield calories
            calories = 0
        else:
            calories += int(line.strip())


def get_max_calories(data: list[str]) -> int:
    return max(get_calories(data))


def get_top_calories(data: list[str], top: int = 3) -> list[int]:
    calories = sorted(get_calories(data), reverse=True)
    return calories[:top]


if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    data = input_file.read_text()
    print(get_max_calories(data))

    top_calories = get_top_calories(data)
    print(sum(top_calories))

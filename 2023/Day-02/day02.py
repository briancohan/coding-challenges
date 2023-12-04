from pathlib import Path
import logging
from itertools import batched
from math import prod

logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s",
    filename=Path(__file__).with_suffix(".log"),
    filemode="w",
)


def parse_game(input: str) -> list:
    game_id, bag = input.split(":")

    game_id = int(game_id.split(" ")[1])

    pulls = [
        dict([(c, int(n)) for n, c in batched(pull.split(), 2)])
        for pull in bag.replace(",", "").split(";")
    ]
    return game_id, pulls


def possible_game(game: list[dict[str, int]], cubes: dict[str, int]) -> bool:
    for pull in game:
        for color, count in pull.items():
            if count > cubes[color]:
                return False
    return True


def game_power(game: list[dict[str, int]]) -> int:
    n_cubes = game[0]
    for pull in game[1:]:
        for color, count in pull.items():
            if color in n_cubes and count > n_cubes[color]:
                n_cubes[color] = count
            elif color not in n_cubes:
                n_cubes[color] = count
    return prod(n_cubes.values())


def part_1(data: list[str], cubes: dict[str, int]) -> int:
    games = [parse_game(line) for line in data]
    possible_games = [game for game, pulls in games if possible_game(pulls, cubes)]
    return sum(possible_games)


def part_2(data: list[str]) -> int:
    games = [parse_game(line) for line in data]
    return sum(game_power(pulls) for _, pulls in games)


if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    data = input_file.read_text().splitlines()

    cubes = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    print(part_1(data, cubes))
    print(part_2(data))

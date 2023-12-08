from itertools import batched
from math import prod
from pathlib import Path
from typing import NewType

Data = NewType("Data", dict[int, list[dict[str, int]]])


def parse_input(full: bool = True, file_name: Path = None) -> Data:
    if file_name is None:
        file_name = "input.txt" if full else "sample.txt"
    input_file = Path(__file__).parent / file_name

    games = dict()
    for line in input_file.read_text().strip().splitlines():
        game_id, bag = line.split(":")

        game_id = int(game_id.split(" ")[1])

        pulls = [
            dict([(color, int(n)) for n, color in batched(pull.split(), 2)])
            for pull in bag.replace(",", "").split(";")
        ]
        games[game_id] = pulls

    return games


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


def part_1(data: list[str]) -> int:
    cubes = {"red": 12, "green": 13, "blue": 14}
    possible_games = [
        game for game, pulls in data.items() if possible_game(pulls, cubes)
    ]
    return sum(possible_games)


def part_2(data: list[str]) -> int:
    return sum(game_power(pulls) for _, pulls in data.items())


if __name__ == "__main__":
    data = parse_input()

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")

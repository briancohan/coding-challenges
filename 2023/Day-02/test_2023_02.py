import pytest
import day02

sample_input = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".strip().splitlines()


def test_correct_game_id():
    game_id, cubes = day02.parse_game(sample_input[0])

    expected_game_id = 1
    assert game_id == expected_game_id

    expected_cubes = [
        {"blue": 3, "red": 4},
        {"red": 1, "green": 2, "blue": 6},
        {"green": 2},
    ]
    assert cubes == expected_cubes


def test_correct_score_for_part_1():
    cubes = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    expected_score = 8
    assert day02.part_1(sample_input, cubes) == expected_score


def test_correct_score_for_part_2():
    expected_score = 2286
    assert day02.part_2(sample_input) == expected_score

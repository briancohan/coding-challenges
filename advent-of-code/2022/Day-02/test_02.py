import day02
import pytest

sample_input = """
A Y
B X
C Z
"""


@pytest.mark.parametrize(
    "opponent_selection, my_selection, expected_score",
    [
        ("A", "Y", 8),
        ("B", "X", 1),
        ("C", "Z", 6),
    ],
)
def test_score_round_correctly(
    opponent_selection: str, my_selection: str, expected_score: int
):
    _my_selection = day02.Shape.decode(my_selection)
    _opponent_selection = day02.Shape.decode(opponent_selection)
    assert day02.score_round(_my_selection, _opponent_selection) == expected_score


def test_correct_tournament_score():
    rounds = sample_input.strip().split("\n")
    assert day02.score_tournament(rounds, day02.Strategy.DECODE) == 15


def test_select_correct_shape_based_on_opponent_and_desired_outcome():
    assert day02.Shape.ROCK.will_win_against() == day02.Shape.SCISSORS
    assert day02.Shape.PAPER.will_win_against() == day02.Shape.ROCK
    assert day02.Shape.SCISSORS.will_win_against() == day02.Shape.PAPER

    assert day02.Shape.ROCK.will_lose_against() == day02.Shape.PAPER
    assert day02.Shape.PAPER.will_lose_against() == day02.Shape.SCISSORS
    assert day02.Shape.SCISSORS.will_lose_against() == day02.Shape.ROCK

    assert day02.Shape.ROCK.will_draw_against() == day02.Shape.ROCK
    assert day02.Shape.PAPER.will_draw_against() == day02.Shape.PAPER
    assert day02.Shape.SCISSORS.will_draw_against() == day02.Shape.SCISSORS


def test_shape_enum_comparisons():
    assert day02.Shape.ROCK == day02.Shape.ROCK
    assert day02.Shape.PAPER == day02.Shape.PAPER
    assert day02.Shape.SCISSORS == day02.Shape.SCISSORS

    assert day02.Shape.ROCK < day02.Shape.PAPER
    assert day02.Shape.PAPER < day02.Shape.SCISSORS
    assert day02.Shape.SCISSORS < day02.Shape.ROCK


def test_correct_modified_tournament_score():
    rounds = sample_input.strip().split("\n")
    assert day02.score_tournament(rounds, day02.Strategy.PICK) == 12

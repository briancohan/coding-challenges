from pathlib import Path
from enum import Enum


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __lt__(self, other) -> bool:
        if self == self.ROCK:
            return other == self.PAPER
        elif self == self.PAPER:
            return other == self.SCISSORS
        elif self == self.SCISSORS:
            return other == self.ROCK

    def will_win_against(self):
        if self == self.ROCK:
            return self.SCISSORS
        elif self == self.PAPER:
            return self.ROCK
        elif self == self.SCISSORS:
            return self.PAPER

    def will_lose_against(self):
        if self == self.ROCK:
            return self.PAPER
        elif self == self.PAPER:
            return self.SCISSORS
        elif self == self.SCISSORS:
            return self.ROCK

    def will_draw_against(self):
        return self

    @staticmethod
    def decode(code: str):
        return {
            "A": Shape.ROCK,
            "B": Shape.PAPER,
            "C": Shape.SCISSORS,
            "X": Shape.ROCK,
            "Y": Shape.PAPER,
            "Z": Shape.SCISSORS,
        }[code]


class Strategy(Enum):
    """Strategies to use to pick the shape for the round.

    DECODE: Decode the shape from the input.
    PICK: Pick the shape based on the opponent's shape and desired outcome.
    """

    DECODE = 1
    PICK = 2


def score_round(my_selection: Shape, opponent_selection: Shape) -> int:
    """Calculates the score based on outcome and what shape was used.

    Win: 6, Draw: 3, Loose: 0
    Rock: 1, Paper: 2, Scissors: 3 (as defined in Shape enum)
    """
    if my_selection > opponent_selection:
        return 6 + my_selection.value
    elif my_selection == opponent_selection:
        return 3 + my_selection.value
    elif my_selection < opponent_selection:
        return 0 + my_selection.value


def decode_round(round: str, strategy: Strategy) -> tuple[Shape, Shape]:
    """Determine shapes in play based on the round and strategy."""
    opponent_key, my_key = round.split()
    opponent_selection = Shape.decode(opponent_key)

    if strategy == Strategy.DECODE:
        my_selection = Shape.decode(my_key)

    elif strategy == Strategy.PICK:
        if my_key == "X":  # Loose
            my_selection = opponent_selection.will_win_against()
        elif my_key == "Y":  # Draw
            my_selection = opponent_selection.will_draw_against()
        elif my_key == "Z":  # Win
            my_selection = opponent_selection.will_lose_against()

    return opponent_selection, my_selection


def score_tournament(rounds: list[str], strategy: Strategy) -> int:
    my_score = 0

    for round in rounds:
        opponent_selection, my_selection = decode_round(round, strategy)
        my_score += score_round(my_selection, opponent_selection)

    return my_score


if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    rounds = input_file.read_text().strip().split("\n")

    score = score_tournament(rounds, Strategy.DECODE)
    print(score)

    score = score_tournament(rounds, Strategy.PICK)
    print(score)

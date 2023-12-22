import day03
import pytest

sample_input = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


@pytest.mark.parametrize(
    "input, expected",
    [
        ("vJrwpWtwJgWrhcsFMMfFFhFp", "p"),
        ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "L"),
        ("PmmdzqPrVvPwwTWBwg", "P"),
        ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "v"),
        ("ttgJtRGJQctTZtZT", "t"),
        ("CrZsJsPPZsGzwwsLwLmpwMDw", "s"),
    ],
)
def test_duplicate_item_found(input, expected):
    assert day03.find_duplicate_item(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("p", 16),
        ("L", 38),
        ("P", 42),
        ("v", 22),
        ("t", 20),
        ("s", 19),
    ],
)
def test_get_item_priority(input, expected):
    assert day03.get_item_priority(input) == expected


def test_score_packlist():
    assert day03.score_packlist(sample_input.split()) == 157


def test_find_correct_badge():
    assert day03.find_group_badge(sample_input.split()[:3]) == "r"
    assert day03.find_group_badge(sample_input.split()[3:]) == "Z"


def test_score_packlist_groups():
    assert day03.score_packlist_groups(sample_input.split()) == 70

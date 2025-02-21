import day04
import pytest

sample_input = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


def test_is_subset_when_fully_contained():
    range_a = (3, 4)
    range_b = (2, 5)
    assert day04.is_subset(range_a, range_b) == True
    assert day04.is_subset(range_b, range_a) == True


def test_is_subset_with_same_starting_number():
    range_a, range_b = (4, 5), (4, 8)
    assert day04.is_subset(range_a, range_b) == True
    assert day04.is_subset(range_b, range_a) == True


def test_is_subset_with_same_ending_number():
    range_a, range_b = (3, 8), (4, 8)
    assert day04.is_subset(range_a, range_b) == True
    assert day04.is_subset(range_b, range_a) == True


def test_is_not_subset():
    range_a = (2, 4)
    range_b = (3, 5)
    assert day04.is_subset(range_a, range_b) == False
    assert day04.is_subset(range_b, range_a) == False


@pytest.mark.parametrize(
    "range_str, expected",
    [
        ("2-4,6-8", ((2, 4), (6, 8))),
        ("2-3,4-5", ((2, 3), (4, 5))),
        ("5-7,7-9", ((5, 7), (7, 9))),
        ("2-8,3-7", ((2, 8), (3, 7))),
        ("6-6,4-6", ((6, 6), (4, 6))),
        ("2-6,4-8", ((2, 6), (4, 8))),
    ],
)
def test_parse_range(range_str, expected):
    assert day04.parse_range(range_str) == expected


def test_correct_number_of_overlaps_found():
    overlaps = day04.count_overlaps(sample_input)
    assert overlaps == 2


def test_correct_number_of_intersections_found():
    intersections = day04.count_intersections(sample_input)
    assert intersections == 4

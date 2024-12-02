import aoc_2024_02 as challenge
import pytest

sample_input = challenge.parse_input(full=False)
full_input = challenge.parse_input()


def test_part_1_sample_input():
    result = challenge.part_1(sample_input)
    assert result == 2


def test_part_1_full_input():
    result = challenge.part_1(full_input)
    assert result == 559


def test_part_2_sample_input():
    result = challenge.part_2(sample_input)
    assert result == 4


def test_part_2_full_input():
    result = challenge.part_2(full_input)
    assert result == 601


def test__is_safe__when_slowly_increasing():
    assert challenge.is_safe("1 2 3 4 5") is True


def test__is_safe__when_slowly_decreasing():
    assert challenge.is_safe("5 4 3 2 1") is True


def test__is_not_safe__with_duplicates():
    assert challenge.is_safe("1 2 3 4 4") is False


def test__is_not_safe__when_jumping():
    assert challenge.is_safe("1 7") is False


def test__is_not_safe__when_meandering():
    assert challenge.is_safe("1 3 2 4") is False


@pytest.mark.parametrize(
    "report",
    [
        ("1 2 2 3"),  # Remove the first 2.
        ("1 2 8"),  # Remove the 8.
        ("1 3 2 4 5"),  # Remove the 3.
        ("8 6 4 4 1"),  # Remove either 4.
        ("2 1 2 3 4"),  # Remove the first 2.
    ],
)
def test__is_safe__with_dampening(report):
    assert challenge.is_safe(report, dampen=True) is True

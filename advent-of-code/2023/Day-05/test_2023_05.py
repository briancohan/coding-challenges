import aoc_2023_05 as challenge
import pytest

sample_input = challenge.parse_input(full=False)
full_input = challenge.parse_input()


def test_part_1_sample_input():
    result = challenge.part_1(sample_input)
    assert result == 35


def test_part_1_full_input():
    result = challenge.part_1(full_input)
    assert result == 84470622


def test_part_2_sample_input():
    result = challenge.part_2(sample_input)
    assert result == 46


@pytest.mark.skip(reason="Takes ~1 hr")
def test_part_2_full_input():
    result = challenge.part_2(full_input)
    assert result == 26714516

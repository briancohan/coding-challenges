import pytest
import day06 as day

sample_input = """
Time:      7  15   30
Distance:  9  40  200
"""


def test_correct_answer_part_1():
    result = day.part_1(sample_input)
    expected = 288
    assert result == expected


# Part 1 = 32076


def test_correct_answer_part_2():
    result = day.part_2(sample_input)
    expected = 71503
    assert result == expected


# Part 2 = 34278221

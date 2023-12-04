import pytest
import day03

sample_input = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def test_correct_answer_part_1():
    result = day03.part_1(sample_input)
    expected = 4361
    assert result == expected


# Part 1 = 544433


def test_correct_answer_part_2():
    result = day03.part_2(sample_input)
    expected = 467835
    assert result == expected


# Part 2 = 76314915

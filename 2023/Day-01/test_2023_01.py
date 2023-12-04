import pytest
import day01

sample_input = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""


@pytest.mark.parametrize(
    "input, expected",
    [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
    ],
)
def test_get_digit(input, expected):
    """Test that the first and last digits are returned."""
    assert day01.get_digit(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
        ("twone3", 23),
        ("nineeighttworhtvxdtxp8twoneh", 92),
        ("twospxvtbcjfour3seven", 27),
    ],
)
def test_get_digit_with_alpha(input, expected):
    """Test that the first and last digits are returned."""
    assert day01.get_digit(input, convert_alpha=True) == expected


# 54868 - too low

import aoc_2023_02 as challenge

sample_input = challenge.parse_input(full=False)
full_input = challenge.parse_input()


def test_part_1_sample_input():
    result = challenge.part_1(sample_input)
    assert result == 8


def test_part_1_full_input():
    result = challenge.part_1(full_input)
    assert result == 2207


def test_part_2_sample_input():
    result = challenge.part_2(sample_input)
    assert result == 2286


def test_part_2_full_input():
    result = challenge.part_2(full_input)
    assert result == 62241

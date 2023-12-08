import aoc_2023_04 as challenge

sample_input = challenge.parse_input(full=False)
full_input = challenge.parse_input(full=True)


def test_part_1_sample_input():
    result = challenge.part_1(sample_input)
    assert result == 13


def test_part_1_full_input():
    result = challenge.part_1(full_input)
    assert result == 21485


def test_part_2_sample_input():
    result = challenge.part_2(sample_input)
    assert result == 30


def test_part_2_full_input():
    result = challenge.part_2(full_input)
    assert result == 11024379

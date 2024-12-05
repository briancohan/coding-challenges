import aoc_2024_05 as challenge

sample_input = challenge.parse_input(full=False)
full_input = challenge.parse_input()


def test_part_1_sample_input():
    result = challenge.part_1(sample_input)
    assert result == 143


def test_part_1_full_input():
    result = challenge.part_1(full_input)
    assert result == 6612


def test_part_2_sample_input():
    result = challenge.part_2(sample_input)
    assert result == 123


def test_part_2_full_input():
    result = challenge.part_2(full_input)
    assert result == 4944

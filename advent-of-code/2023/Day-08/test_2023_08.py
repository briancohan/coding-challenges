import aoc_2023_08 as challenge

sample_input = challenge.parse_input(full=False)
sample_input2 = challenge.parse_input(file_name="sample2.txt")
full_input = challenge.parse_input()


def test_part_1_sample_input():
    result = challenge.part_1(sample_input)
    assert result == 2


def test_part_1_full_input():
    result = challenge.part_1(full_input)
    assert result == 15989


def test_part_2_sample_input():
    result = challenge.part_2(sample_input2)
    assert result == 6


def test_part_2_full_input():
    result = challenge.part_2(full_input)
    assert result == 13830919117339

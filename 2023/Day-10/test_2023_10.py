import aoc_2023_10 as challenge

sample_input = challenge.parse_input(full=False)
sample_input2 = challenge.parse_input(file_name="sample2.txt")
full_input = challenge.parse_input()


def test_part_1_sample_input():
    result = challenge.part_1(sample_input)
    assert result == 8


def test_part_1_full_input():
    result = challenge.part_1(full_input)
    assert result == 7145


def test_part_2_sample_input():
    result = challenge.part_2(sample_input2)
    assert result == 10


def test_part_2_full_input():
    result = challenge.part_2(full_input)
    assert result == 0


# 557 too high

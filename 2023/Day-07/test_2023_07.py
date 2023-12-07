import aoc_2023_07 as challenge

sample_input = challenge.parse_input(full=False)
full_input = challenge.parse_input()


def test_part_1_sample_input():
    result = challenge.part_1(sample_input)
    assert result == 6440


def test_part_1_full_input():
    result = challenge.part_1(full_input)
    assert result == 253910319


def test_part_2_sample_input():
    result = challenge.part_2(sample_input)
    assert result == 5905


def test_part_2_full_input():
    result = challenge.part_2(full_input)
    assert result == 254083736

import aoc_2024_04 as challenge

sample_input = challenge.parse_input(full=False)
full_input = challenge.parse_input()


def test_part_1_sample_input():
    result = challenge.part_1(sample_input)
    assert result == 18


def test_part_1_full_input():
    result = challenge.part_1(full_input)
    assert result == 2468


def test_part_2_sample_input():
    result = challenge.part_2(sample_input)
    assert result == 9


def test_part_2_full_input():
    result = challenge.part_2(full_input)
    assert result == 1864


def test_set_equality():
    assert {"s", "m"} == {"m", "s"}

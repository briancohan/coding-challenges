import aoc_2023_12 as challenge

sample_input = challenge.parse_input(full=False)
full_input = challenge.parse_input()


def test_part_1_sample_input():
    result = challenge.part_1(sample_input)
    assert result == 21


def test_part_1_full_input():
    result = challenge.part_1(full_input)
    assert result == 7307


def test_part_2_sample_input():
    result = challenge.part_2(sample_input)
    assert result == 525152


def test_part_2_full_input():
    result = challenge.part_2(full_input)
    assert result == 0


def test_arr():
    arr = [1, 2, 3]
    assert arr * 3 == [1, 2, 3, 1, 2, 3, 1, 2, 3]

    s0 = ".??..??...?##."
    s1 = ".??..??...?##.?.??..??...?##.?.??..??...?##."
    assert "?".join([s0] * 3) == s1

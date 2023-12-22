import aoc_2023_17 as challenge

sample_input = challenge.parse_input(full=False)
full_input = challenge.parse_input()


def test_part_1_sample_input():
    result = challenge.part_1(sample_input)
    assert result == 102


def test_part_1_full_input():
    result = challenge.part_1(full_input)
    assert result == 0


# 1140 too high


def test_part_2_sample_input():
    result = challenge.part_2(sample_input)
    assert result == 0


def test_part_2_full_input():
    result = challenge.part_2(full_input)
    assert result == 0


def test_short_trajectory():
    trajectory = [(0, 0)]
    node = (0, 1)
    result = challenge.is_legal(trajectory, node)
    assert result is True


def test_legal_trajectory():
    trajectory = [(0, 0), (0, 1)]
    node = (2, 1)
    result = challenge.is_legal(trajectory, node)
    assert result is True


def test_illegal_trajectory():
    trajectory = [(0, 0), (0, 1)]
    node = (0, 2)
    result = challenge.is_legal(trajectory, node)
    assert result is False

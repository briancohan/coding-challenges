import aoc_2023_16 as challenge
import pytest

sample_input = challenge.parse_input(full=False)
full_input = challenge.parse_input()


def test_part_1_sample_input():
    result = challenge.part_1(sample_input)
    assert result == 46


def test_part_1_full_input():
    result = challenge.part_1(full_input)
    assert result == 7979


def test_part_2_sample_input():
    result = challenge.part_2(sample_input)
    assert result == 51


def test_part_2_full_input():
    result = challenge.part_2(full_input)
    assert result == 8437


@pytest.mark.parametrize(
    argnames=["direction", "expected"],
    argvalues=[
        (">", [challenge.Node(0, 1, ">")]),
        ("<", [challenge.Node(0, -1, "<")]),
        ("^", [challenge.Node(-1, 0, "^")]),
        ("v", [challenge.Node(1, 0, "v")]),
    ],
    ids=["right", "left", "up", "down"],
)
def test_dot(direction, expected):
    node = challenge.Node(0, 0, direction)
    next_nodes = challenge.get_next(node, ["."])
    assert next_nodes == expected


@pytest.mark.parametrize(
    argnames=["direction", "expected"],
    argvalues=[
        (">", [challenge.Node(0, 1, ">")]),
        ("<", [challenge.Node(0, -1, "<")]),
        ("^", [challenge.Node(0, -1, "<"), challenge.Node(0, 1, ">")]),
        ("v", [challenge.Node(0, -1, "<"), challenge.Node(0, 1, ">")]),
    ],
    ids=["right", "left", "up", "down"],
)
def test_dash(direction, expected):
    node = challenge.Node(0, 0, direction)
    next_nodes = challenge.get_next(node, ["-"])
    assert next_nodes == expected


@pytest.mark.parametrize(
    argnames=["direction", "expected"],
    argvalues=[
        (">", [challenge.Node(-1, 0, "^"), challenge.Node(1, 0, "v")]),
        ("<", [challenge.Node(-1, 0, "^"), challenge.Node(1, 0, "v")]),
        ("^", [challenge.Node(-1, 0, "^")]),
        ("v", [challenge.Node(1, 0, "v")]),
    ],
    ids=["right", "left", "up", "down"],
)
def test_pipe(direction, expected):
    node = challenge.Node(0, 0, direction)
    next_nodes = challenge.get_next(node, ["|"])
    assert next_nodes == expected


@pytest.mark.parametrize(
    argnames=["direction", "expected"],
    argvalues=[
        (">", [challenge.Node(-1, 0, "^")]),
        ("<", [challenge.Node(1, 0, "v")]),
        ("^", [challenge.Node(0, 1, ">")]),
        ("v", [challenge.Node(0, -1, "<")]),
    ],
    ids=["right", "left", "up", "down"],
)
def test_fslash(direction, expected):
    node = challenge.Node(0, 0, direction)
    next_nodes = challenge.get_next(node, ["/"])
    assert next_nodes == expected


@pytest.mark.parametrize(
    argnames=["direction", "expected"],
    argvalues=[
        (">", [challenge.Node(1, 0, "v")]),
        ("<", [challenge.Node(-1, 0, "^")]),
        ("^", [challenge.Node(0, -1, "<")]),
        ("v", [challenge.Node(0, 1, ">")]),
    ],
    ids=["right", "left", "up", "down"],
)
def test_bslash(direction, expected):
    node = challenge.Node(0, 0, direction)
    next_nodes = challenge.get_next(node, ["\\"])
    assert next_nodes == expected

import day05
import pytest

sample_input = """
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


def test_towers_processed():
    expected = {
        1: ["Z", "N"],
        2: ["M", "C", "D"],
        3: ["P"],
    }
    result = day05.process_towers(sample_input)
    print(result)
    assert result == expected


def test_instructions_processed():
    expected = [
        day05.Instruction(qty=1, from_tower=2, to_tower=1),
        day05.Instruction(qty=3, from_tower=1, to_tower=3),
        day05.Instruction(qty=2, from_tower=2, to_tower=1),
        day05.Instruction(qty=1, from_tower=1, to_tower=2),
    ]
    result = day05.process_instructions(sample_input)
    print(result)
    assert result == expected


def test_rearranged_moving_one_at_a_time():
    expected = {
        1: ["C"],
        2: ["M"],
        3: ["P", "D", "N", "Z"],
    }
    towers = day05.process_towers(sample_input)
    instructions = day05.process_instructions(sample_input)
    day05.rearrange_towers(towers, instructions, 9000)
    assert towers == expected


def test_rearranged_moving_one_stack_at_a_time():
    expected = {
        1: ["M"],
        2: ["C"],
        3: ["P", "Z", "N", "D"],
    }
    towers = day05.process_towers(sample_input)
    instructions = day05.process_instructions(sample_input)
    day05.rearrange_towers(towers, instructions, 9001)
    assert towers == expected

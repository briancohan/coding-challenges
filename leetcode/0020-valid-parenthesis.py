# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pytest",
# ]
# ///
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Constraints:
- 1 <= s.length <= 104
- s consists of parentheses only '()[]{}'.

Topics:
- String
- Stack
"""

import pytest


class Solution(object):
    def isValid(self, s: str) -> bool:
        table = {")": "(", "]": "[", "}": "{"}
        stack = ""
        for char in s:
            if char in "([{":
                stack += char
            elif stack and stack[-1] == table[char]:
                stack = stack[:-1]
            else:
                return False

        return not stack


@pytest.mark.parametrize(
    "input, expected",
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("[", False),
        ("]", False),
    ],
)
def test_examples(input, expected) -> None:
    solution = Solution()
    assert solution.isValid(input) == expected

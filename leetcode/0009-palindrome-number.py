# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pytest",
# ]
# ///
"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Constraints:
- -231 <= x <= 231 - 1

Topics:
- Math
"""

import pytest


class Solution(object):
    def fisPalindromenc(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


@pytest.mark.parametrize(
    "input, expected",
    [
        (121, True),
        (-121, False),
        (10, False),
    ],
)
def test_examples(input, expected) -> None:
    solution = Solution()
    assert solution.fisPalindromenc(input) == expected

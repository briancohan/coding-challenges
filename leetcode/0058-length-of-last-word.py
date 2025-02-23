# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pytest",
# ]
# ///
"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Constraints:
- 1 <= s.length <= 104
- s consists of only English letters and spaces ' '.
- There will be at least one word in s.

Topics:
- String
"""

import pytest


class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.split()[-1])


@pytest.mark.parametrize(
    "input, expected",
    [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
    ],
)
def test_examples(input: str, expected: int) -> None:
    solution = Solution()
    assert solution.lengthOfLastWord(input) == expected

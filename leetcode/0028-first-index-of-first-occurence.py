# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pytest",
# ]
# ///
"""
Given two strings needle and haystack, return the index of the first occurrence of needle
in haystack, or -1 if needle is not part of haystack.

Constraints:
- 1 <= haystack.length, needle.length <= 104
- haystack and needle consist of only lowercase English characters.

Topics:
- Two Pointers
- String
- String Matching
"""

import pytest


class Solution(object):
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.index(needle) if needle in haystack else -1


@pytest.mark.parametrize(
    "input, expected",
    [
        (("sadbutsad", "sad"), 0),
        (("leetcode", "leeto"), -1),
    ],
)
def test_examples(input, expected) -> None:
    solution = Solution()
    assert solution.strStr(*input) == expected

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pytest",
# ]
# ///
"""
Given a string s, find the length of the longest substring without duplicate characters.

Constraints:
- 0 <= s.length <= 5 * 104
- s consists of English letters, digits, symbols and spaces.

Topics:
- Hash Table
- String
- Sliding Window

Explanation
- Starting at the beginning of the string, iterate through each position.
- Keep track of the last time you saw each character
- If the character is new, then you know it's unique and the span between the left
  marker and the index will increase
- If the character has been seen before, move the left marker to after the previous
  instance.
- Keep track of what the longest distance has been.
"""

import pytest


class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(set(s)) == len(s):
            return len(s)

        left = 0
        max_length = 0
        seen = {}

        for ix in range(len(s)):
            char = s[ix]
            # Check if we need to move the left marker
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            # Update the table for char
            seen[char] = ix
            # Compute running max length
            max_length = max(max_length, ix - left + 1)

        return max_length


@pytest.mark.parametrize(
    "input, expected",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("aab", 2),
    ],
)
def test_examples(input: str, expected: int) -> None:
    solution = Solution()
    assert solution.lengthOfLongestSubstring(input) == expected

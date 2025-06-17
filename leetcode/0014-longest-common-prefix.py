# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pytest",
# ]
# ///
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters if it is non-empty.

Topics:
- String
- Trie
"""

import pytest


class Solution(object):
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]
        if not prefix:
            return ""

        for _str in strs[1:]:
            if not _str:
                return ""
            ix = 0
            for ix, (s, p) in enumerate(zip(_str, prefix)):
                if s != p:
                    break
            else:
                ix += 1

            prefix = prefix[:ix]

        return prefix


@pytest.mark.parametrize(
    "input, expected",
    [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["ab", "a"], "a"),
        (["abab", "aba", ""], ""),
    ],
)
def test_examples(input, expected) -> None:
    solution = Solution()
    assert solution.longestCommonPrefix(input) == expected

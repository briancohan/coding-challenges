# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pytest",
# ]
# ///
"""
Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.

Constraints:
- 2 <= nums.length <= 104
- -109 <= nums[i] <= 109
- -109 <= target <= 109
- Only one valid answer exists.

Topics:
- Array
- Hash Table
"""

import pytest


class Solution(object):
    def twoSum(self, nums, target):
        mapping = {n: i for i, n in enumerate(nums)}

        for ix1, n in enumerate(nums):
            ix2 = mapping.get(target - n, None)
            if ix2 and ix1 != ix2:
                return sorted([ix1, ix2])


@pytest.mark.parametrize(
    "input, expected",
    [
        (([2, 7, 11, 15], 9), [0, 1]),
        (([3, 2, 4], 6), [1, 2]),
        (([3, 3], 6), [0, 1]),
        (([1, 3, 4, 2], 6), [2, 3])
    ],
)
def test_examples(input, expected) -> None:
    solution = Solution()
    assert solution.twoSum(*input) == expected

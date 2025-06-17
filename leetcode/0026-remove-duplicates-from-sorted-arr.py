# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pytest",
# ]
# ///
"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.


Constraints:
- 1 <= nums.length <= 3 * 104
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order.

Topics:
- Array
- Two Pointers
"""

import pytest


class Solution(object):
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        for ix in range(1, len(nums)):
            if nums[ix] > nums[ix - 1]:
                nums[k] = nums[ix]
                k += 1

        return k


@pytest.mark.parametrize(
    "input, expected, k",
    [
        ([1, 1, 2], [1, 2], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4], 5),
    ],
)
def test_examples(input, expected, k) -> None:
    solution = Solution()
    assert solution.removeDuplicates(input) == k
    assert input[:k] == expected[:k]

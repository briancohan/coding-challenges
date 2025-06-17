# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pytest",
# ]
# ///
"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Constraints:
- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -106 <= nums1[i], nums2[i] <= 106

Topics:
- Array
- Binary Search
- Divide and Conquer
"""

import pytest


class Solution(object):
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        l1, l2 = len(nums1), len(nums2)
        mid = (l1 + l2) / 2
        stop = int(mid // 1 if mid % 1 else mid) + 1

        ix1, ix2 = 0, 0
        a, b = 0, 0
        while ix1 < l1 and ix2 < l2 and (ix1 + ix2) < stop:
            if nums1[ix1] < nums2[ix2]:
                a, b = b, nums1[ix1]
                ix1 += 1
            else:
                a, b = b, nums2[ix2]
                ix2 += 1

        while ix1 < l1 and (ix1 + ix2) < stop:
            a, b = b, nums1[ix1]
            ix1 += 1

        while ix2 < l2 and (ix1 + ix2) < stop:
            a, b = b, nums2[ix2]
            ix2 += 1

        if mid % 1:
            return b
        return (a + b) / 2

    def findMedianSortedArrays_more_efficient(
        self, nums1: list[int], nums2: list[int]
    ) -> float:
        arr = sorted(nums1 + nums2)
        mid = len(arr) // 2

        if len(arr) % 2:
            return arr[mid]
        return (arr[mid] + arr[mid - 1]) / 2


@pytest.mark.parametrize(
    "input, expected",
    [
        (([1, 3], [2]), 2.0),
        (([1, 2], [3, 4]), 2.5),
        (([], [1]), 1.0),
        (([1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), 9.0),
    ],
)
def test_examples(input, expected) -> None:
    solution = Solution()
    assert solution.findMedianSortedArrays(*input) == expected
    assert solution.findMedianSortedArrays_more_efficient(*input) == expected

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pytest",
# ]
# ///
"""
<Description>

Constraints:
-

Topics:
-
"""

import pytest


class Solution(object):
    def func(self): ...


@pytest.mark.parametrize(
    "input, expected",
    [],
)
def test_examples(input, expected) -> None:
    solution = Solution()
    assert solution.func(*input) == expected

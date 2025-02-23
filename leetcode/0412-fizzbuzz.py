# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pytest",
# ]
# ///
"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Constraints:
- 1 <= n <= 104

Topics:
- Math
- String
- Simulation
"""

import pytest


class Solution(object):
    def fizzBuzz(self, n: int) -> list[str]:
        arr = [str(i) for i in range(1, n + 1)]

        for interval, word in ((3, "Fizz"), (5, "Buzz"), (15, "FizzBuzz")):
            for i in range(interval - 1, n, interval):
                arr[i] = word

        return arr


print(Solution().fizzBuzz(300))


@pytest.mark.parametrize(
    "input, expected",
    [
        (3, ["1", "2", "Fizz"]),
        (5, ["1", "2", "Fizz", "4", "Buzz"]),
        (
            15,
            [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz",
            ],
        ),
    ],
)
def test_examples(input: int, expected: list[str]) -> None:
    solution = Solution()
    assert solution.fizzBuzz(input) == expected

"""
Problem: Convert Integer to the Sum of Two No-Zero Integers
Date: 08-09-2024
Difficulty: Easy
Time taken: ~1 minute
Link: https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
"""

from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        check = lambda x: "0" not in str(x)
        for i in range(1, n):
            j = n - i
            if check(i) and check(j):
                return [i, j]

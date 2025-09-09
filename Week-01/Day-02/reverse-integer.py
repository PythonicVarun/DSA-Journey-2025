"""
Problem: Reverse Integer
Date: 09-09-2024
Difficulty: Easy
Time taken: ~1 minute
Link: https://leetcode.com/problems/reverse-integer/
"""

class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        INT32_MIN = -(2**31)
        INT32_MAX = -INT32_MIN - 1

        neg = x.startswith("-")
        res = int((x[:0:-1] if neg else x[::-1])) * (-1 if neg else 1)
        return res * (1 if INT32_MIN <= res <= INT32_MAX else 0)

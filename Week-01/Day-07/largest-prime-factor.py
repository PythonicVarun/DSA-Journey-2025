"""
Problem: Largest prime factor
Date: 14-09-2025
Difficulty: Medium
Time taken: ~2 minutes
Link: https://www.geeksforgeeks.org/problems/largest-prime-factor2601/1
"""


class Solution:
    def largestPrimeFactor(self, n):
        # code here
        factor = 2
        while factor * factor <= n:
            if n % factor == 0:
                n //= factor
            else:
                factor += 1
        return n

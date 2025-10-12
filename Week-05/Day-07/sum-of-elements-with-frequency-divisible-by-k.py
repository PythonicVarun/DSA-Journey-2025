"""
Problem: Sum of Elements With Frequency Divisible by K
Date: 12-10-2025
Difficulty: Easy
Time taken: ~30 seconds
Link: https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k
"""

from collections import Counter
from typing import List


class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        res = 0
        cntr = Counter(nums)
        for i, j in cntr.items():
            if j % k == 0:
                res += j * i
        return res

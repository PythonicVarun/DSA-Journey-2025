"""
Problem: Find Triangular Sum of an Array
Date: 30-09-2025
Difficulty: Medium
Time taken: ~30 minutes
Link: https://leetcode.com/problems/find-triangular-sum-of-an-array
"""

from math import comb
from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            res = (res + comb(n - 1, i) * nums[i]) % 10
        return res

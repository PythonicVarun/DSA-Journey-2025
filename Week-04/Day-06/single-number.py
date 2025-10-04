"""
Problem: Single Number
Date: 04-10-2025
Difficulty: Easy
Time taken: ~15 minutes
Link: https://leetcode.com/problems/single-number
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res

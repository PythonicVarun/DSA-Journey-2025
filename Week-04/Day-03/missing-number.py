"""
Problem: Missing Number
Date: 01-10-2025
Difficulty: Easy
Time taken: ~1 minute
Link: https://leetcode.com/problems/missing-number
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return list(set(range(len(nums) + 1)) - set(nums))[0]

"""
Problem: Two Sum
Date: 15-09-2025
Difficulty: Easy
Time taken: ~1 minute
Link: https://leetcode.com/problems/two-sum/
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dp = {}
        for i, num in enumerate(nums):
            if target - num in dp:
                return list(sorted([i, dp[target - num]]))
            dp[num] = i

"""
Problem: Max Consecutive Ones
Date: 03-10-2025
Difficulty: Easy
Time taken: ~1 minute
Link: https://leetcode.com/problems/max-consecutive-ones
"""

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        curr = 0
        for i in nums:
            if i == 0:
                res = max(curr, res)
                curr = 0
            curr += i
        return max(curr, res)

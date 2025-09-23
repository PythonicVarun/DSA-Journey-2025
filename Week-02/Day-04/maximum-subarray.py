"""
Problem: Maximum Subarray
Date: 18-09-2025
Difficulty: Medium
Time taken: ~1 minute
Link: https://leetcode.com/problems/maximum-subarray/
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        currSum = nums[0]
        for i in nums[1:]:
            currSum = max(i + currSum, i)
            res = max(res, currSum)
        return res

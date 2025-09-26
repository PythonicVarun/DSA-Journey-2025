"""
Problem: Valid Triangle Number
Date: 26-09-2025
Difficulty: Medium
Time taken: ~5 minutes
Link: https://leetcode.com/problems/valid-triangle-number
"""

from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums) - 1, 1, -1):
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    res += r - l
                    r -= 1
                else:
                    l += 1
        return res

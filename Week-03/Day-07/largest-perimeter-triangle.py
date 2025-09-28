"""
Problem: Largest Perimeter Triangle
Date: 28-09-2025
Difficulty: Medium
Time taken: ~5 minutes
Link: https://leetcode.com/problems/largest-perimeter-triangle
"""

from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i + 1] + nums[i + 2] > nums[i]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0

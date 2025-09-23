"""
Problem: Sort Colors
Date: 16-09-2025
Difficulty: Easy
Time taken: ~1 minute
Link: https://leetcode.com/problems/sort-colors/
"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort()  # Simple approach but not optimal

        zeros, ones, n = 0, 0, len(nums)
        for i in nums:
            if i == 1:
                ones += 1
            elif i == 0:
                zeros += 1

        for i in range(0, zeros):
            nums[i] = 0

        for i in range(zeros, zeros + ones):
            nums[i] = 1

        for i in range(zeros + ones, n):
            nums[i] = 2

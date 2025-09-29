"""
Problem: Move Zeroes
Date: 28-09-2025
Difficulty: Easy
Time taken: ~1 minute
Link: https://leetcode.com/problems/move-zeroes
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=lambda x: x == 0)

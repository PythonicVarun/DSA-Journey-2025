"""
Problem: Smallest Absent Positive Greater Than Average
Date: 09-10-2025
Difficulty: Easy
Time taken: ~1 minute
Link: https://leetcode.com/problems/smallest-absent-positive-greater-than-average
"""

from typing import List


class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg = max(1, sum(nums) // len(nums) + 1)
        while avg in set(nums):
            avg += 1
        return avg

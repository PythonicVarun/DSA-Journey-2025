"""
Problem: Check if Array Is Sorted and Rotated
Date: 20-09-2024
Difficulty: Medium
Time taken: ~1 minute
Link: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
"""

from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        return sum(nums[i - 1] > v for i, v in enumerate(nums)) <= 1

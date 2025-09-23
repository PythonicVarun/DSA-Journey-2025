"""
Problem: Majority Element
Date: 17-09-2025
Difficulty: Easy
Time taken: ~30 seconds
Link: https://leetcode.com/problems/majority-element/
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]

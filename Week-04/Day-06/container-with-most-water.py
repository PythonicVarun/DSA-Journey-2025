"""
Problem: Container With Most Water
Date: 04-10-2025
Difficulty: Medium
Time taken: ~15 minutes
Link: https://leetcode.com/problems/container-with-most-water
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        i, j = 0, len(height) - 1
        while i < j:
            curr = min(height[i], height[j]) * (j - i)
            res = max(res, curr)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res

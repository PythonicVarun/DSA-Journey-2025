"""
Problem: Jump Game
Date: 22-09-2025
Difficulty: Medium
Time taken: ~1 minute
Link: https://leetcode.com/problems/jump-game/
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return goal == 0

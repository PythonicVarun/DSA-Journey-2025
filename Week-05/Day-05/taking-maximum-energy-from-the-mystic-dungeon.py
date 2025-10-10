"""
Problem: Taking Maximum Energy From the Mystic Dungeon
Date: 10-10-2025
Difficulty: Medium
Time taken: ~15 minutes
Link: https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon
"""

from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = energy
        for i in range(len(energy) - k - 1, -1, -1):
            dp[i] += dp[i + k]
        return max(dp)

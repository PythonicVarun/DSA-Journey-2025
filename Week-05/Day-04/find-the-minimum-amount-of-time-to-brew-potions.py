"""
Problem: Find the Minimum Amount of Time to Brew Potions
Date: 09-10-2025
Difficulty: Medium
Time taken: ~15 minutes
Link: https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions
"""

from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        time = [0] * n
        for x in mana:
            time[0] = time[0] + skill[0] * x
            for i in range(1, n):
                time[i] = max(time[i], time[i - 1]) + skill[i] * x
            for i in range(n - 2, -1, -1):
                time[i] = time[i + 1] - skill[i + 1] * x
        return time[-1]

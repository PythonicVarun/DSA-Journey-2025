"""
Problem: Water Bottles
Date: 01-10-2025
Difficulty: Easy
Time taken: ~30 seconds
Link: https://leetcode.com/problems/water-bottles
"""


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return int(numBottles + (numBottles - 1) / (numExchange - 1))

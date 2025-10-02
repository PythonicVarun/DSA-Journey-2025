"""
Problem: Water Bottles II
Date: 02-10-2025
Difficulty: Medium
Time taken: ~10 minutes
Link: https://leetcode.com/problems/water-bottles-ii
"""


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = 0
        empty = 0
        while numBottles > 0:
            while numBottles > 0 and empty < numExchange:
                res += 1
                empty += 1
                numBottles -= 1

            if empty == numExchange:
                numExchange += 1
                empty = 0
                numBottles += 1
        return res

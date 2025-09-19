"""
Problem: Best Time to Buy and Sell Stock
Date: 19-09-2024
Difficulty: Easy
Time taken: ~1 minute
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curr = prices[0]
        for i in prices:
            curr = min(i, curr)
            res = max(i - curr, res)
        return res

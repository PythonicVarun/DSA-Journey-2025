"""
Problem: Minimum Adjacent Swaps to Alternate Parity
Date: 10-10-2025
Difficulty: Medium
Time taken: ~1 hour
Link: https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity
"""

from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        evens = []
        odds = []
        for i, num in enumerate(nums):
            if num % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)

        N_e = len(evens)
        N_o = len(odds)
        if abs(N_e - N_o) > 1:
            return -1

        def calculate_swaps(indices, idx):
            swaps = 0
            target_index = idx
            for i in indices:
                swaps += abs(i - target_index)
                target_index += 2
            return swaps

        res = float("inf")
        if N_e >= N_o:
            res = min(res, calculate_swaps(evens, 0))

        if N_o >= N_e:
            res = min(res, calculate_swaps(odds, 0))

        return res

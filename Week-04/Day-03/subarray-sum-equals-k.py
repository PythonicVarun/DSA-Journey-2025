"""
Problem: Subarray Sum Equals K
Date: 01-10-2025
Difficulty: Medium
Time taken: ~2 minutes
Link: https://leetcode.com/problems/subarray-sum-equals-k
"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curr = 0
        d = {0: 1}
        for i in nums:
            curr = curr + i
            if curr - k in d:
                res = res + d[curr - k]

            d[curr] = (d[curr] + 1) if curr in d else 1
        return res

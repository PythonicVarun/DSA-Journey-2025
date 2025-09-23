"""
Problem: Rearrange Array Elements by Sign
Date: 20-09-2025
Difficulty: Medium
Time taken: ~1 minute
Link: https://leetcode.com/problems/rearrange-array-elements-by-sign/
"""

from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos, neg = [], []
        for i in nums:
            if i >= 0:
                pos.append(i)
            else:
                neg.append(i)

        res = []
        for i in range(n // 2):
            res.append(pos[i])
            res.append(neg[i])
        return res

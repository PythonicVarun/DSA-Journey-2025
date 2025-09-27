"""
Problem: Longest Consecutive Sequence
Date: 27-09-2025
Difficulty: Medium
Time taken: ~5 minutes
Link: https://leetcode.com/problems/longest-consecutive-sequence/
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        uniq = set(nums)
        for i in uniq:
            if i - 1 not in uniq:
                length = 1
                while i + length in uniq:
                    length += 1
                res = max(res, length)
        return res

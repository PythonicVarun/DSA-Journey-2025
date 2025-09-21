"""
Problem: Partition Array According to Given Pivot
Date: 21-09-2024
Difficulty: Medium
Time taken: ~1 minute
Link: https://leetcode.com/problems/partition-array-according-to-given-pivot/
"""

from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l, h, eq = [], [], 0
        for i in nums:
            if i < pivot:
                l.append(i)
            elif i == pivot:
                eq += 1
            else:
                h.append(i)
        return l + [pivot] * eq + h

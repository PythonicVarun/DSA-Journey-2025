"""
Problem: Merge Intervals
Date: 09-10-2025
Difficulty: Medium
Time taken: ~1 minute
Link: https://leetcode.com/problems/merge-intervals
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        merged = []
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= prev[1]:
                prev[1] = max(prev[1], intervals[i][1])
            else:
                merged.append(prev)
                prev = intervals[i]

        merged.append(prev)
        return merged

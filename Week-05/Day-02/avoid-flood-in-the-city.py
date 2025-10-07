"""
Problem: Avoid Flood in The City
Date: 07-10-2025
Difficulty: Medium
Time taken: ~1 hour
Link: https://leetcode.com/problems/avoid-flood-in-the-city
"""

from bisect import bisect_right
from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        dry = []
        last = {}
        res = [1] * n
        for i, j in enumerate(rains):
            if j == 0:
                dry.append(i)
            else:
                res[i] = -1
                if j in last:
                    idx = bisect_right(dry, last[j])
                    if idx == len(dry):
                        return []
                    res[dry[idx]] = j
                    dry.pop(idx)
                last[j] = i
        return res

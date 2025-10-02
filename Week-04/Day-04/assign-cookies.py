"""
Problem: Assign Cookies
Date: 02-10-2025
Difficulty: Easy
Time taken: ~15 minutes
Link: https://leetcode.com/problems/assign-cookies
"""

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j, res = 0, 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                res += 1
                i += 1
            j += 1
        return res

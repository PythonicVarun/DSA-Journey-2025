"""
Problem: Compare Version Numbers
Date: 23-09-2025
Difficulty: Medium
Time taken: ~2 minutes
Link: https://leetcode.com/problems/compare-version-numbers/
"""

from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        conv = lambda x: list(map(int, x.split(".")))
        version1, version2 = conv(version1), conv(version2)
        for i, j in zip_longest(version1, version2, fillvalue=0):
            if i == j:
                continue
            return -1 if i < j else 1
        return 0

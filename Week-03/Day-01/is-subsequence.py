"""
Problem: Is Subsequence
Date: 22-09-2025
Difficulty: Easy
Time taken: ~1 minute
Link: https://leetcode.com/problems/is-subsequence/
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

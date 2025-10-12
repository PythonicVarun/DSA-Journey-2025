"""
Problem: Longest Balanced Substring I
Date: 12-10-2025
Difficulty: Medium
Time taken: ~15 minutes
Link: https://leetcode.com/problems/longest-balanced-substring-i
"""


class Solution:
    def longestBalanced(self, s: str) -> int:
        n, res = len(s), 0
        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                freq[ord(s[j]) - ord("a")] += 1
                non_zero = [f for f in freq if f > 0]
                if non_zero:
                    if min(non_zero) == max(non_zero):
                        res = max(res, j - i + 1)
        return res

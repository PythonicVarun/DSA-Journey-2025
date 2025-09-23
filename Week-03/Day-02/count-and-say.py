"""
Problem: Count and Say
Date: 23-09-2025
Difficulty: Medium
Time taken: ~10 minutes
Link: https://leetcode.com/problems/count-and-say/
"""

from functools import cache


class Solution:
    @cache
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        s = self.countAndSay(n - 1)
        arr = (
            [-1] + [i - 1 for i in range(1, len(s)) if s[i - 1] != s[i]] + [len(s) - 1]
        )
        return "".join(str(arr[i] - arr[i - 1]) + s[arr[i]] for i in range(1, len(arr)))

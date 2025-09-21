"""
Problem: Check if All A's Appears Before All B's
Date: 21-09-2024
Difficulty: Easy
Time taken: ~30 seconds
Link: https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/
"""


class Solution:
    def checkString(self, s: str) -> bool:
        # return "ba" not in s # Simple and efficient solution

        # Manual check
        for i in range(1, len(s)):
            if s[i - 1] > s[i]:
                return False
        return True

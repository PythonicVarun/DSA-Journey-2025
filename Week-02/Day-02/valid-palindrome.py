"""
Problem: Valid Palindrome
Date: 16-09-2024
Difficulty: Easy
Time taken: ~1 minute
Link: https://leetcode.com/problems/valid-palindrome/
"""

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        return s == s[::-1]

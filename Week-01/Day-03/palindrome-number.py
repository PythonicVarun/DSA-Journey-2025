"""
Problem: Palindrome Number
Date: 10-09-2025
Difficulty: Easy
Time taken: ~30 seconds
Link: https://leetcode.com/problems/palindrome-number/
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

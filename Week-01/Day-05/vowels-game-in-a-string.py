"""
Problem: Vowels Game in a String
Date: 12-09-2024
Difficulty: Medium
Time taken: ~15 minutes
Link: https://leetcode.com/problems/vowels-game-in-a-string/
"""


class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return sum(1 for c in s if c in "aeiou") > 0

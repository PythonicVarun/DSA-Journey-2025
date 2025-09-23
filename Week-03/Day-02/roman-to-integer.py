"""
Problem: Roman to Integer
Date: 23-09-2025
Difficulty: Easy
Time taken: ~5 minutes
Link: https://leetcode.com/problems/roman-to-integer/
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        romanMap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and romanMap[s[i]] < romanMap[s[i + 1]]:
                res -= romanMap[s[i]]
            else:
                res += romanMap[s[i]]
        return res

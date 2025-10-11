"""
Problem: Reverse Degree of a String
Date: 11-10-2025
Difficulty: Easy
Time taken: ~1 minute
Link: https://leetcode.com/problems/reverse-degree-of-a-string
"""

from string import ascii_lowercase


class Solution:
    def reverseDegree(self, s: str) -> int:
        deg = 0
        idx = {j: 26 - i for i, j in enumerate(ascii_lowercase)}
        for i, j in enumerate(s, start=1):
            deg += i * idx[j]
        return deg

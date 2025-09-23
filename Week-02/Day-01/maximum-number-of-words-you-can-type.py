"""
Problem: Maximum Number of Words You Can Type
Date: 15-09-2025
Difficulty: Easy
Time taken: ~1 minute
Link: https://leetcode.com/problems/maximum-number-of-words-you-can-type/
"""


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        return sum(1 for w in text.split() if not any([c in brokenLetters for c in w]))

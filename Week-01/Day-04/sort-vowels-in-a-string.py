"""
Problem: Sort Vowels in a String
Date: 11-09-2025
Difficulty: Medium
Time taken: ~3 minutes
Link: https://leetcode.com/problems/sort-vowels-in-a-string/
"""


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiou"
        vow = [c for c in s if c.lower() in vowels]
        vow = iter(sorted(vow))

        res = list(s)
        for i in range(len(s)):
            if s[i].lower() in vowels:
                res[i] = next(vow)
        return "".join(res)

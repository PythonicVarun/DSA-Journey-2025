"""
Problem: Find Most Frequent Vowel and Consonant
Date: 13-09-2024
Difficulty: Easy
Time taken: ~1 minute
Link: https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/
"""

from collections import defaultdict


class Solution:
    def maxFreqSum(self, s: str) -> int:
        counter = defaultdict(int)

        vowels = "aeiou"
        maxVow, maxCons = 0, 0
        for i in s:
            counter[i] += 1
            if i in vowels:
                maxVow = max(maxVow, counter[i])
            else:
                maxCons = max(maxCons, counter[i])
        return maxVow + maxCons

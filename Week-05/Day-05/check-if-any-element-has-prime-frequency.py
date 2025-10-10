"""
Problem: Check if Any Element Has Prime Frequency
Date: 10-10-2025
Difficulty: Easy
Time taken: ~1 minute
Link: https://leetcode.com/problems/check-if-any-element-has-prime-frequency
"""

from collections import Counter
from functools import cache
from math import sqrt
from typing import List


class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        @cache
        def isPrime(n):
            if n == 1 or (n % 2 == 0 and n != 2):
                return False
            if n == 2:
                return True
            for div in range(3, int(sqrt(n)) + 1, 2):
                if n % div == 0:
                    return False
            return True

        counts = Counter(nums)
        for count in counts.keys():
            if isPrime(counts[count]):
                return True
        return False

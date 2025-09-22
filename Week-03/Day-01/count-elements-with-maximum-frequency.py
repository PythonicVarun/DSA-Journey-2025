"""
Problem: Count Elements With Maximum Frequency
Date: 22-09-2024
Difficulty: Easy
Time taken: ~2 minutes
Link: https://leetcode.com/problems/count-elements-with-maximum-frequency/
"""

from collections import defaultdict
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        maxF, res = 0, 0
        cntr = defaultdict(int)
        for i in nums:
            cntr[i] += 1
            if cntr[i] > maxF:
                res = cntr[i]
                maxF = cntr[i]
            elif cntr[i] == maxF:
                res += cntr[i]
        return res

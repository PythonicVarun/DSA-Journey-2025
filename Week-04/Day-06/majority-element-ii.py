"""
Problem: Majority Element II
Date: 04-10-2025
Difficulty: Medium
Time taken: ~1 minute
Link: https://leetcode.com/problems/majority-element-ii
"""

from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = set()
        n = int(len(nums) / 3)
        cntr = defaultdict(int)
        for i in nums:
            cntr[i] += 1
            if cntr[i] > n:
                res.add(i)
        return list(res)

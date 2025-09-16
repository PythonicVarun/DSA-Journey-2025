"""
Problem: Replace Non-Coprime Numbers in Array
Date: 16-09-2024
Difficulty: Hard
Time taken: ~30 minutes
Link: https://leetcode.com/problems/replace-non-coprime-numbers-in-array/
"""

from math import gcd
from typing import List


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for i in nums:
            while stack:
                g = gcd(stack[-1], i)
                if g == 1:
                    break
                i = (stack.pop() * i) // g
            stack.append(i)
        return stack

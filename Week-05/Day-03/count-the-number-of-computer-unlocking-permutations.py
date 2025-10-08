"""
Problem: Count the Number of Computer Unlocking Permutations
Date: 08-10-2025
Difficulty: Medium
Time taken: ~2 minutes
Link: https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations
"""

from math import factorial
from typing import List


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        if complexity[0] > min(complexity) or complexity.count(complexity[0]) > 1:
            return 0
        return factorial(len(complexity) - 1) % (10**9 + 7)

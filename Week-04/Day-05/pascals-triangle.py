"""
Problem: Pascal's Triangle
Date: 03-10-2025
Difficulty: Easy
Time taken: ~1 minute
Link: https://leetcode.com/problems/pascals-triangle
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            res += [list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1]))]
        return res[:numRows]

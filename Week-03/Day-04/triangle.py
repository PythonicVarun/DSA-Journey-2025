"""
Problem: Triangle
Date: 25-09-2025
Difficulty: Medium
Time taken: ~5 minutes
Link: https://leetcode.com/problems/triangle/
"""

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]

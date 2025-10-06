"""
Problem: Swim in Rising Water
Date: 06-10-2025
Difficulty: Hard
Time taken: ~3 hours
Link: https://leetcode.com/problems/swim-in-rising-water
"""

import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        min_heap = [(grid[0][0], 0, 0)]
        while min_heap:
            curr, r, c = heapq.heappop(min_heap)
            if visited[r][c]:
                continue

            visited[r][c] = True
            res = max(res, curr)
            if r == n - 1 and c == n - 1:
                return res

            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + i, c + j
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    heapq.heappush(min_heap, (grid[nr][nc], nr, nc))
        return res

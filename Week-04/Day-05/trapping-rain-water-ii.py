"""
Problem: Trapping Rain Water II
Date: 03-10-2025
Difficulty: Hard
Time taken: ~1 hour
Link: https://leetcode.com/problems/trapping-rain-water-ii
"""

from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        dir = (0, 1, 0, -1, 0)
        m, n = len(heightMap), len(heightMap[0])
        if m <= 2 or n <= 2:
            return 0

        boundary = []
        for i in range(m):
            boundary.append((heightMap[i][0], i, 0))
            boundary.append((heightMap[i][-1], i, n - 1))
            heightMap[i][0] = heightMap[i][-1] = -1

        for j in range(n):
            boundary.append((heightMap[0][j], 0, j))
            boundary.append((heightMap[-1][j], m - 1, j))
            heightMap[0][j] = heightMap[-1][j] = -1

        heapify(boundary)
        ans, water_level = 0, 0
        while boundary:
            h, i, j = heappop(boundary)
            water_level = max(water_level, h)
            for a in range(4):
                i0, j0 = i + dir[a], j + dir[a + 1]
                if i0 < 0 or i0 >= m or j0 < 0 or j0 >= n or heightMap[i0][j0] == -1:
                    continue

                currH = heightMap[i0][j0]
                if currH < water_level:
                    ans += water_level - currH
                heightMap[i0][j0] = -1
                heappush(boundary, (currH, i0, j0))
        return ans

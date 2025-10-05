"""
Problem: Pacific Atlantic Water Flow
Date: 05-10-2025
Difficulty: Medium
Time taken: ~2 hours
Link: https://leetcode.com/problems/pacific-atlantic-water-flow
"""

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        ans = [[[False, False] for _ in range(m)] for _ in range(n)]
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y, ocean):
            if (ocean == "p" and ans[x][y][0]) or (ocean != "p" and ans[x][y][1]):
                return
            if ocean == "p":
                ans[x][y][0] = True
            else:
                ans[x][y][1] = True

            for dx, dy in dir:
                cx, cy = x + dx, y + dy
                if 0 <= cx < n and 0 <= cy < m and heights[cx][cy] >= heights[x][y]:
                    dfs(cx, cy, ocean)

        for i in range(m):
            dfs(0, i, "p")
        for i in range(n):
            dfs(i, 0, "p")
        for i in range(m):
            dfs(n - 1, i, "heights")
        for i in range(n):
            dfs(i, m - 1, "heights")

        res = []
        for i in range(n):
            for j in range(m):
                if ans[i][j][0] and ans[i][j][1]:
                    res.append([i, j])
        return res

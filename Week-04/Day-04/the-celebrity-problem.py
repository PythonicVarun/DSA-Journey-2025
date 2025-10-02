"""
Problem: The Celebrity Problem
Date: 02-10-2025
Difficulty: Medium
Time taken: ~10 minutes
Link: https://geeksforgeeks.org/problems/the-celebrity-problem/1
"""


class Solution:
    def celebrity(self, mat):
        # code here
        n = len(mat)
        outdegree = [0] * n
        indegree = [0] * n
        for i in range(n):
            for j in range(n):
                if mat[i][j] and i != j:
                    outdegree[i] += 1
                    indegree[j] += 1

        for i in range(n):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i
        return -1

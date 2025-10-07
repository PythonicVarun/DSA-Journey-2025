"""
Problem: Next Smaller Element
Date: 07-10-2025
Difficulty: Medium
Time taken: ~15 minutes
Link: https://geeksforgeeks.org/problems/immediate-smaller-element1142/1
"""


class Solution:
    def nextSmallerEle(self, arr):
        # code here
        stack = []
        res = [-1] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            while stack and arr[i] <= stack[-1]:
                stack.pop()

            if stack:
                res[i] = stack[-1]

            stack.append(arr[i])
        return res

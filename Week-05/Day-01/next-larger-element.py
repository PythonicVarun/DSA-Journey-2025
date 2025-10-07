"""
Problem: Next Greater Element
Date: 06-10-2025
Difficulty: Medium
Time taken: ~10 minutes
Link: https://geeksforgeeks.org/problems/next-larger-element-1587115620/1
"""


class Solution:
    def nextLargerElement(self, arr):
        # code here
        stack = [-1]
        stack.append(arr[-1])
        arr[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            while arr[i] >= stack[-1] and stack[-1] != -1:
                stack.pop()

            temp = arr[i]
            arr[i] = stack[-1]
            stack.append(temp)
        return arr

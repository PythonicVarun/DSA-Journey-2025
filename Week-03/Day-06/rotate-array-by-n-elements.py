"""
Problem: Rotate Array
Date: 27-09-2025
Difficulty: Medium
Time taken: ~2 minutes
Link: https://geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1
"""


class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction.
    def rotateArr(self, arr, d):
        # Your code here
        d = d % len(arr)
        arr[:] = arr[d:] + arr[:d]
        return arr

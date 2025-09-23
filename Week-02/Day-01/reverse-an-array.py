"""
Problem: Reverse an Array
Date: 15-09-2025
Difficulty: Easy
Time taken: ~30 seconds
Link: https://geeksforgeeks.org/problems/reverse-an-array/1
"""


class Solution:
    def reverseArray(self, arr):
        # code here
        arr[::] = arr[::-1]

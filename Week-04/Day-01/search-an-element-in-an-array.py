"""
Problem: Array Search
Date: 29-09-2025
Difficulty: Easy
Time taken: ~30 seconds
Link: https://geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/1
"""


class Solution:
    def search(self, arr, x):
        # code here
        return arr.index(x) if x in arr else -1

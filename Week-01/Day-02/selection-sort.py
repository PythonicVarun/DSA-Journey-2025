"""
Problem: Selection Sort
Date: 09-09-2024
Difficulty: Easy
Time taken: ~1 minute
Link: https://geeksforgeeks.org/problems/selection-sort/1
"""


class Solution:
    def selectionSort(self, arr):
        # code here
        n = len(arr)
        for i in range(n):
            idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[idx]:
                    idx = j
            arr[i], arr[idx] = arr[idx], arr[i]

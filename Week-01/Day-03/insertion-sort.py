"""
Problem: Insertion Sort
Date: 10-09-2024
Difficulty: Easy
Time taken: ~2 minutes
Link: https://geeksforgeeks.org/problems/insertion-sort/1
"""


class Solution:
    def insertionSort(self, arr):
        # code here
        n = len(arr)
        for i in range(1, n):
            k = arr[i]
            j = i - 1
            while j >= 0 and k < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = k

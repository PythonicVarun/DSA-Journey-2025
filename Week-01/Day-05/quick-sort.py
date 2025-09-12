"""
Problem: Quick Sort
Date: 12-09-2024
Difficulty: Easy
Time taken: ~2 minutes
Link: https://geeksforgeeks.org/problems/quick-sort/1
"""


class Solution:
    def quickSort(self, arr, low, high):
        # code here
        if low < high:
            pivot = self.partition(arr, low, high)
            self.quickSort(arr, low, pivot - 1)
            self.quickSort(arr, pivot + 1, high)

    def partition(self, arr, low, high):
        # code here
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

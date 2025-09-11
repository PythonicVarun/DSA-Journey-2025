"""
Problem: Bubble Sort
Date: 08-09-2024
Difficulty: Easy
Time taken: ~1 minute
Link: https://geeksforgeeks.org/problems/bubble-sort/1
"""


class Solution:
    def bubbleSort(self, arr):
        # code here
        n = len(arr)
        for i in range(n - 1):
            flag = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    flag = True
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            if not flag:
                break

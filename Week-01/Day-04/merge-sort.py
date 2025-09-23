"""
Problem: Merge Sort
Date: 11-09-2025
Difficulty: Easy
Time taken: ~7 minutes
Link: https://geeksforgeeks.org/problems/merge-sort/1
"""


class Solution:
    def _merge(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        L = [0] * n1
        R = [0] * n2

        for i in range(n1):
            L[i] = arr[l + i]
        for j in range(n2):
            R[j] = arr[m + 1 + j]

        k = l
        i = j = 0
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def mergeSort(self, arr, l, r):
        # code here
        if l < r:
            m = l + (r - l) // 2

            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)
            self._merge(arr, l, m, r)

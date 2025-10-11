"""
Problem: Missing And Repeating
Date: 11-10-2025
Difficulty: Easy
Time taken: ~1 minute
Link: https://geeksforgeeks.org/problems/find-missing-and-repeating2512/1
"""


class Solution:
    def findTwoElement(self, arr):
        # code here
        n = len(arr)
        s1 = set(arr)
        s2 = set(range(1, n + 1))
        missing = list(s2 - s1)[0]

        expected_sum = n * (n + 1) // 2
        actual_sum = sum(arr)
        duplicate = actual_sum - expected_sum + missing

        return [duplicate, missing]

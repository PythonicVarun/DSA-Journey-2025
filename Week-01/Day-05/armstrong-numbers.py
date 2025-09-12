"""
Problem: Armstrong Numbers
Date: 12-09-2024
Difficulty: Easy
Time taken: ~30 seconds
Link: https://geeksforgeeks.org/problems/armstrong-numbers2727/1
"""


class Solution:
    def armstrongNumber(self, n):
        # code here
        return n == sum(int(d) ** 3 for d in str(n))

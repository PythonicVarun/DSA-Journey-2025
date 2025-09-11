"""
Problem: Count Digits
Date: 08-09-2024
Difficulty: Easy
Time taken: ~30 seconds
Link: https://geeksforgeeks.org/problems/count-digits-1606889545/1
"""

import math


class Solution:
    def countDigits(self, n):
        # code here
        return int(math.log(n, 10)) + 1

"""
Problem: GCD of two numbers
Date: 11-09-2024
Difficulty: Easy
Time taken: ~30 seconds
Link: https://geeksforgeeks.org/problems/gcd-of-two-numbers3459/1
"""


class Solution:
    def gcd(self, a, b):
        # code here
        if b == 0:
            return a
        return self.gcd(b, a % b)

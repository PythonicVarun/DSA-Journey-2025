"""
Problem: Fibonacci Number
Date: 17-09-2025
Difficulty: Easy
Time taken: ~30 seconds
Link: https://leetcode.com/problems/fibonacci-number/
"""


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

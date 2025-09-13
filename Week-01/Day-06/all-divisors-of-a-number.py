"""
Problem: All divisors of a Number
Date: 13-09-2024
Difficulty: Easy
Time taken: ~5 minutes
Link: https://geeksforgeeks.org/problems/all-divisors-of-a-number/1
"""


class Solution:
    def print_divisors(self, N):
        # code here
        divisors = set()
        for i in range(1, int(N**0.5) + 1):
            if N % i == 0:
                divisors.add(i)
                divisors.add(N // i)

        # print(*sorted(divisors)) # doesn't work on GFG :(
        for d in sorted(divisors):
            print(d, end=" ")

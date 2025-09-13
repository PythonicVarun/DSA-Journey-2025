"""
Problem: Sieve of Eratosthenes
Date: 13-09-2024
Difficulty: Medium
Time taken: ~2 minutes
Link: https://geeksforgeeks.org/problems/sieve-of-eratosthenes5242/1
"""


class Solution:
    def sieve(self, n):
        # code here
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        if n > 4:
            for i in range(4, n + 1, 2):
                primes[i] = False

        for i in range(3, int(n**0.5) + 1, 2):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False

        return [i for i in range(n + 1) if primes[i]]

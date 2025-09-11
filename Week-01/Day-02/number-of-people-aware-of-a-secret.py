"""
Problem: Number of People Aware of a Secret
Date: 09-09-2024
Difficulty: Medium
Time taken: ~3 minutes
Link: https://leetcode.com/problems/number-of-people-aware-of-a-secret/
"""


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        aware, spread, res = [0] * n, 0, 1
        aware[0] = 1
        for i in range(1, n):
            if i >= delay:
                spread += aware[i - delay]
            if i >= forget:
                forgot = aware[i - forget]
                res -= forgot
                spread -= forgot

            aware[i] = spread
            res += spread
        return res % int(1e9 + 7)

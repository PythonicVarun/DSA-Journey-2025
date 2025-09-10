"""
Problem: Minimum Number of People to Teach
Date: 10-09-2024
Difficulty: Medium
Time taken: ~10 minutes
Link: https://leetcode.com/problems/minimum-number-of-people-to-teach/
"""

from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        teach = set()
        for u, v in friendships:
            u -= 1
            v -= 1
            flag = False
            for l in languages[u]:
                if l in languages[v]:
                    flag = True
                    break

            if not flag:
                teach |= {u, v}

        res = len(languages) - 1
        for l in range(1, n+1):
            cnt = 0
            for u in teach:
                if l not in languages[u]:
                    cnt += 1
            res = min(res, cnt)
        return res

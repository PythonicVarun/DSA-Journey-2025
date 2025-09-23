"""
Problem: Second Largest
Date: 19-09-2025
Difficulty: Easy
Time taken: ~1 minute
Link: https://geeksforgeeks.org/problems/second-largest3735/1
"""

import heapq


class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        uniq = [-i for i in set(arr)]
        if len(uniq) < 2:
            return -1

        heapq.heapify(uniq)
        heapq.heappop(uniq)
        return -uniq[0]

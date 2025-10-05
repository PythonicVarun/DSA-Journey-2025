"""
Problem: Binary Search
Date: 05-10-2025
Difficulty: Easy
Time taken: ~30 seconds
Link: https://leetcode.com/problems/binary-search
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                h = mid - 1
            else:
                l = mid + 1
        return -1

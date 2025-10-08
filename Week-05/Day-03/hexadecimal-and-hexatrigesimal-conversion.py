"""
Problem: Hexadecimal and Hexatrigesimal Conversion
Date: 08-10-2025
Difficulty: Easy
Time taken: ~2 minutes
Link: https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion
"""


class Solution:
    def concatHex36(self, n: int) -> str:
        nums = {i: f"{i}" for i in range(10)}
        for i in range(10, 36):
            nums[i] = chr(65 + i - 10)

        n2 = n * n
        n3 = n2 * n

        s1 = ""
        while n2:
            s1 = nums[n2 % 16] + s1
            n2 //= 16

        s2 = ""
        while n3:
            s2 = nums[n3 % 36] + s2
            n3 //= 36
        return s1 + s2

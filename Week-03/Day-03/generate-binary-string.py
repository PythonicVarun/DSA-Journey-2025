"""
Problem: Generate binary string
Date: 24-09-2025
Difficulty: Easy
Time taken: ~10 minutes
Link: https://www.geeksforgeeks.org/problems/generate-binary-string3642/1
"""


class Solution:
    def generate_binary_string(self, s):
        # Code here
        res = []

        def generate(idx, curr):
            if idx == len(s):
                res.append(curr)
                return

            if s[idx] == "?":
                generate(idx + 1, curr + "0")
                generate(idx + 1, curr + "1")
            else:
                generate(idx + 1, curr + s[idx])

        generate(0, "")
        return res

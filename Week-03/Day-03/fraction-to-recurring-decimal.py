"""
Problem: Fraction to Recurring Decimal
Date: 24-09-2025
Difficulty: Medium
Time taken: ~15 minutes
Link: https://leetcode.com/problems/fraction-to-recurring-decimal/
"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)

        sign = "-" if numerator * denominator < 0 else ""
        num, den = abs(numerator), abs(denominator)

        res = sign + str(num // den) + "."
        num %= den
        seen = {}
        while num:
            if num in seen:
                i = seen[num]
                return res[:i] + "(" + res[i:] + ")"
            seen[num] = len(res)
            num *= 10
            res += str(num // den)
            num %= den
        return res

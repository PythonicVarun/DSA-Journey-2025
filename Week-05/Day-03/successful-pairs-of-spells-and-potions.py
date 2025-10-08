"""
Problem: Successful Pairs of Spells and Potions
Date: 08-10-2025
Difficulty: Medium
Time taken: ~5 minutes
Link: https://leetcode.com/problems/successful-pairs-of-spells-and-potions
"""

import bisect
import math
from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        potion_count = len(potions)
        res = []
        for spell_power in spells:
            required_strength = math.ceil(success / spell_power)
            if required_strength > potions[-1]:
                res.append(0)
                continue
            index = bisect.bisect_left(potions, required_strength)
            res.append(potion_count - index)
        return res

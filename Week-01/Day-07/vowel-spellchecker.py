"""
Problem: Vowel Spellchecker
Date: 14-09-2025
Difficulty: Medium
Time taken: ~5 minutes
Link: https://leetcode.com/problems/vowel-spellchecker/
"""

import re
from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        res = []
        mask = lambda s: re.sub(r"[aeiou]", "a", s.lower())

        lst = set(wordlist)
        lowerlst = {}
        maskedlst = {}
        for w in wordlist[::-1]:
            lowerlst[w.lower()] = w
            maskedlst[mask(w)] = w

        for q in queries:
            if q in lst:
                res.append(q)
                continue

            if q.lower() in lowerlst:
                res.append(lowerlst[q.lower()])
                continue

            res.append(maskedlst.get(mask(q), ""))
        return res

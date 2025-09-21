"""
Problem: Design Movie Rental System
Date: 21-09-2024
Difficulty: Hard
Time taken: ~10 minutes
Link: https://leetcode.com/problems/design-movie-rental-system/
"""

from collections import defaultdict
from typing import List

from sortedcontainers import SortedSet


class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.price = {}
        self.rented = SortedSet()
        self.available = defaultdict(SortedSet)
        for s, m, p in entries:
            self.available[m].add((p, s))
            self.price[(m, s)] = p

    def search(self, movie: int) -> List[int]:
        return [s for _, s in self.available[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.price[(movie, shop)]
        self.rented.add((price, shop, movie))
        self.available[movie].discard((price, shop))

    def drop(self, shop: int, movie: int) -> None:
        price = self.price[(movie, shop)]
        self.rented.discard((price, shop, movie))
        self.available[movie].add((price, shop))

    def report(self) -> List[List[int]]:
        return [[s, m] for _, s, m in self.rented[:5]]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()

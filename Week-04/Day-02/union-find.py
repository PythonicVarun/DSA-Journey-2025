"""
Problem: Union-Find
Date: 30-09-2025
Difficulty: Easy
Time taken: ~15 minutes
Link: https://geeksforgeeks.org/problems/union-find/1
"""


class Solution:
    def find(self, x, par):
        if par[x] == x:
            return x
        return self.find(par[x], par)

    # Function to merge two nodes a and b.
    def union_(self, a, b, par, rank1):
        # code here
        a_rep = self.find(a, par)
        b_rep = self.find(b, par)
        if a_rep == b_rep:
            return
        if rank1[a_rep] > rank1[b_rep]:
            par[b_rep] = a_rep
        elif rank1[b_rep] > rank1[a_rep]:
            par[a_rep] = b_rep
        else:
            par[b_rep] = a_rep
        rank1[a_rep] += 1

    # Function to check whether 2 nodes are connected or not.
    def isConnected(self, x, y, par, rank1):
        # code here
        x_rep = self.find(x, par)
        y_rep = self.find(y, par)
        return x_rep == y_rep
